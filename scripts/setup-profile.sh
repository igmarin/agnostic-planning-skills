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

verify_trusted_upstream() {
  local checkout="$1" repository="$2" upstream remote remote_url expected
  expected="igmarin/$repository"

  if ! upstream="$(git -C "$checkout" rev-parse --abbrev-ref --symbolic-full-name '@{upstream}' 2>/dev/null)"; then
    echo "Setup stopped: $repository/main has no configured upstream." >&2
    exit 1
  fi
  remote="${upstream%%/*}"
  if ! remote_url="$(git -C "$checkout" remote get-url "$remote" 2>/dev/null)"; then
    echo "Setup stopped: cannot read the $remote remote for $repository." >&2
    exit 1
  fi

  case "$remote_url" in
    "https://github.com/$expected"|"https://github.com/$expected.git"|\
    "git@github.com:$expected"|"git@github.com:$expected.git"|\
    "ssh://git@github.com/$expected"|"ssh://git@github.com/$expected.git") ;;
    *)
      echo "Setup stopped: $repository/main tracks a non-canonical source; expected igmarin/$repository on GitHub." >&2
      exit 1
      ;;
  esac
}

for repository in "${repositories[@]}"; do
  checkout="$projects_root/$repository"
  if [[ -e "$checkout" ]]; then
    if [[ ! -e "$checkout/.git" ]]; then
      echo "Setup stopped: $checkout exists but is not a Git checkout." >&2
      exit 1
    fi
    if [[ -n "$(git -C "$checkout" status --porcelain -- . ':(exclude).clinerules')" ]]; then
      echo "Setup stopped: $repository has local changes. Commit, stash, or resolve them first." >&2
      exit 1
    fi
    branch="$(git -C "$checkout" branch --show-current)"
    if [[ "$branch" != "main" ]]; then
      if ! git -C "$checkout" show-ref --verify --quiet refs/heads/main; then
        echo "Setup stopped: $repository has no local main branch." >&2
        exit 1
      fi
      echo "Switching clean $repository checkout from '${branch:-detached HEAD}' to main."
      git -C "$checkout" switch main
    fi
    verify_trusted_upstream "$checkout" "$repository"
    git -C "$checkout" pull --ff-only
    if [[ "$repository" == "agnostic-planning-skills" && ! -f "$planning_repo/scripts/install-profile.py" ]]; then
      echo "Setup stopped: merge the profile setup PR before installing profiles." >&2
      exit 1
    fi
  else
    git clone "https://github.com/igmarin/$repository.git" "$checkout"
  fi
done

python3 "$planning_repo/scripts/install-profile.py" "$profile" --projects-root "$projects_root"
