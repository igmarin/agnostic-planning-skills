---
name: plan-sprint
license: MIT
description: >
  Plans a sprint: selects tickets from a prioritized backlog based on team capacity
  and historical velocity, defines a sprint goal, and produces a sprint plan.
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
3. **Select tickets** — start from the top of the backlog, stop when total estimate reaches ≤80% of capacity (see [SPRINT_PLANNING_GUIDE.md](./SPRINT_PLANNING_GUIDE.md) for capacity heuristics).
4. **Validate** — check no ticket has unresolved dependencies, unclear acceptance criteria, or missing estimates.
5. **Flag** — tickets that almost made the cut (next sprint), dependency risks, stretch goals.
6. **Output** — sprint plan.

## Extended Resources (Progressive Disclosure)

Load these files only when needed:

- **[SPRINT_PLANNING_GUIDE.md](./SPRINT_PLANNING_GUIDE.md)** — Capacity heuristics, velocity calculations, and common sprint planning anti-patterns.

## Output Style

1. **Sprint header** — name, dates, duration, team capacity.
2. **Sprint goal** — one sentence.
3. **Selected tickets** — `| Rank | Ticket | Estimate | Confidence | Notes |`
4. **Capacity allocation** — total committed, buffer (%), stretch goals.
5. **Deferred** — top 3 items that didn't fit, for next sprint visibility.
6. **English only** unless user requests otherwise.

## Integration

| Skill | When to chain |
| **prioritize-backlog** | Use ordered backlog as input to ticket selection |
| **estimate-tasks** | Reference estimates for capacity-based selection |
| **identify-risks** | Scan sprint plan for dependency and capacity risks |
