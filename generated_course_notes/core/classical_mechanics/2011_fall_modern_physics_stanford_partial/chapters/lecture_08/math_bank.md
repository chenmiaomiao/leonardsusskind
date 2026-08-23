# Math Bank

## Electromagnetic Mechanics

\[
m\ddot{\mathbf x}=q\mathbf E+q\dot{\mathbf x}\times\mathbf B,
\qquad
\mathbf B=\nabla\times\mathbf A,
\qquad
\mathbf E=-\nabla V.
\]

\[
L=\frac12m\dot{\mathbf x}^{\,2}
  +q\mathbf A\cdot\dot{\mathbf x}-qV,
\qquad
\mathbf p=m\mathbf v+q\mathbf A.
\]

For a static gauge transformation,
\[
\mathbf A\mapsto\mathbf A+\nabla\lambda,
\qquad
L\mapsto L+q\frac{d\lambda}{dt}.
\]

\[
m\ddot x
=q(\partial_xA_y-\partial_yA_x)\dot y-q\partial_xV
=qB_z\dot y+qE_x.
\]

## Uniform Field and Guiding Center

With conventional z pointing out of the page,
\[
\mathbf B=-B\hat{\mathbf z},\quad B>0.
\]

\[
A_x=By,\ A_y=0
\quad\Longrightarrow\quad
p_x=m\dot x+qBy,
\]
\[
A_x=0,\ A_y=-Bx
\quad\Longrightarrow\quad
p_y=m\dot y-qBx.
\]

\[
\dot x=-\frac{qB}{m}y,\qquad
\dot y=\frac{qB}{m}x,\qquad
\omega_c=\frac{qB}{m}.
\]

For a circle centered at \((x_0,y_0)\),
\[
p_x=qBy_0,\qquad p_y=-qBx_0.
\]

For crossed fields,
\[
m\ddot x+qB\dot y=qE,\qquad
m\ddot y-qB\dot x=0,
\]
\[
\mathbf v_D=\frac{\mathbf E\times\mathbf B}{B^2},
\qquad v_{D,y}=\frac{E}{B}.
\]

\[
H=\frac{(\mathbf p-q\mathbf A)^2}{2m}+qV.
\]

## Poisson Brackets

\[
\{A,B\}=\sum_i\left(
\frac{\partial A}{\partial q_i}\frac{\partial B}{\partial p_i}
-\frac{\partial A}{\partial p_i}\frac{\partial B}{\partial q_i}
\right),
\qquad
\dot A=\{A,H\}.
\]

\[
\{q_i,p_j\}=\delta_{ij},\qquad
\{q_i,q_j\}=\{p_i,p_j\}=0.
\]

\[
\{P,F\}=-\frac{\partial F}{\partial Q},
\qquad
\{Q,F\}=\frac{\partial F}{\partial P}.
\]

\[
\{\alpha A+\beta C,B\}
=\alpha\{A,B\}+\beta\{C,B\},
\]
\[
\{AB,C\}=A\{B,C\}+B\{A,C\}.
\]

## Source-Sensitive Corrections

- The board changes orientation conventions while listing gauges. The chapter
  fixes one right-handed convention and checks every curl and force sign.
- The signed cyclotron frequency is qB/m for the convention used; its measured
  magnitude is abs(q)B/m.
- The drift is the E cross B drift and is independent of charge magnitude.
- For explicit time dependence, dA/dt equals partial A/partial t plus {A,H}.
