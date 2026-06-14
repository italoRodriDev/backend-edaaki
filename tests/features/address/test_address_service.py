import pytest
from unittest.mock import AsyncMock, MagicMock
from app.features.address.schemas.address_schemas import AddressCreate, AddressUpdate
from app.features.address.services.address_service import AddressService

@pytest.fixture
def repository():
    return MagicMock()

@pytest.fixture
def service(repository):
    return AddressService(repository)

@pytest.mark.asyncio
async def test_create_address(service, repository):
    repository.create = AsyncMock(return_value={"id": 1, "street": "Rua das Flores"})
    
    address_data = AddressCreate(
        street="Rua das Flores",
        number="123",
        city="João Pessoa",
        state="PB",
        zip_code="58000-000",
        is_default=True,
        type_address="Casa",        # Campo faltante
        neighborhood="Bairro Teste", # Campo faltante
        postal_code="58000-000"     # Campo faltante
    )

    result = await service.create_address(1, address_data)
    assert result["id"] == 1
    repository.create.assert_called_once()

@pytest.mark.asyncio
async def test_list_user_addresses(service, repository):
    repository.get_all_by_user = AsyncMock(return_value=[{"id": 1}, {"id": 2}])
    result = await service.list_user_addresses(1)
    
    assert len(result) == 2
    # CORREÇÃO: Adicionando o parâmetro que o service realmente envia
    repository.get_all_by_user.assert_called_once_with(1, limit=100)

@pytest.mark.asyncio
async def test_update_address(service, repository):
    # Setup
    repository.update = AsyncMock(return_value=True)
    update_data = AddressUpdate(street="Rua Nova")

    # Execução
    result = await service.update_address(1, 10, update_data) # user_id 1, address_id 10

    # Asserções
    assert result is True
    repository.update.assert_called_once()

@pytest.mark.asyncio
async def test_delete_address(service, repository):
    # Setup
    repository.delete = AsyncMock(return_value=True)

    # Execução
    result = await service.delete_address(1, 10)

    # Asserções
    assert result is True
    repository.delete.assert_called_once_with(1, 10)

@pytest.mark.asyncio
async def test_delete_address_not_found(service, repository):
    # Setup
    repository.delete = AsyncMock(return_value=False)

    # Execução
    result = await service.delete_address(1, 999)

    # Asserções
    assert result is False