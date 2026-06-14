from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional

class IAddressRepository(ABC):
    @abstractmethod
    async def get_all_by_user(self, user_id: int) -> List[Any]: pass
    
    @abstractmethod
    async def create(self, data: Dict[str, Any]) -> Any: pass
    
    @abstractmethod
    async def update(self, user_id: int, address_id: int, data: Dict[str, Any]) -> bool: pass
    
    @abstractmethod
    async def delete(self, user_id: int, address_id: int) -> bool: pass