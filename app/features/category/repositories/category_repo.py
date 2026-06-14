from sqlalchemy import delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.features.category.models.category_model import CategoryModel
from app.features.category.interfaces.category_interface import ICategoryRepository

class SQLCategoryRepository(ICategoryRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self, limit: int = 100) -> list:
        # Traz as top 100 categorias conforme você mencionou no SELECT
        stmt = select(CategoryModel).limit(limit)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def create(self, category_data: dict) -> CategoryModel:
        new_category = CategoryModel(**category_data)
        self.session.add(new_category)
        await self.session.commit()
        await self.session.refresh(new_category)
        return new_category
    
    async def update(self, category_id: int, category_data: dict) -> bool:
        stmt = (
            update(CategoryModel)
            .where(CategoryModel.id == category_id)
            .values(**category_data)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.rowcount > 0

    async def delete(self, category_id: int) -> bool:
        stmt = delete(CategoryModel).where(CategoryModel.id == category_id)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.rowcount > 0