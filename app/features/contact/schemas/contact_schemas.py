from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ContactBase(BaseModel):
    number_contact: str = Field(..., max_length=50)
    type_contact: str = Field(..., max_length=50)

class ContactCreate(ContactBase):
    model_config = {
        "json_schema_extra": {
            "example": {
                "number_contact": "+55 11 98765-4321",
                "type_contact": "WhatsApp"
            }
        }
    }

class ContactUpdate(BaseModel):
    number_contact: Optional[str] = Field(None, max_length=50)
    type_contact: Optional[str] = Field(None, max_length=50)

    model_config = {
        "json_schema_extra": {
            "example": {
                "number_contact": "+55 11 91234-5678",
                "type_contact": "Telefone Fixo"
            }
        }
    }

class ContactResponse(ContactBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True