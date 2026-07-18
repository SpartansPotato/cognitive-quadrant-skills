# Install in Codex

Codex discovers user Skills under `~/.agents/skills/` and repository Skills under `.agents/skills/`.

## Personal installation

From the repository root:

```bash
bash scripts/install-codex.sh
```

Windows PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/install-codex.ps1
```

Manual installation:

```bash
mkdir -p ~/.agents/skills
cp -R skills/cognitive-quadrant-general ~/.agents/skills/
cp -R skills/cognitive-quadrant-teacher-research ~/.agents/skills/
```

Restart Codex only if the new Skills do not appear automatically. In CLI or IDE, use `/skills` or type `$` to mention a Skill explicitly.

## Repository installation

Copy the folders into:

```text
<repo>/.agents/skills/
```

This makes the Skills available when Codex works in that repository.

Official documentation: https://developers.openai.com/codex/build-skills
