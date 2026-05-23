---
name: estimate-tasks
license: MIT
description: >
  Assigns effort estimates to tasks using story points (Fibonacci), t-shirt sizes,
  or time ranges. Flags high-uncertainty items. Language-agnostic.
  Use when the user asks to estimate effort, size tasks, or assign story points to
  backlog items. Trigger words: estimate, story points, t-shirt size, effort, sizing, fibonacci.
metadata:
  version: 1.0.0
  user-invocable: "true"
---
# Estimating Task Effort

Assign relative complexity estimates. Focus on comparison, not calendar time.

## Quick Reference

- **Input:** Task list (from `generate-tasks`) or PRD requirements.
- **Frameworks:** Story points, t-shirt sizes, time ranges.
- **Output:** Each task annotated with estimate + confidence.
- **Rule:** Flag uncertainty — never fabricate precision.

## HARD-GATE

```text
DO NOT assign estimates you don't understand.
DO NOT default to "3 points" or "Medium" as a placeholder.
DO flag tasks needing further breakdown.
DO state confidence (high/medium/low) for every estimate.
```

## Core Process

1. **Receive** — task list or PRD requirements.
2. **Detect framework** — ask user or infer from context (see Estimation Frameworks below).
3. **Analyze each task** — scope, unknowns, whether it needs further breakdown.
4. **Assign** — relative sizing, confidence level per task.
5. **Flag** — low-confidence tasks (recommend spike), oversized tasks (recommend split).
6. **Output** — annotated task list.

## Estimation Frameworks

### Story Points (Fibonacci)
Use when the team tracks velocity or works in sprints. Points are relative, not hours.

| Points | Meaning |
|--------|---------|
| 1 | Trivial — near-zero unknowns, minutes of work |
| 2 | Small — well-understood, no surprises expected |
| 3 | Small-medium — clear scope, minor edge cases possible |
| 5 | Medium — some unknowns, may touch multiple areas |
| 8 | Large — significant complexity or cross-team dependencies |
| 13 | Very large — recommend splitting before estimating |
| 21+ | Epic — must be broken down; do not assign directly |

### T-Shirt Sizes
Use when stakeholders prefer intuitive buckets over numeric precision.

| Size | Meaning |
|------|---------|
| XS | Trivial change |
| S | Well-scoped, low risk |
| M | Moderate scope, manageable unknowns |
| L | Complex, multiple components |
| XL | Very large; consider splitting |
| XXL | Must be decomposed first |

### Time Ranges
Use when stakeholders need rough calendar anchors (e.g., early discovery, fixed-bid scoping).

| Range | Typical use |
|-------|-------------|
| < 1 day | Hotfix, config change |
| 1–2 days | Small feature or isolated bug |
| 3–5 days | Standard feature with tests |
| 1–2 weeks | Multi-component work, moderate unknowns |
| 2–4 weeks | Large feature; strong candidate for splitting |
| > 1 month | Epic — must be broken down |

> **Mixing frameworks:** Never mix frameworks within a single estimation table. If the user switches frameworks mid-session, re-estimate the full table.

## Output Style

1. **Framework** — state which framework was used and why.
2. **Estimation table** — `| ID | Task | Estimate | Confidence | Notes |`
3. **Flagged items** — tasks needing spikes or splits, with reasoning.
4. **Summary** — total estimate, confidence distribution, callouts.
5. **English only** unless user requests otherwise.

## Worked Example

**Framework:** Story points (Fibonacci) — inferred from backlog context.

| ID | Task | Estimate | Confidence | Notes |
|----|------|----------|------------|-------|
| T1 | Add user login via email/password | 3 | High | Well-understood auth pattern, existing library available |
| T2 | Build admin dashboard with role filtering | 8 | Medium | UI scope is clear; role logic may expand |
| T3 | Integrate payment gateway | ⚠️ TBD | Low | API complexity unknown — spike required before estimating |
| T4 | Write unit tests for auth module | 2 | High | Scope directly tied to T1, straightforward |

**Flagged items:**
- **T3 — "Integrate payment gateway":** Low confidence. Recommend a time-boxed spike (1–2 days) to evaluate API docs, sandbox availability, and edge-case handling before assigning points.

**Summary:** 3 estimated tasks total 13 points (High: 2, Medium: 1). T3 blocked pending spike. Re-estimate T3 after spike completes.

## Integration

| Skill | When to chain |
|-------|---------------|
| **generate-tasks** | Estimate tasks immediately after generation |
| **identify-risks** | After estimation, assess dependency and uncertainty risks |
| **plan-sprint** | Select tickets based on capacity vs estimates |
