import sys
import os
import pytest
from fastapi.testclient import TestClient
from app.main import app
# Importe aqui a dependência do seu banco (get_db, etc)
# from app.core.database import get_db

@pytest.fixture(scope="module")
def client():
    # Aqui você poderia sobrescrever dependências se necessário
    # app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c

# Isso força o Python a ver a pasta raiz como um local de módulos
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))