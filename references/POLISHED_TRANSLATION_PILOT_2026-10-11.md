# Polished Translation Pilot - 2026-10-11

Source: the accepted final `supplementary/higgs_boson/2012_summer` edition.
English source files remain unchanged. The Japanese and Simplified Chinese
translations each cover 97/97 prepared text segments, including front matter,
headings, introductions, captions, classroom questions and answers.

| Edition | Pages | PDF outline entries | Images | Overflows | Missing glyphs |
| --- | ---: | ---: | ---: | ---: | ---: |
| Japanese | 20 | 18 | 13 lecture figures + cover | 0 | 0 |
| Simplified Chinese | 18 | 18 | 13 lecture figures + cover | 0 | 0 |

The source layout and cover illustration are retained. Cover and section titles,
captions, and explanatory prose are translated. English writing in original board
images and text inside frozen mathematical displays remains as in the source.

## Fixes Learned

- Supply a read-only legend for immutable TeX/math tokens, so the translator can
  understand formulas, reference values, formatting boundaries and years.
- Accept verified number-word equivalents such as `six` / `6` and `one and a
  half` / `1.5`, rather than retrying correct paragraphs.
- Protect an accented name as a complete lexical unit. Do not put an immutable
  accent macro between translated syllables.
- Preserve every token, even punctuation/formatting markers. Retry only rejected
  paragraphs, keeping the accepted work.
- Date expressions need Japanese `年に` and Chinese `年`, not a mechanical
  translation of the English preposition `in`.
- The distant charged plates are outside the observer's view; they are not
  described as being unable to see each other. This sentence was manually
  corrected in both versions against the English source.
- Use a prose-only Unicode fallback for Greek letters such as mu and tau.
  Do not activate all Greek characters globally, which interferes with microtype.
- Semantic reviewers must report actual errors with evidence, not put statements
  that a translation is correct into a failing issue list.

## Verification Scope

Eleven unit tests cover lossless math/path preservation, introductions, captions,
questions, unsafe output rejection, accented names, numerals, segment-only retries,
resumption, source mutation, and CJK preamble adaptation. Preparation also verified
lossless reconstruction of all 145 selected final chapters and course wrappers.

Both pilot editions pass three-pass XeLaTeX builds and sampled semantic review.
Visual review covered the cover, front matter, TOC, opening text, equations,
figure/caption pages, and ending. This is not a claim that every translated
sentence in the book has undergone expert human review.

Runtime evidence, usage records and rendered page PNGs are kept privately in
`.translation-work/`. Public per-edition `quality.json` files record hashes and
checks. Fifteen remaining books advance one by one only after pilot approval,
with at most five simultaneous DeepSeek requests.
