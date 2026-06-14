from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime

# 1. ESQUEMA BASE (Campos compartilhados)
class UserBase(BaseModel):
    name: str = Field(..., min_length=2, description="Nome completo do usuário")
    email: EmailStr = Field(..., description="E-mail válido e único")
    cpf_cnpj: Optional[str] = Field(None, description="Documento (CPF ou CNPJ)")
    phone: Optional[str] = Field(None, description="Telefone de contato")
    cep: Optional[str] = None
    lat: Optional[str] = None
    long: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = Field("Brasil", description="País padrão")
    region: Optional[str] = None
    type: Optional[str] = Field("CLIENTE", description="Tipo de usuário (ex: CLIENTE, LOJA)")
    code_flat: Optional[str] = None
    status: Optional[str] = Field("ATIVO", description="Status da conta")
    role: Optional[str] = Field("USER", description="Papel de permissão (USER, ADMIN)")
    gender: Optional[str] = Field(None, max_length=1, min_length=1) # Ajustado para Optional não conflitar sem default
    civil_state: Optional[str] = None
    birth_date: Optional[datetime] = None
    fantasy_name: Optional[str] = None
    logo: Optional[str] = Field(None, description="URL da imagem salva no Firebase Storage")

# 2. ESQUEMA DE CRIAÇÃO (POST)
class UserCreate(UserBase):
    password: str = Field(..., min_length=6, description="Senha do usuário")

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "João da Silva",
                "email": "joao.silva@email.com",
                "cpf_cnpj": "123.456.789-00",
                "phone": "5583999887766",
                "cep": "58000-000",
                "lat": "-7.1150",
                "long": "-34.8631",
                "address": "Av. Epitácio Pessoa, 1000",
                "city": "João Pessoa",
                "state": "PB",
                "country": "Brasil",
                "region": "Nordeste",
                "type": "CLIENTE",
                "code_flat": "APT-402",
                "status": "ATIVO",
                "role": "USER",
                "gender": "M",
                "civil_state": "S",
                "birth_date": "1995-05-15T08:30:00.000Z",
                "fantasy_name": "Joãozinho Entregas",
                "logo": "https://firebasestorage.googleapis.com/v0/b/curriculo-italodev.firebasestorage.app/o/profiles%2Fjoao_avatar.png",
                "password": "senhaSegura123"
            }
        }
    }

# 3. ESQUEMA DE ATUALIZAÇÃO (PUT/PATCH)
class UserUpdate(BaseModel):
    # Todos os campos são opcionais para permitir que o app atualize apenas o necessário
    name: Optional[str] = None
    phone: Optional[str] = None
    cep: Optional[str] = None
    lat: Optional[str] = None
    long: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    logo: Optional[str] = None
    status: Optional[str] = None
    fantasy_name: Optional[str] = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "phone": "5583988776655",
                "address": "Av. Presidente Epitácio Pessoa, 1500",
                "logo": "https://firebasestorage.googleapis.com/v0/b/curriculo-italodev.firebasestorage.app/o/profiles%2Fjoao_avatar_v2.png"
            }
        }
    }

# 4. ESQUEMA DE RESPOSTA (GET)
class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        # Permite que o Pydantic leia o objeto do SQLAlchemy diretamente
        from_attributes = True