# Deploy and Environments

## Environments
- dev, staging, prod. Separate Neon branches and Redis DBs.

## CI/CD
- GitHub Actions: build → test → scan → deploy with approvals.
- Blue/green for API. Cloudflare Pages previews for PRs.

## Migrations
- Alembic migrations auto-run. Gate deploy on success.

## Feature Flags
- Boolean flags in Redis. Include kill-switch for models and live feeds.
