from pydantic import BaseModel
from typing import Optional

class CategoryBase(BaseModel):
    name: str
    colour: Optional[str] = None
    image: Optional[str] = None
    macro: Optional[str] = None

class CategoryCreate(CategoryBase):
    # Herda os campos do CategoryBase normalmente
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Bebidas Alcoólicas",
                "colour": "#FF5733",
                "image": "https://meubucket.s3.amazonaws.com/categorias/bebidas.png",
                "macro": "Bebidas"
            }
        }
    }

class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    colour: Optional[str] = None
    image: Optional[str] = None
    macro: Optional[str] = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "colour": "#C0392B",
                "image": "https://meubucket.s3.amazonaws.com/categorias/bebidas_v2.png"
            }
        }
    }

class CategoryResponse(CategoryBase):
    id: int

    class Config:
        from_attributes = True