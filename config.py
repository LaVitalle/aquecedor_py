import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Configurações da aplicação"""
    
    # Configurações básicas
    app_name: str = os.getenv("APP_NAME", "Aquecedor Whatsapp API")
    app_version: str = os.getenv("APP_VERSION", "1.0.0")
    debug: bool = os.getenv("DEBUG", "True").lower() in ("true", "1", "yes")
    
    # Configurações do servidor
    host: str = os.getenv("HOST", "0.0.0.0")
    port: int = int(os.getenv("PORT", "8845"))
    
    # Configurações de banco de dados
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./app.db")
    
    # Configurações de segurança
    secret_key: str = os.getenv("SECRET_KEY", "your-secret-key-here")
    algorithm: str = os.getenv("ALGORITHM", "HS256")
    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
    
    # Configurações de CORS
    cors_origins: list = ["*"]  # This could be parsed from CORS_ORIGINS env var if needed
    
    class Config:
        env_file = ".env"
        case_sensitive = False

# Instância global das configurações
settings = Settings()