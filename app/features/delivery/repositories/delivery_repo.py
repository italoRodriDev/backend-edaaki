from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, and_
from app.features.delivery.models.delivery_model import DeliveryModel
from app.features.delivery.interfaces.delivery_interface import IDeliveryRepository

class SQLDeliveryRepository(IDeliveryRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_by_seller(self, seller_id: int, limit: int = 100) -> list:
        stmt = (
            select(DeliveryModel)
            .where(
                and_(
                    DeliveryModel.seller_id == seller_id,
                    DeliveryModel.deleted == False
                )
            )
            .limit(limit)
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def create(self, delivery_data: dict) -> DeliveryModel:
        new_delivery = DeliveryModel(**delivery_data)
        self.session.add(new_delivery)
        await self.session.commit()
        await self.session.refresh(new_delivery)
        return new_delivery

    async def update(self, seller_id: int, delivery_id: int, delivery_data: dict) -> bool:
        stmt = (
            update(DeliveryModel)
            .where(and_(DeliveryModel.id == delivery_id, DeliveryModel.seller_id == seller_id))
            .values(**delivery_data)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.rowcount > 0

    async def delete(self, seller_id: int, delivery_id: int) -> bool:
        # Soft delete (Apenas marca como deletado, não apaga o histórico de vendas)
        stmt = (
            update(DeliveryModel)
            .where(and_(DeliveryModel.id == delivery_id, DeliveryModel.seller_id == seller_id))
            .values(deleted=True)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.rowcount > 0