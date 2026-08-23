# Figure Notes

## Reviewed Blackboard Frames

- `lecture_09_figure_02.png` (`00:09:11.730`): reject. The frame catches only the first strokes of the Euler--Lagrange operator, with no complete equation and too much blank board to add useful evidence.
- `lecture_09_figure_03.png` (`00:10:53.836`): keep with limits. The right board preserves the Euler--Lagrange equation and its Newton-like scalar-field reduction; the top line is partly obscured, so the nearby TeX supplies the complete expression.
- `lecture_09_figure_04.png` (`00:13:26.528`): keep with limits. The potential sketch and the transition from energy density to Lagrangian density are visible, while the incomplete right-board algebra is not treated as independently legible.
- `lecture_09_figure_05.png` (`00:18:35.380`): keep with limits. This is the strongest comparison frame for the fixed-volume and expanding-volume field equations, although some right-hand sides are cut off.
- `lecture_09_figure_06.png` (`00:41:04.178`): keep. The Friedmann equation, scalar-field substitution, and boxed potential-dominated approximation are legible enough to support the surrounding explanation.

## Mathematical Reconstruction

The screenshots are evidence of the board sequence, not substitutes for typeset mathematics. The chapter reconstructs the following equations next to the relevant frames:

\[
\frac{d}{dt}\left(\frac{\partial \mathcal L}{\partial\dot\phi}\right)
=\frac{\partial \mathcal L}{\partial\phi},
\qquad
\ddot\phi=-\frac{\partial V}{\partial\phi},
\]

\[
\frac{d}{dt}\left(a^3\dot\phi\right)
=-a^3\frac{\partial V}{\partial\phi},
\qquad
\ddot\phi+3H\dot\phi=-\frac{\partial V}{\partial\phi},
\]

and

\[
H^2=\frac{8\pi G}{3}\left(\frac{\dot\phi^2}{2}+V(\phi)\right)
\approx \frac{8\pi G}{3}V(\phi).
\]

These complete forms are supported jointly by the spoken derivations, adjacent board states, and standard notation. They are not represented as literal transcriptions of every visible chalk mark.

## Reconstructed Diagrams

- The inflationary-potential TikZ figure clarifies that the horizontal axis is the field value `\phi`, not time, and distinguishes the slow-roll plateau, exit, and reheating region.
- The one-dimensional caustic TikZ figure reconstructs the map `y=x+v(x)t` and the folding that occurs when its Jacobian vanishes.
- The two-dimensional caustic TikZ figure gives only the lecture's qualitative hierarchy of filaments, intersections, and voids; it does not claim to reproduce a specific board drawing.

## Uncertainties

- The complete denominator in the earliest Euler--Lagrange board state is not visible.
- The algebra in `lecture_09_figure_04.png` and portions of `lecture_09_figure_05.png` is fragmentary.
- The exact equality or approximation sign before the boxed square root in `lecture_09_figure_06.png` is obscured.
- The inflationary potential is schematic: the lecture does not derive its detailed shape or a reheating decay law.
