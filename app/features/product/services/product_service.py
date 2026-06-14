from app.features.product.schemas.product_schemas import ProductCreate

class ProductService:
    def __init__(self, repo):
        self.repo = repo

    async def create_product(self, user_id: int, product_data: ProductCreate):
        data = product_data.model_dump()
        data['user_id'] = user_id  # Garante que o produto pertença ao usuário logado
        return await self.repo.save(data)

    async def get_my_products(self, user_id: int):
        return await self.repo.find_by_user(user_id)

    async def update_products_in_bulk(self, user_id: int, items: list):
        return await self.repo.bulk_update(user_id, items)
    
    async def update_product(self, user_id: int, product_id: int, data: ProductUpdate) -> bool:
        update_data = data.model_dump(exclude_unset=True)
        
        if not update_data:
            return True # Nada foi enviado para atualizar
            
        return await self.repo.update(user_id, product_id, update_data)

    async def delete_product(self, user_id: int, product_id: int) -> bool:
        return await self.repo.delete(user_id, product_id)