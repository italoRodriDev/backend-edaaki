from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.core.database import Base

class DeliveryModel(Base):
    __tablename__ = "delivery"

    id = Column(Integer, primary_key=True, index=True)
    
    # Relações com os usuários (Vendedor, Comprador, Entregador)
    seller_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    buyer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    deliveryman_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    
    status = Column(String(50), nullable=False, default="pending") # Ex: pending, shipped, delivered
    session_id = Column(String(255)) # ID da sessão de pagamento ou rastreio
    
    deleted = Column(Boolean, default=False)