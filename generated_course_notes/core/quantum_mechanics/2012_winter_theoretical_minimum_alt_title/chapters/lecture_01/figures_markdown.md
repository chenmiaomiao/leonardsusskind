# Figure Notes

## Verified Image Inventory

| Asset | Time | Blackboard content | Use in chapter |
| --- | --- | --- | --- |
| `lecture_01_figure_02.png` | 00:22:44 | Heads/tails, `\sigma=\pm1`, and up/down arrows | Establish the three labels for the two measured states. |
| `lecture_01_figure_03.png` | 00:36:21 | Prepared up arrow, upright analyzer, and sideways analyzer | Preserve the experimental setup; use the clean TikZ diagram for the corrected geometry. |
| `lecture_01_figure_04.png` | 00:48:55 | Prepared vertical ensemble, tilted analyzer, and angle `\theta` | Anchor the arbitrary-angle experiment and cosine mean. |
| `lecture_01_figure_05.png` | 01:14:28 | Addition and complex scalar multiplication of two-component columns | Support the first concrete vector-space model. |
| `lecture_01_figure_06.png` | 01:23:15 | Ket-to-bra correspondence for sums and complex scalar multiples | Support antilinearity of the dual map. |
| `lecture_01_figure_07.png` | 01:31:25 | Row-times-column inner product | Support `\langle\beta|\alpha\rangle=\beta_1^*\alpha_1+\beta_2^*\alpha_2`. |
| `lecture_01_figure_08.png` | 01:34:40 | Self-inner-product as a sum of component magnitudes | Support positivity and the squared norm. |
| `lecture_01_figure_09.png` | 01:39:50 | Columns `(1,0)^{\mathsf T}` and `(0,1)^{\mathsf T}` labeled orthogonal | Support the standard orthogonal basis and dimension discussion. |

## Equation Reading

- Frame 02 visibly establishes `\sigma=1\leftrightarrow\uparrow` and `\sigma=-1\leftrightarrow\downarrow`; the heads/tails equivalence is completed from the surrounding narration.
- Frame 03 is geometric rather than algebraic. The exact chalk-arrow directions are not copied because an audience correction occurs during the live drawing.
- Frame 04 supports the geometry of a relative angle `\theta`; the mean `\langle\sigma\rangle_\theta=\cos\theta` comes from the narration rather than a fully legible formula in this frame.
- Frame 05 visibly supports
  \[
  \begin{pmatrix}\alpha_1\\\alpha_2\end{pmatrix}
  +
  \begin{pmatrix}\beta_1\\\beta_2\end{pmatrix}
  =
  \begin{pmatrix}\alpha_1+\beta_1\\\alpha_2+\beta_2\end{pmatrix},
  \qquad
  z\begin{pmatrix}\alpha_1\\\alpha_2\end{pmatrix}
  =
  \begin{pmatrix}z\alpha_1\\z\alpha_2\end{pmatrix}.
  \]
- Frame 06 supports the additive ket-to-bra rule and the conjugation of a complex scalar, written cleanly as `\langle zA|=z^*\langle A|`.
- Frame 07 supports `\langle\beta|\alpha\rangle=\beta_1^*\alpha_1+\beta_2^*\alpha_2`.
- Frame 08 supports `\langle\alpha|\alpha\rangle=|\alpha_1|^2+|\alpha_2|^2`.
- Frame 09 supports `\langle e_1|e_2\rangle=0` for the two standard columns.

## Reconstruction Decisions

- Every listed screenshot remains in the final notes as lecture evidence.
- The analyzer experiment also receives a TikZ reconstruction because the live board is spatially useful but contains corrected arrows.
- Blackboard notation is normalized in displayed LaTeX; normalization never replaces the source frame.
- No Pauli matrices or named spin basis kets are imported into this first lecture.
- The half-angle probabilities are not attributed to a board frame. They are explicitly labeled as an editorial algebraic consequence of the transcript's two outcomes and cosine mean.

## Caption Set

- Frame 02: Qubit labels `\sigma=\pm1` and up/down notation.
- Frame 03: Prepared up state with upright and sideways analyzers.
- Frame 04: A prepared ensemble measured along an axis tilted by `\theta`.
- Frame 05: Component rules for two-component complex columns.
- Frame 06: Antilinear ket-to-bra correspondence.
- Frame 07: Two-component Hermitian inner product.
- Frame 08: Self-inner-product and squared norm.
- Frame 09: Standard orthogonal basis columns.

## Uncertainties

- In frame 02, the lower `\sigma=-1` label is partly occluded; the board layout and transcript jointly establish it.
- In frame 03, the orientation cue above the apparatus is cropped, and the live arrows are later corrected. The chapter therefore relies on the experiment's spoken logic for the redraw.
- In frame 05, the short note identifying complex entries is blurred; the safe normalized statement is `\alpha_i,\beta_i,z\in\mathbb C`.
- Frames 06--09 were selected after the corresponding expressions were complete and the lecturer no longer blocked their essential terms.
