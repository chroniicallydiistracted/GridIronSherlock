"""Team endpoints."""
from __future__ import annotations

from uuid import UUID

from fastapi import APIRouter

from .. import models as m
from .. import stubs

router = APIRouter(prefix="/v1", tags=["Teams"])


@router.get("/teams/{team_id}/lineup", response_model=m.TeamLineupResponse)
async def get_team_lineup(team_id: UUID) -> m.TeamLineupResponse:
    """Return a synthetic lineup for the specified team."""

    return stubs.team_lineup(team_id)


@router.post("/teams/{team_id}/optimize", response_model=m.OptimizationResponse)
async def optimize_team_lineup(
    team_id: UUID,
    request: m.OptimizationRequest,
) -> m.OptimizationResponse:
    """Return a fake optimization result."""

    return stubs.optimize_lineup(team_id, request)
