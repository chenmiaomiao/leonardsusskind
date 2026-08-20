# Math Bank

## Convention

Use $Y\sim Y+2\pi R$, where $R$ is the compactification radius. The lecture suppresses $2\pi$ and $\alpha'$ and often calls the compact size $r$. The published chapter restores the standard factors once, then relates them to the lecture units.

## Closed-String T-Duality

- Compact momentum:
  \[
  p_Y=\frac{n}{R},\qquad n\in\mathbb Z.
  \]
- Fundamental-string tension and winding energy:
  \[
  T_{\rm F}=\frac{1}{2\pi\alpha'},\qquad
  E_{\rm wind}=2\pi |w|RT_{\rm F}=\frac{|w|R}{\alpha'}.
  \]
- Radius inversion and quantum-number exchange:
  \[
  n\leftrightarrow w,\qquad R\leftrightarrow\widetilde R=\frac{\alpha'}{R}.
  \]
- Self-dual radius:
  \[
  R=\sqrt{\alpha'}.
  \]
- Worldsheet momentum and winding:
  \[
  P_Y=\frac{1}{2\pi\alpha'}\int_0^{2\pi}d\sigma\,\partial_\tau Y,
  \qquad
  w=\frac{1}{2\pi R}\int_0^{2\pi}d\sigma\,\partial_\sigma Y.
  \]
- Wound boundary condition:
  \[
  Y(\tau,\sigma+2\pi)=Y(\tau,\sigma)+2\pi wR.
  \]
- Derivative exchange:
  \[
  \partial_\tau Y\leftrightarrow\partial_\sigma\widetilde Y,
  \qquad
  \partial_\sigma Y\leftrightarrow\partial_\tau\widetilde Y.
  \]

## Reduced Spacetime Fields

- Five-dimensional metric decomposition:
  \[
  G_{MN}\longrightarrow\{G_{\mu\nu},G_{\mu5},G_{55}\}.
  \]
- Four-dimensional interpretation:
  \[
  G_{\mu5}=A_\mu,\qquad G_{55}=e^{2\varphi}.
  \]
- First level-matched closed-string excitation:
  \[
  \alpha_{-1}^{I}\widetilde\alpha_{-1}^{J}\ket{0;k}.
  \]
- Mixed vector states:
  \[
  \alpha_{-1}^{\mu}\widetilde\alpha_{-1}^{5}\ket{0;k},
  \qquad
  \alpha_{-1}^{5}\widetilde\alpha_{-1}^{\mu}\ket{0;k}.
  \]
- Symmetric and antisymmetric combinations:
  \[
  \alpha_{-1}^{(\mu}\widetilde\alpha_{-1}^{5)}\leftrightarrow G_{\mu5},
  \qquad
  \alpha_{-1}^{[\mu}\widetilde\alpha_{-1}^{5]}\leftrightarrow B_{\mu5}.
  \]
- Field exchange under T-duality:
  \[
  G_{\mu5}\leftrightarrow B_{\mu5}.
  \]

## Open Strings And D-Branes

- Neumann endpoint condition:
  \[
  \left.\partial_\sigma Y\right|_{\partial\Sigma}=0.
  \]
- T-dual Dirichlet condition:
  \[
  \left.\partial_\tau\widetilde Y\right|_{\partial\Sigma}=0,
  \qquad
  \left.\widetilde Y\right|_{\partial\Sigma}=Y_0.
  \]
- D-brane dimension in nine spatial dimensions with $k$ Dirichlet directions:
  \[
  p=9-k.
  \]
- D-string and fundamental-string tensions:
  \[
  T_{\rm D1}=\frac{1}{2\pi\alpha'g_s},
  \qquad
  T_{\rm F1}=\frac{1}{2\pi\alpha'}.
  \]

## Gauge Fields On Branes

- Chan--Paton matrix for $N$ coincident branes:
  \[
  A_\mu{}^i{}_j,\qquad i,j=1,\ldots,N.
  \]
- Endpoint composition:
  \[
  (R,G)\circ(G,B)\longrightarrow(R,B).
  \]
- Three-brane-stack algebra:
  \[
  \mathfrak u(3)=\mathfrak{su}(3)\oplus\mathfrak u(1).
  \]

## Qualifications

- $G_{55}$ is the radius modulus in this reduction, not automatically the ten-dimensional string dilaton.
- The oscillator formulas are standard reconstruction of a garbled spoken passage and remain explicitly schematic.
- Stable BPS D$p$-branes have even $p$ in type IIA and odd $p$ in type IIB; a circle T-duality changes $p$ by one and exchanges the two theories.
- A stack of three coincident D-branes gives $U(3)$, including a diagonal $U(1)$; the QCD octet is the traceless $SU(3)$ sector.
- Brane constructions motivate Yang--Mills and monopole physics but do not by themselves derive nonsupersymmetric QCD or the observed particle spectrum.
