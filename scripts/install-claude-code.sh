#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="${HOME}/.claude/skills"
mkdir -p "$DEST"
for skill in cognitive-quadrant-general cognitive-quadrant-teacher-research; do
  rm -rf "$DEST/$skill"
  cp -R "$ROOT/skills/$skill" "$DEST/$skill"
  echo "Installed $skill -> $DEST/$skill"
done
echo "Claude Code installation complete. Invoke /cognitive-quadrant-general or /cognitive-quadrant-teacher-research."
