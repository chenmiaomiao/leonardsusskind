# Figure Notes

## Verified Inventory

- **lecture_08_figure_01.png** at 00:23:20 shows the oscillator Hamiltonian,
  q-dot bracket, and p-dot bracket after both derivations are complete.
- **lecture_08_figure_02.png** at 00:34:00 shows all three Cartesian
  angular-momentum components and the cross-product form.
- **lecture_08_figure_03.png** at 00:38:41 shows the complete coordinate
  brackets with L_z.
- **lecture_08_figure_04.png** at 00:42:08 shows the corresponding position
  and momentum rotation rules together.
- **lecture_08_figure_05.png** at 00:53:18 shows the translation result
  \(\{F(q),p\}=dF/dq\).
- **lecture_08_figure_06.png** at 01:03:05 shows \(\{G,H\}=0\) and
  \(\{H,G\}=0\).
- **lecture_08_figure_07.png** at 01:10:52 shows the three cyclic brackets
  among L_x, L_y, and L_z.
- **lecture_08_figure_08.png** at 01:18:54 shows the gyroscope diagram,
  \(L^2/(2I)\), and the cancellation in the torque-free calculation.
- **lecture_08_figure_09.png** at 01:25:35 shows
  \(\boldsymbol L=\ell\boldsymbol r\) and \(L_z=\ell z\).
- **lecture_08_figure_10.png** at 01:22:43 shows the intermediate board sign
  \(V=-cL_z\), retained only with an explicit correction in the caption.
- **lecture_08_figure_11.png** at 01:30:35 shows the final component equations
  for precession.

## Reconstruction Decisions

The Stanford opening card was removed because it contains no lecture content.
The former image set contained several nearly redundant gyroscope gestures but
no evidence for the earlier calculations. They were replaced with completed
blackboard states at the relevant timestamps.

A clean TikZ diagram accompanies the original gyroscope frames. It separates
the pivot, fixed position vector, flywheel, vertical coordinate, and aligned
angular momentum. The original frame remains beside the reconstructed
equations so the diagram can be checked against the lecture.

## Uncertainties Resolved

The slanted gyroscope line is ultimately the position vector from the pivot to
the wheel center; a physical axle lies along the same direction in the model.
The angular momentum is assumed aligned with it, not identified with the
position vector dimensionally.

The negative potential sign in figure 10 is not treated as a final equation.
The lecture later chooses z upward and corrects the sign. The notes therefore
derive \(V=Mgz=+cL_z\) for positive \(\ell\), while preserving the frame as a
record of the live correction.
