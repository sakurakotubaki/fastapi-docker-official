import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = os.getenv(
        "DATABASE_URL", "postgresql://postgres:postgres@db:5432/fastapi_db"
    )
    jwt_secret_key: str = os.getenv(
        "JWT_SECRET_KEY", "your-super-secret-key-change-in-production"
    )
    jwt_algorithm: str = os.getenv("JWT_ALGORITHM", "HS256")
    jwt_expire_minutes: int = int(os.getenv("JWT_EXPIRE_MINUTES", "30"))

    class Config:
        env_file = ".env"


settings = Settings()
