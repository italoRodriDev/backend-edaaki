from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class OrderBase(BaseModel):
    buyer_id: int
    product_id: int
    price: float = Field(..., gt=0, description="Preço unitário no momento da compra")
    quantity: int = Field(..., gt=0)
    total: float = Field(..., gt=0, description="Preço unitário * quantidade")
    status: str = Field(default="pending", max_length=50)

class OrderCreate(OrderBase):
    # seller_id não é recebido no body, será injetado pela URL por segurança
    pass

class OrderUpdate(BaseModel):
    # Geralmente, em um pedido, você só atualiza o status ou aplica soft delete
    status: Optional[str] = Field(None, max_length=50)
    deleted: Optional[bool] = None

class OrderResponse(OrderBase):
    id: int
    seller_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted: bool

    class Config:
        from_attributes = True