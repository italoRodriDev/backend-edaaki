from abc import ABC, abstractmethod
from typing import List

class IAddressRepository(ABC):
    @abstractmethod
    async def get_all_by_user(self, user_id: int, limit: int) -> List:
        pass

    @abstractmethod
    async def create(self, address_data: dict):
        pass

    @abstractmethod
    async def update(self, user_id: int, address_id: int, data: dict) -> bool:
        pass

    @abstractmethod
    async def delete(self, user_id: int, address_id: int) -> bool:
        pass