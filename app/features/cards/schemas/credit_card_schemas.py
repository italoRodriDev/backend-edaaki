from pydantic import BaseModel, Field
from typing import Optional

class CreditCardCreate(BaseModel):
    payment_method_id: Optional[str] = None
    card_name: str = Field(..., max_length=255)
    # Front envia já mascarado (ex: **** 1234)
    card_number: str = Field(..., max_length=50) 
    card_expdate_month: int = Field(..., ge=1, le=12)
    card_expdate_year: int = Field(..., ge=2026) 
    split: bool = False

# --- ADICIONE ESTE SCHEMA QUE ESTAVA FALTANDO ---
class CreditCardUpdate(BaseModel):
    payment_method_id: Optional[str] = None
    card_name: Optional[str] = Field(None, max_length=255)
    card_expdate_month: Optional[int] = Field(None, ge=1, le=12)
    card_expdate_year: Optional[int] = Field(None, ge=2026)
    split: Optional[bool] = None
# --------------------------------------------------

class CreditCardResponse(BaseModel):
    id: int
    user_id: int
    payment_method_id: Optional[str] = None
    card_name: str
    card_number: str # Retorna a versão mascarada
    card_expdate_month: int
    card_expdate_year: int
    split: bool

    class Config:
        from_attributes = True