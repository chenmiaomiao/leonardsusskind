# Mathematical Content

## Central-Force Mechanics

\[
v_r=\dot r,\qquad v_\theta=r\dot\theta,
\qquad
\mathcal L=\frac m2(\dot r^2+r^2\dot\theta^2)-U(r).
\]

\[
\pi_i=\frac{\partial\mathcal L}{\partial\dot q_i},
\qquad
\dot\pi_i=\frac{\partial\mathcal L}{\partial q_i}.
\]

\[
m\ddot r=mr\dot\theta^2-\frac{dU}{dr},
\qquad
L=mr^2\dot\theta=\text{constant}.
\]

\[
m\ddot r=-\frac{dU}{dr}+\frac{L^2}{mr^3},
\qquad
U_{\mathrm{eff}}(r)=U(r)+\frac{L^2}{2mr^2}.
\]

## Variations And Noether Charge

\[
\delta F=\sum_i\frac{\partial F}{\partial\alpha_i}\delta\alpha_i,
\qquad
\delta A=0.
\]

For an infinitesimal symmetry
\[
\delta q_i=\epsilon f_i(q),
\]
the on-shell variation reduces to
\[
0=\left[\sum_i\pi_i\delta q_i\right]_{t_1}^{t_2}.
\]
Therefore
\[
Q=\sum_i\pi_i f_i(q)
\]
is conserved.

For translation,
\[
Q_x=\sum_a p_{x_a}.
\]
For planar rotation,
\[
\delta x=-\epsilon y,\qquad \delta y=\epsilon x,
\qquad
Q=xp_y-yp_x.
\]

## Time Translation And Energy

\[
q_i(t)\longmapsto q_i(t-\epsilon),
\qquad
\delta q_i=-\epsilon\dot q_i.
\]

Including the endpoint overhangs gives
\[
0=\epsilon\left[
\mathcal L-\sum_i\pi_i\dot q_i
\right]_{t_1}^{t_2}.
\]
The conventional Hamiltonian is
\[
\boxed{H=\sum_i\pi_i\dot q_i-\mathcal L}.
\]

For
\[
\mathcal L=\frac12m\dot x^2-U(x),
\]
one obtains
\[
H=\frac12m\dot x^2+U(x).
\]

For a regular Legendre transformation,
\[
\det\left(\frac{\partial^2\mathcal L}
{\partial\dot q_i\,\partial\dot q_j}\right)\ne0.
\]
When \(\partial\mathcal L/\partial t\ne0\), time translation is not a
symmetry and the corresponding energy need not be conserved.
