# Changelog

All notable changes to `agnostic-planning-skills` will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [5.0.0] — Unreleased

### Added
- New atomic skill `github-issue` at `skills/infrastructure/github-issue/SKILL.md` for creating and managing GitHub issues with project board integration, milestones, and stage lifecycle management.
- `github-issue` wired into `plan-tickets` Integration section and `product-owner` persona Phase 5 (Ticket Generation).
- `requirements-clarifier` wired into `product-owner`, `delivery-lead`, and `tech-lead` persona dependency lists.
- Explicit 16-skill path array in `.tessl-plugin/plugin.json`.
- Analysis category group in `skills.sh.json`.
- Infrastructure category group in `skills.sh.json`.

### Changed
- **Breaking:** Skill count updated from 11 to 12 across all documentation (README, SKILL.md, CLAUDE.md, GEMINI.md, docs).
- **Breaking:** `requirements-clarifier` moved from `skills/requirements-clarifier/` to `skills/analysis/requirements-clarifier/`.
- **Breaking:** `github-issue` moved from `skills/github-issue/` to `skills/infrastructure/github-issue/`.
- **Breaking:** `directory.json` version bumped to `5.0.0`.
- **Breaking:** `.tessl-plugin/plugin.json` version bumped to `5.0.0`, changed from directory path to explicit skill array.
- `github-issue` SKILL.md now has `type: atomic` and `license: MIT` frontmatter fields.
- `docs/architecture.md` directory tree updated to show all 8 categories.
- `docs/persona-guide.md` updated with `requirements-clarifier` in product-owner Phase 1 and `github-issue` in Phase 5.
- `docs/reference/integration-matrix.md` added `github-issue` integration and category-path annotations.
- `delivery-lead` persona sub-skill manifest updated to include `requirements-clarifier` in Scope phase.

### Fixed
- `.tessl-plugin/plugin.json` now lists all 16 skill directories explicitly instead of a single root path.

### Removed
- Tessl integration: publish and review GitHub Actions workflows, `.tessl-plugin/`, `tessl.json`, `.tesslignore`, Tessl eval scripts, and the `tessl-evals/` tree.
- Tessl registry badge from README and Tessl MCP server config (`.mcp.json`).
- Tessl plugin path check from `.github/review-prompt.md`.

## [4.0.0]

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
