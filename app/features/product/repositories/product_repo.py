from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete, and_
from app.features.product.models.product_model import ProductModel
from app.features.product.interfaces.product_interface import IProductRepository
from sqlalchemy.future import select
from sqlalchemy import and_

# Agora a classe HERDA da interface
class SQLProductRepository(IProductRepository): 
    # O tipo aqui deve ser AsyncSession
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, product_data: dict) -> ProductModel:
        new_product = ProductModel(**product_data)
        self.session.add(new_product)
        # Lembre-se: se o seu Service fizer o commit, remova daqui.
        # Mas mantendo aqui, está funcional.
        await self.session.commit()
        await self.session.refresh(new_product)
        return new_product

    async def find_by_user(self, user_id: int, limit: int = 100) -> list:
    # Isso gera EXATAMENTE o SELECT TOP 100 que você mandou, 
    # filtrando pelo dono da loja e escondendo os deletados!
        stmt = select(ProductModel).where(
            and_(
                ProductModel.user_id == user_id,
                ProductModel.deleted == False
            )
        ).limit(limit)
    
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def bulk_update(self, user_id: int, products_data: list) -> bool:
        for item in products_data:
            # .pop('id') é perfeito aqui para separar a chave dos dados
            product_id = item.pop('id')
            stmt = (
                update(ProductModel)
                .where(and_(ProductModel.id == product_id, ProductModel.user_id == user_id))
                .values(**item)
            )
            await self.session.execute(stmt)
        await self.session.commit()
        return True

    async def update(self, user_id: int, product_id: int, product_data: dict) -> bool:
        stmt = (
            update(ProductModel)
            .where(
                and_(
                    ProductModel.id == product_id, 
                    ProductModel.user_id == user_id
                )
            )
            .values(**product_data)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.rowcount > 0

    async def delete(self, user_id: int, product_id: int) -> bool:
        # Aqui você tem duas opções:
        # Opção 1: Exclusão real do banco (HARD DELETE)
        # stmt = delete(ProductModel).where(and_(ProductModel.id == product_id, ProductModel.user_id == user_id))
        
        # Opção 2: Como você tem a coluna 'deleted', vamos fazer um SOFT DELETE (Recomendado)
        stmt = (
            update(ProductModel)
            .where(and_(ProductModel.id == product_id, ProductModel.user_id == user_id))
            .values(deleted=True)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.rowcount > 0