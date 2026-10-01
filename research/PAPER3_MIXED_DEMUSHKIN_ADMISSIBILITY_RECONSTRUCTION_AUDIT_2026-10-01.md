# MIXED FOX — DEMUŠKIN ADMISSIBILITY / EXTENSION-FIBER RECONSTRUCTION AUDIT — 2026-10-01

## Scope

This audit attacks the load-bearing prerequisite exposed by the broad same-pair no-go:

- define the admissible category precisely;
- determine whether the forgetful map
  \[
  U:\mathbf{ExtWin}_k^{\mathrm{Dem}}\to\mathbf{Pair}_k
  \]
  has nontrivial fibers;
- do not use the arbitrary central-extension counterexample as evidence against the Demuškin category.

The active project is the odd-prime standard finite-rank Demuškin family relevant to the mixed (3,I)-adic branch. For p=3, fix even rank d (in particular the rank-4 family used by the project), and
\[
N_k=3^{k-1}+1.
\]
For an infinite Demuškin group G of this standard odd-p type,
\[
Q_k=G/D_{N_k},\quad E_k=G/D_{N_k+1},\quad A_k=D_{N_k}/D_{N_k+1}.
\]

## 1. Admissible category

Define \(\mathbf{ExtWin}^{\mathrm{Dem}}_{k,d}\) to have as objects the canonical windows
\[
\mathsf W_k^{\mathrm{ext}}(G)
=(A_k\hookrightarrow E_k\twoheadrightarrow Q_k)
\]
arising from infinite odd-p Demuškin groups of fixed rank d, with q(G) in
\[
\{p^s:s\ge1\}\cup\{0\},
\]
where q=0 denotes the infinite-q case.

Morphisms are isomorphisms of the whole filtered extension diagram. The forgetful functor is
\[
U(\mathsf W_k^{\mathrm{ext}}(G))=(Q_k,A_k).
\]

This is the category needed for the project's original finite-pair question. It is deliberately narrower than the category of arbitrary finite central extensions.

The odd-p Demuškin classification states that the group is classified by rank and q, and admits the standard one-relator form
\[
r=x_1^q[x_1,x_2][x_3,x_4]\cdots[x_{d-1},x_d],
\]
with q a p-power or 0. citeturn2search0turn2search28

## 2. Fiber analysis: q < N_k

The Zassenhaus degree of the commutator part of r is 2, while the q-power term has Zassenhaus degree q.

Hence, when q<N_k, the quotient Q_k already sees the first q-dependent graded relation: the characteristic Zassenhaus filtration of Q_k contains the degree-q restricted relation defect.

Equivalently, the sequence of intrinsic graded dimensions
\[
\dim_{\mathbf F_p}D_j/D_{j+1},\qquad j<N_k,
\]
contains the first q-dependent drop at j=q.

The literature gives explicit dimension formulas for Zassenhaus graded pieces of Demuškin groups, so this is not presentation-local data. citeturn4academia13turn7view0

Therefore two standard odd-p Demuškin windows with isomorphic Q_k cannot have distinct q<N_k.

## 3. Fiber analysis: q = N_k

Here Q_k does not see the q-power term, because the q-dependent relation lies exactly at the next Zassenhaus layer.

But A_k does see it.

At degree N_k the q-power component contributes one additional relation to the free Demuškin graded object. Thus the intrinsic dimension of
\[
A_k=D_{N_k}/D_{N_k+1}
\]
differs by one from the q>N_k (including q=0) case.

Therefore the bare pair (Q_k,A_k) distinguishes q=N_k from q>N_k.

This is the only boundary case in which Q_k alone loses the parameter but A_k restores it.

## 4. Fiber analysis: q > N_k

If q>N_k, then the q-power term of the standard Demuškin relator is invisible modulo D_{N_k+1}.

Consequently the truncated presentations for all q>N_k (including q=0) have the same relation through the entire window
\[
G/D_{N_k+1}.
\]

Thus their extension windows are isomorphic:
\[
\mathsf W_k^{\mathrm{ext}}(G_q)
\cong
\mathsf W_k^{\mathrm{ext}}(G_{q'}),\qquad q,q'>N_k.
\]

So although Q_k and A_k do not determine q itself once q>N_k, they do determine the extension window because the extension window is already independent of q in this range.

## 5. Reconstruction conclusion

Combining the three cases gives the standard-family fiber statement:

\[
\boxed{
U^{-1}(Q_k,A_k)
\text{ is a singleton up to extension-window isomorphism}
}
\]

within \(\mathbf{ExtWin}^{\mathrm{Dem}}_{k,d}\).

More explicitly:

- q<N_k is recovered from Q_k;
- q=N_k is separated by dim A_k;
- q>N_k gives the same E_k anyway.

This is the key point the earlier audit was missing.

It means that the arbitrary-extension no-go does **not** propagate to the standard odd-p Demuškin category.

## 6. What this does and does not prove

It does prove a Demuškin-specific reconstruction statement at the level of the standard finite-rank family:

\[
(Q_k,A_k)
\Longrightarrow
[E_k\to Q_k]
\]
up to extension-window isomorphism.

It does **not yet** prove the full mixed Fox finite-pair theorem, because the second half still has to be written as a formal natural transformation:
\[
\mathsf W_k^{\mathrm{ext}}
\longrightarrow
\mathcal M_k^{\mathrm{mix}}
\]
and shown invariant under the relevant extension-window isomorphisms/projective gauge.

The existing weighted Magnus and stable Fox audits support that construction at PASS/LOCAL, but the categorical proof has not yet been promoted to PASS/CLOSED.

## 7. Consequence for the earlier “admissibility” critique

The critique was correct that “admissible” cannot remain an undefined word.

It is now possible to define it non-tautologically for the active branch:

> admissible = canonical Zassenhaus extension windows arising from infinite odd-p finite-rank Demuškin groups of the fixed rank under study.

This is much stronger than saying “extensions that happen to work,” and much narrower than arbitrary central extensions.

The resulting admissibility condition is mathematically substantive because it invokes the Demuškin classification and the canonical Zassenhaus filtration.

## Classification

- arbitrary finite central-extension pair descent: **FAIL / CLOSED** (broad-category statement only);
- admissible Demuškin category definition: **PASS / CLOSED** at the declared standard odd-p fixed-rank scope;
- Demuškin fiber reconstruction \((Q_k,A_k)\Rightarrow[E_k\to Q_k]\): **PASS / LOCAL** — structural proof complete at classification/graded-detection level; formal lemma packaging and edge-case audit remain;
- extension-window → mixed Fox: **PASS / LOCAL**;
- original finite-pair → mixed Fox: **OPEN / LOAD-BEARING**, but the previous “admissibility prerequisite” is now substantially discharged;
- genuine new-carrier status: **OPEN**;
- Paper 3: **FROZEN / COMPLETE**.

## Next authorized action

Do not construct a broad-category counterexample again.

The next decisive task is to write the reconstruction lemma formally and combine it with the already established extension-window → mixed Fox construction. Then independently check naturality/projective covariance.

If that succeeds, the Mixed Fox branch reaches **PASS / LOCAL** for the original finite-pair factorization at the declared standard Demuškin scope. Novelty/non-redundancy remains a separate question and must not be conflated with the descent theorem.
