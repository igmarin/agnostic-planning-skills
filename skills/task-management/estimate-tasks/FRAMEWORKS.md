# Estimation Frameworks Reference

Detailed framework definitions for the estimate-tasks skill. See SKILL.md for main workflow.

## Story Points (Fibonacci)

Use when the team tracks velocity or works in sprints. Points are relative, not hours.

| Points | Meaning |
|--------|---------|
| 1 | Trivial - near-zero unknowns, minutes of work |
| 2 | Small - well-understood, no surprises expected |
| 3 | Small-medium - clear scope, minor edge cases possible |
| 5 | Medium - some unknowns, may touch multiple areas |
| 8 | Large - significant complexity or cross-team dependencies |
| 13 | Very large - recommend splitting before estimating |
| 21+ | Epic - must be broken down; do not assign directly |

**When to use:**
- Agile teams with established velocity
- Sprint-based planning
- Relative sizing preferred over time estimates

## T-Shirt Sizes

Use when stakeholders prefer intuitive buckets over numeric precision.

| Size | Meaning |
|------|---------|
| XS | Trivial change |
| S | Well-scoped, low risk |
| M | Moderate scope, manageable unknowns |
| L | Complex, multiple components |
| XL | Very large; consider splitting |
| XXL | Must be decomposed first |

**When to use:**
- Stakeholder communication
- High-level roadmap planning
- When numeric precision adds false confidence

## Time Ranges

Use when stakeholders need rough calendar anchors (e.g., early discovery, fixed-bid scoping).

| Range | Typical use |
|-------|-------------|
| < 1 day | Hotfix, config change |
| 1-2 days | Small feature or isolated bug |
| 3-5 days | Standard feature with tests |
| 1-2 weeks | Multi-component work, moderate unknowns |
| 2-4 weeks | Large feature; strong candidate for splitting |
| > 1 month | Epic - must be broken down |

**When to use:**
- Fixed-bid projects
- Client communication needing calendar time
- Early discovery phases when velocity is unknown

## Framework Selection Guidelines

| Context | Recommended Framework |
|---------|----------------------|
| Internal agile team | Story points |
| Executive reporting | T-shirt sizes |
| Client contracts | Time ranges |
| Mixed audience | Start with story points, translate as needed |

> **Mixing frameworks:** Never mix frameworks within a single estimation table. If the user switches frameworks mid-session, re-estimate the full table.
