# Caching and Performance

## Redis Keys
- `proj:{league}:{week}` — projections snapshot
- `player:{id}` — player profile
- `team:{id}:lineup` — current lineup
- `waivers:{league}:{week}`

## TTLs
- Projections: 15 min Tue–Sat, 5 min Sun–Mon.
- Fantasy state: 2 min during live windows.

## HTTP Caching
- ETag over payload hash. Stale-while-revalidate 60s.

## DB
- Covering indexes on hot queries. Analyze weekly. Avoid N+1 with prefetch patterns.
