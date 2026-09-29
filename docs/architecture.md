# Profile model

`profiles.json` lists the skills installed together. `foundation` is inherited by each stack profile. `ruby-rails-rust` extends `ruby-rails` and adds Rust, for people who use both stacks on one computer.

The `work-router` selects exactly one next skill when intent is unclear. The selected skill owns the task and may consult a specialist when needed. Role names such as product owner or tech lead are routing hints, not separate workflows.

Source repositories remain authoritative. `scripts/install-profile.py` copies one profile into `~/.agents/skills` by default; do not edit installed copies. Codex, Pi, and Kilo support this shared Agent Skills location. Other tools may need a separate install path. The installer tracks the active set, preserves unrelated skills, and archives the old profile when switching. Directories that agents read themselves are outside its scope. `directory.json` remains each repository's skill registry.
