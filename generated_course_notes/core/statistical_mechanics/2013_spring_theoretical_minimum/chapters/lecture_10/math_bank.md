# Lecture 10 Mathematics Bank

## Ising Model

\[
\mathcal H=-J\sum_{\langle ij\rangle}\sigma_i\sigma_j+h\sum_i\sigma_i,
\qquad \sigma_i=\pm1.
\]

\[
\Delta E_{\rm broken\ bond}=2J,
\qquad N_{\rm links}=dN.
\]

With the chosen sign convention, \(h>0\) favors \(\sigma=-1\).

## Mean Field

\[
\mathcal H_{\rm mf}(\sigma)=(-2dJm+h)\sigma,
\qquad
m=\tanh[\beta(2dJm-h)].
\]

\[
y=2\beta dJm,
\qquad
\frac{yT}{2dJ}=\tanh(y-\beta h).
\]

At \(h=0\), tangency at the origin gives

\[
T_c^{\rm MF}=2dJ.
\]

Near the transition,

\[
\tanh y=y-\frac{y^3}{3}+\cdots,
\qquad
m\propto(T_c-T)^{1/2}.
\]

## Grand Canonical Ensemble

\[
\Xi(T,\mu)=\sum_{N=0}^{\infty}\sum_{\mathcal C_N}
\exp[-\beta E(\mathcal C_N)+\beta\mu N].
\]

## Lattice-Gas Dictionary

\[
n_i=\frac{1+\sigma_i}{2},
\qquad
\rho=\langle n_i\rangle=\frac{1+m}{2}.
\]

\[
\mathcal H
=-4J\sum_{\langle ij\rangle}n_in_j
+(4dJ+2h)\sum_i n_i+\text{constant}.
\]

Comparing with

\[
\mathcal H_{\rm lg}
=-\epsilon\sum_{\langle ij\rangle}n_in_j-\mu\sum_i n_i+\text{constant}
\]

gives

\[
\epsilon=4J,
\qquad
\mu=-(4dJ+2h),
\qquad
\mu_{\rm coex}=-4dJ.
\]

In two dimensions, one isolated particle costs \(8J\), two distant particles cost \(16J\), and an adjacent pair costs \(12J\). The nearest-neighbor attraction is therefore \(4J\).

## Critical Scaling

\[
t=\frac{T-T_c}{T_c},
\qquad
m\sim(-t)^{\beta_{\rm crit}},
\qquad
\chi\sim|t|^{-\gamma},
\qquad
\xi\sim|t|^{-\nu}.
\]

Mean field gives \(\beta_{\rm crit}=1/2\); fluctuation-corrected exponents depend on the universality class.

## Postlecture Quantitative Relations

Atomic scales used to clarify parameter sensitivity:

\[
E_{\rm atom}\sim\alpha^2m_e,
\qquad
a_0\sim(\alpha m_e)^{-1},
\]

in units \(\hbar=c=1\). These are contextual additions consistent with the discussion, not equations written on the board.
