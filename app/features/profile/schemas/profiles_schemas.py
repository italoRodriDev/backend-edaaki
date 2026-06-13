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
    gender: Optional[str] = Field(max_length=1, min_length=1)
    civil_state: Optional[str] = None
    birth_date: Optional[datetime] = None
    fantasy_name: Optional[str] = None
    logo: Optional[str] = Field(None, description="URL da imagem salva no Firebase Storage")

# 2. ESQUEMA DE CRIAÇÃO (POST)
class UserCreate(UserBase):
    password: str = Field(..., min_length=6, description="Senha do usuário")

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

# 4. ESQUEMA DE RESPOSTA (GET)
class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        # Permite que o Pydantic leia o objeto do SQLAlchemy diretamente
        from_attributes = True