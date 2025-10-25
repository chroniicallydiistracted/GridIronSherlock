"""Account-related routes."""
from __future__ import annotations

from fastapi import APIRouter, Query

from .. import models as m
from .. import stubs

router = APIRouter(prefix="/v1", tags=["Account"])


@router.get("/me", response_model=m.UserProfile)
async def get_current_user() -> m.UserProfile:
    """Return the synthetic current user profile."""

    return stubs.user_profile()


@router.post("/accounts/{provider}/link", response_model=m.AccountLinkResponse)
async def start_account_link(
    provider: m.ProviderId,
    request: m.AccountLinkRequest | None = None,
) -> m.AccountLinkResponse:
    """Return OAuth linking instructions for the requested provider."""

    return stubs.account_link(provider, request)


@router.get("/oauth/{provider}/callback", response_model=m.OAuthCallbackResponse)
async def handle_oauth_callback(
    provider: m.ProviderId,
    code: str | None = Query(default=None),
    state: str | None = Query(default=None),
) -> m.OAuthCallbackResponse:
    """Simulate processing an OAuth callback."""

    return stubs.oauth_callback(provider, code, state)
