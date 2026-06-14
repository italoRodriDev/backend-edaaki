from abc import ABC, abstractmethod
from typing import List, Optional

class IPlanRepository(ABC):
    @abstractmethod
    async def get_all(self, limit: int) -> List:
        pass

    @abstractmethod
    async def create(self, plan_data: dict):
        pass

    @abstractmethod
    async def delete(self, plan_id: int) -> bool:
        pass