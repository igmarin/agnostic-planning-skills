# Repository guidance

- `directory.json` is the skill registry. Keep every listed path valid.
- `profiles.json` is the install allowlist; update it with registry changes.
- Keep `work-router` to one profile skill; require proof for behavior changes and blocking checkpoints only for high-risk work.
- `plan-tickets` drafts only. `github-issue` owns GitHub issue mutations.
- `task-complexity-classifier` requires a TYPESAFE_API_KEY configuration but fails gracefully without it.
- Keep machine-specific MCP/editor configuration out of this repository.
- Run `scripts/validate-skills.sh` and `python3 scripts/validate-profiles.py` after changes.
