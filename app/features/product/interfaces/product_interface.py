from abc import ABC, abstractmethod
from typing import Any, Dict, List
class IProductRepository(ABC):
    
    @abstractmethod
    async def save(self, data: Dict[str, Any]) -> Any: pass
    
    @abstractmethod
    async def find_by_user(self, user_id: int) -> List[Any]: pass
    
    @abstractmethod
    async def update(self, user_id: int, product_id: int, data: Dict[str, Any]) -> bool: pass
    
    @abstractmethod
    async def delete(self, user_id: int, product_id: int) -> bool: pass