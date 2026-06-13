from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update as sql_update, delete as sql_delete
from datetime import datetime, timezone

from app.core.firebase import get_bucket
from app.features.profile.interfaces.interfaces import IProfileRepository # Ajuste o nome da interface se necessário
from app.features.profile.models.profile_model import ProfileModel

class SQLUserRepository(IProfileRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
        # Mantemos o bucket do Firebase para lidar com o Firestorage!
        self.bucket = get_bucket()

    async def save_user(self, user_data: dict) -> dict:
        # Define as datas de criação
        user_data['created_at'] = datetime.now(timezone.utc)
        user_data['updated_at'] = datetime.now(timezone.utc)
        
        # O logo já deve vir no user_data (URL gerada pelo Firestorage)
        new_user = ProfileModel(**user_data)
        
        self.session.add(new_user)
        await self.session.commit()
        await self.session.refresh(new_user)
        
        return self._to_dict(new_user)

    async def get_user_by_id(self, user_id: int) -> dict | None:
        result = await self.session.execute(
            select(ProfileModel).where(ProfileModel.id == user_id)
        )
        user = result.scalars().first()
        
        if user:
            return self._to_dict(user)
        return None

    async def update(self, user_id: int, update_data: dict) -> dict | None:
        update_data['updated_at'] = datetime.now(timezone.utc)
        
        stmt = (
            sql_update(ProfileModel)
            .where(ProfileModel.id == user_id)
            .values(**update_data)
        )
        
        await self.session.execute(stmt)
        await self.session.commit()
        
        return await self.get_user_by_id(user_id)

    async def delete(self, user_id: int) -> bool:
        stmt = sql_delete(ProfileModel).where(ProfileModel.id == user_id)
        result = await self.session.execute(stmt)
        await self.session.commit()
        
        return result.rowcount > 0
        
    def _to_dict(self, model) -> dict:
        """Função auxiliar para transformar o modelo SQLAlchemy em Dicionário"""
        return {column.name: getattr(model, column.name) for column in model.__table__.columns}