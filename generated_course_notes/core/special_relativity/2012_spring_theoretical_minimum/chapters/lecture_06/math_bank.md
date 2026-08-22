# Math Bank: Lecture 6

## Index Notation

- Metric: \(\eta_{\mu\nu}=\operatorname{diag}(-1,1,1,1)\).
- Lowering: \(A_\mu=\eta_{\mu\nu}A^\nu\), so \(A_0=-A^0\) and \(A_m=A^m\).
- Contraction: \(A_\mu B^\mu=-A^0B^0+\sum_{m=1}^3A^mB^m\).
- Gradient: \(\partial_\mu=\partial/\partial x^\mu\) and \(d\phi=\partial_\mu\phi\,dx^\mu\).
- Four-divergence: \(\partial_\mu B^\mu\).

## Lorentz Matrices and Tensors

- Vector transformation: \((A^\mu)'=L^\mu{}_\nu A^\nu\).
- Covector transformation: \((A_\mu)'=M_\mu{}^\nu A_\nu\), with \(M=\eta L\eta\).
- Rank two: \((T^{\mu\nu})'=L^\mu{}_\sigma L^\nu{}_\tau T^{\sigma\tau}\).
- Rank three: \((T^{\mu\nu\lambda})'=L^\mu{}_\sigma L^\nu{}_\tau L^\lambda{}_\kappa T^{\sigma\tau\kappa}\).
- Index lowering: \(T^\mu{}_\nu=T^{\mu\sigma}\eta_{\sigma\nu}\).
- Antisymmetry: \(F^{\mu\nu}=-F^{\nu\mu}\), so \(F^{\mu\mu}=0\) and six independent components remain.

## Charged-Particle Action

- Free action: \(S_{\mathrm{free}}=-m\int d\tau\).
- Interaction: \(S_{\mathrm{int}}=-e\int A_\mu dx^\mu\).
- Ordinary-time Lagrangian:
  \[
  L=-m\sqrt{1-\dot{\mathbf x}^{\,2}}-eA_0-e\dot x^mA_m.
  \]
- Canonical momentum:
  \[
  \frac{\partial L}{\partial\dot x^m}
  =\frac{m\dot x_m}{\sqrt{1-\dot{\mathbf x}^{\,2}}}-eA_m.
  \]
- Derivative along the path:
  \[
  \frac{dA_m}{dt}=\partial_0A_m+\dot x^n\partial_nA_m.
  \]

## Lorentz Force

- Grouped spatial equation:
  \[
  m\frac{d}{dt}\left(\frac{\dot x_m}{\sqrt{1-\dot{\mathbf x}^{\,2}}}\right)
  =e(\partial_0A_m-\partial_mA_0)
  +e\dot x^n(\partial_nA_m-\partial_mA_n).
  \]
- Four-velocity: \(u^\mu=dx^\mu/d\tau\).
- Covariant equation in the lecture convention:
  \[
  m\frac{du^\mu}{d\tau}
  =e(\partial_\nu A^\mu-\partial^\mu A_\nu)u^\nu.
  \]
- With \(F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu\):
  \[
  m\frac{du^\mu}{d\tau}=-eF^\mu{}_\nu u^\nu.
  \]
- Fourth component: \(dK/dt=\mathbf F\cdot\mathbf v\).

## Field-Theory Principles

- Local action: \(S=\int d^3x\,dt\,\mathcal L(\phi,\partial_\mu\phi)\).
- Lorentz invariance is enforced by scalar construction.
- Gauge invariance is announced as the next constraint on the four-potential.

## Editorial Clarifications

- The sign in the compact force law is fixed by the interaction sign and field-tensor definition used here; other conventions may move that sign.
- Latin spatial indices may be raised or lowered freely in Cartesian coordinates because the spatial metric is the identity.
- The fourth component of proper acceleration is not generally zero because \(dt/d\tau=\gamma\) changes with speed.
- Magnetic force does no work because it is perpendicular to the velocity.
