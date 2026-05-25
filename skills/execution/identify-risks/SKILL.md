---
name: identify-risks
license: MIT
description: >
  Scans plans for risks backed by evidence not speculation — check dependency
  chains single points of failure ambiguous requirements external dependencies
  capacity and technical uncertainty, classify each risk with Likelihood Impact
  and Proximity, reference the specific task or requirement as evidence, and
  include concrete mitigations.
  Language-agnostic.
  Use when asked about risks, risk assessment, blockers, what could go wrong, or
  to produce a risk register for a plan, PRD, ticket set, or sprint.
metadata:
  version: 1.0.0
  user-invocable: "true"
---
# Identifying Project Risks

Scan plans for risks backed by concrete evidence — not speculation.

## Quick Reference

- **Input:** Task list, PRD, ticket set, or sprint plan.
- **Output:** Risk register (description, likelihood, impact, mitigation).
- **Rule:** Every risk cites specific evidence from the plan.

## HARD-GATE

```text
DO NOT fabricate risks. Every risk MUST reference a specific task or requirement.
DO NOT flag everything as high-risk — use the likelihood/impact matrix honestly.
DO NOT skip mitigations — every risk needs at least one concrete mitigation.
```

## Core Process

1. **Receive** — task list, PRD, ticket set, or sprint plan.
2. **Scan risk patterns** (see Risk Patterns below) — dependency chains, external deps, ambiguity, single points of failure, capacity, technical uncertainty.
3. **Classify** — Likelihood (High/Medium/Low), Impact (High/Medium/Low), Proximity (Immediate/Near-term/Future).
4. **Suggest mitigations** — prevention, contingency, owner.
5. **Validate** — cross-check each risk against the plan:
   - Remove any risk that lacks direct evidence from the source material
   - Flag gaps where patterns apply but no risk was identified
   - Verify likelihood/impact ratings are justified by evidence
6. **Output** — structured risk register.

## Risk Patterns

Apply these six patterns when scanning the plan:

| # | Pattern | Signals |
|---|---|---|
| 1 | **Dependency Chain** | Task B cannot start until Task A completes; A is not yet done |
| 2 | **Single Point of Failure** | Only one person owns a critical path item; no documented backup |
| 3 | **Ambiguous Requirement** | Acceptance criteria missing, TBD placeholders, or vague verbs ("improve", "enhance") |
| 4 | **External Dependency** | Third-party API, vendor delivery, regulatory approval, or customer sign-off required |
| 5 | **Capacity / Resource** | Team member over-allocated; holiday or leave overlaps delivery window |
| 6 | **Technical Uncertainty** | New technology, unproven integration, or no spike/prototype yet planned |

## Concrete Example

**Sample input task:** "Integrate payment gateway — assigned to Alice, go-live Friday. Vendor sandbox access not yet confirmed."

**Resulting risk register row:**

| ID | Risk | Likelihood | Impact | Proximity | Evidence | Mitigation |
|----|------|-----------|--------|-----------|----------|------------|
| R1 | Payment gateway integration blocked by missing vendor sandbox access | High | High | Immediate | Task: "Vendor sandbox access not yet confirmed" | Owner: Alice escalates to vendor by EOD Monday; contingency: mock server for internal testing until access granted |

## Output Style

1. **Risk Register** — `| ID | Risk | Likelihood | Impact | Proximity | Evidence | Mitigation |`
2. **Summary** — count by severity and proximity.
3. **Top 3 risks** — detailed mitigation recommendations.
4. **Assumptions** — about team, timeline, or external factors.
5. **English only** unless user requests otherwise.

## Integration

| Skill | When to chain |
|---|---|
| **estimate-tasks** | After estimation, assess risks from high-uncertainty tasks |
| **generate-tasks** | After task breakdown, identify dependency risks |
| **generate-status-report** | Include risk updates in stakeholder status reports |
