# PAPER 4 — T1 MULTI-SINK / SCALE-FIXING AUDIT — 2026-10-02

## Decision

The critical scale objection is real, but the common-sink and multi-sink calculation gives a stronger resolution than the previous 2-generator argument.

The finite window need not normalize a projective line by an arbitrary basis choice. It can, in the local special-edge model, **select the actual vector on that line**: the unique vector whose first q-defect against an intrinsic origin q-power equals the normalized generator q-power itself. Thus the scale is fixed by the extension data, not by an external basis rescaling.

This is PASS / LOCAL only. The remaining global issue is whether this local selection is intrinsic and whether multi-sink linear combinations are excluded.

## 1. Common-sink calculation

Take
  G=<v_1,...,v_m,w | [v_i,v_j]=1, w v_i w^{-1}=v_i^{1+q}>.

At degree one:
  L_1=<bar v_1,...,bar v_m,bar w>.

The origin sector is
  O_q=<bar v_1,...,bar v_m>,

so
  U_q=L_1/O_q=<bar w>.

The first q-defect satisfies
  B_q(bar w,bar v_i)=overline{v_i^q}
for every i.

Now replace bar w by lambda bar w, lambda in F_p^*. The defect becomes
  lambda overline{v_i^q}.

Since the q-power classes overline{v_i^q} are independently determined by the restricted-power structure of the origin sector, lambda=1 is forced by equality with the normalized q-power vector. Therefore the finite extension data distinguish the canonical vector bar w from its nonzero scalar multiples.

This resolves the specific 2-generator scale objection at the local level.

## 2. What the scale argument does NOT prove

It does not prove that the origin q-power class is itself canonically normalized in an arbitrary abstract window. The argument only shows:

  **conditional local statement:** once the intrinsic restricted-power target is identified, the special direction has a unique scale.

Thus the earlier status must be corrected from "2-generator normalization PASS / LOCAL" to:

  coefficient observability: PASS / LOCAL;
  scale fixing relative to intrinsic q-power target: PASS / LOCAL;
  existence of the intrinsic q-power target in the general T1 input: OPEN.

## 3. Multiple-sink control

Consider a specially oriented graph with distinct special vertices w_1,...,w_r and ordinary origin vertices. For each sink w_j choose an ordinary origin v_{j,a} with a special edge (v_{j,a},w_j). Assume initially that there are no cross-relations connecting distinct sink components; this is the minimal multi-sink control.

Modulo O_q, write
  U_q=span_Fp{bar w_1,...,bar w_r}.

For
  u=sum_j alpha_j bar w_j
and an origin direction v_{j,a}, the first q-defect has component
  alpha_j overline{v_{j,a}^q}.

If at least two alpha_j are nonzero and the corresponding q-power targets are independent, then the defect has rank at least two across the origin sectors. Hence the local special-edge signature, which requires a rank-one target aligned with one origin q-power sector, excludes generic sums of distinct sink directions.

Therefore the candidate set P_q can, in these controls, recover the individual normalized sink vectors rather than merely their span.

## 4. The key remaining ambiguity

There is one nontrivial possibility: two sink directions could share enough origin q-power target data that a linear combination still has rank-one defect.

This is not excluded by the abstract rank argument alone. It requires the actual graph/filtered structure to show that distinct sink directions have sufficiently independent origin sectors, or else a different intrinsic invariant must separate them.

Hence:
  rank-one accidental-direction exclusion: OPEN.

## 5. Symmetry / filtered-isomorphism test

Permuting two indistinguishable sink components preserves the set
  {bar w_1,...,bar w_r}
and also preserves the functional
  omega_q(sum alpha_j bar w_j)=sum alpha_j.

Thus graph automorphism symmetry does not create a normalization ambiguity: the desired functional is symmetric under sink permutation.

A dangerous filtered automorphism would instead have to send
  bar w_1 -> bar w_1 + c bar w_2
while preserving all first-defect data. In the minimal separated multi-sink model, the defect against an origin attached only to w_1 detects c, so such a shear is not an automorphism of the filtered pair. This is a useful local obstruction to GL_r gauge freedom.

## 6. Revised T1 formal statement

The correct target is now not "normalize a projective direction" but:

  **intrinsically identify the affine set of normalized sink vectors**
  S_q subset U_q

by the finite extension data, where each s in S_q is characterized by a rank-one special-edge defect whose target is a restricted-power class of O_q.

Then define omega_q by
  omega_q(s)=1 for all s in S_q.

The logical order is:

  W_q <- W_{q+1}
    -> O_q
    -> intrinsic q-power target(s)
    -> normalized sink vectors S_q
    -> omega_q.

No arbitrary basis normalization is allowed.

## 7. New failure criterion

T1 closes if either:

1. there exists a multi-sink model with an accidental normalized vector
   u not equal to a sink direction but having the same intrinsic rank-one special-edge signature; or
2. there are two specially oriented RAAGs with isomorphic adjacent windows for which the induced normalized sink-vector sets, hence omega_q, differ; or
3. the restricted-power target required to fix scale cannot itself be recovered q-blindly from the adjacent window.

The third condition is now the cleanest possible bottleneck.

## 8. Classification

- common-sink coefficient observability: PASS / LOCAL;
- common-sink scale fixing relative to q-power target: PASS / LOCAL;
- separated multi-sink rank test: PASS / LOCAL;
- sink permutation symmetry: harmless / PASS / LOCAL;
- shear-gauge obstruction in separated control: PASS / LOCAL;
- intrinsic q-power target in general window: OPEN / LOAD-BEARING;
- rank-one accidental-direction exclusion in general: OPEN / LOAD-BEARING;
- filtered-isomorphism invariance of S_q: OPEN / LOAD-BEARING;
- T1: OPEN / LOAD-BEARING.

## Next authorized attack

Do not return to 2-generator normalization or search for a new carrier.

The next decisive calculation is to construct the smallest **overlapping multi-sink model**, where two sinkholes share one or more origin sectors, and determine whether the intrinsic q-power targets remain separable. If an accidental rank-one direction appears, T1 closes. If not, the next task is the q-blind intrinsic construction of the target set S_q itself.
