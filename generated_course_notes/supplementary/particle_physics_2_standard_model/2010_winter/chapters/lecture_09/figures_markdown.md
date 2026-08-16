# Figure Notes
## Image Inventory
- `lecture_09_figure_02.png`: Whiteboard with the field-strength tensor written across the top left and a separate `F^2` written below it. Susskind stands at the right edge, leaving the equation unobstructed. This is a board-summary frame for the gauge-field Lagrangian.
- `lecture_09_figure_03.png`: Whiteboard showing the frozen Higgs-field substitution `\phi = f e^{i\alpha}` at top, then a two-line covariant-derivative calculation for `D\phi`, and below that a small hand-drawn broken-potential sketch with a minimum labeled near `f`. The lecturer is mostly out of frame.
- `lecture_09_figure_04.png`: Tighter whiteboard crop continuing the same broken-phase derivation. The upper lines still show `D\phi` and the combination `(\partial \alpha + A)`, while the middle line shows a term of the form `f^2(\partial \alpha + A)^2`. The lowest visible line isolates `f^2 A^2`, and Susskind’s finger points directly at `A^2`.
- `lecture_09_figure_05.png`: Whiteboard with a three-line stack of fermion equations. The top line is a Dirac-like equation with time and spatial derivatives and a mass term `m\beta\Psi`; the next two lines split it into coupled equations for `\Psi_R` and `\Psi_L`. Susskind appears only at the far right edge.

## Blackboard Equations
- `lecture_09_figure_02.png`: \(F_{\mu\nu}=\dfrac{\partial A_\mu}{\partial x^\nu}-\dfrac{\partial A_\nu}{\partial x^\mu}\) [visible]
- `lecture_09_figure_02.png`: \(F^2\) [visible]

- `lecture_09_figure_03.png`: \(\phi = f e^{i\alpha}\) [visible]
- `lecture_09_figure_03.png`: \(D\phi = \partial\phi + iA\phi\) [visible]
- `lecture_09_figure_03.png`: \(D\phi = i(\partial\alpha + A)\, f e^{i\alpha}\) [visible]

- `lecture_09_figure_04.png`: \(D\phi = \partial\phi + iA\phi\) [partially visible]
- `lecture_09_figure_04.png`: \(D\phi = i(\partial\alpha + A)\, f e^{i\alpha}\) [partially visible]
- `lecture_09_figure_04.png`: \(f^2(\partial\alpha + A)^2\) [visible]
- `lecture_09_figure_04.png`: \(f^2 A^2\) [visible]
- `lecture_09_figure_04.png`: \(|D_\mu\phi|^2 \sim f^2(\partial_\mu\alpha + A_\mu)(\partial^\mu\alpha + A^\mu)\) [standard reconstruction]
- `lecture_09_figure_04.png`: \(f^2 A_\mu A^\mu\) [standard reconstruction]

- `lecture_09_figure_05.png`: \(i\left(\dfrac{\partial \Psi}{\partial t} + \alpha_i \dfrac{\partial \Psi}{\partial x_i}\right)= m\beta\Psi\) [visible]
- `lecture_09_figure_05.png`: \(i\left(\dfrac{\partial \Psi_R}{\partial t} + i\,\alpha_i \dfrac{\partial \Psi_R}{\partial x_i}\right)= m\Psi_L\) [standard reconstruction]
- `lecture_09_figure_05.png`: \(i\left(\dfrac{\partial \Psi_L}{\partial t} - i\,\alpha_i \dfrac{\partial \Psi_L}{\partial x_i}\right)= m\Psi_R\) [standard reconstruction]
- `lecture_09_figure_05.png`: \(m\Psi_L,\; m\Psi_R\) [visible]

## Diagram And Layout Reading
- `lecture_09_figure_02.png` is organized like a compact reminder board: the definition of \(F_{\mu\nu}\) occupies the upper left, while `F^2` sits lower left as lecture shorthand for the gauge-field kinetic term. There is no diagram, but the spatial separation of the two expressions matters because it visually supports the spoken move from field tensor to Lagrangian.
- `lecture_09_figure_03.png` has a clear vertical derivational flow. The top line freezes the Higgs field at radius \(f\), the middle line defines the covariant derivative, and the next line substitutes the frozen form. Beneath these equations sits a small broken-potential doodle, drawn as a radial slice with a minimum labeled \(f\); it functions as a memory aid for the frozen-radius approximation rather than as a precise geometric diagram.
- `lecture_09_figure_04.png` tightens the focus from the earlier derivation onto the effective mass term. The upper derivation remains visible but secondary; the middle board line isolates the square of the \((\partial\alpha + A)\) combination, and the lowest line emphasizes \(A^2\). The pointing finger is part of the board logic here because it marks the exact term that is being interpreted as a gauge-boson mass contribution.
- `lecture_09_figure_05.png` is laid out as a three-step algebra board. The top line gives the unsplit Dirac equation. The next two lines rewrite it as coupled equations for right- and left-handed components. There is no separate diagram, only the structured equation stack. This layout is useful because the later symmetry argument refers to the mismatch between the left- and right-hand sides of these coupled equations under a \(U(1)\) transformation.

## TeX Reconstruction Plan
- `lecture_09_figure_02.png` should remain visible in the notes. Pair it with a cleaned displayed equation for \(F_{\mu\nu}\) and a short sentence that `F^2` is lecture shorthand for the gauge-field Lagrangian term. No TikZ redraw is needed.
- `lecture_09_figure_03.png` should remain visible. Typeset the three displayed equations cleanly nearby, and if the chapter wants a more legible broken-potential visual, add a small TikZ redraw of the radial slice beside or below the screenshot. The screenshot should still stay because it shows how Susskind organized the board.
- `lecture_09_figure_04.png` should remain visible as the evidence frame for the effective mass-term step. The notes should reconstruct the mathematics in indexed form, first as the square of the \((\partial_\mu\alpha + A_\mu)\) combination and then, after the gauge choice, as an effective \(A_\mu A^\mu\) term. No TikZ is needed here.
- `lecture_09_figure_05.png` should remain visible, but the equations should be retypeset carefully in LaTeX after checking the transcript for the exact sign and index conventions. This frame is an equation-evidence screenshot only; it does not need a TikZ redraw.
- More generally, the screenshots should not be asked to carry the full mathematical burden by themselves. Each one should sit near a cleaned displayed equation block that restores suppressed indices, fixes notation, and explains the local step in the lecture.

## Caption Drafts
- `lecture_09_figure_02.png`: Field-strength definition and \(F^2\) shorthand.
- `lecture_09_figure_03.png`: Frozen Higgs field and broken-phase covariant derivative.
- `lecture_09_figure_04.png`: Emergent \(f^2A^2\) term in the broken phase.
- `lecture_09_figure_05.png`: Coupled left- and right-handed fermion equations.

## Added Frame Notes
- **lecture_09_figure_06.png, 00:51:30:** Unobstructed board view of the scalar-dressed left- and right-chiral equations. Use it with the invariant Yukawa term \(\bar\psi_L\phi\psi_R+\mathrm{h.c.}\), not as authority for unstable board signs.
- **lecture_09_figure_07.png, 01:01:15:** Close view of the Higgs vacuum value plus radial fluctuation inside the Yukawa factor. The pointing hand identifies the factor being split into a mass contribution and a physical Higgs coupling.
- **lecture_09_figure_08.png, 01:16:30:** The upper board states \(m_i=g_i f\). The lower board contains earlier equations and the lecturer, but neither obscures the species-indexed mass relation.

Final captions should describe only these visible claims: the symmetry-allowed scalar insertion, restoration of the Higgs fluctuation, and the common vacuum scale multiplied by species-dependent Yukawa couplings.

## Uncertainties
- In `lecture_09_figure_02.png`, the derivative notation is legible in intent but written in a nonstandard fraction form with \(x^\mu\) and \(x^\nu\) in the denominators. The final notes should typeset the standard \(F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu\) form while noting that the screenshot preserves the board-level reminder.
- In `lecture_09_figure_03.png`, the derivative in \((\partial\alpha + A)\) is written schematically without Lorentz indices, and the sign convention for the covariant derivative is only locally reliable. The transcript should control the final indexed form.
- The small broken-potential doodle in `lecture_09_figure_03.png` is faint and schematic. It is good evidence that Susskind is still thinking about the Mexican-hat minimum at \(f\), but it is not precise enough to serve as the only diagram.
- In `lecture_09_figure_04.png`, the visible `A^2` is clear, but the intended relativistic object is only recoverable by standard completion as \(A_\mu A^\mu\). The screenshot itself does not display the indices.
- In `lecture_09_figure_05.png`, the exact matrix symbol multiplying the spatial derivative is somewhat ambiguous on the board, though the transcript strongly supports \(\alpha_i\). The split equations for \(\Psi_R\) and \(\Psi_L\) are readable in structure, but the exact placement of \(i\) factors and spatial indices should be checked against the transcript before final typesetting.
- Also in `lecture_09_figure_05.png`, the board uses a hybrid level of shorthand: the top line is more complete than the lower two, while the lower equations suppress some index detail. The final notes should standardize the notation rather than copying the board literally.
