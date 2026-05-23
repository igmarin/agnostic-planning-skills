---
name: product-owner
license: MIT
description: >
  Orchestrates the full product planning lifecycle: clarifies scope, drafts a PRD,
  iterates on feedback, breaks work into implementation tasks, generates tracker-ready
  tickets, and places them in sprints. Language-agnostic — works with any tech stack.
  Use when planning a feature, running a product discovery, defining requirements,
  breaking down work, or preparing a sprint backlog.
metadata:
  version: 1.0.0
  user-invocable: "true"
  entry_point: "Invoke when planning a feature, defining product requirements, or preparing work for a sprint"
  phases: "Phase 1: Discovery & Clarification, Phase 2: PRD Draft, Phase 3: Review & Revise, Phase 4: Task Estimation, Phase 5: Ticket Generation, Phase 6: Sprint Placement"
  hard_gates: "PRD Approval, Ticket Approval, Sprint Confirmation"
  dependencies: "create-prd, generate-tasks, plan-tickets"
  keywords: product, planning, prd, tickets, sprint, backlog, discovery, requirements, orchestration
---
# Product Owner Agent

Orchestrates end-to-end product planning: from feature idea to sprint-ready tickets. Chains three atomic skills through six phases with explicit approval gates.

## When to Use

- A feature needs scoping, PRD, and task breakdown before development
- A product idea needs structured requirements and sprint-ready tickets
- Stakeholders need a repeatable planning pipeline with review checkpoints

## Anti-Patterns

- Do not use for bugs or small fixes — those don't need a full PRD
- Do not skip the PRD approval gate unless the scope is trivial
- Do not create tickets in a tracker without explicit user confirmation
- Do not assume sprint placement without user input on capacity and priorities

## Agent Phases

### Phase 1: Discovery & Clarification

1. Receive the feature description or product idea.
2. Clarify scope: ask 3-5 targeted questions only if the goal, scope, and success signals are unclear.
3. Confirm the user's priorities, constraints, and non-goals.
4. Proceed to Phase 2 when scope is unambiguous.

**Decision Gate:**
- If scope remains ambiguous after clarification → ask the user to provide a one-sentence goal statement before proceeding.

---

### Phase 2: PRD Draft

1. Activate **prd/create-prd**: Generate the PRD following `PRD_TEMPLATE.md`.
2. Save to `/tasks/prd-<feature-slug>.md`.
3. Present the PRD for review.

**HARD GATE — PRD Approval:**
```text
The PRD MUST be explicitly approved by the user before any task generation.
DO NOT proceed to Phase 4 until approval is given.
If the user requests changes, move to Phase 3.
If the PRD is rejected outright, return to Phase 1.
```

---

### Phase 3: Review & Revise

1. Collect user feedback on the PRD.
2. Revise the PRD document in place at `/tasks/prd-<feature-slug>.md`.
3. Re-present for approval.

**Decision Gate:**
- After 3 revision rounds without approval → push for a decision: "Which section of the PRD is the blocker? Can we scope it down or mark it as an open question?"
- On approval → proceed to Phase 4.

---

### Phase 4: Task Estimation

1. Activate **task-management/generate-tasks**: Break the approved PRD into implementation tasks.
2. Auto-detect the project's test command, source directory, and documentation conventions.
3. Generate TDD task groups (write test → run fail → implement → run pass).
4. Save to `/tasks/tasks-<feature-name>.md`.
5. Present the task breakdown for review (informational — no hard gate here).

**Quality Check:**
- Every functional requirement from the PRD is covered by at least one task.
- File paths are concrete (detected from project conventions).
- **If quality check fails:** Return to task estimation and fill the gaps before presenting the breakdown.

---

### Phase 5: Ticket Generation

1. Activate **task-management/plan-tickets**: Convert the task breakdown into tracker-ready tickets.
2. Classify each ticket by type, area, execution order, dependency level, and target bucket.
3. Apply title conventions (`BE |`, `FE |`, `Mobile |`) where applicable.
4. Draft tickets in the standard five-section structure: Summary, Background, Acceptance Criteria, Dependencies, Technical Notes.

**HARD GATE — Ticket Approval:**
```text
Ticket drafts MUST be explicitly approved before any tracker creation.
DO NOT create issues unless the user explicitly asks for creation.
Default mode is draft-only — return markdown tickets for review.
```

---

### Phase 6: Sprint Placement

1. Apply the sprint placement heuristics from `plan-tickets` §3 (Sprint Placement Heuristics).
2. Present the sprint-ordered backlog.

**HARD GATE — Sprint Confirmation:**
```text
Sprint placement MUST be confirmed by the user.
DO NOT assume sprint IDs, capacity, or team availability.
If creating tracker issues, validate one issue before bulk creation.
```

---

## Error Recovery

| Scenario | Recovery |
|----------|----------|
| PRD template not found | Ask user for the template path or fall back to a minimal PRD structure |
| Cannot auto-detect test command | Ask: "What test command should I use for this project?" |
| Cannot auto-detect source directory | Ask: "Where does your source code live? (e.g., `src/`, `lib/`, `app/`)" |
| Tracker integration fails | Return to draft-only mode and report the error |
| User rejects PRD 3+ times | Scope down: "Can we reduce this to a minimal viable version?" |

## Output Style / Report

After completing all phases, produce a summary:

```markdown
## Planning Complete: [Feature Name]

### Artifacts Produced
- PRD: `/tasks/prd-[slug].md`
- Task Breakdown: `/tasks/tasks-[name].md`
- Ticket Drafts: [N] tickets drafted

### Sprint Readiness
- [N] tickets ready for next sprint
- [N] tickets in ready-to-refine
- [N] tickets deferred

### Pending Decisions
- [Any unresolved open questions from the PRD]
```
