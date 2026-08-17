# Visual Evidence
## Frame Inventory
- `lecture_01_figure_02.png`: Early rest-frame board layout with a vertical \(t\)-axis, marked times, a lower horizontal baseline, and the first constant-position line; this screenshot should remain in the final notes as visual evidence for the initial spacetime lattice.
- `lecture_01_figure_03.png`: Mixed equation-and-sketch frame showing the Galilean transformation material together with a leftover fragment of the spacetime picture; this screenshot should remain because it preserves the lecture’s geometry-to-algebra transition.
- `lecture_01_figure_04.png`: Simultaneity/light-ray construction with colored lines, an interior dashed segment, and the clearest visible label \(x=t\); this screenshot should remain because the board geometry matters as much as the equation.
- `lecture_01_figure_05.png`: Cleaner symmetric version of the same construction, emphasizing the \(c=1\) symmetry of the tilted axes and light-ray geometry; this screenshot should remain because the lecture explicitly treats the symmetry as a visual fact.

## Equation Extraction
- `lecture_01_figure_02.png`: \(t\) [visible]
- `lecture_01_figure_03.png`: \(x' = x - vt\) [partially visible]
- `lecture_01_figure_03.png`: \(t=t'\) [visible]
- `lecture_01_figure_03.png`: \(x=x'+vt\) [partially visible]
- `lecture_01_figure_03.png`: \(x=x'+vt'\) [standard completion]
- `lecture_01_figure_03.png`: \(x\) as the horizontal axis label or arrow direction [partially visible]
- `lecture_01_figure_04.png`: \(x=t\) [visible]
- `lecture_01_figure_04.png`: \(x=vt+L\) [standard completion]
- `lecture_01_figure_04.png`: \(x=vt+2L\) [standard completion]
- `lecture_01_figure_05.png`: No new standalone equation is securely readable beyond the geometric labeling already better anchored by the previous frame [partially visible]

## Diagram Extraction
- `lecture_01_figure_02.png` should be shown both as a screenshot and as a TikZ redraw. The redraw should present the rest-frame lattice: \(t\) vertical, \(x\) horizontal, several constant-\(x\) worldlines, and several constant-\(t\) slices, while the screenshot preserves the original board layout and spacing.
- `lecture_01_figure_03.png` should remain as a screenshot and be paired with clean displayed equations. A full TikZ redraw is optional here; the main point is that the board still shows the equations being read off a spacetime picture rather than introduced abstractly.
- `lecture_01_figure_04.png` should be shown both ways. The TikZ redraw should include the lower baseline, the moving family of nearly vertical shifted worldlines, the forward light ray labeled \(x=t\), the descending backward light ray, the apex/intersection structure, and the internal dashed segment.
- `lecture_01_figure_05.png` should also be shown both ways. The TikZ redraw should abstract the earlier construction into the symmetric \(c=1\) diagram with unprimed axes, primed axes, and the two 45-degree light rays that organize the symmetry.
- The two later frames, `lecture_01_figure_04.png` and `lecture_01_figure_05.png`, should appear close together in the final notes. The first supports the concrete construction; the second supports the cleaned symmetric abstraction.
- The board’s red-versus-blue line families should not be discarded conceptually. Even if the TikZ redraw uses a simplified palette, the screenshot should stay nearby so the original visual grouping remains available to the reader.

## Reconstruction Guidance
- Use `lecture_01_figure_02.png` as evidence for board layout, not as a complete mathematical object. The transcript should supply the missing horizontal constant-time slices that are only beginning to appear in the screenshot.
- Use `lecture_01_figure_03.png` to justify a clean typeset presentation of the Galilean transformation and its inverse:
  \[
  t'=t,\qquad x'=x-vt,
  \]
  followed by
  \[
  t=t',\qquad x=x'+vt'.
  \]
  The screenshot shows enough to anchor the form, but the final lower term should be completed from the lecture logic rather than from the crop alone.
- Use `lecture_01_figure_04.png` to anchor the local simultaneity calculation. The visible board is good evidence for the geometry, while the transcript should be used to identify the specific lines as \(x=t\), \(x=vt+L\), and \(x=vt+2L\), and to explain which segment is the backward light ray.
- Use `lecture_01_figure_05.png` when the notes move from the concrete construction to the abstracted symmetric picture. This is the right place to redraw the unprimed and primed axes cleanly and explain that the simultaneity line tilts in the same geometric manner as the moving time axis.
- Keep the screenshots nearby whenever the original board composition matters. In this lecture, that is especially true for the colored simultaneity constructions: the notes should not replace those frames with polished TikZ alone.
- Prefer cautious completions over aggressive transcription. If a symbol is too small or too cropped to be trusted from the frame, state it in clean mathematical form only when the transcript and surrounding construction make the intended line unambiguous.

## Added Verified Frames
- **lecture_01_figure_06.png (01:32:38):** Keep. The completed \(c=1\) Lorentz pair is legible and minimally obstructed.
- **lecture_01_figure_07.png (01:35:58):** Keep. The restored factors of \(c\) are visible in both transformation equations.

## Remaining Uncertainties
- In `lecture_01_figure_02.png`, the subtitle refers to drawing horizontal lines, but the frame itself preserves the vertical and worldline structure more clearly than the finished grid. The full lattice must therefore be completed from the transcript.
- In `lecture_01_figure_03.png`, the lower inverse equation is cropped, so the final factor after \(v\) is not securely legible from the image alone. The lecture context strongly supports \(t'\), with \(t\) temporarily interchangeable because \(t=t'\).
- In `lecture_01_figure_03.png`, the upper equation \(x'=x-vt\) is only partially framed and should not be treated as a perfect board transcription.
- In `lecture_01_figure_04.png`, \(x=t\) is the only equation that is plainly secure from the frame itself. Other line identifications belong to cautious reconstruction, not direct visual transcription.
- In `lecture_01_figure_04.png` and `lecture_01_figure_05.png`, not every colored segment is self-explanatory from the image alone. The transcript is needed to tell which slanted line is the forward light ray, which is the backward one, and which shifted lines are moving-worldline loci.
- In `lecture_01_figure_05.png`, the slanted black labels associated with the primed geometry are too small to quote reliably. The final notes should redraw those labels cleanly instead of pretending the frame preserves them clearly.
- The transcript itself has garbled passages later in the derivation, including a dropped \(t\) in a line that should read \(x=vt+2L\). Where the frames and the clean surrounding mathematics agree, that kind of transcript corruption should be corrected cautiously rather than reproduced.
