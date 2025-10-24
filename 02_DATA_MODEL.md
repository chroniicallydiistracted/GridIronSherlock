# Domain Data Model

## Entities
- providers, users, user_accounts
- leagues, teams
- players, games, pbp, injuries
- features, projections
- optimizer_runs, recommendations

## SQL DDL (core)
```sql
create table providers (
  provider_id text primary key, -- 'yahoo','espn','sleeper','nfl'
  auth_type text not null
);

create table users (
  user_id uuid primary key,
  email text unique not null,
  created_at timestamptz not null default now()
);

create table user_accounts (
  user_id uuid references users(user_id),
  provider_id text references providers(provider_id),
  provider_user_id text not null,
  access_token_enc text not null,
  refresh_token_enc text,
  token_scopes text[],
  token_expires_at timestamptz,
  primary key(user_id, provider_id)
);

create table leagues (
  league_id uuid primary key,
  provider_id text references providers(provider_id),
  provider_league_id text not null,
  name text,
  season int,
  scoring_json jsonb,
  roster_settings_json jsonb,
  UNIQUE(provider_id, provider_league_id)
);

create table teams (
  team_id uuid primary key,
  league_id uuid references leagues(league_id),
  provider_team_id text not null,
  name text,
  manager_user_id uuid references users(user_id),
  UNIQUE(league_id, provider_team_id)
);

create table players (
  player_id uuid primary key,
  gsis_id text, -- nflfastR canonical
  espn_id text,
  yahoo_id text,
  sleeper_id text,
  nfl_id text,
  full_name text,
  pos text,
  team text,
  birthdate date
);

create table games (
  game_id text primary key, -- nflfastR game_id
  season int,
  week int,
  home_team text,
  away_team text,
  gameday timestamptz,
  status text
);

create table pbp (
  game_id text references games(game_id),
  play_id bigint,
  offense text,
  defense text,
  quarter int,
  time_remaining_seconds int,
  yardline_100 int,
  epa double precision,
  cpoe double precision,
  air_yards double precision,
  rush text,
  pass text,
  primary key(game_id, play_id)
);

create table injuries (
  season int,
  week int,
  gsis_id text,
  status text,
  details jsonb,
  primary key(season, week, gsis_id)
);

create table features (
  season int,
  week int,
  gsis_id text,
  pos text,
  snap_share double precision,
  route_share double precision,
  target_share double precision,
  rush_share double precision,
  rz_share double precision,
  g2g_share double precision,
  ldd_snaps double precision,
  yprr double precision,
  adot double precision,
  racr double precision,
  epa_per_target double precision,
  epa_per_rush double precision,
  success_rate double precision,
  pace double precision,
  proe double precision,
  opp_epa_allowed_pass double precision,
  opp_epa_allowed_rush double precision,
  explosive_allowed double precision,
  pressure_rate double precision,
  stdev double precision,
  cv double precision,
  p25 double precision,
  p75 double precision,
  xtd_minus_td double precision,
  model_inputs jsonb,
  source_version text,
  created_at timestamptz default now(),
  primary key(season, week, gsis_id, source_version)
);

create table projections (
  season int,
  week int,
  gsis_id text,
  pos text,
  mean_points double precision,
  p20 double precision,
  p50 double precision,
  p80 double precision,
  boom_prob double precision,
  bust_prob double precision,
  model_version text,
  created_at timestamptz default now(),
  primary key(season, week, gsis_id, model_version)
);

create table optimizer_runs (
  run_id uuid primary key,
  user_id uuid references users(user_id),
  league_id uuid references leagues(league_id),
  team_id uuid references teams(team_id),
  season int, week int,
  objective_json jsonb,
  result_json jsonb,
  created_at timestamptz default now()
);

create table recommendations (
  rec_id uuid primary key,
  user_id uuid references users(user_id),
  league_id uuid references leagues(league_id),
  kind text, -- 'start_sit','waiver','trade'
  payload jsonb,
  score double precision,
  created_at timestamptz default now()
);
```

## Indexing
- Hot paths: `(season, week, pos)` on projections and features.
- Lookup: `(gsis_id)` on players, `(league_id, provider_team_id)` on teams.
