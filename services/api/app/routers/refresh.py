"""Refresh endpoints."""
from __future__ import annotations

from fastapi import APIRouter, status

from .. import models as m
from .. import stubs

router = APIRouter(prefix="/v1", tags=["Refresh"])


@router.post(
    "/refresh/{scope}",
    response_model=m.RefreshResponse,
    status_code=status.HTTP_202_ACCEPTED,
)
async def trigger_refresh(
    scope: m.ScopeId,
    request: m.RefreshRequest | None = None,
) -> m.RefreshResponse:
    """Return a stub refresh acknowledgement."""

    return stubs.refresh(scope, request)
