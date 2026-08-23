# Math Bank

## Recurrence

- Phase-space coordinate:
  \(\Gamma=(\bm x_1,\ldots,\bm x_N;\bm p_1,\ldots,\bm p_N)\).
- Two particles in one half:
  \(P_2=1/4\).
- \(N\) particles in one half:
  \(P_{\rm half}=2^{-N}\).
- General constrained spatial volume:
  \(P(v)=(v/V)^N\).
- Entropy form:
  \(P(A)=\Omega_A/\Omega_{\rm eq}
  =\exp(S_A-S_{\rm eq})=e^{-\Delta S}\).
- Half-room entropy deficit:
  \(\Delta S=N\log 2\).
- Waiting scale:
  \(\tau_{\rm rec}\sim\tau_{\rm mix}/P(A)
  \sim\tau_{\rm mix}e^{\Delta S}\).

The microscopic timescale is required for dimensional consistency. The
lecture's \(2^N\) is the dimensionless recurrence-time ratio. Return means
re-entry into a finite macrostate region, or arbitrarily close recurrence in
the theorem, not exact equality of all continuous coordinates.

## Open-System Entropy

\[
\dot S_{\rm total}
=\dot S_{\rm subsystem}+\dot S_{\rm environment}\geq0.
\]

This equation supports the life-and-solar-flow discussion without claiming
that every local entropy must increase.

## Independent Spins

- Spin variable: \(\sigma_i=\pm1\).
- Lecture sign convention: \(\epsilon_i=\mu H\sigma_i\).
- Counts: \(n+m=N\).
- Configuration energy: \(E=(n-m)\mu H\).
- Multiplicity:
  \(\Omega(n,m)=N!/(n!\,m!)\).
- Partition sum:
  \[
  Z_N=\sum_{n=0}^{N}\binom{N}{n}
  (e^{-\beta\mu H})^n(e^{+\beta\mu H})^{N-n}.
  \]
- Closed form:
  \[
  Z_N=[e^{-\beta\mu H}+e^{+\beta\mu H}]^N
     =[2\cosh(\beta\mu H)]^N.
  \]
- Configuration magnetization:
  \(M_{\rm conf}=(n-m)/N\).
- Ensemble magnetization:
  \(M=\langle M_{\rm conf}\rangle\).
- Energy relation:
  \(\langle E\rangle=N\mu H M\).
- Thermodynamic derivative:
  \[
  \langle E\rangle
  =-\partial_\beta\log Z_N
  =-N\mu H\tanh(\beta\mu H).
  \]
- Final result:
  \(M=-\tanh(\beta\mu H)\).
- Limits:
  \(M\to-1\) as \(T\to0\) and \(M\to0\) as \(T\to\infty\).

The minus sign is not an error. Positive \(H\) lowers the energy of
\(\sigma=-1\) under the convention used in the lecture.

## Ising Chain

- Pair energy:
  \(E_{12}=-J\sigma_1\sigma_2\), \(J>0\).
- Open chain:
  \({\cal H}=-J\sum_{i=1}^{N-1}\sigma_i\sigma_{i+1}\).
- Infinite-temperature bond average:
  \(\langle\sigma_i\sigma_{i+1}\rangle=0\).
- Global symmetry:
  \(\sigma_i\mapsto-\sigma_i\) for every site.
- Ground states:
  all spins up and all spins down.
- Broken-symmetry order parameter:
  \[
  M_*=\lim_{H\to0^+}\lim_{N\to\infty}M_N(H).
  \]

The one-dimensional nearest-neighbor model has no finite-temperature
transition. The two-dimensional zero-field model does.

## Figure Support

- Figures 02, 07, and 08 support the recurrence geometry.
- Figures 03, 04, 05, and 09 support independent-spin equations and limits.
- Figures 06, 10, and 11 support the local coupling, chain Hamiltonian, and
  global symmetry.
