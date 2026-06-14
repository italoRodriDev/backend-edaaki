from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PlanBase(BaseModel):
    name: str
    description: Optional[str] = None
    status: bool = True
    fixed_value: float
    type_plan: Optional[str] = None
    period_plan: Optional[int] = None
    type_period: Optional[str] = None
    loyalty: Optional[int] = None
    qty_photos: Optional[int] = None
    rate_off: Optional[float] = None
    rate_on: Optional[float] = None
    support: Optional[str] = None

class PlanCreate(PlanBase):
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

class PlanResponse(PlanBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True