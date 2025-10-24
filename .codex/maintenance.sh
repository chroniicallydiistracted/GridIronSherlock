#!/usr/bin/env bash
set -euo pipefail

if [ -f package.json ]; then
  if [ -f pnpm-lock.yaml ]; then pnpm install || true; fi
  if [ -f yarn.lock ]; then yarn install || true; fi
  if [ -f package-lock.json ]; then npm ci || npm install || true; fi
fi

if [ -f pyproject.toml ]; then
  if command -v uv >/dev/null 2>&1; then uv pip install -r requirements.txt || true; fi
  if command -v poetry >/dev/null 2>&1; then poetry install || true; fi
  if [ -f requirements.txt ]; then pip install -r requirements.txt || true; fi
fi

if [ -f Makefile ]; then
  make lint || true
  make test || true
fi
