# Editorial Audit: Lecture 7

**Status:** Pass

The revised chapter preserves all 22 substantive lecture beats, 21 verified classroom exchanges, and the argument-bearing blackboard mathematics. It follows the lecture from one-particle quantum mechanics into the simplest nonrelativistic quantum field, retains the answer-first Hamiltonian derivation, and ends with the stated preview of decay and scattering rather than an invented summary.

## Coverage

- All 22 mapped lecture beats are present in chronological order.
- All 21 published Q&A blocks have direct transcript support and ordered timestamps.
- The number-density, field-Hamiltonian, local-energy-density, and momentum derivations retain their intermediate algebra.
- The beta-decay example, relativistic localization caveat, electromagnetic aside, operator-ordering discussion, and Dirac-notation anecdote are preserved with narrow factual clarifications where needed.
- No substantive topic, example, caveat, useful repetition, or classroom exchange is omitted.

## Figures

| Asset | Time | Decision | Reason |
| --- | --- | --- | --- |
| `lecture_07_frame_01.png` | 00:08:25 | keep | The box modes match the node-count discussion; the adjacent TikZ reconstruction resolves partial lecturer occlusion. |
| `lecture_07_frame_02.png` | 00:54:10 | keep | The one-particle Schrodinger equation, momentum representation, and Laplacian form are complete and legible. |
| `lecture_07_frame_03.png` | 01:05:34 | keep | The replacement frame is synchronized with the local-energy discussion and shows the field Hamiltonian more clearly than the rejected 01:09:47 frame. |

## Validation

- Video2Book hard-scan, fidelity, and TeX-structure gates pass without findings.
- The chapter compiles in two `pdflatex` passes to a 16-page letter-size PDF.
- The final log has no warnings, unresolved references, missing figures, or overfull/underfull boxes.
- The title matter states provenance explicitly; the lecture body contains no workflow, prompt, or conversation leakage.
- Equation, figure, Q&A, field-Hamiltonian, and late-lecture pages were visually inspected after the final sequencing pass.
- Final PDF SHA-256: `170fea3cd583f5b6918ad83ae636040146dc8d58c70cf4bf385e9dde8617b080`.
