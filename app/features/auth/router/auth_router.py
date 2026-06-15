from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db_session
from app.features.auth.auth import get_current_user
from app.features.auth.schemas.auth_schemas import AuthResponse, ResetPasswordRequest, RegisterRequest
from app.features.auth.services.auth_service import AuthService
from app.features.profile.repositories.profile_repo import SQLProfileRepository

router = APIRouter(prefix="/auth", tags=["Auth"])

def get_auth_service(db: AsyncSession = Depends(get_db_session)):
    user_repo = SQLProfileRepository(db)
    return AuthService(user_repo)

@router.post("/register", response_model=AuthResponse, status_code=status.HTTP_201_CREATED)
async def register_user(
    data: RegisterRequest,
    service: AuthService = Depends(get_auth_service)
):
    try:
        user = await service.register_with_email_and_password(data)
        return {"message": "Usuário criado com sucesso.", "user": user}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/sync", response_model=AuthResponse, status_code=status.HTTP_200_OK)
async def login_or_register(
    decoded_token: dict = Depends(get_current_user), 
    service: AuthService = Depends(get_auth_service)
):
    """
    Sincroniza o usuário logado via Firebase (Google/Facebook ou Login com Email).
    """
    try:
        user = await service.sync_firebase_user(decoded_token)
        return {"message": "Autenticação realizada com sucesso.", "user": user}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/reset-password", status_code=status.HTTP_200_OK)
async def reset_password(
    data: ResetPasswordRequest,
    service: AuthService = Depends(get_auth_service)
):
    """
    Gera link de redefinição de senha para o usuário.
    """
    try:
        link = await service.generate_reset_password_link(data.email)
        return {
            "message": "Instruções de resete geradas com sucesso.", 
            "reset_link": link 
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))