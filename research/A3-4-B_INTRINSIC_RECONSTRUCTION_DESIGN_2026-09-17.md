# A3-4-B — Intrinsic Reconstruction Design (2026-09-17)

## Purpose

Test whether the degree-4 submodule \(W_d\) can be characterized without externally specifying the distinguished generator \(X_1\) (and ideally \(X_2\)).

This is an **intrinsic reconstruction** test, not a q-recovery test by itself.

## Ambient space

Use the authoritative degree-4 free-Lie ambient space
\[
L_4=\mathbb F_3\text{-span of degree-4 Lie words},\qquad \dim L_4=60.
\]
The distinguished previously constructed submodule is \(W=W_{45}\), with
\[
\dim W=45,\qquad \dim W_d=45,\qquad \dim(W\cap W_d)=35,\qquad \dim(W+W_d)=55.
\]

The earlier notation “45-dimensional subspace of \(Q_4\)” is not used here: the current exact construction places \(W_d\) in \(L_4\), and quotient descent must be checked separately rather than assumed.

## Candidate set

Define
\[
\mathcal C(W)=\{M\le L_4:\ M\text{ is }Sp_4(\mathbb F_3)\text{-stable},\ \dim M=45,\ \dim(M\cap W)=35\}.
\]

The first question is whether \(W_d\) is uniquely determined by these module-theoretic conditions.

### Interpretation

- **Unique:** \(\mathcal C(W)=\{W_d\}\). This gives a strong intrinsic characterization relative to \((L_4,H,W)\).
- **Multiple:** there are other candidates. Then the stated conditions are insufficient to characterize \(W_d\) uniquely.
- **Single canonical orbit/class:** if several candidates exist but are related by a canonical symmetry, record that weaker intrinsic characterization rather than claiming uniqueness.
- **Invalid/inconclusive:** if the computational procedure does not exhaust the candidate space.

## Important distinction

This B1 test is intrinsic **relative to the distinguished pair \((L_4,H,W)\)**. It is not yet an absolute reconstruction from \(Q_4\) alone.

A stronger future B2 question is whether the relevant object can be recovered from the \(H\)-module structure of the quotient itself, without supplying \(W\) as external data.

## Computational strategy

Brute-force enumeration of all 45-dimensional subspaces is impossible. The implementation must enumerate candidates through exact \(H\)-submodule/module-extension structure (e.g. MeatAxe/invariant-subspace machinery), and must include an explicit exhaustiveness assertion.

For every candidate returned, verify directly in the 60-dimensional ambient coordinates:

1. stability under all generating symplectic matrices;
2. dimension 45;
3. intersection dimension with W equal to 35;
4. equality/non-equality with the known \(W_d\).

No uniqueness claim is valid unless the search is exhaustive.

## Status

DESIGN — computation to follow.
