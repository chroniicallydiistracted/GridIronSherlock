# UI Specification

## Design Language
- 12-column grid. 8-point spacing. Inter/SF with tabular numerals. Color-blind safe palette.

## Shell
- Left rail: Dashboard, Lineup, Matchup, Waivers, Trades, Players, Projections, Research, Live, Settings.
- Top bar: global search, source badge, last refresh.
- Right panel: compare queue and pinned insights.

## Screens
1. Dashboard: health index, matchup difficulty, start/sit changes, waiver snapshot, trade radar, trends, bye/injury timeline.
2. Lineup Optimizer: objective sliders, roster grid with quantiles and risk, one-click apply, explanation drawer.
3. Matchup: game environment, positional battles, startability matrix.
4. Waivers: filters, value table, FAAB ranges, multi-add planner.
5. Trades: needs matrix, proposals with fairness and deltas, risk panel.
6. Players Index: faceted search, role/efficiency/matchup/projection columns, compare mode.
7. Player Detail: overview, usage, efficiency, matchups, news, explain.
8. Projections: weekly and ROS tables with quantiles, downloads, model version selector.
9. Research Lab: query builder, saved studies, chart templates.
10. Live: real-time tiles, impact feed, rapid what-if swaps.
11. Settings: account linking, scoring display and override, notifications.

## Interaction
- Progressive disclosure. Drilldowns everywhere. Sticky compare. Keyboard shortcuts.
- Accessibility: full keyboard nav, ARIA, WCAG AA.

## Provenance
- Source chips, hover details, metric definitions and formulas on demand.

## Performance
- p95 ≤ 1.5 s on cached data. Virtualized tables. Chart downsampling. SWR on client.
