from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, and_
from app.features.order.models.order_model import OrderModel
from app.features.order.interfaces.order_interface import IOrderRepository

class SQLOrderRepository(IOrderRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_by_seller(self, seller_id: int, limit: int = 100) -> list:
        stmt = (
            select(OrderModel)
            .where(
                and_(
                    OrderModel.seller_id == seller_id,
                    OrderModel.deleted == False
                )
            )
            .order_by(OrderModel.created_at.desc()) # Mais recentes primeiro
            .limit(limit)
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def create(self, order_data: dict) -> OrderModel:
        new_order = OrderModel(**order_data)
        self.session.add(new_order)
        await self.session.commit()
        await self.session.refresh(new_order)
        return new_order

    async def update(self, seller_id: int, order_id: int, order_data: dict) -> bool:
        stmt = (
            update(OrderModel)
            .where(and_(OrderModel.id == order_id, OrderModel.seller_id == seller_id))
            .values(**order_data)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.rowcount > 0

    async def delete(self, seller_id: int, order_id: int) -> bool:
        # Soft delete: Oculta o pedido do painel, mas mantém os dados financeiros
        stmt = (
            update(OrderModel)
            .where(and_(OrderModel.id == order_id, OrderModel.seller_id == seller_id))
            .values(deleted=True)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.rowcount > 0