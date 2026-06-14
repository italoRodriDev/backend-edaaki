from pydantic import BaseModel, Field
from typing import Optional

class CreditCardCreate(BaseModel):
    payment_method_id: Optional[str] = None
    card_name: str = Field(..., max_length=255)
    # Front envia já mascarado (ex: **** **** **** 3132) ou o número real dependendo do seu fluxo
    card_number: str = Field(..., max_length=50) 
    card_expdate_month: int = Field(..., ge=1, le=12)
    card_expdate_year: int = Field(..., ge=2026) 
    
    # Adicionado pois existe na tabela do banco de dados
    card_cvv: str = Field(..., min_length=3, max_length=4) 
    split: bool = False

    model_config = {
        "json_schema_extra": {
            "example": {
                "payment_method_id": "3",
                "card_name": "STEPHEN STRANGE",
                "card_number": "**** **** **** 3132",
                "card_expdate_month": 12,
                "card_expdate_year": 2028,
                "card_cvv": "121",
                "split": True
            }
        }
    }

class CreditCardUpdate(BaseModel):
    payment_method_id: Optional[str] = None
    card_name: Optional[str] = Field(None, max_length=255)
    card_expdate_month: Optional[int] = Field(None, ge=1, le=12)
    card_expdate_year: Optional[int] = Field(None, ge=2026)
    split: Optional[bool] = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "card_expdate_month": 5,
                "card_expdate_year": 2030,
                "split": False
            }
        }
    }

class CreditCardResponse(BaseModel):
    # CORRIGIDO: O banco usa UUID (nvarchar), então deve ser str, não int!
    id: str 
    user_id: int
    payment_method_id: Optional[str] = None
    card_name: str
    card_number: str 
    card_expdate_month: int
    card_expdate_year: int
    split: bool
    # Não retornamos o card_cvv aqui por questões de segurança (PCI Compliance)

    class Config:
        from_attributes = True