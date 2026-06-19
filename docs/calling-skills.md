# Calling Skills and Personas

Agnostic Planning Skills can be invoked in different ways depending on your environment and desired level of autonomy.

## Invocation Methods

| Method | Syntax | Best For |
|--------|--------|----------|
| **Chat Commands** | `@skill-name` or `/skill-name` | Explicitly forcing the agent to follow a specific skill's instructions |
| **CLI (`gh skill` / `skills.sh`)** | `gh skill install ...` | Local installation, pinning versions, reproducible setups |

> MCP support (`use_skill`, `use_agent`) is planned but not yet implemented.

---

## Using Skills

### Via Chat Commands

In environments like Cursor, Windsurf, or Gemini CLI:

```text
@create-prd Add Google OAuth login to the app
@review-prd Review the login PRD for completeness
@generate-tasks Break down the approved login PRD
@estimate-tasks Estimate the login task breakdown
@identify-risks Scan the login plan for risks
@prioritize-backlog Rank the remaining feature requests
@plan-tickets Draft tickets for the search feature
@plan-sprint Select tickets and define the sprint goal
@generate-status-report Create a status report for stakeholders
@create-retrospective Generate the sprint retrospective
```

---

## Using Personas

Personas orchestrate multiple skills through phases with approval gates.

### Via Chat Commands

```text
@requirements-clarifier Clarify the user notification system requirements
@github-issue Create an issue for the notification API bug
@product-owner Plan the user notification system feature
@project-manager Track execution of the current sprint
@tech-lead Review the notification PRD for feasibility
@delivery-lead Run the full delivery cycle for the notification feature
```

---

## Installing Skills

### Via GitHub CLI

```bash
# Install a specific skill
gh skill install igmarin/agnostic-planning-skills create-prd --scope project

# Install all skills
gh skill install igmarin/agnostic-planning-skills
```

### Via skills.sh

> [!NOTE]
> The root `SKILL.md` is the catalog orchestrator (not a standalone skill). The `--full-depth` flag ensures discovery of all nested skills under `skills/<category>/<name>/`.

#### Project-Level (Local) Installation
To install skills for your current project workspace:
```bash
# Install ALL skills and personas
npx skills add igmarin/agnostic-planning-skills --full-depth --all

# Install a specific skill (e.g., create-prd)
npx skills add igmarin/agnostic-planning-skills@create-prd --full-depth
```

#### Global Installation
To install skills globally for your AI coding assistant:
```bash
# Install ALL skills and personas globally
npx skills add igmarin/agnostic-planning-skills --full-depth --all --global

# Install a specific skill globally (e.g., create-prd)
npx skills add igmarin/agnostic-planning-skills@create-prd --full-depth --global
```

---

## Available Skills and Personas

### Skills (12)

| Name | Category | Description |
|------|----------|-------------|
| `create-prd` | PRD | Generate Product Requirements Documents |
| `review-prd` | PRD | Review PRDs for completeness and feasibility |
| `generate-tasks` | Task Management | Break features into TDD task checklists |
| `plan-tickets` | Task Management | Draft tracker-ready tickets |
| `estimate-tasks` | Task Management | Assign effort estimates with confidence levels |
| `prioritize-backlog` | Backlog | Rank items using RICE, MoSCoW, or value-vs-effort |
| `plan-sprint` | Ceremony | Select tickets, define goal, allocate capacity |
| `create-retrospective` | Ceremony | Generate sprint retrospectives with action items |
| `identify-risks` | Execution | Scan plans for dependency and capacity risks |
| `generate-status-report` | Execution | Generate stakeholder status reports |
| `requirements-clarifier` | Analysis | Transform vague requests into actionable specifications |
| `github-issue` | Infrastructure | Create, track, and manage GitHub issues with project boards and milestones |

### Personas (4)

| Name | Phases | Focus |
|------|--------|-------|
| `product-owner` | Discovery → PRD → Tasks → Tickets → Sprint | Scope & planning |
| `project-manager` | Estimation → Risks → Tracking → Reports | Execution tracking |
| `tech-lead` | PRD Review → Feasibility → Estimation Quality → Report | Technical feasibility |
| `delivery-lead` | Scope → Plan → Prioritize → Sprint → Execute → Retrospect | End-to-end pipeline |
