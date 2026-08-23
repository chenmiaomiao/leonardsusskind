# Lecture 9 Mathematics

## One Spin

\[
\sigma=\pm1,\qquad E=-J\sigma,\qquad
z=2\cosh(\beta J).
\]

\[
\langle E\rangle=-\partial_\beta\log z=-J\tanh(\beta J),
\qquad
\langle\sigma\rangle=\tanh(\beta J).
\]

## Exact Open Chain

\[
H=-J\sum_{i=1}^{N-1}\sigma_i\sigma_{i+1},\qquad
\mu_i=\sigma_i\sigma_{i+1}.
\]

\[
Z_N=2\left[2\cosh(\beta J)\right]^{N-1},
\qquad
\langle\mu_i\rangle=\tanh(\beta J).
\]

If \(p_{\rm same}\) is the probability that neighboring spins agree,

\[
2p_{\rm same}-1=\langle\mu_i\rangle=\tanh(\beta J),
\qquad
p_{\rm same}=\frac{1+\tanh(\beta J)}{2}.
\]

For a separation of \(r\) bonds,

\[
C(r)=\langle\sigma_i\sigma_{i+r}\rangle
=\left[\tanh(\beta J)\right]^r
=e^{-r/\xi},
\qquad
\xi^{-1}=-\log\tanh(\beta J).
\]

At low temperature, \(\xi\simeq \tfrac12 e^{2\beta J}\).

## Mean Field

\[
H_i^{\rm MF}=-2dJm\,\sigma_i,\qquad
m=\tanh(2\beta dJm).
\]

With \(y=2\beta dJm\),

\[
\frac{y}{2\beta dJ}=\tanh y,\qquad
T_c^{\rm MF}=2dJ
\quad (k_B=1).
\]

A convenient mean-field free-energy density is

\[
f_{\rm MF}(m)=dJm^2-\frac1\beta
\log\!\left[2\cosh(2\beta dJm)\right].
\]

Near the transition the nonzero solution has the mean-field square-root onset

\[
m^2\simeq
\frac{3\left[(2\beta dJ)^2-1\right]}{(2\beta dJ)^3}.
\]

## Domains and an External Field

Each broken ferromagnetic bond costs \(2J\). On a square lattice, one isolated flip breaks four bonds and costs \(8J\); two adjacent flips break six bonds and cost \(12J\). In one dimension, any nonempty reversed interval has two walls and costs \(4J\), independent of its length.

\[
H_i^{\rm MF}(h)=-(2dJm+h)\sigma_i,\qquad
m=\tanh\!\left[\beta(2dJm+h)\right].
\]

\[
m\simeq\frac{\beta h}{1-2\beta dJ}
\quad\text{at high temperature},\qquad
\lim_{h\to0^+}\lim_{N\to\infty}m_N(h)>0
\quad\text{below the ordered transition}.
\]
