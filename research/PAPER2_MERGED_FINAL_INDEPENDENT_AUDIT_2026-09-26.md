# Paper 2 + absorbed Paper 3 — final independent audit — 2026-09-26

## Scope

Independent final audit performed after the Paper 3 application corpus was absorbed into
Paper 2 on branch `paper2-paper3-merged-2026-09-26`.

Controlling manuscript:
- `paper/successor_main.tex`
- final head commit: `0194e01176ae1c21fc70858be3797eeb1a3e7c18`

## Pre-check

Object: affine crossed-cocycle representations
\[
\psi=(z,\rho):G\to A_k\rtimes U_{1,k},
\qquad A_k=\mathbf Z/p^k.
\]

Input: the full affine representation category; no q is inserted into the
factorization statement.

Functoriality: Zassenhaus filtration is functorial under continuous homomorphisms.

Gauge/orientation boundary: presentation coordinates are used only for explicit
sharpness and marked-quotient examples; the upper factorization theorem is intrinsic.

Separation: the paper explicitly separates factorization from orientation recognition
and states the free-pro-p counterexample only for the Kummer predicate, not for every
possible selector.

Novelty boundary: the claim is restricted to the exact affine target calculation and
sharpness statement; canonical Demushkin orientation itself is not claimed as new.

## Independent mathematical checks

### 1. Target filtration

The manuscript proves
\[
P_n(A_k\rtimes U_{1,k})
=
p^{e(n)}A_k\rtimes U_{e(n)+1},
\qquad e(n)=\lceil\log_p n\rceil.
\]
The endpoint
\[
P_{p^{k-1}}\ne1,\qquad P_{p^{k-1}+1}=1
\]
is consistent with the Zassenhaus/Jennings product.

**PASS / CLOSED.**

### 2. Arbitrary-candidate factorization

The homomorphism/cocycle identification
\[
(z,\rho):G\to A_k\rtimes U_{1,k}
\]
and functoriality give factorization through
\[
G/P_{p^{k-1}+1}(G).
\]

**PASS / CLOSED.**

### 3. Sharpness

For f<k, the canonical orientation together with z(x_1)=1 gives
z(x_1^{p^{k-1}})=p^{k-1}.

For f>=k, the independent witness
\[
\rho(x_2)=1+p,\qquad z(x_2)=1
\]
has nonzero value on x_2^{p^{k-1}} by LTE. It works already in rank two,
so no hidden d>=4 hypothesis is being used.

**PASS / CLOSED.**

### 4. Paper 3 absorption

The free-product section does not enter the proof of the sharp affine theorem.
It is a genuine consequence/application layer:
- reflected Zassenhaus truncation preserves finite free pro-p coproducts;
- mixed commutators are absorbed by the reflected P_n-kernel;
- the finite-depth f-profile is a marked finite-quotient consequence;
- the heterogeneous example is illustrative rather than load-bearing;
- blockwise Kummer recognition is explicitly restricted to finite free pro-3
  products of rank-four q=3 Demushkin blocks and uses Paper 1 as an input.

**PASS / CLOSED.**

### 5. Redundancy

The former Paper 3 does not contain an independent publication-level theorem
after separation of imported results from genuinely new content. Absorption is
therefore logically cleaner and does not weaken Paper 2's independent core.

**PASS / CLOSED.**

### 6. Prior-art boundary

The audited literature supports the classical status of canonical Demushkin
orientation/Kummerian theory and the general Zassenhaus representation framework.
A targeted search for the exact combined statement
\[
n_{\mathrm{aff}}(k)=p^{k-1}+1
\]
in the present affine target category did not locate an earlier theorem stated
in this form. This is a defensible boundary, not an absolute priority claim.

**CONDITIONAL / publication-level novelty.**

## Final decision

- Manuscript mathematical core: **PASS / CLOSED**
- Paper 3 absorption: **PASS / CLOSED**
- Independent referee gate: **PASS / CLOSED**
- Novelty/redundancy gate: **PASS / CLOSED for the structural decision**
- Exact publication novelty: **CONDITIONAL**
- Absolute carrier minimality: **not claimed**
- Broader elementary-type uniformity: **not claimed**
- Final CI for commit `0194e01176ae1c21fc70858be3797eeb1a3e7c18`: **PASS**
- Final merged manuscript PDF: **PASS**

No further mathematical repair is authorized or presently indicated before
submission. Remaining work is venue selection and submission metadata, plus any
venue-specific formatting requirements.
