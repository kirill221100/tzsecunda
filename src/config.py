from functools import lru_cache
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_HOST: str
    API_KEY: str
    DEBUG: bool
    RELOAD: bool
    model_config = SettingsConfigDict(env_file=Path(__file__).parent.parent.resolve().joinpath('.env'))

@lru_cache
def get_config():
    return Config()

cfg = get_config()
