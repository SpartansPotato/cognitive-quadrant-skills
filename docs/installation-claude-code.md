# Install in Claude Code

Claude Code discovers personal Skills under `~/.claude/skills/` and project Skills under `.claude/skills/`. The directory name is the slash-command name.

## Personal installation

From the repository root:

```bash
bash scripts/install-claude-code.sh
```

Windows PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/install-claude-code.ps1
```

Manual installation:

```bash
mkdir -p ~/.claude/skills
cp -R skills/cognitive-quadrant-general ~/.claude/skills/
cp -R skills/cognitive-quadrant-teacher-research ~/.claude/skills/
```

Invoke directly:

```text
/cognitive-quadrant-general
/cognitive-quadrant-teacher-research
```

Claude can also load a Skill automatically when the request matches its description.

## Project installation

Copy the folders into:

```text
<repo>/.claude/skills/
```

Official documentation: https://code.claude.com/docs/en/skills
