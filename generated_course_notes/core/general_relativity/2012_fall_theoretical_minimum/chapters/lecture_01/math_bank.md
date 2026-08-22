# Mathematical Source Bank

## Elevator and Apparent Gravity

- Coordinate map: \(z'=z-L(t)\), \(t'=t\), \(x'=x\).
- Uniform motion: \(L(t)=vt\), hence \(\ddot z'=\ddot z\).
- Accelerated motion: \(L(t)=gt^2/2\), hence \(\ddot z'=\ddot z-g\).
- Transformed Newton law: \(m\ddot z'=F-mg\).
- Accelerated-frame light ray: \(x=ct\), \(z'=-gt^2/2=-gx^2/(2c^2)\).
- Newtonian tidal preview: \(\delta a^i \simeq \partial_j g^i\,\xi^j\).

The sign of the fictitious force is normalized after the lecture's live check. The light equation restores the factor \(1/2\) required by the same coordinate map.

## Local Geometry

- Proper time with \(c=1\): \(d\tau^2=dt^2-dx^2\).
- With explicit units: \(c^2d\tau^2=c^2dt^2-dx^2\).
- Euclidean metric: \(ds^2=\delta_{mn}\,dx^m dx^n\).
- General metric: \(ds^2=g_{mn}(x)\,dx^m dx^n\).
- Sphere with polar angle: \(ds^2=R^2(d\theta^2+\sin^2\theta\,d\phi^2)\).
- Sphere with latitude: \(ds^2=R^2(d\lambda^2+\cos^2\lambda\,d\phi^2)\).
- Regional flatness criterion: there exist coordinates with \(g_{mn}=\delta_{mn}\) throughout the region.
- Relativistic tidal preview:
  \[
  \frac{D^2\xi^\mu}{D\tau^2}
  =-R^\mu{}_{\nu\rho\sigma}u^\nu\xi^\rho u^\sigma .
  \]

The geodesic-deviation formula is standard connective knowledge. It formalizes the lecture's explicit identification of curvature with invariant tidal acceleration but is not presented as a board derivation.

## Coordinate Transformations

- Mutual maps: \(x^m=x^m(y)\), \(y^m=y^m(x)\).
- Differential vector: \(dy^m=(\partial y^m/\partial x^p)dx^p\).
- Contravariant vector:
  \[
  (V')^m=\frac{\partial y^m}{\partial x^p}V^p .
  \]
- Scalar gradient: \(W_p=\partial S/\partial x^p\).
- Covector:
  \[
  W'_m=\frac{\partial x^p}{\partial y^m}W_p .
  \]
- Rank-two contravariant tensor:
  \[
  (T')^{mn}
  =\frac{\partial y^m}{\partial x^p}
   \frac{\partial y^n}{\partial x^q}T^{pq}.
  \]
- Rank-two covariant tensor:
  \[
  T'_{mn}
  =\frac{\partial x^p}{\partial y^m}
   \frac{\partial x^q}{\partial y^n}T_{pq}.
  \]
- Metric transformation:
  \[
  g'_{pq}(y)
  =\frac{\partial x^m}{\partial y^p}
   \frac{\partial x^n}{\partial y^q}g_{mn}(x(y)).
  \]

The final line is the direct completion of the substitution begun at the end of the recording. It introduces no result beyond the chain rule and invariance of \(ds^2\).
