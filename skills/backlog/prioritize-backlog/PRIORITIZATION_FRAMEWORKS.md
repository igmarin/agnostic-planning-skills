# Prioritization Frameworks Reference

## RICE

**Formula:** Reach × Impact × Confidence ÷ Effort

| Dimension | Scale | Meaning |
|-----------|-------|---------|
| **Reach** | 1–10 | How many users/customers affected in a quarter? |
| **Impact** | 1–10 | How much does this move the needle? (1=minimal, 10=massive) |
| **Confidence** | 0.1–1.0 | How certain are you about the reach/impact/effort estimates? (1.0=high, 0.5=medium, 0.1=low) |
| **Effort** | 1–10 | Person-weeks or relative effort |

**Example:**
- Reach: 500 users = 6
- Impact: Significant improvement = 7
- Confidence: Medium = 0.7
- Effort: 2 person-weeks = 3
- **RICE Score:** (6 × 7 × 0.7) ÷ 3 = 9.8

Higher score = higher priority.

---

## MoSCoW

Categorical prioritization — no numeric scoring.

| Category | Meaning | Allocation guideline |
|----------|---------|---------------------|
| **Must have** | Critical for launch. Without it, the release fails. | ≤ 60% of capacity |
| **Should have** | Important but not critical. Can work around it. | ≤ 20% of capacity |
| **Could have** | Nice to have. Include if time allows. | ≤ 20% of capacity |
| **Won't have** | Explicitly deferred. Not in this release. | Documented for future |

**Rules:**
- "Must have" items must be justified with a concrete consequence of not doing them.
- If >60% of items are "Must have," the categorization is too generous.

---

## Value vs Effort

Plot items on a 2×2 matrix:

```
        High Value
            |
  Quick Wins | Strategic
  (do first) | (plan carefully)
            |
  -----------+----------- Effort
            |
  Fill-ins   | Thankless
  (defer)    | (avoid)
            |
        Low Value
```

**Quadrants:**
- **Quick Wins** (high value, low effort) — Do first.
- **Strategic** (high value, high effort) — Plan and resource carefully.
- **Fill-ins** (low value, low effort) — Defer; do when there's slack.
- **Thankless** (low value, high effort) — Avoid unless required.

---

## WSJF (Weighted Shortest Job First)

**Formula:** Cost of Delay ÷ Job Size

| Dimension | Meaning |
|-----------|---------|
| **Cost of Delay** | What's the weekly cost of NOT doing this? (revenue, user impact, technical debt accumulation) |
| **Job Size** | Relative size (1–10, using story points or relative estimation) |

**Example:**
- Cost of Delay: $5,000/week = 8
- Job Size: 3 points
- **WSJF Score:** 8 ÷ 3 = 2.7

Higher score = higher priority. Do the highest-WSJF items first.
