from fastapi import APIRouter, Depends, status, Path, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db_session
from app.features.address.schemas.address_schemas import AddressCreate, AddressUpdate, AddressResponse
from app.features.address.services.address_service import AddressService
from app.features.address.repositories.address_repo import SQLAddressRepository # Implementação real

router = APIRouter(prefix="/users/{user_id}/addresses", tags=["Addresses"])

def get_service(db: AsyncSession = Depends(get_db_session)) -> AddressService:
    return AddressService(SQLAddressRepository(db))

@router.get("/", response_model=list[AddressResponse])
async def list_addresses(user_id: int = Path(..., gt=0), s: AddressService = Depends(get_service)):
    return await s.list_user_addresses(user_id)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=AddressResponse)
async def create(user_id: int, data: AddressCreate, s: AddressService = Depends(get_service)):
    return await s.create_address(user_id, data)

@router.put("/{address_id}")
async def update(user_id: int, address_id: int, data: AddressUpdate, s: AddressService = Depends(get_service)):
    if not await s.update_address(user_id, address_id, data):
        raise HTTPException(status_code=404, detail="Não encontrado")
    return {"message": "Atualizado"}

@router.delete("/{address_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(user_id: int, address_id: int, s: AddressService = Depends(get_service)):
    if not await s.delete_address(user_id, address_id):
        raise HTTPException(status_code=404, detail="Não encontrado")