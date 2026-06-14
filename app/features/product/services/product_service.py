from app.features.product.schemas.product_schemas import ProductCreate, ProductUpdate
from app.features.product.repositories.product_repo import IProductRepository

class ProductService:
    def __init__(self, repo: IProductRepository):
        self.repo = repo

    def _prepare_data(self, data_dict: dict) -> dict:
        """Traduz campos do Schema para o Banco"""
        if "macro_category_id" in data_dict:
            data_dict["category_id"] = data_dict.pop("macro_category_id")
        return data_dict

    async def create_product(self, user_id: int, product_data: ProductCreate):
        data = self._prepare_data(product_data.model_dump())
        data['user_id'] = user_id
        return await self.repo.save(data)

    async def get_my_products(self, user_id: int):
        return await self.repo.find_by_user(user_id)

    async def update_product(self, user_id: int, product_id: int, data: ProductUpdate):
        data_dict = self._prepare_data(data.model_dump(exclude_unset=True))
        return await self.repo.update(user_id, product_id, data_dict)

    async def delete_product(self, user_id: int, product_id: int) -> bool:
        return await self.repo.delete(user_id, product_id)