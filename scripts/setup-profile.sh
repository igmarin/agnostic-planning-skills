#!/usr/bin/env bash
set -euo pipefail

# Every suite repository is expected to track this owner on GitHub.
GITHUB_OWNER="igmarin"

usage() {
  echo "Usage: bash scripts/setup-profile.sh <foundation|ruby-rails|ruby-rails-rust|elixir-phoenix|rust> [projects-root]" >&2
  exit 2
}

profile="${1:-}"
projects_root_arg="${2:-}"
case "$profile" in
  foundation|ruby-rails|ruby-rails-rust|elixir-phoenix|rust) ;;
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

# Reduce a remote URL to "host/owner/repo" so equivalent spellings of the same
# GitHub source, such as an https clone and an ssh clone, compare equal. Only
# secure transports are recognized; anything else keeps its raw form and fails
# the comparison in verify_trusted_upstream. Userinfo is dropped from the
# authority only, never from the path, so an "@" later in the URL cannot make an
# unrelated host look like github.com.
normalize_remote() {
  local url="$1" host path rest
  url="${url//$'\t'/}"
  url="${url//$'\r'/}"
  url="${url//$'\n'/}"
  while [[ "$url" == *' ' ]]; do url="${url% }"; done
  url="${url%/}"
  case "$url" in
    git@*:*)
      host="${url#git@}"
      host="${host%%:*}"
      host="${host##*@}"
      path="${url#*:}"
      ;;
    ssh://*)
      rest="${url#ssh://}"
      host="${rest%%/*}"
      host="${host##*@}"
      host="${host%%:*}"
      path="${rest#*/}"
      ;;
    https://*)
      rest="${url#*://}"
      host="${rest%%/*}"
      host="${host##*@}"
      host="${host%%:*}"
      path="${rest#*/}"
      ;;
    *)
      printf '%s' "$url"
      return 0
      ;;
  esac
  host="${host,,}"
  path="${path,,}"
  path="${path%.git}"
  printf '%s/%s' "$host" "$path"
}


# Strip any userinfo from a remote URL before printing it, so a token kept in
# the remote config does not reach the terminal or a log. Userinfo comes from the
# authority only, as in normalize_remote, so an "@" in the path is left alone and
# the real host stays visible in the message.
redact_remote() {
  local url="$1" scheme rest authority tail
  if [[ -z "$url" ]]; then
    printf '%s' "<empty>"
    return 0
  fi
  case "$url" in
    *://*)
      scheme="${url%%://*}"
      rest="${url#*://}"
      authority="${rest%%/*}"
      tail="${rest#"$authority"}"
      if [[ "$authority" == *@* ]]; then
        printf '%s://%s@%s%s' "$scheme" '***' "${authority##*@}" "$tail"
      else
        printf '%s' "$url"
      fi
      ;;
    *)
      printf '%s' "$url"
      ;;
  esac
}


verify_trusted_upstream() {
  local checkout="$1" repository="$2" remote merge_ref expected
  local configured_url effective_url remote_url normalized

  # Read main's upstream from config rather than @{upstream}: this checkout may be
  # on another branch now and is switched to main before the pull.
  if ! remote="$(git -C "$checkout" config --get branch.main.remote 2>/dev/null)"; then
    echo "Setup stopped: $repository/main has no configured upstream." >&2
    exit 1
  fi
  if [[ -z "$remote" || "$remote" == "." ]]; then
    echo "Setup stopped: $repository/main tracks a local branch, not a remote." >&2
    exit 1
  fi
  merge_ref="$(git -C "$checkout" config --get branch.main.merge 2>/dev/null || true)"
  if [[ "$merge_ref" != "refs/heads/main" ]]; then
    echo "Setup stopped: $repository/main must track $remote/main, not ${merge_ref:-an unknown ref}." >&2
    exit 1
  fi

  # Compare the URL git will fetch from. `git pull` uses the effective URL after
  # any url.*.insteadOf rewrite, so the configured value is not what runs. Report
  # the rewrite when the two differ, since that is what changed the source.
  configured_url="$(git -C "$checkout" config --get "remote.$remote.url" 2>/dev/null || true)"
  effective_url="$(git -C "$checkout" remote get-url "$remote" 2>/dev/null || true)"
  remote_url="${effective_url:-$configured_url}"
  if [[ -n "$configured_url" && -n "$effective_url" && "$configured_url" != "$effective_url" ]]; then
    echo "Note: git rewrites $remote through url.*.insteadOf: $(redact_remote "$configured_url") -> $(redact_remote "$effective_url")" >&2
  fi

  expected="github.com/$GITHUB_OWNER/$repository"
  normalized="$(normalize_remote "$remote_url")"
  if [[ "${normalized,,}" == "${expected,,}" ]]; then
    return 0
  fi

  echo "Setup stopped: $repository/main tracks a non-canonical source; expected $GITHUB_OWNER/$repository on GitHub." >&2
  echo "  remote: $remote" >&2
  echo "  found:  $(redact_remote "$remote_url")" >&2
  echo "  fix:    git -C '$checkout' remote set-url $remote https://github.com/$GITHUB_OWNER/$repository.git" >&2
  exit 1
}

# Pass 1: read-only checks. Nothing is switched, pulled, or cloned until every
# existing checkout passes, so a rejected remote cannot leave earlier
# repositories already updated.
for repository in "${repositories[@]}"; do
  checkout="$projects_root/$repository"
  if [[ ! -e "$checkout" ]]; then
    continue
  fi
  if [[ ! -e "$checkout/.git" ]]; then
    echo "Setup stopped: $checkout exists but is not a Git checkout." >&2
    exit 1
  fi
  if [[ -n "$(git -C "$checkout" status --porcelain -- . ':(exclude).clinerules')" ]]; then
    echo "Setup stopped: $repository has local changes. Commit, stash, or resolve them first." >&2
    exit 1
  fi
  branch="$(git -C "$checkout" branch --show-current)"
  if [[ "$branch" != "main" ]] && ! git -C "$checkout" show-ref --verify --quiet refs/heads/main; then
    echo "Setup stopped: $repository has no local main branch." >&2
    exit 1
  fi
  verify_trusted_upstream "$checkout" "$repository"
done

# Pass 2: switch each clean checkout to main, then update or clone it.
for repository in "${repositories[@]}"; do
  checkout="$projects_root/$repository"
  if [[ -e "$checkout" ]]; then
    branch="$(git -C "$checkout" branch --show-current)"
    if [[ "$branch" != "main" ]]; then
      echo "Switching clean $repository checkout from '${branch:-detached HEAD}' to main."
      git -C "$checkout" switch main
    fi
    git -C "$checkout" pull --ff-only
    if ! upstream_tip="$(git -C "$checkout" rev-parse --verify '@{upstream}^{commit}' 2>/dev/null)"; then
      echo "Setup stopped: cannot resolve the verified upstream tip for $repository/main after pull." >&2
      exit 1
    fi
    if ! current_revision="$(git -C "$checkout" rev-parse --verify 'HEAD^{commit}' 2>/dev/null)"; then
      echo "Setup stopped: cannot resolve the current revision for $repository/main after pull." >&2
      exit 1
    fi
    if [[ "$current_revision" != "$upstream_tip" ]]; then
      echo "Setup stopped: $repository/main is at $current_revision, not its verified upstream tip $upstream_tip after pull." >&2
      exit 1
    fi
    if [[ "$repository" == "agnostic-planning-skills" && ! -f "$planning_repo/scripts/install-profile.py" ]]; then
      echo "Setup stopped: merge the profile setup PR before installing profiles." >&2
      exit 1
    fi
  else
    git clone "https://github.com/$GITHUB_OWNER/$repository.git" "$checkout"
  fi
done

python3 "$planning_repo/scripts/install-profile.py" "$profile" --projects-root "$projects_root"
