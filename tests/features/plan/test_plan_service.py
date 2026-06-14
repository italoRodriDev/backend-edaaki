import pytest
from unittest.mock import AsyncMock, MagicMock
from app.features.plan.schemas.plan_schemas import PlanCreate
from app.features.plan.services.plan_service import PlanService

@pytest.fixture
def repository():
    return MagicMock()

@pytest.fixture
def service(repository):
    return PlanService(repository)

@pytest.mark.asyncio
async def test_create_plan(service, repository):
    # Setup
    repository.create = AsyncMock(return_value={"id": 1, "name": "Plano Premium"})
    
    plan_data = PlanCreate(
        name="Plano Premium",
        fixed_value=99.90,
        type_plan="Mensal",
        qty_photos=50
    )

    # Execução
    result = await service.create_plan(plan_data)

    # Asserções
    assert result["id"] == 1
    assert result["name"] == "Plano Premium"
    repository.create.assert_called_once()

@pytest.mark.asyncio
async def test_list_plans(service, repository):
    # Setup
    repository.get_all = AsyncMock(return_value=[{"id": 1}, {"id": 2}])

    # Execução
    result = await service.list_plans(limit=100)

    # Asserções
    assert len(result) == 2
    repository.get_all.assert_called_once_with(limit=100)

@pytest.mark.asyncio
async def test_delete_plan(service, repository):
    # Setup
    repository.delete = AsyncMock(return_value=True)

    # Execução
    result = await service.delete_plan(1)

    # Asserções
    assert result is True
    repository.delete.assert_called_once_with(1)

@pytest.mark.asyncio
async def test_delete_plan_not_found(service, repository):
    # Setup
    repository.delete = AsyncMock(return_value=False)

    # Execução
    result = await service.delete_plan(999)

    # Asserções
    assert result is False