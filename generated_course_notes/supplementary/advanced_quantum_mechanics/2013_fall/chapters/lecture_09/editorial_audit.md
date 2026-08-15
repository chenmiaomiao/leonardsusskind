# Editorial Audit: Lecture 9

**Status:** Pass

The revised chapter preserves all 38 substantive lecture beats, 23 verified classroom exchanges, and the argument-bearing blackboard mathematics. It follows the lecture from local nonrelativistic field Hamiltonians and momentum-conserving interactions through decay, exchange, self-energy, and diagrammatic reasoning, then develops the one-dimensional Dirac equation from relativistic dispersion and two chiral components. It ends with negative energies and the (3+1)-dimensional extension explicitly unresolved, exactly where the lecture leaves them.

## Coverage

- All 38 mapped lecture beats are present in chronological order.
- All 23 published Q&A blocks have direct transcript support and ordered timestamps.
- The Fourier-delta, kinetic-energy, contact-interaction, Hermiticity, exchange, self-energy, Klein--Gordon, chiral-wave, and Dirac-algebra arguments retain their intermediate mathematics.
- The static-field, Aharonov--Bohm, Coulomb-limit, coupling, symmetry, atomic-speed, and Lorentz-direction discussions are retained with narrow factual clarifications.
- No substantive topic, example, caveat, useful repetition, or classroom exchange is omitted.

## Figures

| Asset | Time | Decision | Reason |
| --- | --- | --- | --- |
| `lecture_09_frame_01.png` | 00:02:47 | reference only | The lecturer blocks the center and the left edge clips the Hamiltonian; the complete expression is typeset. |
| `lecture_09_frame_02.png` | 00:35:36 | keep | The four-field contact term and meeting-point spacetime sketch match the local scattering discussion; an adjacent TikZ reconstruction removes the occlusion. |
| `lecture_09_frame_03.png` | 01:26:00 | keep | H equals alpha P and the two-component derivative equation are legible during the massless left-right construction. |
| `lecture_09_frame_04.png` | 01:32:02 | reference only | The lecturer obscures the anticommutator while it is being completed; the verified matrix algebra is typeset. |
| `lecture_09_frame_05.png` | 00:48:56 | keep | Both orientations of the A to B plus C vertex are visible and synchronized with the second-order argument. |
| `lecture_09_frame_06.png` | 00:51:22 | keep | The two-vertex exchange process and internal C line are visible; an adjacent TikZ reconstruction makes the topology unambiguous. |
| `lecture_09_frame_07.png` | 01:10:30 | keep | The nonrelativistic and relativistic dispersion relations and c equals one are complete and mark the lecture's pivot. |
| `lecture_09_frame_08.png` | 01:37:44 | keep | Both coupled component equations are complete and the lecturer does not cover the derivative or mass terms. |

## Validation

- Video2Book hard-scan, fidelity, and TeX-structure gates pass without findings.
- The chapter compiles in two `pdflatex` passes to a 19-page letter-size PDF.
- The final log has no warnings, unresolved references, missing figures, or overfull/underfull boxes.
- The title matter states provenance explicitly; the lecture body contains no workflow, prompt, or conversation leakage.
- Every rendered page and all six retained blackboard frames were visually inspected after the final compile.
- Final PDF SHA-256: `9b950f2482e8386ba4db6ff4a878ba18590945b206a67b399fd9bffbb9090aaa`.

