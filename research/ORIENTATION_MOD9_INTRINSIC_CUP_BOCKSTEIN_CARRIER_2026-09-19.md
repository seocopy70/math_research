# Intrinsic carrier via cup-product and Bockstein — 2026-09-19

## Status

**PASS / CLOSED at the mod-9 carrier level.**

The previously closed statement that the ordinary Bockstein does not by itself recover chi mod 9 is retained. The new result is stronger and different:

> The pair consisting of the intrinsic cup-product pairing and the intrinsic Bockstein map canonically reconstructs the coarsest degree-(2,3) recovery carrier \(\overline J_3=[(R,p(P))]\), without choosing a free presentation, a preferred lift, a top-class generator, or inserting q.

Thus the Bockstein is not sufficient alone, but it is precisely sufficient when combined with the quadratic cup-product relation already present in the Demushkin cohomology.

## 1. Intrinsic input

Let
\[
V=H^1(G,\mathbf F_3)^*.
\]
For a rank-4 Demushkin group,
\[
\dim_{\mathbf F_3}H^2(G,\mathbf F_3)=1,
\]
and the cup product is a nondegenerate alternating pairing
\[
\smile:H^1(G,\mathbf F_3)\times H^1(G,\mathbf F_3)\to H^2(G,\mathbf F_3).
\]

Let
\[
\beta:H^1(G,\mathbf F_3)\to H^2(G,\mathbf F_3)
\]
be the canonical Bockstein for
\[
0\to\mathbf F_3\xrightarrow{3}\mathbf Z/9\to\mathbf F_3\to0.
\]

Both maps are intrinsic to G and the coefficient sequence.

## 2. Extracting the projective pair

Choose temporarily a nonzero top-class generator \(\omega\in H^2(G,\mathbf F_3)\). There are unique
\[
R\in\Lambda^2V,\qquad p\in V
\]
such that
\[
f\smile g=(f\wedge g)(R)\,\omega,
\]
and
\[
\beta(f)=f(p)\,\omega.
\]

More precisely, because the degree-3 restricted-cube layer is Frobenius-twisted, the second component should be regarded as
\[
p\in V^{(1)}
\]
rather than as an ordinary V-vector.

If \(\omega' = u\omega\), then
\[
R' = u^{-1}R,\qquad p'=u^{-1}p.
\]
Therefore the projective pair
\[
\boxed{\overline J_3(G):=[(R,p)]}
\]
is independent of the arbitrary choice of \(\omega\).

This is exactly the common-unit projective ambiguity of the relation-jet carrier.

## 3. Identification with the filtered relation jet

For a minimal one-relator pro-3 presentation with filtered relator
\[
r=(R_2,P_3)+O(4),
\]
the standard transgression/Bockstein calculation gives, in the frozen convention,
\[
R=R_2,
\qquad
p=p(P_3)
\]
up to the same common scalar determined by the choice of generator of \(H^2\).

For the q=3 normal form,
\[
R=[X_1,X_2]+[X_3,X_4],
\qquad
p=X_1^{(1)}.
\]
For q=\infty,
\[
R=[X_1,X_2]+[X_3,X_4],
\qquad
p=0.
\]

Thus the intrinsic cohomological pair \(([R],[p])\) and the previously constructed filtered relation carrier \(\overline J_3\) agree at the mod-3 degree-(2,3) information level.

## 4. Recovery functional

The carrier determines the same intrinsic evaluation family
\[
\overline\Theta_{(R,p)}(\lambda)(f)
=
f(p)+(\lambda\wedge f)(R).
\]

Because R is nondegenerate, the map
\[
\Phi_R:V^*\to V^*,\qquad
\Phi_R(\lambda)(f)=(\lambda\wedge f)(R)
\]
is an isomorphism.

Hence there is a unique zero \(\lambda_\chi\) satisfying
\[
f(p)+(\lambda_\chi\wedge f)(R)=0
\quad\forall f.
\]

For the q=3 normal form this gives
\[
\lambda_\chi=e_2^*,
\]
and therefore
\[
\chi(x_1),\chi(x_2),\chi(x_3),\chi(x_4)
\equiv(1,4,1,1)\pmod9.
\]

For q=\infty, \(p=0\), so \(\lambda_\chi=0\) and the corresponding first nontrivial orientation layer is trivial.

## 5. What was closed and what is newly established

The earlier Bockstein audit remains correct:

- \(\beta\) alone does not canonically contain the scalar 4 in \((\mathbf Z/9)^\times\);
- changing the top-class generator rescales Bockstein coordinates;
- Bockstein alone is therefore **FAIL / CLOSED** as a mod-9 orientation carrier.

The new theorem-level combination is:

\[
\boxed{
(\text{cup product},\beta)
\Longrightarrow
\overline J_3=[(R,p)]
\Longrightarrow
\chi\bmod9.
}
\]

Thus the information loss was not in the Bockstein mechanism itself, but in discarding the quadratic symplectic relation that supplies the inverse pairing \(\Phi_R^{-1}\).

## 6. Intrinsicity / functoriality

Both cup product and Bockstein are natural under group isomorphisms and coefficient maps. The projective common-scaling ambiguity is exactly removed by passing to \([(R,p)]\).

No free-group lift, preferred Nielsen lift, q-label, or chosen top-class generator survives in the definition.

This supplies the missing intrinsic carrier functor at the mod-9 level:
\[
\boxed{
G\longmapsto
\overline J_3(G):=[(R_G,p_G)]
}
\]
constructed from \(H^1(G,\mathbf F_3)\), \(H^2(G,\mathbf F_3)\), the cup product, and the canonical Bockstein.

## 7. Logical boundary

This result does **not** prove:

1. a full 3-adic intrinsic carrier functor from only cup/Bockstein data;
2. recovery of all \(\chi\bmod 3^n\) from ordinary mod-3 Bockstein data;
3. a non-tautological finite exact \(\mathbf Z_3\)-carrier;
4. equivalence with the Pál–Quick A3/Hochschild canonical class.

The result is specifically the mod-9 carrier/factorization theorem.

## 8. Decision

**PASS / CLOSED — M1 at the mod-9 level.**

The intrinsic carrier can be defined directly from canonical cohomological data:
\[
(H^1,H^2,\smile,\beta)
\mapsto
[(R,p)]
\mapsto
\chi\bmod9.
\]

The standalone Bockstein candidate remains **FAIL / CLOSED**.

The next structural target is therefore M3: compare this intrinsic \((\smile,\beta)\)-carrier with the independent Pál–Quick A3/Hochschild canonical class, or prove a structural obstruction to a natural factorization. No broad computational scan is authorized.
