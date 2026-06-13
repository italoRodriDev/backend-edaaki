import pytest
from unittest.mock import AsyncMock, MagicMock
from app.features.profile.schemas.profiles_schemas import UserCreate, UserUpdate
from app.features.profile.services.profile_service import ProfileService

@pytest.fixture
def repository():
    return MagicMock()

@pytest.fixture
def service(repository):
    return ProfileService(repository)

@pytest.mark.asyncio
async def test_create_user(service, repository):
    # Setup
    repository.save_user = AsyncMock(return_value={"id": 1, "name": "João da Silva"})
    
    user_data = UserCreate(
        name="João da Silva",
        email="joao@email.com",
        password="password123",
        cpf_cnpj="123.456.789-00",
        phone="5583999887766",
        cep="58000-000",
        lat="-7.1150",
        long="-34.8631",
        address="Rua Teste",
        city="João Pessoa",
        state="PB",
        country="Brasil",
        type="CLIENTE",
        status="ATIVO",
        role="USER",
        gender="M",
        civil_state="S",
        birth_date="1995-05-15T08:30:00.000Z"
    )

    result = await service.create_user(user_data)

    assert result["id"] == 1
    assert result["name"] == "João da Silva"
    repository.save_user.assert_called_once()

@pytest.mark.asyncio
async def test_get_user_not_found(service, repository):
    # Setup: Simula que o usuário não existe no DB
    repository.get_user_by_id = AsyncMock(return_value=None)

    # Execução e Asserção de Erro
    with pytest.raises(ValueError, match="Usuário não encontrado."):
        await service.get_user(999)

@pytest.mark.asyncio
async def test_update_user(service, repository):
    # Setup
    repository.update = AsyncMock(return_value={"id": 1, "name": "Novo Nome"})
    
    update_data = UserUpdate(name="Novo Nome")

    # Execução
    result = await service.update_user(1, update_data)

    # Asserções
    assert result["name"] == "Novo Nome"
    repository.update.assert_called_once_with(1, {"name": "Novo Nome"})

@pytest.mark.asyncio
async def test_delete_user(service, repository):
    # Setup
    repository.delete = AsyncMock(return_value=True)

    # Execução
    result = await service.delete_user(1)

    # Asserções
    assert result["message"] == "Usuário deletado com sucesso"
    repository.delete.assert_called_once_with(1)

@pytest.mark.asyncio
async def test_delete_user_not_found(service, repository):
    # Setup
    repository.delete = AsyncMock(return_value=False)

    # Execução
    with pytest.raises(ValueError, match="Usuário não encontrado para exclusão."):
        await service.delete_user(999)