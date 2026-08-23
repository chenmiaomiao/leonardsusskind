# Mathematical Content

## Calculus Tools

\[
\int_{t_1}^{t_2}\dot F(t)\,dt=F(t_2)-F(t_1)
\]

\[
\frac{d}{dt}(fg)=\dot f\,g+f\,\dot g
\]

\[
\int_{t_1}^{t_2}\dot f\,g\,dt
=[fg]_{t_1}^{t_2}
-\int_{t_1}^{t_2}f\,\dot g\,dt
\]

For \(f(t_1)=f(t_2)=0\),
\[
\int_{t_1}^{t_2}\dot f\,g\,dt
=-\int_{t_1}^{t_2}f\,\dot g\,dt.
\]

Fundamental lemma:
\[
\int_{t_1}^{t_2}a(t)f(t)\,dt=0
\quad\text{for arbitrary }f
\quad\Longrightarrow\quad
a(t)=0.
\]

## Variation

\[
q_i(t,\alpha)=\hat q_i(t)+\alpha f_i(t),
\qquad
f_i(t_1)=f_i(t_2)=0
\]

\[
A[q]=\int_{t_1}^{t_2}L(q,\dot q,t)\,dt,
\qquad
\left.\frac{dA}{d\alpha}\right|_{\alpha=0}=0
\]

\[
\frac{\partial q_i}{\partial\alpha}=f_i,
\qquad
\frac{\partial\dot q_i}{\partial\alpha}=\dot f_i
\]

\[
\frac{dA}{d\alpha}
=
\int_{t_1}^{t_2}\sum_i
\left(
\frac{\partial L}{\partial q_i}f_i
+
\frac{\partial L}{\partial\dot q_i}\dot f_i
\right)dt
\]

\[
\delta A
=
\int_{t_1}^{t_2}\sum_i
\left[
\frac{\partial L}{\partial q_i}
-
\frac{d}{dt}
\left(\frac{\partial L}{\partial\dot q_i}\right)
\right]f_i\,dt
\]

\[
\boxed{
\frac{d}{dt}
\left(\frac{\partial L}{\partial\dot q_i}\right)
=
\frac{\partial L}{\partial q_i}
}
\]

## Momentum and Force

\[
\pi_i=\frac{\partial L}{\partial\dot q_i},
\qquad
\dot\pi_i=\frac{\partial L}{\partial q_i}
\]

For one particle,
\[
L=\frac12m\dot x^2-U(x),
\qquad
m\ddot x=-\frac{dU}{dx}.
\]

For many Cartesian coordinates,
\[
L=\sum_i\frac12m_i\dot x_i^2-U(x_1,\ldots,x_n),
\qquad
\dot p_i=-\frac{\partial U}{\partial x_i}.
\]

## Translation Symmetry

\[
L=
\frac12m_1\dot x_1^2+
\frac12m_2\dot x_2^2-
U(x_1-x_2)
\]

With \(d=x_1-x_2\),
\[
\frac{\partial U}{\partial x_1}=\frac{dU}{dd},
\qquad
\frac{\partial U}{\partial x_2}=-\frac{dU}{dd}.
\]

\[
\frac{d}{dt}(p_1+p_2)=0.
\]

## Near-Earth Motion

\[
L=\frac12m\dot x^2+\frac12m\dot y^2-mgy
\]

\[
\frac{d}{dt}(m\dot x)=0,
\qquad
\frac{d}{dt}(m\dot y)=-mg.
\]

\[
U\mapsto U+C
\quad\Longrightarrow\quad
-\frac{d(U+C)}{dq}=-\frac{dU}{dq}.
\]

## Polar Coordinates

\[
v_r=\dot r,
\qquad
v_\perp=r\dot\theta
\]

\[
L=
\frac12m\dot r^2+
\frac12mr^2\dot\theta^2-
U(r)
\]

The complete radial equation is
\[
m\ddot r=mr\dot\theta^2-\frac{dU}{dr}.
\]
The \(mr\dot\theta^2\) term is required by the displayed Lagrangian even
though an isolated board line in the source omits it.

\[
p_\theta=mr^2\dot\theta=\ell,
\qquad
\frac{d\ell}{dt}=0,
\qquad
\dot\theta=\frac{\ell}{mr^2}.
\]
