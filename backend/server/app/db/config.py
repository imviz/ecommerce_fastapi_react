from typing import Any, Dict, List, Optional, Union

from pydantic import (
    AnyHttpUrl,
    BaseSettings,
    PostgresDsn,
    SecretStr,
    root_validator,
    validator,
)

# from pydantic_settings import BaseSettings

DictStrAny = Dict[str, Any]


class Settings(BaseSettings):

    # --- server --- #

    SERVER_PORT: int = 8080
    UI_PORT: Optional[int] = None

    API_PREFIX: str = "api"

    SERVER_TLS: bool = False
    PROJECT_DOMAIN_URL: AnyHttpUrl = ""  # Generated

    @validator("PROJECT_DOMAIN_URL", always=True, pre=True)
    def generate_project_domain(cls, _, values: DictStrAny) -> AnyHttpUrl:
        protocol = "https" if values.get("SERVER_TLS") else "http"
        ui_port = "" if values.get("SERVER_TLS") else values.get("UI_PORT")
        port_suffix = f":{ui_port}" if ui_port else ""
        domain_url = f"{protocol}://{values.get('PROJECT_DOMAIN')}{port_suffix}"
        return domain_url

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def valid_cors_origins(cls, value: Union[str, List[str]]) -> Union[str, List[str]]:
        if isinstance(value, str) and not value.startswith("["):
            return [i.strip() for i in value.split(",")]
        elif isinstance(value, (list, str)):
            return value
        raise ValueError(value)

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
                user=values.get("POSTGRES_USER"),
                password=values.get("POSTGRES_PASSWORD"),
                host=values.get("POSTGRES_SERVER"),
                path=f"/{values.get('POSTGRES_DB')}",
            )
            values["SQLALCHEMY_DATABASE_URL"] = value
        return values

    # FIRST_SUPERUSER_NAME: str
    # FIRST_SUPERUSER_EMAIL: EmailStr
    # FIRST_SUPERUSER_PASSWORD: SecretStr

    # # Token life
    # ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    # REFRESH_TOKEN_EXPIRE_MINUTES: int = 15

    # # Blob Storage
    # BLOB_ACCOUNT_NAME: str
    # BLOB_CONNECTION_STRING: str
    # BLOB_ACCOUNT_KEY: SecretStr
    # BLOB_ACCOUNT_URL: HttpUrl
    # BLOB_CONTAINER_NAME: str

    # # S3 bucket
    # AWS_SECRET_ACCESS_KEY: SecretStr
    # AWS_ACCESS_KEY_ID: str
    # AWS_REGION: str
    # AWS_S3_BUCKET_NAME: str

    # # Sharepoint
    # SHAREPOINT_USERNAME: str = "notficationsv@genproresearch.net"
    # SHAREPOINT_PASSWORD: SecretStr
    # SHAREPOINT_SITE: str = "https://genprolifesciences.sharepoint.com/sites/tsl/PT/dt"
    # SHAREPOINT_SITE_NAME: str = "tsl/PT/dt"
    # SHAREPOINT_DOC: str = "Shared Documents"
    # ROOT_FOLDER_NAME: str = "Dsur"

    # # JWT_KEY: str
    # JWT_ALGORITH = "HS256"

    # TRIGGER_TIMEOUT: int

    # # SCOPES AND USER TYPES
    # SCOPE_USER = "dsur:user"
    # SCOPE_MANAGER = "dsur:manager"
    # SCOPE_ADMIN = "dsur:admin"
    # INTERNAL_LOGIN_METHOD = "internal"
    # MICROSOFT_LOGIN_METHOD = "microsoft_login_method"
    # SCOPES = {
    #     SCOPE_USER: "Access users",
    #     SCOPE_MANAGER: "Access for managers",
    #     SCOPE_ADMIN: "Access for admins",
    # }

    # # filter config
    # FILTER_CONFIG_FILE: str = "/app/list_filter.yaml"
    # # --- SSO --- #

    # # Microsoft SSO
    # MS_CLIENT_ID: Optional[str]
    # MS_CLIENT_SECRET: SecretStr = ""
    # MS_TENANT_ID: Optional[str]
    # MS_REDIRECT_ENDPOINT: Optional[str]
    # MS_AUTHORITY: Optional[HttpUrl] = None  # Generated
    # MS_REDIRECT_URI: Optional[AnyHttpUrl] = None  # Generated
    # ENABLE_MS_SSO: bool  # Generated. To enable/disable, use features.

    # @root_validator(pre=True)
    # def valid_ms_sso_fields(cls, values: DictStrAny) -> DictStrAny:
    #     required_keys = {
    #         "MS_CLIENT_ID",
    #         "MS_CLIENT_SECRET",
    #         "MS_TENANT_ID",
    #         "MS_REDIRECT_ENDPOINT",
    #     }
    #     missing_keys = required_keys - values.keys()
    #     given_keys = required_keys - missing_keys

    #     if missing_keys and given_keys:
    #         # Remove all set keys if only some required keys are set
    #         for k in given_keys:
    #             del values[k]
    #     # The feature will be unavailable if there is a missing key
    #     values["ENABLE_MS_SSO"] = not missing_keys

    #     return values

    # @validator("MS_AUTHORITY", always=True)
    # def valid_ms_authority(cls, _: HttpUrl, values: DictStrAny) -> Optional[HttpUrl]:
    #     tenant_id = values.get("MS_TENANT_ID")
    #     if not tenant_id:
    #         return None
    #     return parse_obj_as(HttpUrl, f"https://login.microsoftonline.com/{tenant_id}")

    # @validator("MS_REDIRECT_URI", always=True)
    # def valid_redirect_uri(
    #     cls, _: AnyHttpUrl, values: DictStrAny
    # ) -> Optional[AnyHttpUrl]:
    #     redirect_endpoint = values.get("MS_REDIRECT_ENDPOINT")
    #     if not redirect_endpoint:
    #         return None
    #     domain_url = values.get("PROJECT_DOMAIN_URL")
    #     return parse_obj_as(AnyHttpUrl, f"{domain_url}{redirect_endpoint}")

    # # Worker
    # WORKER_API_USER: str
    # WORKER_API_PASSWORD: SecretStr

    # # Permission types
    # PERMISSION_GET = "get"
    # PERMISSION_DELETE = "delete"
    # PERMISSION_EDIT = "edit"
    # PERMISSION_ALL = "all"

    # # environment
    # ENV: str
    # # SENTRY
    # CARS_SENTRY_DSN: AnyHttpUrl = None
    # CARS_SENTRY_TEAM: str = None
    # USER: str = None
    # GIT_BRANCH: str = None
    # LAST_PULLED_DATE: str = None

    # # Redis Cache for Server
    # SERVER_CACHE_STORAGE_URL: str

    # # Smart-Mapping
    # SMART_MAPPING_URL: HttpUrl
    # SMART_MAPPING_API_USER: str
    # SMART_MAPPING_API_PASSWORD: SecretStr
    # SMART_MAPPING_MIN_RATIO: float

    # # Sync folders
    # SYNC_FOLDER_CACHE_EXPIRE_IN_SECONDS: int = 30

    # # Server
    # SERVER_LOCK_URL: str
    # LOCK_EXPIRY: int
    # LOCK_RAISE_EXCEPTION_AFTER_SEC: int

    # EXPORT_WORKER_TIMEOUT: int


settings = Settings()
