from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PrivacityBase(BaseModel):
    isAccepted: bool
    policyVersion: str

class PrivacityCreate(PrivacityBase):
    model_config = {
        "json_schema_extra": {
            "example": {
                "isAccepted": True,
                "policyVersion": "v1.2.0"
            }
        }
    }

class PrivacityUpdate(BaseModel):
    isAccepted: Optional[bool] = None
    policyVersion: Optional[str] = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "isAccepted": False,
                "policyVersion": "v2.0.0"
            }
        }
    }

class PrivacityResponse(PrivacityBase):
    id: int
    user_id: int
    acceptanceDate: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True