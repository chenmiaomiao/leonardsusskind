# Mathematical Ledger

## Core Relations

- Coarse velocity estimate:
  \(\displaystyle v_{\mathrm{avg}}\simeq L/T\),
  \(\displaystyle \Delta v_{\mathrm{avg}}\sim\delta/T\).
- Localization recoil scale:
  \(\displaystyle \Delta p_{\mathrm{kick}}\sim\hbar/\delta\).
- Complex conjugation:
  \(\displaystyle (z_1z_2)^*=z_1^*z_2^*\) and
  \(\displaystyle (z_1^*z_2)^*=z_2^*z_1\).
- Complex linear combination:
  \(\displaystyle \alpha|A\rangle+\beta|B\rangle\).
- Ket-to-bra rule:
  \(\displaystyle \alpha|A\rangle\leftrightarrow
  \langle A|\alpha^*\).
- Conjugate symmetry:
  \(\displaystyle \langle A|B\rangle=\langle B|A\rangle^*\).
- Positive definiteness:
  \(\displaystyle \langle A|A\rangle\geq0\), with equality only for the zero
  vector.
- Function inner product:
  \(\displaystyle \langle\phi|\psi\rangle
  =\int_I\phi^*(x)\psi(x)\,dx\).
- Column inner product:
  \(\displaystyle \langle b|a\rangle=\sum_i b_i^*a_i\).
- Orthonormality:
  \(\displaystyle \langle b_i|b_j\rangle=\delta_{ij}\).
- Component extraction:
  \(\displaystyle v_j=\langle b_j|v\rangle\).
- Basis reconstruction:
  \(\displaystyle |v\rangle=\sum_i|b_i\rangle\langle b_i|v\rangle\).
- Born probabilities:
  \(\displaystyle P(i)=|\alpha_i|^2\).
- Normalization:
  \(\displaystyle \sum_i|\alpha_i|^2=\langle\psi|\psi\rangle=1\).
- Operator linearity:
  \(\displaystyle \hat L(\alpha|A\rangle+\beta|B\rangle)
  =\alpha\hat L|A\rangle+\beta\hat L|B\rangle\).

## Derivation Checks

1. The first position measurement supplies the recoil that invalidates the
   apparent velocity loophole.
2. The conjugated row, not the ket coordinate list, carries starred
   components.
3. Orthonormality collapses the coefficient sum through the Kronecker delta.
4. Coin normalization follows from total probability one and orthogonality of
   heads and tails.
5. Equal probabilities determine only amplitude magnitudes; arbitrary unit
   phases remain.
6. A fixed rotation preserves both scalar multiplication and vector
   addition, while length-squaring does not.

## Scope Boundaries

- The uncertainty relation remains an order-of-magnitude measurement argument,
  not the later sharp variance inequality.
- No matrix representation of an operator is introduced.
- No eigenvalue equation or self-adjointness condition is inferred before the
  lecture reaches it.
- The function-space example establishes infinite dimension, not a complete
  discussion of infinite-dimensional bases.
