# Editorial Revision Status

The generated PDFs are independently edited companion notes reconstructed from machine transcripts, subtitles, selected blackboard frames, and identified references. They are not exact transcripts, Leonard Susskind's original manuscripts, or lecturer-endorsed editions.

## Corpus Baseline

The July 2026 audit covers 19 generated books and 175 chapters. It found systematic prompt-shaped prose, repetitive lecture choreography, forced Q&A and summaries, missing provenance, weak figure metadata, duplicate title pages, and ambiguous authorship declarations. The detailed reproducible audit is maintained in [`Video2Book/references/susskind-corpus-audit-2026-07.md`](../Video2Book/references/susskind-corpus-audit-2026-07.md).

## Revision Order

The approved production queue now covers 15 books and 137 chapters. It revises all nine supplementary courses first, followed by the latest complete Classical Mechanics, Quantum Mechanics, Special Relativity, General Relativity, Statistical Mechanics, and Cosmology runs. The completed Cosmology pilot and three older or partial duplicate runs are excluded from this pass.

The tracked manifest at `references/editorial_revision_queue.json` remains the source of truth for course selection and order. Current work is performed directly, one chapter at a time, under [`direct_editorial_goal.md`](direct_editorial_goal.md), without a tmux writer queue. Each accepted chapter receives an exhaustive transcript-beat audit, blackboard and Q&A verification, a fidelity report, a machine-readable source map, a clean compile, and its own commit and push. Normal and pocket PDFs are republished only after every chapter in a course passes.

## Pilot Result

The Cosmology pilot completed on July 16, 2026. All eight chapters pass the source-fidelity critic and deterministic prose scan, covering 92 verified classroom exchanges, 27 figure decisions, and 222 timestamped source-map entries. The merged 83-page edition compiles without final-pass errors, undefined references, or overfull boxes.

Local 6-by-9-inch review editions were also built at normal and 1.2-times font size. They contain 122 and 152 pages respectively, and both report zero actionable overfulls, page-builder overflows, underfull paragraphs, or leaked TeX sizing tokens. The normal, pocket, and 1.2-times pocket artifacts were visually checked at the cover, front matter, chapter openings, wrapped running heads, equations, Q&A blocks, and retained blackboard figures.

The pilot informed the stricter direct editorial standard. Older duplicate editions remain available but are excluded while the canonical supplementary and latest complete core sequence is revised.
