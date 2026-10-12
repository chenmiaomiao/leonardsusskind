# Final Polished Japanese and Chinese Editions

This queue translates the **accepted editorial TeX**, never `draft.tex`, OCR,
legacy unpolished PDFs, or the earlier duplicate lecture runs. It includes the
15-course editorial queue and its completed eight-chapter Cosmology pilot:
16 books, 145 chapters, Japanese and Simplified Chinese editions.

Each language is an **independent, normally readable book**, not an interlinear
export. The original English edition remains unchanged. Bunko/LazyLearn may
later compose interlinear editions from the aligned paragraph data, but that
must not replace or delay these standalone translations.

The short Higgs book is the first pilot. Both translated PDFs must pass a
manual visual/semantic review before the other courses start. These are
AI-assisted companion translations, not Susskind manuscripts or endorsed
translations. Automatic checks and sampled semantic review do not establish
error-free translation throughout a book.

## Pipeline

1. Verify chapter counts and passing `editorial_fidelity.json` records.
2. Hash-lock the final TeX and prepare losslessly masked paragraph segments.
3. Use pylatexenc's structured parser to preserve all syntax, equations,
   numeric values, references, asset paths and environments. Translate prose,
   titles, introductions, captions, questions and responses with DeepSeek.
   Inline math/reference tokens can reorder within the same structural block
   for natural Japanese syntax; display equations, braces and environments
   cannot move. Reordered and retried rows receive additional semantic review.
4. Cache valid segments and retry only invalid segments once. Up to two targeted
   reasoning-model repairs may then address the failed segments. Attempts are
   persisted before requests, so restarting cannot silently reset the budget.
   API transport errors have three bounded attempts; exhaustion stops new calls
   across all workers. There is no perpetual quota retry loop or hidden Codex
   reviewer fleet.
5. Reassemble real TeX, retaining source figure assets and the accepted layout.
   Use XeLaTeX with Noto CJK fonts. Original blackboard writing and English labels
   inside frozen mathematical displays are intentionally retained, not redrawn.
6. Build three passes; require a nonempty PDF and outline, CJK text, no missing
   glyphs, unresolved references or overfull boxes. Run a sampled semantic audit
   covering opening and technical paragraphs from each chapter plus repaired or
   reordered rows, in bounded ten-pair review batches. Unresolved issues
   receive up to two source-bound, paragraph-only semantic repairs followed by
   a fresh review. Unresolved issues block that language's publication, not the
   remaining chapters or later books, and never create an available download.
7. Update the README availability table, with PDF links only for validated output.

No source English file is overwritten. Per-language output is under
`translations/<course-id>/{ja,zh}/`; intermediate requests, caches, usage logs,
build artifacts and queue state are under ignored `.translation-work/`.
Original figure directories are referenced by relative TeX paths, not duplicated.
Availability is bound to the PDF and translated-TeX hashes. Preparation and manual
compilation share the queue lock and cannot race a live worker run.

## Commands

Dependencies: Python with `pylatexenc==2.10`, `openai`, `PyMuPDF`; XeLaTeX,
Noto Serif/Sans CJK fonts and tmux. Reuse the shared Python environment. The
transport comes from `../ZhJpBook/scripts/interlinear/llm_chat_backend.py`;
override `--toolkit-root` for another checkout. Credentials are supplied through
`DEEPSEEK_API_KEY` or an owner-only `DEEPSEEK_API_KEY_FILE`, never tracked.

```bash
python scripts/polished_translation.py prepare
python -m unittest discover -s scripts -p test_polished_translation.py
bash scripts/start_polished_translation_tmux.sh --pilot-only
python scripts/polished_translation.py status
# After reviewing the two pilot PDFs:
python scripts/polished_translation.py approve-pilot --evidence 'Review findings'
bash scripts/start_polished_translation_tmux.sh --publish
```

One tmux session: `susskind-polished-translations`. At most five simultaneous
requests, staggered one second apart; books advance sequentially, not in parallel.
Compile jobs are serial. `touch .translation-work/STOP` stops at the next book
boundary. Remove that marker to resume. Accepted caches survive interruptions.
Check `.translation-work/status.json` and `queue.log` before restarting.
Per-book failures and publication state are retained under
`.translation-work/book-state/`. Final queue state distinguishes `complete`,
`finished_with_blockers`, `provider_blocked`, and user-requested `paused`.
An interrupted request with a saved valid response is recovered without a new
API call. Malformed or missing responses still consume the finite content
attempt budget; transport failures refund it because they produced no content.
Transient connection, timeout, rate-limit or server failures may resume the
queue twice after five- and ten-minute cooldowns. No calls run during the wait;
STOP is checked every five seconds. Authentication/payment failures stop for
owner attention, never automatic charging or endless credit checks. Override
with `--transport-resumes` and `--transport-retry-seconds`.

## Validation Repairs

Number-word validation recognizes zero through ninety-nine (including compound
forms), first through twelfth, single occurrences, common fractions, and
mathematical unity/unit magnitude. It also recognizes "once", ordinal centuries
through twentieth, and spelled-out fractions such as "two-thirds".
Large spelled-out quantities and shared ranges such as "ten to twelve billion"
are compared to their values in target notation (`100億` to `120億`), not just
the visible digits. Unit names such as `千克` retain their coefficient rather
than being mistaken for a numeric multiplier. Wrong magnitudes still fail.
Japanese denominator-first fractions such as
`4分の1` are compared as rational values; penny/dime denominations are recognized
when those exact source words occur. It still
rejects unsupported new quantities. Immutable accented names and nonbreaking
reference glue may follow natural target-language word order. Math can pass
around a complete emphasis group, but not into or out of its braces. Duplicate
tokens, missing figures, structural movement, and changed equations still fail.

Use `repair --repairs PATH.json` for reviewed corrections. The packet records
the book ID and per-row language, source file, segment ID, source hash, complete
restored source, masked translation, and review reason. The tool validates the
entire packet first, backs up changed caches, and schedules every repair for
additional semantic review. Replacing already accepted text also requires its
`previous_sha256`. No full-chapter regeneration is required.

On 2026-10-12, ten Advanced Quantum Mechanics segments were checked against the
English source. Most failures were overly restrictive numerical/order checks;
one Chinese paragraph repeated a Hamiltonian token and was rewritten to use it
once. Unsupported numeric paraphrases were corrected without loosening the
global preservation checks. Balance was not the blocker.

The subsequent PDF gate caught two U+FFFD replacement characters in otherwise
intact words. Both were checked against the source and repaired; the segment
validator now rejects corrupt Unicode/control characters before compilation.
Front matter is included in semantic review, and ordinary English wording must
be translated even when nearby proper names remain Latin. These repairs do not
change any frozen equation or original image.

Semantic review now runs before the expensive PDF passes. The `review --book ID
--language ja` command reruns only changed review batches without compiling.
Already validated language editions are skipped when the other language needs
repair. Source-checked false positives can be explicitly adjudicated under
`.translation-work/review-decisions/`: each dismissal is tied to the exact
source/translation sample hash and exact issue hash, with a written reason.
The original report is retained, and the published quality record includes the
decisions. A changed sample or new issue cannot inherit a dismissal. There is
no blanket reviewer bypass or automatic acceptance of model corrections.

Visual TOC inspection also caught translated words placed after a heading's
closing braces. The parser now protects adjacent argument endings separately,
allowing natural Japanese/Chinese suffixes *inside* a title. Existing caches
are migrated without changing their restored TeX or making translation calls;
invalid entries are not silently retained. Whole-heading AST checks reject
text outside its argument, and stray placeholder characters fail validation.
Corrections mark the affected PDF as needing a rebuild. New quality records
also bind availability to accepted-translation hashes, not only PDF/TeX hashes.

Malformed JSON responses are archived and retried once at the transport level;
invalid cached review replies cannot permanently poison a resume. No accepted
translation is discarded by that retry.

### Review Model Qualification

Translation remains on `deepseek-chat`; semantic review uses the independently
tested `deepseek-reasoner` route (`--review-model` overrides it). The basic chat
reviewer repeatedly called equivalent translations errors, and once suggested
reversing an operator product that was copied faithfully. In a six-case pilot,
the reasoning route correctly accepted all five faithful passages and rejected
a deliberately reversed electric-charge statement. This is pilot evidence,
not a guarantee. Review caches include the model identity, so a model change
cannot silently reuse a weaker review. No Codex translation workers were added.

## Verified Checkpoint: 2026-10-12

Advanced Quantum Mechanics is complete in both standalone languages:

| Check | Japanese | Chinese |
| --- | ---: | ---: |
| Accepted segments | 840/840 | 840/840 |
| PDF pages | 142 | 128 |
| Outline entries | 130 | 130 |
| Image placements, including cover | 30 | 30 |
| Displayed equation environments retained | 501 | 501 |
| Inline math fragments retained | 1,147 | 1,147 |
| Chapter figure commands retained | 29 | 29 |
| Reasoning-model semantic sample | 56 pairs | 38 pairs |
| Overflow / missing glyph / out-of-page text | 0 | 0 |

The final reasoning reviews passed with no issues and no manual dismissals.
Cover, contents and figure pages were visually inspected, including the repaired
math-bearing title. The final books were pushed in `50b47822`. All 16 original
English source sets were verified unchanged. This is sampled semantic evidence,
not a claim of exhaustive error-free translation. The next Quantum Entanglement
book resumes from its cached segments; remaining books still require generation
and all finalization gates.

### Part 3 Recovery And Queue Hardening

Eight source-checked passages in Quantum Entanglement Part 3 were recovered on
2026-10-12. Ordinal/fraction representations were validator false positives;
indefinite unit expressions were translated naturally without introducing
digits. One Chinese paragraph duplicated its frozen electric/magnetic-field
tokens: the prose was corrected to keep each expression exactly once. All eight
are included in the next semantic review.

The controller now drains every chapter, records all failures, finalizes each
complete language independently, and advances to later books. It never exports
an incomplete language or labels a skipped book complete. Repairs cannot change
frozen TeX or equations, and prior accepted wording is retained in the local
repair history. Deterministic publication/compile failures remain explicit
blockers; no agent is authorized to weaken checks or rewrite pipeline code.

Readme status is generated deterministically. `--publish` makes a scoped commit
and pushes each validated pair of PDFs. It refuses a pre-existing staged index,
README edits outside the generated block, or files over 95 MiB. A publication
failure is recorded in `.translation-work/publication.json` without discarding
accepted translations or stopping the next book. No inference prompts, keys or
private logs are committed. Without `--publish`, all work remains local.

Parser reference: [pylatexenc LatexWalker](https://pylatexenc.readthedocs.io/en/v2.10/latexwalker/).
