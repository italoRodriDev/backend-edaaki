from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    logo: Optional[str] = None
    status: Optional[str] = "ATIVO"
    role: Optional[str] = "USER"
    type: Optional[str] = "CLIENTE"

class UserResponse(UserBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True