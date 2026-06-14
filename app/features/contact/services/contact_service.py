from app.features.contact.schemas.contact_schemas import ContactCreate, ContactUpdate
from app.features.contact.interfaces.contact_interface import IContactRepository

class ContactService:
    def __init__(self, repo: IContactRepository):
        self.repo = repo

    async def list_user_contacts(self, user_id: int):
        return await self.repo.get_all_by_user(user_id)

    async def create_contact(self, user_id: int, data: ContactCreate):
        contact_dict = data.model_dump()
        contact_dict['user_id'] = user_id
        return await self.repo.create(contact_dict)

    async def update_contact(self, user_id: int, contact_id: int, data: ContactUpdate) -> bool:
        update_data = data.model_dump(exclude_unset=True)
        if not update_data:
            return True
        return await self.repo.update(user_id, contact_id, update_data)

    async def delete_contact(self, user_id: int, contact_id: int) -> bool:
        return await self.repo.delete(user_id, contact_id)