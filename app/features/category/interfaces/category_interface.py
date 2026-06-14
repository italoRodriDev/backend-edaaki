from abc import ABC, abstractmethod
from typing import List

class ICategoryRepository(ABC):
    @abstractmethod
    async def get_all(self) -> List:
        pass

    @abstractmethod
    async def create(self, category_data: dict):
        pass
    
    @abstractmethod
    async def update(self, category_id: int, category_data: dict) -> bool:
        pass

    @abstractmethod
    async def delete(self, category_id: int) -> bool:
        pass