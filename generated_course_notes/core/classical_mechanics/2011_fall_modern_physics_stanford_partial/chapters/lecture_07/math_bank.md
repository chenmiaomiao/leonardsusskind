# Math Bank

## Liouville Flow

\[
d\Gamma=\prod_{i=1}^{N}dq_i\,dp_i,
\qquad
\dot q_i=\frac{\partial H}{\partial p_i},
\qquad
\dot p_i=-\frac{\partial H}{\partial q_i}.
\]

\[
\nabla_{q,p}\cdot\bm u_H
=\sum_i\left(
\frac{\partial\dot q_i}{\partial q_i}
+\frac{\partial\dot p_i}{\partial p_i}
\right)
=\sum_i(H_{q_ip_i}-H_{p_iq_i})=0.
\]

For a density \(\rho\),
\[
\partial_t\rho+\nabla\cdot(\rho\bm v)=0.
\]

## Canonical Scaling

\[
L=\frac{\dot x^2}{2},
\qquad y=\alpha x,
\qquad
L=\frac{\dot y^2}{2\alpha^2},
\qquad
p_y=\frac{p_x}{\alpha}.
\]

\[
\Delta y\,\Delta p_y=\Delta x\,\Delta p_x.
\]

For coarse-grained detectable volume,
\[
S=k_B\log\left(\frac{\Omega_{\mathrm{cg}}}{\Omega_0}\right).
\]

## Magnetic Dynamics

\[
\bm F=q\bm v\times\bm B,
\qquad
\bm B=\nabla\times\bm A.
\]

\[
S=\int\frac12mv^2\,dt+q\int_\gamma\bm A\cdot d\bm x,
\qquad
L=\frac12m\dot{\bm x}^{,2}+q\bm A\cdot\dot{\bm x}.
\]

\[
p_i=m\dot x_i+qA_i,
\qquad
\bm p_{\mathrm{mech}}=\bm p-q\bm A.
\]

The explicit \(z\)-component reduction is
\[
m\ddot z
=q\dot x(\partial_zA_x-\partial_xA_z)
+q\dot y(\partial_zA_y-\partial_yA_z)
=q(\bm v\times\bm B)_z.
\]

For a static vector potential,
\[
H=\sum_i p_i\dot x_i-L=\frac12mv^2
=\frac{1}{2m}(\bm p-q\bm A)^2.
\]

Hamilton's equations imply
\[
m\dot v_i=qv_j(\partial_iA_j-\partial_jA_i)
=q(\bm v\times\bm B)_i.
\]

## Source-Sensitive Corrections

- Fine-grained Liouville volume never grows; only the fixed-resolution cell
  cover can grow.
- Relative phase-space volume gives long-time probability only with an
  appropriate invariant/ergodic component.
- Static means no explicit time dependence, not spatial uniformity.
- Gauge freedom changes the static Lagrangian by a total derivative.
- The correct canonical Hamiltonian denominator is \(2m\), not \(2m^2\).
