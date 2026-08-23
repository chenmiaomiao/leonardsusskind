# Mathematics Bank

## Discrete State Laws

- Stroboscopic update: (q_n\mapsto q_{n+1}).
- Coin phase space: (\Gamma=\{H,T\}).
- Identity: (H\mapsto H\), (T\mapsto T).
- Alternation: (H\mapsto T\), (T\mapsto H).
- Six-cycle: (1\mapsto2\mapsto3\mapsto4\mapsto5\mapsto6\mapsto1).
- Reversible finite update: a bijection (\sigma:\Gamma\to\Gamma), equivalently one in-arrow and one out-arrow per state.
- Infinite translation: (n\mapsto n+1), (n\in\mathbb Z).

## Conservation and Phase Space

- Component label: (C(q_{n+1})=C(q_n)).
- Particle state on a line: ((x,v)), with (v=\dot x).
- Canonical alternative for fixed mass: ((x,p)), (p=mv).
- Three-dimensional particle: six state coordinates.

## Differential-Equation Order

- Dot notation: (\dot x=dx/dt), (\ddot x=d^2x/dt^2).
- Schematic first-order law: (F(x)=m\dot x).
- Chain rule: (dF/dt=F'(x)\dot x=m\ddot x).
- Newton's law: (F(x)=m\ddot x).
- Phase-space form: (\dot x=v), (\dot v=F(x)/m).
- A third-order law would require ((x,\dot x,\ddot x)) as independent state data.

## Two-Step Coin Rule

- Pair state space: (\Gamma_2=\{HH,HT,TH,TT\}).
- Shift update: ((a_n,a_{n+1})\mapsto(a_{n+1},f(a_n,a_{n+1}))).
- Completed rule: (HH\mapsto HH), (HT\mapsto TT), (TT\mapsto TH), (TH\mapsto HT).
- With (H=0,T=1): (a_{n+2}=a_n+a_{n+1}\pmod2).
- Matrix reconstruction:
  \[
  \binom{a_{n+1}}{a_{n+2}}
  =\begin{pmatrix}0&1\\1&1\end{pmatrix}
  \binom{a_n}{a_{n+1}}\pmod2.
  \]
  Its determinant is nonzero modulo two, so the pair update is invertible.

## Source Repairs

- Normalize the isolated “sixteen states” ASR error to six states for a die.
- Normalize negative velocity to motion toward decreasing (x).
- Treat the phony first-order law as schematic and preserve its pedagogical role.
- Use the final corrected truth table rather than any abandoned intermediate row.
