from pydantic import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    API_V1_STR: str = "/api"
    PROJECT_NAME: str = "ReqRes API Clone"

    # CORS Configuration
    BACKEND_CORS_ORIGINS: list[str] = ["*"]

    # API Documentation
    DOCS_URL: str = "/docs"
    REDOC_URL: str = "/redoc"
    OPENAPI_URL: str = "/openapi.json"

    # Support Information
    SUPPORT_URL: str = "https://contentcaddy.io"
    SUPPORT_TEXT: str = "Tired of writing endless social media content? Let Content Caddy generate it for you."

    class Config:
        case_sensitive = True


settings = Settings()
