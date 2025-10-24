# OAuth and Provider Integrations

## Flow
- Authorization Code + PKCE when supported.
- Redirect: `{APP_URL}/api/oauth/{provider}/callback`

## Token Storage
- AES-GCM encrypted at rest. Rotate keys. Track scopes and expiry.

## Sync Strategy
- On connect: leagues, rosters, scoring settings.
- Scheduled: hourly roster/waiver snapshot, nightly matchups.

## Resilience
- Exponential backoff. Honor `Retry-After`. Circuit breaker per provider.

## Adapters
- Isolate each provider. Log request/response metadata without PII.
