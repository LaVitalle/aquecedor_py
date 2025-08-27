import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Configurações da aplicação"""
    
    # Configurações básicas
    app_name: str = "Aquecedor Whatsapp API"
    app_version: str = "1.0.0"
    debug: bool = os.getenv("DEBUG", True)
    
    # Configurações do servidor
    host: str = "0.0.0.0"
    port: int = 8000
    
    # Configurações de banco de dados
    database_url: str = "sqlite:///./app.db"
    
    # Configurações de segurança
    secret_key: str = "your-secret-key-here"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # Configurações de CORS
    cors_origins: list = ["*"]
    
    class Config:
        env_file = ".env"
        case_sensitive = False

# Instância global das configurações
settings = Settings()