from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, DateTime, func
from app.core.database import Base 

class ProductModel(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    category_id = Column(Integer, nullable=False)
    
    name = Column(String(255), nullable=False)
    description = Column(String(500))
    price = Column(Float, nullable=False)
    old_price = Column(Float)
    quantity = Column(Integer, default=0)
    available = Column(Boolean, default=True)
    
    # --- NOVOS CAMPOS DA SUA QUERY ---
    promotion_percent = Column(Float)
    promotion_price = Column(Float)
    size = Column(String(50))
    price_freight = Column(Float)
    deleted = Column(Boolean, default=False)
    vehicle_type = Column(String(100))
    
    # Campos de Logística (Capacidades)
    bike = Column(Boolean, default=False)
    bike_capacity = Column(String(50))
    car = Column(Boolean, default=False)
    car_capacity = Column(String(50))
    cargotrailer = Column(Boolean, default=False)
    cargotrailer_capacity = Column(String(50))
    motorbike = Column(Boolean, default=False)
    motorbike_capacity = Column(String(50))
    pickuptruck = Column(Boolean, default=False)
    pickuptruck_capacity = Column(String(50))
    truck = Column(Boolean, default=False)
    truck_capacity = Column(String(50))
    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())