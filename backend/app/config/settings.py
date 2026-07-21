from pydantic_settings import BaseSettings
from urllib.parse import quote_plus


class Settings(BaseSettings):
    APP_NAME: str
    VERSION: str
    ENVIRONMENT: str

    SECRET_KEY: str
    GROQ_API_KEY: str
    UPLOAD_FOLDER: str = "uploads/resumes"
    MAX_FILE_SIZE: int = 10 * 1024 * 1024  # 10 MB
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    model_config = {
        "env_file": ".env",
        "extra": "ignore"
    }

    @property
    def DATABASE_URL(self):
        password = quote_plus(self.DB_PASSWORD)
        return (
            f"postgresql://{self.DB_USER}:{password}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )


settings = Settings()