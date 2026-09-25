# PAPER / Literature merge audit — 2026-09-25

## Scope

Compared the current `paper/main.tex` against the audited Kummerian/cyclotomic literature and the controlling U5/N1 research records. The goal was not to import new mathematics, but to retain only literature-supported improvements in framing, definitions, logical separation, and novelty boundaries.

## Authoritative basis

- `RESEARCH_MAP.md`
- `CURRENT_STATE.md`
- `research/00_RESEARCH_LOG.md`
- `research/RESEARCH_CONTINUITY_PROTOCOL.md`
- `research/U5_INTRINSIC_FINITE_SELECTOR_AUDIT_2026-09-24.md`
- `research/N1_LITERATURE_GATE_KUMMERIAN_CYCLOTOMIC_DEMUSHKIN_2026-09-24.md`
- audited Labute (1967), Efrat–Quadrelli (2019), Quadrelli–Weigel (2020, 2022)
- recent uploaded literature was checked for boundary relevance; no claim from it was inserted unless independently supported by the controlling project records.

## Changes retained

1. **Candidate domain corrected and made explicit.**
   The theorem uses principal-unit characters
   [
   ho:Q_k	o U_{1,k}=1+3(mathbf Z/3^kmathbf Z),
   ]
   rather than arbitrary ((mathbf Z/3^k)^	imes)-valued characters. This matches the standard oriented/Kummerian setup and ensures trivial reduction of the coefficient action modulo (3).

2. **Intrinsic predicate separated from proof coordinates.**
   The finite Kummer predicate is defined directly on ((Q_k,ho)). Presentation, relator, Fox derivatives, preferred (H^2)-generator, (q), and (chi) are explicitly excluded from the definition.

3. **Finite-depth factorization promoted to its own logical step.**
   The semidirect-product argument is presented before the one-relator/Fox calculation. This makes clear that the finite selector is genuinely a quotient-level predicate and is not merely the classical full-group Kummerian theorem rewritten with finite coefficients.

4. **Classical literature separated from the proposed finite statement.**
   Labute/Efrat–Quadrelli/Quadrelli–Weigel are used for the already-known Kummerian/cyclotomic orientation theory. The manuscript no longer presents uniqueness of the Kummerian orientation itself as novel.

5. **q-blindness boundary made explicit.**
   The manuscript now says that q-blindness concerns the selector input only. It does not claim a uniform theorem over all Demuškin invariants q.

6. **Minimality boundary retained.**
   (P_{k+1}) is stated as sufficient, not minimal.

7. **Literature novelty language tightened.**
   The manuscript claims only that the exact combined bare-(Q_k), arbitrary-candidate, finite-factorization formulation was not found in the audited corpus. It does not make an absolute priority claim.

## What was deliberately NOT imported

- No claim that the canonical orientation itself is new.
- No classification-based reconstruction presented as the finite selector.
- No revival of the closed (t_2), naive degree-3 Fox, or other closed branches.
- No uniform-in-(q) theorem.
- No minimality theorem.
- No claim that recent A_3-formality or variation papers prove the finite selector; their relevance is only as a novelty-boundary check.

## Mathematical status

- Manuscript finite-window theorem: **PASS / CLOSED** under the current fixed-group hypotheses and the controlling U5 proof.
- Classical Kummerian orientation: **HISTORICAL / SUPERSEDED as novelty**.
- Exact publication novelty of the finite-window formulation: **PASS / CONDITIONAL**.
- Minimal finite depth: **OPEN**.
- Uniform extension to a Demuškin family: **OPEN**.

## Commit

`paper/main.tex` updated in commit `46eaa54ccc34ab7eafa1680624e221653ff885de`.

This record is a manuscript-quality framing audit, not an independent proof audit of every displayed lemma.
