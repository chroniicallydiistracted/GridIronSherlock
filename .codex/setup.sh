#!/usr/bin/env bash
set -euo pipefail

# Optional setup script to help local dev
# - pins OpenAPI generator version
# - ensures node modules are installed

if command -v npm >/dev/null 2>&1; then
  npm run openapi:pin
fi

echo "codex setup complete"
