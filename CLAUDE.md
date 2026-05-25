# Agnostic Planning Skills — Claude Code Configuration

This file instructs Claude Code on how to discover and invoke skills from the `agnostic-planning-skills` repository.

## Repository Purpose

`agnostic-planning-skills` is a curated library of 10 language-agnostic skills and 4 callable agents for technical project management, product planning, and agile execution. It teaches AI coding agents how to scope requirements, draft PRDs, estimate work, manage backlogs, plan sprints, and track execution health independently of any particular technology stack.

## Skill Catalog

The repository contains 10 atomic planning skills and 4 agents covering:

| Skill | Category | Use when... |
|-------|----------|-------------|
| `create-prd` | PRD | Scoping requirements, defining features, and writing product requirements documents (PRDs). |
| `review-prd` | PRD | Auditing an existing PRD for clarity, completeness, alignment, and gaps. |
| `generate-tasks` | Task Management | Breaking down requirements into implementation tasks with clear TDD ordering. |
| `plan-tickets` | Task Management | Formatting tasks into agile-ready tracker tickets (user stories, chores, tests). |
| `estimate-tasks` | Task Management | Estimating complexity or effort points for planned tasks. |
| `prioritize-backlog` | Backlog | Organizing and ordering backlog items by value, risk, and dependencies. |
| `plan-sprint` | Ceremony | Selecting tickets from a backlog to plan a sprint capacity. |
| `create-retrospective` | Ceremony | Reflecting on a completed sprint or milestone to capture lessons and actions. |
| `generate-status-report` | Execution | Preparing milestone or sprint execution status reports for stakeholders. |
| `identify-risks` | Execution | Conducting risk assessments and mapping mitigations for active projects. |

## How to Discover Skills

1. **MCP Server** (preferred): The `agnostic-planning-skills` MCP server exposes `list_skills` and `use_skill` tools. Load skills on demand to keep context small.
2. **Direct file reference**: Reference skills by canonical `name` from frontmatter.
3. **GitHub CLI**: `gh skill install igmarin/agnostic-planning-skills <canonical-name>`

## How to Invoke a Skill

Reference skills by their canonical `name` from YAML frontmatter:

- `create-prd`
- `generate-tasks`
- `plan-tickets`
- `product-owner` (agent)
- `delivery-lead` (agent)

File paths (for reference only):
- `skills/prd/create-prd/SKILL.md`
- `skills/task-management/generate-tasks/SKILL.md`
- `agents/product-owner/SKILL.md`

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

## Progressive Disclosure

When loading skills:
1. **Discovery**: Load only the name and description of each skill
2. **Activation**: When a task matches a skill's description, read the full SKILL.md
3. **Execution**: Follow the instructions, optionally executing bundled code or loading referenced templates
