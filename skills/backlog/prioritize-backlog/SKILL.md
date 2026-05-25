---
name: prioritize-backlog
license: MIT
description: >
  Prioritizes a backlog using a framework (RICE MoSCoW value-vs-effort WSJF) —
  rank items by impact and urgency not gut feeling, produce an ordered backlog
  table with Rank Item Score Rationale, and justify every ranking decision.
  Language-agnostic.
  Trigger words: prioritize, backlog, RICE, MoSCoW, ranking, what should we build first,
  value vs effort, WSJF, priority order.
metadata:
  version: 1.0.0
  user-invocable: "true"
---
# Prioritizing a Backlog

Rank work items by impact and urgency. Use a framework — not gut feeling.

## Quick Reference

- **Input:** Ticket list, task list, or feature requests.
- **Frameworks:** RICE, MoSCoW, value-vs-effort, WSJF.
- **Output:** Ordered backlog with scores and rationale.
- **Rule:** Every ranking decision needs a stated reason.

## HARD-GATE

```text
DO NOT prioritize without understanding each item's impact and effort.
DO NOT assign scores without stated criteria for each dimension.
DO NOT rank everything "high priority" — force relative ordering.
```

## Core Process

1. **Receive** — ticket list, task list, or feature requests.
2. **Detect framework** — ask user or infer from context (see scoring criteria below):
   - **RICE** — Reach × Impact × Confidence ÷ Effort.
   - **MoSCoW** — Must have, Should have, Could have, Won't have.
   - **Value-vs-Effort** — Plot on a 2×2 matrix.
   - **WSJF** — Cost of Delay ÷ Job Size.
3. **Score each item** — apply the framework consistently, state rationale.
4. **Order** — rank by score, with ties broken by strategic alignment or dependencies.
5. **Flag** — items needing clarification before scoring, dependency conflicts.
6. **Output** — ordered backlog.

## Inline Scoring Criteria

### RICE
| Dimension | Scale | Notes |
|-----------|-------|-------|
| Reach | # users/period | Estimate users affected per quarter |
| Impact | 0.25 / 0.5 / 1 / 2 / 3 | Minimal → Massive |
| Confidence | 50% / 80% / 100% | Low / Medium / High |
| Effort | Person-weeks | Total across team |

**Formula:** `(Reach × Impact × Confidence) ÷ Effort` — higher score = higher priority.

### MoSCoW
- **Must** — without it the release fails or is illegal.
- **Should** — high value, painful to omit but workable.
- **Could** — nice to have; cut first under time pressure.
- **Won't** — explicitly deferred; document why.

### Value-vs-Effort (2×2)
- **High value / Low effort** → Do first (quick wins).
- **High value / High effort** → Schedule carefully (big bets).
- **Low value / Low effort** → Fill-in work only.
- **Low value / High effort** → Eliminate or defer.

### WSJF
| Dimension | Scale 1–10 | Notes |
|-----------|------------|-------|
| User/Business value | 1–10 | Revenue, satisfaction, risk reduction |
| Time criticality | 1–10 | Value decays over time? |
| Risk reduction / opportunity | 1–10 | Unlocks other work or removes risk |
| Job size | 1–10 | Relative effort (higher = bigger) |

**Formula:** `(User value + Time criticality + Risk reduction) ÷ Job size`.

## Worked Example — RICE

Input: four feature requests for a SaaS product.

| Rank | Item | Reach | Impact | Confidence | Effort (wks) | RICE Score | Rationale |
|------|------|-------|--------|------------|--------------|------------|-----------|
| 1 | Bulk CSV export | 800 | 2 | 80% | 2 | **640** | High reach (power users), medium effort, strong confidence |
| 2 | SSO / SAML login | 200 | 3 | 80% | 4 | **120** | High impact per user (enterprise blocker), higher effort |
| 3 | Dark mode | 1 000 | 0.5 | 100% | 3 | **167** | Wide reach but low impact; bumped below SSO due to strategic weight |
| 4 | CSV import wizard | 150 | 1 | 50% | 3 | **25** | Low confidence in estimates; flag for refinement |

**Flagged:** "CSV import wizard" — effort estimate uncertain, revisit after spike.

## Output Style

1. **Framework** — state which framework was used and why.
2. **Ordered backlog** — `| Rank | Item | Score | Rationale |`
3. **Framework breakdown** — per-item dimension scores (for scored frameworks).
4. **Flagged items** — items needing clarification or with dependency constraints.
5. **English only** unless user requests otherwise.

## Integration

| Skill | When to chain |
|-------|---------------|
| **plan-tickets** | Prioritize tickets after they are drafted |
| **plan-sprint** | Use ordered backlog to select sprint candidates |
| **estimate-tasks** | Use estimates as input to effort-based frameworks |
