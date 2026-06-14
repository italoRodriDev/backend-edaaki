from tests.base_test import BaseAPITest

class TestCategoryRoutes(BaseAPITest):
    def test_list_all(self, client):
        response = client.get("/categories/")
        assert response.status_code == 200

    def test_create_invalid(self, client):
        # Testa validação de erro (422 Unprocessable Entity)
        response = client.post("/categories/", json={"name": ""})
        assert response.status_code == 422

class TestAddressRoutes(BaseAPITest):
    def test_list_addresses(self, client):
        # Aqui você pode testar se a rota existe
        response = client.get("/address/")
        # Se precisar de Auth, aqui vai falhar como 401 ou 403, o que é esperado
        assert response.status_code in [200, 401, 403]