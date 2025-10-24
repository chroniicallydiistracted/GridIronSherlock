# Optimizer Service

## Solver
- OR-Tools MIP. Cloud Run on demand.

## Objective
- Maximize `mean + λ*ceiling − μ*variance`.

## Constraints
- Roster slots, positional limits, injury and bye status, max players per NFL team if configured.

## Inputs
- Team roster, eligibility matrix, projections, risk parameters.

## Outputs
- Optimal lineup, top-k alternatives, sensitivity deltas.
