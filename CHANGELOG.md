# Changelog

All notable changes to `agnostic-planning-skills` are recorded here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- `ruby-rails-rust` profile for using Ruby/Rails and Rust skills together.

### Changed
- Setup documentation now explains the shared Agent Skills directory and use across supported coding tools.

### Fixed
- `scripts/setup-profile.sh` reports the remote URL it rejected, instead of only the URL it expected, and does not echo a token kept in a remote URL.
- The trusted-source check no longer stops on equivalent spellings of the same GitHub remote, such as an explicit port, a trailing slash, a missing `.git`, or a different owner casing.
- The trusted-source check verifies the URL git will fetch from, so a `url.*.insteadOf` rewrite that lands on `igmarin/<repository>` passes and one that lands elsewhere is reported with both URLs.
- Setup verifies every repository before pulling any of them, so a rejected remote cannot leave an earlier checkout already updated.

## [5.0.0] - 2026-09-26

### Added
- `work-router` selects one skill from the active profile and reports only the relevant behavior proof or high-risk checkpoint.
- Profile installer for the planning, Ruby/Rails, Elixir/Phoenix, and Rust repositories.

### Changed
- `profiles.json` is the install allowlist; the installer supports a clean user-level setup or project-specific skills directory.
- `plan-tickets` drafts only; `github-issue` owns GitHub issue mutations.
- README and migration guide explain setup and switching profiles on another computer.

### Removed
- Per-role planning personas and orchestration wrappers; use `work-router` intents.
- Tracked machine-specific MCP/editor configs and bundled review binaries.

### Fixed
- Profile switching preserves unrelated skills, archives replaced generated copies, and recovers after an interrupted install.

## [4.1.0] - 2026-09-23

### Added
- `judgment-gate` for independent go/no-go judgments on plans, backlogs, and designs.
- `llm-judgment-layer` for app integration patterns where code retains decision authority.
- `scripts/validate-skills.sh` and CI checks for frontmatter, description size, file length, and registry-to-disk drift.
- `docs/reference/gaps.md` for missing skills, evaluation ownership, and CI notes.

### Changed
- Flattened skills to `skills/<name>/SKILL.md` and grouped the install catalog in `skills.sh.json`.
- Kept workflow guidance in skill bodies and shortened descriptions.
- Consolidated host guidance and updated the skill catalog, calling docs, and profile references.

### Removed
- Unused local merge shortcuts, completed migration notes, and OpenCode install wrappers.

### Fixed
- Clarified frontmatter size limits, agent dependency syntax, risk-register ownership, and Python version-manager handling in validation.
