# PAPER 4 — MINIMAL NONABELIAN FINITE-EXTENSION OBJECT / PRE-CHECK — 2026-10-02

## Candidate

Given an extension 1 -> N -> G -> D -> 1, the most direct intrinsic nonabelian object is the finite relative extension induced by the Zassenhaus window:

1 -> N/(N ∩ D_n(G)) -> G/D_n(G) -> D/D_n(D) -> 1.

This exists functorially because G -> D sends D_n(G) into D_n(D).

## Pre-check

### Object
PASS / LOCAL. The finite relative extension is intrinsic once the quotient map G -> D is part of the structured input.

### Input
FAIL as a compression candidate under the bare-window program unless the quotient map to D/D_n(D) is itself recoverable from the window. The object is not a new invariant of Q_n; it is essentially Q_n together with its relative quotient structure.

### Functoriality
PASS / LOCAL for morphisms of extensions preserving the map to D.

### Gauge
PASS / LOCAL at the extension level: presentation, relator and section choices are not part of the definition.

### Orientation bridge
OPEN. No non-tautological scalar character to orientation/deep extension depth has been derived.

### q-blindness
PASS. q is not inserted.

### Separation
PASS / LOCAL in the stress presentation: once n exceeds the relevant relation depth, the finite extension changes.

### Novelty
FAIL / CLOSED as a proposed carrier by itself. It is a repackaging of the finite window, not a compression.

### Stop
PASS. Do not compute extension-class coordinates merely to rediscover the whole finite window.

## Consequence

The research question is now sharply isolated:

> Does there exist a **strictly smaller, intrinsic, gauge-invariant scalar/module quotient** of the finite relative extension whose value is not equivalent to the whole window and which recovers a declared target (extension-depth truncation, relation defect, or orientation data)?

The ordinary untwisted homological candidates are already closed in the q>0 deep-tail stress model. The full finite relative extension survives but is not a carrier because it re-encodes the input.

Therefore the remaining route is not “compute the extension”; it is to find or rule out a genuine compression of that extension.

Classification:
- finite relative extension object: PASS / LOCAL but **FAIL / CLOSED as a novel compression carrier**;
- strict intrinsic compression: OPEN / LOAD-BEARING;
- universal impossibility of all compressions: OPEN;
- RAAG/carrier return: STOP.
