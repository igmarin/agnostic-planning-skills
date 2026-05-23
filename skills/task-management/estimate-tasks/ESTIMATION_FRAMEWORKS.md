# Estimation Frameworks Reference

## Story Points (Fibonacci)

Best for: Scrum teams doing relative sizing. Most common in software development.

**Scale:** 1, 2, 3, 5, 8, 13, 21

| Points | Meaning | Typical scope |
|--------|---------|---------------|
| 1 | Trivial | Typo fix, config change, one-line change |
| 2 | Small | Simple endpoint, well-known pattern |
| 3 | Medium | Standard feature slice, known conventions |
| 5 | Large | Multiple files, moderate complexity |
| 8 | Complex | New integration, multi-service coordination |
| 13 | Very complex | New subsystem, significant unknowns |
| 21 | Epic | Needs decomposition — split into smaller tasks |

**Rules:**
- Use relative sizing: "Is this task bigger or smaller than that 5-point task?"
- 1 point = baseline (the smallest task you can think of).
- If a task is 13+, recommend splitting.
- Story points measure complexity + effort + uncertainty, not time.

---

## T-Shirt Sizes

Best for: Early-stage estimation, roadmap planning, or non-Scrum teams.

**Scale:** XS, S, M, L, XL

| Size | Meaning | Approx story point equivalent |
|------|---------|------------------------------|
| XS | Minutes to hours | 1 |
| S | Hours to 1 day | 2-3 |
| M | 1-3 days | 5 |
| L | 3-5 days | 8 |
| XL | 1-2 weeks | 13+ |

**Rules:**
- Useful when the team hasn't calibrated on story points.
- Good for stakeholder-facing estimates (more intuitive than points).
- XL items should be broken down before sprint commitment.

---

## Time Ranges

Best for: Teams that estimate in calendar time. Less common in Agile, but used in some organizations.

**Scale:** <1 day, 1-3 days, 3-5 days, 1-2 weeks, 2+ weeks

**Rules:**
- Time estimates are the least reliable — they ignore uncertainty and complexity.
- Always pair time estimates with confidence levels.
- Convert to a range, not a single number: "3-5 days" not "4 days."
- 2+ week tasks must be decomposed.
