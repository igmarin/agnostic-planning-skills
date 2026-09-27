#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "Usage: bash scripts/setup-profile.sh <foundation|ruby-rails|elixir-phoenix|rust> [projects-root]" >&2
  exit 2
}

profile="${1:-}"
projects_root_arg="${2:-}"
case "$profile" in
  foundation|ruby-rails|elixir-phoenix|rust) ;;
  *) usage ;;
esac

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
planning_repo="$(cd -- "$script_dir/.." && pwd)"
if [[ -n "$projects_root_arg" ]]; then
  projects_root="$projects_root_arg"
else
  projects_root="$(dirname -- "$planning_repo")"
fi
mkdir -p -- "$projects_root"
projects_root="$(cd -- "$projects_root" && pwd)"
if [[ "$planning_repo" != "$projects_root/agnostic-planning-skills" ]]; then
  echo "Setup stopped: run this script from the agnostic-planning-skills checkout inside projects-root." >&2
  exit 1
fi

repositories=(
  agnostic-planning-skills
  elixir-phoenix-skills
  rust-core-skills
  ruby-core-skills
  rails-agent-skills
)

for repository in "${repositories[@]}"; do
  checkout="$projects_root/$repository"
  if [[ -e "$checkout" ]]; then
    if [[ ! -e "$checkout/.git" ]]; then
      echo "Setup stopped: $checkout exists but is not a Git checkout." >&2
      exit 1
    fi
    branch="$(git -C "$checkout" branch --show-current)"
    if [[ "$branch" != "main" ]]; then
      echo "Setup stopped: $repository is on '$branch'; switch to main after its PR is merged." >&2
      exit 1
    fi
    if [[ -n "$(git -C "$checkout" status --porcelain -- . ':(exclude).clinerules')" ]]; then
      echo "Setup stopped: $repository has local changes. Commit, stash, or resolve them first." >&2
      exit 1
    fi
    git -C "$checkout" pull --ff-only
  else
    git clone "https://github.com/igmarin/$repository.git" "$checkout"
  fi
done

python3 "$planning_repo/scripts/install-profile.py" "$profile" --projects-root "$projects_root"
