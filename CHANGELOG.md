# Changelog

## Repository rename — 2026-10-09

- Rename the GitHub repository to `ShawnRen57/omni-learning-assistant`.
- Update current repository URLs, installation commands, release notes and the existing DSH community post.
- This repository-only change keeps the installable skill at v0.2.0.


## 0.2.0 — 2026-10-09

- Rename the installable skill and invocation to `omni-learning-assistant` (Omni Learning Assistant).
- Rename the CLI entrypoint to `omni_learning.py`; preserve course format and legacy `.learnpath.lock` to avoid migration races.
- Keep the GitHub repository URL and all historical sample outputs unchanged.
- Verify public-ZIP installation, native skill loading and first PDF generation in Codex CLI and DSH Desktop; see the installation validation report.
- Reject Python below 3.10 explicitly and report the actual interpreter version.

## 0.1.1 — 2026-10-09

- Add bilingual DeepSeek Harness installation, verification and community guidance.
- Correct older schedule-overlay documentation using current upstream Host Schedule sources, including persistence, pause and delivery limits.
- Repackage the skill with updated platform guidance; runtime code and sample PDFs are unchanged.

## 0.1.0 — 2026-10-08

- Universal topic intake, plan approval before scheduling, evidence-grounded daily lessons.
- Portable Agent Skills folder, host adaptation notes, bilingual user instructions.
- XeLaTeX PDFs with figures, expansion links, font checks and page previews.
- Atomic progress files, concurrent-run lock, plan/config binding, review and delivery gates.
- Six 30-day curricula with Day01–Day03 examples, original teaching illustrations and source metadata.
- Documented platform limits; sample simulation does not claim verified native timed delivery.
