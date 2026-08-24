# Textless Cover Art Direction

The generated course books use text-free artwork beneath exact LaTeX title and
credit panels. Keeping typography out of the raster image prevents misspelled
titles, false equations, and inconsistent attribution.

## Collection Style

- Use a clean portrait composition with one dominant physics motif.
- Favor restrained Japanese editorial and screen-print aesthetics: tactile
  paper grain, broad negative space, crisp geometry, and a limited palette.
- Keep the middle visually distinctive while leaving calm regions near the top
  and bottom for the LaTeX overlays.
- Make each image legible as a small README or website thumbnail.
- Do not generate words, letters, numbers, equations, labels, logos,
  signatures, watermarks, classroom scenes, or decorative scientific clutter.

## Topic Motifs

| Course family | Visual language |
| --- | --- |
| Classical mechanics | Pendulum, trajectory, phase-space motion |
| Quantum mechanics | Interference, paired paths, symmetry |
| Relativity | Light cones, geodesics, curved surfaces |
| Statistical mechanics | Ordered and dispersed microstates |
| Cosmology | Horizons and expanding arcs |
| Particle physics | Interaction vertices and related geometric families |
| Quantum entanglement | Shared waves and multipartite ribbons |
| String theory | A string, horizon, or folded membrane |

## Production Workflow

The 2026 collection was generated with Codex's built-in image-generation tool.
Each selected image was center-cropped, never stretched, to the pixel dimensions
of its existing `assets/cover-art.png`. The actual `course.tex` title page was
compiled twice before acceptance because TikZ `remember picture` overlays need
a second pass for stable placement. README and website previews must always be
extracted from page one of the final published PDF, not from the raw artwork.
