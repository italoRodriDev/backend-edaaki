from app.features.category.schemas.category_schemas import CategoryCreate, CategoryUpdate
from app.features.category.interfaces.category_interface import ICategoryRepository

class CategoryService:
    def __init__(self, repo: ICategoryRepository):
        self.repo = repo

    async def list_categories(self):
        return await self.repo.get_all()

    async def create_category(self, data: CategoryCreate):
        category_dict = data.model_dump()
        return await self.repo.create(category_dict)
    
    async def update_category(self, category_id: int, data: CategoryUpdate) -> bool:
        # exclude_unset=True ignora os campos que o usuário não enviou na requisição
        category_dict = data.model_dump(exclude_unset=True)
        
        if not category_dict:
            return True # Não há o que atualizar
            
        return await self.repo.update(category_id, category_dict)

    async def delete_category(self, category_id: int) -> bool:
        return await self.repo.delete(category_id)