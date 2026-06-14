from app.features.order.schemas.order_schemas import OrderCreate, OrderUpdate
from app.features.order.interfaces.order_interface import IOrderRepository

class OrderService:
    def __init__(self, repo: IOrderRepository):
        self.repo = repo

    async def list_seller_orders(self, seller_id: int):
        return await self.repo.get_all_by_seller(seller_id, limit=100)

    async def create_order(self, seller_id: int, data: OrderCreate):
        order_dict = data.model_dump()
        order_dict['seller_id'] = seller_id # Proteção: Vendedor é injetado pelo sistema
        # Você também poderia recalcular o 'total' aqui para evitar fraudes no front-end:
        # order_dict['total'] = order_dict['price'] * order_dict['quantity']
        return await self.repo.create(order_dict)

    async def update_order(self, seller_id: int, order_id: int, data: OrderUpdate) -> bool:
        update_data = data.model_dump(exclude_unset=True)
        if not update_data:
            return True
        return await self.repo.update(seller_id, order_id, update_data)

    async def delete_order(self, seller_id: int, order_id: int) -> bool:
        return await self.repo.delete(seller_id, order_id)