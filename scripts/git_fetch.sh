#!/usr/bin/env bash

set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$repo_root"

remote="${1:-origin}"
branch="${2:-$(git branch --show-current)}"

if [[ -z "$branch" ]]; then
  echo "Error: could not determine the current branch."
  echo "Usage: $0 [remote] [branch]"
  exit 1
fi

echo "Fetching from ${remote}/${branch}..."
git fetch "$remote" "$branch"

echo
echo "Local status:"
git status --short

echo
echo "Incoming commits on ${remote}/${branch}:"
git log --oneline --decorate HEAD.."${remote}/${branch}" || true
