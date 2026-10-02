# PAPER 4 — ARBITRARY LINEAR-DIRECTION TEST FOR J_q — 2026-10-02

## Question

Does the exact-depth centralizer jump
\[
J_q(u)=C_q(u)/C_{q+1}(u)
\]
remain a pure incidence detector for an arbitrary linear direction \(u\in L_1\), or do linear combinations create spurious q-incidence?

## Verdict

**A structural counterexample exists. The one-direction purity statement is false.**

The smallest decisive model is the already audited complete three-vertex specially oriented graph
\[
G=\langle s,a,b\mid [a,b]=1,\;sas^{-1}=a^{1+q},\;sbs^{-1}=b^{1+q}\rangle ,
\]
with \(s\) the special terminus and \(a,b\) ordinary origins.

Let
\[
L_1=D_1/D_2=\mathbf F_p\bar a\oplus\mathbf F_p\bar b\oplus\mathbf F_p\bar s.
\]
Modulo \(D_{q+1}\), the degree-q commutator defect is
\[
B_q(\bar a,\bar s)=\overline{a^q},\qquad
B_q(\bar b,\bar s)=\overline{b^q},\qquad
B_q(\bar a,\bar b)=0,
\]
up to the harmless sign determined by the commutator convention.

For an arbitrary
\[
u=\alpha\bar a+\beta\bar b+\gamma\bar s
\]
and
\[
x=\alpha'\bar a+\beta'\bar b+\gamma'\bar s,
\]
one obtains
\[
B_q(u,x)
=(\alpha\gamma'-\gamma\alpha')\overline{a^q}
 +(\beta\gamma'-\gamma\beta')\overline{b^q}.
\]

### Consequence 1: every nonzero linear direction has a q-jump

The alternating form above has zero radical. Indeed, if \(B_q(u,x)=0\) for every \(x\), then taking \(x=\bar s\) gives \(\alpha=\beta=0\), and taking \(x=\bar a\) gives \(\gamma=0\).

In this complete model every degree-1 pair commutator lies in \(D_q\), so
\[
C_q(u)=L_1.
\]
Moreover
\[
C_{q+1}(u)=\ker(B_q(u,-)).
\]
Hence
\[
J_q(u)\cong L_1/\ker(B_q(u,-))
\]
is nonzero for **every** nonzero \(u\in L_1\).

Thus \(J_q(u)\neq0\) is not equivalent to \(u\) being a genuine ordinary origin direction.

### Consequence 2: the smallest explicit spurious direction

Take
\[
u=\bar s+\bar a.
\]
This projective direction is not in the ordinary/origin plane
\[
O=\operatorname{span}(\bar a,\bar b).
\]
Nevertheless
\[
B_q(u,\bar a)=B_q(\bar s,\bar a)
=\pm\overline{a^q}\neq0,
\]
so
\[
J_q(\bar s+\bar a)\neq0.
\]

Even the pure sinkhole direction \(u=\bar s\) has
\[
B_q(\bar s,\bar a)=\pm\overline{a^q}\neq0,
\]
hence \(J_q(\bar s)\neq0\).

Therefore the failure is not an accidental cancellation phenomenon. It is a structural consequence of allowing arbitrary linear directions in the complete special graph.

## What exactly fails

The following proposed load-bearing statement is **FAIL / CLOSED**:
\[
J_q(u)\neq0
\quad\Longleftrightarrow\quad
u\text{ carries genuine special-edge incidence as an origin direction.}
\]

The exact-depth construction successfully removes ordinary-edge contamination, but it does **not** by itself classify degree-one directions into genuine graph vertices/origin directions.

The prior local checks
- mixed ordinary/special model,
- RP-5 A/B,
- complete one-sink model,

remain valid as pairwise q-depth calculations. What fails is the extrapolation from those calculations to a **one-direction purity theorem for arbitrary linear combinations**.

## Interpretation

The complete-graph counterexample also explains the earlier Grassmannian failure more precisely.

The q-layer is still present and highly structured; what is lost is vertex purity after passing from basis directions to arbitrary projective directions. In the complete one-sink model, the q-defect is an alternating map
\[
B_q:\Lambda^2 L_1\to
\operatorname{span}(\overline{a^q},\overline{b^q}),
\]
and its support is not the origin plane as a set of q-active projective points: every nonzero projective point is q-active.

So replacing a Grassmannian carrier by the scalar predicate \(J_q(u)\neq0\) does not repair the purity problem.

## Salvage boundary

A viable Paper-4 carrier must use more than the predicate \(J_q(u)\neq0\). At minimum it must retain some **target-labelled / pairwise / restricted-power anchoring** that distinguishes:

1. the origin plane \(O\subset L_1\),
2. the special terminus direction(s),
3. the incidence relation between them.

The previously observed restricted-power recovery
\[
P_q^{-1}(\operatorname{im}\kappa_q)=O
\]
in the complete one-sink/common-sink models is therefore still relevant. It cannot be replaced by the bare nonvanishing of \(J_q(u)\).

No claim is made here that the combined \((P_q,B_q)\) carrier succeeds globally; that is a separate object/intrinsicity/functoriality/gauge/separation audit.

## Classification

- exact-depth definition \(J_m(u)\): **PASS / LOCAL**;
- ordinary-edge removal by exact depth: **PASS / LOCAL**;
- RP-5 pairwise separation: **PASS / LOCAL**;
- arbitrary-linear-direction purity \(J_q(u)\neq0\iff u\) is a genuine origin direction: **FAIL / CLOSED**;
- linear-combination purity as the current bottleneck: **FAIL / CLOSED — the proposed formulation is false**;
- joint target-labelled / restricted-power refinement: **OPEN / LOAD-BEARING**;
- full directed-incidence reconstruction: **OPEN**;
- full orientation reconstruction: **OPEN**.

## Next authorized action

Do not attempt to prove the false purity theorem or merely enlarge the scan.

The next branch must redefine the carrier so that arbitrary linear directions are handled structurally, most naturally by testing whether the pair
\[
(P_q,\,B_q)
\]
or an equivalent intrinsic extension-class object admits a q-blind, functorial reconstruction of the origin subspace and the directed incidence relation.

