# Mathematical Reference

## Linear Polarization

\[
|x\rangle=(1,0)^T,\qquad |y\rangle=(0,1)^T,
\qquad
\hat P_0=|x\rangle\langle x|-|y\rangle\langle y|=\sigma_z .
\]

\[
|\theta\rangle=
\begin{pmatrix}\cos\theta\\ \sin\theta\end{pmatrix},
\qquad
|\theta_\perp\rangle=
\begin{pmatrix}-\sin\theta\\ \cos\theta\end{pmatrix}.
\]

\[
\operatorname{Prob}(\beta|\alpha)
=|\langle\beta|\alpha\rangle|^2
=\cos^2(\alpha-\beta).
\]

\[
\hat P_\theta
=|\theta\rangle\langle\theta|
-|\theta_\perp\rangle\langle\theta_\perp|
=
\begin{pmatrix}
\cos2\theta&\sin2\theta\\
\sin2\theta&-\cos2\theta
\end{pmatrix}.
\]

## Circular Polarization

\[
|c_\pm\rangle=\frac{1}{\sqrt2}(1,\pm i)^T,
\qquad
\hat P_c=
\begin{pmatrix}0&-i\\ i&0\end{pmatrix}.
\]

For phase \(\phi=kz-\omega t\), equal transverse components in quadrature
trace a circle:

\[
E_x=E_0\sin\phi,\qquad E_y=E_0\cos\phi.
\]

## Incompatibility and Average Value

\[
[\hat P_\alpha,\hat P_\beta]
=2i\sin\!\bigl(2(\beta-\alpha)\bigr)\sigma_y.
\]

\[
\langle\hat K\rangle_\psi
=\langle\psi|\hat K|\psi\rangle
=\sum_n\lambda_n|\langle n|\psi\rangle|^2.
\]

\[
\langle\hat P_0\rangle_\theta
=\cos^2\theta-\sin^2\theta
=\cos2\theta.
\]
