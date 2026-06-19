---
name: agnostic-planning-skills
type: catalog
description: >
  Master orchestrator for the Agnostic Planning Skills library. Use to discover and
  activate 11 language-agnostic skills and 4 personas for product planning,
  task breakdown, estimation, risk assessment, ticket generation, backlog
  prioritization, sprint planning, retrospectives, requirements clarification,
  and status reporting. Personas guide end-to-end workflows.
  prd, planning, tasks, tickets, estimation, risks, status, backlog, sprint,
  retrospective, tdd, agile, product management, requirements, clarification.
metadata:
  internal: true
---
# Agnostic Planning Skills

Master entry point. Navigate and activate 11 language-agnostic planning skills plus 4 personas.

**Core principle:** Atomic, task-specific instructions that turn AI coding assistants into reliable product collaborators through structured planning, estimation, risk assessment, and execution tracking.

## Quick Reference

| Task | Primary Skill |
|------|---------------|
| **Write a PRD** | `create-prd` |
| **Review a PRD** | `review-prd` |
| **Break down a feature** | `generate-tasks` |
| **Estimate effort** | `estimate-tasks` |
| **Generate tickets** | `plan-tickets` |
| **Prioritize backlog** | `prioritize-backlog` |
| **Plan a sprint** | `plan-sprint` |
| **Retrospective** | `create-retrospective` |
| **Identify risks** | `identify-risks` |
| **Status report** | `generate-status-report` |
| **Clarify requirements** | `requirements-clarifier` |
| **End-to-end planning** | `product-owner` (persona) |
| **Execution tracking** | `project-manager` (persona) |
| **Technical feasibility** | `tech-lead` (persona) |
| **Full delivery cycle** | `delivery-lead` (persona) |

## HARD-GATE

```text
DO NOT generate implementation code, tasks, or tickets without an approved PRD.
DO NOT fabricate estimates, progress, or risks — be honest about uncertainty.
The PRD is the single source of truth for scope — everything flows from it.
```

## Core Process

1. **Scope** → `create-prd` → `review-prd`
2. **Plan** → `generate-tasks` → `estimate-tasks` → `identify-risks`
3. **Prioritize** → `prioritize-backlog` → `plan-tickets`
4. **Sprint** → `plan-sprint`
5. **Execute** → `generate-status-report` → `identify-risks`
6. **Retrospect** → `create-retrospective`
7. **Clarify** → `requirements-clarifier` (if requirements are vague)
8. **Orchestrate** → Use `product-owner`, `project-manager`, `tech-lead`, or `delivery-lead` personas

## Skill Catalog

| Category | Skills |
|----------|--------|
| **PRD** | `create-prd`, `review-prd` |
| **Task Management** | `generate-tasks`, `plan-tickets`, `estimate-tasks` |
| **Backlog** | `prioritize-backlog` |
| **Ceremony** | `plan-sprint`, `create-retrospective` |
| **Execution** | `generate-status-report`, `identify-risks` |
| **Analysis** | `requirements-clarifier` |

## Personas

| Persona | Focus | Phases |
|---------|-------|--------|
| **product-owner** | Scope & planning | Discovery → PRD → Tasks → Tickets → Sprint |
| **project-manager** | Execution tracking | Estimation → Risks → Tracking → Status Reports |
| **tech-lead** | Technical feasibility | PRD Review → Feasibility → Estimation Quality → Risk Report |
| **delivery-lead** | End-to-end pipeline | Scope → Plan → Prioritize → Sprint → Execute → Retrospect |

## Integration

- **Source of Truth:** `directory.json` (skill registry)
- **Reference:** `docs/reference/skill-catalog.md`, `docs/reference/integration-matrix.md`
- **Persona Workflows:** `docs/persona-guide.md`
