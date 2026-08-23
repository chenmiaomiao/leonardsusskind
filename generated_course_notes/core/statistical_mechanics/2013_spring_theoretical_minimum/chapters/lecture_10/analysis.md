# Lecture 10 Source Analysis

## Source

- Canonical recording: 184 - Statistical Mechanics Lecture 10 [IWtcFAP3ju4].mkv
- Canonical transcript: 184 - Statistical Mechanics Lecture 10 [IWtcFAP3ju4].md
- Duration: approximately 2:04:24
- Transcript size: 30,287 words
- Formal statistical-mechanics lecture: 00:00:07--01:24:13
- Postlecture fine-tuning discussion: 01:24:45--02:04:12

## Editorial Scope

The chapter preserves both parts of the recording but marks their boundary explicitly. The formal lecture completes the mean-field Ising calculation, derives the lattice-gas dictionary, and closes with liquid--gas criticality and universality. The postlecture exchange is retained as a separate section because it is substantive source material, not because it belongs to the lattice-gas derivation.

The rewritten body represents all 85 chronological movements in source_map.json, including 33 classroom exchanges. It does not retain filler, false starts, or personal attacks. Live mathematical corrections are preserved as corrections and resolved into one consistent notation.

## Physics Decisions

- Hamiltonian convention: \(\mathcal H=-J\sum_{\langle ij\rangle}\sigma_i\sigma_j+h\sum_i\sigma_i\); positive \(h\) favors \(\sigma=-1\).
- Mean field: \(m=\tanh[\beta(2dJm-h)]\), \(T_c^{\rm MF}=2dJ\).
- Occupancy: \(n_i=(1+\sigma_i)/2\), \(\rho=(1+m)/2\).
- Lattice gas: \(\epsilon=4J\), \(\mu=-(4dJ+2h)\).
- The board's live \(2J\) attraction statement is corrected to \(4J\) by the six-versus-eight broken-bond count.
- Critical exponents are not described as uniformly irrational; exact rational and nontrivial numerical examples are distinguished.
- Selection effects are presented as conditional reasoning that still requires an ensemble, mechanism, and tests.

## Visual Decisions

Ten frames were inspected at full resolution and retained. They show the mean-field equation, reduced graphing equation, magnetic phase diagram, potential well, grand partition sum, lattice occupancy, particle-energy count, field/energy dictionary, density map, and liquid--gas diagram. The opening title card and low-information postlecture doodles were rejected. Clean TikZ reconstructions supplement rather than impersonate the board evidence.
