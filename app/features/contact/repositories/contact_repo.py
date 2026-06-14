from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete, and_
from app.features.contact.models.contact_model import ContactModel
from app.features.contact.interfaces.contact_interface import IContactRepository

class SQLContactRepository(IContactRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_by_user(self, user_id: int, limit: int = 100) -> list:
        stmt = (
            select(ContactModel)
            .where(ContactModel.user_id == user_id)
            .limit(limit)
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def create(self, contact_data: dict) -> ContactModel:
        new_contact = ContactModel(**contact_data)
        self.session.add(new_contact)
        await self.session.commit()
        await self.session.refresh(new_contact)
        return new_contact

    async def update(self, user_id: int, contact_id: int, contact_data: dict) -> bool:
        stmt = (
            update(ContactModel)
            .where(and_(ContactModel.id == contact_id, ContactModel.user_id == user_id))
            .values(**contact_data)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.rowcount > 0

    async def delete(self, user_id: int, contact_id: int) -> bool:
        stmt = delete(ContactModel).where(
            and_(ContactModel.id == contact_id, ContactModel.user_id == user_id)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.rowcount > 0