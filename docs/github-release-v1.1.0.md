# Publish v1.1.0 on GitHub

If v1.0.0 has not been published, use v1.1.0 as the first public release.

## Upload source files

1. Extract `cognitive-quadrant-skills-github-ready-v1.1.0.zip`.
2. Open the extracted `cognitive-quadrant-skills` directory.
3. Upload everything inside that directory to the repository root.
4. Confirm that `README.md`, `README.zh-CN.md`, `skills/`, and `releases/` appear directly at the root.
5. Suggested commit message:

```text
Release v1.1.0: cross-platform WorkBuddy, Codex and Claude Code support
```

## Create the GitHub Release

- Tag: `v1.1.0`
- Title: `Cognitive Quadrant Skills v1.1.0 / 认知四象限 Skills v1.1.0`
- Description: copy `RELEASE_NOTES_v1.1.0.md`
- Assets: upload both ZIP files from `releases/`

## If v1.0.0 is already published

Keep the old Release as history. Replace the repository source with v1.1.0 or update it through Git. Because v1.1.0 removes the `-cn` suffix from Skill directory names, users should remove old installed directories before installing the new release to avoid duplicate Skills.
