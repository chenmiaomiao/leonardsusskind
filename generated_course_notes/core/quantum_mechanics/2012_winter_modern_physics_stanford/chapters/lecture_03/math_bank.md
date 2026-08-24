# Mathematics Bank

## Discrete Basis Algebra

- Operator action:
  \(\hat K\lvert A\rangle=\lvert C\rangle\).
- Matrix element:
  \(K_{mn}=\langle m\rvert\hat K\lvert n\rangle\).
- Components:
  \(A_n=\langle n\vert A\rangle\).
- Expansion:
  \(\lvert A\rangle=\sum_n A_n\lvert n\rangle\).
- Completeness:
  \(\sum_n\lvert n\rangle\langle n\rvert=\mathbb I\).
- Matrix action:
  \((KA)_n=\sum_mK_{nm}A_m\).
- Product:
  \((KL)_{nm}=\sum_rK_{nr}L_{rm}\).

## Hermitian Operators

- Definition:
  \(\langle B\rvert\hat H\lvert A\rangle
  =(\langle A\rvert\hat H\lvert B\rangle)^*\).
- Eigenvalue equation:
  \(\hat H\lvert\lambda\rangle=\lambda\lvert\lambda\rangle\).
- Real eigenvalues follow from
  \(\langle\lambda\rvert\hat H\lvert\lambda\rangle
  =\lambda\langle\lambda\vert\lambda\rangle\).
- Orthogonality follows from
  \((\lambda_2-\lambda_1)
  \langle\lambda_1\vert\lambda_2\rangle=0\).
- Degenerate eigenspaces admit an orthonormal basis.
- A finite rotation is unitary. Its infinitesimal generator is
  anti-Hermitian, or minus i times a Hermitian generator.

## Measurement

- Discrete Born rule:
  \(P(\lambda_n\mid A)=
  |\langle\lambda_n\vert A\rangle|^2\).
- Normalization:
  \(\sum_nP(\lambda_n\mid A)=1\).
- A state is not itself an observable.
- An apparatus records eigenvalues, not eigenvectors.
- Definite means probability one for the associated eigenvalue.

## Particle on a Line

- Function inner product:
  \(\langle\phi\vert\psi\rangle=
  \int\phi^*(x)\psi(x)\,dx\).
- Position operator:
  \((\hat x\psi)(x)=x\psi(x)\).
- Position eigenvalue equation:
  \((x-\lambda)\psi_\lambda(x)=0\).
- Generalized position eigenfunction:
  \(\langle x\vert\lambda\rangle=\delta(x-\lambda)\).
- Continuous normalization:
  \(\langle x\vert x'\rangle=\delta(x-x')\).
- Continuous completeness:
  \(\int\lvert x\rangle\langle x\rvert\,dx=\mathbb I\).
- Delta sampling:
  \(\int\delta(x-\lambda)f(x)\,dx=f(\lambda)\).
- Position representation:
  \(\psi(x)=\langle x\vert\psi\rangle\).
- Position density:
  \(\rho(x)=|\psi(x)|^2\).
- Interval probability:
  \(P(a\leq x\leq b)=\int_a^b|\psi(x)|^2\,dx\).

## Wave Number and Momentum

- Anti-Hermitian derivative:
  \((d/dx)^\dagger=-d/dx\), subject to the domain and boundary
  conditions.
- Hermitian wave-number operator:
  \(\hat K=-i\,d/dx\).
- Eigenvalue equation:
  \(-i\,d\psi_k/dx=k\psi_k\).
- Plane wave:
  \(\psi_k(x)\propto e^{ikx}\).
- Constant modulus:
  \(|e^{ikx}|^2=1\).
- Wavelength:
  \(kL=2\pi\), with \(L=2\pi/|k|\).
- de Broglie:
  \(p=h/L=\hbar k\), including the sign of k for direction.
- Momentum operator:
  \(\hat p=-i\hbar\,d/dx\).

## Domain Cautions

- The delta function and plane waves are generalized eigenfunctions, not
  ordinary square-integrable states.
- The unit-area rectangle used to motivate a delta distribution has squared
  norm proportional to one over epsilon.
- The integration-by-parts proof requires vanishing boundary terms.
- Long wave packets or box normalization reconcile practical calculations
  with the nondecaying plane-wave idealization.
