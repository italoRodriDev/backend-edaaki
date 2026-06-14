from app.features.address.schemas.address_schemas import AddressCreate, AddressUpdate
from app.features.address.interfaces.address_interface import IAddressRepository

class AddressService:
    def __init__(self, repo: IAddressRepository):
        self.repo = repo

    async def list_user_addresses(self, user_id: int):
        return await self.repo.get_all_by_user(user_id, limit=100)

    async def create_address(self, user_id: int, data: AddressCreate):
        address_dict = data.model_dump()
        address_dict['user_id'] = user_id
        return await self.repo.create(address_dict)

    async def update_address(self, user_id: int, address_id: int, data: AddressUpdate) -> bool:
        update_data = data.model_dump(exclude_unset=True)
        if not update_data:
            return True
        return await self.repo.update(user_id, address_id, update_data)

    async def delete_address(self, user_id: int, address_id: int) -> bool:
        return await self.repo.delete(user_id, address_id)