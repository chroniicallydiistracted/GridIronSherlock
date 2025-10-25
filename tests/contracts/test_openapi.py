import hashlib
import json
from pathlib import Path
from typing import Any, Dict

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
OPENAPI_PATH = REPO_ROOT / "CONTRACTS" / "openapi.yaml"
SCHEMA_DIR = REPO_ROOT / "CONTRACTS" / "schemas"
SNAPSHOT_PATH = REPO_ROOT / "CONTRACTS" / "snapshots" / "openapi.sha256"


def _load_openapi() -> Dict[str, Any]:
    with OPENAPI_PATH.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def test_openapi_version_and_metadata() -> None:
    doc = _load_openapi()
    assert doc["openapi"] == "3.1.0"
    info = doc["info"]
    assert info["title"] == "GridIron Sherlock API"
    assert info["version"] == "1.0.0"
    assert doc["servers"], "OpenAPI document must declare servers"
    assert doc["components"]["schemas"], "Expected component schemas"


def test_component_schemas_have_mirrors() -> None:
    doc = _load_openapi()
    for name, schema in sorted(doc["components"]["schemas"].items()):
        schema_path = SCHEMA_DIR / f"{name}.json"
        assert schema_path.exists(), f"Missing schema file for {name}"
        with schema_path.open("r", encoding="utf-8") as fh:
            disk_schema = json.load(fh)
        assert disk_schema == schema, f"Schema mismatch for {name}"


@pytest.mark.parametrize("path_key", sorted(_load_openapi()["paths"].keys()))
def test_responses_reference_known_components(path_key: str) -> None:
    doc = _load_openapi()
    path_item = doc["paths"][path_key]
    for method, operation in path_item.items():
        if method.startswith("x-"):
            continue
        responses = operation.get("responses", {})
        assert responses, f"{path_key} {method} missing responses"
        for response_def in responses.values():
            content = response_def.get("content", {})
            for media in content.values():
                schema = media.get("schema")
                assert schema is not None, f"{path_key} {method} response missing schema"
                ref = schema.get("$ref")
                if ref:
                    component = ref.split("/")[-1]
                    assert (
                        component in doc["components"]["schemas"]
                    ), f"{path_key} {method} references unknown schema {component}"


def test_openapi_snapshot_hash_matches_file() -> None:
    doc = _load_openapi()
    serialized = json.dumps(doc, sort_keys=True).encode("utf-8")
    digest = hashlib.sha256(serialized).hexdigest()
    with SNAPSHOT_PATH.open("r", encoding="utf-8") as fh:
        expected = fh.read().strip()
    assert digest == expected, "OpenAPI snapshot hash mismatch"
