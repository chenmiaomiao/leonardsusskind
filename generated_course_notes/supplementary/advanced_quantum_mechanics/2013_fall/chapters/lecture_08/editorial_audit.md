# Editorial Audit: Lecture 8

**Status:** Pass

The revised chapter preserves all 26 substantive lecture beats, 23 verified classroom exchanges, and the argument-bearing blackboard mathematics. It follows the lecture from two-state tunneling and neutrino oscillation through discrete symmetries and the electron electric-dipole search, then returns after the break to continuum fields, locality, EPR correlations, and the fermionic preview. It ends where the lecture ends rather than imposing a synthetic summary.

## Coverage

- All 26 mapped lecture beats are present in chronological order.
- All 23 published Q&A blocks have direct transcript support and ordered timestamps.
- The double-well transfer, spin-precession, parity/time-reversal, Fourier-transform, field-commutator, and fermionic-anticommutator arguments retain their intermediate mathematics.
- The ammonia, solar-neutrino, quantum-dumbbell, electron-shape, EDM-search, fixed-magnetic-field, and EPR discussions are retained with narrow factual clarifications.
- No substantive topic, example, caveat, useful repetition, or classroom exchange is omitted.

## Figures

| Asset | Time | Decision | Reason |
| --- | --- | --- | --- |
| `lecture_08_frame_01.png` | 00:05:55 | reference only | The lecturer obscures the localized-state sketch; its reliable content is reconstructed in TikZ. |
| `lecture_08_frame_02.png` | 00:06:19 | keep | The symmetric tunneling tail and double-well potential match the parity-eigenstate discussion. |
| `lecture_08_frame_03.png` | 00:11:24 | reject | The energy-level region is washed out and partly blocked; a clean reconstruction carries the content. |
| `lecture_08_frame_04.png` | 00:11:36 | reference only | The lower normalized combination is incomplete, so verified equations are typeset instead. |
| `lecture_08_frame_05.png` | 00:17:52 | keep | The relative phases and complete-transfer condition are legible and synchronized. |
| `lecture_08_frame_06.png` | 01:06:10 | keep | The paired time-reversal sketches support the adjacent EDM reconstruction. |
| `lecture_08_frame_07.png` | 01:20:00 | keep | Both directions of the one-particle Fourier transform are complete and unobstructed. |
| `lecture_08_frame_08.png` | 01:31:00 | keep | The mode and local field commutators appear together during the delta-function argument. |

## Validation

- Video2Book hard-scan, fidelity, and TeX-structure gates pass without findings.
- The chapter compiles in two `pdflatex` passes to a 20-page letter-size PDF.
- The final log has no warnings, unresolved references, missing figures, or overfull/underfull boxes.
- The title matter states provenance explicitly; the lecture body contains no workflow, prompt, or conversation leakage.
- Equation, figure, Q&A, symmetry, Fourier-transform, locality, and closing pages were visually inspected after the final sequencing pass.
- Final PDF SHA-256: `49f0389ec324b74e2d45a2010f27c8492632f82f9ab89ba77b62c3f9c80910af`.
