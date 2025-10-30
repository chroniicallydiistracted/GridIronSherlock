"""Structured logging middleware."""
from __future__ import annotations

import json
import logging
import time
from typing import Awaitable, Callable

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

from ..config import get_settings


class LoggingMiddleware(BaseHTTPMiddleware):
    """Emit JSON-structured request logs."""

    def __init__(self, app, logger: logging.Logger | None = None) -> None:  # type: ignore[override]
        super().__init__(app)
        self.logger = logger or logging.getLogger("gridiron.api")

    async def dispatch(self, request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:  # type: ignore[override]
        settings = get_settings()
        self.logger.setLevel(settings.log_level.upper())

        start = time.perf_counter()
        request_id = getattr(request.state, "request_id", None)
        try:
            response = await call_next(request)
        except Exception:
            duration_ms = (time.perf_counter() - start) * 1000
            payload = {
                "event": "request_error",
                "method": request.method,
                "path": request.url.path,
                "status": 500,
                "duration_ms": round(duration_ms, 2),
                "request_id": request_id,
            }
            self.logger.exception(json.dumps(payload))
            raise

        duration_ms = (time.perf_counter() - start) * 1000
        payload = {
            "event": "request_completed",
            "method": request.method,
            "path": request.url.path,
            "status": response.status_code,
            "duration_ms": round(duration_ms, 2),
            "request_id": request_id,
        }
        self.logger.info(json.dumps(payload))
        return response
