# PAPER 4 — CORRECTION + NEXT NONABELIAN GATE — 2026-10-02

## A. Correction of the previous kernel-shear audit

The earlier whole-package shear no-go overclaimed. The intrinsic map
P_E:L(X)->A, P_E(xbar)=x~^{e(X)}, is a restricted-power map and cannot be treated as pointwise fixed under an arbitrary shear of U.

Therefore the earlier claim that the shear g_c fixes the entire package (U,O,A,P_E,Phi) is NOT justified as written. That classification is HISTORICAL/SUPERSEDED.

The kernel facts remain valid:
k=u-s-t is in ker Phi, while omega_q(k)=-1 != 0 for odd p.
Hence omega_q does not descend through U/ker Phi.

## B. Corrected status

The correct conclusion is:
- ker Phi alone is not an orientation carrier;
- the full P_E+Phi package has NOT been closed by the earlier shear argument;
- a whole-package no-go would require an automorphism of the structured pair, including the transported restricted-power map.

Thus the previous absolute closure of the full linear package is withdrawn.

## C. Convention correction

For oriented pro-p RAAGs, absence of an edge does not mean commutation. Ordinary edges give commutation, while a special edge w->u gives w u w^{-1}=u^{1+q}. This is stated in the literature. 

Therefore any prior explanation of the separated accidental direction saying that t commutes with a is incorrect.

The valid mechanism is lower-filtration contamination: t has no special q-defect with a, but its commutator with a begins at a lower filtration degree. The q-layer projection can discard that lower term, producing the apparent false positive.

## D. New nonabelian gate

The next observable is the full filtered commutator profile before q-layer projection.

For u in U and origin x in O, retain the intrinsic condition
[u,x] in D_q
rather than projecting immediately to the q-layer.

When this holds, define c_x(u) by
[u,x] = c_x(u) P_E(x) mod D_{q+1}.

For specially oriented RAAGs:
- lower-degree vanishing forces the supported vertices of u to be joined to x;
- special neighbors contribute their coefficients;
- ordinary neighbors contribute zero;
- hence, when all special support is visible from x, c_x(u)=omega_q(u).

This separates the separated-model false positive s+t: its q-layer projection may retain the s contribution, but the full commutator has a lower-degree contribution from t, so s+t is not q-flat with a.

In the overlapping common-sink model, if s and t are both special neighbors of a, then s+t is genuinely q-flat and its q-defect is 2P_E(a). Normalizing to P_E(a) forces coefficient sum 1, so omega_q=1.

## E. Remaining theorem

Let Q_q be the set of pairs (u,x) with x in O, [u,x] in D_q, and q-defect P_E(x).

The load-bearing question is whether these normalized q-flat pairs determine a unique global linear functional omega_q on U.

A positive result needs a spanning/extension theorem. A negative result needs an admissible model with identical normalized filtered profiles but different omega_q.

The decisive test models are:
1. separated two-sink;
2. overlapping common-sink;
3. complete one-sink;
4. three-special-vertex chordal tree.

No large scan is authorized.

Classification:
- kernel-only branch: FAIL / CLOSED;
- previous whole-linear-package shear closure: HISTORICAL / SUPERSEDED;
- lower-filtration + q-defect profile: OPEN / LOAD-BEARING;
- Paper 4: OPEN.
