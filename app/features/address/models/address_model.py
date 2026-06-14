from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from app.core.database import Base

class AddressModel(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    type_address = Column(String(50), nullable=False) # Ex: "Residencial", "Comercial", "Entrega"
    street = Column(String(255), nullable=False)
    number = Column(String(20), nullable=False)       # String para aceitar "S/N" ou "123A"
    completion = Column(String(255))                  # Complemento (opcional)
    neighborhood = Column(String(100), nullable=False)
    postal_code = Column(String(20), nullable=False)
    city = Column(String(100), nullable=False)
    state = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False, default="Brasil")
    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())