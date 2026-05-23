# Sprint Planning Guide

## Capacity Heuristics

**The 80% Rule:** Never commit to more than 80% of theoretical capacity. The other 20% covers meetings, interruptions, bug fixes, and unexpected complexity.

| Team size | Sprint length | Typical capacity (story points) | 80% commit target |
|-----------|-------------|--------------------------------|-------------------|
| 3 devs | 1 week | 15-20 | 12-16 |
| 3 devs | 2 weeks | 30-40 | 24-32 |
| 5 devs | 1 week | 25-35 | 20-28 |
| 5 devs | 2 weeks | 50-70 | 40-56 |

These are starting points. Replace with the team's actual historical velocity.

---

## Using Historical Velocity

1. Look at the last 3-4 sprints.
2. Take the average completed points per sprint.
3. Use that average as capacity, not the theoretical maximum.
4. If velocity is trending down, investigate why before committing to the next sprint.

---

## Sprint Goal Quality

A good sprint goal:
- Is a single outcome, not a list of tasks.
- Every ticket in the sprint directly supports it.
- Can be stated in one sentence: "Users can log in with Google OAuth."
- Answers: "At the end of this sprint, the team has delivered _____."

**Bad:** "Work on authentication and fix bugs."
**Good:** "Users can sign up and log in using their Google account."

---

## Common Anti-Patterns

| Anti-Pattern | Why it's bad | Fix |
|-------------|-------------|-----|
| Overcommitting (100%+ capacity) | Guaranteed to miss the sprint goal | Cap at 80%, use historical velocity |
| No sprint goal | Team works on unrelated items, no cohesive outcome | Define a single goal first, then select tickets |
| Selecting unestimated tickets | Can't tell if they fit in capacity | Estimate before sprint commitment |
| Including tickets with unresolved dependencies | Sprint blocked waiting for external team | Move to next sprint or add as blocked with contingency |
| Sprint goal is "finish all tickets" | Not a goal — it's a tautology | Define the outcome the tickets deliver |
