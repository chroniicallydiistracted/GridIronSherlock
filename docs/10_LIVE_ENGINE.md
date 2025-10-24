# Live Game and Impact Engine

## Ingest
- Poll incremental PBP every 15–30 s when available. Fallback to ESPN scoreboard proxies.

## Event Bus
- Publish normalized events to Redis `live:v1`.

## Fanout
- `/v1/live/stream` SSE pushes impacts: projection changes, scores, injuries.

## De-duplication
- Idempotency key `game_id:play_id`. Drop repeats.
