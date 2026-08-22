# Math Bank: Lecture 4

## Mechanics Prototype

\[
A=\int_a^b dt\,L,\qquad
L=\frac{m}{2}\dot\phi^2-V(\phi),\qquad
m\ddot\phi=-\frac{dV}{d\phi}.
\]

Particle mechanics becomes a field theory in 0+1 dimensions when phi(t) is read as the value of a time-dependent field.

## Field Action and Variation

\[
A[\phi]=\int d^4x\,\mathcal L(\phi,\partial_\mu\phi;x^\mu),
\]
\[
\partial_\mu\left[
\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}
\right]
-\frac{\partial\mathcal L}{\partial\phi}=0.
\]

The lattice picture replaces derivatives by finite differences and makes the action an ordinary function of all interior field values.

## Scalar Dynamics

\[
\mathcal L=
\frac12\left[
\frac{1}{c^2}\phi_t^2-|\nabla\phi|^2
\right]-V(\phi),
\]
\[
\frac{1}{c^2}\phi_{tt}-\nabla^2\phi+\frac{dV}{d\phi}=0.
\]

For V=0:
\[
\frac{1}{c^2}\phi_{tt}-\nabla^2\phi=0.
\]

For \(V=\frac12\mu^2\phi^2\):
\[
\frac{1}{c^2}\phi_{tt}-\nabla^2\phi+\mu^2\phi=0.
\]

## Lorentz Structure

\[
\phi'(x')=\phi(x),
\]
\[
t'=\gamma(t-vx),\qquad
x'=\gamma(x-vt),\qquad
y'=y,\qquad z'=z,
\]
\[
A'^0=\gamma(A^0-vA^x),\qquad
A'^x=\gamma(A^x-vA^0),
\]
\[
A_\mu A^\mu=(A^0)^2-(A^x)^2-(A^y)^2-(A^z)^2.
\]

The gradient of a scalar is a covector:
\[
\partial_\mu\phi\,\partial^\mu\phi
=
\frac{1}{c^2}\phi_t^2-|\nabla\phi|^2.
\]

## Particle in a Scalar Background

\[
A=\int d\tau\,[-m+\phi(x,t)],
\]
\[
L=-(m-\phi)\sqrt{1-\dot x^2},
\qquad
p=(m-\phi)\frac{\dot x}{\sqrt{1-\dot x^2}},
\]
\[
\frac{d}{dt}\left[
(m-\phi)\frac{\dot x}{\sqrt{1-\dot x^2}}
\right]
=
\phi_x\sqrt{1-\dot x^2}.
\]

For a static background:
\[
\dot\phi=\phi_x\dot x.
\]

At low speed:
\[
\frac{d}{dt}[(m-\phi)\dot x]\approx\phi_x,
\qquad
U\approx-\phi.
\]

The sign follows from the action \(L=(\phi-m)\sqrt{1-\dot x^2}\). The scalar background shifts the effective mass to \(m_{\mathrm{eff}}=m-\phi\); this is a Higgs-like toy model, not the full Higgs mechanism.
