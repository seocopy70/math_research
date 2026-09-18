# Q3/Q∞ — Independent-definition gate for d∞
# Date: 2026-09-18

## Global position

Q3-2A-R structural census is complete for the authoritative q=3 object d3 and its H-orbit. The observed size-40 vector/projective orbit is not promoted to a q-detector.

The q=∞ side is now defined by the project's fixed q=∞ baseline-relative construction, rather than by an observed orbit value:

\[
\Delta_3(q):=\operatorname{in}_3(s_q)-\operatorname{in}_3(s_\infty),
\qquad
d_q:=[\Delta_3(q),X_2].
\]

The independent exact Magnus verification gives

\[
\Delta_3(3)=X_1^{[3]},\qquad \Delta_3(\infty)=0.
\]

Therefore

\[
d_3=[X_1^{[3]},X_2],\qquad d_\infty=[0,X_2]=0.
\]

This is a derivation from the fixed q=∞ baseline, not a value selected to force separation.

## Analytic zero-case consequence

Because N is linear,

\[
N(d_\infty)=N(0)=0.
\]

Because the preregistered invariant is the vector-orbit invariant

\[
J(v):=|H_U\cdot v|,
\]

and 0 is fixed by every linear element of H_U,

\[
J(N(d_\infty))=J(0)=1.
\]

Thus the q=∞ value 1 is **analytically determined before execution**. A later computation of the q=∞ side is therefore an **IMPLEMENTATION-LEVEL CONSISTENCY / SANITY CHECK**, not a new MATHEMATICAL PASS.

The substantive q=3 question is the single decision criterion

\[
\boxed{J(N(d_3))\stackrel{?}{\ne}1}.
\]

If \(J(N(d_3))=1\), this particular N/J probe does not distinguish the q-sensitive source from the q=∞ baseline. If \(J(N(d_3))\ne1\), this invariant distinguishes the two cases. Neither outcome establishes or refutes orientation survival in the whole Zassenhaus filtration; the claim is restricted to this specific source, N, H-action, and invariant.

## Purpose

The purpose of the next computation is consequently narrower than the original Q3/Q∞ comparison: verify the fixed implementation against the analytically determined zero case, and compute the q=3 invariant without changing N, coordinates, normalization, or H-action.

## Dependencies

Frozen inputs:

- Current research map: `RESEARCH_MAP.md`.
- Mathematical/computational conventions: `research/03_CONVENTIONS_AND_IMPLEMENTATION.md`.
- Q3 zero-case pre-registration: `research/Q3_QINF_zero_case_prereg_2026-09-18.md`.
- Q3-2A-R robustness audit: Actions run `35345371915`, head `ded57a8dd0605f48db2b04f7b7718fff40ffdc6f`.
- The q=3 local object and N construction are taken from the already-authoritative pipeline.
- The q-sensitive d definition is recorded in `research/03_CONVENTIONS_AND_IMPLEMENTATION.md`, commit `996fefbf8603375db427d44260cb763557620c09`.

## Independence criteria

The q=∞ definition satisfies the following audit conditions:

1. **Mathematical source fixed first.** The q=∞ baseline is the pure-commutator presentation/control obtained by deleting the finite-q power term.
2. **No target-value selection.** The definition does not refer to J(N(d3)) or any observed orbit size.
3. **No representative cloning.** d∞ is the baseline-relative difference object derived from \(\Delta_3(\infty)\), not a copied or deformed d3.
4. **Local data explicit.** The source is degree 3, followed by the fixed bracket with X2; for q=3, \(\Delta_3(3)=X_1^{[3]}\), so d3 has the corresponding degree-4 multidegree.
5. **N fixed before evaluation.** The authoritative N is applied unchanged.
6. **Zero is derived.** d∞=0 and N(d∞)=0 follow analytically.
7. **Same invariant.** J is applied to both sides.
8. **Zero convention audited.** J(0)=1 is a direct consequence of the vector-orbit definition under a linear group action; it is not an ad hoc projective-zero assignment.

## Execution gate

The definition gate is now **ACCEPTED**.

The smallest admissible computation is:

1. compute the fixed q=3 value J(N(d3));
2. compute the q=∞ implementation path and verify it returns N(d∞)=0 and J=1;
3. classify the q=∞ result as an implementation sanity check;
4. classify the q=3 result against the single substantive criterion J(N(d3)) != 1.

No threshold, ranking, post-hoc exception, or altered q=∞ normalization may be introduced.

## Invalid-test guards

Any result is **INVALID TEST** if it:

- mixes row/right and column/left coordinate conventions;
- uses a stale or modified N;
- changes H-action or normalization between q=3 and q=∞;
- silently substitutes zero instead of deriving it;
- computes an incomplete H-closure;
- uses non-exact finite-field arithmetic.

## Current status

Definition gate: **ACCEPTED**.

Substantive q-detection result: **OPEN**.

The earlier size-40 observation remains:

> **H-EQUIVALENT STABILITY OBSERVED (inside H·d3; no q-claim).**
