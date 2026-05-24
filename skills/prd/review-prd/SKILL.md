---
name: review-prd
license: MIT
description: >
  Reviews a Product Requirements Document (PRD) for completeness, testability, clarity, and feasibility.
  Produces findings categorized as Critical (blocking), Suggestion, or Note.
  Language-agnostic — evaluates structure and content, not technology.
  Trigger words: review PRD, PRD review, validate PRD, feasibility check, product requirements document review, PRD checklist.
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
2. **Scan the checklist** (see [Review Checklist](#review-checklist) below) — covers completeness, testability, clarity, feasibility, scope, dependencies, and edge cases.
3. **Classify:** Critical (blocks implementation), Suggestion (improves it), Note (observation).
4. **Produce** — findings table with severity, evidence, and recommendation.
5. **Verdict:** Approved / Approved with Suggestions / Needs Revision.
6. **Feedback loop:** If verdict is **Needs Revision**, instruct the author to address Critical findings and resubmit. Re-run this review on the updated PRD before proceeding downstream.

## Review Checklist

Apply all applicable items. Skip items that are genuinely not relevant to the PRD's domain.

**Completeness**
- [ ] Goals and success metrics are stated and measurable.
- [ ] All in-scope features are listed; out-of-scope is explicit.
- [ ] Actors / user roles are identified.
- [ ] Non-functional requirements (performance, security, accessibility) are present.

**Testability**
- [ ] Each requirement can be verified with a concrete pass/fail test.
- [ ] Acceptance criteria are specific (no vague words like "fast", "easy", "good").
- [ ] Edge cases and error states are addressed.

**Clarity**
- [ ] No undefined acronyms or jargon without a glossary entry.
- [ ] No ambiguous modal verbs ("should" vs. "must" vs. "may").
- [ ] Contradictions between sections are absent.

**Feasibility**
- [ ] Timeline and milestones are realistic given stated scope.
- [ ] Dependencies (systems, teams, data) are identified.
- [ ] Technical constraints or assumptions are explicit.

**Scope & Edge Cases**
- [ ] Rollback / failure scenarios are described.
- [ ] Data migration or compatibility concerns are addressed if applicable.
- [ ] Regulatory or compliance requirements are noted if applicable.

## Output Style

1. **Verdict** — Approved / Approved with Suggestions / Needs Revision.
2. **Findings table** — `| # | Severity | Section | Finding | Evidence | Recommendation |`
3. **Summary** — count by severity + one-paragraph assessment.
4. **What's Good** — acknowledge well-written sections.
5. **English only** unless user requests otherwise.

### Example Findings Table

| # | Severity | Section | Finding | Evidence | Recommendation |
|---|----------|---------|---------|----------|----------------|
| 1 | Critical | §3 Acceptance Criteria | "The page must load quickly" is not testable — no threshold defined. | §3: "The dashboard shall load quickly under normal conditions." | Replace with a measurable SLA, e.g. "Dashboard initial load ≤ 2 s at p95 on a 10 Mbps connection." |
| 2 | Suggestion | §5 Dependencies | External payments API dependency is mentioned but no fallback behavior is specified. | §5: "Integration with PaymentsProvider v2 API." | Add a requirement describing user-facing behavior when the API is unavailable (timeout, retry, graceful error). |
| 3 | Note | §1 Goals | Success metric for user adoption is aspirational but not tied to a measurement method. | §1: "Achieve high user adoption within 90 days." | Consider specifying the data source (e.g. analytics event) used to measure adoption. |

## Integration

| Skill | When to chain |
|-------|---------------|
| **create-prd** | Review immediately after PRD generation |
| **generate-tasks** | After review passes, proceed to task breakdown |
| **tech-lead** agent | For deeper feasibility and estimation quality review |
