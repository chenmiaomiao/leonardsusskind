# Figure Notes
## Image Inventory
- `lecture_01_figure_02.png`: A mostly clean early board state for the rest-frame spacetime lattice. The lecturer stands to the left of a vertical axis labeled \(t\), with a series of marked points running upward, a lower horizontal baseline, and a tall light-blue nearly vertical line to the right. The board is still sparse, so it functions mainly as layout evidence for the initial coordinate grid.
- `lecture_01_figure_03.png`: A mixed algebra-and-diagram board state. The lower board shows the inverse Galilean relations in handwritten form, with an \(x\)-axis arrow drawn to the right; the upper board retains part of the earlier transformation equation. At the far left, a fragment of the spacetime sketch is still visible.
- `lecture_01_figure_04.png`: A later spacetime construction dominated by colored geometry. A red sloping segment rises from a lower-left point to an upper apex, another red segment descends to the right, a dashed red interior segment is present, and several light-blue nearly vertical guide lines remain visible. A slanted line labeled \(x=t\) is the clearest equation-level content.
- `lecture_01_figure_05.png`: A cleaner, more symmetric version of the same spacetime construction. Both red sloping sides of the central peak are visible together, the lower horizontal baseline is intact, blue vertical guide lines remain, and the internal dashed red segment is clear. The point of the image is the symmetry of the whole diagram rather than any single equation.

## Blackboard Equations
- `lecture_01_figure_02.png`: \(t\) [visible]
- `lecture_01_figure_03.png`: \(x' = x - vt\) [partially visible]
- `lecture_01_figure_03.png`: \(t=t'\) [visible]
- `lecture_01_figure_03.png`: \(x=x'+vt\) [partially visible]
- `lecture_01_figure_03.png`: \(x=x'+vt'\) [standard reconstruction]
- `lecture_01_figure_04.png`: \(x=t\) [visible]
- `lecture_01_figure_04.png`: \(x=vt+l\) [standard reconstruction]
- `lecture_01_figure_04.png`: \(x=vt+2l\) [standard reconstruction]
- `lecture_01_figure_05.png`: No additional standalone equation is securely legible beyond line labels and geometric relations already better preserved in the neighboring figure [partially visible]

## Diagram And Layout Reading
- `lecture_01_figure_02.png` shows the lecture’s first clean spacetime-board layout: time vertical, a horizontal base line for \(t=0\), and a first family of constant-position worldlines. It is not yet a rich diagram, but it captures the board rhetoric of “build the lattice from axes and repeated lines.”
- In `lecture_01_figure_03.png`, the board is doing two jobs at once. The lower half contains the Galilean transformation formulas, while the upper-left remnant of the sketch reminds us that these equations are being read directly off a spacetime picture. This is useful evidence for the lecture’s rhythm: geometry first, algebra immediately after.
- `lecture_01_figure_04.png` is a local simultaneity/light-ray construction. The horizontal lower edge acts as the baseline, the light-blue nearly vertical lines mark the moving family of worldlines, the red sloping lines encode the light-ray or signal paths, and the dashed red segment marks an internal comparison path. The labeled \(x=t\) line anchors the whole calculation.
- `lecture_01_figure_05.png` is the same construction after Susskind has abstracted it into its \(c=1\) symmetric form. The important visual fact is that the tilted axis and the tilted simultaneity surface mirror one another about the 45-degree light-ray structure. This screenshot is therefore primarily a symmetry witness.
- The red and blue color coding matters. Even if the final notes redraw the diagram in TikZ, the screenshot should remain nearby because the original board uses color to distinguish different geometric families.

## TeX Reconstruction Plan
- `lecture_01_figure_02.png` should remain visible in the notes. It should be paired with a simple TikZ redraw of the initial rest-frame spacetime lattice: vertical \(t\)-axis, horizontal \(x\)-axis, repeated constant-\(x\) worldlines, and constant-\(t\) slices. The screenshot is valuable as evidence of the board layout, while TikZ should supply the cleaner full lattice that the lecture is in the process of building.
- `lecture_01_figure_03.png` should remain visible and be paired with nearby displayed equations for the Galilean transformation and its inverse:
  \[
  t'=t,\qquad x'=x-vt,
  \]
  and then
  \[
  t=t',\qquad x=x'+vt'
  \]
  or equivalently \(x=x'+vt\) once \(t=t'\) has been stated. A small TikZ fragment is optional here, but the main reconstruction work should be typeset equations rather than a full redraw.
- `lecture_01_figure_04.png` should remain visible and be paired with both a clean displayed equation for the light-ray line \(x=t\) and a TikZ redraw of the local simultaneity construction. The redraw should keep the lower baseline, the slanted signal line \(x=t\), the shifted moving-worldline family, the apex point, and the dashed interior segment. Any equations for the additional slanted lines, such as \(x=vt+l\), should be introduced in the prose or in nearby displays rather than forced into the figure itself.
- `lecture_01_figure_05.png` should remain visible and be paired with the cleaned TikZ version of the symmetric \(c=1\) spacetime diagram. This is the natural place to show the unprimed axes, the primed axes, the 45-degree light rays, and the tilted simultaneity surface. The screenshot should stay because the lecture’s claim about “a lovely symmetry” is a claim about the look of the board as much as about any formula.
- In the final chapter, `lecture_01_figure_04.png` and `lecture_01_figure_05.png` may work especially well as a sequence: first the computed light-ray construction, then the abstract symmetric redraw.

## Caption Drafts
- `lecture_01_figure_02.png`: Rest-frame time axis and emerging spacetime lattice
- `lecture_01_figure_03.png`: Galilean coordinate shift beside the spacetime sketch
- `lecture_01_figure_04.png`: Light-ray line \(x=t\) in the simultaneity construction
- `lecture_01_figure_05.png`: Symmetric \(c=1\) spacetime diagram

## Added Verified Frames
- **lecture_01_figure_06.png (01:32:38):** Both completed natural-unit equations are visible with minimal obstruction:
  \[
  x'=\frac{x-vt}{\sqrt{1-v^2}},\qquad
  t'=\frac{t-vx}{\sqrt{1-v^2}}.
  \]
- **lecture_01_figure_07.png (01:35:58):** Both dimensionally restored equations are visible, including \(v^2/c^2\) in the denominators and \(vx/c^2\) in the time numerator.

## Remaining Uncertainties
- In `lecture_01_figure_02.png`, the subtitle refers to drawing horizontal lines, but the frame preserves the vertical axis and worldline structure more clearly than the full set of horizontal constant-time slices. The redraw should therefore use the transcript to complete the grid, not the screenshot alone.
- In `lecture_01_figure_03.png`, the inverse lower equation is cropped. The visible writing supports \(x=x'+v\cdots\), but the final factor is not fully shown in the image. The transcript strongly indicates \(vt\) or \(vt'\), with the lecture immediately noting that \(t=t'\).
- In `lecture_01_figure_03.png`, the upper equation \(x'=x-vt\) is only partially framed. It is legible enough to identify the transformation, but not presented as a clean standalone board line.
- In `lecture_01_figure_04.png`, the line label \(x=t\) is the only equation that is plainly secure. Other line labels are present but too small or angled to transcribe confidently from the image alone.
- In `lecture_01_figure_04.png` and `lecture_01_figure_05.png`, the exact meaning of every colored segment is not fully recoverable from the screenshot without the surrounding lecture context. The transcript is needed to decide which lines are worldlines, which are light rays, and which segment marks the backward trace.
- In `lecture_01_figure_05.png`, the slanted black reference lines almost certainly correspond to the primed-axis geometry, but their labels are not legible enough to quote directly. The final notes should redraw the axes cleanly rather than pretend the board labels are fully readable.
