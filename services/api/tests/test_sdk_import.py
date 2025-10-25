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
    config_module = importlib.import_module("packages.sdk.python.openapi_client.configuration")
    configuration_cls = getattr(config_module, "Configuration", None)
    assert configuration_cls is not None, "Configuration class missing from python SDK"

    client_config = configuration_cls()
    assert hasattr(client_config, "host"), "Configuration instance missing host attribute"

