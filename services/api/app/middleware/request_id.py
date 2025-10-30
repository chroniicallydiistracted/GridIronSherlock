"""Request ID middleware."""
from __future__ import annotations

import uuid
from typing import Awaitable, Callable

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response


HEADER_NAME = "x-request-id"


class RequestIDMiddleware(BaseHTTPMiddleware):
    """Attach a request identifier to the request state and response headers."""

    async def dispatch(self, request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:  # type: ignore[override]
        request_id = request.headers.get(HEADER_NAME, str(uuid.uuid4()))
        request.state.request_id = request_id
        response = await call_next(request)
        response.headers.setdefault(HEADER_NAME, request_id)
        return response
