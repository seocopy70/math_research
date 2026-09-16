# A3-4-B Run Record — 2026-09-17

## Scope

This run executes the exact scaffold for the proposed intrinsic-reconstruction test. It verifies the known \(W_d\) satisfies the target numerical conditions, but it does **not** enumerate all 45-dimensional \(H\)-stable subspaces.

## Verified target data

\[
\dim L_4=60,
\quad \dim W=45,
\quad \dim W_d=45,
\]
\[
\dim(W\cap W_d)=35,
\quad \dim(W+W_d)=55.
\]

The known \(W_d\) therefore lies in the candidate set
\[
\mathcal C(W)=\{M\le L_4:M\text{ is }H\text{-stable},\dim M=45,\dim(M\cap W)=35\},
\]
subject to the already-established exact H-stability of its orbit construction.

## Exhaustiveness status

**NOT YET EXHAUSTIVE.** The present computation is a scaffold/guard only. Consequently it does not establish uniqueness of \(W_d\), nor does it establish that another candidate exists.

## Next exact task

Replace the scaffold with an exhaustive module-theoretic candidate enumeration (MeatAxe/invariant-submodule or an equivalent exact extension-space calculation), with explicit verification of every candidate and an exhaustiveness certificate.

## Status

INCONCLUSIVE BY DESIGN — no uniqueness claim.
