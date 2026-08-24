# Mathematical Reconstruction

## Classical and Quantum Generators

\[
\dot F=\{F,H\}_{\mathrm{PB}},\qquad
U^\dagger(t)U(t)=I,
\]
\[
U(\epsilon)=I-\frac{i\epsilon}{\hbar}\hat H+O(\epsilon^2),
\qquad
\hat H^\dagger=\hat H.
\]

Taking the infinitesimal limit gives
\[
i\hbar\frac{d}{dt}\lvert\psi(t)\rangle
=\hat H\lvert\psi(t)\rangle.
\]

## Polarization Interference

For \(\hat H\lvert x\rangle=E_x\lvert x\rangle\) and
\(\hat H\lvert y\rangle=E_y\lvert y\rangle\),
\[
\lvert\psi(t)\rangle
=\alpha e^{-iE_xt/\hbar}\lvert x\rangle
+\beta e^{-iE_yt/\hbar}\lvert y\rangle.
\]

An equal-amplitude state tested by the \(45\)-degree analyzer has
\[
P_+(t)
=\frac12\left[
1+\cos\left(\frac{(E_y-E_x)t}{\hbar}\right)
\right].
\]
Only the energy difference enters; a common shift of all energies contributes
only a global phase.

## Expectation Values and Conservation

For a time-independent observable \(\hat K\),
\[
\frac{d}{dt}\langle\hat K\rangle
=\frac{i}{\hbar}\langle[\hat H,\hat K]\rangle
=-\frac{i}{\hbar}\langle[\hat K,\hat H]\rangle.
\]
Thus \([\hat H,\hat K]=0\) makes \(\hat K\) conserved under a
time-independent Hamiltonian.

## Free Particle

\[
\hat p=-i\hbar\frac{\partial}{\partial x},\qquad
\hat H=\frac{\hat p^2}{2m}
=-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2},
\]
\[
i\hbar\frac{\partial\psi}{\partial t}
=-\frac{\hbar^2}{2m}\frac{\partial^2\psi}{\partial x^2}.
\]
The definite-momentum solution is
\[
\psi_p(x,t)=C\exp\left[
\frac{i}{\hbar}\left(px-\frac{p^2}{2m}t\right)
\right].
\]

## Corrective Qualifications

- The simple exponential group law assumes a time-independent Hamiltonian.
- The equal-amplitude polarization state is generally elliptical between its
  linear extrema; it is circular at the quarter-cycle points.
- Operator domains and boundary conditions are required for self-adjointness
  in an infinite-dimensional Hilbert space.
- A plane wave is delta-normalized, not square-integrable; localized states
  are superpositions of momentum eigenstates.
