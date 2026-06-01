# Contributing to agnostic-planning-skills

Contributions are welcome. This repository follows a Markdown + YAML frontmatter architecture for skills and personas.

## Getting Started

1. Clone the repository
2. Review [docs/architecture.md](docs/architecture.md) for structural conventions

## Adding a New Skill

1. Create the directory: `skills/<category>/<skill-name>/`
2. Create `SKILL.md` following the conventions in [docs/architecture.md](docs/architecture.md)
3. Add companion files (templates, examples, heuristics) as needed
4. Register the skill in `tile.json`
5. Add the skill to `docs/reference/skill-catalog.md`
6. Add the skill to `docs/reference/integration-matrix.md`

## Adding a New Persona

1. Create the directory: `skills/personas/<persona-name>/`
2. Create `SKILL.md` with `type: persona` in frontmatter
3. Register the persona in `directory.json`
4. Add the persona to `docs/reference/skill-catalog.md`
5. Update `docs/persona-guide.md` with the new persona's workflow

## Conventions

- All generated artifacts in English unless the user explicitly requests another language
- Skill names match directory names (kebab-case)
- Frontmatter `description` starts with action-oriented trigger language
- HARD-GATE rules go in fenced code blocks
- Keep public docs consistent with `directory.json`
