# Lecture 8 Mathematics Bank

## Operator Form

\[
(\nabla_\mu V)^\alpha
=
\partial_\mu V^\alpha+\Gamma^\alpha{}_{\mu\beta}V^\beta,
\qquad
\nabla_\mu=\partial_\mu+\Gamma_\mu.
\]

\[
[A,B]=AB-BA,
\qquad
[\partial_x,F(x)]V=F'(x)V.
\]

## Curvature Convention

\[
[\nabla_\mu,\nabla_\nu]V^\alpha
=
R^\alpha{}_{\beta\mu\nu}V^\beta.
\]

\[
R^\alpha{}_{\beta\mu\nu}
=
\partial_\mu\Gamma^\alpha{}_{\nu\beta}
-\partial_\nu\Gamma^\alpha{}_{\mu\beta}
+\Gamma^\alpha{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\beta}
-\Gamma^\alpha{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\beta}.
\]

\[
\Delta V^\alpha
=
\frac12R^\alpha{}_{\beta\mu\nu}V^\beta\Sigma^{\mu\nu}
+O(\ell^3),
\qquad
\Sigma^{\mu\nu}
=
\epsilon^\mu\eta^\nu-\epsilon^\nu\eta^\mu.
\]

## Riemann Symmetries

\[
R_{\alpha\beta\mu\nu}
=-R_{\beta\alpha\mu\nu}
=-R_{\alpha\beta\nu\mu}
=R_{\mu\nu\alpha\beta},
\qquad
R_{\alpha[\beta\mu\nu]}=0.
\]

\[
N_R(n)=\frac{n^2(n^2-1)}{12},
\qquad
N_R(2)=1,\quad N_R(3)=6,\quad N_R(4)=20.
\]

## Contractions

\[
R_{\beta\nu}=R^\alpha{}_{\beta\alpha\nu},
\qquad
R_{\mu\nu}=R_{\nu\mu},
\qquad
R=g^{\mu\nu}R_{\mu\nu}.
\]

In two dimensions,
\[
R_{\alpha\beta\mu\nu}
=
\frac{R}{2}
\left(
g_{\alpha\mu}g_{\beta\nu}
-g_{\alpha\nu}g_{\beta\mu}
\right).
\]

## Geodesic and Newtonian Limit

\[
\frac{d^2x^\mu}{d\tau^2}
+\Gamma^\mu{}_{\sigma\lambda}
\frac{dx^\sigma}{d\tau}
\frac{dx^\lambda}{d\tau}=0.
\]

\[
g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu},
\qquad
x^0=t\simeq\tau,
\qquad
\frac{dx^0}{d\tau}\simeq1,
\qquad
\frac{dx^i}{d\tau}\ll1.
\]

\[
\frac{d^2x^i}{dt^2}\simeq-\Gamma^i{}_{00},
\qquad
\Gamma^i{}_{00}
\simeq
\frac12\delta^{ij}\partial_jg_{00}.
\]

For signature \(+---\),
\[
\frac{d^2x^i}{dt^2}
\simeq
-\frac12\delta^{ij}\partial_jg_{00}
=-\delta^{ij}\partial_j\Phi,
\]
so
\[
g_{00}\simeq1+2\Phi
\quad(c=1),
\qquad
g_{00}\simeq1+\frac{2\Phi}{c^2}
\quad(\text{restored units}).
\]

## Source Equation and Tensor Candidate

\[
\nabla^2\Phi=4\pi G\rho,
\qquad
T_{00}\simeq\rho,
\qquad
\nabla^2g_{00}=8\pi G T_{00}.
\]

\[
A R_{\mu\nu}+B g_{\mu\nu}R=8\pi G T_{\mu\nu}.
\]

The previewed combination is
\[
G_{\mu\nu}
=
R_{\mu\nu}-\frac12g_{\mu\nu}R.
\]

## Sign and Scope Checks

- Reversing the commutator order or loop orientation reverses the Riemann
  sign.
- The weak-field relation assumes signature \(+---\), slow motion, weak
  perturbations, and negligible time derivatives of the metric.
- A zero curvature scalar does not imply flatness in dimensions four and
  higher.
- The final Einstein tensor is previewed, not derived, in this lecture.
