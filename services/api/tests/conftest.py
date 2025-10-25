from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from services.api.app.main import get_app


@pytest.fixture(scope="session")
def client() -> TestClient:
    with TestClient(get_app(), raise_server_exceptions=False) as test_client:
        yield test_client
