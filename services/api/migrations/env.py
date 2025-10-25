"""Alembic environment placeholder."""
from __future__ import annotations

from alembic import context

# config = context.config  # noqa: ERA001


def run_migrations_offline() -> None:
    """Run migrations in offline mode (no-op stub)."""

    pass


def run_migrations_online() -> None:
    """Run migrations in online mode (no-op stub)."""

    pass


def run_migrations() -> None:
    """Entry point for Alembic (no-op)."""

    pass


if context.is_offline_mode():  # type: ignore[attr-defined]
    run_migrations_offline()
else:
    run_migrations_online()
