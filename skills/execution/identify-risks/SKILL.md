---
name: identify-risks
license: MIT
description: >
  Scans plans and tasks for risks: dependency chains, single points of failure,
  ambiguous requirements, external deps, and capacity concerns. Produces a risk
  register with likelihood, impact, and mitigations. Language-agnostic.
  Trigger words: risks, risk assessment, blockers, what could go wrong, risk register.
metadata:
  version: 1.0.0
  user-invocable: "true"
---
# Identifying Project Risks

Scan plans for risks backed by concrete evidence — not speculation.

## Quick Reference

- **Input:** Task list, PRD, ticket set, or sprint plan.
- **Output:** Risk register (description, likelihood, impact, mitigation).
- **Rule:** Every risk cites specific evidence from the plan.

## HARD-GATE

```text
DO NOT fabricate risks. Every risk MUST reference a specific task or requirement.
DO NOT flag everything as high-risk — use the likelihood/impact matrix honestly.
DO NOT skip mitigations — every risk needs at least one concrete mitigation.
```

## Core Process

1. **Receive** — task list, PRD, ticket set, or sprint plan.
2. **Scan risk patterns** (see [RISK_PATTERNS.md](./RISK_PATTERNS.md)) — dependency chains, external deps, ambiguity, single points of failure, capacity, technical uncertainty.
3. **Classify** — Likelihood (High/Medium/Low), Impact (High/Medium/Low), Proximity (Immediate/Near-term/Future).
4. **Suggest mitigations** — prevention, contingency, owner.
5. **Output** — structured risk register.

## Extended Resources (Progressive Disclosure)

Load these files only when needed:

- **[RISK_PATTERNS.md](./RISK_PATTERNS.md)** — Catalog of 6 risk patterns with examples.

## Output Style

1. **Risk Register** — `| ID | Risk | Likelihood | Impact | Proximity | Evidence | Mitigation |`
2. **Summary** — count by severity and proximity.
3. **Top 3 risks** — detailed mitigation recommendations.
4. **Assumptions** — about team, timeline, or external factors.
5. **English only** unless user requests otherwise.

## Integration

| Skill | When to chain |
| **estimate-tasks** | After estimation, assess risks from high-uncertainty tasks |
| **generate-tasks** | After task breakdown, identify dependency risks |
| **generate-status-report** | Include risk updates in stakeholder status reports |
