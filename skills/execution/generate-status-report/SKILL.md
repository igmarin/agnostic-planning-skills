---
name: generate-status-report
license: MIT
description: >
  Generates a stakeholder status report from task data — never fabricate progress
  mark unknowns as "needs update", include Executive Summary (health key
  accomplishment top concern) then accomplishments in-progress blockers risks and
  next steps, verify no status is fabricated or assumed.
  Language-agnostic.
  Trigger words: status report, sprint update, stakeholder update, progress report,
  weekly update, project status.
metadata:
  version: 1.0.0
  user-invocable: "true"
---
# Generating a Status Report

Produce a clear, honest status report. Focus on progress, blockers, and what's next.

## HARD-GATE

```text
DO NOT fabricate or assume progress. Unknown → "Status unknown — needs update."
DO NOT hide blockers or risks to make the report look better.
DO NOT use passive language ("was delayed" → "Blocked on Y, owner: Z").
```

## Core Process

- **Input:** Task progress, sprint info, blocker list, risk register (optional).
- **Output:** Structured markdown report with sections: Executive Summary, Accomplishments, In Progress, Blocked, Risks, Next Steps.
- **Rule:** Never fabricate progress — mark unknowns as "needs update."

1. **Gather** — task progress, sprint info, blocker list, optional risk register.
2. **Categorize** — Accomplished, In Progress, Blocked, Upcoming.
3. **Write Executive Summary** — 2-4 sentences: health, key accomplishment, top concern.
4. **Fill template** — follow the STATUS_REPORT_TEMPLATE below, section by section.
5. **Review** — verify no status is fabricated or assumed.

## STATUS_REPORT_TEMPLATE

```markdown
# Status Report: [Project / Sprint Name]
**Period:** [Start Date] – [End Date]   **Prepared:** [Date]   **Author:** [Name]

## Executive Summary
**Health:** On Track | At Risk | Blocked
[2-4 sentences: overall health, key accomplishment, top concern.]

## Accomplishments
- [Task / milestone completed] — [brief context, e.g., "merged PR #42, closes Auth epic"]
- …

## In Progress
| Task | Owner | Status | ETA |
|------|-------|--------|-----|
| [Task name] | [Owner] | [% or narrative] | [Date] |

## Blocked
| Task | Blocker | Owner | Resolution Plan |
|------|---------|-------|------------------|
| [Task name] | [Specific blocker description] | [Owner] | [Next action + target date] |

## Risks & Concerns
| # | Risk | Likelihood | Impact | Status Change |
|---|------|-----------|--------|---------------|
| 1 | [Risk description] | High/Med/Low | High/Med/Low | New / Unchanged / Resolved |

## Next Steps
- [Action] — Owner: [Name], Due: [Date]
- …
```

## Concrete Example

**Sample input (provided by user or gathered from context):**

```
Sprint 14 | May 6–10 2025
Done: Deploy auth service to staging (owner: Ana)
In Progress: API rate-limiting (owner: Ben, 60%, ETA May 10); Dashboard redesign (owner: Cara, 30%, ETA May 14)
Blocked: Payment integration — third-party API keys not received, owner: Dan, escalated to procurement May 7
Risk: Rate-limiting miss could delay beta by one week
```

**Resulting report excerpt:**

```markdown
# Status Report: Sprint 14
**Period:** May 6–10 2025   **Prepared:** May 10 2025   **Author:** Agent

## Executive Summary
**Health:** At Risk
Auth service is deployed to staging on schedule. API rate-limiting is on track for
Friday but payment integration is blocked pending third-party credentials, putting the
beta timeline at risk by up to one week.

## Accomplishments
- Auth service deployed to staging — closes Sprint 13 carry-over (owner: Ana)

## In Progress
| Task | Owner | Status | ETA |
|------|-------|--------|-----|
| API rate-limiting | Ben | 60% | May 10 |
| Dashboard redesign | Cara | 30% | May 14 |

## Blocked
| Task | Blocker | Owner | Resolution Plan |
|------|---------|-------|------------------|
| Payment integration | Third-party API keys not received | Dan | Escalated to procurement May 7; follow up May 10 |

## Risks & Concerns
| # | Risk | Likelihood | Impact | Status Change |
|---|------|-----------|--------|---------------|
| 1 | Rate-limiting slip delays beta | Medium | High | New |

## Next Steps
- Confirm API keys received — Owner: Dan, Due: May 10
- Complete rate-limiting — Owner: Ben, Due: May 10
```

## Integration

| Skill | When to chain |
|-------|---------------|
| **identify-risks** | Include latest risk register in the status report |
| **estimate-tasks** | Reference estimates when reporting vs planned effort |
| **product-owner** | Report on PRD-aligned scope and scope changes |
