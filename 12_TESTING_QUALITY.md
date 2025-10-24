# Testing and Quality

## Unit
- Adapters, feature builders, scoring mappers.

## Integration
- Provider sandboxes or recorded cassettes. DB migrations on Neon branch.

## Data Quality
- dbt-style checks: key uniqueness, null constraints, range checks. Fail build on breach.

## Backtests
- Weekly scheduled. Store MAE, calibration, hit rates. Alert on regression.

## E2E
- Playwright for link, sync, optimize, waivers, trades, and live flow.
