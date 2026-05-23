---
name: generate-status-report
license: MIT
description: >
  Generates a structured stakeholder status report from task progress and blocker
  data. Follows a standard template: executive summary, accomplishments, in-progress,
  blockers, risks, next steps. Language-agnostic.
  Trigger words: status report, sprint update, stakeholder update, progress report,
  weekly update, project status.
metadata:
  version: 1.0.0
  user-invocable: "true"
---
# Generating a Status Report

Produce a clear, honest status report. Focus on progress, blockers, and what's next.

## Quick Reference

- **Input:** Task progress, sprint info, blocker list, risk register (optional).
- **Output:** Structured markdown report.
- **Sections:** Executive Summary, Accomplishments, In Progress, Blocked, Risks, Next Steps.
- **Rule:** Never fabricate progress — mark unknowns as "needs update."

## HARD-GATE

```text
DO NOT fabricate or assume progress. Unknown → "Status unknown — needs update."
DO NOT hide blockers or risks to make the report look better.
DO NOT use passive language ("was delayed" → "Blocked on Y, owner: Z").
```

## Core Process

1. **Gather** — task progress, sprint info, blocker list, optional risk register.
2. **Categorize** — Accomplished, In Progress, Blocked, Upcoming.
3. **Write Executive Summary** — 2-4 sentences: health, key accomplishment, top concern.
4. **Fill template** — follow [STATUS_REPORT_TEMPLATE.md](./STATUS_REPORT_TEMPLATE.md) section by section.
5. **Review** — verify no status is fabricated or assumed.

## Extended Resources (Progressive Disclosure)

Load these files only when needed:

- **[STATUS_REPORT_TEMPLATE.md](./STATUS_REPORT_TEMPLATE.md)** — Standard report structure.

## Output Style

1. **Header** — project/sprint name, period, date.
2. **Executive Summary** — health (On Track / At Risk / Blocked), key accomplishment, top concern.
3. **Accomplishments** — bulleted list with brief context.
4. **In Progress** — `| Task | Owner | Status | ETA |`
5. **Blocked** — `| Task | Blocker | Owner | Resolution Plan |`
6. **Risks & Concerns** — top 3-5, with status changes since last report.
7. **Next Steps** — what's happening before the next report.
8. **English only** unless user requests otherwise.

## Integration

| Skill | When to chain |
| **identify-risks** | Include latest risk register in the status report |
| **estimate-tasks** | Reference estimates when reporting vs planned effort |
| **product-owner** | Report on PRD-aligned scope and scope changes |
