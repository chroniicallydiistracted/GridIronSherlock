from __future__ import annotations

from fastapi.testclient import TestClient


def test_healthz(client: TestClient) -> None:
    response = client.get("/healthz")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert payload["version"]
    assert payload["commit"]


def test_error_envelope_on_404(client: TestClient) -> None:
    response = client.get("/v1/not-a-real-route")
    assert response.status_code == 404
    body = response.json()
    assert body["error"]["code"] == "http_404"
    assert body["error"]["message"]
