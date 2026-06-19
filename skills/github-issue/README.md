# github-issue Skill

A universal skill for creating and managing GitHub issues with automatic project board integration, milestone tracking, and stage lifecycle management.

## What It Does

- **Creates well-structured issues** with proper labels, descriptions, and acceptance criteria
- **Integrates with project boards** (GitHub Projects V2 and Classic) automatically
- **Tracks issue lifecycle** through stages: `todo` → `in-progress` → `in-review` → `done`
- **Suggests milestones** based on active releases/sprints
- **Respects repo conventions** by detecting and using existing issue templates
- **Validates before creating** — always shows you the draft before submitting

## Requirements

- **GitHub CLI (`gh`)** installed and authenticated
  - Install: https://cli.github.com/
  - Auth: `gh auth login`
- Working in a git repository with a GitHub remote

## Installation

### OpenCode (Primary)

The skill is installed at:
```
~/.opencode/skills/github-issue/
```

It will automatically trigger when you mention creating issues, tracking work, or updating issue status.

### Cross-Tool Setup

Run the setup script to create symlinks for other tools:

```bash
~/.opencode/skills/github-issue/setup.sh
```

This creates symlinks in:
- `~/.cursor/rules/github-issue` → Cursor
- `~/.vscode/skills/github-issue` → VSCode

### Manual Setup for Other Tools

For tools like Gemini CLI, Devin, or others:

1. **Copy the skill:**
   ```bash
   cp -r ~/.opencode/skills/github-issue /path/to/tool/skills/
   ```

2. **Or reference in project AGENTS.md:**
   ```markdown
   ## GitHub Issue Management
   Use the github-issue skill at ~/.opencode/skills/github-issue/ for creating and tracking issues.
   ```

3. **Or add to tool-specific config:**
   - Gemini: Add to `.gemini/instructions.md`
   - Copilot: Add to `.github/copilot-instructions.md`
   - Claude Code: Already works via opencode skills

## Usage

### Creating an Issue

**Example 1: From conversation context**
```
User: "We need to add retry logic to the API client, it keeps failing on timeouts"

Skill will:
1. Ask clarifying questions (error messages, expected behavior)
2. Detect repo setup and issue templates
3. Determine type: bug
4. Draft a well-structured issue
5. Show you the draft for approval
6. Create with labels: todo, bug
7. Add to project board if detected
```

**Example 2: Explicit request**
```
User: "Create a new issue for adding dark mode support"

Skill will:
1. Ask for details (scope, acceptance criteria)
2. Determine type: new-feature
3. Draft the issue
4. Validate with user
5. Create and track
```

### Updating Issue Status

**Example 1: Explicit command**
```
User: "Move #42 to in-progress"

Skill will:
1. Fetch issue #42
2. Update labels: todo → in-progress
3. Move project card to "In Progress" column
4. Confirm update
```

**Example 2: Inferred from context**
```
User: "I'm working on the API retry logic issue"

Skill will:
1. Search for the issue
2. Detect stage change: todo → in-progress
3. Update labels and project board
4. Confirm update
```

### Closing Completed Work

```
User: "The fix for #42 is deployed, we can close it"

Skill will:
1. Fetch issue #42
2. Update labels: current stage → done
3. Close the issue
4. Move project card to "Done" column
5. Confirm closure
```

## Stage Lifecycle

Issues flow through these stages:

```
todo → in-progress → in-review → done (closed)
```

**Label meanings:**
- `todo` — Not started, ready to be picked up
- `in-progress` — Actively being worked on
- `in-review` — Work complete, awaiting review or testing
- `done` — Complete and verified (issue is closed)

## Label Conventions

**Type labels** (pick one):
- `bug` — Something isn't working
- `new-feature` — Request for new functionality
- `improvement` — Enhancement to existing functionality
- `refactor` — Code restructuring without behavior change
- `security` — Security vulnerability or hardening

**Stage labels** (lifecycle):
- `todo`, `in-progress`, `in-review`, `done`

**Phase labels** (optional):
- `phase-1`, `phase-2`, etc.
- Or use milestones instead

**Priority labels** (optional):
- `priority:high`, `priority:medium`, `priority:low`

All labels use kebab-case for consistency.

## Project Board Integration

The skill automatically detects and integrates with:

1. **GitHub Projects V2** (newer, more flexible)
2. **Classic Projects** (older, simpler boards)
3. **Milestones** (release/sprint tracking)

When creating or updating issues, the skill:
- Adds the issue to the appropriate project board
- Moves cards when status changes
- Suggests milestones if active ones exist

## Issue Templates

If your repo has issue templates in `.github/ISSUE_TEMPLATE/`, the skill will:
- Detect them automatically
- Format the issue body to match the template
- Use the template's structure and fields

This ensures consistency with your team's conventions.

## Validation Flow

Before creating any issue, the skill:
1. Shows you the complete draft (title, labels, description)
2. Asks for explicit approval
3. Only creates after you confirm

This prevents junk issues and gives you a chance to refine the scope.

## Troubleshooting

**"gh: command not found"**
```bash
# Install GitHub CLI
brew install gh  # macOS
# or see https://cli.github.com/
```

**"gh: Not authenticated"**
```bash
gh auth login
```

**"No projects found"**
That's fine — the skill will skip project board integration if none exist.

**"Permission denied"**
```bash
# Check your permissions
gh repo view --json viewerPermission

# You need write access to create/edit issues
```

## Files

```
github-issue/
├── SKILL.md              # Main skill instructions
├── README.md             # This file
├── setup.sh              # Cross-tool setup script
└── references/
    └── gh-commands.md    # Quick reference for gh CLI commands
```

## How It Works Across Tools

The skill is written as a universal SKILL.md that works across different AI coding tools:

- **OpenCode**: Loads automatically from `~/.opencode/skills/`
- **Cursor**: Loads from `~/.cursor/rules/` (symlinked)
- **VSCode**: Loads from `~/.vscode/skills/` (symlinked)
- **Other tools**: Copy the SKILL.md or reference it in your project config

The instructions are tool-agnostic — they use natural language and standard `gh` CLI commands that any AI assistant can execute.

## Contributing

To improve this skill:
1. Edit the SKILL.md file
2. Test with real issues
3. Share improvements via PR or issue

## License

Part of your personal skill library. Use freely across your projects.
