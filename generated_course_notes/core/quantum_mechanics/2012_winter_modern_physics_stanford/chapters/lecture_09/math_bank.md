# Mathematical Bank

## Thermal Prelude

\[
E_{\rm mode}=kT,\qquad E_n=nh\nu.
\]

## Free Particle

\[
\hat p=-i\hbar\partial_x,\qquad
\hat H=\frac{\hat p^2}{2m},\qquad
i\hbar\partial_t\psi=-\frac{\hbar^2}{2m}\partial_x^2\psi.
\]

\[
\psi_p(x,t)=\exp\!\left[\frac{i}{\hbar}
\left(px-\frac{p^2}{2m}t\right)\right],
\qquad E=\frac{p^2}{2m}.
\]

## Fourier Evolution

\[
\psi(x,t)=\frac{1}{\sqrt{2\pi\hbar}}\int dp\,
e^{ipx/\hbar-ip^2t/(2m\hbar)}\widetilde\psi(p).
\]

\[
\widetilde\psi(p)=\frac{1}{\sqrt{2\pi\hbar}}\int dx\,
e^{-ipx/\hbar}\psi(x,0).
\]

\[
\rho_E(E)=\frac{m}{\sqrt{2mE}}
\left(
|\widetilde\psi(\sqrt{2mE})|^2+
|\widetilde\psi(-\sqrt{2mE})|^2
\right).
\]

## Brackets and Evolution

\[
\frac{d}{dt}\langle K\rangle
=\frac{i}{\hbar}\langle[H,K]\rangle
+\left\langle\frac{\partial K}{\partial t}\right\rangle,
\qquad
\dot K=\{K,H\}_{\rm PB}.
\]

\[
[f(\hat x),\hat p]=i\hbar f'(\hat x),\qquad
[\hat x,g(\hat p)]=i\hbar g'(\hat p).
\]

\[
[AB,C]=A[B,C]+[A,C]B.
\]

## Ehrenfest Equations

\[
\frac{d}{dt}\langle x\rangle=\frac{\langle p\rangle}{m},
\qquad
\frac{d}{dt}\langle p\rangle=-\langle U'(\hat x)\rangle.
\]
