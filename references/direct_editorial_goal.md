# Direct Editorial Goal

## Objective

Polish the Leonard Susskind lecture notes directly, one chapter at a time, without a tmux writer queue. The finished prose should read like naturally prepared notes for the lecture itself: direct, mathematically serious, conversational when useful, and faithful to Susskind's explanatory rhythm. It must not sound like a transcript summary, an AI reconstruction report, or commentary about what the lecturer is doing. Front matter must still state honestly that these are independently reconstructed companion notes, not Susskind's original manuscript.

## Source Authority

Use evidence in this order:

1. The complete timestamped transcript, including audience questions and answers.
2. The corresponding video and legible blackboard equations, diagrams, labels, and gestures.
3. Identified Susskind books or trusted course references for notation and damaged passages.
4. Physics knowledge only for accurate connective explanation, corrected notation, standard definitions, and algebra logically implied by the sourced argument.

Never replace the lecture with a more familiar textbook derivation or add unrelated material merely to make a chapter look comprehensive.

## No-Reduction Rule

Cover every substantive transcript beat: topics, definitions, claims, derivations, examples, analogies, caveats, rhetorical explanations, pedagogically useful repetition, and verified classroom exchanges. Remove only stutters, verbal filler, obvious ASR debris, and abandoned false starts that contain no substantive content. Do not collapse a multi-step explanation into a terse summary. If a substantive passage is uncertain, verify it or mark the uncertainty; do not silently omit it.

Before rewriting, make an exhaustive timestamped beat inventory. Acceptance requires every substantive beat to be represented in the chapter and every genuine question-and-answer exchange to appear in a dedicated `classroomqa` block.

## Mathematics And Figures

Recover all mathematics that carries the argument, including intermediate blackboard steps that speech leaves implicit. Every equation must be traceable to the transcript, a verified frame, an identified reference, or a logically necessary intermediate step. Preserve relevant board frames at correct timestamps and use clean LaTeX or TikZ reconstructions when they improve legibility without changing the argument. Reject decorative, mistimed, unreadable, or irrelevant figures.

## Voice And Prose

- Present the physics directly, usually in neutral exposition or natural first-person plural: “we now consider,” “let us calculate,” and similar language only where it fits.
- Follow the lecture's order, pacing, questions, examples, and changes of viewpoint.
- Suppress formulaic AI prose, generic previews and summaries, repeated signposting, inflated claims, tidy but artificial section symmetry, and phrases such as “the lecturer explains.”
- Preserve the human rhythm of explanation while joining broken transcript fragments into smooth prose.
- Never mention prompts, agents, workflows, private conversations, curation instructions, or production decisions in the chapter body.

## Chapter Workflow

1. Read the full transcript, current TeX, metadata, figures, and relevant reference material.
2. Inventory every substantive beat, classroom exchange, equation, and board figure with timestamps.
3. Rewrite the complete chapter in the lecture's natural order and voice without substantive reduction.
4. Perform a source-fidelity review for omissions, inventions, altered derivations, weak figures, and AI-like prose.
5. Compile the chapter and course; check missing assets, LaTeX errors, overflow, references, and representative rendered pages.
6. Commit and push the accepted chapter before moving to the next one.

Process all supplementary courses first, then only the latest complete version of each core course. Exclude partial, superseded, and duplicate runs. Re-audit any chapters polished under an older charter before declaring their course complete.

## Acceptance Standard

A chapter passes only when substantive transcript coverage is complete, all genuine Q&A is preserved, board mathematics and figures are verified, added connective knowledge is accurate and restrained, the prose reads naturally rather than algorithmically, the TeX and PDF compile cleanly, and no internal production language remains.
