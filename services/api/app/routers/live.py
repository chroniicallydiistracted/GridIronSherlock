"""Live streaming endpoints."""
from __future__ import annotations

import json
from typing import AsyncIterator

from fastapi import APIRouter
from starlette.responses import StreamingResponse

router = APIRouter(prefix="/v1", tags=["Live"])


async def _event_stream() -> AsyncIterator[str]:
    # Minimal synthetic payload used by contract smoke tests.
    payload = {"type": "synthetic", "ts": 1700000000}
    yield f"data: {json.dumps(payload)}\n\n"


@router.get("/live/stream")
async def stream_live_impacts() -> StreamingResponse:
    """Return a single contract-shaped live impact event via SSE."""
    return StreamingResponse(
        _event_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        },
    )
