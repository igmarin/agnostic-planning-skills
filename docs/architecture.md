# Profile model

`profiles.json` is the allowlist for one active Codex profile. `foundation` is inherited by `ruby-rails`, `elixir-phoenix`, and `rust`. A profile names skills by repository and skill name, so unrelated packs do not enter the active catalog.

The `work-router` selects exactly one next skill when intent is unclear. The selected skill owns the task and may consult a specialist when needed. Role names such as product owner or tech lead are routing hints, not separate workflows.

Source repositories remain authoritative. `scripts/install-profile.py` copies one profile into Codex's user skills directory by default; do not edit installed copies. It tracks the active set, preserves unrelated skills, and archives the old profile when switching. `directory.json` remains each repository's skill registry.
