---
name: review-prd
license: MIT
description: >
  Reviews a PRD for completeness, testability, clarity, and feasibility.
  Produces findings categorized as Critical (blocking), Suggestion, or Note.
  Language-agnostic — evaluates structure and content, not technology.
  Trigger words: review PRD, PRD review, validate PRD, feasibility check.
metadata:
  version: 1.0.0
  user-invocable: "true"
---
# Reviewing a Product Requirements Document

Evaluate a PRD for quality — not agreement with a preferred solution. Focus on whether it's complete, clear, and actionable.

## Quick Reference

- **Input:** A PRD (from `create-prd` or existing document).
- **Output:** Findings as Critical, Suggestion, or Note.
- **Checks:** Completeness, testability, ambiguity, feasibility, edge cases, dependencies.
- **Rule:** Every finding cites the specific PRD section as evidence.

## HARD-GATE

```text
DO NOT review the idea — review the document's quality.
DO NOT suggest alternative solutions unless a requirement is infeasible.
EVERY finding MUST cite the specific PRD section, line, or requirement.
```

## Core Process

1. **Receive the PRD** — from `create-prd`, user document, or `/tasks/prd-*.md`.
2. **Scan the checklist** (see [REVIEW_CHECKLIST.md](./REVIEW_CHECKLIST.md)) — covers completeness, testability, clarity, feasibility, scope, dependencies, and edge cases.
3. **Classify:** Critical (blocks implementation), Suggestion (improves it), Note (observation).
4. **Produce** — findings table with severity, evidence, and recommendation.
5. **Verdict:** Approved / Approved with Suggestions / Needs Revision.

## Extended Resources (Progressive Disclosure)

Load these files only when needed:

- **[REVIEW_CHECKLIST.md](./REVIEW_CHECKLIST.md)** — Comprehensive checklist organized by PRD section.

## Output Style

1. **Verdict** — Approved / Approved with Suggestions / Needs Revision.
2. **Findings table** — `| # | Severity | Section | Finding | Evidence | Recommendation |`
3. **Summary** — count by severity + one-paragraph assessment.
4. **What's Good** — acknowledge well-written sections.
5. **English only** unless user requests otherwise.

## Integration

| Skill | When to chain |
| **create-prd** | Review immediately after PRD generation |
| **generate-tasks** | After review passes, proceed to task breakdown |
| **tech-lead** agent | For deeper feasibility and estimation quality review |
