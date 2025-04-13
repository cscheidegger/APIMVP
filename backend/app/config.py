from pydantic_settings import BaseSettings
from pydantic import PostgresDsn
from typing import Optional, List


class Settings(BaseSettings):
    API_V1_STR: str = "/api"
    PROJECT_NAME: str = "Proteus.lab API"

    # JWT
    SECRET_KEY: str = "insecure-secret-key-for-dev-only"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Database
    DATABASE_URL: Optional[PostgresDsn] = None

    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:5173"]

    # Uploads
    UPLOAD_DIR: str = "uploads"
    MAX_UPLOAD_SIZE: int = 50 * 1024 * 1024
    ALLOWED_EXTENSIONS: List[str] = [".stl", ".obj", ".3mf"]

    # Email
    EMAIL_ENABLED: bool = False
    EMAIL_SENDER: str = "noreply@proteuslab.com"
    SMTP_SERVER: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USERNAME: str = ""
    SMTP_PASSWORD: str = ""
    SMTP_USE_TLS: bool = True

    # Frontend
    FRONTEND_URL: str = "http://localhost:5173"

    # Google Drive
    GDRIVE_ENABLED: bool = False
    GDRIVE_FOLDER_ID: str = ""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()
