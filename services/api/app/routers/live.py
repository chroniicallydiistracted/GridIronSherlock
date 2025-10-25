"""Live streaming endpoints."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import AsyncIterator, Any, Dict

from fastapi import APIRouter
from starlette.responses import StreamingResponse

# Prefer using the contract-shaped stub if available
try:
    from app.stubs import live_event  # returns a LiveImpactEvent-like object
except Exception:  # pragma: no cover
    live_event = None  # type: ignore

router = APIRouter(prefix="/v1", tags=["Live"])


def _build_contract_event() -> Dict[str, Any]:
    """Return a contract-shaped LiveImpactEvent payload."""
    payload: Dict[str, Any]
    if callable(live_event):
        evt = live_event()
        if hasattr(evt, "model_dump"):
            payload = evt.model_dump(mode="json")  # pydantic v2
        elif hasattr(evt, "dict"):
            payload = evt.dict()  # pydantic v1
        elif isinstance(evt, dict):
            payload = evt
        else:
            payload = {}
    else:
        payload = {}

    # Ensure required fields exist even if stub changed
    now = datetime.now(timezone.utc).isoformat()
    payload.setdefault("eventId", "synthetic-1")
    payload.setdefault("gameId", "SYN-000")
    payload.setdefault("playId", "SYN-0")
    payload.setdefault("occurredAt", now)
    payload.setdefault("impactType", "synthetic")
    return payload


async def _event_stream() -> AsyncIterator[str]:
    evt = _build_contract_event()
    event_id = str(evt.get("eventId", "synthetic-1"))
    data = json.dumps(evt, separators=(",", ":"))
    # Emit a single SSE frame
    yield f"id: {event_id}\nevent: impact\ndata: {data}\n\n"


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
