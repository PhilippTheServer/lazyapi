"""Core configuration."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    app_name: str = "FastAPI"
    debug: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
