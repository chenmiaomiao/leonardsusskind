# Mathematical Content

## Simple Pendulum

\[
x=r\sin\theta,\qquad y=r\cos\theta,
\]
\[
v_x=r\cos\theta\,\dot\theta,\qquad
v_y=-r\sin\theta\,\dot\theta,\qquad
v^2=r^2\dot\theta^2.
\]

\[
T=\frac12mr^2\dot\theta^2,\qquad
U=-mgr\cos\theta,\qquad
\mathcal L=\frac12mr^2\dot\theta^2+mgr\cos\theta.
\]

\[
\pi_\theta=mr^2\dot\theta,\qquad
\ddot\theta+\frac gr\sin\theta=0,
\]
\[
H=\frac12mr^2\dot\theta^2-mgr\cos\theta.
\]

The energy barrier between bottom and upright configurations is
\[
U(\pi)-U(0)=2mgr.
\]
For a kinetic energy homogeneous of degree two in the velocities,
\[
\sum_i\frac{\partial T}{\partial\dot q_i}\dot q_i=2T.
\]

## Equal-Mass, Equal-Length Double Pendulum

Both angles are measured from the downward vertical. For the lower bob,
\[
v_{2x}=r\cos\theta\,\dot\theta+r\cos\phi\,\dot\phi,
\qquad
v_{2y}=-r\sin\theta\,\dot\theta-r\sin\phi\,\dot\phi.
\]

\[
T=mr^2\dot\theta^2+\frac12mr^2\dot\phi^2
  +mr^2\dot\theta\dot\phi\cos(\theta-\phi),
\]
\[
U=-2mgr\cos\theta-mgr\cos\phi,
\]
\[
\mathcal L=T-U.
\]

With \(\Delta=\theta-\phi\), the equations are
\[
2\ddot\theta+\ddot\phi\cos\Delta+\dot\phi^2\sin\Delta
  +2\frac gr\sin\theta=0,
\]
\[
\ddot\phi+\ddot\theta\cos\Delta-\dot\theta^2\sin\Delta
  +\frac gr\sin\phi=0.
\]

After gravity is removed,
\[
\theta\mapsto\theta+\epsilon,\qquad
\phi\mapsto\phi+\epsilon,
\]
and
\[
\pi_\theta=2mr^2\dot\theta+mr^2\dot\phi\cos\Delta,
\qquad
\pi_\phi=mr^2\dot\phi+mr^2\dot\theta\cos\Delta.
\]
The conserved Noether charge is
\[
Q=\pi_\theta+\pi_\phi.
\]

## Small Oscillations

\[
U(\theta)=-mgr\cos\theta
=-mgr+\frac12mgr\,\theta^2-\frac1{24}mgr\,\theta^4+\cdots.
\]

For a smooth potential near equilibrium,
\[
U(x)=U_0+ax+\frac12kx^2+c_3x^3+c_4x^4+\cdots.
\]
At equilibrium \(a=0\); at a nondegenerate stable minimum \(k>0\). A cubic
term may correct a positive quadratic term, but it cannot be the leading
nonzero term at a genuine smooth minimum.

## Harmonic Oscillator And Phase Space

\[
\mathcal L=\frac12m\dot x^2-\frac12kx^2,\qquad
F=-kx,\qquad
\omega^2=\frac km.
\]

\[
x(t)=A\cos\omega t+B\sin\omega t
=C\cos\!\left[\omega(t-t_0)\right].
\]

\[
p=m\dot x,\qquad
H(x,p)=\frac{p^2}{2m}+\frac12kx^2.
\]

\[
\frac{p^2}{2m}+\frac12kx^2=E,\qquad
x_{\max}=\sqrt{\frac{2E}{k}},\qquad
p_{\max}=\sqrt{2mE}.
\]

The velocity-to-momentum map is locally regular when
\[
\det\left(
\frac{\partial^2\mathcal L}
{\partial\dot q_i\,\partial\dot q_j}
\right)\ne0.
\]
