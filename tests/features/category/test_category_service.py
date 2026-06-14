import pytest
from unittest.mock import AsyncMock, MagicMock
from app.features.category.schemas.category_schemas import CategoryCreate, CategoryUpdate
from app.features.category.services.category_service import CategoryService

@pytest.fixture
def repository():
    return MagicMock()

@pytest.fixture
def service(repository):
    return CategoryService(repository)

@pytest.mark.asyncio
async def test_create_category(service, repository):
    # Setup
    repository.create = AsyncMock(return_value={"id": 1, "name": "Eletrônicos"})
    
    category_data = CategoryCreate(
        name="Eletrônicos",
        colour="#FFFFFF",
        image="url_imagem",
        macro=1
    )

    # Execução
    result = await service.create_category(category_data)

    # Asserções
    assert result["id"] == 1
    assert result["name"] == "Eletrônicos"
    repository.create.assert_called_once()

@pytest.mark.asyncio
async def test_update_category(service, repository):
    # Setup
    repository.update = AsyncMock(return_value=True)
    update_data = CategoryUpdate(name="Eletroportáteis")

    # Execução
    result = await service.update_category(1, update_data)

    # Asserções
    assert result is True
    repository.update.assert_called_once()

@pytest.mark.asyncio
async def test_delete_category(service, repository):
    # Setup
    repository.delete = AsyncMock(return_value=True)

    # Execução
    result = await service.delete_category(1)

    # Asserções
    assert result is True
    repository.delete.assert_called_once_with(1)