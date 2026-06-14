from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PrivacityBase(BaseModel):
    isAccepted: bool
    policyVersion: str

class PrivacityCreate(PrivacityBase):
    pass

class PrivacityUpdate(BaseModel):
    isAccepted: Optional[bool] = None
    policyVersion: Optional[str] = None

class PrivacityResponse(PrivacityBase):
    id: int
    user_id: int
    acceptanceDate: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True