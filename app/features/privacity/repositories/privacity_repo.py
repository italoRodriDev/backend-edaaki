from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, and_
from app.features.privacity.models.privacity_model import PrivacityModel
from app.features.privacity.interfaces.privacity_interface import IPrivacityRepository

class SQLPrivacityRepository(IPrivacityRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_user(self, user_id: int) -> PrivacityModel | None:
        # Pega a política mais recente que o usuário aceitou/recusou
        stmt = (
            select(PrivacityModel)
            .where(PrivacityModel.user_id == user_id)
            .order_by(PrivacityModel.id.desc())
        )
        result = await self.session.execute(stmt)
        return result.scalars().first()

    async def create(self, privacity_data: dict) -> PrivacityModel:
        new_privacity = PrivacityModel(**privacity_data)
        self.session.add(new_privacity)
        await self.session.commit()
        await self.session.refresh(new_privacity)
        return new_privacity

    async def update(self, user_id: int, privacity_id: int, privacity_data: dict) -> bool:
        stmt = (
            update(PrivacityModel)
            .where(and_(PrivacityModel.id == privacity_id, PrivacityModel.user_id == user_id))
            .values(**privacity_data)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.rowcount > 0