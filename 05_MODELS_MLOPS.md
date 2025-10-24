# Modeling and MLOps

## Targets
- Weekly fantasy points per league scoring mapped to a canonical schema.

## Models
- Gradient-boosted trees for mean.
- Quantile models for p20 and p80.
- Separate models per position (QB, RB, WR, TE, K, DST).

## Training
- Train on 2019–2023. Validate 2024. Weekly rolling evaluation on 2025.
- Metrics: MAE, pinball loss, CRPS, calibration by decile.

## Registry and Artifacts
- Store binaries and signatures in R2 `models/<version>/`. Register in Postgres.

## Inference
- Batch weekly by league scoring.
- Online per request with scoring overrides. Cache results.

## Explainability
- Global importances. On-demand local SHAP. Persist summaries to R2.
