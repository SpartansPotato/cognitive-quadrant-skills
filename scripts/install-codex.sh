#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="${HOME}/.agents/skills"
mkdir -p "$DEST"
for skill in cognitive-quadrant-general cognitive-quadrant-teacher-research; do
  rm -rf "$DEST/$skill"
  cp -R "$ROOT/skills/$skill" "$DEST/$skill"
  echo "Installed $skill -> $DEST/$skill"
done
echo "Codex installation complete. If Skills do not appear, restart Codex."
