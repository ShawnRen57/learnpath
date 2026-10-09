# Plan research notes

Checked in Asia/Shanghai on 2026-10-09. Search and page reading were performed with the host web tool. Source records in sources.json retain exact URLs, publishers, publication-date uncertainty, update dates and recommended reading. Search-result relative dates were not substituted for publication dates.

## Search trail
- site.science.nasa.gov skywatching stars planets twinkle city dark sky
- site.science.nasa.gov moon phases sunlight not shadow
- site.timeanddate.com astronomy night sky use sky map

Opened the five sources in sources.json, read the relevant sections, and followed the NASA FAQ location link to its canonical destination. These are specific sources, not homepage quotas.

## Evidence and curriculum decisions
- S1: supports a beginner course with unaided eyes and optional chart assistance; separates faint-target conditions from bright-target possibilities. No object is promised on a trip.
- S2: atmospheric turbulence explains the typical appearance difference. The chart-confirmation task is an instructional decision; the source is an older expert answer, not a current observing forecast. Only its relevant explanation is used; old external links are unnecessary.
- S3: supports the lit-half model and approximate phase-related timing. Use simplified geometry with its limits made explicit, and distinguish ordinary phases from eclipse shadow.
- S4: publisher help documents show the need to set place, date and time and read visibility. No app was tested. Existing phone-chart workflows may differ.
- S5: supports the outing checks. Avoid repeating the page’s ambiguous phrase about weeks around new Moon; use actual local phase and rise/set checks instead.
- The learning sequence, indoor practices, daily review intervals and assessment threshold are course-design choices. Hypothetical city/rural plans are not measured field results.

## Image source investigation
Opened https://science.nasa.gov/resource/phases-of-the-moon-2/ (published 2014-08-14, credit NASA/Bill Dunford, page updated 2025-08-15). Opened its image download URL: https://assets.science.nasa.gov/dynamicimage/assets/science/psd/solar/2023/09/m/moon_phases.png?crop=faces%2Cfocalpoint&fit=clip&h=3728&w=3728 . Also opened NASA media usage guidance: https://www.nasa.gov/nasa-brand-center/images-and-media/ . The guidance permits educational use of NASA content under its terms and distinguishes third-party rights; no blanket rights were inferred for every NASA-hosted photograph.

Command urllib download failed with DNS resolution error. IAB unavailable; two Chrome extension attempts failed with request-header-policy errors; native Chrome computer access not approved. The NASA image was therefore not redistributed.

## Supported alternative
Used real host image_gen generation for the course navigation figure. No code-drawn illustration, developer checkout, old course example, copied learner identity, or fabricated source diagram was used. See image-prompt.txt and image-provenance.json. Inspected the selected image: exact day headings and footer are legible; panel sequence matches the curriculum; the two Moon icons are explicitly captioned as alternatives. No orbit geometry, visibility scale or official logo appears.

## Capability limits
Specified Python 3.12.14 and existing TinyTeX XeLaTeX were found by installed helper doctor. Host search/page reading and local file/command access work. PDF previews are produced by the installed helper and visually inspected by the agent. Image generation works, with a native tool cache outside the course directory; all course-owned files and exports are local here. No scheduler or external notification workflow is exercised: this sample explicitly forbids live schedules. Final chat links are the plan delivery route; no lesson delivery is recorded.

Course timing is an estimate, not a timed learner trial. No China website accessibility, live phone compass, local weather or site-access testing was performed. Later lessons must search/open sources again and retain fresh notes.
