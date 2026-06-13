from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ProfileModel(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "dbo"} # 🚀 Aponta direto pro seu schema do print

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    cpf_cnpj = Column(String)
    cep = Column(String)
    lat = Column(String)
    long = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    region = Column(String)
    type = Column(String)
    code_flat = Column(String)
    status = Column(String)
    access_token = Column(String)
    role = Column(String)
    recpass_token = Column(String)
    gender = Column(String)
    civil_state = Column(String)
    phone = Column(String)
    birth_date = Column(DateTime)
    fantasy_name = Column(String)
    logo = Column(String) # Aqui guardaremos a URL do Firestorage
    created_at = Column(DateTime)
    updated_at = Column(DateTime)