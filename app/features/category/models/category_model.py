from sqlalchemy import Column, Integer, String
from app.core.database import Base 

class CategoryModel(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    colour = Column(String(50))
    image = Column(String(500))
    macro = Column(Integer) # Assumindo que 'macro' seja um ID ou um indicador numérico