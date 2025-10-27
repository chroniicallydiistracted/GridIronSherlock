SHELL := /bin/bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c

COMPOSE_FILE := docker-compose.dev.yml
COMPOSE := docker compose -f $(COMPOSE_FILE)
OPENAPI := CONTRACTS/openapi.yaml

# Only source .env when all non-comment, non-empty lines are KEY=VALUE (and no '<...>' placeholders)
LOAD_ENV := set -o allexport; \
	if [ -f .env ]; then \
		clean=1; \
		while IFS= read -r line; do \
			case "$$line" in \
				""|"#"*) ;; \
				*"<"*) clean=0 ;; \
				[A-Za-z_]*=*) ;; \
				*) clean=0 ;; \
			esac; \
		done < .env; \
		if [ "$$clean" -eq 1 ]; then . .env; fi; \
	fi; \
	set +o allexport;

.PHONY: help openapi setup generate maybe-generate fmt lint type test api.run e2e build migrate seed start dev clean smoke

help:
	@printf "\nGridIronSherlock - Makefile targets\n\n"
	@printf "  setup     Install deps and prepare workspace (no Docker start)\n"
	@printf "  start     Start local infra (docker compose up -d)\n"
	@printf "  generate  Generate SDKs from $(OPENAPI)\n"
	@printf "  fmt       Format code (prettier/black)\n"
	@printf "  lint      Run linters\n"
	@printf "  type      Run type checks\n"
	@printf "  test      Run unit and contract tests\n"
	@printf "  e2e       Run e2e tests (Playwright)\n"
	@printf "  build     Build web and API artifacts\n"
	@printf "  migrate   Run DB migrations (alembic)\n"
	@printf "  api.run   Run the API locally with uvicorn\n"
	@printf "  seed      Seed DB from db/seed\n"
	@printf "  dev       Start dev servers (api + web)\n"
	@printf "  clean     Tear down infra and remove local artifacts\n\n"

setup:
	@echo "==> setup: creating dirs and preparing workspace"
	@mkdir -p artifacts tmp ./tmp/r2
	@[ -f .env ] || { [ -f .env.example ] && cp .env.example .env && echo "Copied .env.example -> .env (edit values)"; true; }
	@if [ -d apps/web ]; then \
		echo "Installing web deps"; \
		cd apps/web; \
		if [ -f package-lock.json ]; then npm ci; \
		elif [ -f yarn.lock ]; then yarn install; \
		else npm install; fi; \
	fi
	@if [ -d services/api ]; then \
		echo "Installing python deps (services/api)"; \
		if [ -f services/api/requirements-dev.txt ]; then \
			python3 -m pip install -U pip && python3 -m pip install -r services/api/requirements-dev.txt; \
		elif [ -f services/api/pyproject.toml ]; then \
			python3 -m pip install -U pip && (cd services/api && python3 -m pip install -e .); \
		else \
			echo "No python requirements found at services/api"; \
		fi; \
	fi
	@echo "==> setup complete (edit .env if required)"

# alias
openapi: generate

maybe-generate:
	if [ "$(SKIP_GENERATE)" = "1" ]; then
		echo "Skipping SDK generation (SKIP_GENERATE=1)"
	else
		$(MAKE) generate
	fi

generate:
	if [ "$(SKIP_GENERATE)" = "1" ]; then
		echo "Skipping SDK generation (SKIP_GENERATE=1)"
		exit 0
	fi
	if [ ! -f "$(OPENAPI)" ]; then
		echo "$(OPENAPI) not found"
		exit 1
	fi
	mkdir -p packages/sdk
	rm -rf packages/sdk/typescript packages/sdk/python
	npx --yes openapi-generator-cli version-manager set 7.7.0
	# Generate TypeScript SDK
	npx --yes openapi-generator-cli generate \
		-i $(OPENAPI) \
		-g typescript-fetch \
		-o packages/sdk/typescript \
		--skip-validate-spec \
		--additional-properties supportsES6=true,npmVersion=0.1.0
	# Generate Python SDK
	npx --yes openapi-generator-cli generate \
		-i $(OPENAPI) \
		-g python \
		-o packages/sdk/python \
		--skip-validate-spec \
		--additional-properties packageName=gridiron_sherlock_sdk,projectName=gridiron-sherlock-sdk
	# Build TypeScript SDK to dist (ESM + CJS shim)
	if [ -d packages/sdk/typescript ]; then
		cd packages/sdk/typescript
		if [ ! -f package.json ]; then echo '{"name":"@gridiron/sherlock-sdk","version":"0.0.0","type":"module","private":true}' > package.json; fi
		npm pkg set type=module >/dev/null 2>&1 || true
		npm pkg set main="dist/index.js" module="dist/index.js" types="dist/index.d.ts" >/dev/null 2>&1 || true
		npm i -D typescript@^5 >/dev/null 2>&1
		cat > tsconfig.esm.json <<-'EOF'
	{
	  "compilerOptions": {
	    "target": "ES2020",
	    "module": "ES2020",
	    "declaration": true,
	    "outDir": "dist",
	    "strict": true,
	    "lib": ["ES2020", "DOM"],
	    "moduleResolution": "Bundler",
	    "skipLibCheck": true,
	    "esModuleInterop": true
	  },
	  "include": ["**/*.ts"],
	  "exclude": ["node_modules", "dist", "dist-cjs"]
	}
	EOF
		npx tsc -p tsconfig.esm.json
		find dist -type f -name "*.js" -print0 | xargs -0 sed -E -i \
		  -e "s#(export\\s+\\*\\s+from\\s+['\"](\\.\\.?/[^'\"]+))(\\.js)?(['\"])#\\1.js\\4#g" \
		  -e "/export\\s+\\*\\s+from/! s#(from\\s+['\"](\\.\\.?/[^'\"]+))(\\.js)?(['\"])#\\1.js\\4#g" \
		  -e "s#(import\\(\\s*['\"](\\.\\.?/[^'\"]+))(\\.js)?(['\"])#\\1.js\\4#g" || true
		cat > tsconfig.cjs.json <<-'EOF'
	{
	  "compilerOptions": {
	    "target": "ES2019",
	    "module": "CommonJS",
	    "declaration": false,
	    "outDir": "dist-cjs",
	    "strict": true,
	    "lib": ["ES2020", "DOM"],
	    "moduleResolution": "Node",
	    "skipLibCheck": true,
	    "esModuleInterop": true
	  },
	  "include": ["**/*.ts"],
	  "exclude": ["node_modules", "dist", "dist-cjs"]
	}
	EOF
		npx tsc -p tsconfig.cjs.json
		if [ -f dist-cjs/index.js ]; then cp dist-cjs/index.js dist/index.cjs; fi
		rm -f tsconfig.esm.json tsconfig.cjs.json
		cd - >/dev/null
	fi
	cp CONTRACTS/openapi.yaml services/api/app/contracts/openapi.yaml
	@echo "SDKs generated under packages/sdk/ (TypeScript dist built)"

fmt:
	if [ -d apps/web ]; then
		(
			cd apps/web
			(npm run fmt --silent || true) || (command -v npx >/dev/null 2>&1 && npx prettier --write . || true)
		)
	fi
	if [ -d services/api ]; then
		(
			cd services/api
			command -v black >/dev/null 2>&1 && black . || true
		)
	fi
	@echo "fmt complete"

lint: maybe-generate
	if [ -d apps/web ]; then \
		( \
			cd apps/web; \
			if npm run -s lint; then :; \
			elif command -v npx >/dev/null 2>&1 && ls .eslintrc* >/dev/null 2>&1; then npx eslint .; \
			else echo 'no web linter configured' >&2; exit 2; \
			fi \
		); status=$$?; if [ $$status -ne 0 ]; then exit $$status; fi; \
	fi
	if [ -d services/api ]; then \
		( \
			cd services/api; \
			if command -v ruff >/dev/null 2>&1; then \
				if ruff --help 2>/dev/null | grep -q "[[:space:]]check[[:space:]]"; then ruff check .; \
				else ruff .; \
				fi; \
			elif command -v flake8 >/dev/null 2>&1; then flake8 .; \
			else echo 'no python linter configured' >&2; exit 2; \
			fi \
		); status=$$?; if [ $$status -ne 0 ]; then exit $$status; fi; \
	fi
	@echo "lint complete"

type: maybe-generate
	if [ -d apps/web ] && [ -f apps/web/tsconfig.json ]; then \
		( \
			cd apps/web; \
			if npm run -s type; then :; \
			elif command -v npx >/dev/null 2>&1; then npx tsc --noEmit; \
			else echo 'TypeScript not available for web type checks' >&2; exit 2; \
			fi \
		); status=$$?; if [ $$status -ne 0 ]; then exit $$status; fi; \
	else \
		echo 'no web tsconfig.json; skipping web type checks' >&2; \
	fi
	@echo "type checks done"

test: maybe-generate
	@echo "Running backend tests"
	if [ -d services/api ]; then \
		( \
			cd services/api; \
			if command -v pytest >/dev/null 2>&1; then pytest -q --maxfail=1; \
			else echo 'pytest is required; run make setup to install dev deps' >&2; exit 2; \
			fi \
		); status=$$?; if [ $$status -ne 0 ]; then exit $$status; fi; \
	fi
	@echo "Running frontend tests"
	if [ -d apps/web ] && [ -f apps/web/package.json ]; then \
		( \
			cd apps/web; \
			if node -e "const p=require('./package.json');process.exit(p.scripts&&p.scripts.test?0:1)"; then npm test --silent; \
			else echo 'no frontend test script' >&2; \
			fi \
		); status=$$?; if [ $$status -ne 0 ]; then exit $$status; fi; \
	fi
	@echo "Running contract tests"
	if [ -d tests/contracts ]; then \
		if command -v pytest >/dev/null 2>&1; then pytest -q tests/contracts; \
		else echo 'pytest is required for contract tests; run make setup' >&2; exit 2; \
		fi; \
	fi
	@echo "all tests completed"

api.run:
	@$(LOAD_ENV)
	cd services/api && uvicorn app.main:app --host 0.0.0.0 --port $${PORT_API:-8000}

e2e:
	@$(LOAD_ENV)
	$(COMPOSE) up -d
	sleep 3
	if [ -d apps/web ]; then
		(
			cd apps/web
			(npm run test:e2e --silent || true) || (command -v npx >/dev/null 2>&1 && [ -d tests/e2e ] && npx playwright test || true)
		)
	fi

build:
	@$(LOAD_ENV)
	if [ -d apps/web ]; then
		(
			cd apps/web
			npm run build || true
		)
	fi
	if [ -d services/api ]; then
		docker build -t gridiron-sherlock-api services/api || true
	fi
	@echo "build complete"

migrate:
	@echo "No migrations to apply (stub)"

seed:
	@$(LOAD_ENV)
	if [ -d db/seed ]; then
		for f in db/seed/*.sql; do
			echo "Seeding $$f"
			psql "$$DATABASE_URL" -f "$$f" || echo "psql failed for $$f"
		done
	else
		echo "no db/seed directory"
	fi

start:
	@$(LOAD_ENV)
	$(COMPOSE) up -d
	$(COMPOSE) ps
	@echo "infra started (use make dev to run services locally)"

dev:
	@$(LOAD_ENV)
	(
		cd services/api
		uvicorn app.main:app --reload --host 0.0.0.0 --port $${PORT_API:-8000}
	) & (
		cd apps/web
		npm run dev
	) ; wait

clean:
	@$(LOAD_ENV)
	$(COMPOSE) down -v
	rm -rf node_modules apps/web/.next services/api/.venv .pytest_cache .coverage artifacts tmp packages/sdk/* || true

smoke: maybe-generate
	@echo "-> ESM import check"
	node --input-type=module -e "import { Configuration } from './packages/sdk/typescript/dist/index.js'; console.log('esm:', typeof Configuration)"
	@echo "-> CJS import check"
	node -e "console.log('cjs:', typeof require('./packages/sdk/typescript/dist/index.cjs').Configuration)"
	@echo "-> Python import check"
	@if command -v python >/dev/null 2>&1; then \
		PYTHONPATH=packages/sdk/python python -c "import gridiron_sherlock_sdk as s; print('py:', 'ok')"; \
	else \
		PYTHONPATH=packages/sdk/python python3 -c "import gridiron_sherlock_sdk as s; print('py:', 'ok')"; \
	fi
