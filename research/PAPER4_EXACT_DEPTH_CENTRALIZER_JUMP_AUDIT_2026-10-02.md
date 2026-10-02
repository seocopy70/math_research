# PAPER 4 — EXACT-DEPTH CENTRALIZER JUMP / ORDINARY CONTAMINATION TEST — 2026-10-02

## Final result of the current gate

The naive quotient of the entire degree-2 sector is rejected as the wrong abstraction.

A sharper intrinsic object is the **exact-depth centralizer jump**. For u in L_1=D_1/D_2 and m>=2, define
\[
C_m(u)=\{x\in L_1:[\tilde u,\tilde x]\in D_m\}.
\]
Then the degree-q special incidence is represented by
\[
J_q(u):=C_q(u)/C_{q+1}(u).
\]

This is the correct filtration-theoretic distinction:
- an ordinary edge gives commutator depth infinity, hence belongs to C_{q+1};
- a special edge gives exact depth q, hence contributes to C_q but not C_{q+1};
- a nonedge has depth 2 and does not enter C_q.

Therefore ordinary edges are not “subtracted” by a presentation-dependent quotient: they disappear automatically because the construction records the **jump at the exact special depth**.

## Explicit checks

### Mixed ordinary/special graph

For
\[
G=\langle a,b,s\mid [a,b]=1,;sas^{-1}=a^{1+q}\rangle,
\]
one gets
\[
C_q(\bar a)=\langle\bar a,\bar b,\bar s\rangle,
\qquad
C_{q+1}(\bar a)=\langle\bar a,\bar b\rangle,
\]
so
\[
J_q(\bar a)=\mathbf F_p\bar s.
\]
For \(\bar b\),
\[
C_q(\bar b)=C_{q+1}(\bar b)=\langle\bar a,\bar b\rangle,
\]
so \(J_q(\bar b)=0\).

This is the cleanest ordinary-vs-special test found so far.

### RP-5

For A=(a,s),(b,s):
\[
J_q(\bar a)=\mathbf F_p\bar s,
\qquad
J_q(\bar b)=\mathbf F_p\bar s.
\]

For B=(a,s),(b,t):
\[
J_q(\bar a)=\mathbf F_p\bar s,
\qquad
J_q(\bar b)=\mathbf F_p\bar t.
\]

Thus RP-5 separation survives in a strictly finer form than the previous rank-only cross-defect:
\[
\boxed{\text{the exact-depth jump records origin-to-terminus incidence locally.}}
\]

### Complete one-sink graph

For
\[
G=\langle s,a,b\mid [a,b]=1,;sas^{-1}=a^{1+q},;bsb^{-1}=b^{1+q}\rangle
\]
the exact-depth construction gives
\[
J_q(\bar a)=\mathbf F_p\bar s,
\qquad
J_q(\bar b)=\mathbf F_p\bar s.
\]
For a general origin direction u=alpha\bar a+beta\bar b, the q-layer value against s is
\[
[\tilde u,\tilde s]\equiv
\alpha\bar a^{[q]}+\beta\bar b^{[q]}
\pmod{D_{q+1}},
\]
so no new special direction appears merely from the earlier Grassmannian accidental-plane phenomenon. The Grassmannian failure was therefore caused by forgetting the **target-labelled exact-depth map**, not by disappearance of the q-signal itself.

## q-blindness

Do not define q in advance. For every m define C_m(u), and let the nontrivial exact-depth spectrum be
\[
\Sigma(u)=\{m:C_m(u)\ne C_{m+1}(u)\}.
\]
For a special origin direction the relevant special jump is the first common positive jump detected across the corresponding incidence family. Thus q can be discovered from the finite filtration rather than inserted into the definition.

The global synchronization of the first jump is still a theorem requirement; local q-blindness is established.

## Functoriality and gauge

The definition uses only the intrinsic Zassenhaus filtration and commutators. Filtered isomorphisms preserve C_m(u), C_{m+1}(u), and J_m(u). Scaling u by a nonzero scalar leaves the projective centralizer data unchanged.

No generator labels, presentation relators, or lift choices occur in the definition.

## Critical issue that remains

The remaining problem is no longer “ordinary contamination”. It is **linear-combination cancellation**:

> Can a nonzero u which is not a genuine origin direction produce a spurious J_q(u), or can a genuine special incidence disappear because the q-layer values cancel?

The 2024 literature gives an important warning. Quadrelli proves that certain three-vertex induced configurations produce essential q-fold Massey products for a linear combination alpha=u^*+v^*, including configurations where the degree-2 incidence alone does not reveal the higher obstruction. citeturn14view0 This does not directly compute J_q(u), but it proves that higher-q behaviour of linear combinations is a real phenomenon and cannot be dismissed as a technicality.

Therefore the centralizer-jump purity theorem remains load-bearing.

## Important literature boundary

The same literature explicitly states that H^1 and H^2 of oriented pro-p RAAGs are determined by the incidence structure, while q-fold Massey products detect the stronger special-clique property. citeturn13view0 This strongly supports the methodological direction “quadratic layer -> higher filtered obstruction”, but it also means that a claim that the Paper-4 carrier is already a known Massey invariant would be an overclaim.

## Current classification

- naive global quotient W_2^ord: **FAIL / CLOSED as the primary abstraction**;
- exact-depth centralizer jump J_m(u): **PASS / LOCAL**;
- ordinary/special separation in mixed model: **PASS / LOCAL**;
- RP-5 incidence separation: **PASS / LOCAL, strengthened**;
- complete one-sink stress test: **PASS / LOCAL**;
- q-blind local definition: **PASS / LOCAL**;
- linear-combination purity: **OPEN / LOAD-BEARING**;
- arbitrary graph incidence reconstruction: **OPEN**;
- full orientation reconstruction: **OPEN**.

## Decision

The ordinary-contamination gate has been materially advanced: **we no longer need to quotient the ordinary degree-2 sector globally. Exact filtration depth itself separates ordinary edges from special q-defects.**

The decisive next theorem is now narrowly stated:

\[
\boxed{
J_q(u)\ne0
\quad\Longleftrightarrow\quad
u\text{ carries genuine special-edge incidence,}
}
\]
with the correct formulation allowing linear-combination/projective directions and possible multi-neighbor support.

No large scan is authorized before this purity theorem is resolved.

Paper 4 therefore remains **OPEN / LOAD-BEARING**, but the main bottleneck has been reduced from an undefined quotient problem to a precise one-direction exact-depth theorem.
