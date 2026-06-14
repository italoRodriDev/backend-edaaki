from abc import ABC, abstractmethod
from typing import List, Optional

class IProductRepository(ABC):
    @abstractmethod
    async def save(self, product_data: dict):
        pass
    
    @abstractmethod
    async def update(self, user_id: int, product_id: int, product_data: dict) -> bool:
        pass

    @abstractmethod
    async def delete(self, user_id: int, product_id: int) -> bool:
        pass

    @abstractmethod
    async def find_by_user(self, user_id: int, limit: int) -> List:
        pass

    @abstractmethod
    async def bulk_update(self, user_id: int, products_data: List[dict]) -> bool:
        pass

    @abstractmethod
    async def delete(self, user_id: int, product_id: int) -> bool:
        pass