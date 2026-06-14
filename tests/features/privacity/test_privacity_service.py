import pytest
from unittest.mock import AsyncMock, MagicMock
from app.features.privacity.schemas.privacity_schemas import PrivacityCreate, PrivacityUpdate
from app.features.privacity.services.privacity_service import PrivacityService

@pytest.fixture
def repository():
    # 'spec' diz ao mock para apenas aceitar métodos que já existem,
    # impedindo que ele crie métodos mágicos que não foram definidos.
    repo = MagicMock(spec=['update', 'get_by_user', 'create', 'delete'])
    repo.update = AsyncMock()
    return repo

@pytest.fixture
def service(repository):
    return PrivacityService(repository)

@pytest.mark.asyncio
async def test_create_privacity(service, repository):
    # Setup
    repository.create = AsyncMock(return_value={"id": 1, "isAccepted": True})
    
    privacity_data = PrivacityCreate(
        isAccepted=True,
        policyVersion="1.0.0"
    )

    # Execução
    result = await service.create_privacity(1, privacity_data) # 1 é o user_id

    # Asserções
    assert result["id"] == 1
    assert result["isAccepted"] is True
    repository.create.assert_called_once()
    # Verifica se o user_id foi injetado pelo service
    assert repository.create.call_args[0][0]['user_id'] == 1

@pytest.mark.asyncio
async def test_get_user_privacity(service, repository):
    # Setup
    repository.get_by_user = AsyncMock(return_value={"id": 1, "isAccepted": True})

    # Execução
    result = await service.get_user_privacity(1)

    # Asserções
    assert result["isAccepted"] is True
    repository.get_by_user.assert_called_once_with(1)

@pytest.mark.asyncio
async def test_update_privacity_no_data(service, repository):
    # Setup: Se passar nada, garante que o model_dump seja vazio
    update_data = PrivacityUpdate() 
    
    # Execução
    result = await service.update_privacity(1, 10, update_data)
    
    # Asserção
    assert result is True
    repository.update.assert_not_called()

@pytest.mark.asyncio
async def test_update_privacity_no_data(service, repository):
    # Setup: Precisamos garantir que o update do repo não seja chamado.
    # Se o service não encontrar dados, ele retorna True sem chamar o repo.
    update_data = PrivacityUpdate(isAccepted=None, policyVersion=None)
    
    # Execução
    result = await service.update_privacity(1, 10, update_data)
    
    # Asserção
    assert result is True
    # Verificamos que o repositório NUNCA foi chamado
    repository.update.assert_not_called()