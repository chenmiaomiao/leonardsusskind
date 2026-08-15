# Figure Notes
## Image Inventory
- `lecture_07_figure_02.png`: Susskind stands between two boards, pointing with his left hand at the left-board equation block while beginning to write on the blank right board. The visible mathematics on the left board consists of a short top line ending in a superposition of slit states and two lower lines giving expansions with $\psi$ and $\phi$ coefficients in a screen basis.
- `lecture_07_figure_03.png`: A right-board equation frame. The top line shows the summed screen-state expansion after both paths contribute, and the line below expands the probability at a fixed site into four terms. Susskind stands clear enough that the main equations are readable.
- `lecture_07_figure_04.png`: A close crop of the board showing the projector at fixed screen site $m$ with two spin sectors. The equation is centered on the dyadic sum, while the upper line only preserves a fragment of an earlier $\phi$-expansion.
- `lecture_07_figure_05.png`: A mostly diagrammatic board moment. Near the upper board there is a sparse symmetric sketch with two slanted branches and a marked point above them, while a lower circled algebraic expression from the previous discussion remains on the board but is not the main content.
- `lecture_07_figure_06.png`: Susskind stands in front of the board during the transition to density matrices. On the right board a ket-state expression points by an arrow into a large circled region containing several small marks, suggesting an ensemble or many-state schematic rather than a finished matrix formula.

## Blackboard Equations
- `lecture_07_figure_02.png`: $|A\rangle + |B\rangle$ [visible]
- `lecture_07_figure_02.png`: $\sum_m \psi_m |m\rangle$ [partially visible]
- `lecture_07_figure_02.png`: $\sum_m \phi_m |m\rangle$ [partially visible]
- `lecture_07_figure_02.png`: $|A\rangle \to \sum_m \psi_m |m\rangle,\qquad |B\rangle \to \sum_m \phi_m |m\rangle$ [standard reconstruction]

- `lecture_07_figure_03.png`: $\sum_n (\psi_n+\phi_n)\,|n\rangle$ [partially visible]
- `lecture_07_figure_03.png`: $P_m=\psi_m^*\psi_m+\phi_m^*\phi_m+\psi_m^*\phi_m+\phi_m^*\psi_m$ [visible]
- `lecture_07_figure_03.png`: $P_m=|\psi_m+\phi_m|^2$ [standard reconstruction]

- `lecture_07_figure_04.png`: $|m,u\rangle\langle m,u|+|m,d\rangle\langle m,d|$ [partially visible]
- `lecture_07_figure_04.png`: $\Pi_m=|m,u\rangle\langle m,u|+|m,d\rangle\langle m,d|$ [standard reconstruction]
- `lecture_07_figure_04.png`: $\sum_n \phi_n |n\rangle$ [partially visible]

- `lecture_07_figure_05.png`: $A,\ B$ [partially visible]
- `lecture_07_figure_05.png`: No reliable stand-alone equation is legible; the useful content is primarily diagrammatic. [standard reconstruction]

- `lecture_07_figure_06.png`: $|\cdot\rangle \to \cdots$ [partially visible]
- `lecture_07_figure_06.png`: No reliable density-matrix formula is yet legible in the frame; the visual content is schematic rather than algebraic. [standard reconstruction]

## Diagram And Layout Reading
- `lecture_07_figure_02.png` is mainly a board-layout witness. The equations are arranged as a short superposition line above two path-to-screen expansions. Susskind’s pointing gesture identifies the $\psi$-coefficient line as the relevant line for “the amplitude at $m$.”
- `lecture_07_figure_03.png` is a compact derivation block. The top line gives the state after both slit contributions are added; the lower line is the expanded probability at a fixed screen site. This frame is useful because it preserves the lecture’s top-to-bottom logic: first amplitudes add, then probabilities are formed.
- `lecture_07_figure_04.png` is not a broad board view but a targeted crop of the projector argument. The important layout point is that the “electron at $m$” property is represented by a sum over two orthogonal spin-tagged states, one with spin up and one with spin down.
- `lecture_07_figure_05.png` is a sparse geometry sketch. Two slanted branches suggest the two hole-to-detector routes, and a marked point above them indicates a symmetrically placed spin or detector. The lower circled expression belongs to the previous algebra and should not dominate the reading of this figure.
- `lecture_07_figure_06.png` is a schematic transition figure rather than a formula frame. A ket-state expression on the left points into a large oval containing several small marks, suggesting a move from a single state-vector description to a many-possibility or ensemble description. The figure is valuable mainly for the board rhetoric and spatial organization of that transition.

## TeX Reconstruction Plan
- `lecture_07_figure_02.png` must remain visible. Nearby, reconstruct the path-to-screen expansions in clean display math, explicitly as $|A\rangle \to \sum_m \psi_m |m\rangle$ and $|B\rangle \to \sum_m \phi_m |m\rangle$, with a short sentence tying the pointed term to the amplitude at site $m$.
- `lecture_07_figure_03.png` must remain visible. Typeset the clean equations nearby:
  $\sum_n (\psi_n+\phi_n)|n\rangle$
  and
  $P_m=|\psi_m+\phi_m|^2=\psi_m^*\psi_m+\phi_m^*\phi_m+\psi_m^*\phi_m+\phi_m^*\psi_m$.
  This should stay an equation figure, not a TikZ redraw.
- `lecture_07_figure_04.png` must remain visible. Reconstruct the fixed-$m$ projector clearly as
  $\Pi_m=|m,u\rangle\langle m,u|+|m,d\rangle\langle m,d|$,
  and place it near the text explaining that $\psi_m$ and $\phi_m$ multiply different ket vectors.
- `lecture_07_figure_05.png` must remain visible. Redraw the symmetric spin-placement geometry in TikZ nearby, with two branches and a symmetrically placed spin/detector point. The screenshot should be used as board-layout evidence rather than as the clean final diagram.
- `lecture_07_figure_06.png` must remain visible. Use a small TikZ schematic nearby to represent a single prepared state feeding into an ensemble or statistical description. Do not force a detailed formula out of the screenshot; let the transcript supply the density-matrix interpretation while the screenshot preserves the board’s conceptual layout.

## Caption Drafts
- `lecture_07_figure_02.png`: Screen-basis amplitude expansion
- `lecture_07_figure_03.png`: Interference probability and cross terms
- `lecture_07_figure_04.png`: Projector onto a fixed screen position
- `lecture_07_figure_05.png`: Symmetric placement of the spin detector
- `lecture_07_figure_06.png`: Schematic transition to a density-matrix description

## Editorially Verified Additions

- lecture_07_figure_07.png, 01:16:08: the board preserves \(S=\log n\), \(S=-\sum_i p_i\log p_i\), and the equal-probability reduction. The nearby typeset derivation supplies the small subscripts that are soft in the frame.
- lecture_07_figure_08.png, 01:21:20: the completed definition \(\sum_i\langle i|M|i\rangle=\operatorname{Tr}M\) is unobstructed. This is direct equation evidence.
- lecture_07_figure_09.png, 01:32:12: the diagonal entries \(\rho_1,\rho_2,\ldots\) and the normalization discussion are visible. The full matrix and \(\operatorname{Tr}\rho=1\) are typeset beside it.
- lecture_07_figure_10.png, 01:35:05: \(\langle F\rangle=\operatorname{Tr}(F\rho)\) and the start of its basis expansion are legible. The completed two-index derivation comes from the continuous transcript argument.
- lecture_07_figure_11.png, 01:41:25: the boxed equation \(S=-\operatorname{Tr}(\rho\log\rho)\) is complete, with the classical entropy formula retained above it.

All five additions were inspected against adjacent candidate frames. Each chosen timestamp shows a completed board state rather than an equation still being written, and none is used to support mathematics outside its visible or continuously spoken context.

## Uncertainties
- `lecture_07_figure_02.png`: The subscripts on the summed basis expansion are not perfectly sharp, and the crop does not fully preserve the left-hand arrows. The transcript is needed to regularize these as the $A$- and $B$-path expansions into the screen basis.
- `lecture_07_figure_03.png`: The left edge of the top line is slightly cropped, so the full initial state on that line should be completed from the transcript. The lower probability expansion is much clearer than the top line.
- `lecture_07_figure_04.png`: The first dyad is slightly clipped at the left edge, and the upper partial $\phi$-line is too incomplete to use independently. The projector formula is reliable only with cautious completion.
- `lecture_07_figure_05.png`: The labels near the slanted branches are not fully readable, and the marked point is clear as a location but not self-identifying from the image alone. The transcript is needed to confirm that this is the symmetric placement of the spin.
- `lecture_07_figure_06.png`: The ket label to the left of the arrow and the small marks inside the oval are not sharp enough for exact transcription. The frame should therefore be used as schematic evidence for the conceptual transition to mixtures or density matrices, not as a source for a precise board equation.
