# Data Ingestion and Orchestration

## Pipeline Types
- Reference sync: players, teams, crosswalks. Weekly.
- Schedule/games: preseason bulk, weekly refresh, game-day hourly.
- PBP: nflfastR to Parquet on R2. Incremental during live. Finalize post-game.
- Injuries: nflreadr + fantasy notes. Daily and on-demand.
- Fantasy state: leagues, rosters, waivers, matchups via selected provider. Hourly in-season, manual refresh on demand.

## Workers
- `etl-nflverse`: R container with nflreadr/nflfastR/nflseedR. Writes Parquet + manifests.
- `etl-fantasy`: Python with provider SDKs + PyESPN. Normalizes to Postgres.

## Scheduling
- Cloud Scheduler → Cloud Run Jobs with parameters (`scope`, `season`, `week`).

## Idempotency
- Upserts keyed by natural IDs. Store `source_etag`, `ingested_at`. Retry-safe.

## Provenance
- Persist `source_version` and job metadata. Immutable once published.
