# Visual Evidence

## Selection Result

Twenty frames were selected from the 1:47:48 source video. They cover every board-dependent transition in the chapter: orientation, both winding reconnections, the two spectra, worldsheet integrals, pair production, dimensional reduction, oscillator states, open-string boundary conditions, representative D-branes, brane-stack color labels, and the D-string monopole.

The final inventory and image-by-image descriptions are in `figures_markdown.md`. Machine-readable timestamps and verdicts are in `metadata.json` and `editorial_fidelity.json`.

## Evidence Rules

- A frame is included only where its visible board content matches the surrounding transcript interval.
- The timestamp marks the actual source state, not a later moment when an old board happened to remain visible.
- An incomplete equation is never silently completed in the caption. The clean TeX equation appears in the body and states its normalization.
- A redraw is paired with the source frame when geometry is meaningful but board occlusion or projection makes the original hard to parse.
- Redraws preserve the lecture's topology and endpoint logic; they do not add decorative physics.

## Qualified Reconstructions

- The lecture suppresses $2\pi$ and $\alpha'$ in the momentum and winding formulas. The chapter uses $Y\sim Y+2\pi R$, $p_Y=n/R$, and $E_{\rm wind}=|w|R/\alpha'$.
- The scalar below $G_{55}$ is visible, but its precise interpretation is supplied by the surrounding lecture and qualified as a radius modulus.
- The two mixed oscillator states are visible; their symmetric and antisymmetric combinations are standard reconstruction from the closed-string massless sector.
- The T-duality board summary is partly occluded, so the complete $G_{\mu5}\leftrightarrow B_{\mu5}$ line is typeset separately.
- The Neumann and Dirichlet endpoint conditions are represented by separate completed board states rather than the inherited half-written frame.
- The color-stack and monopole redraws clarify only endpoint labels and flux interpretation already stated in the lecture.

## Rejected Alternatives

- Opening campus and lecturer-only shots carry no mathematical content.
- Frames dominated by board erasing, an unfinished symbol, or the lecturer fully blocking the relevant equation were rejected.
- A later frame was not used merely because the board was cleaner if its timestamp no longer matched the topic being discussed.
