from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base

class AddressModel(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    type_address = Column(String(50))
    street = Column(String(255))
    number = Column(String(20))
    completion = Column(String(100), nullable=True)
    neighborhood = Column(String(100))
    postal_code = Column(String(20))
    city = Column(String(100))
    state = Column(String(50))
    country = Column(String(50))
    user_id = Column(Integer, index=True) # Indexado para performance
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())