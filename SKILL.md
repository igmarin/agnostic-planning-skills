---
name: agnostic-planning-skills
description: >
  Master orchestrator for the Agnostic Planning Skills library. Use to discover and
  activate language-agnostic skills for product planning, task breakdown, and ticket
  generation. Covers PRDs, TDD task lists, sprint planning, and Agile workflows.
  prd, planning, tasks, tickets, tdd, agile, product management, sprint.
---
# Agnostic Planning Skills

Master entry point for the library. This skill helps you navigate and activate language-agnostic planning skills for disciplined product development.

**Core principle:** Atomic, task-specific instructions that turn AI coding assistants into reliable product collaborators through structured planning and TDD workflow design.

## Quick Reference

| Task | Primary Skill |
|------|---------------|
| **Write a PRD** | `create-prd` |
| **Break down a feature** | `generate-tasks` |
| **Generate tickets** | `plan-tickets` |
| **End-to-end planning** | `product-owner` (agent) |

## HARD-GATE

```text
DO NOT generate implementation code, tasks, or tickets without an approved PRD.
The PRD is the single source of truth for scope — everything flows from it.
```

## Core Process

1. **Discovery:** Clarify scope and goals with the user.
2. **Plan:** Activate `create-prd` to draft a Product Requirements Document.
3. **Break Down:** Activate `generate-tasks` to produce a TDD task checklist from the approved PRD.
4. **Ticket:** Activate `plan-tickets` to convert tasks into tracker-ready tickets.
5. **Orchestrate:** Use the `product-owner` agent for the full end-to-end pipeline with approval gates.

## Skill Catalog

| Category | Skills |
|----------|--------|
| **PRD** | `create-prd` |
| **Task Management** | `generate-tasks`, `plan-tickets` |

## Agents

| Agent | Description |
|-------|-------------|
| **product-owner** | Full planning lifecycle: Discovery → PRD → Tasks → Tickets → Sprint |

*See `tile.json` for the complete skill registry and `agents.json` for the agent registry.*

## Integration

- **Source of Truth:** `tile.json` (skill registry), `agents.json` (agent registry)
- **Reference:** `docs/reference/skill-catalog.md`, `docs/reference/integration-matrix.md`
- **Agent Workflows:** `docs/agent-guide.md`
