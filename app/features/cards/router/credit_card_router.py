from fastapi import APIRouter, Depends, status, Path, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db_session
from app.features.cards.schemas.credit_card_schemas import CreditCardCreate, CreditCardResponse
from app.features.cards.repositories.credit_card_repo import SQLCreditCardRepository

router = APIRouter(prefix="/users/{user_id}/credit-cards", tags=["Credit Cards"])

@router.post("/", response_model=CreditCardResponse)
async def create_card(
    data: CreditCardCreate,
    user_id: int = Path(...),
    db: AsyncSession = Depends(get_db_session)
):
    repo = SQLCreditCardRepository(db)
    card_dict = data.model_dump()
    card_dict['user_id'] = user_id
    return await repo.create(card_dict)

@router.get("/", response_model=list[CreditCardResponse])
async def list_cards(
    user_id: int = Path(...),
    db: AsyncSession = Depends(get_db_session)
):
    repo = SQLCreditCardRepository(db)
    return await repo.get_by_user(user_id)

@router.delete("/{card_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_credit_card(
    card_id: int = Path(..., title="ID do Cartão"),
    user_id: int = Path(..., title="ID do Usuário"),
    db: AsyncSession = Depends(get_db_session)
):
    repo = SQLCreditCardRepository(db)
    deleted = await repo.delete(user_id, card_id)
    
    if not deleted:
        raise HTTPException(
            status_code=404, 
            detail="Cartão não encontrado ou não pertence a este usuário."
        )
    return None