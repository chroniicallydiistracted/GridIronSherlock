# API Design (REST + SSE)

Base path: `/v1`

## Auth
- Session cookie for UI. Service tokens for jobs.

## Endpoints
- `GET /me`
- `POST /accounts/{provider}/link`  — start OAuth
- `GET /oauth/{provider}/callback`
- `GET /leagues` | `GET /leagues/{id}`
- `GET /teams/{id}/lineup` | `POST /teams/{id}/optimize`
- `GET /projections?week=&pos=&leagueId=`
- `GET /players?query=&pos=&team=`
- `GET /players/{id}`
- `GET /waivers?leagueId=&week=`
- `POST /trades/estimate`
- `GET /live/stream`  — SSE for impacts
- `POST /refresh/{scope}`

## Errors
- Envelope: `{ "error": { "code": "string", "message": "string", "details": {...} } }`

## Rate Limits
- Sliding window in Redis per user and IP.
