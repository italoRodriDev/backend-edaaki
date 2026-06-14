from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ContactBase(BaseModel):
    number_contact: str = Field(..., max_length=50)
    type_contact: str = Field(..., max_length=50)

class ContactCreate(ContactBase):
    pass

class ContactUpdate(BaseModel):
    number_contact: Optional[str] = Field(None, max_length=50)
    type_contact: Optional[str] = Field(None, max_length=50)

class ContactResponse(ContactBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True