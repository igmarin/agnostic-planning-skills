# Agnostic Planning Skills — Docs

10 language-agnostic skills and 4 orchestration agents for product planning, estimation, risk assessment, backlog prioritization, sprint planning, retrospectives, and status reporting.

## Quick Navigation

| Need | Document |
|------|----------|
| Browse all skills and agents | [reference/skill-catalog.md](reference/skill-catalog.md) |
| Understand skill chaining | [reference/integration-matrix.md](reference/integration-matrix.md) |
| Agent workflows with diagrams | [agent-guide.md](agent-guide.md) |
| Repository structure and conventions | [architecture.md](architecture.md) |
| Invoke skills and agents | [calling-skills.md](calling-skills.md) |

## Skill Categories

| Category | Skills |
|----------|--------|
| PRD | `create-prd`, `review-prd` |
| Task Management | `generate-tasks`, `plan-tickets`, `estimate-tasks` |
| Backlog | `prioritize-backlog` |
| Ceremony | `plan-sprint`, `create-retrospective` |
| Execution | `identify-risks`, `generate-status-report` |

## Agents

| Agent | Focus |
|-------|-------|
| `product-owner` | Scope & planning: PRD → Tasks → Tickets → Sprint |
| `project-manager` | Execution tracking: Estimation → Risks → Tracking → Reports |
| `tech-lead` | Technical feasibility: PRD Review → Feasibility → Estimation Quality |
| `delivery-lead` | End-to-end pipeline: Scope → Plan → Prioritize → Sprint → Execute → Retrospect |
