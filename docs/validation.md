# Validation / 验收记录

Run date: 2026-10-08. Version: 0.1.0. Platform: macOS, Codex local tools, TinyTeX XeLaTeX. No existing learner automation was changed.

## Executed checks

- **24 PDFs / 55 pages**: six complete 30-day plans and six sets of Day01–Day03. All final rendered pages inspected using contact sheets; full-resolution previews retained. Each PDF has an explanatory figure, at least five working PDF URL annotations, embedded fonts and nonempty pages. The link check confirms PDF annotation targets, not permanent external website availability.
- **21 tests passed**: approval and changed-plan/config gates, sequential days, no advance before delivery, daily limit, retry/reuse, pause, completion, concurrency lock, initialization race regression, archived-plan overwrite protection, path validation and changed-PDF rejection. Integration test actually compiles a one-section multilingual document, verifies its image, URL annotations and literal escaped TeX content, and confirms an unreviewed PDF cannot be approved. The fixture uses synthetic example.com links and is not counted as research.
- Codex bundled `quick_validate.py`: **Skill is valid**. Standard package has required YAML metadata and no unfinished scaffold placeholders.
- Standalone ZIP extracted to a temporary directory; all entrypoint/runtime/reference files found and extracted `doctor` command executed successfully. No installation into an existing user skills folder was required.
- **Six sequential example runs**: initialize → render plan → inspect → simulated approval → Day01/02/03 render/inspect/simulated delivery. All states select Day04 next; sample projects reject live schedule registration. Every final manifest hash was checked.
- Real source search/page reading and text-to-image generation were performed by the authoring agent; see [research notes](research-notes.md), [image prompts](image-prompts.json), and each course's source metadata.

Actual PDF fonts: FandolFang-Regular (Chinese FangSong fallback) and Times New Roman (English). PDFium correctly extracts Chinese text. pypdf's text extraction does not fully decode the CJK CID font mapping in this environment; it is used for PDF objects/links/fonts, while PDFium is used for accurate CJK extraction and page rendering. No missing-glyph or overfull-box warning remains in final sample manifests.

## Independent review and fixes

A separate read-only agent reproduced a concurrent initialization overwrite, an archived-plan overwrite and a one-section missing-figure defect. All three were fixed and covered by regression/integration checks. Subsequent visual review found nearly empty pages from the initial spacing helper; rejected pre-delivery versions were isolated locally and the layout helper was corrected. No rejected draft is included in the published examples. A final independent read-only pass reran all 21 tests and the 24-PDF artifact validator, confirmed the three fixes and the README compatibility disclosures, and found no blocking issue.

These checks do not mechanically verify factual truth, pedagogy, actual learner approval, image rights, or notification delivery. Those remain agent/user responsibilities. A `review` record is an attestation after inspection, not an automatic image assessment.

## Compatibility evidence

| Environment | Package / helper execution | Native scheduled delivery |
|---|---|---|
| Codex local work environment | Authoring and all six examples executed | Native tool available; multi-day delivery not tested |
| WorkBuddy | Documentation-backed import instructions | Not tested |
| DeepSeek Harness | Official local source and guide inspected | Session-local overlay limitations documented; not tested |
| OpenClaw | Documentation-backed install instructions | Not tested |
| Doubao consumer client | Native import/execution not verified | Not verified |

The Skills CLI remote install command is documented by its official site; a published-repository install has not been claimed as tested. A common file standard alone does not establish full host support. The six examples are accelerated demos, not evidence of 30 days of successful operation or learner mastery.

## Reproduce

Install dependencies from the Skill's `references/setup.md`, then run:

```sh
python3 -m unittest discover -s tests -v
python3 tools/validate_artifacts.py
python3 tools/package_skill.py
```

The test suite needs pypdf, pypdfium2, Pillow, and XeLaTeX for the integration test. PDF sample checks validate archived outputs without changing their historical source-check date. Reauthor and research a new course to test future content generation.
