# Lecture 6 Editorial Audit

## Result

**Pass.** The chapter follows the complete 1:24:23 recording in chronological
order and maps 67 substantive source beats. Eight source-limited intervals
are identified explicitly. Completed board states and the declared metric
convention secure the formulas wherever the spoken derivation contains false
starts or sign corrections.

## Coverage

- The opening fermionic-string recap and compactification deferral lead into
  the experimental meaning of a scattering amplitude.
- Four-momentum, the mostly-plus mass shell, all-incoming notation,
  center-of-mass reduction, Mandelstam variables, and their equal-mass
  constraint are derived in the lecture's order.
- Direct, crossed, and third-channel poles retain their angular
  interpretation before the historical meson problem introduces the
  Veneziano amplitude and channel duality.
- The string mechanism retains the open-string interval, worldsheet wave
  equation, discrete chain, endpoint joining, product wavefunction,
  propagation, final projection, and integral over the joined lifetime.
- The change of variables (z=e^{-\tau}) is carried through to the Euler
  beta function with consistent exponent signs, followed by every closing
  question and the photon/graviton interaction test.

## Evidence

- 12 classroom exchanges appear in dedicated Q&A blocks.
- 13 source frames were checked at their listed video times.
- One clean TikZ join-propagate-split diagram accompanies rather than
  replaces the original board frame.
- Three modern qualifications are visibly labeled as editorial material.

## Build

- `latexmk` completed repeated `pdflatex` passes successfully.
- The PDF contains 16 letter-size pages and passes `qpdf --check`.
- The final log contains no overfull boxes, unresolved references, package
  warnings, or LaTeX errors.
- Every page was rendered and reviewed for margins, chronology, figure
  legibility, equation placement, captions, timestamps, and header fit.
