"""Database session stubs."""
from __future__ import annotations

from contextlib import asynccontextmanager
from typing import AsyncIterator, Optional

from ..config import settings


@asynccontextmanager
async def session_scope() -> AsyncIterator[None]:
    """Yield a placeholder async session.

    Once database integration is added this will provide an AsyncSession
    connected to the configured Neon instance.
    """

    yield None


async def get_session() -> AsyncIterator[None]:
    """FastAPI dependency wrapper for :func:`session_scope`."""

    async with session_scope() as session:
        yield session


def database_url() -> Optional[str]:
    """Return the configured database URL if available."""

    return settings.neon_database_url
