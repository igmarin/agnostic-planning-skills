---
name: estimate-tasks
license: MIT
description: >
  Assigns effort estimates to tasks using story points (Fibonacci), t-shirt sizes,
  or time ranges. Flags high-uncertainty items. Language-agnostic.
  Trigger words: estimate, story points, t-shirt size, effort, sizing, fibonacci.
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
2. **Detect framework** — ask user or infer from context (see [ESTIMATION_FRAMEWORKS.md](./ESTIMATION_FRAMEWORKS.md) for scale details).
3. **Analyze each task** — scope, unknowns, whether it needs further breakdown.
4. **Assign** — relative sizing, confidence level per task.
5. **Flag** — low-confidence tasks (recommend spike), oversized tasks (recommend split).
6. **Output** — annotated task list.

## Extended Resources (Progressive Disclosure)

Load these files only when needed:

- **[ESTIMATION_FRAMEWORKS.md](./ESTIMATION_FRAMEWORKS.md)** — Story point, t-shirt, and time-range scales with usage guidance.

## Output Style

1. **Framework** — state which framework was used and why.
2. **Estimation table** — `| ID | Task | Estimate | Confidence | Notes |`
3. **Flagged items** — tasks needing spikes or splits, with reasoning.
4. **Summary** — total estimate, confidence distribution, callouts.
5. **English only** unless user requests otherwise.

## Integration

| Skill | When to chain |
| **generate-tasks** | Estimate tasks immediately after generation |
| **identify-risks** | After estimation, assess dependency and uncertainty risks |
| **plan-sprint** | Select tickets based on capacity vs estimates |
