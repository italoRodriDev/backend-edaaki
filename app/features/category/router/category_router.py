from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db_session
from app.features.category.schemas.category_schemas import CategoryCreate, CategoryResponse, CategoryUpdate
from app.features.category.services.category_service import CategoryService
from app.features.category.repositories.category_repo import SQLCategoryRepository

router = APIRouter(prefix="/categories", tags=["Categories"])

def get_category_service(db: AsyncSession = Depends(get_db_session)):
    repo = SQLCategoryRepository(db)
    return CategoryService(repo)

@router.get("/", response_model=list[CategoryResponse])
async def list_categories(service: CategoryService = Depends(get_category_service)):
    return await service.list_categories()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CategoryResponse)
async def create_category(
    data: CategoryCreate, 
    service: CategoryService = Depends(get_category_service)
):
    return await service.create_category(data)

@router.put("/{category_id}", status_code=status.HTTP_200_OK)
async def update_category(
    category_id: int = Path(..., title="ID da Categoria"),
    data: CategoryUpdate = ...,
    service: CategoryService = Depends(get_category_service)
):
    updated = await service.update_category(category_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Categoria não encontrada ou não atualizada.")
    return {"message": "Categoria atualizada com sucesso!"}

@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(
    category_id: int = Path(..., title="ID da Categoria"),
    service: CategoryService = Depends(get_category_service)
):
    deleted = await service.delete_category(category_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Categoria não encontrada.")
    return None