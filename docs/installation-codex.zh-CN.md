# 在 Codex 中安装

Codex 会从用户目录 `~/.agents/skills/` 读取个人 Skill，也会从项目中的 `.agents/skills/` 读取仓库级 Skill。

## 用户级安装

在仓库根目录运行：

```bash
bash scripts/install-codex.sh
```

Windows PowerShell：

```powershell
powershell -ExecutionPolicy Bypass -File scripts/install-codex.ps1
```

手动安装：

```bash
mkdir -p ~/.agents/skills
cp -R skills/cognitive-quadrant-general ~/.agents/skills/
cp -R skills/cognitive-quadrant-teacher-research ~/.agents/skills/
```

如果 Skill 没有自动出现，再重启 Codex。在 CLI 或 IDE 中可以使用 `/skills`，或输入 `$` 后选择 Skill。

## 项目级安装

将两个 Skill 文件夹复制到：

```text
<项目根目录>/.agents/skills/
```

这样 Codex 在该仓库工作时就能发现它们。

官方文档：https://developers.openai.com/codex/build-skills
