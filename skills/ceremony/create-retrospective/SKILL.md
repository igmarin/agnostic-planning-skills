---
name: create-retrospective
license: MIT
description: >
  Generates a sprint retrospective from sprint data feedback and metrics —
  cover what went well what didn't and action items, group related feedback into
  themes, ensure every "what didn't" has at least one specific owned time-bound
  action item, use the retrospective template when available, include Owner
  Timeline and Linked Issue columns.
  Language-agnostic.
  Trigger words: retrospective, retro, sprint review, what went well, what didn't,
  improvement items, lessons learned, sprint retrospective.
metadata:
  version: 1.0.0
  user-invocable: "true"
---
# Creating a Sprint Retrospective

Generate a structured retrospective focused on learning and actionable improvements.

## Quick Reference

- **Input:** Sprint data (goal, completed/not completed), team feedback, metrics.
- **Output:** Retrospective document with action items.
- **Sections:** What Went Well, What Didn't, Action Items, Metrics, Kudos.
- **Rule:** Every "what didn't" needs an action item with an owner.

## HARD-GATE

```text
DO NOT fabricate feedback — only include input the team actually provided.
DO NOT skip action items — every "what didn't" must have at least one action.
DO assign an owner and timeline to every action item.
```

## Core Process

1. **Gather** — sprint data (goal met? completed/not completed tickets), team feedback, relevant metrics.
2. **Categorize**:
   - **What Went Well** — wins, effective practices, things to continue.
   - **What Didn't** — blockers, bottlenecks, process issues, surprises.
   - **Kudos** — shout-outs and recognition.
3. **Identify themes** — group related feedback into themes rather than listing raw comments.
4. **Draft action items** — specific, owned, time-bound. Use the template in [RETROSPECTIVE_TEMPLATE.md](./RETROSPECTIVE_TEMPLATE.md) if available; otherwise use the inline minimal template below.
5. **Review** — verify every "what didn't" maps to an action item.

## Extended Resources (Progressive Disclosure)

Load these files only when needed:

- **[RETROSPECTIVE_TEMPLATE.md](./RETROSPECTIVE_TEMPLATE.md)** — Standard retrospective structure with examples (if bundled). If not available, use the minimal template below.

### Minimal Inline Template

Use this when `RETROSPECTIVE_TEMPLATE.md` is not available in the bundle:

```
## Sprint [Name/Number] Retrospective
**Dates:** YYYY-MM-DD – YYYY-MM-DD  |  **Goal:** <goal text>  |  **Goal Met:** Yes / No / Partial

### What Went Well
- **[Theme: CI Pipeline]** Automated tests caught three regressions before merge — saved estimated 4 h of manual QA.

### What Didn't
- **[Theme: Unclear Requirements]** Two tickets were blocked mid-sprint due to missing acceptance criteria → see Action #1.

### Action Items
| # | Action | Owner | Timeline | Linked Issue |
|---|--------|-------|----------|--------------|
| 1 | Add acceptance criteria checklist to Definition of Ready | Product Owner | Next sprint kickoff | PROJ-42 |

### Metrics
- Velocity: 34 pts committed / 28 pts completed (82%)
- Carried over: 2 tickets

### Kudos
- Alice for unblocking the auth service on short notice.
```

## Output Notes

- Use **English only** unless the user requests otherwise.
- Follow the section order in the template: header → What Went Well → What Didn't → Action Items → Metrics → Kudos.
- Themed bullets should include specific examples; the action item table must always include Owner, Timeline, and Linked Issue columns.

## Integration

| Skill | When to chain |
|-------|---------------|
| **plan-sprint** | Review the sprint plan vs what was actually delivered |
| **generate-status-report** | Include retrospective insights in the next status report |
| **project-manager** | Feed action items into the execution tracking pipeline |
