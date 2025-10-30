"""Projection endpoints."""
from __future__ import annotations

from fastapi import APIRouter

from .. import models as m
from .. import stubs

router = APIRouter(prefix="/v1", tags=["Projections"])


@router.get("/projections", response_model=m.ProjectionListResponse)
async def list_projections() -> m.ProjectionListResponse:
    """Return mock projections."""

    return stubs.projection_list()
