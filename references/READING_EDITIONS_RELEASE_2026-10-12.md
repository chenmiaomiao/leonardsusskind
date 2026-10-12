# Multilingual Reading Editions - 2026-10-12

## Published Scope

- 16 final polished companion books, 145 chapters.
- 13,236 source-bound segments per language, complete in Japanese and Simplified Chinese.
- 32 independent translated PDFs, 6,962 pages total, with covers and outlines.
- Default translated PDF paper: **177.6 x 252 mm**, 12 pt body on a 17 pt baseline.
- Original English TeX and PDFs remain unchanged; legacy `pocket_1_2x` names
  describe type enlargement, not the new paper dimensions.
- These are independently edited, AI-assisted companion notes, not original
  Susskind manuscripts or lecturer-endorsed translations.

## Verification

All 32 PDFs passed compilation, source/translation/hash coverage, outline,
missing-glyph, reference, overflow, page-dimension and text-bound checks.
Chapter math, diagram and figure-command inventories match the final English
source. See [the machine-readable audit](reading_editions_audit.json) and each
edition's `quality.json`. Semantic review is sampled, not exhaustive.

Bunko exports preserve 17,848 aligned reading blocks and 1,617 figure blocks
across all 145 chapters. All 62,721 rich mathematical expressions across the
three language layers passed the app's KaTeX renderer. Front matter, overview
paragraphs, classroom Q&A, footnotes, captions and simple tables are retained.
Existing book identities, matched passage IDs and old content-addressed chapter
files are preserved. Updated bundles use the existing schema-1 app contract.

Verification completed:

- 39 translation-pipeline tests, 12 importer/figure tests, 8 catalogue tests,
  and 33 LazyLearn reader tests passed.
- Local desktop/mobile Bunko checks passed for Higgs and Particle Physics 2.
- Published Bunko Higgs checks passed: 114 aligned blocks in each language,
  rendered figures, no KaTeX errors or outer-page horizontal overflow.
- Published LazyLearn Japanese/Chinese PDF.js canvas checks passed on desktop
  and mobile; the sidebar starts closed and pages fit the reader width.
- GitHub's 32 PDF blob hashes match the verified local PDFs.
- The live Bunko catalogue advertises all 16 books as `en`, `ja`, `zh`.
- All eleven README availability notices and cover-language links are generated
  from verified editions, and repeat generation is idempotent.

The broad profile README lint still reports pre-existing differences in section
counts and historical command examples between translations. Those unrelated
document structures were preserved; this is not an all-green profile-lint claim.
The updated availability, citation and collaboration sections are synchronized.

## Release Locations

| Artifact | Repository / revision |
| --- | --- |
| Independent PDFs, TeX, audit and multilingual README | [leonardsusskind, 4ff189d6](https://github.com/lachlanchen/leonardsusskind/commit/4ff189d6) |
| Aligned reader bundles and catalogue | [bunko-books, 7a25f0a2](https://github.com/lachlanchen/bunko-books/commit/7a25f0a2) |
| Language selector and reading links | [LazyLearn, bb1526b](https://github.com/lachlanchen/LazyLearn/commit/bb1526b) |

Read through [Bunko](https://lachlan.lazying.art/Bunko/) or
[LazyLearn](https://learn.lazying.art/leonardsusskind-reader.html).
The Bunko exporter and browser checks are committed on the existing tooling
branch; no unrelated native-app changes were deployed. LazyLearn's unrelated
local catalogue and cover work was not included in the publication commit.

The translation tmux session exited after completing its queue. No other
project's queue or desktop was restarted. See
[the workflow](POLISHED_TRANSLATIONS.md#reading-editions-and-release-checks)
for repeatable validation and release commands.
