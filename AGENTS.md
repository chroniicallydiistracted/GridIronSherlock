# GridIron Sherlock — Build the entire repo from SPEC

You are the coding agent for the GridIron Sherlock web app. Build the repository end-to-end from the SPEC files already in the GitHub repo `GridironSherlock`. Do not wait for clarification unless blocked by missing secrets or provider constraints. Ship in small, verified PRs. All outputs must match the SPEC and pass automated gates.

## Non-negotiable rules

1. **Never disable or remove a feature to “fix” a bug or error.** Fix root cause.
2. **Never hide errors.** No swallowing exceptions, no `|| true`, no muted logging.
3. **No silent fallbacks or silent failures.** Fail fast, fail loudly, emit clear diagnostics.
4. **Follow official docs.** For every dependency, use the vendor-recommended approach. If deviating, document why and how.
5. **Clean up.** Remove temporary scripts, scaffolds, and dead files once they’re no longer needed.

Enforcement:
- CI rejects PRs that mute errors, disable features, or add silent fallbacks.
- Any deviation from docs requires an ADR (`docs/adr/NNN-title.md`) plus links to sources.

---

## Context

- **Repo:** `GridironSherlock` (SPEC files already present).
- **Targets:** Next.js 14 (Cloudflare Pages), FastAPI (Cloud Run), Neon Postgres, Upstash Redis, Cloudflare R2, Google Secret Manager, Google Cloud Scheduler, OR-Tools, R-based ETL (NFLVerse), Python ETL (fantasy providers).

## Objectives

1) Implement contracts first.  
2) Generate SDKs.  
3) Stand up API and UI shells that compile.  
4) Land ETL jobs with fixtures.  
5) Land optimizer service.  
6) Wire caching, monitoring, CI gates.  
7) Prove flow with synthetic league fixtures.  
8) Keep costs low.

## Ground rules

- **Spec-first.** No endpoints or payloads outside OpenAPI. No undocumented fields.
- **Deterministic CI.** Lockfiles committed. Pinned toolchain. Reproducible builds.
- **Secrets:** never in git. Read from env only. `.env.example` contains placeholders.
- **Networking:** timeouts, retries with backoff, circuit breakers. Respect rate limits.
- **Every PR:** tests + docs. Failing tests block merge. No commented-out code as “fix”.
- **Minimal deps.** Prefer stdlib and first-party SDKs.
- **Error policy:** loud failures, structured logs, exit non-zero on any gate failure.
- **No silent fallbacks:** do not auto-skip tasks; print reason and fail.
- **No feature removal to green tests:** track regressions, fix, add tests.
- **Docs compliance:** consult official docs for each tool used and implement the recommended path; cite links in PR description.
- **Cleanup:** remove scaffolds and temp files after use (generators, snapshots, throwaway scripts).
## Ground rules

- **Spec-first.** No endpoints or payloads outside OpenAPI. No undocumented fields.
- **Deterministic CI.** Lockfiles committed. Pinned toolchain. Reproducible builds.
- **Secrets:** never in git. Read from env only. `.env.example` contains placeholders.
- **Networking:** timeouts, retries with backoff, circuit breakers. Respect rate limits.
- **Every PR:** tests + docs. Failing tests block merge. No commented-out code as “fix”.
- **Minimal deps.** Prefer stdlib and first-party SDKs.
- **Error policy:** loud failures, structured logs, exit non-zero on any gate failure.
- **No silent fallbacks:** do not auto-skip tasks; print reason and fail.
- **No feature removal to green tests:** track regressions, fix, add tests.
- **Docs compliance:** consult official docs for each tool used and implement the recommended path; cite links in PR description.
- **Cleanup:** remove scaffolds and temp files after use (generators, snapshots, throwaway scripts).

# Deliverables (top-level)
- CONTRACTS/openapi.yaml covering /v1 as defined in SPEC.
- packages/sdk/typescript and packages/sdk/python generated from openapi.yaml.
- apps/web Next.js 14 shell with routes and mocked data bound to schemas.
- services/api FastAPI app implementing /v1 with skeletal handlers and real contracts.
- services/etl-nflverse R job container that outputs Parquet and a manifest.
- services/etl-fantasy Python job container that normalizes provider data to Postgres.
- services/optimizer OR-Tools MIP service with objective and constraints.
- infra/ GitHub Actions workflows, Dockerfiles, devcontainer, IaC stubs.
- db/ migrations and seed fixtures for synthetic leagues and crosswalks.
- tests/ unit, integration, backtests, contract tests, Playwright e2e.

# Branching and PR cadence
- Create branch per milestone. Open small PRs. Each PR must run: unit, integration (with fixtures), type-checks, linters, security scan, OpenAPI diff, e2e smoke on web+api with mock data.
- Name PRs: feat/contracts, feat/sdk, feat/api-skeleton, feat/web-shell, feat/etl-nflverse, feat/etl-fantasy, feat/optimizer, feat/live-sse, feat/caching, feat/ci, feat/e2e.

## PR Template (include in PR description)
- Purpose
- Changes
- Tests
- Contracts touched
- Screenshots or artifacts
- Risks
- Checklist: [ ] unit [ ] integration [ ] contract [ ] e2e [ ] security [ ] docs

# Milestone 0: Repo hygiene
- Add .editorconfig, .gitattributes, CONTRIBUTING.md, CODEOWNERS, SECURITY.md, LICENSE.
- Add devcontainer with Node 22, Python 3.11, Java 21, R 4.4, Docker CLI.
- Add Makefile with targets: setup, fmt, lint, test, e2e, build, dev, generate, migrate, seed.

# Milestone 1: Contracts-first
- Read SPEC files in repo: 01_ARCHITECTURE.md to 20_UI_SPEC.md and the Overall SPEC markdown.
- Draft CONTRACTS/openapi.yaml for /v1 routes listed in SPEC.
- Include schemas for all payloads and error envelope {error:{code,message,details}}.
- Add JSON Schemas in CONTRACTS/schemas mirroring OpenAPI components.
- Add contract tests: tests/contracts ensure every server response matches schema.
- Add “contract snapshots” in CONTRACTS/snapshots for OpenAPI diff gating.

# Milestone 2: SDKs
- Generate typescript and python SDKs from openapi.yaml.
- Publish locally within monorepo. No external publish.
- Add smoke tests that import SDKs in web and api projects.

# Milestone 3: API skeleton
- Scaffold services/api with FastAPI.
- Implement routers for all endpoints with stubbed providers and fake stores wired to schemas.
- Add pydantic models generated from OpenAPI.
- Add middlewares: request ID, rate limit via Redis, structured logging, tracing (OTel).
- Add HTMX-free HTML health endpoint /healthz returning status ok and versions.
- Add Alembic and base migrations from 02_DATA_MODEL.md.

# Milestone 4: Web shell
- Scaffold apps/web Next.js 14 with App Router.
- Pages: Dashboard, Lineup, Matchup, Waivers, Trades, Players, Projections, Research, Live, Settings.
- Bind mock fetchers to SDK types. Table virtualization for large lists.
- Add Lighthouse and a11y checks in CI. p95 interactive ≤ 1.5 s using mocked data.

# Milestone 5: Storage and migrations
- Implement db schema from 02_DATA_MODEL.md.
- Add seed scripts for synthetic leagues, teams, players, crosswalks, minimal games.
- Provide db/seed/*.sql and a Python seeder that can run against Neon and local Postgres.

# Milestone 6: ETL — NFLVerse (R)
- Create services/etl-nflverse R project.
- Jobs: reference-sync, schedules, pbp-ingest, injuries.
- Output Parquet to local artifacts folder and mock R2 interface.
- Manifests include dataset name, season, week, etag, row counts, schema version.
- Add fixture-based tests using small csv/parquet samples and hash assertions.

# Milestone 7: ETL — Fantasy providers (Python)
- Create services/etl-fantasy with provider adapters for yahoo, espn, sleeper, nfl.
- Abstract interface: list_leagues, list_teams, list_roster, list_waivers, list_matchups.
- Normalize into db tables. Idempotent upserts. Store source_etag and ingested_at.
- Record provider metadata and rate-limit headers.
- Tests use recorded cassettes or provider-supplied sandboxes. Provide fixtures only.

# Milestone 8: Feature engineering layer
- Build feature jobs in Python using DuckDB over Parquet and Postgres.
- Columns per 04_FEATURE_ENGINEERING.md. Wide numeric, no nested JSON.
- Validate ranges and nulls. Fail job on drift. Persist with source_version.

# Milestone 9: Modeling
- Implement training pipeline per 05_MODELS_MLOPS.md.
- Add baseline gradient-boosted models per position. Quantile outputs p20/p50/p80.
- Register artifacts in R2 mock and database.
- Add backtest harness for seasons 2019–2023 with summary metrics and stored reports.
- Add calibration metrics and plots saved under artifacts.

# Milestone 10: Optimizer service
- OR-Tools MIP in services/optimizer.
- Inputs: roster, eligibility, projections, variance proxy, constraints.
- Output: optimal lineup and top-k alternatives with deltas.
- Unit tests for objective and constraints. Deterministic seeds.

# Milestone 11: Live engine and SSE
- Implement incremental ingest loop that consumes mock live pbp.
- Normalize to events. Publish to Redis pub/sub channel live:v1.
- API exposes /v1/live/stream SSE. De-duplicate by game_id:play_id.
- Add front-end Live tiles and an Impact feed with payloads from SSE.

# Milestone 12: Caching and performance
- Implement Redis caches for projections, players, team lineups, waivers with TTLs defined in SPEC.
- Add ETag and stale-while-revalidate on list endpoints.
- Add fast pagination envelopes with total, page, pageSize, items.

# Milestone 13: OAuth scaffolding
- Implement stubs for OAuth link flows for yahoo, espn, sleeper, nfl.
- Callback paths: /api/oauth/{provider}/callback.
- Use in-memory secret placeholders only. Add .env.example keys for local testing.

# Milestone 14: CI/CD
- .github/workflows:
  - ci.yml: setup, build, type-check, lint, unit, integration, db migrate against ephemeral Postgres, contract tests, OpenAPI diff, Lighthouse, a11y.
  - e2e.yml: Playwright against api+web compose.
  - security.yml: Trivy or Snyk, CodeQL.
- Upload artifacts: OpenAPI, SDK tars, test reports, backtest summaries.
- Required checks on main.

# Milestone 15: Docs
- Generate minimal docs site from SPEC and add /docs directory.
- Add RUNBOOKS.md links. Add ENV_VARS.md example template.
- Add API reference generated from openapi.yaml.

# Definitions of Done per milestone
- All tests pass. Contracts unchanged or diff accepted.
- Coverage trend non-decreasing.
- Lint and type checks pass. Security scan with no criticals.
- Reproducible in devcontainer using make setup and make test.

# Project structure
- apps/web
- services/api
- services/etl-nflverse
- services/etl-fantasy
- services/optimizer
- packages/sdk/typescript
- packages/sdk/python
- CONTRACTS
- db/migrations, db/seed
- infra
- tests
- .github/workflows
- .devcontainer

# Makefile targets (implement)
- setup
- generate
- fmt
- lint
- test
- e2e
- build
- migrate
- seed
- start

# Test data and fixtures
- Commit synthetic league JSON and compact Parquet samples under tests/fixtures.
- Golden files for contract tests under CONTRACTS/snapshots.
- Backtest small seasons slice for speed.

# Acceptance gates for initial merge to main
- apps/web builds and renders all routes with mocked data.
- services/api exposes /healthz and all /v1 endpoints with schema-correct stubs.
- CONTRACTS/openapi.yaml complete. SDKs generated and imported by web and api.
- db migrations apply cleanly and seeds load.
- ETL jobs run on fixtures and write manifests.
- Optimizer returns a valid lineup on a seeded league with mocked projections.
- Live SSE pushes at least one synthetic event to web client.

# Output expectations
- Create PRs in order. Include a short README per service. Include run commands and env var list.
- Where secrets or provider sandboxes are required, stop and open a PR that documents the needed inputs.

Begin with Milestone 1 (Contracts-first). Do not modify SPEC files. Work only under new directories. Report progress via PR descriptions and checklists.

## CHANGELOG ##
