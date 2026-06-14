import pytest
from unittest.mock import AsyncMock, MagicMock
from app.features.product.schemas.product_schemas import ProductCreate, ProductUpdate
from app.features.product.services.product_service import ProductService

@pytest.fixture
def repository():
    return MagicMock()

@pytest.fixture
def service(repository):
    return ProductService(repository)

@pytest.mark.asyncio
async def test_create_product(service, repository):
    repository.save = AsyncMock(return_value={"id": 1, "name": "Produto Teste"})
    
    product_data = ProductCreate(
        category_id=1,
        name="Produto Teste",
        price=100.0,
        quantity=10,
        available=True,
        size="M",
        bike=True,
        description="Descrição completa",    # Campo faltante
        macro_category_id=1                  # Campo faltante
    )

    result = await service.create_product(user_id=1, product_data=product_data)
    assert result["id"] == 1
    repository.save.assert_called_once()

@pytest.mark.asyncio
async def test_update_product(service, repository):
    # Setup
    repository.update = AsyncMock(return_value=True)
    update_data = ProductUpdate(price=150.0)

    # Execução
    result = await service.update_product(user_id=1, product_id=10, data=update_data)

    # Asserções
    assert result is True
    # Verifica se chamou a atualização com os campos corretos
    repository.update.assert_called_once_with(1, 10, {"price": 150.0})

@pytest.mark.asyncio
async def test_delete_product(service, repository):
    # Setup
    repository.delete = AsyncMock(return_value=True)

    # Execução
    result = await service.delete_product(user_id=1, product_id=10)

    # Asserções
    assert result is True
    repository.delete.assert_called_once_with(1, 10)

@pytest.mark.asyncio
async def test_update_product_empty_data(service, repository):
    # Setup
    update_data = ProductUpdate() # Sem campos preenchidos

    # Execução
    result = await service.update_product(user_id=1, product_id=10, data=update_data)

    # Asserções
    assert result is True
    # O repositório não deve nem ser chamado se não houver o que atualizar
    repository.update.assert_not_called()