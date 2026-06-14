import pytest
from unittest.mock import AsyncMock, MagicMock
from app.features.contact.schemas.contact_schemas import ContactCreate, ContactUpdate
from app.features.contact.services.contact_service import ContactService

@pytest.fixture
def repository():
    return MagicMock()

@pytest.fixture
def service(repository):
    return ContactService(repository)

@pytest.mark.asyncio
async def test_create_contact(service, repository):
    # Setup
    repository.create = AsyncMock(return_value={"id": 1, "number_contact": "999999999"})
    
    contact_data = ContactCreate(
        number_contact="999999999",
        type_contact="WhatsApp"
    )

    # Execução
    result = await service.create_contact(1, contact_data) # 1 é o user_id

    # Asserções
    assert result["id"] == 1
    # Verifica se o seller/user ID foi injetado pelo service
    repository.create.assert_called_once()
    assert repository.create.call_args[0][0]['user_id'] == 1

@pytest.mark.asyncio
async def test_list_contacts(service, repository):
    # Setup
    repository.get_all_by_user = AsyncMock(return_value=[{"id": 1}, {"id": 2}])

    # Execução
    result = await service.list_user_contacts(1)

    # Asserções
    assert len(result) == 2
    repository.get_all_by_user.assert_called_once_with(1)

@pytest.mark.asyncio
async def test_update_contact(service, repository):
    # Setup
    repository.update = AsyncMock(return_value=True)
    update_data = ContactUpdate(type_contact="Telefone Fixo")

    # Execução
    result = await service.update_contact(1, 10, update_data)

    # Asserções
    assert result is True
    repository.update.assert_called_once()

@pytest.mark.asyncio
async def test_delete_contact(service, repository):
    # Setup
    repository.delete = AsyncMock(return_value=True)

    # Execução
    result = await service.delete_contact(1, 10)

    # Asserções
    assert result is True
    repository.delete.assert_called_once_with(1, 10)

@pytest.mark.asyncio
async def test_delete_contact_not_found(service, repository):
    # Setup
    repository.delete = AsyncMock(return_value=False)

    # Execução
    result = await service.delete_contact(1, 999)

    # Asserções
    assert result is False