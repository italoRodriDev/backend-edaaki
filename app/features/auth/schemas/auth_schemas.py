from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
from app.features.auth.schemas.user_schemas import UserResponse

class RegisterRequest(BaseModel):
    name: str = Field(..., min_length=2)
    email: EmailStr
    password: str = Field(..., min_length=6)
    
    cpf_cnpj: Optional[str] = None
    cep: Optional[str] = None
    lat: Optional[str] = None
    long: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = "BRA"
    region: Optional[str] = None
    type: Optional[str] = "CLIENTE"
    code_flat: Optional[str] = None
    gender: Optional[str] = None
    civil_state: Optional[str] = None
    phone: Optional[str] = None
    birth_date: Optional[datetime] = None
    fantasy_name: Optional[str] = None
    logo: Optional[str] = None
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Ítalo Rodrigues",
                "email": "italo.teste@gmail.com",
                "password": "SenhaSegura123",
                "cpf_cnpj": "123.456.789-00",
                "cep": "58045-010",
                "lat": "-7.1150",
                "long": "-34.8631",
                "address": "Av. Cabo Branco, 1500",
                "city": "João Pessoa",
                "state": "PB",
                "country": "BRA",
                "region": "Nordeste",
                "type": "CLIENTE",
                "code_flat": "Apto 201",
                "gender": "M",
                "civil_state": "S",
                "phone": "+5583996244003",
                "birth_date": "1999-01-01T00:00:00.000Z",
                "fantasy_name": "Minha Loja PB",
                "logo": "https://firebasestorage.googleapis.com/v0/b/seu-app.appspot.com/o/avatar.png"
            }
        }
    }

class TokenRequest(BaseModel):
    id_token: str

class ResetPasswordRequest(BaseModel):
    email: EmailStr

class AuthResponse(BaseModel):
    message: str
    user: UserResponse