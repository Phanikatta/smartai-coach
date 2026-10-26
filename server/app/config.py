from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "SmartAI Coach"
    environment: str = "development"
    debug: bool = False

    database_url: str

    jwt_secret: str
    jwt_expire_minutes: int = 60

    llm_provider: str = "groq"
    llm_api_key: str = ""

    embedding_model: str = "BAAI/bge-small-en-v1.5"

    max_upload_mb: int = 20
    max_pages_per_doc: int = 200
    max_documents_total: int = 100
    max_uploads_per_admin_per_day: int = 20
    max_question_chars: int = 1000
    rate_limit_questions_per_min: int = 10

    cors_origins: str = "http://localhost:5173"

    @property
    def cors_origin_list(self) -> list[str]:
        return [o.strip() for o in self.cors_origins.split(",") if o.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()