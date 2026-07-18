# Compatibility model

The repository uses one core Skill directory per capability rather than maintaining separate platform forks.

- WorkBuddy reads `SKILL.md`, `manifest.yaml`, references, and assets.
- Codex reads `SKILL.md`, references, assets, and optional `agents/openai.yaml`.
- Claude Code reads `SKILL.md`, references, assets, and examples; the directory name becomes the slash command.

Unknown metadata files are intentionally passive. The Skill instructions require capability detection before using web, file, image, spreadsheet, or document-generation tools.

## Compatibility claim

“Compatible” means that the package follows the published directory and metadata conventions and contains no deliberate host lock-in. It does not mean that every model or client version has been exhaustively tested.
