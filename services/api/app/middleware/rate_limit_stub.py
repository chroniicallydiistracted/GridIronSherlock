"""Rate limiting stub middleware."""
from __future__ import annotations

from typing import Awaitable, Callable

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response


class RateLimitStubMiddleware(BaseHTTPMiddleware):
    """Attach placeholder rate limit headers without enforcing quotas."""

    def __init__(self, app, limit: int = 1000) -> None:  # type: ignore[override]
        super().__init__(app)
        self.limit = limit

    async def dispatch(self, request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:  # type: ignore[override]
        response = await call_next(request)
        response.headers.setdefault("x-ratelimit-limit", str(self.limit))
        response.headers.setdefault("x-ratelimit-remaining", str(self.limit))
        response.headers.setdefault("x-ratelimit-reset", "0")
        return response
