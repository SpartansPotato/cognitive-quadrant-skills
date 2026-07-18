<p align="center">
  <img src="./docs/assets/github-banner.png"
       alt="认知四象限 Skills 项目横幅"
       width="100%">
</p>

# 认知四象限 Skills

**Express 表达 · Ask 求助 · Iterate 迭代 · Explore 探索**

<p align="center">
  <img src="./docs/assets/workflow-overview.png"
       alt="表达 提问 迭代 探索工作流"
       width="92%">
</p>

一套面向反思性思考、知识边界拓展与教师科研的双语、跨平台 Agent Skills。**v1.1.0** 将两个 Skill 重构为平台中立核心，可用于 **WorkBuddy、OpenAI Codex 和 Claude Code**。

[English README](README.md)

> 当前工具包已经按照三个平台公开文档中的 Skill 结构进行适配。不同平台开放的联网、文件、搜索和成果生成能力可能不同，实际运行效果仍取决于宿主平台、模型与权限配置。

## 这个项目有什么不同？

本项目不把“已知—未知四象限”当作一次性填写的 2×2 表格，而是把它转化为持续推进认知的四个动作：

1. **Express｜表达**：区分事实、经验、判断、假设、限制与已有资源；
2. **Ask｜求助**：把模糊困惑转化为可回答、可检索、可询问或可验证的问题；
3. **Iterate｜迭代**：发现隐性经验、默认假设、逻辑矛盾、未使用的证据和新的问题定义；
4. **Explore｜探索**：引入新视角、新理论、新变量、新利益相关者、新风险、新机会和未来情境。

最终目标不是让 AI 生成更多内容，而是形成：

> **更准确的问题定义、明确的不确定性地图，以及可以验证的下一步行动。**

## 包含两个 Skill

### 认知四象限·思考与探索助手

目录：[`skills/cognitive-quadrant-general`](skills/cognitive-quadrant-general)

适用于：

- 看清复杂问题；
- 检查假设和认知盲区；
- 比较选择；
- 迭代项目、计划、产品或内容想法；
- 在需要时结合证据拓宽知识边界；
- 形成行动计划、可编辑报告或四象限总结。

通用安装包：[`releases/cognitive-quadrant-general-v1.1.0.zip`](releases/cognitive-quadrant-general-v1.1.0.zip)

### 认知四象限·教师科研与创新助手

目录：[`skills/cognitive-quadrant-teacher-research`](skills/cognitive-quadrant-teacher-research)

适用于：

- 将教学实践转化为可研究的问题；
- 优化选题、研究问题、申报书、论文或研究框架；
- 识别证据缺口和理论视角；
- 区分真正的创新与热门词语组合；
- 提出包含验证路径与风险的创新方向；
- 生成可编辑研究报告和证据表。

通用安装包：[`releases/cognitive-quadrant-teacher-research-v1.1.0.zip`](releases/cognitive-quadrant-teacher-research-v1.1.0.zip)

## 中英文可编辑模板

<p align="center">
  <img src="./docs/assets/template-preview.png"
       alt="中英文双语模板包"
       width="92%">
</p>

两个 Skill 均包含完整的**英文版**和**简体中文版**可编辑 Word 模板。每套语言模板均包括：

- 模板包使用说明；
- 四象限认知梳理模板；
- 深度分析模板；
- 填写完成示例；
- Markdown 降级模板。

目录：

- `skills/cognitive-quadrant-general/assets/templates/en/`
- `skills/cognitive-quadrant-general/assets/templates/zh-CN/`
- `skills/cognitive-quadrant-teacher-research/assets/templates/en/`
- `skills/cognitive-quadrant-teacher-research/assets/templates/zh-CN/`

中英文 Word 文件采用相互对应的结构、视觉系统和报告逻辑，可根据用户语言生成相应成果。

## 三个平台的兼容关系

| 能力 | WorkBuddy | Codex | Claude Code |
|---|---|---|---|
| 核心 `SKILL.md` 工作流 | 支持 | 支持 | 支持 |
| 根据描述自动匹配 | 取决于平台版本 | 支持 | 支持 |
| 显式调用 | Skill界面或提示词 | `$skill-name` 或 `/skills` | `/skill-name` |
| 用户级安装 | 本地上传Skill | `~/.agents/skills/` | `~/.claude/skills/` |
| 项目级安装 | 取决于平台版本 | `.agents/skills/` | `.claude/skills/` |
| `manifest.yaml` | WorkBuddy读取 | 忽略 | 忽略 |
| `agents/openai.yaml` | 忽略 | 支持时读取 | 忽略 |
| 联网、文件与成果输出 | 取决于平台 | 取决于工具配置 | 取决于权限和工具 |

不同平台只读取自己认识的配置文件，其他文件不会改变核心工作流。

## 快速安装

### WorkBuddy

1. 从 [`releases`](releases) 下载其中一个 ZIP；
2. 在 WorkBuddy 中打开 Skill 管理；
3. 选择上传或导入本地 Skill；
4. 上传 ZIP 并启用。

详细说明：[`docs/installation-workbuddy.zh-CN.md`](docs/installation-workbuddy.zh-CN.md)

### Codex

用户级安装：

```bash
mkdir -p ~/.agents/skills
cp -R skills/cognitive-quadrant-general ~/.agents/skills/
cp -R skills/cognitive-quadrant-teacher-research ~/.agents/skills/
```

也可以运行：

```bash
bash scripts/install-codex.sh
```

详细说明：[`docs/installation-codex.zh-CN.md`](docs/installation-codex.zh-CN.md)

### Claude Code

用户级安装：

```bash
mkdir -p ~/.claude/skills
cp -R skills/cognitive-quadrant-general ~/.claude/skills/
cp -R skills/cognitive-quadrant-teacher-research ~/.claude/skills/
```

也可以运行：

```bash
bash scripts/install-claude-code.sh
```

详细说明：[`docs/installation-claude-code.zh-CN.md`](docs/installation-claude-code.zh-CN.md)

## 设计原则

- **平台中立**：不能默认某个模型、搜索、文件、API或操作系统一定存在；
- **跟随用户语言**：中文用户使用自然简体中文，英文用户使用清晰专业英文；
- **渐进式加载**：主 Skill 保持简洁，需要时再读取详细参考文档；
- **证据分级**：区分已核实事实、有来源解释、推断、假设与未知；
- **联网降级**：无法联网或不能生成文件时继续分析，明确局限并形成验证清单；
- **行动导向**：最终提出少量、可逆、可观察、可验证的下一步行动；
- **诚实交付**：只有宿主平台真正生成文件后，才能告诉用户文件已经完成。

## 验证

```bash
python scripts/validate_skills.py
```

仓库中的 GitHub Actions 会在提交和 Pull Request 时运行相同的结构检查。

## 原创性说明

本项目不主张发明“已知—未知四象限”。原创贡献主要包括：

- 将四象限重构为 **Express—Ask—Iterate—Explore** 连续认知工作流；
- 将用户对话、材料分析、证据检索、认知更新、创新生成和成果交付串联起来；
- 面向中国教师、国内模型和受限网络环境进行适配；
- 使用同一套核心工作流兼容 WorkBuddy、Codex 和 Claude Code。

详见 [`docs/originality-and-prior-art.md`](docs/originality-and-prior-art.md)。

## 局限

- Skill 可以提高流程一致性，但不能保证事实准确、选题原创或决策正确；
- “未知的未知”属于探索假设，不是已经证实的事实；
- 健康、法律、金融和安全等高风险事项仍需专业人员复核；
- 实际可使用的工具和文件格式取决于宿主平台。

## 许可证

Apache License 2.0，详见 [`LICENSE`](LICENSE)。

## 作者

由 **马潇（Ma Xiao）** 创建和维护。研究方向包括酒店管理教育、生成式人工智能、教师发展和职业教育。
