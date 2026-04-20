#!/usr/bin/env bash

set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$repo_root"

description="${1:-}"
remote="${2:-origin}"
branch="${3:-$(git branch --show-current)}"

if [[ -z "$description" ]]; then
  echo "Usage: $0 \"commit description\" [remote] [branch]"
  exit 1
fi

if [[ -z "$branch" ]]; then
  echo "Error: could not determine the current branch."
  echo "Usage: $0 \"commit description\" [remote] [branch]"
  exit 1
fi

tracked_changes=()
while IFS= read -r file; do
  [[ -n "$file" ]] && tracked_changes+=("$file")
done < <(git diff --name-only)

untracked_changes=()
while IFS= read -r file; do
  [[ -n "$file" ]] && untracked_changes+=("$file")
done < <(git ls-files --others --exclude-standard)

files_to_add=()

for file in "${tracked_changes[@]}" "${untracked_changes[@]}"; do
  if [[ -n "$file" && "$file" != ".DS_Store" && "$file" != **"/.DS_Store" ]]; then
    files_to_add+=("$file")
  fi
done

if (( ${#files_to_add[@]} > 0 )); then
  git add -- "${files_to_add[@]}"
fi

if [[ -n "$(git status --porcelain)" ]]; then
  git commit -m "$description"
  git push "$remote" "$branch"
else
  echo "No changes to commit."
fi

echo
echo "Current status:"
git status --short
