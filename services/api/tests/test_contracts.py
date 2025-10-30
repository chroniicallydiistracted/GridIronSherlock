from __future__ import annotations

import copy
from pathlib import Path
from typing import Any, Dict, Tuple

import yaml
from fastapi.testclient import TestClient
from jsonschema import Draft202012Validator, RefResolver

from services.api.app import models as m

SPEC_PATH = Path(__file__).resolve().parents[3] / "CONTRACTS" / "openapi.yaml"

LEAGUE_ID = "00000000-0000-0000-0000-000000000001"
TEAM_ID = "00000000-0000-0000-0000-000000000002"
OPP_TEAM_ID = "00000000-0000-0000-0000-000000000003"
PLAYER_ID = "00000000-0000-0000-0000-000000000004"

PARAM_VALUES: Dict[str, str] = {
    "provider": m.ProviderId.espn.value,
    "leagueId": LEAGUE_ID,
    "teamId": TEAM_ID,
    "playerId": PLAYER_ID,
    "scope": m.ScopeId.players.value,
}

ACCOUNT_LINK_REQUEST = m.AccountLinkRequest(scopes=["league.read"]).model_dump(mode="json")
OPTIMIZATION_REQUEST = m.OptimizationRequest(
    period=m.ScoringPeriod(season=2024, week=8),
    objective=m.OptimizationObjective(focus=m.Focus.balanced),
).model_dump(mode="json")
TRADE_REQUEST = m.TradeEstimateRequest(
    leagueId=LEAGUE_ID,
    fromTeamId=TEAM_ID,
    toTeamId=OPP_TEAM_ID,
    offer=[m.TradeAsset(type=m.Type.player, id="offer-player", teamId=TEAM_ID)],
    request=[m.TradeAsset(type=m.Type.player, id="request-player", teamId=OPP_TEAM_ID)],
).model_dump(mode="json")
REFRESH_REQUEST = m.RefreshRequest(leagueId=LEAGUE_ID, force=True).model_dump(mode="json")

REQUEST_CONFIG: Dict[Tuple[str, str], Dict[str, Any]] = {
    ("post", "/accounts/{provider}/link"): {"json": ACCOUNT_LINK_REQUEST},
    ("post", "/teams/{teamId}/optimize"): {"json": OPTIMIZATION_REQUEST},
    ("post", "/trades/estimate"): {"json": TRADE_REQUEST},
    ("post", "/refresh/{scope}"): {"json": REFRESH_REQUEST},
    ("get", "/oauth/{provider}/callback"): {"params": {"code": "sample", "state": "nonce"}},
}

EXPECTED_STATUS: Dict[Tuple[str, str], int] = {
    ("post", "/refresh/{scope}"): 202,
}


def _load_spec() -> Dict[str, Any]:
    return yaml.safe_load(SPEC_PATH.read_text(encoding="utf-8"))


def _format_path(template: str) -> str:
    path = template
    for name, value in PARAM_VALUES.items():
        path = path.replace(f"{{{name}}}", value)
    return f"/v1{path}"


def _normalize_nullable(schema: Any) -> Any:
    if isinstance(schema, dict):
        normalized: Dict[str, Any] = {}
        for key, value in schema.items():
            if key == "nullable":
                continue
            normalized[key] = _normalize_nullable(value)

        if schema.get("nullable"):
            type_value = normalized.get("type")
            if isinstance(type_value, list):
                if "null" not in type_value:
                    normalized["type"] = [*type_value, "null"]
            elif isinstance(type_value, str):
                normalized["type"] = [type_value, "null"]
            elif "$ref" in normalized:
                normalized = {"anyOf": [normalized, {"type": "null"}]}
            else:
                normalized["type"] = ["null"]

        return normalized

    if isinstance(schema, list):
        return [_normalize_nullable(item) for item in schema]

    return schema


def _success_response(operation: Dict[str, Any]) -> Tuple[int, Dict[str, Any]] | None:
    for status_code, response in operation.get("responses", {}).items():
        if not status_code.startswith("2"):
            continue
        content = response.get("content", {})
        json_content = content.get("application/json")
        if not json_content:
            continue
        schema = json_content.get("schema")
        if schema:
            return int(status_code), schema
    return None


def test_contract_responses_match_schema(client: TestClient) -> None:
    raw_spec = _load_spec()
    spec = _normalize_nullable(copy.deepcopy(raw_spec))
    resolver = RefResolver(base_uri=f"file://{SPEC_PATH.resolve()}", referrer=spec)

    for raw_path, methods in spec["paths"].items():
        for method, operation in methods.items():
            key = (method.lower(), raw_path)
            if key == ("get", "/live/stream"):
                continue

            success = _success_response(operation)
            if success is None:
                continue

            default_status, schema = success
            expected_status = EXPECTED_STATUS.get(key, default_status)
            url = _format_path(raw_path)
            request_kwargs = REQUEST_CONFIG.get(key, {})
            response = client.request(method, url, **request_kwargs)
            assert response.status_code == expected_status, f"{method.upper()} {url}"

            payload = response.json()
            Draft202012Validator(schema, resolver=resolver).validate(payload)
