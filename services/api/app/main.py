"""FastAPI application entrypoint."""
from __future__ import annotations

import json
import logging
import os
from pathlib import Path
from typing import Any, Dict

import yaml
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from .config import settings
from .middleware import LoggingMiddleware, RateLimitStubMiddleware, RequestIDMiddleware
from .routers import accounts, leagues, live, players, projections, refresh, teams, trades, waivers

logger = logging.getLogger("gridiron.api")


def _contract_path() -> Path:
    """Resolve the OpenAPI contract location."""

    file_override = os.getenv("CONTRACTS_FILE")
    if file_override:
        candidate = Path(file_override)
        if candidate.exists():
            return candidate

    dir_override = os.getenv("CONTRACTS_DIR")
    if dir_override:
        candidate = Path(dir_override) / "openapi.yaml"
        if candidate.exists():
            return candidate

    repo_candidate = Path(__file__).resolve().parents[3] / "CONTRACTS" / "openapi.yaml"
    if repo_candidate.exists():
        return repo_candidate

    raise FileNotFoundError("openapi.yaml not found; ensure CONTRACTS/openapi.yaml is present")


def _load_contract() -> Dict[str, Any]:
    """Load the OpenAPI contract as a dictionary."""

    path = _contract_path()
    with path.open("r", encoding="utf-8") as handle:
        if path.suffix in {".yaml", ".yml"}:
            return yaml.safe_load(handle)
        return json.load(handle)


app = FastAPI(title="GridIron Sherlock API", version=settings.version, docs_url=None, redoc_url=None, openapi_url=None)


@app.on_event("startup")
async def configure_logging() -> None:
    logging.basicConfig(level=settings.log_level.upper(), format="%(message)s")


app.add_middleware(RequestIDMiddleware)
app.add_middleware(LoggingMiddleware)
app.add_middleware(RateLimitStubMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/healthz")
async def healthz() -> Dict[str, Any]:
    """Return service health metadata."""

    return {"status": "ok", "version": settings.version, "commit": settings.commit}


@app.get("/openapi.json", include_in_schema=False)
async def contract_spec() -> JSONResponse:
    """Serve the checked-in OpenAPI document."""

    return JSONResponse(_load_contract())


def _error_response(status_code: int, code: str, message: str, details: Any | None = None) -> JSONResponse:
    payload: Dict[str, Any] = {"error": {"code": code, "message": message}}
    if details is not None:
        payload["error"]["details"] = details
    return JSONResponse(status_code=status_code, content=payload)


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException) -> JSONResponse:
    message = exc.detail if isinstance(exc.detail, str) else str(exc.detail)
    code = f"http_{exc.status_code}"
    return _error_response(exc.status_code, code, message)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    return _error_response(422, "validation_error", "Validation failed", exc.errors())


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    logger.exception("Unhandled error", exc_info=exc)
    return _error_response(500, "internal_error", "Internal server error")


app.include_router(accounts.router)
app.include_router(leagues.router)
app.include_router(teams.router)
app.include_router(projections.router)
app.include_router(players.router)
app.include_router(waivers.router)
app.include_router(trades.router)
app.include_router(live.router)
app.include_router(refresh.router)


def custom_openapi() -> Dict[str, Any]:
    return _load_contract()


def get_app() -> FastAPI:
    """Return the configured FastAPI application."""

    return app


app.openapi = custom_openapi  # type: ignore[method-assign]
