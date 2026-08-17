# Mathematics Bank

## Core Relations

- Natural units: \(c=\hbar=1\), hence \([M]=L^{-1}\).
- Planck area: \(G_N=\ell_p^2\).
- Effective string--gravity scaling: \(G_N\sim g_s^2\ell_s^2\), so \(\ell_p\sim g_s\ell_s\).
- Long-string count: \(S_{\mathrm{str}}\sim L/\ell_s\).
- Long-string mass: \(M\sim L/\ell_s^2\).
- Long-string entropy: \(S_{\mathrm{str}}\sim M\ell_s\).
- Semiclassical black-hole entropy: \(S_{\mathrm{BH}}=A/(4G_N)\).
- Schwarzschild scaling: \(R_s\sim MG_N\), hence \(S_{\mathrm{BH}}\sim M^2G_N\).
- Isentrope at fixed \(\ell_s\): \(Mg_s=M_0g_{s,0}\).
- Correspondence curve: \(R_s\sim\ell_s\), or \(Mg_s^2\sim1/\ell_s\).
- Crossover result: \(M_*\ell_s\sim M_0^2g_{s,0}^2\ell_s^2\sim M_0^2G_{N,0}\).
- Ordinary cell count: \(\Omega=2^N\), \(S_{\max}=N\log2\sim V/V_{\mathrm{cell}}\).
- Gravitational maximum: \(S_{\max}=A/(4G_N)\).
- Flat expanding metric: \(ds^2=-dt^2+a(t)^2\delta_{ij}dx^idx^j\).
- Proper distance and recession: \(D=a\Delta x\), \(V=\dot D=HD\), \(H=\dot a/a\).
- Constant-H solution: \(a(t)=a_0e^{Ht}\), with characteristic scale \(H^{-1}\).

## Derivation Chain

1. From \(E=\hbar c/\lambda\) and \(E=mc^2\), setting \(c=\hbar=1\) gives \(m\sim1/\lambda\).
2. Newtonian dimensional bookkeeping, \(a\sim G_NM/R^2\), then gives \([G_N]=L^2\).
3. Two string interaction vertices supply \(g_s^2\); the string length supplies the missing area, yielding \(G_N\sim g_s^2\ell_s^2\).
4. A random walk of \(N=L/\ell_s\) steps has exponentially many configurations, so \(S_{\mathrm{str}}\sim N\).
5. Each step has mass \(1/\ell_s\), so \(M\sim(L/\ell_s)(1/\ell_s)\) and \(S_{\mathrm{str}}\sim M\ell_s\).
6. With \(A\sim R_s^2\) and \(R_s\sim MG_N\), the area law gives \(S_{\mathrm{BH}}\sim M^2G_N\).
7. Entropy depends on \(M\ell_p\sim Mg_s\ell_s\). At fixed \(\ell_s\), a reversible isentrope therefore keeps \(Mg_s\) fixed.
8. At the crossover, \(R_s\sim\ell_s\), giving \(Mg_s^2\sim1/\ell_s\).
9. Squaring the isentrope and dividing by the crossover equation gives \(M_*\ell_s\sim M_0^2G_{N,0}\), which is the target area-law scaling.
10. A shell that turns a region into a black hole cannot lower entropy, so the region's initial entropy is bounded by \(A/(4G_N)\).
11. Differentiating \(D(t)=a(t)\Delta x\) at fixed comoving separation gives \(V=(\dot a/a)D\).
12. If \(H=\dot a/a\) is constant, integration gives \(a(t)=a_0e^{Ht}\).

## Notation and Scope

- Use \(g_s\) for string coupling and \(G_N\) for Newton's constant.
- Use \(\ell_s\) and \(\ell_p\) for string and Planck lengths.
- Use \(M_0,g_{s,0}\) for the target black hole and \(M_*,g_{s,*}\) at crossover.
- Use \(\sim\) when numerical coefficients or compactification factors are suppressed.
- Reserve \(=\) for definitions and exact formulas, especially \(S_{\mathrm{BH}}=A/(4G_N)\).
- The relation \(G_N\sim g_s^2\ell_s^2\) is schematic for the effective four-dimensional setting.
- The neutral correspondence argument recovers scaling, not the exact coefficient \(1/4\).
- The shell argument is the spherical precursor to more general covariant entropy bounds.
- \(H^{-1}\) is generally a Hubble radius; it is a fixed event-horizon scale in the ideal de Sitter case developed here.
