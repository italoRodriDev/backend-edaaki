from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class ProductBase(BaseModel):
    name: str = Field(..., max_length=255)
    description: str
    price: float
    old_price: Optional[float] = None
    quantity: int
    category_id: int
    macro_category_id: int
    available: bool = True
    
    # Capacidades (agrupadas para facilitar)
    bike: bool = False
    bike_capacity: Optional[str] = None
    car: bool = False
    car_capacity: Optional[str] = None
    cargotrailer: bool = False
    cargotrailer_capacity: Optional[str] = None
    motorbike: bool = False
    motorbike_capacity: Optional[str] = None
    pickuptruck: bool = False
    pickuptruck_capacity: Optional[str] = None
    truck: bool = False
    truck_capacity: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        
class ProductUpdate(BaseModel):
    category_id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    old_price: Optional[float] = None
    quantity: Optional[int] = None
    available: Optional[bool] = None
    
    # Promoção e Frete
    promotion_percent: Optional[float] = None
    promotion_price: Optional[float] = None
    size: Optional[str] = None
    price_freight: Optional[float] = None
    
    # Veículos
    vehicle_type: Optional[str] = None
    bike: Optional[bool] = None
    bike_capacity: Optional[str] = None
    car: Optional[bool] = None
    car_capacity: Optional[str] = None
    cargotrailer: Optional[bool] = None
    cargotrailer_capacity: Optional[str] = None
    motorbike: Optional[bool] = None
    motorbike_capacity: Optional[str] = None
    pickuptruck: Optional[bool] = None
    pickuptruck_capacity: Optional[str] = None
    truck: Optional[bool] = None
    truck_capacity: Optional[str] = None