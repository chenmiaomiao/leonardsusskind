# Lecture 9 Mathematics Bank

## Point Particle And String Size

\[
E=\frac{p^2}{2m},\qquad L=pR,\qquad
I=mR^2,\qquad E=\frac{L^2}{2I}.
\]

The structural open-string expansion is
\[
X(\sigma)-X_{\rm cm}\sim
\sum_{n\geq1}\frac{a_n+a_n^\dagger}{\sqrt n}\cos(n\sigma).
\]
With
\(\langle0|a_na_m^\dagger|0\rangle=\delta_{nm}\),
\[
\left\langle(X-X_{\rm cm})^2\right\rangle_0
\sim\sum_{n\geq1}\frac{\cos^2(n\sigma)}{n}
\sim\frac12\sum_{n\geq1}\frac1n.
\]
At finite cutoff \(N\), the result grows as
\(\frac12\log N+O(1)\).  Exact coefficients in the mode expansion are not
claimed from the source.

## Effective Geometry And Gravity

For the spread string on a sphere,
\[
I=\int r_\perp^2\,dm,\qquad
I_{\rm eff}<mR^2,\qquad
E_{\rm rot}=\frac{L^2}{2I_{\rm eff}}
=\frac{L^2}{2mR_{\rm eff}^2}.
\]
The leading cutoff flow is schematic:
\[
\frac{\partial g_{\mu\nu}}{\partial\log\Lambda}
=-C R_{\mu\nu}+\cdots .
\]
Equivalently, conventional worldsheet notation begins with
\[
\beta^g_{\mu\nu}=\alpha'R_{\mu\nu}+\cdots .
\]
The fixed-point condition is independent of flow-direction convention:
\[
R_{\mu\nu}=0.
\]

With gravitational constants suppressed,
\[
G_{\mu\nu}
=R_{\mu\nu}-\frac12g_{\mu\nu}R
=T_{\mu\nu}.
\]
In vacuum and \(D\neq2\),
\[
0=g^{\mu\nu}G_{\mu\nu}
=\left(1-\frac D2\right)R
\quad\Longrightarrow\quad
R=0
\quad\Longrightarrow\quad
R_{\mu\nu}=0.
\]

## Flat Tori

A two-torus is a parallelogram with opposite edges identified.  Its area is
the simplest Kahler modulus.  Its complex structure
\(\tau=\tau_1+i\tau_2\) packages shear and aspect ratio after scale is
removed.  A Dehn twist acts discretely as
\(\tau\mapsto\tau+1\); it is not the continuous shear itself.  A reflected
edge identification instead produces a Klein bottle.

## Circle Momentum

Single-valuedness on a circle of circumference \(2\pi R\) gives
\[
e^{ip_c(x+2\pi R)/\hbar}=e^{ip_cx/\hbar},
\qquad
p_c=\frac{n\hbar}{R}.
\]
With \(c=\hbar=1\), a higher-dimensional massless state obeys
\[
E^2=\mathbf p_{\rm large}^2+\frac{n^2}{R^2},
\]
so the lower-dimensional Kaluza--Klein masses are
\[
m_n=\frac{|n|}{R}.
\]

## Winding And T-Duality

For string tension \(T=1/(2\pi\alpha')\), a closed string wound \(w\) times
has
\[
m_w=2\pi T|w|R=\frac{|w|R}{\alpha'}.
\]
The lecture sets \(\alpha'=1\), giving \(m_w=|w|R\).  Momentum and winding
towers exchange under
\[
R\longleftrightarrow\frac{\alpha'}{R},
\qquad
n\longleftrightarrow w.
\]
The self-dual radius is \(R=\sqrt{\alpha'}\).  In lecture units it is
\(R=1\).

## Conserved Winding

An unwound closed loop may be stretched so that opposite segments carry
opposite orientation around the circle.  Reconnection can split it into
two strings with
\[
w_1=+1,\qquad w_2=-1,\qquad w_{\rm total}=0.
\]
The construction proves that winding sectors are dynamically required
while preserving net winding.

## Source Cautions

- Do not reconstruct the garbled rotor algebra beyond the completed board
  result.
- Do not assign an exact coefficient to the string-size sum or Ricci flow
  from this lecture.
- Keep worldsheet conformal invariance distinct from spacetime conformal
  symmetry.
- State the lecture's \(\alpha'=1\) convention before using
  \(R\leftrightarrow1/R\).
- Treat the final small-radius statement as an equivalence of circle
  backgrounds, not an unrestricted proof of one universal minimum length.
