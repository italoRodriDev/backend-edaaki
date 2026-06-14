from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from app.core.database import Base

class ContactModel(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    number_contact = Column(String(50), nullable=False) # Ex: "11999999999" ou "email@teste.com"
    type_contact = Column(String(50), nullable=False)   # Ex: "WhatsApp", "Telefone", "Email"
    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())