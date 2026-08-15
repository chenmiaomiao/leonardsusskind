# Editorial Audit: Lecture 1

**Status:** Pass

The revised chapter follows the full 01:35:34 source in chronological order, from the limits of evolved intuition through classical information, reversible update laws, coarse-graining, and the matrix algebra prepared for qubits. It retains all 27 substantive beats and 11 physics or mathematics classroom exchanges. Administrative banter is not promoted into exposition.

## Coverage

- The bit count, logarithmic information measure, finite-precision encoding, lattice-field encoding, and occupancy-bit construction are present.
- Configuration space is distinguished from physical space, and dynamics is built from explicit update rules.
- Reversibility, time-reversal symmetry, deterministic branching, coarse-graining, the gas example, black-hole information, and the quantum preview of unitarity remain distinct.
- Row and column vectors, the inner product, matrix action, one-hot states, the corrected cyclic permutation, repeated updating, matrix products, left action, and invertibility are derived in sequence.
- The spoken \(10^{100}\) slip is corrected to \(2^{100}\) with a narrow editorial footnote; the live five-to-four-state matrix correction is explained rather than silently hidden.

## Figures

| Asset | Time | Decision | Reason |
| --- | --- | --- | --- |
| lecture_01_figure_02.png | 00:53:21 | keep | The reversible cycles, merging pattern, and handwritten unitarity label are simultaneously visible. |
| lecture_01_figure_03.png | 01:03:05 | replace/keep | A new direct frame clearly shows the same components as a row and column. |
| lecture_01_figure_04.png | 01:12:45 | replace/keep | A new direct frame shows the matrix, input column, and expanded output together. |
| lecture_01_figure_05.png | 01:26:30 | replace/keep | The marked row and columns support the matrix-product rule; exact entries are typeset. |

The Stanford title card is deliberately excluded.

## Validation

- Video2Book hard-scan and TeX-structure checks pass.
- The standalone chapter compiles in two pdflatex passes to a 15-page letter-size PDF.
- The final log has no unresolved references, missing figures, overfull boxes, or underfull boxes.
- All 15 rendered pages and all four retained frames were visually inspected.
- The body contains no prompt, workflow, conversation, or false-authorship language.
- Final PDF SHA-256: 7943714a4405ce9e175b94c071b6ede533209755220ee5fc957a6c29c58e2113.
