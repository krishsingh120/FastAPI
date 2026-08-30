from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str
    mongo_url: str
    database_name: str
    port: int

    model_config = SettingsConfigDict(
        env_file=".env"
    )


settings = Settings()