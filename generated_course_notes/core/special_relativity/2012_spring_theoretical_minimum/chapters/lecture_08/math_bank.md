# Lecture 8 Mathematics Bank

## Conventions

- Metric: eta with lower indices equals diag of minus one, one, one, one.
- Coordinates: x with upper zero equals t; spatial labels are x, y, z.
- Field tensor: F with lower mu nu equals partial mu A nu minus partial nu A mu.
- Electric field: E sub i equals F sub zero i.
- Magnetic field: B equals spatial curl of A.
- Four-current: J with upper mu equals rho, J x, J y, J z.
- Units absorb c and the vacuum constants except where the black-hole crossing time is written explicitly.

## Electromagnetic Tensor

\[
F_{\mu\nu}=
\begin{pmatrix}
0&E_x&E_y&E_z\\
-E_x&0&B_z&-B_y\\
-E_y&-B_z&0&B_x\\
-E_z&B_y&-B_x&0
\end{pmatrix},
\qquad
F^{\mu\nu}=
\begin{pmatrix}
0&-E_x&-E_y&-E_z\\
E_x&0&B_z&-B_y\\
E_y&-B_z&0&B_x\\
E_z&B_y&-B_x&0
\end{pmatrix}.
\]

For a boost along x,

\[
\Lambda^\mu{}_\nu=
\begin{pmatrix}
\gamma&-\gamma v&0&0\\
-\gamma v&\gamma&0&0\\
0&0&1&0\\
0&0&0&1
\end{pmatrix},
\qquad
\gamma=(1-v^2)^{-1/2}.
\]

\[
F'^{\mu\nu}
=
\Lambda^\mu{}_\sigma
\Lambda^\nu{}_\tau
F^{\sigma\tau}.
\]

For a pure B y field, F upper x z equals minus B y and

\[
F'^{0z}
=(-\gamma v)(-B_y)
=\gamma vB_y,
\qquad
E'_z=-\gamma vB_y.
\]

The lecture's essential conclusion is the nonzero magnitude, not an axis-independent sign.

## Maxwell Equations

The potential identities give

\[
\boldsymbol\nabla\cdot\mathbf B=0,
\qquad
\boldsymbol\nabla\times\mathbf E-\partial_t\mathbf B=\mathbf0.
\]

With the conventions above, the sourced pair is

\[
\boldsymbol\nabla\cdot\mathbf E=\rho,
\qquad
\boldsymbol\nabla\times\mathbf B+\partial_t\mathbf E=-\mathbf J.
\]

The current sign follows directly from

\[
\partial_\mu F^{\mu\nu}=J^\nu.
\]

In particular, taking a divergence of the spatial equation and a time derivative of Gauss's law gives

\[
\partial_t\rho+\boldsymbol\nabla\cdot\mathbf J=0.
\]

## Charge as Flow

\[
\rho(t,\mathbf x)
=
\lim_{\Delta V\to0}\frac{\Delta Q}{\Delta V},
\qquad
J_x
=
\lim_{\Delta A_x,\Delta t\to0}
\frac{\Delta Q_x}{\Delta A_x\Delta t}.
\]

The y and z components use windows normal to those axes. In covariant form,

\[
J^\mu=(\rho,J_x,J_y,J_z),
\qquad
\partial_\mu J^\mu=0.
\]

## Bianchi Identity

\[
\partial_\sigma F_{\nu\tau}
+\partial_\nu F_{\tau\sigma}
+\partial_\tau F_{\sigma\nu}
=0,
\qquad
\partial_{[\sigma}F_{\nu\tau]}=0.
\]

The all-spatial triple gives divergence B equals zero. A triple with one time index gives one component of Faraday's equation. Of 64 ordered triples, 40 contain repeated indices and vanish; the remaining 24 are six permutations of each of four independent triples.

## Standard Clarifications

- The live board's provisional source sign is normalized to the declared tensor convention and the continuity equation.
- The horizon discussion distinguishes coordinate-time asymptotics from what a finite detector can receive.
- A shrinking Schwarzschild black hole becomes hotter and evaporates faster; its characteristic Hawking wavelength shortens.
- Magnetic monopoles require patchwise or singular gauge potentials when one retains a potential description.
