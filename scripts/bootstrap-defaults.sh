#!/usr/bin/env bash
# Install the personal default skills on this computer, for every agent.
# Safe to re-run: `npx skills add` overwrites in place and `update -g` keeps them current.
#
# Usage: bash scripts/bootstrap-defaults.sh [--no-python-deps]
# Override agents with: SKILLS_AGENTS="claude-code codex" bash scripts/bootstrap-defaults.sh
set -euo pipefail

agents="${SKILLS_AGENTS:-claude-code codex devin antigravity cline kilo pi zed}"
install_python_deps=1
[[ "${1:-}" == "--no-python-deps" ]] && install_python_deps=0

command -v npx >/dev/null || { echo "npx not found: install Node.js first." >&2; exit 1; }

# source | skills ('*' = every skill in the repo)
defaults=(
  "igmarin/agnostic-planning-skills|task-complexity-classifier github-issue"
  "dietrichgebert/ponytail|*"
  "ayghri/i-have-adhd|i-have-adhd"
)

for entry in "${defaults[@]}"; do
  source="${entry%%|*}"
  names="${entry#*|}"
  args=()
  read -ra list <<<"$names"  # read, not word-splitting: keeps "*" from globbing
  for name in "${list[@]}"; do args+=(--skill "$name"); done
  echo "==> $source ($names)"
  # shellcheck disable=SC2086
  npx -y skills add "$source" -g "${args[@]}" -a $agents -y
done

if [[ "$install_python_deps" == 1 ]]; then
  echo "==> Python deps for task-complexity-classifier"
  if command -v uv >/dev/null; then
    uv pip install --system typesafe-sdk python-dotenv
  else
    python3 -m pip install --user typesafe-sdk python-dotenv
  fi
fi

echo "==> Verify"
missing=0
for skill in task-complexity-classifier github-issue i-have-adhd \
  ponytail ponytail-audit ponytail-debt ponytail-gain ponytail-help ponytail-review; do
  if [[ -f "$HOME/.agents/skills/$skill/SKILL.md" ]]; then
    echo "ok       $skill"
  else
    echo "MISSING  $skill"
    missing=1
  fi
done
[[ "$missing" == 0 ]] || exit 1

if [[ -z "${TYPESAFE_API_KEY:-}" ]]; then
  echo
  echo "Next: export TYPESAFE_API_KEY in ~/.zshrc (this script never writes keys)."
fi
echo "Restart open agents so they pick up the new skills."
