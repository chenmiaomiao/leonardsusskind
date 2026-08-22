# Mathematical Spine

## Metric

\[
ds^2=g_{mn}\,dx^m dx^n,\qquad
g^{mn}g_{nr}=\delta^m{}_r,\qquad
V_m=g_{mn}V^n.
\]

## Normal Coordinates at a Point

\[
g_{mn}(P)=\delta_{mn},\qquad
\partial_r g_{mn}(P)=0,\qquad
\partial_r\partial_s g_{mn}(P)\ne 0
\quad\hbox{in general}.
\]

\[
x^m=y^m+C^m{}_{nr}y^n y^r+O(y^3).
\]

In four dimensions the symmetric pair nr has ten values. Four upper-index choices give forty quadratic coefficients, matching the forty first derivatives of the ten independent metric components.

## Covariant Differentiation

\[
\nabla_rV_m=\partial_rV_m-\Gamma^t{}_{rm}V_t,
\]
\[
\nabla_sT_{mn}
=\partial_sT_{mn}
-\Gamma^t{}_{sm}T_{tn}
-\Gamma^t{}_{sn}T_{mt}.
\]

\[
\Gamma^t{}_{mn}=\Gamma^t{}_{nm},\qquad
\nabla_sg_{mn}=0.
\]

## Levi-Civita Connection

\[
\Gamma^r{}_{mn}
=\frac12g^{rs}
\left(
\partial_mg_{sn}
+\partial_ng_{sm}
-\partial_sg_{mn}
\right).
\]

## Curvature Convention

\[
(\nabla_s\nabla_r-\nabla_r\nabla_s)V_n
=R_{srn}{}^tV_t,
\]
\[
R_{srn}{}^t
=\partial_r\Gamma^t{}_{sn}
-\partial_s\Gamma^t{}_{rn}
+\Gamma^p{}_{sn}\Gamma^t{}_{pr}
-\Gamma^p{}_{rn}\Gamma^t{}_{ps}.
\]

The convention is fixed by the commutator equation; other index orders may carry an overall sign change.

## Tidal Interpretation

\[
\frac{D^2\xi^\mu}{D\tau^2}
=-R^\mu{}_{\nu\rho\sigma}
u^\nu\xi^\rho u^\sigma,
\]

with the sign tied to the selected Riemann convention.
