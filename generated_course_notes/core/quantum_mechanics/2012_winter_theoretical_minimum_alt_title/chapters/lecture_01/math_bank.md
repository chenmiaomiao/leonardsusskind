# Math Bank
## Core Equations
- `\mathcal S_{\text{coin}}=\{H,T\}` [standard reconstruction]
- `\mathcal S_{\text{die}}=\{1,2,3,4,5,6\}` [standard reconstruction]
- `\mathcal S_{\text{particle on a line}}=\{(q,p)\mid q,p\in\mathbb R\}` [standard reconstruction]
- `P\wedge Q \leftrightarrow P\cap Q` [standard reconstruction]
- `P\vee Q \leftrightarrow P\cup Q` [standard reconstruction]
- `\sigma\in\{+1,-1\}` [transcript-backed]
- `H \leftrightarrow \sigma=1 \leftrightarrow \uparrow` [standard reconstruction]
- `T \leftrightarrow \sigma=-1 \leftrightarrow \downarrow` [standard reconstruction]
- `\text{readout}\in\{+1,-1\}` [transcript-backed]
- `\text{average horizontal readout}=0` [transcript-backed]
- `\text{average readout at angle }\theta=\cos\theta` [transcript-backed]
- `p_+(\theta)+p_-(\theta)=1` [editorial clarification from the two-outcome experiment]
- `p_+(\theta)-p_-(\theta)=\cos\theta` [editorial clarification from the stated mean]
- `p_+(\theta)=\cos^2(\theta/2),\quad p_-(\theta)=\sin^2(\theta/2)` [editorial consequence]
- `\begin{pmatrix}\alpha_1\\ \alpha_2\end{pmatrix}+\begin{pmatrix}\beta_1\\ \beta_2\end{pmatrix}=\begin{pmatrix}\alpha_1+\beta_1\\ \alpha_2+\beta_2\end{pmatrix}` [visible]
- `z\begin{pmatrix}\alpha_1\\ \alpha_2\end{pmatrix}=\begin{pmatrix}z\alpha_1\\ z\alpha_2\end{pmatrix}` [visible]
- `\alpha_1,\alpha_2,\beta_1,\beta_2,z\in\mathbb C` [standard reconstruction]
- `|\alpha\rangle \leftrightarrow \begin{pmatrix}\alpha_1\\ \alpha_2\end{pmatrix}` [standard reconstruction]
- `\langle\alpha| \leftrightarrow \begin{pmatrix}\alpha_1^* & \alpha_2^*\end{pmatrix}` [standard reconstruction]
- `\langle A+B|=\langle A|+\langle B|` [standard reconstruction]
- `\langle zA|=z^*\langle A|` [standard reconstruction]
- `\langle\beta|\alpha\rangle=\beta_1^*\alpha_1+\beta_2^*\alpha_2` [transcript-backed]
- `\langle A|B\rangle=\langle B|A\rangle^*` [standard reconstruction]
- `\langle A|A\rangle=\langle A|A\rangle^*\in\mathbb R_{\ge 0}` [standard reconstruction]
- `\langle\alpha|\alpha\rangle=\alpha_1^*\alpha_1+\alpha_2^*\alpha_2=|\alpha_1|^2+|\alpha_2|^2` [transcript-backed]
- `\langle A|B\rangle=0` [transcript-backed]
- `\begin{pmatrix}1&0\end{pmatrix}\begin{pmatrix}0\\1\end{pmatrix}=0` [transcript-backed]
- `\dim V=\max\{\text{number of mutually orthogonal nonzero vectors in }V\}` [standard reconstruction]

## Definitions And Objects
- `Closed system`: isolated system, temporarily not interacting with anything else.
- `State`: in the classical opening, the data needed to predict future evolution.
- `Classical space of states`: a set of possible states.
- `Phase space`: for a particle on a line, the plane of possible `(q,p)` values.
- `Proposition`: a collection of states, i.e. a subset of classical state space.
- `Qubit`: the two-state quantum analogue of a classical bit.
- `c-bit`: the classical two-state analogue, i.e. coin-like heads/tails logic.
- `\sigma`: the two-valued degree of freedom used to label qubit outcomes.
- `A`: the apparatus, treated for now as an oriented black box with a readout window.
- `Prepared state`: the state fixed by a prior measurement in a given orientation.
- `Pointer`: Susskind’s name for an ordinary spatial arrow, to distinguish it from an abstract vector.
- `Vector space`: a collection of mathematical objects closed under addition and scalar multiplication.
- `Real vector space`: scalars restricted to real numbers.
- `Complex vector space`: scalars allowed to be complex numbers.
- `Column`: the concrete model `\begin{pmatrix}\alpha_1\\ \alpha_2\end{pmatrix}` for a two-dimensional complex vector.
- `Ket`: an abstract vector, written `|A\rangle`.
- `Bra`: the corresponding dual vector, written `\langle A|`.
- `Dual vector space`: the space in one-to-one correspondence with the original vector space, behaving like the complex-conjugate space.
- `Inner product`: product of a bra with a ket, generalizing the dot product.
- `Length`: defined by the square root of the inner product of a vector with itself.
- `Orthogonality`: vanishing inner product.
- `Dimension`: maximal number of mutually orthogonal nonzero vectors.
- `Function-space example`: complex-valued functions of a real variable as a more general vector space example.

## Derivation Steps
1. `Classical logic from sets`: identify each proposition with a subset of the state space; overlap of two propositions gives `and`; union gives inclusive `or`; conclude that classical reasoning is set-theoretic.
2. `Measurement as preparation`: measure a qubit once; get `+1` or `-1`; reset the apparatus and repeat immediately in the same orientation; get the same value again; conclude that the first measurement has prepared the state.
3. `Directionality from the upside-down detector`: prepare the qubit “up”; flip the detector by `180^\circ`; the readout changes sign; restore the detector upright and recover the original sign; infer genuine spatial directionality.
4. `Failure of the naive classical-vector picture`: prepare “up”; turn the detector sideways; classical expectation would be zero horizontal component; actual single-shot result is always `+1` or `-1`, never `0`.
5. `Ensemble average at `90^\circ``: repeat the sideways experiment on many identically prepared “up” qubits; get random `+1/-1`; count equal frequencies; conclude that the average horizontal readout is zero.
6. `Why one qubit is not enough`: measure a rotated detector on one prepared qubit; obtain one definite `+1` or `-1`; repeat on the same qubit with the same detector orientation; only confirm the previous result; therefore a distribution requires many identically prepared qubits.
7. `Arbitrary-angle law`: rotate the detector by angle `\theta`; each trial still yields only `+1` or `-1`; over many identically prepared qubits, the average readout becomes `\cos\theta`.
8. `Two-outcome probability law`: combine `p_++p_-=1` with `p_+-p_-=\cos\theta`; solve for `p_\pm`; use the half-angle identities. Mark this as an editorial clarification rather than a blackboard derivation.
9. `Column vectors form a complex vector space`: take two columns of the same length; define addition entrywise; multiply a column by a complex scalar entrywise; closure under both operations gives the concrete example.
10. `Dual vector from the concrete column`: start with `\begin{pmatrix}\alpha_1\\ \alpha_2\end{pmatrix}`; complex-conjugate the entries; rewrite them as a row `\begin{pmatrix}\alpha_1^* & \alpha_2^*\end{pmatrix}` to mark that the object lives in the dual space.
11. `Inner product construction`: pair the bra `\begin{pmatrix}\beta_1^* & \beta_2^*\end{pmatrix}` with the ket `\begin{pmatrix}\alpha_1\\ \alpha_2\end{pmatrix}`; multiply matching components; sum the products; obtain `\beta_1^*\alpha_1+\beta_2^*\alpha_2`.
12. `Hermitian symmetry`: interchange `A` and `B` in the inner product; the expression becomes `\alpha_1^*\beta_1+\alpha_2^*\beta_2`; recognize this as the complex conjugate of the original; conclude `\langle A|B\rangle=\langle B|A\rangle^*`.
13. `Norm positivity`: set `B=A`; then the inner product equals its own complex conjugate, so it is real; in the concrete column model it becomes `\alpha_1^*\alpha_1+\alpha_2^*\alpha_2`; each term is nonnegative; conclude the norm-squared is real and positive.
14. `Order-independence of orthogonality`: if `\langle A|B\rangle=0`, then `\langle B|A\rangle=0^*=0`; therefore orthogonality does not depend on order even though the inner product does.
15. `Dimension from orthogonal vectors`: exhibit `\begin{pmatrix}1\\0\end{pmatrix}` and `\begin{pmatrix}0\\1\end{pmatrix}` as orthogonal; observe there is no third nonzero vector orthogonal to both in this two-component space; identify the dimension as two.

## Notation Choices
- Use `\sigma` for the qubit’s two-valued degree of freedom, with values `+1` and `-1`.
- Keep the lecture’s three parallel labels together: heads/tails, `\sigma=\pm1`, and `\uparrow/\downarrow`.
- Do not introduce Pauli-matrix notation such as `\sigma_x`, `\sigma_z`, or later spin basis kets like `|u\rangle,|d\rangle`.
- Use `A` for the apparatus exactly as in the lecture.
- Use `q` and `p` for the classical point-particle phase-space coordinates.
- Reserve `pointer` for an ordinary spatial arrow; reserve `vector` for the abstract vector-space object.
- Use `|A\rangle, |B\rangle` for abstract vectors and `\langle A|, \langle B|` for duals.
- Use `z` for a complex scalar, not `c`.
- Use star `(^*)` for complex conjugation, matching the lecture.
- Use row form for bras and column form for kets in the concrete two-component model.
- Use `column` rather than `matrix` when describing `\begin{pmatrix}\alpha_1\\ \alpha_2\end{pmatrix}`, since Susskind reserves `matrix` mainly for square arrays.
- If the final chapter needs a compact symbol for average readout, treat it as editorial notation, not lecture notation.

## Uncertain Mathematics
- No explicit board notation is available for “average value”; symbolic forms such as `\overline{\sigma(\theta)}` should be introduced only as editorial cleanup.
- The transcript explicitly gives the two outcomes and average `\cos\theta`, but it does not write the probability formulas. They may appear only as a clearly labeled editorial consequence of those two statements.
- The lecture strongly suggests vector-like behavior for averages, but it does not formalize rotated observables with operator notation; keep that language cautious.
- The symmetry law for the inner product is spoken somewhat loosely; the clean Hermitian form should be presented as a standard reconstruction.
- The function-space discussion near `01:43` to `01:44` is garbled; retain only the claim that complex-valued functions can form a vector space.
- The late audience question announces that reversed bra-ket order gives an outer product and a matrix. Keep that distinction concise; do not develop operator algebra here.
- The detector-as-quantum-system issue is postponed; do not introduce tensor-product or composite-system formalism here.
- The sideways detector sketch in the frame is visually imperfect and later corrected in discussion; no mathematical inference should depend on its literal chalk-arrow directions.
