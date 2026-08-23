# Math Bank

## Canonical Construction

\[
p_i=\frac{\partial L}{\partial\dot q_i},
\qquad
H(q,p,t)=\sum_i p_i\dot q_i-L(q,\dot q,t).
\]

\[
\delta H
=\sum_i\dot q_i\,\delta p_i
-\sum_i\frac{\partial L}{\partial q_i}\,\delta q_i,
\qquad
\dot q_i=\frac{\partial H}{\partial p_i},
\qquad
\dot p_i=-\frac{\partial H}{\partial q_i}.
\]

The transform is locally regular when
\[
\det\left(\frac{\partial^2L}
{\partial\dot q_i\partial\dot q_j}\right)\neq0.
\]

## Legendre Reciprocity

\[
P=\frac{dL}{dV},
\qquad
H(P)=PV-L(V),
\qquad
\frac{dH}{dP}=V.
\]

With the lecture's origin convention and a monotone inverse graph,
\[
L(V)=\int_0^V P(V')\,dV',
\qquad
H(P)=\int_0^P V(P')\,dP',
\qquad
L+H=PV.
\]

## Ordinary Particle

\[
L=\frac12m\dot x^2-U(x),
\qquad
p=m\dot x,
\qquad
H=\frac{p^2}{2m}+U(x).
\]

\[
\dot x=\frac{p}{m},
\qquad
\dot p=-\frac{dU}{dx},
\qquad
m\ddot x=-\frac{dU}{dx}.
\]

## Conservation and Flow

\[
\frac{dH}{dt}
=\sum_i\left(H_{q_i}H_{p_i}-H_{p_i}H_{q_i}\right)=0
\]
for a Hamiltonian with no explicit time dependence.

\[
\nabla_{q,p}\cdot
\left(H_{p_1},\ldots,H_{p_N},-H_{q_1},\ldots,-H_{q_N}\right)=0.
\]

For the oscillator,
\[
H=\frac{p^2}{2m}+\frac12m\omega^2q^2,
\]
so constant-energy curves are ellipses.

## Poisson Brackets

\[
\{A,B\}
=\sum_i\left(
A_{q_i}B_{p_i}-A_{p_i}B_{q_i}
\right),
\qquad
\frac{dA}{dt}=\{A,H\}+\frac{\partial A}{\partial t}.
\]

\[
\{q_i,p_j\}=\delta_{ij},
\qquad
\{q_i,q_j\}=\{p_i,p_j\}=0,
\qquad
\{A,H\}=0
\]
is the conservation criterion when \(A\) has no explicit time dependence.

## Source-Sensitive Corrections

- Reversibility motivates the opening discussion, but the divergence-free
  canonical vector field proves local phase-volume preservation.
- The area identity assumes compatible additive constants; the definition
  \(H=PV-L\) does not.
- A singular momentum--velocity map calls for constrained mechanics rather
  than the claim that every such system is physically meaningless.
- The lecture's \(H=p^3+q^3\) example gives
  \(\dot q=3p^2\), \(\dot p=-3q^2\), but its Legendre inverse is not globally
  regular.
- For explicit time dependence,
  \[
  \frac{dH}{dt}=\frac{\partial H}{\partial t},
  \qquad
  \frac{\partial H}{\partial t}
  =-\frac{\partial L}{\partial t}.
  \]
