# Omni Learning Assistant

**把「我想学……」变成一条每天可以走下去的学习路径。**  
**Turn “I want to learn…” into a source-grounded daily learning path.**

[下载发布版 / Releases](https://github.com/ShawnRen57/omni-learning-assistant/releases) · [中文](#中文使用指南) · [English](#english-guide) · [24 份样例 / 24 sample PDFs](examples/README.md) · [验证记录 / Validation](docs/validation.md) · [DSH 社区展示 / Community showcase](https://github.com/deepseek-ai/deepseek-harness/discussions/9207)

Omni Learning Assistant 是遵循 [Agent Skills 标准](https://agentskills.io/specification)的独立 Skill，适用于科技、经济、音乐、历史、建筑等宏观主题，以及 Agent 产品、西方建筑史、明朝历史等细分主题。它先了解你的目标与基础，生成 PDF 学习计划，获得确认后再创建每日任务。

Omni Learning Assistant is an independent Agent Skill for broad subjects and focused topics. It clarifies your goals and baseline, produces a PDF curriculum, and creates daily tasks only after you approve the plan. It is not affiliated with other products named Omni Learning Assistant.

原名 LearnPath，自 v0.2.0 起技能名与调用指令为 `omni-learning-assistant`。GitHub 仓库也已更名；现有样例和旧发布包保留原名称。

Formerly LearnPath. Since v0.2.0, the skill identifier is `omni-learning-assistant`; the GitHub repository has also been renamed; historical samples retain their original names.

## 中文使用指南

### 1. 安装

**通用方式：** 下载仓库 ZIP，找到 `skills/omni-learning-assistant/`，将整个文件夹导入或复制到 Agent 的技能目录。不要只复制 `SKILL.md`，它还需要 `scripts/` 和 `references/`。可单独下载 [轻量安装包](dist/omni-learning-assistant-skill-v0.2.0.zip)，解压后根目录为 `omni-learning-assistant/`。

支持 [Skills CLI](https://www.skills.sh/docs/cli) 的环境可运行以下命令，并在交互界面选择目标 Agent。该命令依赖 Node.js、网络和 CLI 对目标客户端的支持。

```sh
npx skills add ShawnRen57/omni-learning-assistant
```

**Codex：** 在对话中发送：

```text
请用 skill-installer 安装 https://github.com/ShawnRen57/omni-learning-assistant
仓库中的 skills/omni-learning-assistant，然后按客户端提示刷新或重启以加载。
```

也可将技能文件夹复制到当前 Codex 支持的用户技能目录；本项目开发环境为 `~/.codex/skills/omni-learning-assistant/`。以你的客户端配置和安装器检测结果为准。

| 平台 | 安装入口 | 本版本验证范围 |
|---|---|---|
| Codex | Skill 安装器或用户技能目录 | 已实测公开 ZIP 安装、CLI 原生加载与首次 PDF；未连续多日实测定时通知 |
| WorkBuddy | Skills 界面的本地包导入 | 官方文档支持；未在客户端实测完整链路 |
| DeepSeek Harness | 配置的 `.dsh/skills/omni-learning-assistant/` | 已实测公开 ZIP 安装、桌面端原生加载与首次 PDF；未实测连续定时交付 |
| OpenClaw | 工作区 skills 或 `~/.openclaw/skills/omni-learning-assistant/` | 官方文档支持；未在客户端实测完整链路 |
| 豆包 | 须先确认具体客户端版本与能力 | 未验证原生第三方 Skill + 本地执行 + 定时链路；可人工使用提示词，但不等于安装即用 |

[v0.2.0 安装与首次使用实测](docs/installation-validation.md)包含两个宿主的验收 PDF、环境版本及验证范围。建议优先使用轻量安装包。

平台入口、依据和限制见 [平台适配说明](skills/omni-learning-assistant/references/platforms.md)。**安装 Skill 不会自动补齐搜索、运行代码、文生图或定时能力。** 完整使用需要这些宿主能力以及 Python 3.10+、XeLaTeX。Agent 会按[环境说明](skills/omni-learning-assistant/references/setup.md)检查并安装缺失依赖；受限设备需采用其允许的安装方式。

**DeepSeek Harness 用户：** 见[中英双语安装与定时指南](docs/deepseek-harness.md)。使用原生文件系统 Skill 加载，无需另装 Cordis 服务插件。

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

Download the repository ZIP and import or copy the complete `skills/omni-learning-assistant/` folder into your agent's supported skill directory. The [standalone ZIP](dist/omni-learning-assistant-skill-v0.2.0.zip) contains a top-level `omni-learning-assistant/` folder. Keep its scripts and references. With a compatible Skills CLI environment, run:

```sh
npx skills add ShawnRen57/omni-learning-assistant
```

For Codex, ask its skill installer to install `skills/omni-learning-assistant` from this repository, then refresh/restart as directed by your client. WorkBuddy offers local skill import; DeepSeek Harness uses configured skills roots such as `.dsh/skills`; OpenClaw supports workspace/managed skills. **Native Doubao support has not been verified.** Prompt adaptation is not a full installation. See the [host-specific evidence and limits](skills/omni-learning-assistant/references/platforms.md).

[v0.2.0 first-use validation](docs/installation-validation.md) covers public ZIP installation, native loading and first PDF generation in Codex CLI and DSH Desktop; multi-day scheduling remains untested.

Full operation requires an agent with web research, file/command access, image access or generation, PDF inspection and suitable scheduling/delivery, plus Python 3.10+ and XeLaTeX. The package does not supply an LLM, a search subscription or a scheduler. Follow [runtime setup](skills/omni-learning-assistant/references/setup.md).

**DeepSeek Harness:** see the [bilingual installation and scheduling guide](docs/deepseek-harness.md). Omni Learning Assistant loads through the native filesystem skill provider.

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

These are accelerated, isolated demo runs with simulated approval/delivery, not a multi-day scheduler test. The [validation report](docs/validation.md) distinguishes executed tests from documentation-only platform support. Sources were checked on 2026-10-08; future lessons require fresh research.

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
