from abc import ABC, abstractmethod
from typing import Optional

class IPrivacityRepository(ABC):
    @abstractmethod
    async def get_by_user(self, user_id: int):
        pass

    @abstractmethod
    async def create(self, privacity_data: dict):
        pass

    @abstractmethod
    async def update(self, user_id: int, privacity_id: int, data: dict) -> bool:
        pass