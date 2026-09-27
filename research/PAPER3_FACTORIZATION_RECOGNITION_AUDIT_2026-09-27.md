# Paper 3 — Factorization vs Recognition Audit (F1–F4)

Date: 2026-09-27
Status: COMPLETED / NEXT GATE = SEPARATION

## Scope

This audit tests whether the Paper 3 distinction between factorization threshold and recognition threshold is already present in the audited finite-determinacy, Efrat–Mináč, and Zassenhaus/cohomology literature.

Definitions under audit:

\[
f_T(\mathcal C;D_\bullet)=\min\{n:T\text{ factors through }W_n\},
\]

and

\[
r_T(\mathcal C;D_\bullet)=\min\{n:W_n(G)\cong W_n(H)\Rightarrow T(G)\cong T(H)\ \forall G,H\in\mathcal C\}.
\]

These quantities must not be identified without a separate theorem.

## F1 — Factorization

**Result: NON-NOVEL / CLOSED.**

Efrat–Mináč and related literature explicitly contains the quotient-determines-target direction: for example, the finite quotient \(G/G_{(3)}\) determines the relevant cohomological target, expressed through inflation isomorphisms. Thus the basic notion “target factors through a finite filtered quotient” is established prior art.

**Boundary:** Paper 3 cannot claim novelty merely for introducing a factorization threshold.

## F2 — Recognition of a quotient from the target

**Result: PARTIALLY COVERED / KNOWN.**

The literature also contains reverse determination statements, such as low-degree cohomology determining a particular quotient \(G_{[3]}\). This is recognition/reconstruction of a quotient from target-side data.

This is logically distinct from Paper 3's proposed \(r_T\), where the finite window is the input and the target \(T\) is the output.

## F3 — Explicit separation of the two thresholds

**Result: OPEN / STRONG CANDIDATE.**

The audited corpus did not identify a theorem that explicitly defines factorization depth and recognition depth as separate threshold invariants and studies whether they can differ. Existing results generally use “determines” in one direction or provide dual determination results, rather than isolating these two numerical thresholds.

This is a research lead, **not yet a novelty claim**.

## F4 — Concrete separation phenomenon

**Result: OPEN / LOAD-BEARING.**

No verified explicit example was found in the audited corpus that demonstrates a genuine difference between the two thresholds. A concrete construction, or a theorem forcing equality in the relevant class, is therefore the decisive next gate.

The desired evidence must be formulated precisely after fixing the category, filtration, window morphisms/markings, and target. A merely linguistic distinction is insufficient.

## Decision

The next authorized research attack is:

> **Construct or rule out a genuine factorization-vs-recognition separation example.**

Do **not** begin the pure Bockstein sharpness calculation yet. If F4 yields a genuine separation theorem, it becomes the primary Paper 3 novelty candidate. If F4 is closed negatively, move next to the pure Bockstein target and then filtration/category dependence.

## Logical boundaries

- F1 known does not imply F3 is known.
- F3 being absent from the audited corpus does not prove novelty.
- F4 must be established mathematically, not inferred from terminology.
- Any separation result must be category-relative and must distinguish abstract quotient isomorphism from marked/functorial window data.

## Current classification

- Efrat–Mináč A/B: **NON-NOVEL / CLOSED**
- Factorization threshold alone: **NON-NOVEL / CLOSED**
- Recognition-of-quotient direction: **KNOWN / PARTIAL**
- Factorization vs recognition as separate invariants: **OPEN / STRONG CANDIDATE**
- Concrete separation: **OPEN / LOAD-BEARING**
- Pure Bockstein sharpness: **DEFERRED**
- Paper 3 ultimate program: **ACTIVE**
