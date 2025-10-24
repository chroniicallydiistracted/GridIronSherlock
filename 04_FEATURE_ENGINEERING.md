# Feature Engineering

## Windows
- Last 1/3/5 games. Season to date. Role deltas vs prior 3.

## Categories and Columns
- Usage: snap_share, route_share, target_share, rush_share, rz_share, g2g_share, ldd_snaps.
- Efficiency: yprr, adot, racr, epa_per_target, epa_per_rush, success_rate.
- Context: pace, proe, team_total, spread, home, weather (if available).
- Defense vs position: opp_epa_allowed_pass/rush, explosive_allowed, pressure_rate.
- Volatility: stdev, cv, p25, p75.
- Regression: xtd_minus_td; qb xint_minus_int.

## Execution
- Compute in DuckDB for speed on worker. Persist wide numeric rows to Postgres.
- Validate ranges and nulls. Fail pipeline on schema drift.
