
from loguru import logger
from app.features.profile.schemas.profile_schemas import UserCreate, UserUpdate 
from app.features.profile.interfaces.profile_interface import IProfileRepository

class ProfileService:
    def __init__(self, repo: IProfileRepository):
        self.repo = repo
        
    async def create_user(self, user_data: UserCreate):
        logger.info(f"Criando novo usuário: {user_data.name}")
        try:
            # model_dump(exclude_unset=True) pega apenas os dados que foram enviados
            data_dict = user_data.model_dump(exclude_unset=True)
            
            # Chama o repositório SQL
            return await self.repo.save_user(data_dict)
        except Exception as e:
            logger.error(f"Erro ao cadastrar usuário: {str(e)}")
            raise
            
    async def get_user(self, user_id: int):
        logger.info(f"Buscando dados do usuário ID: {user_id}")
        user = await self.repo.get_user_by_id(user_id)
        if not user:
            raise ValueError("Usuário não encontrado.")
        return user

    async def update_user(self, user_id: int, user_data: UserUpdate):
        logger.info(f"Atualizando dados do usuário ID: {user_id}")
        try:
            data_dict = user_data.model_dump(exclude_unset=True)
            updated_user = await self.repo.update(user_id, data_dict)
            
            if not updated_user:
                raise ValueError("Usuário não encontrado para atualização.")
                
            logger.success(f"Usuário {user_id} atualizado com sucesso!")
            return updated_user
        except Exception as e:
            logger.error(f"Erro ao atualizar usuário {user_id}: {str(e)}")
            raise
    
    async def delete_user(self, user_id: int):
        logger.info(f"Solicitação de exclusão para usuário ID: {user_id}")
        try:
            success = await self.repo.delete(user_id)
            if not success:
                raise ValueError("Usuário não encontrado para exclusão.")
                
            logger.success(f"Usuário {user_id} removido com sucesso!")
            return {"message": "Usuário deletado com sucesso", "id": user_id}
        except Exception as e:
            logger.error(f"Erro ao deletar usuário {user_id}: {str(e)}")
            raise