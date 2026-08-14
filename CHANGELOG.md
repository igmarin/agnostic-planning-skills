# Changelog

All notable changes to `agnostic-planning-skills` will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- `scripts/validate-skills.sh` and `.github/workflows/ci.yml` — fail on missing description, description > 600 chars, `SKILL.md` > 500 lines, and `directory.json` ↔ disk drift.
- `docs/reference/gaps.md` — missing skills, eval ownership, description-strategy conflict with `ruby-core-skills`, CI notes.

### Changed
- `requirements-clarifier` moved to `skills/analysis/` and `github-issue` moved to `skills/github-issues/` so all 16 skills follow the uniform `skills/<category>/<name>/SKILL.md` layout. Aligns the filesystem with the existing `skills.sh.json` groupings. Updated `directory.json`, AGENTS.md, architecture, and skill-catalog paths.
- Description contract: when + triggers, target ≤ 600 / spec ceiling 1024. Locked in `docs/architecture.md`. Workflow stays in the body.
- Slimmed all 17 `SKILL.md` descriptions (personas first). Most now ~150–300 chars.
- `AGENTS.md` is the single host-context source. `CLAUDE.md` is a stub.
- README, persona guide, and skill catalog each hold one catalog — not three copies.
- `skills.sh.json` now groups `requirements-clarifier` and the four personas.
- `github-issue` has `type: atomic` and points at `references/gh-commands.md`.

### Removed
- `merge-to-main.sh` — unused local merge shortcut.
- `docs/04-flatten-agents-into-skills.md` — finished migration plan, now stale.
- `skills/github-issue/README.md` and `setup.sh` — leftover OpenCode install wrappers.

### Fixed
- Architecture doc no longer treats 1024 as a budget for the entire frontmatter.
- Docs no longer say “11 skills” (there are 12 atomics + 4 personas).
- Agent dependencies syntax in personas (YAML list of hashes).
- Missing `Owner` column on the `identify-risks` register.
- Install docs now make the `--full-depth` requirement explicit and document the interactive picker (`npx skills add` without `--all`). Without `--full-depth`, the root catalog `SKILL.md` short-circuits discovery and only 1 skill is found.
