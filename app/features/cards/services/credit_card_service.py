from app.features.cards.schemas.credit_card_schemas import CreditCardCreate, CreditCardUpdate
from app.features.cards.interfaces.credit_card_interface import ICreditCardRepository

class CreditCardService:
    def __init__(self, repo: ICreditCardRepository):
        self.repo = repo

    def _mask_card_number(self, card_number: str) -> str:
        """Mantém apenas os últimos 4 dígitos para exibir ao usuário."""
        if len(card_number) >= 4:
            return f"**** **** **** {card_number[-4:]}"
        return "****"

    async def list_user_cards(self, user_id: int):
        cards = await self.repo.get_all_by_user(user_id)
        # Aplica a máscara para não exibir o número completo na tela
        for card in cards:
            card.card_number = self._mask_card_number(card.card_number)
        return cards

    async def create_card(self, user_id: int, data: CreditCardCreate):
        card_dict = data.model_dump()
        card_dict['user_id'] = user_id
        
        # A lógica de persistência é delegada ao repositório
        created_card = await self.repo.create(card_dict)
        
        # Mascara na resposta do POST também
        created_card.card_number = self._mask_card_number(created_card.card_number)
        return created_card

    async def update_card(self, user_id: int, card_id: int, data: CreditCardUpdate) -> bool:
        update_data = data.model_dump(exclude_unset=True)
        if not update_data:
            return True
        return await self.repo.update(user_id, card_id, update_data)

    async def delete_card(self, user_id: int, card_id: int) -> bool:
        return await self.repo.delete(user_id, card_id)