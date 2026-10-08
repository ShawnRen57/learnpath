# Host adaptation / 平台适配

Evidence checked 2026-10-08. A file format is not an execution environment. Full mode requires skill loading, web search/page reading, local Python/XeLaTeX execution, images, PDF inspection, a durable scheduler and usable delivery. Check the installed version at use time.

## Codex
Install via the built-in skill installer from the GitHub repository's `skills/learnpath` path, or copy that folder into a supported user/project skills directory. This package is developed with Codex; confirm the actual client discovers it after installation/restart. Invoke `$learnpath` or describe the learning task.

For scheduling, use the host's automation tool after the approved plan. Prefer a task-bound heartbeat when available. Verify returned job ID, timezone, status and next execution. Include absolute course path, read/next/render/review/deliver sequence, silence on duplicate/non-actionable runs, and stop-on-completion. No automatic email/other-channel sending is implied.

## WorkBuddy
Official docs describe local skill-package import and automation. Import the release ZIP or its extracted skill folder through the current Skills UI. Confirm expected archive root in the import dialog. Use the Automation UI/tool to create the approved schedule and inspect the saved task. Local execution requires the relevant client/computer to remain available; Cloud and Local capabilities differ.

Sources: https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market and https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Automation-Guide . Documentation-backed; not a guarantee that every edition can run XeLaTeX.

## DeepSeek Harness
The official filesystem skill provider scans project/user roots such as `.dsh/skills`; copy `learnpath/` into the configured skills root and start/refresh a session. Verify `/skill` or the skill catalog for the installed version. Official source: https://github.com/deepseek-ai/deepseek-harness/tree/master/packages/skill/skill-filesystem .

The inspected schedule overlay is **session-local**: `dsh web --patch apps/cli/config/examples/schedule/cordis.yml`. It supports after_seconds, absolute at, or every_seconds >=300; not calendar cron. Timers stop with the process/cold session and resume when the original session activates. No external notification. Do not describe fixed 86400-second intervals as local daily calendar scheduling across DST. Source: https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/user/guide/schedule.md . Offer explicit session reminder/manual mode unless durable host scheduling is verified. The skill does not install a daemon.

## OpenClaw
Use the configured workspace skills folder or managed `~/.openclaw/skills/learnpath`. Verify loaded skills with the installed CLI before invoking. Native scheduler is host-owned; confirm actual CLI/tool schema, timezone, session and delivery channel. Official docs: https://docs.openclaw.ai/tools/skills and https://docs.openclaw.ai/cron . Do not invent a cron command based on an older version. No ClawHub listing is claimed by publishing a GitHub repository.

## Doubao / 豆包
Native third-party SKILL.md import + shell/XeLaTeX + scheduling has **not been verified** for an identified Doubao client/version. Do not promise one-click full support. A user may paste the learning instructions or upload the plan for manual conversation use, but that is a prompt adaptation, not skill installation and not full PDF automation. Request the exact client/version and inspect its documented capabilities before changing this status. Doubao model access through another capable harness is distinct from the Doubao consumer client.

## Schedule prompt contract
"Use LearnPath at INSTALLED_SKILL_PATH to continue COURSE_ABSOLUTE_PATH. Read config, approved plan, state and recent two lessons; run next. Respect pause/completion/daily limit. Reuse existing artifact when pending review/delivery. For a new lesson, actually search/read sources, author within time budget, include a teaching figure and >=5 expansion links, compile XeLaTeX, inspect every page, then deliver PDF. Record delivery only when confirmed. Notify on successful lesson, meaningful failure or user action; remain quiet on repeats. When all days are delivered, stop this host schedule and verify."

Replace placeholders with observed paths/IDs. Keep the original host job ID in state. A host task that cannot attach or link the PDF is not complete delivery support.
