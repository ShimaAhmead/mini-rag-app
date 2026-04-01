from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[2]

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    
    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int


    model_config = SettingsConfigDict(
    env_file=BASE_DIR / "src" / ".env",
    env_file_encoding="utf-8",
)
    
def get_settings():
    return Settings()