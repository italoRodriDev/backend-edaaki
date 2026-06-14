class BaseAPITest:
    """Classe base para testes de API"""
    client = None # Será injetado pelos testes

    def get_headers(self):
        # Se você implementar autenticação depois, coloca o token aqui
        return {"Content-Type": "application/json"}