import pytest
from unittest.mock import AsyncMock, MagicMock
from app.features.order.schemas.order_schemas import OrderCreate, OrderUpdate
from app.features.order.services.order_service import OrderService

@pytest.fixture
def repository():
    return MagicMock()

@pytest.fixture
def service(repository):
    return OrderService(repository)

@pytest.mark.asyncio
async def test_create_order(service, repository):
    # Setup
    repository.create = AsyncMock(return_value={"id": 1, "total": 150.0})
    
    order_data = OrderCreate(
        buyer_id=2,
        product_id=5,
        price=50.0,
        quantity=3,
        total=150.0,
        status="pending"
    )

    # Execução: o seller_id (1) é passado na chamada
    result = await service.create_order(1, order_data)

    # Asserções
    assert result["id"] == 1
    assert result["total"] == 150.0
    repository.create.assert_called_once()
    # Verifica se o seller_id foi injetado pelo service
    assert repository.create.call_args[0][0]['seller_id'] == 1

@pytest.mark.asyncio
async def test_list_seller_orders(service, repository):
    # Setup
    repository.get_all_by_seller = AsyncMock(return_value=[{"id": 1}, {"id": 2}])

    # Execução
    result = await service.list_seller_orders(1)

    # Asserções
    assert len(result) == 2
    repository.get_all_by_seller.assert_called_once_with(1, limit=100)

@pytest.mark.asyncio
async def test_update_order_status(service, repository):
    # Setup
    repository.update = AsyncMock(return_value=True)
    update_data = OrderUpdate(status="paid")

    # Execução
    result = await service.update_order(1, 10, update_data)

    # Asserções
    assert result is True
    repository.update.assert_called_once()

@pytest.mark.asyncio
async def test_delete_order_soft_delete(service, repository):
    # Setup
    repository.delete = AsyncMock(return_value=True)

    # Execução
    result = await service.delete_order(1, 10)

    # Asserções
    assert result is True
    repository.delete.assert_called_once_with(1, 10)

@pytest.mark.asyncio
async def test_delete_order_not_found(service, repository):
    # Setup
    repository.delete = AsyncMock(return_value=False)

    # Execução
    result = await service.delete_order(1, 999)

    # Asserções
    assert result is False