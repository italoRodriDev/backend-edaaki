from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete, and_
from app.features.address.models.address_model import AddressModel
from app.features.address.interfaces.address_interface import IAddressRepository

class SQLAddressRepository(IAddressRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_by_user(self, user_id: int, limit: int = 100) -> list:
        stmt = (
            select(AddressModel)
            .where(AddressModel.user_id == user_id)
            .limit(limit)
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def create(self, address_data: dict) -> AddressModel:
        new_address = AddressModel(**address_data)
        self.session.add(new_address)
        await self.session.commit()
        await self.session.refresh(new_address)
        return new_address

    async def update(self, user_id: int, address_id: int, address_data: dict) -> bool:
        stmt = (
            update(AddressModel)
            .where(and_(AddressModel.id == address_id, AddressModel.user_id == user_id))
            .values(**address_data)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.rowcount > 0

    async def delete(self, user_id: int, address_id: int) -> bool:
        stmt = delete(AddressModel).where(
            and_(AddressModel.id == address_id, AddressModel.user_id == user_id)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.rowcount > 0