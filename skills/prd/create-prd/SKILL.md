---
name: create-prd
type: atomic
license: MIT
description: >
  Drafts a clear actionable PRD from a feature — focus on what/why, no code,
  write requirements in natural language, fill PRD_TEMPLATE.md section by section
  without inventing parallel outline, clarify then draft then get approval, save
  to /tasks/prd-SLUG.md in kebab-case, close with next steps like "run generate-tasks once approved".
  Language-agnostic.
  Trigger words: PRD, product requirements, plan a feature, write a spec,
  requirements document.
metadata:
  version: 1.0.0
  user-invocable: "true"
---
# Generating a Product Requirements Document (PRD)

Focus on *what* and *why*, not *how*. No code until the PRD is approved.

## Quick Reference

- **Goal:** Draft a clear, actionable PRD from a feature request.
- **Constraints:** Focus on what/why. No code. Save to `/tasks/prd-<slug>.md`.
- **Flow:** Clarify if ambiguous → Draft using template → Get explicit approval.

## HARD-GATE

```text
Focus exclusively on WHAT and WHY, not HOW.
DO NOT include code, pseudo-code, SQL, class names, or method signatures.
DO NOT generate tasks or code until the PRD is explicitly approved.
```

## Core Process

1. **Receive prompt** — feature description or request.
2. **Clarify only if needed** — if scope is clear, skip questions and draft. If ambiguous, ask 3–5 targeted questions (see [assets/prd_questions.md](./assets/prd_questions.md)).
3. **Draft** — fill **[PRD_TEMPLATE.md](./PRD_TEMPLATE.md)** section by section. Do not invent a parallel outline.
4. **Validate** — present the PRD; get **explicit approval** before tasks or code.

## Extended Resources (Progressive Disclosure)

Load these files only when their specific content is needed:

- **[PRD_TEMPLATE.md](./PRD_TEMPLATE.md)** — Mandatory Markdown structure every PRD follows.
- **[assets/prd_questions.md](./assets/prd_questions.md)** — Clarification inventory. Pick 3–5 questions; do not run all 12.
- **[assets/examples.md](./assets/examples.md)** — Short one-pager + full PRD example.

## Output Style

1. **Save to** `/tasks/prd-<feature-slug>.md` (kebab-case). State the path.
2. **Follow the template** section by section. Every section appears, even if "TBD".
3. **Write requirements in natural language** — not code. "The system must send a confirmation email when…"
4. **Close with next steps** — typically: "Run `generate-tasks` once this PRD is approved."
5. **Request explicit approval** before any implementation or task generation.
6. **English only** unless the user requests otherwise.

After saving, surface the file path and request explicit approval.

## Integration

| Skill | When to chain |
|-------|---------------|
| **generate-tasks** | After PRD approved, to derive implementation steps |
| **plan-tickets** | When tracker tickets are needed from the approved PRD scope |
