from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "AzaPay API"
    DATABASE_URL: str  # Убедись, что используешь DATABASE_URL, а не database_name, database_user и т. д.
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYS: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    class Config:
        env_file = ".env"  # Подключение переменных окружения

settings = Settings()
