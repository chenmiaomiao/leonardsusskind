# Figure Notes
## Image Inventory
- `lecture_08_figure_01.png`: Stanford University opening title card with the block `S` and tree logo on a dark background. No lecturer, board, or mathematical content is present.
- `lecture_08_figure_02.png`: Susskind stands beside a mostly blank white board. Near the upper left of the board there is only a tiny three-armed or Y-shaped sketch, with no legible algebra around it.
- `lecture_08_figure_03.png`: Tight board crop of a matrix computation. Susskind is writing the left matrix, while the middle matrix with all entries `1/2` is already visible; an equals sign and the beginning of a result matrix appear to the right.
- `lecture_08_figure_04.png`: Board view with a stacked block of bra-ket equations. Susskind points near a lower line; the board preserves the layout of a ket evolution line, a bra evolution line, and a lower inner-product expression.
- `lecture_08_figure_05.png`: Board view with two key lines: an energy-eigenvalue equation on top and, below it, a time-evolution statement in which the state at time `t` is proportional to the initial state. Susskind points to the scalar factor on the right-hand side.

## Blackboard Equations
- `lecture_08_figure_01.png`: No blackboard equation content; title card only.

- `lecture_08_figure_02.png`: No reliable equation is legible; only a tiny branching sketch is present.

- `lecture_08_figure_03.png`: `\begin{pmatrix}\tfrac12 & \tfrac12 \\[2pt] \tfrac12 & \tfrac12\end{pmatrix}` [visible]
- `lecture_08_figure_03.png`: `\begin{pmatrix}0 & 1 \\[2pt] 1 & 0\end{pmatrix}` [partially visible]
- `lecture_08_figure_03.png`: `\sigma_1=\begin{pmatrix}0 & 1 \\[2pt] 1 & 0\end{pmatrix}` [standard reconstruction]
- `lecture_08_figure_03.png`: `\begin{pmatrix}0 & 1 \\[2pt] 1 & 0\end{pmatrix}\begin{pmatrix}\tfrac12 & \tfrac12 \\[2pt] \tfrac12 & \tfrac12\end{pmatrix}` [standard reconstruction]

- `lecture_08_figure_04.png`: `|\psi(t)\rangle = U(t)|\psi(0)\rangle` [partially visible]
- `lecture_08_figure_04.png`: `\langle \phi(t)| = \langle \phi(0)|U^\dagger(t)` [partially visible]
- `lecture_08_figure_04.png`: `\langle \phi(t)|\psi(t)\rangle = \langle \phi(0)|U^\dagger(t)U(t)|\psi(0)\rangle` [standard reconstruction]
- `lecture_08_figure_04.png`: `U^\dagger U = I` [standard reconstruction]

- `lecture_08_figure_05.png`: `H|\psi\rangle = E|\psi\rangle` [visible]
- `lecture_08_figure_05.png`: `|\psi(t)\rangle = (\text{scalar function of }t)\,|\psi(0)\rangle` [partially visible]
- `lecture_08_figure_05.png`: `|\psi(t)\rangle = f(t)|\psi(0)\rangle` [standard reconstruction]

## Diagram And Layout Reading
- `lecture_08_figure_01.png` is not a lecture-board frame at all. It is purely an intro slate and has no note-taking value beyond documenting the video source.
- `lecture_08_figure_02.png` preserves only a tiny three-pronged sketch near the upper left corner of a blank board. It does not carry enough labels or surrounding structure to function as a trustworthy mathematical figure.
- `lecture_08_figure_03.png` is organized as a compact algebra block: left matrix being written, central density-matrix-like block already complete, and the start of the product result on the right. The useful visual point is the board sequence of matrix multiplication rather than the final answer.
- `lecture_08_figure_04.png` preserves a vertical derivation layout: time-evolved ket on top, corresponding bra beneath it, and then a lower line where the evolved inner product is written in terms of the initial vectors and the operator product. The board rhetoric is more important here than any single cropped symbol.
- `lecture_08_figure_05.png` has a clean two-line structure. The top line states the energy-eigenvector condition; the lower line expresses the idea that if the initial state is an energy eigenvector, then the later state remains along the same vector up to a time-dependent scalar factor.

## TeX Reconstruction Plan
- `lecture_08_figure_01.png` should not remain visible in the notes. It is a title card, not lecture evidence.
- `lecture_08_figure_02.png` is too weak to carry mathematical weight. It is best omitted from the final notes. If an editor insists on preserving it as atmosphere or board-layout evidence, it should be paired only with a tiny neutral TikZ redraw of the three-branch sketch and no mathematical claims should rest on it.
- `lecture_08_figure_03.png` should remain visible near the discussion of `\sigma_1` acting on the reduced density matrix. The notes should typeset the clean matrix product and, if needed, the resulting trace computation nearby; the screenshot should serve as board evidence for the multiplication setup.
- `lecture_08_figure_04.png` should remain visible near the derivation of unitarity from time-independent inner products. Nearby LaTeX should reconstruct the ket evolution, the bra evolution, the evolved inner product, and the conclusion `U^\dagger U = I`.
- `lecture_08_figure_05.png` should remain visible near the energy-eigenstate discussion. Nearby LaTeX should reconstruct `H|\psi\rangle = E|\psi\rangle` and the ansatz `|\psi(t)\rangle = f(t)|\psi(0)\rangle`, with the subsequent exponential phase solution derived in clean display math.
- No screenshot here calls for a substantial geometric TikZ figure apart from the optional tiny redraw for `lecture_08_figure_02.png`; the mathematically important figures are equation screenshots, not spatial diagrams.

## Caption Drafts
- `lecture_08_figure_01.png`: Stanford title card
- `lecture_08_figure_02.png`: Small branching sketch on the board
- `lecture_08_figure_03.png`: `\sigma_1` acting on the reduced density matrix
- `lecture_08_figure_04.png`: Bra-ket form of the unitarity argument
- `lecture_08_figure_05.png`: Energy eigenstate and scalar time evolution

## Uncertainties
- `lecture_08_figure_02.png`: The tiny sketch has no reliable labels, and its connection to the spoken density-matrix discussion is visually weak. It should not be overinterpreted.
- `lecture_08_figure_03.png`: The left matrix is still being written and is partially blocked by Susskind; the right-hand result matrix is cropped. The transcript is needed to regularize this as the `\sigma_1` multiplication.
- `lecture_08_figure_04.png`: Several left edges are cropped, and the lower line is only partially readable. The full inner-product equation should therefore be reconstructed from the transcript rather than transcribed verbatim from the frame.
- `lecture_08_figure_05.png`: The scalar multiplying `|\psi(0)\rangle` is not fully legible from the frame alone. The transcript supports reading it as a generic time-dependent function, later solved as an exponential phase.
- Across the algebraic frames, the board often shows only part of a derivation block. Clean note equations should therefore do the mathematical work, with the screenshots kept as local evidence of order, emphasis, and board sequencing.

## Editorially Verified Additions

- lecture_08_figure_06.png at 00:09:32: pure-state density matrix acting as a projector.
- lecture_08_figure_07.png at 00:14:25: trace formula reduced to a pure-state expectation value.
- lecture_08_figure_08.png at 00:21:08: entropy definition and the equal-probability value S = log n.
- lecture_08_figure_09.png at 00:33:50: sum over subsystem B leaving the reduced density matrix in A.
- lecture_08_figure_10.png at 00:46:35: product-state factorization and normalization of the B factor.
- lecture_08_figure_11.png at 00:55:35: all four single-spin density-matrix entries for the singlet.
- lecture_08_figure_12.png at 01:11:40: reversible classical evolution as arrows among discrete states.
- lecture_08_figure_13.png at 01:19:00: linear quantum evolution from the initial state.
- lecture_08_figure_14.png at 01:29:35: first-order unitarity and Hermiticity of the generator.
- lecture_08_figure_15.png at 01:32:18: the difference quotient leading to the general Schrodinger equation.
- lecture_08_figure_16.png at 01:46:10: energy-eigenstate phase evolution and E = hbar omega.

The added frames were inspected against their local transcript windows. Figures 01 and 02 remain excluded from the chapter because the first is a title card and the second contains no reliably interpretable mathematical content.
