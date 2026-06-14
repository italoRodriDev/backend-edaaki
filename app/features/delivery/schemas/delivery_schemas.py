from pydantic import BaseModel, Field
from typing import Optional

class DeliveryBase(BaseModel):
    buyer_id: int
    deliveryman_id: Optional[int] = None
    status: str = Field(default="pending", max_length=50)
    session_id: Optional[str] = Field(None, max_length=255)

class DeliveryCreate(DeliveryBase):
    # O seller_id não está aqui porque pegaremos ele da URL por segurança
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "buyer_id": 142,
                "deliveryman_id": None,
                "status": "pending",
                "session_id": "cs_test_a1Wb2c3d4E5f6G"
            }
        }
    }

class DeliveryUpdate(BaseModel):
    status: Optional[str] = Field(None, max_length=50)
    deliveryman_id: Optional[int] = None
    session_id: Optional[str] = Field(None, max_length=255)
    deleted: Optional[bool] = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "status": "em_rota",
                "deliveryman_id": 88,
                "deleted": False
            }
        }
    }

class DeliveryResponse(DeliveryBase):
    id: int
    seller_id: int
    deleted: bool

    class Config:
        from_attributes = True