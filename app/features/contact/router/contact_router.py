from fastapi import APIRouter, Depends, status, Path, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db_session

from app.features.contact.schemas.contact_schemas import ContactCreate, ContactUpdate, ContactResponse
from app.features.contact.services.contact_service import ContactService
from app.features.contact.repositories.contact_repo import SQLContactRepository

# O prefixo usa o user_id para garantir a segurança hierárquica
router = APIRouter(prefix="/users/{user_id}/contacts", tags=["Contacts"])

def get_contact_service(db: AsyncSession = Depends(get_db_session)):
    repo = SQLContactRepository(db)
    return ContactService(repo)

@router.get("/", response_model=list[ContactResponse])
async def list_contacts(
    user_id: int = Path(..., title="ID do Usuário"),
    service: ContactService = Depends(get_contact_service)
):
    return await service.list_user_contacts(user_id)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ContactResponse)
async def create_contact(
    data: ContactCreate,
    user_id: int = Path(..., title="ID do Usuário"),
    service: ContactService = Depends(get_contact_service)
):
    return await service.create_contact(user_id, data)

@router.put("/{contact_id}", status_code=status.HTTP_200_OK)
async def update_contact(
    contact_id: int = Path(..., title="ID do Contato"),
    user_id: int = Path(..., title="ID do Usuário"),
    data: ContactUpdate = ...,
    service: ContactService = Depends(get_contact_service)
):
    updated = await service.update_contact(user_id, contact_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Contato não encontrado ou sem permissão.")
    return {"message": "Contato atualizado com sucesso!"}

@router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_contact(
    contact_id: int = Path(..., title="ID do Contato"),
    user_id: int = Path(..., title="ID do Usuário"),
    service: ContactService = Depends(get_contact_service)
):
    deleted = await service.delete_contact(user_id, contact_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Contato não encontrado ou sem permissão.")
    return None