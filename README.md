# Agnostic Planning Skills

Planning skills for personal and client work. The active profile combines the planning foundation with one stack: `ruby-rails`, `elixir-phoenix`, or `rust`.

## Use

Choose one active profile per Codex skills directory: `foundation`, `ruby-rails`, `elixir-phoenix`, or `rust`. Use the user directory for one default stack, or install per project when you work across stacks at once. Each profile installs only its skills, avoiding same-name collisions. Start uncertain or cross-role requests with `work-router`; invoke a specialist directly when the task is clear.

Install or switch profiles with one command from this repo. It updates clean `main` checkouts of all five sibling repos, then activates the selected profile:

```sh
bash scripts/setup-profile.sh ruby-rails
```

See [profile setup](docs/profile-migration.md) to configure another computer or use a project-specific skills directory.

## Skills

The profiles cover clarification, PRDs, draft tickets, estimation, prioritization, sprints, retrospectives, risk, status, GitHub issues, and routing. `plan-tickets` is draft-only; `github-issue` is the only issue-mutation skill. `judgment-gate` and `llm-judgment-layer` remain specialist source cards and are not installed by a profile.

## Migration

| Old entry | Use |
|---|---|
| `product-owner`, `project-manager`, `tech-lead`, `delivery-lead` | `work-router` with the matching role intent |
| `generate-tasks` | Stack profile task planning; Ruby has `generate-tdd-tasks` |
| `plan-tickets` create mode | Draft with `plan-tickets`; use `github-issue` only when issue mutation is requested |

Validate profiles with `python3 scripts/validate-profiles.py`; validate this pack with `scripts/validate-skills.sh`.
