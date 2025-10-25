"""Application configuration for the API service."""
from __future__ import annotations

from functools import lru_cache
from importlib import metadata
from typing import Literal, Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


def _package_version() -> str:
    """Return the installed package version or a development marker."""

    try:
        return metadata.version("gridiron-sherlock-api")
    except metadata.PackageNotFoundError:  # pragma: no cover - occurs in dev installs
        return "0.0.0"


class Settings(BaseSettings):
    """Runtime configuration loaded from environment variables."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_env: Literal["development", "staging", "production"] | str = Field(
        default="development", alias="APP_ENV"
    )
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")
    version: str = Field(default_factory=_package_version, alias="APP_VERSION")
    commit: str = Field(default="dev", alias="GIT_COMMIT")
    neon_database_url: Optional[str] = Field(default=None, alias="NEON_DATABASE_URL")


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return a cached settings instance."""

    return Settings()


settings = get_settings()
