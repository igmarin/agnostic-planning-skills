# Calling Skills and Agents

Agnostic Planning Skills can be invoked in different ways depending on your environment and desired level of autonomy.

## Invocation Methods

| Method | Syntax | Best For |
| **MCP `use_skill`** | Autonomous tool call by the agent | Autonomous workflows where the LLM discovers and loads the right skill |
| **Chat Commands** | `@skill-name` or `/skill-name` | Explicitly forcing the agent to follow a specific skill's instructions |
| **CLI (`gh skill` / `skills.sh`)** | `gh skill install ...` | Local installation, pinning versions, reproducible setups |

---

## Using Skills

### Via Chat Commands

In environments like Cursor, Windsurf, or Gemini CLI:

```text
@create-prd Add Google OAuth login to the app
@generate-tasks Break down the approved PRD
@plan-tickets Draft tickets for the search feature
```

### Via MCP *(planned)*

> MCP support is planned but not yet implemented. When available, agents will discover skills from `tile.json` and load them with `use_skill(skill_name)`.

---

## Using the Product Owner Agent

The `product-owner` agent chains all three planning skills through six phases with approval gates.

### Via Chat Commands

```text
@product-owner Plan the user notification system feature
```

### Via MCP *(planned)*

> MCP support is planned but not yet implemented. When available, agents will use `list_agents` and `use_agent` to discover and execute the product-owner pipeline.

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

```bash
npx skills add igmarin/agnostic-planning-skills
```

---

## Available Skills and Agent

| Name | Type | Description |
|------|------|-------------|
| `create-prd` | Skill | Generate Product Requirements Documents |
| `generate-tasks` | Skill | Break features into TDD task checklists |
| `plan-tickets` | Skill | Draft tracker-ready tickets |
| `product-owner` | Agent | Full planning lifecycle with approval gates |
