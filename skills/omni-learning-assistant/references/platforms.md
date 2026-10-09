# Host adaptation / 平台适配

Evidence checked 2026-10-08; DeepSeek Harness refreshed 2026-10-09. A file format is not an execution environment. Full mode requires skill loading, web search/page reading, local Python/XeLaTeX execution, images, PDF inspection, a durable scheduler and usable delivery. Check the installed version at use time.

## Codex
Install via the built-in skill installer from the GitHub repository's `skills/omni-learning-assistant` path, or copy that folder into a supported user/project skills directory. This package is developed with Codex; confirm the actual client discovers it after installation/restart. Invoke `$omni-learning-assistant` or describe the learning task.

For scheduling, use the host's automation tool after the approved plan. Prefer a task-bound heartbeat when available. Verify returned job ID, timezone, status and next execution. Include absolute course path, read/next/render/review/deliver sequence, silence on duplicate/non-actionable runs, and stop-on-completion. No automatic email/other-channel sending is implied.

## WorkBuddy
Official docs describe local skill-package import and automation. Import the release ZIP or its extracted skill folder through the current Skills UI. Confirm expected archive root in the import dialog. Use the Automation UI/tool to create the approved schedule and inspect the saved task. Local execution requires the relevant client/computer to remain available; Cloud and Local capabilities differ.

Sources: https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market and https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Automation-Guide . Documentation-backed; not a guarantee that every edition can run XeLaTeX.

## DeepSeek Harness
Install the complete `omni-learning-assistant/` bundle directly under a filesystem-provider root: `<project>/.dsh/skills/omni-learning-assistant/` or `$DSH_HOME/skills/omni-learning-assistant/` (default `~/.dsh/skills/omni-learning-assistant/`). The provider scans one level, so do not nest the repository's `skills/omni-learning-assistant` beneath another folder. Verify that `omni-learning-assistant` appears in the skill catalog and that its scripts/references resolve. With the default watcher, changes reach the next catalog without restart. Custom profiles must mount `@deepseek-ai/dsh-skill` and `@deepseek-ai/dsh-skill-filesystem`. This is an Agent Skill bundle, not a Cordis service plugin.

Current upstream's shipped Web profile provides persistent **Host Schedule**, with `schedule_create`, `schedule_list`, `schedule_update`, and `schedule_delete` in the standard/cordis/ptc presets. It supports daily/weekly local time with an explicit IANA zone and five-field cron. Inspect the installed tool schema; create the approved daily rule, verify it with list/UI, and store the returned job ID in the course state. Do not substitute a fixed 86400-second interval for a local daily rule. Minimal presets and delegated subagents do not expose these tools.

Tasks remain stored when the original session is closed; while the Host runs it restores that session for a due follow-up. Closing the Host stops execution until restart; recurring catch-up emits only the latest missed occurrence. A reminder delivery record proves inbox persistence, not completed PDF generation or external notification. Keep Omni Learning Assistant's separate review/delivery checks and duplicate-run guards.

Native pause is not supported in the inspected upstream. A learner's pause request should pause the course state immediately; explain that the host may still wake and exit quietly. If stopping host wakeups is needed, explain that deleting the task also removes its host delivery history, preserve relevant records, and obtain authorization for that deletion. Completion cleanup should follow the agreed lifecycle and verify the host task is stopped. Do not claim a host pause was performed when only the course was paused.

The older local checkout inspected for LearnPath v0.1.0 used a session-local schedule overlay. That limitation is not a current upstream-wide limitation. Verify the installed version/profile before selecting automatic or manual continuation. Current upstream documentation was checked at commit `5badb15009ae1756c3afe0ae0cef1faafc290ccc`; native DSH end-to-end PDF scheduling has not been tested by this project.

Sources: [filesystem provider](https://github.com/deepseek-ai/deepseek-harness/blob/5badb15009ae1756c3afe0ae0cef1faafc290ccc/packages/skill/skill-filesystem/README.md), [schedule guide](https://github.com/deepseek-ai/deepseek-harness/blob/5badb15009ae1756c3afe0ae0cef1faafc290ccc/docs/user/guide/schedule.md).

## OpenClaw
Use the configured workspace skills folder or managed `~/.openclaw/skills/omni-learning-assistant`. Verify loaded skills with the installed CLI before invoking. Native scheduler is host-owned; confirm actual CLI/tool schema, timezone, session and delivery channel. Official docs: https://docs.openclaw.ai/tools/skills and https://docs.openclaw.ai/cron . Do not invent a cron command based on an older version. No ClawHub listing is claimed by publishing a GitHub repository.

## Doubao / 豆包
Native third-party SKILL.md import + shell/XeLaTeX + scheduling has **not been verified** for an identified Doubao client/version. Do not promise one-click full support. A user may paste the learning instructions or upload the plan for manual conversation use, but that is a prompt adaptation, not skill installation and not full PDF automation. Request the exact client/version and inspect its documented capabilities before changing this status. Doubao model access through another capable harness is distinct from the Doubao consumer client.

## Schedule prompt contract
"Use Omni Learning Assistant at INSTALLED_SKILL_PATH to continue COURSE_ABSOLUTE_PATH. Read config, approved plan, state and recent two lessons; run next. Respect pause/completion/daily limit. Reuse existing artifact when pending review/delivery. For a new lesson, actually search/read sources, author within time budget, include a teaching figure and >=5 expansion links, compile XeLaTeX, inspect every page, then deliver PDF. Record delivery only when confirmed. Notify on successful lesson, meaningful failure or user action; remain quiet on repeats. When all days are delivered, stop this host schedule and verify."

Replace placeholders with observed paths/IDs. Keep the original host job ID in state. A host task that cannot attach or link the PDF is not complete delivery support.
