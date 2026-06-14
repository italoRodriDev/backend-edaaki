# 🚀 Backend API — ItMax

### Desenvolvido por developer Italo Rodri.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green?style=for-the-badge&logo=fastapi)
![Firebase](https://img.shields.io/badge/Firebase-Firestore%20%26%20Storage-orange?style=for-the-badge&logo=firebase)
![Poetry](https://img.shields.io/badge/Poetry-Dependency%20Manager-purple?style=for-the-badge)

---

# ✨ Sobre o Projeto

Backend desenvolvido com **FastAPI** para app edaaki.

A API foi construída com foco em:

- ⚡ Alta performance
- 🧱 Arquitetura organizada
- 🔥 Integração com Firebase
- 🧪 Testes automatizados
- 📦 Gerenciamento moderno de dependências
- 🚀 Escalabilidade

---

# 📋 Pré-requisitos

Antes de iniciar o projeto, certifique-se de possuir:

- Python 3.11+
- Poetry
- Arquivo `serviceAccountKey.json` na raiz do projeto

---

# ⚙️ Como Rodar o Projeto

## 1️⃣ Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
```

---

## 2️⃣ Instalar dependências

```bash
poetry install
```

---

## 3️⃣ Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
FIREBASE_BUCKET_NAME=""

ONESIGNAL_APP_ID=""

ONESIGNAL_REST_KEY=""
```

---

## 4️⃣ Iniciar servidor de desenvolvimento

Rodar localmente:

```bash
poetry run uvicorn app.main:app --reload
```

Rodar na rede privada:

```bash
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

---

# 📚 Documentação da API

## Swagger Docs

```txt
http://127.0.0.1:8000/docs
```

# 🧱 Estrutura do Projeto

```plaintext
src/
└── app/
    ├── core/
    │   ├── config.py       # Leitura do .env
    │   ├── database.py     # Conexão com Azure SQL Server
    │   └── firebase.py     # Configuração do Firebase Auth e Storage
    ├── features/
    │   ├── auth/           # Login, Validação de token
    │   │   ├── router.py
    │   │   └── services.py
    │   └── categories/     # CRUD de categorias (com imagem no Storage)
    │       ├── router.py
    │       ├── schemas.py
    │       ├── models.py
    │       └── services.py
    └── main.py             # Entrypoint da aplicação
```

---

# 🛠️ Tecnologias Utilizadas

- FastAPI
- Firebase Firestore
- Firebase Storage
- Python
- Poetry
- Loguru
- Pytest

---

# 🧪 Testes Unitários

## Instalar dependências de testes

```bash
poetry add pytest pytest-asyncio --group dev
```

---

## Executar testes

```bash
python -m poetry run pytest
```

---

# 📄 Logs da Aplicação

## Instalar Loguru

```bash
poetry add loguru
```

---

## Estrutura sugerida

```plaintext
src/core/logging.py
```

---

# ⚙️ Configuração do Python no Poetry

Atualizar versão no `pyproject.toml`:

```toml
requires-python = ">=3.11,<4.0"
```

---

# 🔄 CI/CD — GitHub Actions

Estrutura recomendada:

```plaintext
.github/workflows/main.yml
```

{
  "name": "João da Silva",
  "email": "joao.silva@email.com",
  "cpf_cnpj": "123.456.789-00",
  "phone": "5583999887766",
  "cep": "58000-000",
  "lat": "-7.1150",
  "long": "-34.8631",
  "address": "Av. Epitácio Pessoa, 1000",
  "city": "João Pessoa",
  "state": "PB",
  "country": "Brasil",
  "region": "Nordeste",
  "type": "CLIENTE",
  "code_flat": "APT-402",
  "status": "ATIVO",
  "role": "USER",
  "gender": "M",
  "civil_state": "S",
  "birth_date": "1995-05-15T08:30:00.000Z",
  "fantasy_name": "Joãozinho Entregas",
  "logo": "https://firebasestorage.googleapis.com/v0/b/curriculo-italodev.firebasestorage.app/o/profiles%2Fjoao_avatar.png",
  "password": "senhaSegura123"
}

# TESTES DE ROTAS

Profiles
>> PENDING POST /api/v1/profile/create
>> PENDING GET /api/v1/profile/{user_id}
>> PENDING PUT /api/v1/profile/update/{user_id}
>> PENDING DELETE /api/v1/profile/delete/{user_id}

Products
>> PASS POST /api/v1/users/{user_id}/products/
>> PASS GET /api/v1/users/{user_id}/products/
>> PASS POST /api/v1/users/{user_id}/products/bulk-update
>> PASS PUT /api/v1/users/{user_id}/products/{product_id}
>> PASS DELETE /api/v1/users/{user_id}/products/{product_id}

Categories
>> PASS GET /api/v1/categories/
>> PASS POST /api/v1/categories/
>> PASS PUT /api/v1/categories/{category_id}
>> PASS DELETE /api/v1/categories/{category_id}

Privacity (Contacts)
>> PASS GET /api/v1/users/{user_id}/contacts/
>> ERRO POST /api/v1/users/{user_id}/contacts/
>> PENDING PUT /api/v1/users/{user_id}/contacts/{contact_id}
>> PENDING DELETE /api/v1/users/{user_id}/contacts/{contact_id}

Addresses
>> PASS GET /api/v1/users/{user_id}/addresses/
>> PASS POST /api/v1/users/{user_id}/addresses/
>> PASS PUT /api/v1/users/{user_id}/addresses/{address_id}
>> PASS DELETE /api/v1/users/{user_id}/addresses/{address_id}

Deliveries
>> PENDING GET /api/v1/users/{user_id}/deliveries/
>> PENDING POST /api/v1/users/{user_id}/deliveries/
>> PENDING PUT /api/v1/users/{user_id}/deliveries/{delivery_id}
>> PENDING DELETE /api/v1/users/{user_id}/deliveries/{delivery_id}

Orders
>> PENDING GET /api/v1/users/{user_id}/orders/
>> PENDING POST /api/v1/users/{user_id}/orders/
>> PENDING PUT /api/v1/users/{user_id}/orders/{order_id}
>> PENDING DELETE /api/v1/users/{user_id}/orders/{order_id}

Credit Cards
>> PENDING POST /api/v1/users/{user_id}/credit-cards/
>> PENDING GET /api/v1/users/{user_id}/credit-cards/
>> PENDING DELETE /api/v1/users/{user_id}/credit-cards/{card_id}

Plans
>> PENDING GET /api/v1/plans/
>> PENDING POST /api/v1/plans/
>> PENDING DELETE /api/v1/plans/{plan_id}


