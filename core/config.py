from pydantic_settings import BaseSettings
from pydantic import AnyUrl
from typing import Optional


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    model_config = {
        "env_file": ".env",
        "case_sensitive": True,
    }


settings = Settings()
