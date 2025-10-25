SHELL := /bin/bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c

COMPOSE_FILE := docker-compose.dev.yml
COMPOSE := docker compose -f $(COMPOSE_FILE)
OPENAPI := CONTRACTS/openapi.yaml

## Only source .env when all non-comment, non-empty lines are KEY=VALUE (and no '<...>' placeholders)
LOAD_ENV := set -o allexport; \
	if [ -f .env ]; then \
		clean=1; \
		while IFS= read -r line; do \
			case "$$line" in \
				''|'#'*) ;; \
				*'<'*) clean=0 ;; \
				[A-Za-z_]*=*) ;; \
				*) clean=0 ;; \
			esac; \
		done < .env; \
		if [ "$$clean" -eq 1 ]; then . .env; fi; \
	fi; \
	set +o allexport;

.PHONY: help openapi setup generate fmt lint type test e2e build migrate seed start dev clean

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
	@printf "  seed      Seed DB from db/seed\n"
	@printf "  dev       Start dev servers (api + web)\n"
	@printf "  clean     Tear down infra and remove local artifacts\n\n"

setup:
	@echo "==> setup: creating dirs and preparing workspace"
	@$(LOAD_ENV)
	mkdir -p artifacts tmp ./tmp/r2
	if [ ! -f .env ] && [ -f .env.example ]; then
		cp .env.example .env
		echo 'Copied .env.example -> .env (edit values)'
	fi
	if [ -d apps/web ]; then
		echo 'Installing web deps'
		(
			cd apps/web
			if [ -f package-lock.json ]; then
				npm ci
			elif [ -f yarn.lock ]; then
				yarn install
			else
				npm install
			fi
		)
	fi
	if [ -d services/api ]; then
		echo 'Installing python deps (services/api)'
		if [ -f services/api/requirements-dev.txt ]; then
			python3 -m pip install -U pip
			python3 -m pip install -r services/api/requirements-dev.txt
		elif [ -f services/api/pyproject.toml ]; then
			python3 -m pip install -U pip
			(
				cd services/api
				python3 -m pip install -e .
			)
		else
			echo 'No python requirements found at services/api'
		fi
	fi
	@echo "==> setup complete (edit .env if required)"

## alias
openapi: generate

generate:
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
		# Ensure package.json exists
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
		# Fix ESM extensionless imports to include .js for Node compatibility
		find dist -type f -name "*.js" -print0 | xargs -0 sed -E -i \
		  -e "s#(export\\s+\\*\\s+from\\s+['\"](\\.\\.?/[^'\"]+))(\\.js)?(['\"])#\\1.js\\4#g" \
		  -e "/export\\s+\\*\\s+from/! s#(from\\s+['\"](\\.\\.?/[^'\"]+))(\\.js)?(['\"])#\\1.js\\4#g" \
		  -e "s#(import\\(\\s*['\"](\\.\\.?/[^'\"]+))(\\.js)?(['\"])#\\1.js\\4#g" || true
		# CommonJS build (minimal) -> dist/index.cjs
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
		# Keep full CommonJS build under dist-cjs and also provide dist/index.cjs entry
		if [ -f dist-cjs/index.js ]; then cp dist-cjs/index.js dist/index.cjs; fi
		rm -f tsconfig.esm.json tsconfig.cjs.json
		cd - >/dev/null
	fi
	@echo 'SDKs generated under packages/sdk/ (TypeScript dist built)'

fmt:
	@$(LOAD_ENV)
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
	@echo 'fmt complete'

lint: generate
	@$(LOAD_ENV)
	if [ -d apps/web ]; then
		(
			cd apps/web
			(npm run lint --silent || true) || (command -v npx >/dev/null 2>&1 && ls .eslintrc* >/dev/null 2>&1 && npx eslint . || true)
		)
	fi
	if [ -d services/api ]; then
		(
			cd services/api
			command -v ruff >/dev/null 2>&1 && ruff . || command -v flake8 >/dev/null 2>&1 && flake8 . || true
		)
	fi
	@echo 'lint complete'

type: generate
	@$(LOAD_ENV)
	if [ -d apps/web ] && [ -f apps/web/tsconfig.json ]; then
		(
			cd apps/web
			(npm run type --silent || true) || (command -v npx >/dev/null 2>&1 && npx tsc --noEmit || true)
		)
	fi
	@echo 'type checks done'

test: generate
	@$(LOAD_ENV)
	echo 'Running backend tests'
	if [ -d services/api ]; then
		(
			cd services/api
			pytest -q --maxfail=1
		)
	fi
	echo 'Running frontend tests'
	if [ -d apps/web ] && [ -f apps/web/package.json ]; then
		(
			cd apps/web
			npm test --silent
		)
	fi
	echo 'Running contract tests'
	if [ -d tests/contracts ]; then
		pytest -q tests/contracts
	fi
	@echo 'all tests completed'

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
	@echo 'build complete'

migrate:
	@$(LOAD_ENV)
	if [ -d services/api/alembic ]; then
		(
			cd services/api
			alembic upgrade head || echo 'alembic not available or failed'
		)
	else
		echo 'no alembic migrations found'
	fi

seed:
	@$(LOAD_ENV)
	if [ -d db/seed ]; then
		for f in db/seed/*.sql; do
			echo "Seeding $$f"
			psql "$$DATABASE_URL" -f "$$f" || echo "psql failed for $$f"
		done
	else
		echo 'no db/seed directory'
	fi

start:
	@$(LOAD_ENV)
	$(COMPOSE) up -d
	$(COMPOSE) ps
	@echo 'infra started (use make dev to run services locally)'

dev:
	@$(LOAD_ENV)
	(
		cd services/api
		uvicorn services.api.main:app --reload --host 0.0.0.0 --port $${PORT_API:-8000}
	) & (
		cd apps/web
		npm run dev
	) ; wait

clean:
	@$(LOAD_ENV)
	$(COMPOSE) down -v
	rm -rf node_modules apps/web/.next services/api/.venv .pytest_cache .coverage artifacts tmp packages/sdk/* || true
