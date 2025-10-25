from __future__ import annotations

import importlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

SDK_ROOT = ROOT / "packages" / "sdk" / "python"
if str(SDK_ROOT) not in sys.path:
    sys.path.insert(0, str(SDK_ROOT))


def test_python_sdk_imports() -> None:
    # Import generated Python SDK configuration directly from file to avoid
    # importing heavy dependencies via package __init__ during smoke test.
    config_path = SDK_ROOT / "gridiron_sherlock_sdk" / "configuration.py"
    assert config_path.exists(), "configuration.py not found in generated SDK"
    spec = importlib.util.spec_from_file_location("gridiron_sherlock_sdk.configuration", str(config_path))
    assert spec and spec.loader
    config_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config_module)  # type: ignore[attr-defined]
    configuration_cls = getattr(config_module, "Configuration", None)
    assert configuration_cls is not None, "Configuration class missing from python SDK"

    client_config = configuration_cls()
    # openapi-generator python client exposes 'host' in Configuration
    assert hasattr(client_config, "host"), "Configuration instance missing host attribute"
