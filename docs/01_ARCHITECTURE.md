# System Architecture

## Overview
- Frontend: Next.js 14 on Cloudflare Pages. SSR via Pages Functions where needed.
- Backend: FastAPI on Google Cloud Run. Autoscale. Private egress to Neon.
- Workers: Cloud Run Jobs for ETL, training, backtests, projections.
- DB: Neon Postgres. Branch per env.
- Cache/Queue: Upstash Redis for caching, queues, pub/sub.
- Object Storage: Cloudflare R2 for Parquet artifacts, models, and exports.
- Scheduler: Google Cloud Scheduler → Cloud Run Jobs.
- Secrets: Google Secret Manager.
- Observability: OpenTelemetry traces + metrics. GCP Cloud Logging and OTLP sink.

## Data Flow (Mermaid)
```mermaid
flowchart LR
  subgraph Client
    UI[Next.js UI]
  end
  UI -->|HTTPS| API[FastAPI /v1]
  API <-->|Redis| Cache[(Upstash Redis)]
  API -->|JDBC| DB[(Neon Postgres)]
  API -->|S3 API| R2[(Cloudflare R2)]
  Scheduler[Cloud Scheduler] --> Jobs[Cloud Run Jobs]
  Jobs --> R2
  Jobs --> DB
  Jobs --> Cache
  Jobs --> API
  ext[NFLVerse + Fantasy APIs] --> Jobs
  ext --> API
```
