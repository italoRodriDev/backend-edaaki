from abc import ABC, abstractmethod
from typing import List

class IDeliveryRepository(ABC):
    @abstractmethod
    async def get_all_by_seller(self, seller_id: int, limit: int) -> List:
        pass

    @abstractmethod
    async def create(self, delivery_data: dict):
        pass

    @abstractmethod
    async def update(self, seller_id: int, delivery_id: int, data: dict) -> bool:
        pass

    @abstractmethod
    async def delete(self, seller_id: int, delivery_id: int) -> bool:
        pass