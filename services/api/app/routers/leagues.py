"""League endpoints."""
from __future__ import annotations

from uuid import UUID

from fastapi import APIRouter

from .. import models as m
from .. import stubs

router = APIRouter(prefix="/v1", tags=["Leagues"])


@router.get("/leagues", response_model=m.LeagueListResponse)
async def list_leagues() -> m.LeagueListResponse:
    """Return a deterministic list of leagues for the current user."""

    return stubs.league_list()


@router.get("/leagues/{league_id}", response_model=m.LeagueDetail)
async def get_league(league_id: UUID) -> m.LeagueDetail:
    """Return the detail view for a specific league."""

    return stubs.league_detail(league_id)
