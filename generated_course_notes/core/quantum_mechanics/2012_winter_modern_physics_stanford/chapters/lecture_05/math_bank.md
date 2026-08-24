# Mathematics Bank

## Periodic Box

- Periodicity: psi(x + 2 pi r) = psi(x).
- Wave number: k = p / hbar.
- Box wavefunction: exp(ikx) / sqrt(2 pi r).
- Quantization: k = n / r and Delta k = 1 / r.
- Orthogonality: the normalized integral gives the Kronecker delta.

## Continuum and Fourier Duality

- Continuum state: ket(k_n) = ket(n) / sqrt(Delta k).
- Kernel: bra(x)ket(k) = exp(ikx) / sqrt(2 pi).
- Normalization: bra(k')ket(k) = delta(k - k').
- Completeness: integral dk ket(k)bra(k) = 1.
- Forward transform uses exp(-ikx); inverse transform uses exp(+ikx).
- In x-space, K = -i partial_x; in k-space, X = +i partial_k.

## Packets

- Localized form: psi(x) = f(x - x_0) exp(ik_0 x).
- Uncertainty: Delta x Delta k is at least one half.
- Classical correspondence is conditional on a narrow packet and a smooth
  potential.

## Polarization

- Horizontal and vertical basis: (1,0) and (0,1).
- P_xy is diag(1,-1).
- Diagonal states: (ket(x) plus or minus ket(y)) / sqrt(2).
- P_45 is the off-diagonal exchange matrix.
- P_xy and P_45 do not commute.
- The projector ket(x)bra(x) has expectation value equal to the
  x-polarization probability.
