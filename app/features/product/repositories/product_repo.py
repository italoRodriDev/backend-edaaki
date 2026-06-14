from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.features.product.interfaces.product_interface import IProductRepository
from app.features.product.models.product_model import ProductModel

class SQLProductRepository(IProductRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def save(self, data: dict):
        new_product = ProductModel(**data)
        self.db.add(new_product)
        await self.db.commit()
        await self.db.refresh(new_product)
        return new_product

    async def find_by_user(self, user_id: int):
        result = await self.db.execute(
            select(ProductModel).where(ProductModel.user_id == user_id, ProductModel.deleted == False)
        )
        return result.scalars().all()

    async def update(self, user_id: int, product_id: int, data: dict) -> bool:
        result = await self.db.execute(
            select(ProductModel).where(
                ProductModel.id == product_id, 
                ProductModel.user_id == user_id,
                ProductModel.deleted == False
            )
        )
        product = result.scalar_one_or_none()
        
        if not product:
            return False
            
        for key, value in data.items():
            setattr(product, key, value)
            
        await self.db.commit()
        return True

    async def delete(self, user_id: int, product_id: int) -> bool:
        result = await self.db.execute(
            select(ProductModel).where(ProductModel.id == product_id, ProductModel.user_id == user_id)
        )
        product = result.scalar_one_or_none()
        if product:
            product.deleted = True # Soft Delete
            await self.db.commit()
            return True
        return False