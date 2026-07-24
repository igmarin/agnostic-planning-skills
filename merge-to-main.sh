#!/bin/bash
# Force merge current branch into main
set -euo pipefail

current_branch=$(git rev-parse --abbrev-ref HEAD)
echo "Current branch: $current_branch"

if [ "$current_branch" = "main" ]; then
  echo "Already on main. Nothing to do."
  exit 0
fi

echo "Merging $current_branch into main..."
git checkout main
git merge --no-ff "$current_branch" -m "Merge branch '$current_branch'"
git push origin main
echo "Merge complete."
