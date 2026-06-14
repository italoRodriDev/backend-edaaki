from app.features.privacity.schemas.privacity_schemas import PrivacityCreate, PrivacityUpdate
from app.features.privacity.interfaces.privacity_interface import IPrivacityRepository

class PrivacityService:
    def __init__(self, repo: IPrivacityRepository):
        self.repo = repo

    async def get_user_privacity(self, user_id: int):
        return await self.repo.get_by_user(user_id)

    async def create_privacity(self, user_id: int, data: PrivacityCreate):
        privacity_dict = data.model_dump()
        privacity_dict['user_id'] = user_id
        return await self.repo.create(privacity_dict)

    async def update_privacity(self, user_id: int, privacity_id: int, data: PrivacityUpdate) -> bool:
        update_data = data.model_dump(exclude_unset=True, exclude_none=True)
        
        if not update_data:
            return True
        return await self.repo.update(user_id, privacity_id, update_data)