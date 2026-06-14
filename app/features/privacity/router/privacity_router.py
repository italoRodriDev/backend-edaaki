from fastapi import APIRouter, Depends, status, Path, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db_session

from app.features.privacity.schemas.privacity_schemas import PrivacityCreate, PrivacityUpdate, PrivacityResponse
from app.features.privacity.services.privacity_service import PrivacityService
from app.features.privacity.repositories.privacity_repo import SQLPrivacityRepository

router = APIRouter(prefix="/users/{user_id}/privacity", tags=["Privacity"])

def get_privacity_service(db: AsyncSession = Depends(get_db_session)):
    repo = SQLPrivacityRepository(db)
    return PrivacityService(repo)

@router.get("/", response_model=PrivacityResponse)
async def get_privacity(
    user_id: int = Path(..., title="ID do Usuário"),
    service: PrivacityService = Depends(get_privacity_service)
):
    privacity = await service.get_user_privacity(user_id)
    if not privacity:
        raise HTTPException(status_code=404, detail="Registro de privacidade não encontrado para este usuário.")
    return privacity

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PrivacityResponse)
async def create_privacity(
    data: PrivacityCreate,
    user_id: int = Path(..., title="ID do Usuário"),
    service: PrivacityService = Depends(get_privacity_service)
):
    return await service.create_privacity(user_id, data)

@router.put("/{privacity_id}", status_code=status.HTTP_200_OK)
async def update_privacity(
    privacity_id: int = Path(..., title="ID do Registro de Privacidade"),
    user_id: int = Path(..., title="ID do Usuário"),
    data: PrivacityUpdate = ...,
    service: PrivacityService = Depends(get_privacity_service)
):
    updated = await service.update_privacity(user_id, privacity_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Registro não encontrado ou sem permissão.")
    return {"message": "Privacidade atualizada com sucesso!"}