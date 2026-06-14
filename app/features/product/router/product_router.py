from fastapi import APIRouter, Depends, Path, HTTPException, status, Body
from typing import List
from app.core.database import get_db_session
from app.features.product.schemas.product_schemas import ProductCreate, ProductUpdate, ProductResponse
from app.features.product.services.product_service import ProductService
from app.features.product.repositories.product_repo import SQLProductRepository

router = APIRouter(prefix="/users/{user_id}/products", tags=["Products"])

def get_product_service(db=Depends(get_db_session)):
    return ProductService(SQLProductRepository(db))

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ProductResponse)
async def create_product(
    user_id: int = Path(..., gt=0),
    data: ProductCreate = Body(...),
    service: ProductService = Depends(get_product_service)
):
    return await service.create_product(user_id, data)

@router.get("/", response_model=List[ProductResponse])
async def list_products(
    user_id: int = Path(..., gt=0),
    service: ProductService = Depends(get_product_service)
):
    return await service.get_my_products(user_id)

@router.put("/{product_id}", status_code=status.HTTP_200_OK)
async def update_product(
    user_id: int = Path(..., gt=0),
    product_id: int = Path(..., gt=0),
    data: ProductUpdate = Body(...),
    service: ProductService = Depends(get_product_service)
):
    success = await service.update_product(user_id, product_id, data)
    if not success:
        raise HTTPException(status_code=404, detail="Produto não encontrado ou acesso negado.")
    return {"message": "Produto atualizado com sucesso."}

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    user_id: int = Path(..., gt=0),
    product_id: int = Path(..., gt=0),
    service: ProductService = Depends(get_product_service)
):
    success = await service.delete_product(user_id, product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Produto não encontrado ou acesso negado.")
    return None