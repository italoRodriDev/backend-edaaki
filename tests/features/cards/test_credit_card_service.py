import pytest
from unittest.mock import AsyncMock, MagicMock
from app.features.cards.schemas.credit_card_schemas import CreditCardCreate, CreditCardUpdate
from app.features.cards.services.credit_card_service import CreditCardService

@pytest.fixture
def repository():
    return MagicMock()

@pytest.fixture
def service(repository):
    return CreditCardService(repository)

@pytest.mark.asyncio
async def test_create_card_masking(service, repository):
    # Setup: Simulando retorno do repo
    mock_card = MagicMock()
    mock_card.card_number = "1234567812345678"
    repository.create = AsyncMock(return_value=mock_card)
    
    card_data = CreditCardCreate(
        card_name="João Silva",
        card_number="1234567812345678",
        card_expdate_month=12,
        card_expdate_year=2030,
        split=True
    )

    # Execução
    result = await service.create_card(1, card_data)

    # Asserções
    assert result.card_number == "**** **** **** 5678"
    repository.create.assert_called_once()

@pytest.mark.asyncio
async def test_list_cards_masking(service, repository):
    # Setup
    card1 = MagicMock()
    card1.card_number = "1111222233334444"
    repository.get_all_by_user = AsyncMock(return_value=[card1])

    # Execução
    result = await service.list_user_cards(1)

    # Asserções
    assert result[0].card_number == "**** **** **** 4444"
    repository.get_all_by_user.assert_called_once_with(1)

@pytest.mark.asyncio
async def test_delete_card(service, repository):
    # Setup
    repository.delete = AsyncMock(return_value=True)

    # Execução
    result = await service.delete_card(1, 10) # user_id 1, card_id 10

    # Asserções
    assert result is True
    repository.delete.assert_called_once_with(1, 10)

@pytest.mark.asyncio
async def test_update_card(service, repository):
    # Setup
    repository.update = AsyncMock(return_value=True)
    update_data = CreditCardUpdate(card_name="Nome Alterado")

    # Execução
    result = await service.update_card(1, 10, update_data)

    # Asserções
    assert result is True
    repository.update.assert_called_once()