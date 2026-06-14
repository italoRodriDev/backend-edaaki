from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.core.database import Base

class CreditCardModel(Base):
    __tablename__ = "creditCard"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    payment_method_id = Column(String(255))
    card_name = Column(String(255), nullable=False)
    
    # Armazena a versão mascarada enviada pelo front (ex: "**** **** **** 1234")
    card_number = Column(String(50), nullable=False) 
    card_expdate_month = Column(Integer, nullable=False)
    card_expdate_year = Column(Integer, nullable=False)
    
    split = Column(Boolean, default=False)