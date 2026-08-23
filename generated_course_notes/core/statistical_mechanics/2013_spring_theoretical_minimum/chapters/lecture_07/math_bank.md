# Math Bank
## Core Equations
- [transcript-backed] \( \frac{3}{2}k_B T = \frac{1}{2} m \langle v^2\rangle \)
- [transcript-backed] \( \langle v^2\rangle = \frac{3k_B T}{m} \)
- [standard reconstruction] \( v_s^2 = \frac{\partial P}{\partial \rho_{\mathrm{mass}}} = \frac{1}{m}\frac{\partial P}{\partial \rho} \)
- [transcript-backed] \( PV = N k_B T \)
- [transcript-backed] \( P = \rho k_B T \)
- [transcript-backed] \( v_s^2 = \frac{k_B T}{m} \) for the ideal-gas formula used in the lecture comparison
- [standard thermodynamic correction] \( c_s^2 = \left(\frac{\partial P}{\partial \rho_{\mathrm{mass}}}\right)_S = \gamma\frac{k_B T}{m} \) for an ideal gas
- [transcript-backed] \( H(x,p) = \frac{p^2}{2m} + \frac{\kappa x^2}{2} \)
- [transcript-backed] \( e^{-\beta H} = e^{-\beta p^2/2m}\, e^{-\beta \kappa x^2/2} \)
- [transcript-backed] \( Z_{\mathrm{cl}} = \int dp\,dx\, e^{-\beta H(x,p)} \)
- [transcript-backed] \( q^2 = \frac{\beta p^2}{2m} \)
- [transcript-backed] \( y^2 = \frac{\beta \kappa x^2}{2} \)
- [standard reconstruction] \( \omega = \sqrt{\frac{\kappa}{m}} \)
- [standard reconstruction] \( Z_{\mathrm{cl}} = \frac{2\pi}{\omega}\,\frac{1}{\beta} \) up to irrelevant multiplicative constants
- [standard phase-space normalization] \( Z_{\mathrm{cl}} = \frac{1}{\beta\hbar\omega} \)
- [standard reconstruction] \( \log Z_{\mathrm{cl}} = \text{const} - \log \beta \)
- [visible] \( E = -\frac{\partial \log Z}{\partial \beta} = \frac{1}{\beta} = T \)
- [transcript-backed] \( \langle K\rangle = \langle U\rangle = \frac{1}{2\beta} = \frac{T}{2} \)
- [standard equipartition consequence] \( \langle p^2\rangle=mT \), \( \langle x^2\rangle=T/\kappa \), and \( \langle \dot{x}^2\rangle=T/m \)
- [transcript-backed] \( E_n = n\hbar\omega \) in the lecture convention before the zero-point correction is discussed
- [transcript-backed] \( Z_{\mathrm{q}} = \sum_{n=0}^{\infty} e^{-\beta n\hbar\omega} \)
- [transcript-backed] \( \sum_{n=0}^{\infty} x^n = \frac{1}{1-x} \)
- [transcript-backed] \( Z_{\mathrm{q}} = \frac{1}{1-e^{-\beta\hbar\omega}} \)
- [transcript-backed] \( E = -\frac{\partial \log Z_{\mathrm{q}}}{\partial \beta} = -\frac{1}{Z_{\mathrm{q}}}\frac{\partial Z_{\mathrm{q}}}{\partial \beta} \)
- [transcript-backed] \( E = \hbar\omega\,\frac{e^{-\beta\hbar\omega}}{1-e^{-\beta\hbar\omega}} \)
- [standard reconstruction] \( E = \frac{\hbar\omega}{e^{\beta\hbar\omega}-1} \)
- [standard zero-point restoration] \( E_n=(n+\tfrac12)\hbar\omega \) and \( E_{\mathrm{phys}}=\hbar\omega/2+\hbar\omega/(e^{\beta\hbar\omega}-1) \)
- [transcript-backed] \( \beta \hbar \omega \ll 1 \Rightarrow E \approx \frac{1}{\beta} = T \)
- [transcript-backed] \( \beta \hbar \omega \gg 1 \Rightarrow E \approx \hbar\omega\, e^{-\beta\hbar\omega} \)
- [transcript-backed] \( \beta \hbar \omega \sim 1 \)
- [transcript-backed] \( T \sim \hbar\omega \)
- [transcript-backed] \( Z_{\mathrm{tot}} = \prod_i Z_i \), so \( \log Z_{\mathrm{tot}} = \sum_i \log Z_i \)
- [transcript-backed] \( E_{\mathrm{tot}} = \sum_i E_i \)
- [standard reconstruction] \( S_{\mathrm{fine}} = -\int d\Gamma\,f\log f = \log \Omega_A \) for a uniform distribution on a phase-space patch
- [transcript-backed] \( V_{\mathrm{blob}}(t) = \text{const} \) under Liouville evolution
- [standard reconstruction] \( S_{\mathrm{cg}} \propto \log V_{\mathrm{coarse}} \) with \( V_{\mathrm{coarse}} \ge V_{\mathrm{blob}} \)
- [standard reconstruction] Recurrence is to an \(\epsilon\)-neighborhood, not necessarily to the exact initial point
- [standard dynamical-systems formulation] \( \lVert\delta\Gamma(t)\rVert\sim e^{\lambda t}\lVert\delta\Gamma(0)\rVert \) for a positive Lyapunov exponent

## Definitions And Objects
- \(T\): temperature.
- \(\beta\): inverse temperature; after the gas example the lecture suppresses \(k_B\), so \(\beta = 1/T\) in lecture units.
- \(k_B\): Boltzmann constant, kept explicitly only in the gas numerology.
- \(\rho\): particle number density, \(\rho = N/V\).
- \(\rho_{\mathrm{mass}}\): mass density, \(\rho_{\mathrm{mass}} = m\rho\).
- \(v_s\): speed of sound.
- \(H\): Hamiltonian/energy function.
- \(x,p\): one-dimensional oscillator coordinate and momentum.
- \(m\): oscillator mass or single-particle mass, depending on context.
- \(\kappa\): spring constant; use this in the notes to avoid conflict with \(k_B\).
- \(\omega\): oscillator frequency, \(\omega = \sqrt{\kappa/m}\).
- \(Z\): partition function.
- \(K,U\): kinetic and potential energy contributions of the oscillator.
- \(n\): quantum oscillator level index.
- \(\hbar\omega\): one quantum of oscillator energy.
- Heat bath: external environment fixing the temperature of the subsystem.
- Phase-space blob: occupied region representing partial knowledge of the system.
- Microscopic entropy: entropy attached to the exact evolved probability distribution.
- Coarse-grained entropy: entropy after finite resolution replaces thin filamentary structure by finite blobs.
- Chaos: exponential separation of nearby trajectories; the lecture later ties this to Lyapunov growth.
- Recurrence: eventual return of the phase point to an \(\epsilon\)-neighborhood of its starting configuration in a finite accessible phase-space region.

## Derivation Steps
Speed-of-sound estimate
1. Start from equipartition for one gas molecule: \( \frac{3}{2}k_B T = \frac{1}{2}m\langle v^2\rangle \).
2. Solve for the molecular speed scale: \( \langle v^2\rangle = 3k_B T/m \).
3. Use this only as a heuristic estimate for how fast an overdensity spreads in a very dilute gas.
4. Introduce the more formal sound-speed formula \( v_s^2 = \partial P/\partial \rho_{\mathrm{mass}} \).
5. Rewrite mass density as \( \rho_{\mathrm{mass}} = m\rho \), so \( v_s^2 = (1/m)\,\partial P/\partial \rho \).
6. Insert the ideal-gas law \( P=\rho k_B T \) at fixed \(T\).
7. Differentiate to get \( \partial P/\partial \rho = k_B T \).
8. Conclude \( v_s^2 = k_B T/m \), differing from the naive molecular-speed estimate by a factor of \(3\) in \(v^2\).

Classical harmonic oscillator
1. Write the one-dimensional Hamiltonian \( H = p^2/(2m) + \kappa x^2/2 \).
2. Form the Boltzmann weight \( e^{-\beta H} \) and factor it into momentum and position pieces.
3. Write the partition function as \( Z_{\mathrm{cl}} = \int dp\,dx\, e^{-\beta p^2/2m} e^{-\beta \kappa x^2/2} \).
4. Separate the integral into a \(p\)-integral and an \(x\)-integral.
5. Change variables in the momentum integral using \( q^2 = \beta p^2/(2m) \), so \( dp \propto \sqrt{2m/\beta}\,dq \).
6. Recognize the remaining integral as Gaussian, contributing only an irrelevant numerical constant times \( \beta^{-1/2} \).
7. Change variables in the position integral using \( y^2 = \beta \kappa x^2/2 \), so \( dx \propto \sqrt{2/(\beta\kappa)}\,dy \).
8. Recognize the second Gaussian, contributing another irrelevant constant times \( \beta^{-1/2} \).
9. Multiply the two factors to get \( Z_{\mathrm{cl}} \propto \sqrt{m/\kappa}\,\beta^{-1} = \omega^{-1}\beta^{-1} \).
10. Write \( \log Z_{\mathrm{cl}} = \text{const} - \log \beta \).
11. Differentiate: \( E = -\partial_\beta \log Z_{\mathrm{cl}} = 1/\beta = T \).
12. Read off equipartition by contribution: each quadratic Gaussian gives \(T/2\), hence \( \langle K\rangle = \langle U\rangle = T/2 \).

Quantum harmonic oscillator
1. Replace the classical continuum by discrete levels \( E_n = n\hbar\omega \) in the lecture convention.
2. Write the quantum partition function \( Z_{\mathrm{q}} = \sum_{n=0}^\infty e^{-\beta n\hbar\omega} \).
3. Set \( x = e^{-\beta\hbar\omega} \) and sum the geometric series.
4. Obtain \( Z_{\mathrm{q}} = 1/(1-e^{-\beta\hbar\omega}) \).
5. Compute the energy from \( E = -\partial_\beta \log Z_{\mathrm{q}} \) or equivalently \( E = -(1/Z_{\mathrm{q}})\,\partial_\beta Z_{\mathrm{q}} \).
6. Differentiate and simplify to \( E = \hbar\omega\, e^{-\beta\hbar\omega}/(1-e^{-\beta\hbar\omega}) \).
7. Take the high-temperature limit \( \beta\hbar\omega \ll 1 \) by expanding the exponential.
8. Recover the classical result \( E \approx 1/\beta = T \).
9. Take the low-temperature limit \( \beta\hbar\omega \gg 1 \), so the exponential is tiny.
10. Obtain \( E \approx \hbar\omega\, e^{-\beta\hbar\omega} \), exponentially small in the lecture convention.

Crossover and activated degrees of freedom
1. Identify the crossover where the exponential ceases to be clearly small or close to one.
2. Set \( \beta\hbar\omega \sim 1 \).
3. Rewrite as \( T \sim \hbar\omega \).
4. Interpret this as the temperature at which the classical oscillator energy reaches one quantum.
5. Conclude that modes with \( \hbar\omega \gg T \) are frozen out.
6. For many oscillators, multiply partition functions and add logarithms.
7. Conclude that only oscillators below the thermal threshold contribute appreciably to the energy.

Phase-space entropy and coarse-graining
1. Begin with a uniform probability distribution over a phase-space blob.
2. Associate entropy with the size of that occupied region.
3. Evolve the blob under Hamiltonian dynamics.
4. Use Liouville’s theorem to keep the exact microscopic phase-space volume fixed.
5. Allow the blob to stretch into thin filaments or a “snake.”
6. Introduce finite resolution: nearby points cannot be distinguished.
7. Replace the filamentary set by coarse-grained blobs.
8. Observe that the coarse-grained occupied volume grows even though the exact volume does not.
9. Define the increasing entropy as the coarse-grained entropy, not the exact microscopic one.
10. Connect the repeated filamentation to chaos.
11. Keep recurrence: in a finite accessible region, return to an \(\epsilon\)-neighborhood occurs after a finite but typically enormous time.
12. State the lecture’s final form cautiously: entropy does not literally always increase; higher-entropy future configurations are overwhelmingly more probable.

## Notation Choices
- Use \(k_B\) for Boltzmann’s constant everywhere it is explicit.
- Use \(\kappa\) for the spring constant, not \(k\).
- Use \(N\) for the number of gas particles in the ideal-gas law; reserve \(n\) for the quantum oscillator level.
- Use \(\rho\) for particle number density and \(\rho_{\mathrm{mass}}=m\rho\) for mass density.
- Use \(v_s\) for speed of sound; do not preserve the garbled “\(E^2\)” or “speed of light” readings from the transcript.
- Use \(H(x,p)\) for the oscillator Hamiltonian and \(E\) for the thermal average energy obtained from \( -\partial_\beta \log Z \).
- Use \(K\) and \(U\) for kinetic and potential pieces when stating equipartition.
- Use \(\omega=\sqrt{\kappa/m}\) consistently.
- Use \(\beta=1/T\) after the lecture drops \(k_B\); if needed in a more standard convention, note that the lecture has already absorbed \(k_B\).
- Use \(Z_{\mathrm{cl}}\) and \(Z_{\mathrm{q}}\) when the chapter needs to distinguish classical and quantum partition functions.
- Use \(S_{\mathrm{micro}}\) and \(S_{\mathrm{cg}}\) as clarifying labels in the notes, even though the lecture speaks informally of “microentropy.”
- Use \(\epsilon\) for recurrence tolerance and for finite-resolution statements in phase space.

## Uncertain Mathematics
- The board line above the visible energy formula is only partially readable; typeset \( \log Z = \text{const} - \log \beta \) as a cautious reconstruction, not a literal full transcription from the screenshot alone.
- The speed-of-sound discussion is approximate and somewhat tentative. Preserve the fixed-temperature board estimate, then distinguish it from the standard adiabatic derivative used for ordinary sound.
- The factor-of-\(\sqrt{3}\) mismatch between the naive molecular-speed estimate and the fixed-temperature formula is left as a live issue in the source. Keep that comparison while explaining the separate adiabatic factor \(\gamma\).
- The lecture briefly says each kinetic/potential contribution is “one half beta”; the intended mathematics is \(1/(2\beta)=T/2\).
- The entropy sign is verbally unstable around the blob discussion. The mathematically usable form for the notes is \(S \propto \log V_{\mathrm{blob}}\), not minus that quantity.
- The garbled transcript around \(01{:}30{:}20\)–\(01{:}31{:}00\) should not be reconstructed in detail beyond the clear nearby claims: nearby trajectories separate, filamentation develops, and coarse-graining fills the accessible region.
- The quantum oscillator uses \(E_n=n\hbar\omega\) until a later audience question raises the missing zero-point term. If the final notes mention the physical spectrum \(E_n=(n+\tfrac12)\hbar\omega\), they should also explain why the lecture could ignore the additive constant in thermodynamic derivatives.
- The low-temperature statement “energy is almost zero” is only correct in the lecture’s shifted-energy convention. It should not be conflated with the full physical oscillator energy including zero-point motion.
- The lecture’s classical-to-quantum comparison via phase-space integrals is motivational, not a full rigorous state-counting proof.
