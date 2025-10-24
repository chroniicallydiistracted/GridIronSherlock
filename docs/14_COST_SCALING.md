# Cost and Scaling

- Cloud Run min instances 0. Concurrency 80 for API, 1 for jobs.
- Neon autoscaling. Branch per PR for ephemeral tests.
- Upstash serverless tiers. Monitor egress for R2.
- Cache hit target ≥ 85% for projections and players.
