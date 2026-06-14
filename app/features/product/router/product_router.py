from fastapi import APIRouter, Depends, HTTPException, status, Path
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db_session
from app.features.product.schemas.product_schemas import ProductCreate, ProductResponse, ProductUpdate
from app.features.product.services.product_service import ProductService
from app.features.product.repositories.product_repo import SQLProductRepository

# O prefixo agora termina em /{user_id} para que todas as rotas abaixo o recebam
router = APIRouter(prefix="/users/{user_id}/products", tags=["Products"])

def get_product_service(db: AsyncSession = Depends(get_db_session)):
    repo = SQLProductRepository(db)
    return ProductService(repo)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ProductResponse)
async def create_product(
    user_id: int = Path(..., title="ID do Produtor"),
    data: ProductCreate = ...,
    service: ProductService = Depends(get_product_service)
):
    # Passamos o user_id capturado da URL para o service
    return await service.create_product(user_id=user_id, product_data=data)

@router.get("/", response_model=list[ProductResponse])
async def list_products(
    user_id: int = Path(..., title="ID do Produtor"),
    service: ProductService = Depends(get_product_service)
):
    return await service.get_my_products(user_id=user_id)

@router.post("/bulk-update")
async def bulk_update(
    user_id: int = Path(..., title="ID do Produtor"),
    items: list = ..., 
    service: ProductService = Depends(get_product_service)
):
    return await service.update_products_in_bulk(user_id=user_id, items=items)

@router.put("/{product_id}", status_code=status.HTTP_200_OK)
async def update_product(
    product_id: int = Path(..., title="ID do Produto"),
    user_id: int = Path(..., title="ID do Produtor"),
    data: ProductUpdate = ...,
    service: ProductService = Depends(get_product_service)
):
    updated = await service.update_product(user_id, product_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Produto não encontrado ou você não tem permissão para editá-lo.")
    return {"message": "Produto atualizado com sucesso!"}

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product_id: int = Path(..., title="ID do Produto"),
    user_id: int = Path(..., title="ID do Produtor"),
    service: ProductService = Depends(get_product_service)
):
    deleted = await service.delete_product(user_id, product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Produto não encontrado ou você não tem permissão para excluí-lo.")
    return None