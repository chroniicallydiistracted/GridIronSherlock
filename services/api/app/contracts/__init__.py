"""Embedded contract artifacts for runtime access."""

from __future__ import annotations

from importlib import resources
from pathlib import Path


def openapi_path() -> Path:
    """Return path to the embedded OpenAPI document."""

    return Path(resources.files(__package__) / "openapi.yaml")
