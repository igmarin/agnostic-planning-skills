# PRD Review Checklist

Comprehensive checklist organized by PRD section. Use to systematically evaluate a PRD's quality.

---

## Introduction

- [ ] States the problem clearly in 1-2 sentences.
- [ ] Explains who is affected and why it matters.
- [ ] Avoids implementation details or solution language.

## Goals

- [ ] Each goal is measurable or verifiable.
- [ ] Goals are outcomes, not tasks or features.
- [ ] No more than 5 goals (fewer is better).

## User Stories

- [ ] Each story follows "As a [role], I want [action] so that [benefit]."
- [ ] Covers all primary user roles affected by the feature.
- [ ] Stories are prioritized or ordered by importance.

## Functional Requirements

- [ ] Each requirement is testable ("The system must..." with observable outcome).
- [ ] No implementation details (no code, class names, or database schema).
- [ ] Requirements cover the full scope implied by the user stories.
- [ ] No contradictory requirements (A says "always do X," B says "never do X").

## Non-Functional Requirements

- [ ] Specific and measurable where possible (not "the system should be fast").
- [ ] Covers relevant concerns: performance, security, accessibility, reliability.
- [ ] Only includes constraints that affect this specific feature.

## Non-Goals

- [ ] Explicitly excludes scope that someone might reasonably assume is included.
- [ ] Each non-goal is specific and clear.

## Design Considerations

- [ ] Links to mockups or design references if UI is involved.
- [ ] Notes any pending design decisions with owners and deadlines.
- [ ] Does not substitute for actual design artifacts if those are required.

## Technical Considerations

- [ ] Identifies relevant constraints (rate limits, data volume, integration limits).
- [ ] Notes technology choices only when they are constraints, not preferences.
- [ ] Does not prescribe implementation details.

## Implementation Surface

- [ ] Lists all areas the feature touches (frontend, backend, database, jobs, integrations).
- [ ] No code — just area identification.
- [ ] Covers infrastructure and deployment considerations if relevant.

## Success Metrics

- [ ] Each metric has a target and a timeframe.
- [ ] Metrics are observable (can be measured without reading code).
- [ ] At least one leading indicator (not just lagging indicators).

## Open Questions

- [ ] Every open question has an owner and deadline (or is explicitly unassigned).
- [ ] No critical path decisions are marked as open questions without a resolution plan.

---

## Cross-Cutting Checks

### Testability
- [ ] Every functional requirement can be verified by a test or manual check.
- [ ] Acceptance criteria use Given/When/Then or equivalent observable format.
- [ ] No requirement relies on internal system state only visible to developers.

### Ambiguity
- [ ] No subjective adjectives without measurable thresholds ("fast" → "<200ms").
- [ ] No undefined terms that a new team member wouldn't understand.
- [ ] No weasel words ("should," "ideally," "maybe," "probably").

### Completeness
- [ ] Edge cases are addressed: empty states, error states, concurrent use, permissions.
- [ ] Rollout strategy is defined if the feature affects existing users.
- [ ] Dependencies on other teams, APIs, or systems are explicitly listed.
- [ ] Migration or data backfill considerations are addressed if relevant.

### Feasibility
- [ ] No requirement contradicts a known technical constraint.
- [ ] External dependencies have confirmed availability or timelines.
- [ ] Scope is realistic for the stated timeline (if a timeline is given).
