# Daily invocation

1. Set the active profile to `foundation`, `ruby-rails`, `elixir-phoenix`, or `rust` by running `python3 scripts/install-profile.py <profile>` once.
2. If the task is clear, invoke one skill from that profile directly.
3. If role or domain is unclear, give the task and profile to `work-router`; it returns one next skill and only a necessary proof/risk checkpoint.

Examples:

- “Profile `ruby-rails`: add an export endpoint.” → `rails-feature`
- “Profile `elixir-phoenix`: add an Ecto preload.” → `ecto-essentials`
- “Profile `rust`: use this new crate API.” → `rust-essentials`, verify the exact-version API before using it.

Do not install the full flat catalog. The installer writes the chosen profile as direct skill folders under Codex's standard user skills directory. Read optional references only when the selected skill asks for them.
