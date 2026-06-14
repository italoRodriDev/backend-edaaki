from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class AddressBase(BaseModel):
    type_address: str
    street: str
    number: str
    completion: Optional[str] = None
    neighborhood: str
    postal_code: str
    city: str
    state: str
    country: str

class AddressCreate(AddressBase):
    model_config = {
        "json_schema_extra": {
            "example": {
                "type_address": "C",
                "street": "Av. Cabo Branco",
                "number": "1500",
                "completion": "Apto 201, Edifício Mar",
                "neighborhood": "Cabo Branco",
                "postal_code": "58045010",
                "city": "João Pessoa",
                "state": "PB",
                "country": "BRA"
            }
        }
    }

class AddressUpdate(BaseModel):
    type_address: Optional[str] = None
    street: Optional[str] = None
    number: Optional[str] = None
    completion: Optional[str] = None
    neighborhood: Optional[str] = None
    postal_code: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "type_address": "T",
                "street": "Av. Cabo Branco",
                "number": "1500A",
                "completion": "Apto 502, Bloco B",
                "neighborhood": "Cabo Branco",
                "postal_code": "58045010",
                "city": "João Pessoa",
                "state": "PB",
                "country": "BRA"
            }
        }
    }

class AddressResponse(AddressBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True