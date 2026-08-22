# Lecture 9 Mathematical Record

## Declared Convention

- Metric: eta equals diag(-1,1,1,1).
- Field tensor: F mu nu equals partial mu A nu minus partial nu A mu.
- Components: F 0i equals E i and F ij equals epsilon ijk B k.
- Sourced equation: partial mu F upper mu nu equals J upper nu.
- Spatial source form in this convention: E dot plus curl B equals minus J.

## Plane Wave

\[
E_i=\epsilon_i\sin(kz-\omega t),\qquad
B_i=\beta_i\sin(kz-\omega t).
\]
\[
\epsilon_z=\beta_z=\epsilon_y=\beta_x=0,
\qquad
\beta_y=-\epsilon_x\frac{\omega}{k},
\qquad
\epsilon_x=-\beta_y\frac{\omega}{k}.
\]
\[
\omega^2=k^2,\qquad \omega=k\ (c=1),\qquad \omega=ck.
\]

## Scalar Warm-Up

\[
\mathcal L_\phi
=-\frac12\partial_\mu\phi\,\partial^\mu\phi-U(\phi).
\]
\[
\partial_\mu\left(
\frac{\partial\mathcal L}{\partial\phi_{,\mu}}
\right)
=
\frac{\partial\mathcal L}{\partial\phi}.
\]
\[
\Box\phi=U'(\phi),
\qquad
\ddot\phi-\nabla^2\phi=-U'(\phi).
\]

## Maxwell Scalar And Variation

\[
F^\mu{}_\mu=0,
\qquad
F_{\mu\nu}F^{\mu\nu}=2(B^2-E^2).
\]
\[
\mathcal L_{\rm EM}
=-\frac14F_{\mu\nu}F^{\mu\nu}
=\frac12(E^2-B^2).
\]
\[
\frac{\partial\mathcal L_{\rm EM}}
{\partial(\partial_\mu A_\nu)}
=-F^{\mu\nu}.
\]
\[
\delta S_{\rm EM}
=
\int d^4x\,
(\partial_\mu F^{\mu\nu})\delta A_\nu.
\]

## Sources And Gauge Invariance

\[
\partial_\mu J^\mu
=
\dot\rho+\nabla\cdot\mathbf J
=0.
\]
\[
\mathcal L
=
-\frac14F_{\mu\nu}F^{\mu\nu}
-J^\mu A_\mu.
\]
\[
\delta_\chi S_{\rm int}
=
-\int d^4x\,J^\mu\partial_\mu\chi
=
\int d^4x\,\chi\,\partial_\mu J^\mu.
\]
\[
\partial_\mu F^{\mu\nu}=J^\nu,
\qquad
\partial_\nu J^\nu
=
\partial_\nu\partial_\mu F^{\mu\nu}
=0.
\]

## Normalizations

- The scalar-field covariant and three-vector equations are checked against the mostly-plus metric.
- The component variation is indexed by field slot first and derivative slot second in comma notation.
- The live plus-current board equation is retained only as the explicitly identified incorrect intermediate state.
- The final source sign agrees with both the covariant field equation and local continuity.
