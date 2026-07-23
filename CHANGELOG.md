# Changelog

All notable changes to `agnostic-planning-skills` will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- Bump `rs-guard` pin to **v1.6.0** (`bin/rs-guard.manifest`, vendored `bin/` binaries, install/smoke/pre-commit version hints).

### Added
- New atomic skill `requirements-clarifier` at `skills/requirements-clarifier/SKILL.md` for transforming vague requests into actionable specifications.
- `.opencode/agents/` wrappers for opencode subagent support (5 wrappers — 4 personas + 1 skill).

### Changed
- **Breaking:** `agents/` directory removed. Agents moved to `skills/personas/` with `type: persona` in frontmatter.
- **Breaking:** `agents.json` removed — all entries merged into `directory.json`.
- **Breaking:** `AGENTS.md` removed — content merged into CLAUDE.md and GEMINI.md.
- **Breaking:** `directory.json` version bumped to `4.0.0`.
- All 10 pre-existing atomic skills now have `type: atomic` in frontmatter.
- Root `SKILL.md` now has `type: catalog` and updated references (agents → personas).
- `README.md` updated to reflect 11 skills + 4 personas.
- `CLAUDE.md` and `GEMINI.md` updated with new skill/persona vocabulary.
- `docs/agent-guide.md` renamed to `docs/persona-guide.md` with updated terminology.
- `docs/architecture.md` updated with new directory structure and skill types.
- `docs/calling-skills.md` updated (agents → personas, added requirements-clarifier).
- `docs/reference/skill-catalog.md` updated with new vocabulary and requirements-clarifier entry.

### Fixed
- Fixed agent dependencies syntax (from string to YAML list of hashes) in `product-owner`, `project-manager`, `tech-lead`, and `delivery-lead` agents to pass ecosystem consistency audit.
