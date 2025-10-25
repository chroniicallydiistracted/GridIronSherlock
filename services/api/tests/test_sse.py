from __future__ import annotations

import json

from fastapi.testclient import TestClient


def test_sse_stream_emits_single_event(client: TestClient) -> None:
    response = client.get("/v1/live/stream")
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/event-stream")

    chunks = [line for line in response.text.splitlines() if line]
    data_lines = [line for line in chunks if line.startswith("data: ")]
    assert data_lines, "expected at least one data line"

    payload = json.loads(data_lines[0].removeprefix("data: "))
    assert payload == {"type": "synthetic", "ts": 1700000000}
