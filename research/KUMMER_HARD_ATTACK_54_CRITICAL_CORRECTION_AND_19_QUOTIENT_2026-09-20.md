# HARD ATTACK 54 — CRITICAL CORRECTION: HA53 CLOSES THE HA52 d3 SURVIVAL CONCERN

Date: 2026-09-20

## Target

HA52 correctly established
\[
\dim E_3^{2,1}=19
\]
by showing that the exterior part of \(H^2(W,\mathbf F_3)\) contributes rank 36 to the incoming \(d_2\), while the fiber-Bockstein 9-dimensional summand is \(d_2\)-closed.

HA52 nevertheless left a warning that the 19-dimensional sector might later be affected by a \(d_3\)-type Bockstein phenomenon.

HA53 resolves this warning completely by bidegree alone.

## Correction

For the LHS spectral sequence of
\[
1\to W\to Q_2\to V\to1,
\]
\[
d_r:E_r^{p,q}\to E_r^{p+r,q-r+1}.
\]

For \((p,q)=(2,1)\) and every \(r\ge3\),
\[
E_r^{2+r,2-r}=0
\]
because \(2-r<0\). Hence there are no outgoing higher differentials.

An incoming differential would have source
\[
E_r^{2-r,r},
\]
which is zero because \(2-r<0\).

Therefore
\[
\boxed{E_3^{2,1}=E_\infty^{2,1}}
\]
and
\[
\boxed{\dim E_\infty^{2,1}=19}.
\]

The warning in HA52 that a \(d_3\) could still remove this particular \((2,1)\)-sector is therefore superseded. The cyclic-kernel \(d_3\)-Bockstein phenomenon remains real as a general LHS phenomenon, but it cannot act on this bidegree.

## Precise surviving object

The permanent piece is canonically represented by
\[
\mathcal S
:=
\frac{
\ker\bigl(
\mu:H^2(V,\mathbf F_3)\otimes K\to H^4(V,\mathbf F_3)
\bigr)
}{
\operatorname{im}\bigl(
d_2:H^2(W,\mathbf F_3)\to H^2(V,\mathbf F_3)\otimes W^*
\bigr)
},
\]
where
\[
K=\operatorname{im}
\bigl(d_2:W^*\to H^2(V,\mathbf F_3)\bigr),
\qquad \dim K=9.
\]

At the frozen \(q=3\) model,
\[
\dim H^2(V)=10,\quad
\dim H^4(V)=35,\quad
\dim K=9,
\]
and
\[
\operatorname{rank}\mu=35,
\qquad
\dim\ker\mu=90-35=55.
\]

HA51–52 give
\[
\dim\operatorname{im}d_2^{0,2}=36,
\]
so
\[
\boxed{\dim\mathcal S=55-36=19}.
\]

This description is preferable to treating “19” as an isolated numerical fact.

## Critical boundary

The following are NOT established:

1. \(\mathcal S\) is an orientation carrier.
2. \(\mathcal S\) has any particular decomposition such as \(10+9\).
3. \(\mathcal S\) is irreducible.
4. \(\mathcal S\) is naturally isomorphic to any previously computed 10-, 25-, 35-, or 45-dimensional module.
5. The twisted coefficient Bockstein \(\beta_\rho^2\) has been computed on \(\mathcal S\).

All such claims remain prohibited until an actual equivariant construction is supplied.

## New authorized attack

The next attack is representation-theoretic and must be constructive:

**A.** Prove that \(\mathcal S\) is an \(H\)-module by deriving the induced action on the exact kernel/image quotient.

**B.** Construct the action from the functorial action on the central extension, not from a dimension guess.

**C.** Determine composition factors or an explicit canonical short exact sequence only after A/B are established.

**D.** Then compute the twisted \(\beta_\rho^2\) map on this exact permanent piece.

No numerical identification by dimension alone is authorized.

## Decision

- HA52 \(d_2\)-calculation: **PASS / CLOSED**.
- HA53 permanence: **PASS / CLOSED**.
- HA52 warning “a \(d_3\) may still remove the 19-dimensional sector”: **HISTORICAL / SUPERSEDED**.
- \(\mathcal S\) as a canonical 19-dimensional LHS filtration piece: **PASS / CLOSED**.
- H-module structure of \(\mathcal S\): **OPEN / LOAD-BEARING**.
- twisted \(\beta_\rho^2\) on \(\mathcal S\): **OPEN / LOAD-BEARING**.
- orientation-selector interpretation: **OPEN / DECISIVE**.
