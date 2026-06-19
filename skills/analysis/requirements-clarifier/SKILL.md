---
name: requirements-clarifier
type: atomic
license: MIT
description: >
  Transforms vague task descriptions into actionable specifications with user stories acceptance criteria and identified edge cases — NEVER write implementation code or suggest solutions, do NOT edit files, do NOT produce configuration or test cases, produce requirements only. Language-agnostic.
  Trigger words: clarify, requirements, spec, define, what should we build, scope this, refine this, unclear task, vague request.
metadata:
  version: 1.0.0
  user-invocable: "true"
  output: Clarified requirements with user stories, acceptance criteria,
          edge cases, and open questions
  constraints: "NO CODE — produces requirements only. Never implementation."
---
# Requirements Clarifier

Transform vague or incomplete task descriptions into precise, actionable specifications.

**Core principle:** Before any implementation begins, requirements must be unambiguous enough that an engineer can build them and QA can test them.

## Quick Reference

| Aspect | Rule |
|--------|------|
| **Input** | Vague feature request, ambiguous task, incomplete description |
| **Output** | Clarified requirements with user stories, acceptance criteria, edge cases, open questions |
| **Format** | Structured markdown — scannable, never prose-heavy |
| **Scope** | WHAT and WHY only. Never HOW. |
| **Hard gate** | Do not produce code, do not edit files, do not suggest implementation |

## HARD-GATE

```text
NO CODE — This skill produces requirements only.
Do not write implementation code, configuration, or test cases.
Do not edit any files. Output clarified requirements as text.
If asked for implementation, respond: "I produce requirements, not code."
```

## Core Process

1. **Analyze the request** — Identify what is stated, what is implied, and what is missing.
2. **Ask clarifying questions** — Surface ambiguities one group at a time:
   - Target users and actors
   - Success criteria and acceptance tests
   - Dependencies and integrations
   - Constraints (performance, security, compliance)
   - Out-of-scope boundaries
3. **Structure the output** using this format:

### Output Template

```markdown
## Clarified Requirements

### Summary
One-paragraph synthesis of what is being asked.

### Scope
**In scope:** Bullet list of what this covers.
**Out of scope:** Bullet list of explicit exclusions.

### User Stories
- As a [user], I want [goal] so that [benefit]. *(Priority: P0/P1/P2)*

### Acceptance Criteria
**Story: [title]**
- [ ] Given [context] when [action] then [expected result]
- [ ] Given [context] when [action] then [expected result]

### Edge Cases & Constraints
- Technical: [performance, security, compatibility]
- Business: [compliance, localization, timing]
- Behavioral: [empty states, concurrent actions, invalid inputs]

### Open Questions
1. [Specific question that blocks implementation]
2. [Specific question that blocks implementation]
```

4. **Validate**: Before submitting, verify:
   - Would an engineer know what to build?
   - Can QA write test cases from the acceptance criteria?
   - Are the 3 most likely edge cases identified?
   - Are questions specific enough to get actionable answers?

## Guidelines & Pitfalls

| Guideline | Detail |
|-----------|--------|
| **No fluff** | Every sentence adds value. Eliminate filler. |
| **Testable criteria** | Acceptance criteria must be verifiable, not aspirational. Use "Given X, when Y, then Z" — never "works correctly" or "should". |
| **Explicit boundaries** | State what is out of scope as clearly as what is in scope. |
| **Proactive depth** | If requirements are already clear, confirm understanding and ask if refinement is needed. |
| **No implementation details** | Output describes what, not how. Never write "use Redis" or "create a POST endpoint". |
| **Edge cases are mandatory** | The most valuable part of this skill is identifying what can go wrong. Never leave the edge cases section empty or with fewer than 3 items. |
| **Use the template** | Do not merge clarifications into a prose blob. Scannability matters. |
| **Watch for drift** | If you find yourself writing code, configuration, or an empty open-questions section for a non-trivial request, stop and reset. |

## Integration

| Skill | When to chain |
|-------|---------------|
| **create-prd** | After clarifying a feature request, draft the PRD |
| **product-owner** (persona) | The product-owner persona invokes this in Phase 1 (Discovery) |
| **tech-lead** (persona) | The tech-lead persona invokes this during feasibility assessment |
| **generate-tasks** | After requirements are clear and approved, break into tasks |
