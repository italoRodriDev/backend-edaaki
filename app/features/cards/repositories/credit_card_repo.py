from sqlalchemy import and_, delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from app.features.cards.interfaces.credit_card_interface import ICreditCardRepository
from app.features.cards.models.credit_card_model import CreditCardModel

class SQLCreditCardRepository(ICreditCardRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_by_user(self, user_id: int) -> list:
        stmt = select(CreditCardModel).where(CreditCardModel.user_id == user_id)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def create(self, card_data: dict) -> CreditCardModel:
        new_card = CreditCardModel(**card_data)
        self.session.add(new_card)
        await self.session.commit()
        await self.session.refresh(new_card)
        return new_card

    async def update(self, user_id: int, card_id: int, card_data: dict) -> bool:
        stmt = (
            update(CreditCardModel)
            .where(and_(CreditCardModel.id == card_id, CreditCardModel.user_id == user_id))
            .values(**card_data)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.rowcount > 0

    async def delete(self, user_id: int, card_id: int) -> bool:
        stmt = delete(CreditCardModel).where(
            and_(CreditCardModel.id == card_id, CreditCardModel.user_id == user_id)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.rowcount > 0