# Lecture 5 Mathematics

## Transformation and Failure

\[
V_m^{(y)}=\frac{\partial x^r}{\partial y^m}V_r^{(x)},
\qquad
\partial_n^{(y)}\phi
=
\frac{\partial x^m}{\partial y^n}\partial_m^{(x)}\phi .
\]

\[
\frac{\partial V_m^{(y)}}{\partial y^n}
=
\frac{\partial x^r}{\partial y^m}
\frac{\partial V_r^{(x)}}{\partial y^n}
+
\frac{\partial^2x^r}{\partial y^n\partial y^m}V_r^{(x)} .
\]

## Standard Levi--Civita Convention

\[
\nabla_nV_m=\partial_nV_m-\Gamma^r{}_{nm}V_r,
\qquad
\nabla_mV^n=\partial_mV^n+\Gamma^n{}_{mr}V^r .
\]

\[
\nabla_pT_{mn}
=
\partial_pT_{mn}
-\Gamma^r{}_{pm}T_{rn}
-\Gamma^r{}_{pn}T_{mr}.
\]

\[
\nabla_pg_{mn}=0,
\qquad
\Gamma^a{}_{bc}
=
\frac12g^{ad}
\left(
\partial_bg_{dc}
+\partial_cg_{db}
-\partial_dg_{bc}
\right).
\]

## Polar Coordinates

\[
ds^2=dr^2+r^2d\theta^2,
\quad
\Gamma^r{}_{\theta\theta}=-r,
\quad
\Gamma^\theta{}_{r\theta}
=
\Gamma^\theta{}_{\theta r}
=
\frac1r.
\]

## Curves

\[
t^m=\frac{dy^m}{ds},
\qquad
\frac{d\phi}{ds}=t^m\partial_m\phi,
\qquad
\frac{DV^n}{Ds}=t^m\nabla_mV^n.
\]

\[
\frac{DV^n}{Ds}
=
\frac{dV^n}{ds}
+
\Gamma^n{}_{mr}V^r\frac{dy^m}{ds}.
\]

\[
\frac{D t^n}{Ds}
=
\frac{d^2y^n}{ds^2}
+
\Gamma^n{}_{mr}
\frac{dy^m}{ds}
\frac{dy^r}{ds}.
\]

A geodesic satisfies \(D t^n/Ds=0\).
