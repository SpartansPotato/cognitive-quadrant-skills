# 在 Claude Code 中安装

Claude Code 会从 `~/.claude/skills/` 读取个人 Skill，从项目中的 `.claude/skills/` 读取项目 Skill。Skill 目录名称同时是斜杠命令名称。

## 用户级安装

在仓库根目录运行：

```bash
bash scripts/install-claude-code.sh
```

Windows PowerShell：

```powershell
powershell -ExecutionPolicy Bypass -File scripts/install-claude-code.ps1
```

手动安装：

```bash
mkdir -p ~/.claude/skills
cp -R skills/cognitive-quadrant-general ~/.claude/skills/
cp -R skills/cognitive-quadrant-teacher-research ~/.claude/skills/
```

直接调用：

```text
/cognitive-quadrant-general
/cognitive-quadrant-teacher-research
```

当用户请求与描述匹配时，Claude 也可以自动加载 Skill。

## 项目级安装

将两个 Skill 文件夹复制到：

```text
<项目根目录>/.claude/skills/
```

官方文档：https://code.claude.com/docs/en/skills
