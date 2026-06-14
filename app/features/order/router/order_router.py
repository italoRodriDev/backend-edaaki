from fastapi import APIRouter, Depends, status, Path, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db_session

from app.features.order.schemas.order_schemas import OrderCreate, OrderUpdate, OrderResponse
from app.features.order.services.order_service import OrderService
from app.features.order.repositories.order_repo import SQLOrderRepository

# O {user_id} raiz representa o dono da loja (Vendedor)
router = APIRouter(prefix="/users/{user_id}/orders", tags=["Orders"])

def get_order_service(db: AsyncSession = Depends(get_db_session)):
    repo = SQLOrderRepository(db)
    return OrderService(repo)

@router.get("/", response_model=list[OrderResponse])
async def list_orders(
    user_id: int = Path(..., title="ID do Vendedor"),
    service: OrderService = Depends(get_order_service)
):
    return await service.list_seller_orders(user_id)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=OrderResponse)
async def create_order(
    data: OrderCreate,
    user_id: int = Path(..., title="ID do Vendedor"),
    service: OrderService = Depends(get_order_service)
):
    return await service.create_order(user_id, data)

@router.put("/{order_id}", status_code=status.HTTP_200_OK)
async def update_order(
    order_id: int = Path(..., title="ID do Pedido"),
    user_id: int = Path(..., title="ID do Vendedor"),
    data: OrderUpdate = ...,
    service: OrderService = Depends(get_order_service)
):
    updated = await service.update_order(user_id, order_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Pedido não encontrado ou sem permissão para editá-lo.")
    return {"message": "Status do pedido atualizado com sucesso!"}

@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(
    order_id: int = Path(..., title="ID do Pedido"),
    user_id: int = Path(..., title="ID do Vendedor"),
    service: OrderService = Depends(get_order_service)
):
    deleted = await service.delete_order(user_id, order_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Pedido não encontrado ou sem permissão para excluí-lo.")
    return None