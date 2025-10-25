"""Trade endpoints."""
from __future__ import annotations

from fastapi import APIRouter

from .. import models as m
from .. import stubs

router = APIRouter(prefix="/v1", tags=["Trades"])


@router.post("/trades/estimate", response_model=m.TradeEstimateResponse)
async def estimate_trade(request: m.TradeEstimateRequest) -> m.TradeEstimateResponse:
    """Return a mock trade estimate."""

    return stubs.trade_estimate(request)
