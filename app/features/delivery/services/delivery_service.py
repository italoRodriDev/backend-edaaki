from app.features.delivery.schemas.delivery_schemas import DeliveryCreate, DeliveryUpdate
from app.features.delivery.interfaces.delivery_interface import IDeliveryRepository

class DeliveryService:
    def __init__(self, repo: IDeliveryRepository):
        self.repo = repo

    async def list_seller_deliveries(self, seller_id: int):
        return await self.repo.get_all_by_seller(seller_id, limit=100)

    async def create_delivery(self, seller_id: int, data: DeliveryCreate):
        delivery_dict = data.model_dump()
        delivery_dict['seller_id'] = seller_id # O usuário logado é o vendedor
        return await self.repo.create(delivery_dict)

    async def update_delivery(self, seller_id: int, delivery_id: int, data: DeliveryUpdate) -> bool:
        update_data = data.model_dump(exclude_unset=True)
        if not update_data:
            return True
        return await self.repo.update(seller_id, delivery_id, update_data)

    async def delete_delivery(self, seller_id: int, delivery_id: int) -> bool:
        return await self.repo.delete(seller_id, delivery_id)