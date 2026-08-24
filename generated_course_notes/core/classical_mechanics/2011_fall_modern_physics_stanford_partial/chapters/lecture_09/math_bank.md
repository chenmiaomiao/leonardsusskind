# Math Bank

## Poisson Algebra

\[
\{A,B\}=-\{B,A\},\qquad
\{\alpha A+\beta B,C\}=\alpha\{A,C\}+\beta\{B,C\},
\]
\[
\{AB,C\}=A\{B,C\}+B\{A,C\}.
\]

## Canonical Relations

\[
\{q_i,q_j\}=0,\qquad
\{p_i,p_j\}=0,\qquad
\{q_i,p_j\}=\delta_{ij}.
\]

\[
\{F(\bm q,\bm p),p_i\}=\frac{\partial F}{\partial q_i},
\qquad
\{q_i,F(\bm q,\bm p)\}=\frac{\partial F}{\partial p_i}.
\]

The monomial proof uses
\[
\{1,p\}=0,\qquad
\{q,p\}=1,\qquad
\{q^2,p\}=2q.
\]

## Hamiltonian Flow

\[
\dot A=\{A,H\}.
\]

For \(H=p^2/(2m)\),
\[
\dot p=0,\qquad \dot q=\frac{p}{m}.
\]

## Canonical Transformations

Noncanonical double stretch:
\[
Q=2q,\quad P=2p,\quad \{Q,P\}=4.
\]

Canonical squeeze:
\[
Q=2q,\quad P=\frac12p,\quad \{Q,P\}=1.
\]

Canonical rotation:
\[
P=\cos\theta\,p+\sin\theta\,q,\qquad
Q=-\sin\theta\,p+\cos\theta\,q.
\]

For several pairs the invariant object is
\[
\omega=\sum_i dq_i\wedge dp_i.
\]

## Generator Flow

\[
Q=q+\delta q,\qquad P=p+\delta p,
\]
\[
\{\delta q,p\}=-\{q,\delta p\}.
\]

\[
\delta q=\epsilon\{q,G\}
=\epsilon\frac{\partial G}{\partial p},
\qquad
\delta p=\epsilon\{p,G\}
=-\epsilon\frac{\partial G}{\partial q}.
\]

\[
\delta A=\epsilon\{A,G\}.
\]

The first-order canonical condition follows from equality of mixed partials.

## Symmetry and Conservation

\[
\delta H=\epsilon\{H,G\},\qquad
\{H,G\}=0
\quad\Longleftrightarrow\quad
\dot G=\{G,H\}=0.
\]

For the two-dimensional free particle,
\[
H=\frac{p_x^2+p_y^2}{2m},\qquad
G=L_z=xp_y-yp_x,
\]
\[
\{G,H\}
=\frac{1}{2m}(2p_xp_y-2p_xp_y)=0.
\]

If \(H_{\mathrm{rot}}=L_z\),
\[
\dot x=-y,\quad \dot y=x,\quad
\dot p_x=-p_y,\quad \dot p_y=p_x.
\]

For \(H=p^2/(2m)+U(q)\),
\[
\dot q=\frac{p}{m},\qquad
\dot p=-\frac{\partial U}{\partial q}.
\]
