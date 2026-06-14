from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class AddressBase(BaseModel):
    type_address: str = Field(..., max_length=50)
    street: str = Field(..., max_length=255)
    number: str = Field(..., max_length=20)
    completion: Optional[str] = Field(None, max_length=255)
    neighborhood: str = Field(..., max_length=100)
    postal_code: str = Field(..., max_length=20)
    city: str = Field(..., max_length=100)
    state: str = Field(..., max_length=50)
    country: str = Field("Brasil", max_length=50)

class AddressCreate(AddressBase):
    pass

class AddressUpdate(BaseModel):
    type_address: Optional[str] = Field(None, max_length=50)
    street: Optional[str] = Field(None, max_length=255)
    number: Optional[str] = Field(None, max_length=20)
    completion: Optional[str] = Field(None, max_length=255)
    neighborhood: Optional[str] = Field(None, max_length=100)
    postal_code: Optional[str] = Field(None, max_length=20)
    city: Optional[str] = Field(None, max_length=100)
    state: Optional[str] = Field(None, max_length=50)
    country: Optional[str] = Field(None, max_length=50)

class AddressResponse(AddressBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True