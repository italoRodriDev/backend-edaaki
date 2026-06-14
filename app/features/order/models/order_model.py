from sqlalchemy import Column, Integer, Float, String, Boolean, DateTime, ForeignKey, func
from app.core.database import Base

class OrderModel(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    
    # Relacionamentos
    seller_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    buyer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    
    # Dados Financeiros e de Produto
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    total = Column(Float, nullable=False)
    
    # Status (Ex: pending, paid, shipped, delivered, canceled)
    status = Column(String(50), nullable=False, default="pending")
    
    # Controle e Auditoria
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    deleted = Column(Boolean, default=False)