# Figure Notes
## Image Inventory
- lecture_06_figure_07.png: An unobstructed close view of \(\sum_n|n\rangle\langle n|=I\).
- lecture_06_figure_08.png: The intersecting-subspace sketch beside the commuting-projector product.
- lecture_06_figure_09.png: The Bell inequality and three columns of analyzer projectors.
- lecture_06_figure_10.png: The finite position lattice beside the linear evolution rules \(A\to A'\) and \(B\to B'\).
- lecture_06_figure_11.png: The screen amplitude and its direct, conjugate, and cross terms.
- lecture_06_figure_12.png: The slit alternatives correlated with up and down detector records.
- lecture_06_figure_13.png: Both path evolutions and their final entangled screen state.
- lecture_06_figure_14.png: Overlapping environmental wave packets used to explain partial path information.
- `lecture_06_figure_02.png`: A mostly blank whiteboard with a compact blue three-vector sketch in the upper-right region. One arrow is horizontal to the right, one is diagonal upward to the right, and a third shorter mark/vector sits near the upper-left side of the sketch. Susskind stands in front of the board but does not cover the main lines.
- `lecture_06_figure_03.png`: A clean equation board for basis vectors and expansion coefficients. At top left is a basis ket, in the middle an orthonormality relation, and below an expansion of an arbitrary state in the basis. A partial note at upper right indicates the index range.
- `lecture_06_figure_04.png`: A sparse board showing two two-spin basis states written side by side, separated by a comma. The left ket is slightly smudged but still readable in substance; the right ket is clearer.
- `lecture_06_figure_05.png`: A projector-construction board. Across the top is a sum of dyads identified with a projector onto a \(k=\lambda\) subspace. Lower on the board are a bra \(\langle\psi|\) and a ket \(|\psi\rangle\), positioned as the setup for an expectation-value calculation.
- `lecture_06_figure_06.png`: A pedagogical emphasis frame: the expression \(\Pi_k|\psi\rangle\) is circled on the board, and Susskind gestures toward it while explaining that it lies in the relevant eigensubspace.

## Blackboard Equations
- `lecture_06_figure_03.png`: \(|n\rangle\) [visible]
- `lecture_06_figure_03.png`: \(\langle m|n\rangle=\delta_{mn}\) [visible]
- `lecture_06_figure_03.png`: \(|\psi\rangle=\sum_n a_n\,|n\rangle\) [visible]
- `lecture_06_figure_03.png`: \(n=1,\ldots\) [partially visible]

- `lecture_06_figure_04.png`: \(|ud\rangle\) [partially visible]
- `lecture_06_figure_04.png`: \(|uu\rangle\) [visible]

- `lecture_06_figure_05.png`: \(\sum_a |a\rangle\langle a|=\Pi_{k=\lambda}\) [partially visible]
- `lecture_06_figure_05.png`: \(\langle\psi|\) [visible]
- `lecture_06_figure_05.png`: \(|\psi\rangle\) [visible]
- `lecture_06_figure_05.png`: \(\langle\psi|\Pi_{k=\lambda}|\psi\rangle\) [standard reconstruction]

- `lecture_06_figure_06.png`: \(\Pi_k|\psi\rangle\) [visible]
- `lecture_06_figure_06.png`: \(\Pi_{k=\lambda}|\psi\rangle\) [standard reconstruction]

- `lecture_06_figure_02.png`: No algebraic notation is legible; the content is diagrammatic rather than symbolic. [visible]

## Diagram And Layout Reading
- `lecture_06_figure_02.png` is a pure board sketch rather than an equation frame. The geometry is compact and unlabelled: a lower point supports a horizontal rightward arrow and a diagonal arrow to an upper point, with a shorter third vector/mark completing the comparison. The transcript makes clear that this sketch belongs to the discussion of linear dependence in a plane, so the figure is valuable mainly as evidence of the board layout and the three-vector teaching move.
- `lecture_06_figure_03.png` has the classic progression Susskind is using in this segment: define a basis vector, state orthonormality, then expand an arbitrary vector. The layout itself is useful because it shows the lecture building from basis notation to coefficients in one visual block.
- `lecture_06_figure_04.png` is not a derivation but a local example board. Its value is that the two basis states are juxtaposed without extra clutter, making the “same \(\sigma_3\) for the first spin” point easy to reconstruct nearby in prose.
- `lecture_06_figure_05.png` shows the transition from subspace basis vectors to the projection operator onto that subspace. The top line is the real content; the lower separated bra and ket indicate that the next move is the probability postulate as an expectation value.
- `lecture_06_figure_06.png` is visually emphatic rather than algebraically rich. The circled expression and Susskind’s gesture record the interpretive step: applying the projector to \(|\psi\rangle\) produces a vector that lies in the eigensubspace. This is useful as board rhetoric and layout evidence.

## TeX Reconstruction Plan
- `lecture_06_figure_02.png` must remain visible. Pair it with a compact TikZ redraw of the three-vector sketch nearby. Do not invent labels from the image alone; let the transcript carry the linear-(in)dependence interpretation, while the screenshot preserves the original board geometry.
- `lecture_06_figure_03.png` must remain visible. Reconstruct the equations cleanly in display math:
  \[
  \langle m|n\rangle=\delta_{mn},\qquad
  |\psi\rangle=\sum_n a_n\,|n\rangle.
  \]
  If the index range is needed, complete it cautiously from the transcript rather than from the cropped chalk alone.
- `lecture_06_figure_04.png` must remain visible. Typeset the two basis states clearly as
  \[
  |ud\rangle,\qquad |uu\rangle
  \]
  and explain in prose that both have the first spin up, hence the same \(\sigma_3\) eigenvalue for the first factor.
- `lecture_06_figure_05.png` must remain visible. Typeset the cleaned projector formula
  \[
  \Pi_{k=\lambda}=\sum_a |a\rangle\langle a|
  \]
  with a short sentence that \(a\) runs over an orthonormal basis of the \(k=\lambda\) subspace. Then place the probability postulate nearby as
  \[
  \mathrm{Prob}(k=\lambda\text{ in }|\psi\rangle)=\langle\psi|\Pi_{k=\lambda}|\psi\rangle.
  \]
- `lecture_06_figure_06.png` must remain visible. Pair it with a short reconstructed displayed line or prose statement explaining that \(\Pi_{k=\lambda}|\psi\rangle\) lies in the \(k=\lambda\) eigensubspace. The screenshot is mainly evidence for the explanatory emphasis, so it should sit close to the text making that interpretive point.

## Caption Drafts
- `lecture_06_figure_02.png`: Three vectors drawn in the plane
- `lecture_06_figure_03.png`: Orthonormal basis and expansion of an arbitrary state
- `lecture_06_figure_04.png`: Two two-spin states with first spin up
- `lecture_06_figure_05.png`: Projector onto the \(k=\lambda\) eigensubspace
- `lecture_06_figure_06.png`: The projected state as a vector in the eigensubspace

## Additional Blackboard Checks
- lecture_06_figure_07.png visibly gives \(\sum_n|n\rangle\langle n|=I\).
- lecture_06_figure_08.png partially shows \(P_kP_\ell|\psi\rangle=P_\ell P_k|\psi\rangle\).
- lecture_06_figure_09.png retains all three Bell joint projectors.
- lecture_06_figure_10.png retains the linear evolution rule beside the finite lattice.
- lecture_06_figure_11.png visibly gives \(|\psi_m+\phi_m|^2\) and its four terms.
- lecture_06_figure_12.png retains the two detector-correlated slit alternatives.
- lecture_06_figure_13.png retains \(\sum_n\psi_n|n,u\rangle+\sum_n\phi_n|n,d\rangle\).
- lecture_06_figure_14.png retains the overlapping and shifted packet sketch.

## Additional Caption Drafts
- lecture_06_figure_07.png: Resolution of identity
- lecture_06_figure_08.png: Commuting projectors select an intersection
- lecture_06_figure_09.png: Bell analyzer projectors
- lecture_06_figure_10.png: Finite-state evolution and linearity
- lecture_06_figure_11.png: Interference cross terms
- lecture_06_figure_12.png: A detector records the path
- lecture_06_figure_13.png: Orthogonal records reach the screen
- lecture_06_figure_14.png: Partial environmental records

## Uncertainties
- Figures 08 and 09 retain some lecturer occlusion; the visible board state verifies the geometry and operator layout, while the adjacent TeX supplies the complete equations.
- Figure 14 is diagrammatic. Its interpretation as distinguishable versus overlapping environmental records is fixed by the simultaneous spoken explanation.
- In `lecture_06_figure_02.png`, the three-vector sketch has no visible labels, and the exact relation among the arrows is not fully fixed by the image alone. The transcript should determine whether the intended point is linear dependence in the plane or comparison with a vector off the plane.
- In `lecture_06_figure_03.png`, the upper-right index note is cropped and soft. It looks like the start of an index range, but the full endpoint is not readable from the screenshot.
- In `lecture_06_figure_04.png`, the left ket is slightly smudged; it reads most plausibly as \(|ud\rangle\), but the transcript is what firmly settles that reading.
- In `lecture_06_figure_05.png`, the projector label on the right is not perfectly sharp; the subscript is best completed from the lecture context as \(k=\lambda\). The lower bra-ket layout does not yet show the full expectation-value formula on the board.
- In `lecture_06_figure_06.png`, only \(\Pi_k|\psi\rangle\) is visibly present. The explicit eigenvalue label and the statement that this lies in the \(k=\lambda\) subspace come from the spoken explanation rather than from extra chalk symbols in the frame.
