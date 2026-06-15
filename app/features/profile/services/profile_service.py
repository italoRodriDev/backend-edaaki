
import firebase_admin
from firebase_admin import auth
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
            
    async def get_user(self, access_token: str):
        logger.info(f"Buscando dados do usuário UUID: {access_token}")
        user = await self.repo.get_user_by_id(access_token)
        if not user:
            raise ValueError("Usuário não encontrado.")
        return user

    async def update_user(self, access_token: str, user_data: UserUpdate):
        logger.info(f"Atualizando dados do usuário ID: {access_token}")
        try:
            data_dict = user_data.model_dump(exclude_unset=True)
            updated_user = await self.repo.update(access_token, data_dict)
            
            if not updated_user:
                raise ValueError("Usuário não encontrado para atualização.")
                
            logger.success(f"Usuário {access_token} atualizado com sucesso!")
            return updated_user
        except Exception as e:
            logger.error(f"Erro ao atualizar usuário {access_token}: {str(e)}")
            raise
    
    async def delete_user(self, access_token: str):
        logger.info(f"Solicitação de exclusão para usuário Firebase UID: {access_token}")
        try:
            # 1. Tenta excluir no Firebase primeiro
            try:
                auth.delete_user(access_token)
                logger.info(f"Usuário {access_token} removido do Firebase com sucesso.")
            except firebase_admin.auth.UserNotFoundError:
                logger.warning(f"Usuário {access_token} não encontrado no Firebase, prosseguindo com exclusão no SQL.")
            except Exception as e:
                logger.error(f"Erro ao remover do Firebase: {str(e)}")
                raise ValueError(f"Falha ao deletar usuário no Firebase: {str(e)}")

            # 2. Exclui no banco de dados SQL
            success = await self.repo.delete(access_token)
            if not success:
                # Opcional: Se quiser tratar como erro apenas se não existir no banco
                raise ValueError("Usuário não encontrado no banco de dados para exclusão.")
                
            logger.success(f"Usuário {access_token} removido com sucesso!")
            return {"message": "Usuário deletado com sucesso", "id": access_token}

        except Exception as e:
            logger.error(f"Erro ao deletar usuário {access_token}: {str(e)}")
            raise