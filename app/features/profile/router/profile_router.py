from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

# Importações de Autenticação e Banco
from app.features.auth.auth import get_current_user
from app.core.database import get_db_session

# Importações de Schemas, Repositório e Serviço
from app.features.profile.repositories.profile_repo import SQLProfileRepository
from app.features.profile.services.profile_service import ProfileService
from app.features.profile.schemas.profile_schemas import UserCreate, UserResponse, UserUpdate

# Definindo o roteador
router = APIRouter(prefix="/profile", tags=["Profiles"])

# Injeção de Dependência do Serviço conectando com a Sessão SQL
def get_user_service(session: AsyncSession = Depends(get_db_session)):
    repo = SQLProfileRepository(session)
    return ProfileService(repo)

# (POST) - Criar Usuário
@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user(
    user_data: UserCreate,
    service: ProfileService = Depends(get_user_service),
    #current_user: dict = Depends(get_current_user) #
):
    try:
        return await service.create_user(user_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno ao criar usuário: {str(e)}")

# (GET) - Buscar Usuário por ID
@router.get("/{access_token}", response_model=UserResponse)
async def get_user(
    access_token: str, # No SQL, o ID costuma ser inteiro
    service: ProfileService = Depends(get_user_service),
    #current_user: dict = Depends(get_current_user) #
):
    try:
        return await service.get_user(access_token)
    except ValueError as val_err:
        raise HTTPException(status_code=404, detail=str(val_err))

# (PUT) - Atualizar Usuário
@router.put("/update/{access_token}", response_model=UserResponse)
async def update_user(
    access_token: str,
    user_data: UserUpdate,
    service: ProfileService = Depends(get_user_service),
    #current_user: dict = Depends(get_current_user) #
):
    try:
        return await service.update_user(access_token, user_data)
    except ValueError as val_err:
        raise HTTPException(status_code=404, detail=str(val_err))

# (DELETE) - Deletar Usuário
@router.delete('/delete/{access_token}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    access_token: str,
    service: ProfileService = Depends(get_user_service),
    #current_user: dict = Depends(get_current_user)
):
    try:
        await service.delete_user(access_token)
        return None
    except ValueError as val_err:
        raise HTTPException(status_code=404, detail=str(val_err))