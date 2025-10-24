# Analytics Specification

## Data Coverage and Precedence
- NFLfastR for on-field events and rates. nflreadr for injuries, rosters, transactions. Fantasy API for roster truth.

## Features
- Usage: snap/route/target/rush shares, red-zone and goal-to-go shares, LDD snaps.
- Efficiency: YPRR, aDOT, RACR, EPA per target/rush, success rate.
- Context: pace, PROE, totals, spread, weather (if available).
- Defense vs position: EPA allowed, explosive rate, pressure rate.
- Volatility: stdev, CV, p25/p75.
- Regression: xTD minus TD, xINT minus INT.
- Fantasy: replacement levels, schedule-adjusted FPA, bye and playoff leverage.

## Models
- Weekly projections: mean, p20, p50, p80, boom/bust probabilities. Calibration per position.
- ROS projections: decay-weighted with role deltas.
- Scenario sims: NFLseedR for season paths.

## Start/Sit
- ILP objective with λ and μ sliders. Sensitivity deltas.

## Waivers and FAAB
- Value over replacement next N weeks × scarcity. FAAB low/med/high bands by league aggressiveness.

## Trades
- ROS delta for both sides. Playoff-weighted. Injury risk discount.

## Explainability
- Global and local explanations. Top drivers surfaced in UI.
