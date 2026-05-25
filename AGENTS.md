# Agnostic Planning Skills — Agent Guidance

This file tells AI agents how to use this repository.

## What This Repository Is

A curated library of 10 language-agnostic skills for technical project management and planning. Skills cover PRD creation, task breakdown, estimation, prioritization, sprint planning, retrospectives, and agile ticket generation. These skills work with ANY technology stack.

## How Skills Are Organized

Each skill lives in its own directory with a `SKILL.md` as the entry point:

```
skill-name/
├── SKILL.md          # Entry point — always read this first
├── EXAMPLES.md       # Concrete examples (when present)
└── TEMPLATE.md       # Output structure (when present)
```

## Skill Selection

| Category | Path | Skills |
|----------|------|--------|
| **PRD** | `skills/prd/` | `create-prd`, `review-prd` |
| **Task Management** | `skills/task-management/` | `generate-tasks`, `plan-tickets`, `estimate-tasks` |
| **Backlog** | `skills/backlog/` | `prioritize-backlog` |
| **Ceremonies** | `skills/ceremony/` | `plan-sprint`, `create-retrospective` |
| **Execution** | `skills/execution/` | `generate-status-report`, `identify-risks` |

## Agents

| Agent | Path | Purpose |
|-------|------|---------|
| **delivery-lead** | `agents/delivery-lead/` | Full delivery pipeline from feature idea through to retrospective |
| **product-owner** | `agents/product-owner/` | Full product planning lifecycle: scope → PRD → task breakdown → ticket generation → sprint placement |
| **project-manager** | `agents/project-manager/` | Execution tracking lifecycle: estimates tasks → identifies risks → tracking checkpoints → status reports |
| **tech-lead** | `agents/tech-lead/` | Technical review of a PRD: feasibility → estimation quality → architectural concerns → technical risk report |

## Ecosystem Context

This repo is part of a larger AI skill ecosystem:
- `igmarin/ruby-core-skills` — Shared Ruby process skills (DDD, patterns, process discipline)
- `igmarin/rails-agent-skills` — Rails-specific skills and agents
- `igmarin/hanakai-yaku` — Hanami/dry-rb/ROM skills and agents
- `igmarin/agnostic-planning-skills` — **This repo** — Language-agnostic planning
- `igmarin/agent-mcp-runtime` — Rust CLI runtime for composing skills via MCP

Planning skills can be combined with any framework-specific skill pack. For example:
`create-prd` → `generate-tasks` → `plan-tickets` → then switch to `rails-agent-skills` for implementation.

## Output Language

All generated artifacts must be in **English** unless the user explicitly requests another language.
