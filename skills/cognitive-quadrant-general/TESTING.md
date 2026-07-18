# General cognition Skill test checklist

## Structure

- `SKILL.md` has valid YAML frontmatter.
- `manifest.yaml` version is 1.1.0.
- `agents/openai.yaml` references an existing icon.
- English and Chinese workflows exist.
- Universal ZIP contains one root Skill folder.

## Behavior

- Automatically matches an English request.
- Automatically matches a Chinese request.
- Can be invoked explicitly in Codex and Claude Code.
- Does not assume web access or file-generation capability.
- Clearly labels unavailable verification.
- Does not claim to generate a file that does not exist.
- Uses no more than three initial questions when information is missing.
- Produces Express, Ask, Iterate, Explore, cognitive update, and next actions.
