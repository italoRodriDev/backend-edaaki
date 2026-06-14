class AddressService:
    def __init__(self, repository):
        self.repository = repository

    async def list_user_addresses(self, user_id: int):
        return await self.repository.get_all_by_user(user_id)

    async def create_address(self, user_id: int, data):
        data_dict = data.model_dump()
        data_dict["user_id"] = user_id
        return await self.repository.create(data_dict)

    async def update_address(self, user_id: int, address_id: int, data):
        return await self.repository.update(user_id, address_id, data.model_dump(exclude_unset=True))

    async def delete_address(self, user_id: int, address_id: int):
        return await self.repository.delete(user_id, address_id)