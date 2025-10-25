"""
Import shim for local SDK development.

Allows `python -c "import gridiron_sherlock_sdk"` to succeed without
installing the generated package, by exposing the generated module's
attributes when available.
"""
from __future__ import annotations

import importlib.util
import os
import sys

_ROOT = os.path.dirname(os.path.abspath(__file__))
_GEN_DIR = os.path.join(_ROOT, "packages", "sdk", "python", "gridiron_sherlock_sdk")

try:
    init_path = os.path.join(_GEN_DIR, "__init__.py")
    if os.path.isfile(init_path):
        spec = importlib.util.spec_from_file_location(
            "_gridiron_sherlock_sdk_generated", init_path
        )
        if spec and spec.loader:
            mod = importlib.util.module_from_spec(spec)
            sys.modules[spec.name] = mod
            spec.loader.exec_module(mod)  # type: ignore[attr-defined]
            # Re-export public attributes into this shim module
            for k, v in mod.__dict__.items():
                if not k.startswith("_"):
                    globals()[k] = v
except Exception:
    # Best-effort shim; ignore if not available
    pass

