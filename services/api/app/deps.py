"""Common dependencies for request handlers."""
from __future__ import annotations

from typing import AsyncIterator

from .config import Settings, get_settings


async def get_db_session() -> AsyncIterator[None]:
    """Yield a placeholder database session.

    The real implementation will provide an AsyncSession connected to Neon.
    """

    yield None


def get_app_settings() -> Settings:
    """Expose cached application settings for dependency injection."""

    return get_settings()
