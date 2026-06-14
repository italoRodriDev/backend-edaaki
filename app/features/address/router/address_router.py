from fastapi import APIRouter, Depends, status, Path, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db_session

from app.features.address.schemas.address_schemas import AddressCreate, AddressUpdate, AddressResponse
from app.features.address.services.address_service import AddressService
from app.features.address.repositories.address_repo import SQLAddressRepository

router = APIRouter(prefix="/users/{user_id}/addresses", tags=["Addresses"])

def get_address_service(db: AsyncSession = Depends(get_db_session)):
    repo = SQLAddressRepository(db)
    return AddressService(repo)

@router.get("/", response_model=list[AddressResponse])
async def list_addresses(
    user_id: int = Path(..., title="ID do Usuário"),
    service: AddressService = Depends(get_address_service)
):
    return await service.list_user_addresses(user_id)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=AddressResponse)
async def create_address(
    data: AddressCreate,
    user_id: int = Path(..., title="ID do Usuário"),
    service: AddressService = Depends(get_address_service)
):
    return await service.create_address(user_id, data)

@router.put("/{address_id}", status_code=status.HTTP_200_OK)
async def update_address(
    address_id: int = Path(..., title="ID do Endereço"),
    user_id: int = Path(..., title="ID do Usuário"),
    data: AddressUpdate = ...,
    service: AddressService = Depends(get_address_service)
):
    updated = await service.update_address(user_id, address_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Endereço não encontrado ou sem permissão.")
    return {"message": "Endereço atualizado com sucesso!"}

@router.delete("/{address_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_address(
    address_id: int = Path(..., title="ID do Endereço"),
    user_id: int = Path(..., title="ID do Usuário"),
    service: AddressService = Depends(get_address_service)
):
    deleted = await service.delete_address(user_id, address_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Endereço não encontrado ou sem permissão.")
    return None