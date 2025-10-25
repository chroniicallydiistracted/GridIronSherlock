"""Player endpoints."""
from __future__ import annotations

from uuid import UUID

from fastapi import APIRouter

from .. import models as m
from .. import stubs

router = APIRouter(prefix="/v1", tags=["Players"])


@router.get("/players", response_model=m.PlayerListResponse)
async def search_players() -> m.PlayerListResponse:
    """Return mock player search results."""

    return stubs.player_list()


@router.get("/players/{player_id}", response_model=m.PlayerDetail)
async def get_player(player_id: UUID) -> m.PlayerDetail:
    """Return mock player detail."""

    return stubs.player_detail(player_id)
