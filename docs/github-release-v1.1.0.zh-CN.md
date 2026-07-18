# 在 GitHub 发布 v1.1.0

如果还没有上传 v1.0.0，建议直接把 v1.1.0 作为仓库的第一个公开版本。

## 上传仓库源码

1. 解压 `cognitive-quadrant-skills-github-ready-v1.1.0.zip`；
2. 打开解压后的 `cognitive-quadrant-skills` 文件夹；
3. 将文件夹内部的全部文件和子文件夹上传到 GitHub 仓库根目录；
4. 确认仓库根目录直接出现 `README.md`、`README.zh-CN.md`、`skills/`、`releases/` 等，而不是再多套一层文件夹；
5. Commit message 可填写：

```text
Release v1.1.0: cross-platform WorkBuddy, Codex and Claude Code support
```

## 创建 Release

- Tag：`v1.1.0`
- Title：`Cognitive Quadrant Skills v1.1.0 / 认知四象限 Skills v1.1.0`
- Description：复制根目录 `RELEASE_NOTES_v1.1.0.md`
- 附件：上传 `releases/` 中的两个 ZIP

## 如果已经上传 v1.0.0

可以删除本地旧目录后上传 v1.1.0 的完整目录，或通过 Git 客户端覆盖更新。v1.0.0 的 Release 可以保留作为历史版本，不需要删除。

v1.1.0 将 Skill 文件夹从带 `-cn` 的名称调整为平台中立名称，因此旧安装用户需要删除旧目录，再安装新的两个目录，避免出现重复 Skill。
