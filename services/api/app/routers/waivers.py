"""Waiver endpoints."""
from __future__ import annotations

from fastapi import APIRouter

from .. import models as m
from .. import stubs

router = APIRouter(prefix="/v1", tags=["Waivers"])


@router.get("/waivers", response_model=m.WaiverListResponse)
async def list_waivers() -> m.WaiverListResponse:
    """Return mock waiver recommendations."""

    return stubs.waiver_list()
