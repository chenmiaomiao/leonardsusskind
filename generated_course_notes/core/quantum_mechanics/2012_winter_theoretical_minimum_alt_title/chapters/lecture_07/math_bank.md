# Mathematics Bank

## State Coordinates

\[
\psi(a,b,c,\ldots)=\langle a,b,c,\ldots|\Psi\rangle,
\qquad
|\Psi\rangle=\sum_{a,b,c,\ldots}\psi(a,b,c,\ldots)|a,b,c,\ldots\rangle.
\]

## Local Observables

\[
L_A=L\otimes I_B,
\qquad
M_B=I_A\otimes M,
\]
\[
\langle L_A\rangle
=\sum_{a',a,b}\Psi^*(a',b)L_{a'a}\Psi(a,b).
\]

For \(\Psi(a,b)=\psi_A(a)\phi_B(b)\),
\[
\langle L_A M_B\rangle
=\langle L_A\rangle\langle M_B\rangle.
\]

## Singlet

\[
|S\rangle=\frac{|ud\rangle-|du\rangle}{\sqrt2},
\qquad
\langle\sigma_i\rangle=\langle\tau_i\rangle=0,
\qquad
\langle\sigma_i\tau_j\rangle=-\delta_{ij}.
\]
\[
(\boldsymbol{\sigma}\cdot\boldsymbol{\tau})|S\rangle=-3|S\rangle,
\]
while each triplet has eigenvalue \(+1\).

## Reduced Density Matrix

\[
(\rho_A)_{aa'}=\sum_b\Psi(a,b)\Psi^*(a',b),
\qquad
\rho_A=\operatorname{Tr}_B|\Psi\rangle\langle\Psi|.
\]
\[
\langle L_A\rangle=\operatorname{Tr}_A(\rho_A L).
\]

For a product pure state,
\[
\rho_A=|\psi_A\rangle\langle\psi_A|,
\qquad
\operatorname{spec}(\rho_A)=\{1,0,\ldots\}.
\]
For the singlet,
\[
\rho_A=\frac12 I,
\qquad
\operatorname{spec}(\rho_A)=\left\{\frac12,\frac12\right\}.
\]
\[
S(\rho_A)=-\operatorname{Tr}(\rho_A\log\rho_A).
\]

## Measurement and Locality

\[
|u,0\rangle\to|u,1\rangle,
\qquad
|d,0\rangle\to|d,0\rangle,
\]
\[
(\alpha|u\rangle+\beta|d\rangle)|0\rangle
\to\alpha|u,1\rangle+\beta|d,0\rangle.
\]

For an unconditioned Bob-local channel,
\[
\rho'_A
=\operatorname{Tr}_B\sum_\mu
(I\otimes K_\mu)\rho_{AB}(I\otimes K_\mu^\dagger)
=\rho_A.
\]

## Qualifications

- Connected correlation is an entanglement witness for pure states, not for every mixed state.
- Equal reduced eigenvalues imply maximal entanglement only across the full smaller subsystem.
- Local tomography needs an ensemble of identically prepared copies.
- A global classical simulator is possible in principle; Bell excludes a separated local simulation satisfying Bell's assumptions.
