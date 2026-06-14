from sqlalchemy import Column, Integer, Boolean, String, DateTime, ForeignKey, func
from app.core.database import Base

class PrivacityModel(Base):
    __tablename__ = "privacity"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Mantive a nomenclatura exata (camelCase) da sua query
    isAccepted = Column(Boolean, default=False)
    policyVersion = Column(String(50), nullable=False)
    
    acceptanceDate = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())