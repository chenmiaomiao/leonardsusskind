# Figure Descriptions: Lecture 9

## Source Frames

- lecture_09_figure_01.png (00:05:10): The left side retains spin-state transitions; the central board decomposes the initial electron state into singlet and \(m=0\) triplet components; the right side records the radiation vacuum and emitted-photon states. This is the visual anchor for linear evolution into a superposition of photon-number sectors.
- lecture_09_figure_02.png (00:14:35): Two reciprocal equations show \(\psi(x)\) as a superposition of plane waves and \(\widetilde\psi(p)\) as the inverse transform. Their matching \(1/\sqrt{2\pi}\) factors make the symmetry explicit.
- lecture_09_figure_03.png (00:19:45): The board isolates \(\int dx\,\delta(x-x')f(x)=f(x')\). The lecturer points at the sampled value, but the full identity remains legible.
- lecture_09_figure_04.png (00:26:23): A boxed inner \(p\)-integral sits inside the reconstruction of \(\psi(x')\). The next line replaces that kernel with a delta-like symbol, exactly at the step where the Fourier representation is recognized.
- lecture_09_figure_05.png (00:35:30): A general ket is written as \(\int dx\,\psi(x)|x\rangle\), followed by \(\langle x|\psi\rangle=\psi(x)\). The two lines visibly connect expansion coefficients with projections.
- lecture_09_figure_06.png (00:41:20): The board displays \(\langle x'|x\rangle=\delta(x-x')\) and the continuous wave-function inner product. These formulas close the position-basis construction.
- lecture_09_figure_07.png (00:45:50): Multiplication by \(x\) is applied to a delta-localized wave function, giving \(x\delta(x-x_0)=x_0\delta(x-x_0)\). The board makes the generalized position eigenfunction concrete.
- lecture_09_figure_08.png (00:51:45): The plane wave \(\psi_p(x)=e^{ipx/\hbar}\) is written as the solution of the momentum eigenvalue equation. The phase and momentum label are clear.
- lecture_09_figure_09.png (01:05:50): Projection onto \(|p\rangle\) is expanded through the position basis, yielding the Fourier integral for \(\widetilde\psi(p)\). The frame documents the central identification of the two representations.
- lecture_09_figure_10.png (01:17:45): The time-dependent Schrodinger equation appears above \(H=cP\), marking the pivot from representation to dynamics.
- lecture_09_figure_11.png (01:20:05): The board reduces the Schrodinger equation to \(\partial_t\psi=-c\,\partial_x\psi\), with the equivalent transport form immediately below.
- lecture_09_figure_12.png (01:25:20): For \(H=cp\), Hamilton's equations give \(\dot x=c\) and \(\dot p=0\). Quantum and classical motion can therefore be compared without extra assumptions.
- lecture_09_figure_13.png (01:33:50): The free-particle equation \(i\hbar\partial_t\psi=-(\hbar^2/2m)\partial_x^2\psi\) is written cleanly after substituting \(P=-i\hbar\partial_x\).

## Placement And Interpretation

The figures follow the same order as the lecture and sit immediately after the corresponding mathematical construction. Each screenshot is accompanied by a complete typeset equation, because documentary board images should preserve the lecture's visual development without forcing the reader to decipher chalk. No TikZ redraw is needed: these frames document equations and board organization rather than geometric diagrams.

## Uncertainty Notes

- The photon-emission frame contains hurried transition arrows; only the state relations independently supported by the transcript are reconstructed.
- The Fourier-kernel frame briefly uses a provisional capital-delta-like symbol. The final notes use the standard Dirac \(\delta\) after the kernel's sampling property is established.
- Continuum plane waves are generalized eigenstates. Their normalization is stated distributionally and checked through the finite-box argument retained from the lecture.
- The late dynamics frames omit some canceled constants on the board. The typeset equations retain \(\hbar\) consistently and reproduce only the standard equations explicitly reached in the lecture.
