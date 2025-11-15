from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    DATABASE_URL: str
    DEBUG: bool = False
    APP_TITLE: str = "QA API"

    class Config:
        env_file = str(Path(__file__).parent.parent / ".env")

settings = Settings()
