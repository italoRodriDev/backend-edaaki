from pydantic import BaseModel
from typing import Optional

class CategoryBase(BaseModel):
    name: str
    colour: Optional[str] = None
    image: Optional[str] = None
    macro: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int

    class Config:
        from_attributes = True
        
class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    colour: Optional[str] = None
    image: Optional[str] = None
    macro: Optional[str] = None