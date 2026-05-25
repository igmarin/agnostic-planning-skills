---
name: plan-tickets
license: MIT
description: >
  Drafts classifies and creates structured tickets from a project plan —
  classify each item then draft tickets with area prefixes description acceptance
  criteria dependencies and labels (type area execution order sprint bucket),
  confirm before tracker creation, never assume tracker credentials fields or
  sprint IDs, omit unneeded fields and use the project's default initial status.
  Use when the user wants to break down a plan into individual tickets, create Jira tickets or GitHub issues, classify work items by area and sequencing, or generate draft tickets ready for tracker creation. Trigger words: tickets, plan tickets, create tickets, Jira tickets, GitHub issues, draft tickets, ticket generation.
metadata:
  version: 1.0.0
  user-invocable: "true"
---
# Plan Tickets

Normalize inputs, classify each work item, apply title conventions, draft tickets in a standard structure, then either return markdown drafts or create issues in the issue tracker after explicit approval.

## Quick Reference

```text
Plan input -> classify each item -> draft tickets -> confirm before tracker creation
Default mode: draft-only, unless the user explicitly asks to create issues.
Ticket shape: Title, Type, Area, Bucket, Summary, Background, Acceptance Criteria, Dependencies, Technical Notes.
```

## HARD-GATE

```text
Do not create tracker issues unless the user explicitly asks for creation.
Do not assume tracker credentials, project fields, sprint IDs, status behavior, or required custom fields.
If the user only asks for tickets, return markdown drafts.
```

## Core Process

### 1. Normalize the initiative
Extract: initiative/theme, project/board, draft-only vs. create-in-tracker, default sprint/bucket, constraints on types/prefixes/labels/status.
- State assumptions for any missing tracker details, plan gaps, or configuration fields.
- Default to English unless requested otherwise.
- If a plan already exists, do not re-plan unless there is a material gap.

### 2. Classify each ticket
Before drafting, assign and output a single classification line for every ticket using this format:
`[type: Story|Task] [area: backend|web|mobile|cross-platform|external] [execution_order: foundation|api|client|follow-up] [dependency_level: unblocked|blocked] [target_bucket: ready-to-refine|next-dev-sprint|later]`

Apply additional attributes if relevant (`coordination_need`: `single-team`|`multi-team`, `external_dependency`: `yes`|`no`, `urgency`: `normal`|`priority`). Backend/API enablers come before dependent client tickets.

### 3. Apply Sprint Placement Heuristics
Determine execution sequence and note sequencing dependencies:
- Place `foundation`/`api` tickets before dependent `client` tickets.
- Exclude `external` confirmation from active sprints.
- Set `follow-up` tickets to `ready-to-refine` or `later` until enabling work is done.
- Treat named future sprints (e.g., *Ready to Refine*) as planning buckets, not execution commitments.

### 4. Apply title conventions
Prefix titles based on ownership: `BE | ` (backend), `FE | ` (frontend), or `Mobile | ` (mobile).
Do not add prefixes to tickets not owned by those areas unless requested.

### 5. Draft tickets in the standard structure
Draft each ticket using exactly five sections in this order:
1. **Summary**: State the business/technical outcome.
2. **Background**: Explain why.
3. **Acceptance Criteria**: List observable criteria verifiable by a reviewer.
4. **Dependencies**: Note blockers/sequencing.
5. **Technical Notes**: Implementation details affecting sequencing or scoping only.

Keep main sections business-facing.

### 6. Output: drafts or create in the issue tracker

**Draft-only mode (Default):**
- Return markdown tickets matching the prefix, classification line, and five-section structure.
- Explicitly state that the output is draft-only (creation boundary).
- Include a **Readiness Checklist** of what must be verified before creation: target project/board, tracker create-metadata endpoint, required fields, integration path, user approval, and default initial status.

**Create-in-tracker mode:**
- Create issues only after explicit user approval. Do not assume tracker credentials.
- Verify target project/board and confirm required fields from the tracker's create-metadata endpoint.
- Omit fields not required. Do not set status on create (use project's default initial status).
- Validate creation with **one** issue before bulk-creating if sprint/workflow behavior is uncertain.
- Report created issue keys, confirmed status, and any skipped fields or assumptions.

**Example field shape for MCP/API creation:**
```json
{
  "project": "<project-key>",
  "issuetype": "Story",
  "summary": "BE | Enable payment webhook processing",
  "description": "<full ticket body>",
  "labels": ["payments", "backend"],
  "components": ["payments-service"],
  "sprint": { "id": "<sprint-id>" },
  "epic": "<epic-key>"
}
```

## Extended Resources (Progressive Disclosure)

Load these files only when their specific content is needed:

- **[EXAMPLES.md](./EXAMPLES.md)** — Use when you need a full plan → ticket draft example with classification applied.
- **[assets/ticket-samples/sample_issue.md](assets/ticket-samples/sample_issue.md)** — Use when you need the detailed format for a single issue.

## Integration

| Skill | When to chain |
|-------|----------------|
| **generate-tasks** | After tasks exist or in parallel — same initiative can feed ticket breakdown |
| **create-prd** | When tickets should align with PRD scope and acceptance themes |
