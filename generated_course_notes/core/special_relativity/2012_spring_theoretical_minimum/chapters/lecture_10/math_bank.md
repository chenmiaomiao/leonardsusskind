# Lecture 10 Math Bank

## Convention Dictionary

\[
\mathbf E_M=-\dot{\mathbf A}+\nabla A_0,
\qquad
\mathbf E_L=+\dot{\mathbf A}-\nabla A_0=-\mathbf E_M,
\qquad
\mathbf B=\nabla\times\mathbf A.
\]

\[
\mathbf J_L=-\mathbf J_F,
\qquad
\rho_L=-\rho_F.
\]

Standard Maxwell--Franklin equations in rationalized units with \(c=1\):

\[
\nabla\times\mathbf E_M=-\dot{\mathbf B},
\quad
\nabla\cdot\mathbf B=0,
\quad
\nabla\times\mathbf B=\dot{\mathbf E}_M+\mathbf J_F,
\quad
\nabla\cdot\mathbf E_M=\rho_F.
\]

The course convention follows by substituting all three sign maps.

## Mechanical, Canonical, and Noether Momentum

\[
\mathbf P_{\mathrm{mech}}=M\dot{\mathbf X}_{\mathrm{cm}},
\qquad
p_i=\frac{\partial L}{\partial\dot q_i},
\qquad
Q=\sum_i p_i\,\delta q_i.
\]

For the board convention of a charged particle:

\[
L=\frac12m\dot{\mathbf x}^{\,2}-V-e\dot{\mathbf x}\cdot\mathbf A,
\qquad
p_i=m\dot x_i-eA_i.
\]

The sign of the vector-potential term depends on charge and interaction conventions; its presence is the invariant lesson.

## Hamiltonian

\[
H=\sum_i p_i\dot q_i-L.
\]

\[
L=\frac12m\dot x^2-V(x)
\quad\Longrightarrow\quad
H=\frac12m\dot x^2+V(x).
\]

The shortcut that reverses the nonvelocity term is valid here because the velocity dependence is a conventional positive quadratic form.

## Field Mechanics

\[
q_i(t)\longrightarrow\phi(\mathbf x,t),
\qquad
\sum_i\longrightarrow\int d^3x.
\]

\[
\partial_x\phi
=\lim_{\epsilon\to0}
\frac{\phi(x+\epsilon)-\phi(x)}{\epsilon}.
\]

\[
S=\int dt\,d^3x\,\mathcal L,
\qquad
\Pi=\frac{\partial\mathcal L}{\partial\dot\phi},
\qquad
\mathcal H=\Pi\dot\phi-\mathcal L,
\qquad
H=\int d^3x\,\mathcal H.
\]

## Scalar Field

\[
\mathcal L
=\frac12\dot\phi^2-\frac12(\nabla\phi)^2-V(\phi),
\qquad
\Pi=\dot\phi.
\]

\[
\mathcal H
=\frac12\dot\phi^2+\frac12(\nabla\phi)^2+V(\phi).
\]

\[
\ddot\phi-\nabla^2\phi=-V'(\phi).
\]

A fixed jump over lattice spacing \(\epsilon\) costs gradient energy proportional to

\[
\left(\frac{\Delta\phi}{\epsilon}\right)^2,
\]

which diverges in the continuum limit unless the field is smooth.

## Energy--Momentum Density

\[
T^{00}=\mathcal H,
\qquad
E=P^0=\int d^3x\,T^{00}.
\]

\[
\partial_\mu T^{\mu\nu}=0.
\]

For a translated scalar field, up to the active/passive sign convention,

\[
\delta\phi=\epsilon^m\partial_m\phi,
\qquad
P_m\propto\int d^3x\,\Pi\,\partial_m\phi,
\qquad
T^{0m}=\Pi\,\partial_m\phi.
\]

## Electromagnetism in Temporal Gauge

\[
A'_\mu=A_\mu+\partial_\mu S,
\qquad
\partial_tS=-A_0,
\qquad
A'_0=0.
\]

\[
\mathbf E=-\dot{\mathbf A},
\qquad
\mathbf B=\nabla\times\mathbf A.
\]

\[
\mathcal L_{\mathrm{EM}}
=-\frac14F_{\mu\nu}F^{\mu\nu}
=\frac12(\mathbf E^2-\mathbf B^2)
=\frac12\dot{\mathbf A}^{\,2}
-\frac12(\nabla\times\mathbf A)^2.
\]

\[
\Pi_m=\dot A_m=-E_m.
\]

\[
T^{00}_{\mathrm{EM}}
=\frac12(\mathbf E^2+\mathbf B^2).
\]

## Poynting Momentum

\[
P_n=\int d^3x\,E_m\partial_nA_m.
\]

\[
E_m\partial_nA_m
=E_m(\partial_nA_m-\partial_mA_n)
+E_m\partial_mA_n.
\]

\[
E_m(\partial_nA_m-\partial_mA_n)
=(\mathbf E\times\mathbf B)_n.
\]

\[
\int d^3x\,E_m\partial_mA_n
=\int_{\partial V}d\Sigma_m\,E_mA_n
-\int d^3x\,A_n\partial_mE_m.
\]

For vanishing boundary terms and a source-free region:

\[
\mathbf P_{\mathrm{EM}}
=\int d^3x\,\mathbf E\times\mathbf B,
\qquad
\mathbf g=\mathbf E\times\mathbf B.
\]

## Tensor Interpretation

\[
T^{00}=u,
\qquad
T^{0i}=g^i,
\qquad
T^{i0}=S^i,
\qquad
T^{ij}=\text{momentum flux or stress}.
\]

For the symmetric physical tensor:

\[
T^{0i}=T^{i0}.
\]

Thus in \(c=1\) units,

\[
\mathbf S=\mathbf g=\mathbf E\times\mathbf B.
\]

With ordinary units restored, \(\mathbf g=\mathbf S/c^2\).

## Convention and Accuracy Notes

- The later electromagnetic calculation uses the standard Maxwell electric field.
- Overall signs in the canonical Noether generator depend on active versus passive translations; the gauge-invariant physical momentum fixes the final direction.
- The field-only integration-by-parts argument assumes no charge density. With sources, matter momentum must be included.
- Static crossed fields can carry field momentum. A closed static apparatus balances the total through matter, supports, stresses, or hidden momentum.
- A canonical energy--momentum tensor need not initially be symmetric; the physical relativistic tensor used for the final interpretation can be improved to a symmetric form.
