# Contributing to agnostic-planning-skills

Contributions are welcome. This repository follows a Markdown + YAML frontmatter architecture for skills and personas.

## Getting Started

1. Clone the repository
2. Review [docs/architecture.md](docs/architecture.md) for structural conventions

## Adding a New Skill

1. Create the directory: `skills/<skill-name>/`
2. Create `SKILL.md` following the conventions in [docs/architecture.md](docs/architecture.md)
3. Add companion files (templates, examples, heuristics) as needed
4. Register the skill in `directory.json`
5. Add the skill to `docs/reference/skill-catalog.md`
6. Add the skill to `docs/reference/integration-matrix.md`

## Adding a New Persona

1. Create the directory: `skills/<persona-name>/`
2. Create `SKILL.md` with `type: persona` in frontmatter
3. Register the persona in `directory.json`
4. Add the persona to `docs/reference/skill-catalog.md`
5. Update `docs/persona-guide.md` with the new persona's workflow

## Local Review with rs-guard

Every PR is reviewed automatically by [rs-guard](https://github.com/nebulaideas/rs-guard) in CI. You can run the same review locally before pushing — it is advisory only and never blocks a commit or push.

### Prerequisites

- An API key for any [supported provider](#supported-providers) set in your shell environment
- The bundled binary for your platform (already in `bin/`; no install needed)

#### Supported providers

| Provider | Environment variable | `.reviewer.toml` `provider` value |
|----------|---------------------|-----------------------------------|
| DeepSeek | `DEEPSEEK_API_KEY` | `deepseek` |
| OpenAI | `OPENAI_API_KEY` | `openai` |
| Kimi (Moonshot AI) | `KIMI_API_KEY` | `kimi` |
| Qwen (Alibaba Cloud) | `DASHSCOPE_API_KEY` | `qwen` |
| OpenRouter | `OPENROUTER_API_KEY` | `openrouter` |

The repo's CI uses DeepSeek by default (configured in `.reviewer.toml`). To use a different provider locally, set its API key and pass `--provider <name>` on the command line — or update `.reviewer.toml`.

### Run a review on your staged changes (pre-commit)

```bash
# Stage your changes first
git add .

# Run the pre-commit hook manually (uses the provider set in .reviewer.toml)
bash hooks/pre-commit-rs-guard
```

### Run a review on any diff file

```bash
# Generate a diff against main
git diff main...HEAD --unified=5 > my.diff

# Run rs-guard against it — replace --provider with your chosen provider
bin/rs-guard-macos-arm64 \
  --diff-file my.diff \
  --prompt-file .github/review-prompt.md \
  --provider deepseek \
  --dry-run
```

Use `bin/rs-guard-linux-x64` instead if you are on Linux. See `bin/CHECKSUMS.txt` for version and integrity information.

### Install the pre-commit hook permanently

```bash
cp hooks/pre-commit-rs-guard .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

After this, every `git commit` automatically runs an advisory review on staged changes. The review result is printed to the terminal; the commit always proceeds regardless of findings.

### Review prompt

The review criteria live in `.github/review-prompt.md`. It checks skill YAML frontmatter, planning artifact quality (PRDs, sprint plans, risk registers, estimations), documentation consistency (`directory.json`, `plugin.json`, `CHANGELOG.md`), and script/workflow hygiene.

---

## Conventions

- All generated artifacts in English unless the user explicitly requests another language
- Skill names match directory names (kebab-case)
- Frontmatter `description` is when + triggers (≤ 600 chars). Do not pack the workflow into YAML. See [docs/architecture.md](docs/architecture.md).
- HARD-GATE rules go in fenced code blocks
- Keep public docs consistent with `directory.json`
- Run `./scripts/validate-skills.sh` before opening a PR
