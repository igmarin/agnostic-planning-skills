# Contributing

Keep skills short, task-focused, and grounded in the active profile model.

- Add planning skills under `skills/<name>/` and register their paths in `directory.json` and `skills.sh.json`.
- Update `profiles.json` only when a skill should be installed by a profile. It maps skills across the five suite repositories.
- Keep role language as `work-router` intent, not separate persona workflows.
- Do not commit machine-specific editor/MCP config or bundled review binaries.
- Run `scripts/validate-skills.sh` and `python3 scripts/validate-profiles.py` before opening a PR.
