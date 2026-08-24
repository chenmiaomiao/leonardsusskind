# Mathematical Reconstruction

## Polarization Observables

\[
P_0=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
P_{\pi/4}=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
P_c=\begin{pmatrix}0&-i\\i&0\end{pmatrix}.
\]

The circular basis is
\[
\lvert c_\pm\rangle=\frac{1}{\sqrt2}(1,\pm i)^T,
\qquad P_c\lvert c_\pm\rangle=\pm\lvert c_\pm\rangle.
\]

## Rays and Polarization Geometry

\[
\lvert\psi\rangle\sim e^{i\chi}\lvert\psi\rangle,\qquad
\lvert\psi\rangle=
\begin{pmatrix}
\cos(\vartheta/2)\\ e^{i\phi}\sin(\vartheta/2)
\end{pmatrix}.
\]

For a linear analyzer at angle \(\theta\),
\[
P_\theta=\frac12\left[
1+(a^2-b^2)\cos2\theta+2ab\cos\phi\sin2\theta
\right],
\]
\[
2\theta_{\rm maj}
=\operatorname{atan2}(2ab\cos\phi,a^2-b^2).
\]

With normalized Stokes parameters,
\[
S_1=a^2-b^2,\quad S_2=2ab\cos\phi,\quad S_3=2ab\sin\phi,
\quad S_1^2+S_2^2+S_3^2=1.
\]

## Adjoint, Hermitian, and Unitary Operators

\[
(L^\dagger)_{mn}=L_{nm}^*,\qquad
L=L^\dagger,\qquad
U^\dagger U=UU^\dagger=I.
\]

For a unitary eigenvector,
\[
U\lvert n\rangle=\lambda_n\lvert n\rangle
\quad\Longrightarrow\quad
\lvert\lambda_n\rvert=1.
\]

## Corrective Qualifications

- A Hermitian matrix has real eigenvalues, not necessarily real eigenvectors.
- In finite dimensions, \(U^\dagger U=I\) implies invertibility and hence
  \(UU^\dagger=I\). In infinite dimensions the first equality alone may
  describe a non-surjective isometry.
- The wave phase is written as \(kz-\omega t\), not as a dimensionally
  inconsistent sum of position and time.
- Handedness depends on a propagation and viewing convention; signed
  ellipticity records it once that convention is fixed.
