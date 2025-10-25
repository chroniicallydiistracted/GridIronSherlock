"""Synthetic payloads that satisfy the OpenAPI contracts."""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from uuid import UUID, uuid5

from . import models as m


def _uuid(name: str) -> UUID:
    """Deterministically derive UUIDs for stub payloads."""

    namespace = UUID("12345678-1234-5678-1234-567812345678")
    return uuid5(namespace, name)


def _now() -> datetime:
    return datetime.now(timezone.utc)


def _provenance(suffix: str = "baseline") -> m.Provenance:
    return m.Provenance(source="gridiron-sherlock", asOf=_now(), modelVersion=f"stub-{suffix}")


def user_profile() -> m.UserProfile:
    league_id = _uuid("league-1")
    return m.UserProfile(
        userId=_uuid("user-1"),
        email="analyst@example.com",
        createdAt=_now() - timedelta(days=30),
        displayName="GridIron Analyst",
        accounts=[
            m.LinkedAccount(
                provider=m.ProviderId.espn,
                status=m.Status1.linked,
                scopes=["league.read", "team.write"],
                linkedAt=_now() - timedelta(days=28),
                lastSyncAt=_now() - timedelta(hours=1),
                needsReauth=False,
            )
        ],
        activeLeagueIds=[league_id],
        preferences=m.Preferences(
            defaultLeagueId=league_id,
            defaultView="dashboard",
            notificationOptIn=True,
        ),
        featureFlags=["mock-data", "beta"],
    )


def account_link(provider: m.ProviderId, request: m.AccountLinkRequest | None) -> m.AccountLinkResponse:
    return m.AccountLinkResponse(
        provider=provider,
        authorizationUrl="https://auth.example.com/redirect",
        state="stub-state-token",
        expiresAt=_now() + timedelta(minutes=5),
        pkce={
            "codeChallenge": "stub-challenge",
            "codeChallengeMethod": "S256",
        },
    )


def oauth_callback(provider: m.ProviderId, code: str | None, state: str | None) -> m.OAuthCallbackResponse:
    linked_account = m.LinkedAccount(
        provider=provider,
        status=m.Status1.linked,
        scopes=["league.read"],
        linkedAt=_now() - timedelta(days=1),
        lastSyncAt=_now(),
        needsReauth=False,
    )
    return m.OAuthCallbackResponse(
        provider=provider,
        status="linked",
        linkedAccount=linked_account,
        redirect="https://app.gridironsherlock.com/settings/accounts",
        message="Account linked successfully",
    )


def _team_reference(team_suffix: str = "1", league_id: UUID | None = None) -> m.TeamReference:
    league = league_id or _uuid("league-1")
    return m.TeamReference(
        teamId=_uuid(f"team-{team_suffix}"),
        leagueId=league,
        name=f"Team {team_suffix}",
        abbreviation=f"T{team_suffix}",
        manager="Coach Sample",
        record=m.Record(wins=5, losses=3, ties=0),
    )


def _player_summary(idx: int) -> m.PlayerSummary:
    return m.PlayerSummary(
        playerId=_uuid(f"player-{idx}"),
        fullName=f"Player {idx}",
        position="WR" if idx % 2 == 0 else "RB",
        team="NYJ" if idx % 2 == 0 else "KC",
        age=27,
        injury=m.InjuryStatus(
            status=m.Status.active,
            updatedAt=_now() - timedelta(days=1),
        ),
    )


def _projection_summary(base: float) -> m.ProjectionSummary:
    return m.ProjectionSummary(
        meanPoints=base,
        p20=base - 2.5,
        p50=base,
        p80=base + 3.1,
        boomProbability=0.2,
        bustProbability=0.1,
        provenance=_provenance("projection"),
    )


def league_list() -> m.LeagueListResponse:
    league = league_detail(_uuid("league-1"))
    return m.LeagueListResponse(total=1, page=1, pageSize=10, items=[league.league])


def league_detail(league_id: UUID) -> m.LeagueDetail:
    summary = m.LeagueSummary(
        leagueId=league_id,
        provider=m.ProviderId.yahoo,
        name="Sherlock League",
        season=2024,
        format="redraft",
        lastSyncAt=_now() - timedelta(minutes=30),
        teams=12,
        status=m.Status3.in_season,
    )
    teams = [_team_reference("1", league_id), _team_reference("2", league_id)]
    standings = [
        m.TeamStanding(team=teams[0], rank=1, pointsFor=820.5, pointsAgainst=790.1),
        m.TeamStanding(team=teams[1], rank=2, pointsFor=810.2, pointsAgainst=795.3),
    ]
    scoring = m.Scoring(type="PPR", ppr=1.0, bonusRules=["100yd bonus"])
    roster = m.RosterSettings(
        slots=[m.RosterSlotRule(slot="QB", count=1), m.RosterSlotRule(slot="RB", count=2)],
        benchSlots=6,
    )
    return m.LeagueDetail(
        league=summary,
        teams=teams,
        standings=standings,
        scoring=scoring,
        rosterSettings=roster,
        provenance=_provenance("league"),
    )


def team_lineup(team_id: UUID) -> m.TeamLineupResponse:
    period = m.ScoringPeriod(season=2024, week=8)
    player_one = _player_summary(1)
    player_two = _player_summary(2)
    lineup_slot = m.LineupSlot(
        slot="WR1",
        player=player_one,
        projected=_projection_summary(18.4),
        status=m.Status4.starting,
    )
    bench_slot = m.LineupSlot(
        slot="BENCH",
        player=player_two,
        projected=_projection_summary(12.1),
        status=m.Status4.bench,
    )
    return m.TeamLineupResponse(
        team=_team_reference("1"),
        period=period,
        lineup=[lineup_slot],
        bench=[bench_slot],
        totalProjected=30.5,
        totalActual=15.0,
        provenance=_provenance("lineup"),
    )


def optimize_lineup(team_id: UUID, request: m.OptimizationRequest) -> m.OptimizationResponse:
    optimized = m.OptimizationSlot(
        slot="FLEX",
        player=_player_summary(3),
        projection=_projection_summary(17.2),
        delta=3.2,
        reason="Higher ceiling in projected shootout",
    )
    bench = m.OptimizationSlot(
        slot="BENCH",
        player=_player_summary(4),
        projection=_projection_summary(10.5),
    )
    alternative = m.OptimizationAlternative(
        rank=1,
        projectedPoints=95.4,
        deltaFromBest=0.0,
        lineup=[optimized],
        changes=[
            m.Change(
                slot="FLEX",
                inPlayerId=optimized.player.playerId,
                outPlayerId=_uuid("player-5"),
            )
        ],
    )
    return m.OptimizationResponse(
        runId=_uuid("optimization-run"),
        submittedAt=_now(),
        objective=request.objective,
        resultLineup=[optimized],
        bench=[bench],
        alternatives=[alternative],
        insights=["Swap FLEX for upside"],
        provenance=_provenance("optimizer"),
    )


def projection_list() -> m.ProjectionListResponse:
    record = m.ProjectionRecord(
        player=_player_summary(6),
        period=m.ScoringPeriod(season=2024, week=8),
        projection=_projection_summary(16.7),
        opponent=m.Opponent(team="BUF", home=False, impliedTotal=24.5),
        usage=m.Usage(snapShare=0.72, routeShare=0.64, targetShare=0.21),
    )
    return m.ProjectionListResponse(total=1, page=1, pageSize=25, items=[record])


def player_list() -> m.PlayerListResponse:
    return m.PlayerListResponse(total=1, page=1, pageSize=25, items=[_player_summary(7)])


def player_detail(player_id: UUID) -> m.PlayerDetail:
    player = _player_summary(7)
    metrics = m.PlayerMetrics(
        season=2024,
        week=8,
        usage=m.Usage1(snapShare=0.68, routeShare=0.61, targetShare=0.19),
        efficiency=m.Efficiency(yprr=2.1, adot=10.4, successRate=0.47),
        context=m.Context1(paceRank=8, proe=0.04, matchupDifficulty="medium"),
        provenance=_provenance("metrics"),
    )
    projections = m.Projections(
        weekly=_projection_summary(17.8),
        ros=_projection_summary(15.3),
    )
    return m.PlayerDetail(
        player=player,
        metrics=metrics,
        projections=projections,
        recentGames=[m.RecentGame(season=2024, week=7, opponent="MIA", fantasyPoints=14.2)],
        insights=["Target share increasing week over week."],
    )


def waiver_list() -> m.WaiverListResponse:
    recommendation = m.WaiverRecommendation(
        player=_player_summary(8),
        projectedPoints=13.4,
        faab=m.FAABRange(low=5, medium=12, high=22),
        priority=1,
        recommendedAction=m.RecommendedAction.add,
        reason="Leads team in routes over last three weeks.",
        replacementComparison=m.ReplacementComparison(deltaPoints=2.3),
        provenance=_provenance("waivers"),
    )
    return m.WaiverListResponse(total=1, page=1, pageSize=10, items=[recommendation])


def trade_estimate(request: m.TradeEstimateRequest) -> m.TradeEstimateResponse:
    impacts = [
        m.TradeImpact(
            teamId=request.fromTeamId,
            projectedDelta=4.5,
            lineupChanges=[
                m.LineupChange(
                    slot="WR1",
                    inPlayerId=_uuid("player-9"),
                    outPlayerId=_uuid("player-10"),
                )
            ],
        ),
        m.TradeImpact(teamId=request.toTeamId, projectedDelta=-2.1, lineupChanges=[]),
    ]
    return m.TradeEstimateResponse(
        fairnessScore=0.62,
        recommendedAction=m.RecommendedAction1.counter,
        summary="Offer favors sending team by ~2 points per week.",
        teamImpacts=impacts,
        replacementImpact=m.ReplacementImpact(delta=1.1, teamId=request.fromTeamId),
        warnings=["Counter with additional depth."],
        provenance=_provenance("trade"),
    )


def refresh(scope: m.ScopeId, request: m.RefreshRequest | None) -> m.RefreshResponse:
    return m.RefreshResponse(
        scope=scope,
        status=m.Status5.queued,
        enqueuedAt=_now(),
        estimatedCompletion=_now() + timedelta(minutes=2),
        context={"requestedBy": "system"},
        provenance=_provenance("refresh"),
    )


def live_event() -> m.LiveImpactEvent:
    return m.LiveImpactEvent(
        eventId="evt-1",
        gameId="2024-NE-KC",
        playId=101,
        occurredAt=_now(),
        headline="Touchdown pass to Player 7",
        description="Player 7 caught a 25-yard touchdown pass.",
        impactType=m.ImpactType.touchdown,
        affectedPlayers=[
            m.AffectedPlayer(
                playerId=_uuid("player-7"),
                team="KC",
                impact="TD reception",
                pointsDelta=6.0,
            )
        ],
        fantasyImplications=["Starter scoring boost", "Matchup swing potential"],
        provenance=_provenance("live"),
        links=["https://example.com/highlight"],
    )
