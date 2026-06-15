from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update as sql_update, delete as sql_delete
from datetime import datetime, timezone

from app.core.firebase import get_bucket
from app.features.profile.interfaces.profile_interface import IProfileRepository # Ajuste o nome da interface se necessário
from app.features.profile.models.profile_model import ProfileModel

class SQLProfileRepository(IProfileRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
        # Mantemos o bucket do Firebase para lidar com o Firestorage!
        self.bucket = get_bucket()
        
    async def find_by_email(self, email: str) -> dict | None:
        stmt = select(ProfileModel).where(ProfileModel.email == email)
        result = await self.session.execute(stmt)
        user = result.scalars().first()
        
        if user:
            print(f"DEBUG: Usuário encontrado no banco: {user.email}")
            return self._to_dict(user)
        
        print(f"DEBUG: Nenhum usuário encontrado para {email}")
        return None

    async def save_user(self, user_data: dict) -> dict:
        # 1. Garanta que as datas estão no dicionário
        from datetime import datetime
        now = datetime.now()
        user_data['created_at'] = now
        user_data['updated_at'] = now
        
        # 2. O erro acontece porque você está passando um dict para o ProfileModel(**user_data)
        # e o ProfileModel não tem created_at/updated_at nos argumentos de __init__.
        # Vamos remover do objeto que criamos, mas manter para o INSERT:
        
        data_para_modelo = user_data.copy()
        data_para_modelo.pop('created_at', None)
        data_para_modelo.pop('updated_at', None)
        
        new_user = ProfileModel(**data_para_modelo)
        
        # 3. Forçamos o SQLALchemy a incluir as colunas manualmente no objeto:
        new_user.created_at = user_data['created_at']
        new_user.updated_at = user_data['updated_at']
        
        self.session.add(new_user)
        await self.session.commit() # Agora as datas serão incluídas!
        await self.session.refresh(new_user)
        
        return self._to_dict(new_user)

    async def get_user_by_id(self, access_token: int) -> dict | None:
        result = await self.session.execute(
            select(ProfileModel).where(ProfileModel.access_token == access_token)
        )
        user = result.scalars().first()
        
        if user:
            return self._to_dict(user)
        return None

    async def update(self, access_token: int, update_data: dict) -> dict | None:
        update_data['updated_at'] = datetime.now(timezone.utc)
        
        stmt = (
            sql_update(ProfileModel)
            .where(ProfileModel.access_token == access_token)
            .values(**update_data)
        )
        
        await self.session.execute(stmt)
        await self.session.commit()
        
        return await self.get_user_by_id(access_token)

    async def delete(self, user_id: int) -> bool:
        stmt = sql_delete(ProfileModel).where(ProfileModel.id == user_id)
        result = await self.session.execute(stmt)
        await self.session.commit()
        
        return result.rowcount > 0
        
    def _to_dict(self, model) -> dict:
        """Função auxiliar para transformar o modelo SQLAlchemy em Dicionário"""
        return {column.name: getattr(model, column.name) for column in model.__table__.columns}