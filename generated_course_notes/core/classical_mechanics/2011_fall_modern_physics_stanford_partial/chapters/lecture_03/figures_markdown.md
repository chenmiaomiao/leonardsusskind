# Figure Notes

## Retained Blackboard Frames

### lecture_03_figure_02.png - 00:45:02

- Content: total time derivative of the velocity derivative of the Lagrangian,
  with a qualitative trajectory sketch on the adjacent board.
- Reading:
  \[
  \frac{d}{dt}\left(\frac{\partial L}{\partial\dot q_i}\right).
  \]
- Use: global-to-local interpretation of the Euler-Lagrange equation.
- Verdict: keep. The equation and trajectory are both visible.

### lecture_03_figure_03.png - 00:46:32

- Content: canonical momentum definition.
- Reading:
  \[
  \pi_i=\frac{\partial L}{\partial\dot q_i}.
  \]
- Uncertainty: the handwritten symbol resembles uppercase \(\Pi_i\); spoken
  language and standard notation support lowercase \(\pi_i\).
- Verdict: keep with normalized typesetting in the text.

### lecture_03_figure_04.png - 01:15:15

- Content: near-Earth coordinate sketch and two-coordinate kinetic energy.
- Reading:
  \[
  T=\frac12m\dot x^2+\frac12m\dot y^2.
  \]
- Use: setup for horizontal and vertical equations.
- Verdict: keep. The unfinished far-right writing is not used as evidence.

### lecture_03_figure_05.png - 00:10:20

- Content: product-rule integral and endpoint-vanishing integration by parts.
- Reading:
  \[
  \int\dot f\,g\,dt=[fg]-\int f\,\dot g\,dt.
  \]
- Verdict: keep. The established equations are legible despite the lecturer
  standing below the upper line.

### lecture_03_figure_06.png - 00:13:30

- Content: \(\int a(t)f(t)\,dt=0\) and a localized test-function sketch.
- Use: fundamental lemma of the calculus of variations.
- Verdict: keep. The blip and chosen point are both visible.

### lecture_03_figure_07.png - 00:22:55

- Content: physical and deformed paths with fixed endpoints, together with
  \(q_i=\hat q_i+\alpha f_i\) and endpoint conditions.
- Verdict: keep. This frame is clearer and less occluded than the inherited
  candidate at 00:22:45.

### lecture_03_figure_08.png - 00:28:42

- Content: action integral with \(L(q(t),\dot q(t))\).
- Reading:
  \[
  A=\int_{t_1}^{t_2}L(q(t),\dot q(t))\,dt.
  \]
- Verdict: keep. The full integral is unobstructed.

### lecture_03_figure_09.png - 00:34:10

- Content: action and first variation before integration by parts.
- Reading:
  \[
  \frac{dA}{d\alpha}
  =
  \int dt\sum_i
  \left(
  \frac{\partial L}{\partial q_i}f_i+
  \frac{\partial L}{\partial\dot q_i}\dot f_i
  \right).
  \]
- Verdict: keep. Both chain-rule contributions are visible.

### lecture_03_figure_10.png - 01:08:50

- Content: two-particle translation-invariant Lagrangian and two momentum
  equations.
- Reading:
  \[
  L=\frac12m_1\dot x_1^2+\frac12m_2\dot x_2^2-U(x_1-x_2).
  \]
- Verdict: keep. The frame supports equal-and-opposite coordinate derivatives.

### lecture_03_figure_11.png - 01:19:15

- Content: completed near-Earth Lagrangian, \(\partial U/\partial x=0\), and
  \(\partial U/\partial y=mg\).
- Verdict: keep. It directly supports the contrast between the two translation
  directions.

### lecture_03_figure_12.png - 01:27:50

- Content: polar geometry, \(v_r=\dot r\), \(v_\perp=r\dot\theta\), and the
  angular kinetic term.
- Verdict: keep. Geometry and formulas appear together and are legible.

### lecture_03_figure_13.png - 01:33:35

- Content: angular equation completed as
  \[
  \frac{d}{dt}(mr^2\dot\theta)=0.
  \]
- Verdict: keep. This later frame replaces the incomplete 01:33:15 candidate.

## Reconstructed Diagram

The rigid-translation TikZ diagram shows two particles shifted by the same
amount while their separation remains fixed. Every element follows directly
from the argument at 00:59:12 to 01:03:49. It is explanatory, not a claimed
copy of a particular board drawing.

## Rejected Candidates

- Opening Stanford announcement: no physics content.
- 00:22:45 varied path: more occluded than the selected 00:22:55 frame.
- 01:02:18 translation Lagrangian: writing is still in progress and occluded.
- 01:10:20 momentum frame: only a partial force derivative remains visible.
- 01:24:30 polar setup: lecturer occludes much of the sketch.
- 01:31:12 radial board: the displayed schematic radial equation omits the
  \(mr\dot\theta^2\) term required by the Lagrangian.
- 01:33:15 angular board: right-hand side is not yet complete.
- Closing Stanford announcement: no physics content.

## Mathematical Correction

From
\[
L=\frac12m\dot r^2+\frac12mr^2\dot\theta^2-U(r),
\]
the radial Euler-Lagrange equation is
\[
m\ddot r=mr\dot\theta^2-\frac{dU}{dr}.
\]
The chapter uses this complete equation rather than the isolated incomplete
board line. Angular momentum conservation is unaffected.
