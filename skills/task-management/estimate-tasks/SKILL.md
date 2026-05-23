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
- **Rule:** Flag uncertainty - never fabricate precision.

## HARD-GATE

```text
DO NOT assign estimates you don't understand.
DO NOT default to "3 points" or "Medium" as a placeholder.
DO flag tasks needing further breakdown.
DO state confidence (high/medium/low) for every estimate.
```

## Core Process

1. **Receive** - task list or PRD requirements.
2. **Detect framework** - ask user or infer from context (see Estimation Frameworks below).
3. **Analyze each task** - scope, unknowns, whether it needs further breakdown.
4. **Assign** - relative sizing, confidence level per task.
5. **Flag** - low-confidence tasks (recommend spike), oversized tasks (recommend split).
6. **Output** - annotated task list.

## Estimation Frameworks

See `FRAMEWORKS.md` for detailed framework definitions and selection guidelines.

### Quick Reference

| Framework | When to Use |
|-----------|------------|
| Story points | Agile teams, sprint planning |
| T-shirt sizes | Stakeholder communication |
| Time ranges | Client contracts, calendar needs |

> **Mixing frameworks:** Never mix frameworks within a single estimation table. If the user switches frameworks mid-session, re-estimate the full table.

## Output Style

1. **Framework** - state which framework was used and why.
2. **Estimation table** - `| ID | Task | Estimate | Confidence | Notes |`
3. **Flagged items** - tasks needing spikes or splits, with reasoning.
4. **Summary** - total estimate, confidence distribution, callouts.
5. **English only** unless user requests otherwise.

## Worked Example

**Framework:** Story points (Fibonacci) - inferred from backlog context.

| ID | Task | Estimate | Confidence | Notes |
|----|------|----------|------------|-------|
| T1 | Add user login via email/password | 3 | High | Well-understood auth pattern, existing library available |
| T2 | Build admin dashboard with role filtering | 8 | Medium | UI scope is clear; role logic may expand |
| T3 | Integrate payment gateway | WARNING TBD | Low | API complexity unknown - spike required before estimating |
| T4 | Write unit tests for auth module | 2 | High | Scope directly tied to T1, straightforward |

**Flagged items:**
- **T3 - "Integrate payment gateway":** Low confidence. Recommend a time-boxed spike (1-2 days) to evaluate API docs, sandbox availability, and edge-case handling before assigning points.

**Summary:** 3 estimated tasks total 13 points (High: 2, Medium: 1). T3 blocked pending spike. Re-estimate T3 after spike completes.

## Integration

| Skill | When to chain |
|-------|---------------|
| **generate-tasks** | Estimate tasks immediately after generation |
| **identify-risks** | After estimation, assess dependency and uncertainty risks |
| **plan-sprint** | Select tickets based on capacity vs estimates |
