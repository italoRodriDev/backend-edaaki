from sqlalchemy import Column, Integer, String, DateTime, func
from app.core.database import Base

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    cpf_cnpj = Column(String(50), nullable=True)
    phone = Column(String(50), nullable=True)
    cep = Column(String(20), nullable=True)
    lat = Column(String(50), nullable=True)
    long = Column(String(50), nullable=True)
    address = Column(String(255), nullable=True)
    city = Column(String(100), nullable=True)
    state = Column(String(50), nullable=True)
    country = Column(String(100), default="Brasil")
    region = Column(String(100), nullable=True)
    type = Column(String(50), default="CLIENTE")
    code_flat = Column(String(50), nullable=True)
    status = Column(String(50), default="ATIVO")
    role = Column(String(50), default="USER")
    gender = Column(String(1), nullable=True)
    civil_state = Column(String(50), nullable=True)
    birth_date = Column(DateTime, nullable=True)
    fantasy_name = Column(String(255), nullable=True)
    logo = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)