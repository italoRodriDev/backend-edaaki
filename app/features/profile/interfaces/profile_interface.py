from abc import ABC, abstractmethod

class IProfileRepository(ABC):
    
    @abstractmethod
    async def save_user(self, user_data: dict) -> dict:
        """Cria um novo usuário no banco de dados"""
        pass
    
    @abstractmethod
    async def get_user_by_id(self, user_id: int) -> dict | None:
        """Busca um usuário específico pelo seu ID"""
        pass

    @abstractmethod
    async def update(self, access_token: int, update_data: dict) -> dict | None:
        """Atualiza os dados de um usuário existente"""
        pass

    @abstractmethod
    async def delete(self, user_id: int) -> bool:
        """Remove um usuário do banco de dados"""
        pass