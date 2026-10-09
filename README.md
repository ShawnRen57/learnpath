# Omni Learning Assistant

**把「我想学……」变成一条每天可以走下去的学习路径。**  
**Turn “I want to learn…” into a source-grounded daily learning path.**

[下载发布版 / Releases](https://github.com/ShawnRen57/omni-learning-assistant/releases) · [中文](#中文使用指南) · [English](#english-guide) · [24 份样例 / 24 sample PDFs](examples/README.md) · [验证记录 / Validation](docs/validation.md) · [v1.0.0 中英验收 / Bilingual acceptance](validation/release-v1.0.0/README.md) · [DSH 社区展示 / Community showcase](https://github.com/deepseek-ai/deepseek-harness/discussions/9207)

Omni Learning Assistant 是遵循 [Agent Skills 标准](https://agentskills.io/specification)的独立 Skill，适用于科技、经济、音乐、历史、建筑等宏观主题，以及 Agent 产品、西方建筑史、明朝历史等细分主题。它先了解你的目标与基础，生成 PDF 学习计划，获得确认后再创建每日任务。

Omni Learning Assistant is an independent Agent Skill for broad subjects and focused topics. It clarifies your goals and baseline, produces a PDF curriculum, and creates daily tasks only after you approve the plan.

## 中文使用指南

### 1. 安装

#### a. 通用快捷安装（对话指令）

把下面的消息发送到 Agent 对话框，由 Agent 按当前客户端的原生技能方式安装：

```text
请安装 omni-learning-assistant：
https://github.com/ShawnRen57/omni-learning-assistant
请优先下载 Releases 最新的轻量 Skill ZIP，完整安装并保留 scripts、references、agents。
安装后确认技能可发现，并告诉我如何开始使用。
```

客户端要求手动上传时，下载 [Skill ZIP](dist/omni-learning-assistant-skill-v1.0.0.zip)，按下方步骤完成。

#### b. 手动安装（按平台）

上传时选择 ZIP；目录安装时解压并复制整个 `omni-learning-assistant/` 文件夹。

| Agent | 手动操作 | 官方依据 |
|---|---|---|
| Codex | 放入 `~/.agents/skills/omni-learning-assistant/`，或项目 `.agents/skills/`；确认加载后用 `$omni-learning-assistant` 调用 | [Skills 文档](https://learn.chatgpt.com/docs/build-skills) |
| WorkBuddy | **专家 · 技能 · 连接器 → 技能 → 添加技能 → 上传技能**，选择 ZIP，导入后启用 | [技能说明](https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market) |
| DeepSeek Harness | 放入 `~/.dsh/skills/omni-learning-assistant/`，或项目 `.dsh/skills/`；在技能目录确认加载 | [文件系统 Skill provider](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/skill/skill-filesystem/README.md) |
| OpenClaw | 解压后执行 `openclaw skills install /path/to/omni-learning-assistant --global`，再用 `openclaw skills list` 查看 | [Skills CLI](https://docs.openclaw.ai/cli/skills) |
| 豆包工作界面 | **插件 · 技能 · 伙伴 → 技能 → 添加 → 上传技能**；选 **选择文件**上传 ZIP，或 **选择文件夹**导入完整目录 | 官方桌面端 2.31.4 上传界面核对，2026-10-09 |

DSH 的“插件 → 添加插件”用于 DSH 插件组合包；本项目采用上表的原生 Skill 目录安装。豆包步骤适用于提供上述技能入口的工作界面。更多操作细节和依据见 [安装说明](skills/omni-learning-assistant/references/install.md)。

Agent 会检查学习材料所需的工具与 Python 3.10+、XeLaTeX 环境，按 [环境说明](skills/omni-learning-assistant/references/setup.md)处理缺失依赖。

### 2. 只说你想学什么

```text
用 omni-learning-assistant 带我学习西方建筑史，目标是旅行时能看懂建筑。
```

Agent 会集中追问：学习目标和已有基础、学习多少天、每天几分钟、每日执行时间与时区、是否包括周末、文档语言及保存位置。你已经提供的信息不会重复询问。

也可以一次说完整：

```text
用 omni-learning-assistant 学习 Agent 产品设计。我是产品经理，有产品经验但 AI 基础有限。
目标是能独立定义 Agent 产品并准备面试。学习 30 天，每天 15 分钟，
每天 10:00，Asia/Shanghai，含周末，中文，保存到我指定的课程文件夹。
先给我 PDF 计划，等我确认后创建每日任务；确认后立即开始 Day01。
```

默认在约定时间**开始生成**，完成检索与检查后交付；不承诺在同一时刻送达。没有可用调度器时，Agent 会说明限制，并提供手动续学方式。

### 3. 确认计划，再开始课程

你先收到包含每日主题、学习目标和节奏的 PDF，随后可回复：

```text
确认这份计划，按上述时间开始，每日材料保存到这个课程目录。
```

之后每份学习材料包含概念说明、教学插图、练习与参考要点、承上启下的回顾，以及不少于 5 个带说明的扩展链接。核心阅读与练习以约定时间为限，选读另计。中文优先仿宋，英文优先 Times New Roman；本机缺字库时使用可用字体，实际结果保留在生成记录中。

继续、暂停和调整示例：

```text
继续这个 Omni Learning Assistant 课程，先检查上次交付到了哪一天。
暂停这个课程，同时暂停对应的定时任务。
我想调整学习目标，请保留旧档案，为我生成新的计划供确认。
```

内容生成、检查、交付分别记录；失败不跳课，重复执行优先复用已有文档。通知与本地文件写入并非原子操作，遇到不确定状态会核对交付记录。收到 PDF 不会被记为已经掌握知识。

### 4. 样例与截图

六组样例均含完整 **30 天计划 + Day01 + Day02 + Day03**，共 **24 份 PDF**；样例为中文。它们使用演示身份、模拟计划批准与连续交付，**没有创建真实定时任务**。联网核验日期为 2026-10-08，详见[研究记录](docs/research-notes.md)。前三天共用一张分区插图，逐课聚焦 A/B/C 区以保持连贯。

| 范围 | 主题与用户短提示词 | 演示侧重点 |
|---|---|---|
| 宏观 | 科技通识：`我想系统学习科技，能看懂重要技术趋势。` | 系统、证据与能量 |
| 宏观 | 经济学：`我想从零学习经济学，理解日常经济现象。` | 选择、供需与边际决策 |
| 宏观 | 音乐通识：`我想学习音乐，提升欣赏不同作品的能力。` | 主动聆听、节奏与旋律 |
| 微观 | Agent 产品设计：`我想学习 Agent 产品设计，准备产品经理面试。` | 任务、控制方式与权限 |
| 微观 | 西方建筑史：`我想学习西方建筑史，旅行时能看懂建筑。` | 空间、柱式与拱券 |
| 微观 | 明朝历史：`我想系统学习明朝历史，理解重要制度和事件。` | 时间线、制度与史料 |

以下均为真实生成 PDF 的首屏截图。点击主题进入该组的四份文档与可复用源文件；[总索引](examples/README.md)提供全部 PDF 的直接链接。

| 科技通识 / Technology | 经济学 / Economics | 音乐通识 / Music |
|---|---|---|
| [![科技首日](docs/screenshots/technology.png)](examples/technology) | [![经济首日](docs/screenshots/economics.png)](examples/economics) | [![音乐首日](docs/screenshots/music.png)](examples/music) |

| Agent 产品 / Agent product | 西方建筑史 / Architecture | 明朝历史 / Ming history |
|---|---|---|
| [![Agent首日](docs/screenshots/agent-product.png)](examples/agent-product) | [![建筑首日](docs/screenshots/architecture.png)](examples/architecture) | [![明史首日](docs/screenshots/ming-history.png)](examples/ming-history) |

## English guide

### Install

#### a. Quick installation through chat

Send this message in your agent's conversation:

```text
Install omni-learning-assistant from:
https://github.com/ShawnRen57/omni-learning-assistant
Prefer the latest lightweight Skill ZIP in Releases. Use this client's native
skill installation mechanism, keep all bundled resources, then verify discovery.
```

If the client requires an upload, download the [Skill ZIP](dist/omni-learning-assistant-skill-v1.0.0.zip) and follow the steps below.

#### b. Manual installation by agent

| Agent | Steps |
|---|---|
| Codex | Copy the extracted folder into user/project `.agents/skills/`; invoke `$omni-learning-assistant`. |
| WorkBuddy | Experts / Skills / Connectors → Skills → Add skill → Upload skill; select the ZIP and enable it. |
| DeepSeek Harness | Copy the complete bundle into user `~/.dsh/skills/` or project `.dsh/skills/`; verify discovery. |
| OpenClaw | Run `openclaw skills install /path/to/omni-learning-assistant --global`, then `openclaw skills list`. |
| Doubao work mode | Plugins / Skills / Partners → Skills → Add → Upload skill; select the ZIP or folder. |

The [installation guide](skills/omni-learning-assistant/references/install.md) links to the official sources. Doubao's upload steps were checked in its official macOS desktop client. DSH's Add plugin dialog handles plugin bundles; use filesystem skill installation for this package.

The agent checks research, execution, image and PDF tools plus Python/XeLaTeX dependencies. See [runtime setup](skills/omni-learning-assistant/references/setup.md).

### Start with a topic

```text
Use $omni-learning-assistant to teach me Western architectural history so I can understand buildings when traveling.
```

The agent asks for missing goals, prior knowledge, course length, daily study time, execution time/timezone, weekdays, language and output folder. For a complete request:

```text
Use $omni-learning-assistant to help me learn Agent product design. I am a product manager
with limited AI background. Plan 30 days at 15 minutes per day, at 10:00
Asia/Shanghai including weekends. Use English and save to my course folder.
Send the PDF plan first. Wait for my approval before scheduling daily lessons.
Start Day01 immediately after approval.
```

Approve the plan or request revisions. The agent then creates and verifies a native host task when supported. Generation starts at the scheduled time; delivery follows research and checks. Without a suitable scheduler, continuation remains manual.

Each lesson includes focused explanation, an illustrative image, a short exercise and answer guidance, a recap, and at least five useful expansion links. Optional reading is outside the core time budget. PDFs use XeLaTeX with detected font fallbacks. Progress advances after delivery, failed work resumes at the same lesson, and completion stops the host schedule.

```text
Continue my Omni Learning Assistant course from the earliest undelivered day.
Pause this course and its host schedule.
Preserve the old course and propose a revised plan for my new goal.
```

### Explore the examples

The [sample index](examples/README.md) links to six Chinese-language curricula: **technology, economics and music** as broad topics, and **Agent product design, Western architectural history and Ming history** as focused topics. Each includes a full 30-day plan and days 1–3. The screenshots above are actual PDF pages.

Short starting prompts: “Help me understand major technology trends”; “Teach me economics from scratch”; “Help me appreciate music”; “Teach me Agent product design for PM interviews”; “Teach me to read Western buildings”; “Help me understand Ming institutions and events.”

These are isolated demo runs with simulated approval/delivery. The [validation report](docs/validation.md) covers Skill behavior and generated documents. Sources were checked on 2026-10-08; future lessons require fresh research.

## Repository & development

```text
skills/omni-learning-assistant/     Installable, self-contained skill
examples/            Six curricula, 24 PDFs, JSON, TeX, Markdown, previews and manifests
docs/                Research, screenshots, validation and design decisions
tests/               State and real XeLaTeX integration checks
tools/               Authored sample content and packaging/inspection helpers
dist/                Lightweight installable ZIP
```

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r skills/omni-learning-assistant/scripts/requirements.txt
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python skills/omni-learning-assistant/scripts/omni_learning.py --project examples/technology doctor
```

Tests include a real XeLaTeX compile when the binary is available. Sample source files are historical authored outputs, not a script that performs web research. Create a new course for new runs; do not relabel old source checks as fresh research or reset the sample state to use it as a learner record.

[MIT license](LICENSE) · [Attribution and font/image notes](ATTRIBUTION.md) · [Changelog](CHANGELOG.md)
