# Lecture 7 Mathematics

## Two-Dimensional Holonomy

\[
\Delta\theta=K\,\Delta A+O((\Delta A)^{3/2}),
\qquad
K_{\mathrm{sphere}}=\frac{1}{a^2}.
\]

## Parallel Transport and Curvature

\[
\frac{DV^\rho}{Ds}
=
\frac{dV^\rho}{ds}
+\Gamma^\rho{}_{\sigma\mu}V^\sigma\frac{dx^\mu}{ds}
=0,
\qquad
dV^\rho=-\Gamma^\rho{}_{\sigma\mu}V^\sigma dx^\mu.
\]

\[
\delta V^\rho
=
R^\rho{}_{\sigma\mu\nu}
V^\sigma\epsilon^\mu\eta^\nu
+O(\ell^3),
\qquad
\Sigma^{\mu\nu}
=
\epsilon^\mu\eta^\nu-\epsilon^\nu\eta^\mu.
\]

\[
[\nabla_\mu,\nabla_\nu]V^\rho
=
R^\rho{}_{\sigma\mu\nu}V^\sigma.
\]

\[
R^\rho{}_{\sigma\mu\nu}
=
\partial_\mu\Gamma^\rho{}_{\nu\sigma}
-\partial_\nu\Gamma^\rho{}_{\mu\sigma}
+\Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma}
-\Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}.
\]

## Riemann Symmetries

\[
R_{\alpha\beta\mu\nu}
=-R_{\beta\alpha\mu\nu}
=-R_{\alpha\beta\nu\mu},
\qquad
R_{\alpha\beta\mu\nu}=R_{\mu\nu\alpha\beta},
\qquad
R_{\alpha[\beta\mu\nu]}=0.
\]

\[
N_R=\frac{D^2(D^2-1)}{12}.
\]

## Ricci Curvature

\[
R_{\beta\nu}
=
R^\alpha{}_{\beta\alpha\nu}
=
g^{\alpha\mu}R_{\alpha\beta\mu\nu},
\qquad
R=g^{\beta\nu}R_{\beta\nu}.
\]

\[
R_{abcd}
=
g_{ac}R_{bd}-g_{ad}R_{bc}
-g_{bc}R_{ad}+g_{bd}R_{ac}
-\frac{R}{2}(g_{ac}g_{bd}-g_{ad}g_{bc})
\]
in three dimensions.

## Charge and Current

\[
\rho_q=\frac{dQ}{dV},
\qquad
j^i=\frac{dQ}{dA_i\,dt},
\qquad
J^\mu=(\rho_q,\mathbf j).
\]

\[
\frac{\partial\rho_q}{\partial t}
+\boldsymbol{\nabla}\cdot\mathbf j=0,
\qquad
\partial_\mu J^\mu=0.
\]

\[
Q=CV,
\qquad
U=\frac12CV^2=\frac{Q^2}{2C}.
\]

## Energy, Momentum, and Stress

\[
P^\mu=(E,\mathbf p).
\]

\[
T^{00}=\text{energy density},
\quad
T^{0i}=\text{energy flux},
\quad
T^{i0}=\text{momentum density},
\quad
T^{ij}=\text{momentum flux}.
\]

\[
\partial_\mu T^{\nu\mu}=0,
\qquad
\nabla_\mu T^{\nu\mu}=0.
\]

## Geodesic Limit

\[
\frac{d^2x^\mu}{d\tau^2}
+\Gamma^\mu{}_{\nu\sigma}
\frac{dx^\nu}{d\tau}
\frac{dx^\sigma}{d\tau}
=0.
\]

\[
\frac{d^2x^i}{dt^2}
\simeq
-\Gamma^i{}_{00},
\qquad
g_{00}\simeq1+2\Phi,
\qquad
\frac{d^2\mathbf x}{dt^2}\simeq-\boldsymbol{\nabla}\Phi.
\]
