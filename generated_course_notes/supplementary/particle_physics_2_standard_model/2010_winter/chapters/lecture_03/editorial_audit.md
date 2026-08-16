# Editorial Audit

- Status: **revise**
- Findings: 7

## Findings

- **critical / leakage** at `Opening production credit and chapter-curation language`: The prior body named production entities and reported how the notes followed the lecture. Repair: Remove credits from body and present physics directly.
- **high / voice** at `Repeated references to Susskind and what the lecture does`: The prior draft narrated the event instead of reading as prepared notes. Repair: Use direct mathematical exposition in lecture order.
- **high / structure** at `Summary section`: The source contains no forced retrospective summary and the section repeats prior material. Repair: Remove it and end at the source closing transition.
- **high / q_and_a** at `Generic Question and Answer subsections`: They merged or synthesized exchanges and omitted timestamps. Repair: Retain only transcript-verified exchanges in classroomqa blocks.
- **high / fidelity** at `Rotation group and representation review`: The prior draft compressed the group axioms, active/passive distinction, dummy-index reasoning, and spin-state examples. Repair: Restore the explanatory sequence and calculations.
- **high / fidelity** at `Infinitesimal SU(2) construction`: The prior draft compressed the anti-Hermitian convention, insertion of i, direct determinant expansion, and trace argument. Repair: Restore every step and correct the spoken subscript slip transparently.
- **medium / figure** at `All three frame figures`: The prior captions lacked required lectureframe timestamps. Repair: Use physics-only captions and attach exact frame timestamps.

## Source Uncertainties

- `00:37:52-00:39:42`: ASR repeats M and later garbles a diagonal subscript in the determinant expansion. Check: Use the explicit two-by-two determinant and identify the linear term as the trace.
- `00:30:53-00:31:15`: The source calls SU(2) the rotation group while deferring two-valuedness. Check: Preserve the local identification and mark the global double-cover clarification as editorial.
