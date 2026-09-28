# Agnostic Planning Skills

Planning skills for personal and client work. Profiles combine the planning foundation with the language skills you want available. Choose one stack, or use `ruby-rails-rust` to keep Ruby/Rails and Rust available together.

## Use

Choose one active profile per skills directory: `foundation`, `ruby-rails`, `ruby-rails-rust`, `elixir-phoenix`, or `rust`. For the same skills in multiple coding agents, install once to `~/.agents/skills`; Codex, Pi, and Kilo document support for this shared location. Use `work-router` when the next skill is unclear; invoke a specialist directly when the task is clear.

Install or switch profiles with one command from this repo. It updates clean `main` checkouts of all five sibling repos, then activates the selected profile:

```sh
bash scripts/setup-profile.sh ruby-rails-rust
```

See [profile setup](docs/profile-migration.md) for another computer, profile switching, and tool compatibility.

Without cloning the source repositories, install a single skill or all of them with `npx skills add igmarin/agnostic-planning-skills -g --skill <name>`. `npx skills update -g` only updates skills you already installed, so run `add` once for each new skill. Details: [Install with npx skills](docs/profile-migration.md#install-with-npx-skills).

## Skills

The profiles cover clarification, PRDs, draft tickets, estimation, prioritization, sprints, retrospectives, risk, status, GitHub issues, routing, and task complexity classification. `plan-tickets` is draft-only; `github-issue` is the only issue-mutation skill. `task-complexity-classifier` uses Jev (TypeSafe AI) to assess task complexity and works across all AI agents. `judgment-gate` and `llm-judgment-layer` remain specialist source cards and are not installed by a profile.

## Migration

| Old entry | Use |
|---|---|
| `product-owner`, `project-manager`, `tech-lead`, `delivery-lead` | `work-router` with the matching role intent |
| `generate-tasks` | Stack profile task planning; Ruby has `generate-tdd-tasks` |
| `plan-tickets` create mode | Draft with `plan-tickets`; use `github-issue` only when issue mutation is requested |

Validate profiles with `python3 scripts/validate-profiles.py`; validate this pack with `scripts/validate-skills.sh`.
