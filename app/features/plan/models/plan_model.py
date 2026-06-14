from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, func
from app.core.database import Base

class PlanModel(Base):
    __tablename__ = "plans"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    status = Column(Boolean, default=True)
    
    fixed_value = Column(Float, nullable=False)
    type_plan = Column(String(50))
    
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    
    period_plan = Column(Integer)
    type_period = Column(String(50)) # Ex: "mensal", "anual"
    loyalty = Column(Integer)        # Meses de fidelidade
    
    qty_photos = Column(Integer)
    rate_off = Column(Float)
    rate_on = Column(Float)
    support = Column(String(100))
    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())