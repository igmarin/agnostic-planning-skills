---
name: plan-sprint
license: MIT
description: >
  Plans a sprint by selecting tickets from a prioritized backlog based on team
  capacity and historical velocity — start from top of backlog stop at ≤80%
  capacity, define a single sprint goal that all selected tickets support, use
  theoretical_capacity × 0.6 when no history exists or most recent sprint for
  declining trends, produce a ticket selection table with estimate and confidence.
  Language-agnostic — works with any tracker or estimation framework.
  Trigger words: plan sprint, sprint planning, sprint goal, sprint capacity,
  what should we work on this sprint, sprint backlog.
metadata:
  version: 1.0.0
  user-invocable: "true"
---
# Planning a Sprint

Select tickets, define a goal, and commit to a sprint scope.

## Quick Reference

- **Input:** Prioritized backlog, team capacity, sprint duration.
- **Output:** Sprint plan with selected tickets, sprint goal, capacity allocation.
- **Rule:** Don't overcommit — plan for ≤80% of theoretical capacity.

## HARD-GATE

```text
DO NOT commit more than the team's historical velocity.
DO NOT select tickets with unresolved dependencies or unclear acceptance criteria.
DO set a single, clear sprint goal that every selected ticket supports.
```

## Core Process

1. **Gather inputs** — prioritized backlog (from `prioritize-backlog`), team capacity, sprint dates, historical velocity.
2. **Define sprint goal** — one sentence describing the sprint's outcome. Every selected ticket should support this goal.
3. **Select tickets** — start from the top of the backlog, stop when total estimate reaches ≤80% of capacity (see [Capacity Heuristics](#capacity-heuristics) below).
4. **Validate** — check no ticket has unresolved dependencies, unclear acceptance criteria, or missing estimates. Use the [Common Anti-Patterns](#common-anti-patterns) table as a checklist.
5. **Flag** — tickets that almost made the cut (next sprint), dependency risks, stretch goals.
6. **Output** — sprint plan using the format in [Output Style](#output-style).

## Capacity Heuristics

Use when raw capacity or velocity data is unavailable or needs sanity-checking.

### Theoretical Capacity
- **Per person per day:** 6 productive hours (subtract meetings, reviews, interruptions).
- **Sprint capacity:** `team_size × sprint_days × 6h × utilisation_factor`
- **Utilisation factor:** 0.8 for stable teams; 0.6–0.7 for new or high-uncertainty teams.

### Velocity
- **Rolling average:** Mean completed points across last 3–5 sprints; exclude holiday/incident-disrupted sprints.
- **No history:** Use `theoretical_capacity × 0.6` as a conservative baseline.
- **Declining trend:** Use the most recent sprint's figure rather than the average.

### Common Anti-Patterns

| Anti-Pattern | Mitigation |
|---|---|
| Planning to 100% capacity | Cap at 80% |
| Including unestimated tickets | Estimate before committing |
| Multiple sprint goals | One goal per sprint |
| Ignoring dependencies | Resolve or defer dependents |
| Carry-over without re-estimation | Re-estimate carry-over tickets |

## Output Style

1. **Sprint header** — name, dates, duration, team capacity.
2. **Sprint goal** — one sentence.
3. **Selected tickets** — `| Rank | Ticket | Estimate | Confidence | Notes |`
4. **Capacity allocation** — total committed, buffer (%), stretch goals.
5. **Deferred** — top 3 items that didn't fit, for next sprint visibility.
6. **English only** unless user requests otherwise.

## Example Sprint Plan

> Reference output illustrating the expected structure and level of detail.

```
Sprint 14 | 2025-08-04 → 2025-08-15 | 10 days | Team: 4 engineers
Capacity: 4 × 10 × 6h × 0.8 = 192h | Velocity baseline: 38 pts

Sprint Goal: Enable customers to reset their own passwords without support intervention.

| Rank | Ticket  | Estimate | Confidence | Notes                        |
|------|---------|----------|------------|------------------------------|
| 1    | AUTH-42 | 8 pts    | High       | Core reset flow              |
| 2    | AUTH-43 | 5 pts    | High       | Email token service          |
| 3    | AUTH-44 | 3 pts    | High       | Rate-limiting middleware     |
| 4    | UI-88   | 5 pts    | Medium     | Reset UI — design ready      |
| 5    | AUTH-47 | 5 pts    | Medium     | Audit logging                |
| 6    | TEST-12 | 3 pts    | High       | E2E tests for reset flow     |

Total committed: 29 pts (76% of velocity — within 80% cap)
Buffer: 9 pts (24%)
Stretch goal: AUTH-50 (3 pts) — token expiry config, pull in if buffer allows.

Deferred (top candidates for Sprint 15):
1. AUTH-51 — SSO integration (13 pts) — too large, split first.
2. UI-90  — Account settings redesign (8 pts) — blocked on design review.
3. PERF-05 — Login latency optimisation (5 pts) — lower priority this cycle.
```

## Integration

| Skill | When to chain |
|---|---|
| **prioritize-backlog** | Use ordered backlog as input to ticket selection |
| **estimate-tasks** | Reference estimates for capacity-based selection |
| **identify-risks** | Scan sprint plan for dependency and capacity risks |
