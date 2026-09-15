# Phase 2-6 / A — Final computational result

Date: 2026-09-15

## A-stage question

Let
\[
W=\langle Sp_4(\mathbb F_3)\cdot[T]\rangle\subset Q_4
\]
and let
\[
N\in\operatorname{End}_{Sp_4(\mathbb F_3)}(W)
\]
be the non-scalar nilpotent endomorphism found in Phase 2-3, with
\[
N^2=0,\qquad \operatorname{rank}N=10.
\]
Set
\[
U=\operatorname{im}N.
\]
Then \(\dim U=10\). The purpose of A was to identify U with the 10-dimensional simple module \(L(2,0)\).

## Model used for L(2,0)

The direct WeylModules computation established that
\[
\Delta(2,0)
\]
has dimension 10 and only its highest-weight maximal vector, hence it is simple:
\[
\Delta(2,0)=L(2,0).
\]

For the finite group calculation we use the natural 4-dimensional symplectic module \(V=\mathbb F_3^4\) and the explicit model
\[
L(2,0)\cong \operatorname{Sym}^2(V).
\]

The symmetric-square basis is
\[
x_1^2,x_1x_2,x_1x_3,x_1x_4,x_2^2,x_2x_3,x_2x_4,x_3^2,x_3x_4,x_4^2.
\]

Crucially, the same five symplectic transvections used in Phase 2-1 were used both for the action on U and for the \(\operatorname{Sym}^2(V)\) model. This avoids any convention mismatch between Chevalley/root-group generators and the finite-group generators.

## Exact computation

The Phase 2-6 script constructs:

1. the 10-dimensional basis of \(U=\operatorname{im}N\);
2. the five restricted 10×10 matrices describing the \(Sp_4(\mathbb F_3)\)-action on U;
3. the five 10×10 matrices for \(\operatorname{Sym}^2(V)\);
4. the simultaneous intertwiner system
\[
P A_i^U=A_i^{\operatorname{Sym}^2(V)}P,
\qquad i=1,\dots,5.
\]

The system has shape
\[
500\times100.
\]

The exact finite-field nullspace computation gives
\[
\boxed{\dim_{\mathbb F_3}\operatorname{Hom}_H(U,L(2,0))=1.}
\]

Moreover, the one-dimensional Hom-space contains a rank-10 intertwiner. Therefore
\[
\boxed{U\cong L(2,0)\cong\operatorname{Sym}^2(V).}
\]

This result was actually executed in GitHub Actions; it is not a hypothetical or unrun calculation.

Workflow run:
`34944075109`

Artifact:
`10386805095`

Artifact SHA-256:
`ae891dd9f5b0b479582a0c363e6b41199c4cb220a96b5503045d540f70a630a6`

## What is now proved computationally

The Phase 2 representation-theoretic chain now includes the exact identification
\[
\boxed{\operatorname{im}N\cong L(2,0).}
\]

Together with Phase 2-3:
\[
0\subset U\subset K\subset W,
\]
\[
\dim U=10,\quad \dim K=35,\quad \dim W=45,
\]
\[
N^2=0,\quad W/K\cong U,
\]
and hence the outer layers are both \(L(2,0)\).

The remaining middle layer is
\[
M=K/U,
\qquad \dim M=25.
\]
Its identification with \(L(2,1)\) is strongly supported by the Weyl-module computation but is not yet recorded here as a direct finite-group intertwiner theorem.

## Next step

The next decisive representation-theoretic task is therefore:

\[
\boxed{M=K/U\stackrel{?}{\cong}L(2,1).}
\]

After that, the main target becomes a direct proof of
\[
\boxed{W\cong T(2,1)}
\]
or an explicit demonstration that W is a different 45-dimensional indecomposable module with the same composition factors.

Only after this distinction is settled should the representation-theoretic result be fed back into the original canonical-orientation question.

## Logical safeguard

The statement
\[
W\cong T(2,1)
\]
is still a hypothesis. The A-stage result proves only the 10-dimensional layer identification. It does not by itself prove the tilting-module identification or recover the Demuškin orientation.
