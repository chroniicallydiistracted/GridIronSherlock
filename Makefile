SHELL := /bin/bash

COMPOSE_FILE := docker-compose.dev.yml
COMPOSE := docker compose -f $(COMPOSE_FILE)
OPENAPI := CONTRACTS/openapi.yaml

# helper: source .env if present in bash commands
LOAD_ENV := set -o allexport; [ -f .env ] && source .env || true; set +o allexport;

.PHONY: help setup generate fmt lint type test e2e build migrate seed start dev clean

help:
    @printf "\nGridIronSherlock - Makefile targets\n\n"
    @printf "  setup     Install deps, create .env and start local infra\n"
    @printf "  generate  Generate SDKs from $(OPENAPI)\n"
    @printf "  fmt       Format code (prettier/black)\n"
    @printf "  lint      Run linters\n"
    @printf "  type      Run type checks\n"
    @printf "  test      Run unit and contract tests\n"
    @printf "  e2e       Run e2e tests (Playwright)\n"
    @printf "  build     Build web and API artifacts\n"
    @printf "  migrate   Run DB migrations (alembic)\n"
    @printf "  seed      Seed DB from db/seed\n"
    @printf "  start     Start infra (docker-compose)\n"
    @printf "  dev       Start dev servers (api + web)\n"
    @printf "  clean     Tear down infra and remove local artifacts\n\n"

setup:
    @echo "==> setup: creating dirs, copying .env.example -> .env (if missing), and bringing up infra"
    @bash -lc '$(LOAD_ENV); mkdir -p artifacts tmp ./tmp/r2; if [ ! -f .env ] && [ -f .env.example ]; then cp .env.example .env && echo "Copied .env.example -> .env (edit values)"; fi'
    @bash -lc '$(LOAD_ENV); $(COMPOSE) up -d --wait || $(COMPOSE) up -d'
    @bash -lc '$(LOAD_ENV); if [ -d apps/web ]; then echo "Installing web deps"; cd apps/web; if [ -f package-lock.json ]; then npm ci; elif [ -f yarn.lock ]; then yarn install; else npm install; fi; fi'
    @bash -lc '$(LOAD_ENV); if [ -d services/api ]; then echo "Installing python deps (services/api)"; if [ -f services/api/requirements-dev.txt ]; then python3 -m pip install --upgrade pip && python3 -m pip install -r services/api/requirements-dev.txt; elif [ -f services/api/pyproject.toml ]; then python3 -m pip install --upgrade pip && (cd services/api && python3 -m pip install -e .); else echo "No python requirements found at services/api"; fi; fi'
    @echo "==> setup complete (edit .env if required)"

generate:
    @bash -lc '$(LOAD_ENV); set -e; if [ ! -f "$(OPENAPI)" ]; then echo "$(OPENAPI) not found"; exit 1; fi; mkdir -p packages/sdk/typescript packages/sdk/python; docker run --rm -v "$$(pwd)":/local openapitools/openapi-generator-cli:v6.6.0 generate -i /local/$(OPENAPI) -g typescript-fetch -o /local/packages/sdk/typescript --skip-validate-spec || true; docker run --rm -v "$$(pwd)":/local openapitools/openapi-generator-cli:v6.6.0 generate -i /local/$(OPENAPI) -g python -o /local/packages/sdk/python --skip-validate-spec || true; echo "SDKs generated under packages/sdk/"'

fmt:
    @bash -lc '$(LOAD_ENV); if [ -d apps/web ]; then cd apps/web && if command -v npm >/dev/null 2>&1 && npm run fmt --silent >/dev/null 2>&1; then npm run fmt || true; elif command -v npx >/dev/null 2>&1; then npx prettier --write . || true; fi; fi; if [ -d services/api ]; then cd services/api && if command -v black >/dev/null 2>&1; then black . || true; fi; fi; echo "fmt complete"'

lint:
    @bash -lc '$(LOAD_ENV); if [ -d apps/web ]; then cd apps/web && if npm run lint --silent >/dev/null 2>&1; then npm run lint || true; elif command -v npx >/dev/null 2>&1 && [ -f .eslintrc* ]; then npx eslint . || true; fi; fi; if [ -d services/api ]; then cd services/api && if command -v ruff >/dev/null 2>&1; then ruff . || true; elif command -v flake8 >/dev/null 2>&1; then flake8 . || true; fi; fi; echo "lint complete"'

type:
    @bash -lc '$(LOAD_ENV); if [ -d apps/web ] && [ -f apps/web/tsconfig.json ]; then cd apps/web && if npm run type --silent >/dev/null 2>&1; then npm run type || true; elif command -v npx >/dev/null 2>&1; then npx tsc --noEmit || true; fi; fi; echo "type checks done"'

test:
    @bash -lc '$(LOAD_ENV); set -e; echo "Running backend tests"; if [ -d services/api ]; then cd services/api && pytest -q --maxfail=1; fi; echo "Running frontend tests"; if [ -d apps/web ] && [ -f apps/web/package.json ]; then cd apps/web && npm test --silent; fi; echo "Running contract tests"; if [ -d tests/contracts ]; then pytest -q tests/contracts; fi; echo "all tests completed"'

e2e:
    @bash -lc '$(LOAD_ENV); set -e; $(COMPOSE) up -d; sleep 3; if [ -d apps/web ]; then cd apps/web && if npm run test:e2e --silent >/dev/null 2>&1; then npm run test:e2e || true; elif command -v npx >/dev/null 2>&1 && [ -d tests/e2e ]; then npx playwright test || true; fi; fi'

build:
    @bash -lc '$(LOAD_ENV); if [ -d apps/web ]; then cd apps/web && npm run build || true; fi; if [ -d services/api ]; then docker build -t gridiron-sherlock-api services/api || true; fi; echo "build complete"'

migrate:
    @bash -lc '$(LOAD_ENV); if [ -d services/api/alembic ]; then cd services/api && alembic upgrade head || echo "alembic not available or failed"; else echo "no alembic migrations found"; fi'

seed:
    @bash -lc '$(LOAD_ENV); if [ -d db/seed ]; then for f in db/seed/*.sql; do echo "Seeding $$f"; psql "$$DATABASE_URL" -f "$$f" || echo "psql failed for $$f"; done; else echo "no db/seed directory"; fi'

start:
    @bash -lc '$(LOAD_ENV); $(COMPOSE) up -d; $(COMPOSE) ps; echo "infra started (use make dev to run services locally)"'

dev:
    @bash -lc '$(LOAD_ENV); (cd services/api && uvicorn services.api.main:app --reload --host 0.0.0.0 --port $${PORT_API:-8000}) & (cd apps/web && npm run dev) ; wait'

clean:
    @bash -lc '$(LOAD_ENV); $(COMPOSE) down -v; rm -rf node_modules apps/web/.next services/api/.venv .pytest_cache .coverage artifacts tmp packages/sdk/* || true'
