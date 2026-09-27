# Repository guidance

- `directory.json` is the skill registry. Keep every listed path valid.
- `profiles.json` is the install allowlist; update it with registry changes.
- Keep `work-router` to one next skill and risk-based checkpoints.
- `plan-tickets` drafts only. `github-issue` owns GitHub issue mutations.
- Keep machine-specific MCP/editor configuration out of this repository.
- Run `scripts/validate-skills.sh` and `python3 scripts/validate-profiles.py` after changes.
