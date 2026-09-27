# Install or switch your active profile

`profiles.json` defines one active project profile: `foundation`, `ruby-rails`, `elixir-phoenix`, or `rust`. Each language profile includes `foundation`.

On a new computer, clone this repository once, then run the setup command. It clones the other four repositories beside it if needed, updates clean `main` checkouts, and activates the chosen profile:

```sh
git clone https://github.com/igmarin/agnostic-planning-skills.git ~/Developer/Projects/agnostic-planning-skills
cd ~/Developer/Projects/agnostic-planning-skills
bash scripts/setup-profile.sh ruby-rails
```

This copies only the selected profile's skills into Codex's personal skills directory, `~/.agents/skills`, where Codex discovers them. Source repositories remain the source of truth; do not edit installed copies. To switch profiles, rerun the command with `foundation`, `elixir-phoenix`, or `rust`.

For this rollout, merge the Ruby, Rails, Elixir, and Rust PRs before the Planning PR. The setup script switches clean sibling checkouts to `main` and pulls them; it stops if other local changes are present. The existing local `.clinerules` edits are preserved.

The installer records its active profile and removes only the prior profile copies it owns. Other skills in `~/.agents/skills` are left alone. On first use, it recognizes old suite entries listed in `.dotskills-manifest.json` and moves those generated mirrors into a timestamped backup at `~/.agents/skill-profile-backups/`. If a same-named skill is not known to the installer, it stops rather than overwrite it; use `--backup-conflicts` only if you want that folder preserved in the same backup location.

If the repositories are not siblings, pass their parent directory as the second argument to `setup-profile.sh`. To install into a project-specific Codex directory instead, run `python3 scripts/install-profile.py ruby-rails --projects-root PATH --output /path/to/project/.agents/skills`.

Use project-specific installs when you have different stacks open at the same time. Codex discovers `.agents/skills` in the project tree; keep the generated directory untracked if you do not want to commit skill copies.

On this computer, run `bash scripts/setup-profile.sh ruby-rails` to update the clean source checkouts and regenerate the profile. Profiles and generated copies are local to each computer; Git syncs the source repositories, not the generated install or Codex settings.

Old persona names are router intents: `product-owner`, `project-manager`, `tech-lead`, and `delivery-lead` map to `work-router` with that role context. The Rails, Ruby, Elixir, and Rust routers are replaced by this shared entry point.

Validate routing and clean, Codex-discoverable profile installs with `python3 scripts/validate-profiles.py`.
