from typing import Any, Dict

from pydantic import (
    PostgresDsn,
    SecretStr,
    root_validator,
)
from pydantic_settings import BaseSettings

DictStrAny = Dict[str, Any]


class Settings(BaseSettings):

    # --- database -- #

    POSTGRES_USER: str
    POSTGRES_PASSWORD: SecretStr
    POSTGRES_SERVER: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URL: PostgresDsn

    @root_validator(pre=True)
    def generate_sqlalchemy_database_url(cls, values: DictStrAny) -> DictStrAny:
        if not values.get("SQLALCHEMY_DATABASE_URL"):
            value = PostgresDsn.build(
                scheme="postgresql",
                # user=values.get("POSTGRES_USER"),
                password=values.get("POSTGRES_PASSWORD"),
                host=values.get("POSTGRES_SERVER"),
                path=f"/{values.get('POSTGRES_DB')}",
            )
            values["SQLALCHEMY_DATABASE_URL"] = value
        return values


settings = Settings()
