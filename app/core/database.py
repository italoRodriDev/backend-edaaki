import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv() # Carrega as variáveis do arquivo .env

# Lê o ambiente atual
env = os.getenv("ENVIRONMENT", "hml")

# Define a URL baseada no ambiente
if env == "prd":
    DATABASE_URL = os.getenv("DATABASE_URL_PRD")
else:
    DATABASE_URL = os.getenv("DATABASE_URL_HML")

print(f"--- Conectando ao banco de: {env.upper()} ---")

engine = create_async_engine(DATABASE_URL, echo=True, future=True)
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# ==========================================
# AQUI ESTÁ A CORREÇÃO DO ERRO DE IMPORTAÇÃO
# ==========================================
Base = declarative_base()

# ==========================================
# GERENCIADOR DE SESSÃO À PROVA DE FALHAS
# ==========================================
async def get_db_session():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()