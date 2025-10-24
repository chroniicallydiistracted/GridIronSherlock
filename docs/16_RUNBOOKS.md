# Runbooks

## Sync Stuck
- Clear job lock `job:{name}:lock`. Re-run last manifest.

## Token Expired
- Invoke `/internal/oauth/refresh` for affected account.

## Hotfix Procedure
- Create Neon branch from prod. Patch. Merge. Promote.

## Data Drift
- Roll back to last good `source_version`. Recompute features and projections.
