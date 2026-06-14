from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ProductBase(BaseModel):
    name: str = Field(..., max_length=255)
    description: str
    price: float
    old_price: Optional[float] = 0.0
    quantity: int
    available: bool = True
    
    # Int no banco de dados
    promotion_percent: Optional[int] = 0 
    promotion_price: Optional[float] = 0.0
    
    size: Optional[str] = ""
    price_freight: Optional[float] = 0.0
    
    # Veículos
    vehicle_type: Optional[str] = ""
    
    # Booleanos e Inteiros (Capacidades)
    bike: bool = False
    bike_capacity: Optional[int] = 0
    car: bool = False
    car_capacity: Optional[int] = 0
    cargotrailer: bool = False
    cargotrailer_capacity: Optional[int] = 0
    motorbike: bool = False
    motorbike_capacity: Optional[int] = 0
    pickuptruck: bool = False
    pickuptruck_capacity: Optional[int] = 0
    truck: bool = False
    truck_capacity: Optional[int] = 0

class ProductCreate(ProductBase):
    macro_category_id: int

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Pinga de Abacaxi Premium",
                "description": "Deliciosa caninha artesanal feita com abacaxi selecionado.",
                "price": 35.50,
                "old_price": 40.00,
                "quantity": 15,
                "available": True,
                "promotion_percent": 0,
                "promotion_price": 0.0,
                "size": "1 Litro",
                "price_freight": 12.50,
                "vehicle_type": "carro",
                "bike": False,
                "bike_capacity": 0,
                "car": True,
                "car_capacity": 50,
                "cargotrailer": False,
                "cargotrailer_capacity": 0,
                "motorbike": False,
                "motorbike_capacity": 0,
                "pickuptruck": False,
                "pickuptruck_capacity": 0,
                "truck": False,
                "truck_capacity": 0,
                "macro_category_id": 33
            }
        }
    }

class ProductUpdate(BaseModel):
    macro_category_id: Optional[int] = None
    category_id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    old_price: Optional[float] = None
    quantity: Optional[int] = None
    available: Optional[bool] = None
    promotion_percent: Optional[int] = None
    promotion_price: Optional[float] = None
    size: Optional[str] = None
    price_freight: Optional[float] = None
    vehicle_type: Optional[str] = None
    bike: Optional[bool] = None
    bike_capacity: Optional[int] = None
    car: Optional[bool] = None
    car_capacity: Optional[int] = None
    cargotrailer: Optional[bool] = None
    cargotrailer_capacity: Optional[int] = None
    motorbike: Optional[bool] = None
    motorbike_capacity: Optional[int] = None
    pickuptruck: Optional[bool] = None
    pickuptruck_capacity: Optional[int] = None
    truck: Optional[bool] = None
    truck_capacity: Optional[int] = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "price": 29.90,
                "old_price": 35.50,
                "quantity": 25,
                "promotion_percent": 15,
                "promotion_price": 29.90,
                "available": True,
                "macro_category_id": 33
            }
        }
    }

class ProductResponse(ProductBase):
    id: int
    user_id: int
    category_id: int
    deleted: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True