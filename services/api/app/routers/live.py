"""Live streaming endpoints."""
from __future__ import annotations

from typing import AsyncIterator

from fastapi import APIRouter
from starlette.responses import StreamingResponse

router = APIRouter(prefix="/v1", tags=["Live"])

_SYNTHETIC_EVENT = '{"type":"synthetic","ts":1700000000}'


async def _event_stream() -> AsyncIterator[str]:
    yield f"data: {_SYNTHETIC_EVENT}\n\n"


@router.get("/live/stream")
async def stream_live_impacts() -> StreamingResponse:
    """Return a single synthetic live impact event."""

    return StreamingResponse(_event_stream(), media_type="text/event-stream")
