# Skill Architecture — Agnostic Planning Skills

Conventions and structure for every `SKILL.md` in this library.

- **Overview and catalog:** [README](../README.md)
- **Agent chains:** [agent-guide.md](agent-guide.md)
- **Docs index:** [index.md](index.md)

## Directory Structure

```text
agnostic-planning-skills/
├── docs/                    # Documentation
│   ├── architecture.md
│   ├── agent-guide.md
│   ├── skill-template.md
│   └── reference/
│       ├── skill-catalog.md
│       └── integration-matrix.md
├── agents/                  # Orchestrated agent skills
│   └── product-owner/
│       └── SKILL.md
├── skills/                  # Categorized skills
│   ├── prd/                 # PRD creation skills
│   │   └── create-prd/
│   └── task-management/     # Task and ticket skills
│       ├── generate-tasks/
│       └── plan-tickets/
├── SKILL.md                 # Root orchestrator
├── tile.json                # Skill registry
├── agents.json              # Agent registry
└── README.md
```

## SKILL.md Structure

Every skill follows this structure:

### 1. YAML Frontmatter (Required)

```yaml
---
name: skill-name
description: >
  Use when [concrete trigger conditions]. Covers [key topics].
  [Additional trigger words for discovery].
---
```

**Rules:**

- `name`: kebab-case, matches directory name
- `description`: starts with "Use when...", third person
- Include concrete trigger words (error symptoms, tools, scenarios)
- Do NOT summarize the workflow (prevents model from skipping the skill body)
- Max 1024 characters total for frontmatter

### 2. Title and Core Principle

```markdown
# Skill Title

Use this skill when [brief trigger].

**Core principle:** [One sentence philosophy]
```

### 3. Quick Reference (High Priority)

A scannable table at the top for fast lookup:

```markdown
## Quick Reference

| Aspect | Rule |
|--------|------|
| ... | ... |
```

### 4. HARD-GATE (Where Applicable)

Non-negotiable blockers in a code block:

```markdown
## HARD-GATE

\```
DO NOT [forbidden action].
ALWAYS [required action].
\```
```

### 5. Core Rules / Process

The main instructions. Use numbered steps for processes, bullet lists for rules.

### 6. Common Mistakes (High Priority)

Table format with "Mistake" and "Reality" columns:

```markdown
## Common Mistakes

| Mistake | Reality |
|---------|---------|
| "Excuse or bad practice" | Why it's wrong and what to do instead |
```

### 7. Red Flags (High Priority)

Bullet list of signals that the skill is being violated:

```markdown
## Red Flags

- Signal that something is wrong
- Another signal
```

### 8. Integration (Medium Priority)

Table of related skills and when to chain them:

```markdown
## Integration

| Skill | When to chain |
|-------|---------------|
| **other-skill** | When [condition] |
```

## Frontmatter Optimization (CSO)

"Claude Search Optimization" — how the description helps AI agents find the right skill:

1. Start with "Use when..." (activation trigger)
2. Include concrete nouns: "controller", "migration", "factory"
3. Include action verbs: "reviewing", "creating", "fixing"
4. Include symptoms: "N+1", "fat model", "flaky tests"
5. Do NOT summarize the workflow (the model will skip reading the body)

**Good:**

```yaml
description: >
  Use when generating a Product Requirements Document, defining feature scope,
  or writing a product spec. Covers goals, user stories, functional requirements,
  success metrics, and open questions.
```

**Bad:**

```yaml
description: >
  This skill creates PRDs by first writing the introduction, then goals, then
  user stories, then requirements, then non-goals, then success metrics.
```

## Skill Types

### Planning Skills

Produce structured artifacts (PRDs, task lists, tickets).

- `create-prd` — Product Requirements Documents
- `generate-tasks` — TDD task checklists from PRDs
- `plan-tickets` — Tracker-ready ticket drafts

### Orchestration Agents

Chain multiple skills with approval gates.

- `product-owner` — Full planning lifecycle: Discovery → PRD → Tasks → Tickets → Sprint

## Skill Reference Formats

Skills are referenced by three conventions depending on context:

| Context | Format | Example |
|---------|--------|---------|
| `tile.json` and `agents.json` | Full path: `skills/<category>/<name>/SKILL.md` | `skills/prd/create-prd/SKILL.md` |
| Agent body (activate calls) | Category-path: `<category>/<name>` | `prd/create-prd` |
| Integration tables | Short name only | `create-prd` |

The category-path format (`<category>/<name>`) drops the `skills/` prefix and the `/SKILL.md` suffix from the full tile.json path. Integration tables use bare names since the surrounding context (which skill file you're in) plus the category taxonomy in the root `SKILL.md` makes disambiguation straightforward.

## Approval Gates

Planning skills use **hard gates** — explicit user approval checkpoints that block progress until confirmed:

### PRD Approval Gate

Defined in: `create-prd`, `product-owner` agent.

Purpose: The PRD must be explicitly approved before any task generation or implementation. This prevents feature work on unapproved scope.

### Ticket Approval Gate

Defined in: `plan-tickets`, `product-owner` agent.

Purpose: Ticket drafts must be reviewed and approved before creating issues in a tracker. Default mode is draft-only.

### Sprint Confirmation Gate

Defined in: `product-owner` agent.

Purpose: Sprint placement must be confirmed by the user. The agent does not assume sprint IDs, capacity, or team availability.

## Platform Compatibility

All skills use standard Markdown and YAML frontmatter, compatible across major AI coding assistants that support skill/plugin loading.
