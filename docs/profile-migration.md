# Install skills on this computer or another one

## The simple rule

Edit skills in their source repositories under `~/Developer/Projects`. The installer copies the profile you choose into `~/.agents/skills`. Do not edit that generated copy.

[Codex](https://learn.chatgpt.com/docs/build-skills), [Pi](https://pi.dev/docs/latest/skills), and [Kilo](https://kilo.ai/docs/customize/skills) all document support for `~/.agents/skills` and the project-level `.agents/skills` directory. Keep each skill in a folder whose name matches its `SKILL.md` frontmatter `name`; include a clear `description`. To use a skill, ask for it by name, for example: “Use `rails-feature` to add an export endpoint.” Each tool may also have its own shortcut for invoking skills.

[Devin's setup docs](https://docs.devin.ai/onboard-devin/repo-setup) mention `.agents/skills` for repository scripts, but do not clearly describe automatic discovery of general Agent Skills. Check that Devin loads a test skill in its workspace before relying on this path there. Other tools may need their own install path; keep the skill source the same and configure only where the files are installed.

## Choose a profile

Choose one profile for each skills directory. Pick the profile that contains the stacks you want available together:

| Profile | Includes |
|---|---|
| `foundation` | Planning and workflow skills |
| `ruby-rails` | Foundation, Ruby, and Rails |
| `ruby-rails-rust` | Foundation, Ruby, Rails, and Rust |
| `elixir-phoenix` | Foundation and Elixir/Phoenix |
| `rust` | Foundation and Rust |

For example, use `ruby-rails-rust` on a computer where you work in both stacks. This keeps both available in Codex, Pi, and Kilo through their shared user skills directory. Use a project-level install only when it does not duplicate skills from your user profile. Each stack profile includes the same foundation skills, so the combined user profile is simpler when you switch stacks often.

## Install with `npx skills`

Use this when you want the skills without cloning the five repositories. It installs to `~/.agents/skills` and links or copies into each agent you name.

```sh
npx skills add igmarin/agnostic-planning-skills -g --skill '*' \
  -a claude-code codex devin antigravity cline kilo pi zed -y
```

Replace `'*'` with a skill name, such as `task-complexity-classifier`, to install one skill. Agent ids come from the CLI; run `npx skills add --help` for options.

What the installer did on a verified run:

| Agent | Result |
|---|---|
| Codex, Antigravity, Cline, Kilo, Zed | Read `~/.agents/skills` directly (universal) |
| Claude Code, Devin, Pi | Symlink to `~/.agents/skills/<skill>` |

### `add` vs `update`

`npx skills update -g` refreshes only skills already recorded in `~/.agents/.skill-lock.json`. It never installs a skill that was added to the repository later. After you push a new skill, run `npx skills add ... --skill <name>` once. Later `update -g` runs then keep it current.

If `update -g` does not show a new skill, check the lock file first:

```sh
grep -c '"<skill-name>"' ~/.agents/.skill-lock.json
```

A count of `0` means the skill was never installed.

## Personal defaults on every computer

One command installs the default skills (`task-complexity-classifier`, `github-issue`, `i-have-adhd`, and all `ponytail*`) for Claude Code, Codex, Devin, Antigravity, Cline, Kilo, Pi, and Zed, and installs the classifier's Python dependencies. It is safe to re-run.

```sh
bash scripts/bootstrap-defaults.sh
```

Override the agents with `SKILLS_AGENTS="claude-code codex"`. Skip the Python step with `--no-python-deps`. The script never writes `TYPESAFE_API_KEY`; export it in `~/.zshrc` on each computer.

## Skills that need setup: `task-complexity-classifier`

This skill calls Jev (TypeSafe AI). Installing it is not enough to get real classifications:

1. `pip install typesafe-sdk python-dotenv` (or `uv add`).
2. Set `TYPESAFE_API_KEY` in your environment or in `~/.config/task-complexity-classifier/.env` (mode 600).
3. Check the wiring without an API call: `python3 ~/.agents/skills/task-complexity-classifier/classifier.py --dry-run "Fix a typo"`.

Without a key it returns `classification: complex` with `fallback_used: true`. Treat that result as "unknown", not as a real classification.

## Set up this computer

From the Planning repository, install or switch the profile with one command:

```sh
cd ~/Developer/Projects/agnostic-planning-skills
bash scripts/setup-profile.sh ruby-rails-rust
```

Use `foundation`, `ruby-rails`, `elixir-phoenix`, or `rust` in place of `ruby-rails-rust` when you want a different profile. The setup script checks all five source repositories, updates them from their `main` branches, then installs the selected profile into `~/.agents/skills`.

It stops if a checkout has uncommitted changes (except the existing local `.clinerules` files), has no local `main` branch, or tracks a remote other than `github.com/igmarin/<repository>`. Check and correct the remote with:

```sh
git -C <path-to-checkout> remote get-url origin
git -C <path-to-checkout> remote set-url origin https://github.com/igmarin/<repository>.git
```

Run this after the profile changes have been merged to the repositories' `main` branches. If Codex, Pi, or Kilo does not show a newly installed skill, reload or restart that tool.

The installer leaves unrelated skills in `~/.agents/skills` alone. If it finds a same-named skill that it does not manage, it stops rather than replace it. Use `--backup-conflicts` with `install-profile.py` only when you want that existing folder backed up before installation.

Keep all five source repositories together as sibling folders. `setup-profile.sh` uses the parent of this checkout as the projects root, so `~/Developer/Projects` above is an example rather than a requirement. Pass a different parent as the second argument. This checkout must still be named `agnostic-planning-skills`.

## Set up another computer

Clone the Planning repository, then run the same setup command. The script clones the other four repositories beside it if they are missing:

```sh
git clone https://github.com/igmarin/agnostic-planning-skills.git ~/Developer/Projects/agnostic-planning-skills
cd ~/Developer/Projects/agnostic-planning-skills
bash scripts/setup-profile.sh ruby-rails-rust
```

Git syncs the five source repositories. Each computer has its own generated `~/.agents/skills` directory, so run setup on each computer after changing profiles or merging skill updates.

## Project-level install

Use this when a project needs a profile that differs from your user-level profile:

```sh
python3 scripts/install-profile.py elixir-phoenix \
  --projects-root ~/Developer/Projects \
  --output /path/to/project/.agents/skills
```

Codex, Pi, and Kilo scan project `.agents/skills` directories. Keep generated skill folders out of the project commit unless that project intentionally shares them. The project and user directories may both load skills. Since the stack profiles share foundation skills, prefer the combined user profile when you regularly switch stacks.

## Updating a skill

Edit the skill in its source repository, commit and merge the change, then rerun setup on each computer that uses it. This refreshes the generated copies without changing unrelated skills.

## Removing skills an agent still lists

`setup-profile.sh` writes to `~/.agents/skills`. `install-profile.py` writes to the directory `--output` names, which defaults to the same place. The directories some agents read themselves are separate: `npx skills add` fills them with symlinks into that directory, and nothing removes a link when you switch profiles. An agent can keep listing a skill that is no longer installed.

Remove the folder or link by hand after switching, then reload the agent if the skill is still listed:

```sh
rm ~/.claude/skills/<skill>
```

See [daily skill use](calling-skills.md) for choosing a direct skill or using `work-router`.
