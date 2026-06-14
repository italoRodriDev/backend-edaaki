import pytest
from unittest.mock import AsyncMock, MagicMock
from app.features.delivery.schemas.delivery_schemas import DeliveryCreate, DeliveryUpdate
from app.features.delivery.services.delivery_service import DeliveryService

@pytest.fixture
def repository():
    return MagicMock()

@pytest.fixture
def service(repository):
    return DeliveryService(repository)

@pytest.mark.asyncio
async def test_create_delivery(service, repository):
    # Setup
    repository.create = AsyncMock(return_value={"id": 1, "status": "pending"})
    
    delivery_data = DeliveryCreate(
        buyer_id=2,
        status="pending"
    )

    # Execução
    result = await service.create_delivery(1, delivery_data) # 1 é o seller_id

    # Asserções
    assert result["id"] == 1
    # Verifica se o seller_id foi injetado pelo service
    repository.create.assert_called_once()
    assert repository.create.call_args[0][0]['seller_id'] == 1

@pytest.mark.asyncio
async def test_list_seller_deliveries(service, repository):
    # Setup
    repository.get_all_by_seller = AsyncMock(return_value=[{"id": 1}, {"id": 2}])

    # Execução
    result = await service.list_seller_deliveries(1)

    # Asserções
    assert len(result) == 2
    repository.get_all_by_seller.assert_called_once_with(1, limit=100)

@pytest.mark.asyncio
async def test_update_delivery(service, repository):
    # Setup
    repository.update = AsyncMock(return_value=True)
    update_data = DeliveryUpdate(status="delivered")

    # Execução
    result = await service.update_delivery(1, 10, update_data)

    # Asserções
    assert result is True
    repository.update.assert_called_once()

@pytest.mark.asyncio
async def test_delete_delivery(service, repository):
    # Setup: No Soft Delete, o delete apenas atualiza a flag
    repository.delete = AsyncMock(return_value=True)

    # Execução
    result = await service.delete_delivery(1, 10)

    # Asserções
    assert result is True
    repository.delete.assert_called_once_with(1, 10)