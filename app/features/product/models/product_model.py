from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, func
from app.core.database import Base

class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    category_id = Column(Integer)
    name = Column(String(255))
    description = Column(String)
    price = Column(Float)
    old_price = Column(Float, nullable=True)
    quantity = Column(Integer)
    available = Column(Boolean, default=True)
    promotion_percent = Column(Float, nullable=True)
    promotion_price = Column(Float, nullable=True)
    size = Column(String(50), nullable=True)
    price_freight = Column(Float, nullable=True)
    
    # Veículos e Capacidades
    vehicle_type = Column(String(50), nullable=True)
    bike = Column(Boolean, default=False)
    bike_capacity = Column(String(50), nullable=True) # ou Float, dependendo de como você salva
    car = Column(Boolean, default=False)
    car_capacity = Column(String(50), nullable=True)
    cargotrailer = Column(Boolean, default=False)
    cargotrailer_capacity = Column(String(50), nullable=True)
    motorbike = Column(Boolean, default=False)
    motorbike_capacity = Column(String(50), nullable=True)
    pickuptruck = Column(Boolean, default=False)
    pickuptruck_capacity = Column(String(50), nullable=True)
    truck = Column(Boolean, default=False)
    truck_capacity = Column(String(50), nullable=True)

    # Controle
    deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())