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
4. Cache valid segments, retry only invalid segments once, and stop on unresolved
   failures. API transport errors have three bounded attempts. There is no
   perpetual quota retry loop or hidden Codex reviewer fleet.
5. Reassemble real TeX, retaining source figure assets and the accepted layout.
   Use XeLaTeX with Noto CJK fonts. Original blackboard writing and English labels
   inside frozen mathematical displays are intentionally retained, not redrawn.
6. Build three passes; require a nonempty PDF and outline, CJK text, no missing
   glyphs, unresolved references or overfull boxes. Run a sampled semantic audit
   covering opening and technical paragraphs from each chapter plus repaired or
   reordered rows, in bounded ten-pair review batches. Unresolved issues
   stop the queue and do not create an available download.
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

## Validation Repairs

Number-word validation recognizes zero through ninety-nine (including compound
forms), common fractions, and mathematical unity/unit magnitude. It still
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

Readme status is generated deterministically. `--publish` makes a scoped commit
and pushes each validated pair of PDFs. It refuses a pre-existing staged index,
README edits outside the generated block, or files over 95 MiB. A publication
failure is recorded in `.translation-work/publication.json` without discarding
accepted translations or stopping the next book. No inference prompts, keys or
private logs are committed. Without `--publish`, all work remains local.

Parser reference: [pylatexenc LatexWalker](https://pylatexenc.readthedocs.io/en/v2.10/latexwalker/).
