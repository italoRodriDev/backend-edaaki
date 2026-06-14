from fastapi import APIRouter, Depends, status, Path, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db_session

from app.features.delivery.schemas.delivery_schemas import DeliveryCreate, DeliveryUpdate, DeliveryResponse
from app.features.delivery.services.delivery_service import DeliveryService
from app.features.delivery.repositories.delivery_repo import SQLDeliveryRepository

# O {user_id} aqui representa o Vendedor (Seller)
router = APIRouter(prefix="/users/{user_id}/deliveries", tags=["Deliveries"])

def get_delivery_service(db: AsyncSession = Depends(get_db_session)):
    repo = SQLDeliveryRepository(db)
    return DeliveryService(repo)

@router.get("/", response_model=list[DeliveryResponse])
async def list_deliveries(
    user_id: int = Path(..., title="ID do Vendedor"),
    service: DeliveryService = Depends(get_delivery_service)
):
    return await service.list_seller_deliveries(user_id)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=DeliveryResponse)
async def create_delivery(
    data: DeliveryCreate,
    user_id: int = Path(..., title="ID do Vendedor"),
    service: DeliveryService = Depends(get_delivery_service)
):
    return await service.create_delivery(user_id, data)

@router.put("/{delivery_id}", status_code=status.HTTP_200_OK)
async def update_delivery(
    delivery_id: int = Path(..., title="ID da Entrega"),
    user_id: int = Path(..., title="ID do Vendedor"),
    data: DeliveryUpdate = ...,
    service: DeliveryService = Depends(get_delivery_service)
):
    updated = await service.update_delivery(user_id, delivery_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Entrega não encontrada ou sem permissão.")
    return {"message": "Status da entrega atualizado com sucesso!"}

@router.delete("/{delivery_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_delivery(
    delivery_id: int = Path(..., title="ID da Entrega"),
    user_id: int = Path(..., title="ID do Vendedor"),
    service: DeliveryService = Depends(get_delivery_service)
):
    deleted = await service.delete_delivery(user_id, delivery_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Entrega não encontrada ou sem permissão.")
    return None