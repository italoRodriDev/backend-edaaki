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

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Plano Premium",
                "description": "Plano ideal para vendedores com alto volume de vendas e destaque na plataforma.",
                "status": True,
                "fixed_value": 99.90,
                "type_plan": "premium",
                "period_plan": 1,
                "type_period": "mes",
                "loyalty": 12,
                "qty_photos": 50,
                "rate_off": 5.0,
                "rate_on": 2.5,
                "support": "24/7 WhatsApp e Email",
                "start_date": "2026-07-01T00:00:00Z",
                "end_date": None
            }
        }
    }

# --- ADICIONADO PARA O SEU ENDPOINT DE UPDATE ---
class PlanUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[bool] = None
    fixed_value: Optional[float] = None
    type_plan: Optional[str] = None
    period_plan: Optional[int] = None
    type_period: Optional[str] = None
    loyalty: Optional[int] = None
    qty_photos: Optional[int] = None
    rate_off: Optional[float] = None
    rate_on: Optional[float] = None
    support: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "fixed_value": 89.90,
                "qty_photos": 100,
                "rate_on": 2.0,
                "description": "Valor promocional aplicado e limite de fotos aumentado."
            }
        }
    }
# ------------------------------------------------

class PlanResponse(PlanBase):
    id: int
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True