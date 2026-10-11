# Final Polished Japanese and Chinese Editions

This queue translates the **accepted editorial TeX**, never `draft.tex`, OCR,
legacy unpolished PDFs, or the earlier duplicate lecture runs. It includes the
15-course editorial queue and its completed eight-chapter Cosmology pilot:
16 books, 145 chapters, Japanese and Simplified Chinese editions.

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
4. Cache valid segments, retry only invalid segments once, and stop on unresolved
   failures. API transport errors have three bounded attempts. There is no
   perpetual quota retry loop or hidden Codex reviewer fleet.
5. Reassemble real TeX, retaining source figure assets and the accepted layout.
   Use XeLaTeX with Noto CJK fonts. Original blackboard writing and English labels
   inside frozen mathematical displays are intentionally retained, not redrawn.
6. Build three passes; require a nonempty PDF and outline, CJK text, no missing
   glyphs, unresolved references or overfull boxes. Run a sampled semantic audit
   covering opening and technical paragraphs from each chapter. Unresolved issues
   stop the queue and do not create an available download.
7. Update the README availability table, with PDF links only for validated output.

No source English file is overwritten. Per-language output is under
`translations/<course-id>/{ja,zh}/`; intermediate requests, caches, usage logs,
build artifacts and queue state are under ignored `.translation-work/`.
Original figure directories are referenced by relative TeX paths, not duplicated.

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

Readme status is generated deterministically. `--publish` makes a scoped commit
and pushes each validated pair of PDFs. It refuses a pre-existing staged index,
README edits outside the generated block, or files over 95 MiB. A publication
failure is recorded in `.translation-work/publication.json` without discarding
accepted translations or stopping the next book. No inference prompts, keys or
private logs are committed. Without `--publish`, all work remains local.

Parser reference: [pylatexenc LatexWalker](https://pylatexenc.readthedocs.io/en/v2.10/latexwalker/).
