# Lecture 7 Mathematics Bank

## Conventions

- Metric: eta mu nu equals diag minus one, one, one, one.
- Coordinates: x mu equals t, x, y, z.
- Greek indices run over spacetime; Latin indices run over space.
- Partial mu equals partial divided by partial x mu.
- Four-velocity: u mu equals dx mu divided by d tau.
- Interaction: I int equals minus e integral A mu dx mu.
- Field tensor: F mu nu equals partial mu A nu minus partial nu A mu.

## Index Recap

\[
ds=\partial_\mu s\,dx^\mu,
\qquad
x_\mu x^\mu=x^2+y^2+z^2-t^2.
\]

\[
\partial^\mu
=
\left(
-\partial_t,\partial_x,\partial_y,\partial_z
\right).
\]

## Local Actions

\[
I[x]=\int dt\,L(x,\dot x),
\qquad
I[\phi]=\int d^4x\,\mathcal L(\phi,\partial_\mu\phi).
\]

## Charged Particle

\[
I=-m\int d\tau-e\int A_\mu dx^\mu.
\]

\[
L=-m\sqrt{1-\dot{\mathbf x}^{\,2}}
-e\left(A_0+A_m\dot x^m\right).
\]

\[
\frac{\partial L}{\partial\dot x^m}
=
\frac{m\dot x_m}{\sqrt{1-\dot{\mathbf x}^{\,2}}}
-eA_m
=
m u_m-eA_m.
\]

\[
\frac{dA_m}{dt}
=
\partial_0A_m+\dot x^n\partial_nA_m.
\]

\[
m\frac{du_m}{dt}
=
e(\partial_0A_m-\partial_mA_0)
+e\dot x^n(\partial_nA_m-\partial_mA_n).
\]

## Proper-Time Form

\[
m\frac{du^\mu}{d\tau}
=
-eF^\mu{}_\nu u^\nu,
\qquad
F_{\mu\nu}
=
\partial_\mu A_\nu-\partial_\nu A_\mu.
\]

\[
F^{\mu\nu}
=
\begin{pmatrix}
0&-E_x&-E_y&-E_z\\
E_x&0&B_z&-B_y\\
E_y&-B_z&0&B_x\\
E_z&B_y&-B_x&0
\end{pmatrix}.
\]

Both-index-up and both-index-down forms are antisymmetric. The mixed array is not antisymmetric under ordinary matrix transposition: its electric slots are symmetric and its spatial magnetic block is antisymmetric.

## Scalar Shift Warm-Up

\[
\mathcal L_0
=
-\frac12\partial_\mu\phi\,\partial^\mu\phi,
\qquad
\phi\longrightarrow\phi+c.
\]

\[
\mathcal L_\mu
=
-\frac12\partial_\mu\phi\,\partial^\mu\phi
-\frac{\mu^2}{2}\phi^2,
\]
so the mass term breaks constant-shift invariance.

\[
\phi\longrightarrow\phi+x,
\qquad
-\frac12(\partial_x\phi+1)^2
=
-\frac12(\partial_x\phi)^2-\partial_x\phi-\frac12.
\]

## Gauge Invariance

\[
A_\mu\longrightarrow A_\mu+\partial_\mu\Lambda.
\]

\[
\Delta I_{\mathrm{int}}
=
-e\int\partial_\mu\Lambda\,dx^\mu
=
-e[\Lambda(x_2)-\Lambda(x_1)].
\]

\[
F'_{\mu\nu}
=
F_{\mu\nu}
+\partial_\mu\partial_\nu\Lambda
-\partial_\nu\partial_\mu\Lambda
=
F_{\mu\nu}.
\]

## Clarifications

- The minus sign in the compact force law follows from the chosen action and field-tensor definition.
- The coin analogy separates correlation from influence; it is not a model of the full strength of quantum Bell correlations.
- The direct-field action obstruction is asserted by the lecture and not proved here.
- Gauge choices may set a selected component to zero locally under suitable regularity and boundary assumptions.
