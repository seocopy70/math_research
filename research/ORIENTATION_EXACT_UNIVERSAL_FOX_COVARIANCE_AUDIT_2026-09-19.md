# HARD ATTACK 4 — COVARIANCE OF THE UNIVERSAL FOX OBSTRUCTION CARRIER — 2026-09-19

## Goal

Test whether the universal Fox obstruction row can survive the presentation ambiguities that defeated the earlier exact carrier candidates.

The key change is to use the **projective universal Fox row**, not a chosen relation generator.

For a minimal one-relator presentation (G=F/N), let
[
A=mathbf Z_3[[U_1,ldots,U_d]],qquad T_i=1+U_i,
]
and evaluate Fox derivatives through (x_imapsto T_i). The row
[
J_r=(J_1,ldots,J_d)
]
is considered projectively, up to multiplication by a unit of (A).

This completed coefficient ring is the correct enlargement if arbitrary pro-3 relation-module generator changes are allowed: the multiplier need not remain a Laurent polynomial, but it is a unit in the completed coefficient ring.

## 1. Relator conjugation — PASS

For (r'=uru^{-1}), the crossed-derivation/Fox product rule gives
[
D(r')=D(u)+	au(u)D(r)+	au(ur)D(u^{-1}).
]
Because (	au(r)=1),
[
	au(ur)=	au(u),qquad
D(u^{-1})=-	au(u)^{-1}D(u),
]
so the first and third terms cancel:
[
D(r')=	au(u)D(r).
]

Therefore
[
J_{uru^{-1}}=	au(u)J_r,
]
with (	au(u)in A^	imes). The projective zero locus is unchanged.

Decision: **PASS / CLOSED**.

## 2. Multiplication by a relation-module unit — PASS at the completed level

In a one-relator pro-3 relation module, changing the chosen generator of the cyclic relation module multiplies the generator by a unit. Applying the universal crossed-derivation boundary is (A)-linear, so the Fox obstruction row is multiplied by the image of that unit.

The required point is that the unit may live in the completed group algebra rather than the finite Laurent polynomial ring. This is exactly why the coefficient ring is upgraded to
[
A=mathbf Z_3[[U_1,ldots,U_d]].
]

Thus the projective class ([J_r]) is unchanged.

Decision: **PASS / CLOSED, conditional on the standard cyclic one-relator relation-module statement**.

This is not a claim that the raw relation-module generator is canonical; only its projective obstruction row is being retained.

## 3. Free-basis/Nielsen change — PASS at the universal-row level

Let (alpha:F_y	o F_x) be a free-group isomorphism and put (r_y=alpha^{-1}(r_x)). Fox's chain rule gives
[
rac{partial r_y}{partial y_j}
=
sum_i
alpha^{-1}!left(rac{partial r_x}{partial x_i}ight)
rac{partial alpha(x_i)}{partial y_j}.
]

After applying the universal abelian coefficient map, the row transforms as
[
J_{r_y}=J_{r_x}^{,alpha},M_alpha,
]
where (M_alpha) is the evaluated Fox Jacobian of the free isomorphism and (J_{r_x}^{,alpha}) is obtained by the induced formal torus substitution.

For a free isomorphism, the Fox Jacobian is invertible over the completed group algebra; after coefficient evaluation it remains invertible. Hence
[
J_{r_y}=0
quadLongleftrightarrowquad
J_{r_x}^{,alpha}=0.
]

The induced map on the coefficient torus is exactly the change of character coordinates
[
T_imapsto	au_y(alpha(x_i)).
]

Therefore the zero scheme is carried to the zero scheme under the presentation change.

Decision: **PASS / CLOSED at the universal Fox-calculus level**.

## 4. Consequence for intrinsicity

The previous exact-carrier obstruction was:

> the finite exact object was defined relative to a chosen relator/cover and its independence was not proved.

The universal Fox construction removes the two problematic choices simultaneously:

- relator conjugation/unit change acts by projective scalar;
- free-basis change acts by invertible coordinate substitution plus an invertible Jacobian.

Therefore the natural object is not a literal vector of coefficients but the **projective universal obstruction scheme**
[
oxed{
mathfrak X_G
=
left[
J_r=0
ight]
subset
operatorname{Hom}_{mathrm{cont}}(G,mathbf Z_3^	imes)
]
together with its presentation-independent projective Fox-Jacobian presentation.

The notation above is shorthand for the functor represented locally by the completed coefficient algebra and the Fox obstruction ideal; it is not a claim that the orientation is inserted into the definition.

## 5. Remaining hard point

One final distinction must not be blurred.

The construction proves presentation covariance of the **universal obstruction scheme**. It does not by itself prove that the scheme has a unique (1+3mathbf Z_3)-valued point for every Demushkin group.

For the frozen rank-4 q=3 group, uniqueness was proved explicitly:
[
T_1=T_3=T_4=1,qquad T_2=-1/2.
]

For a general Demushkin group, uniqueness is supplied by the standard canonical-orientation characterization (Labute/duality), not by the Fox scheme alone.

Thus the logical chain is now:

[
oxed{
	ext{intrinsic universal Fox obstruction scheme}
Longrightarrow
	ext{candidate character locus}
Longrightarrow
	ext{unique canonical point (external theorem)}
Longrightarrow
chi.
}
]

The first arrow is the new carrier result; the last uniqueness arrow is not being claimed as a new classification theorem.

## 6. Final status

- universal Fox row, fixed presentation: **PASS / CLOSED**;
- projective relator-gauge covariance: **PASS / CLOSED**;
- free-basis covariance via Fox chain rule: **PASS / CLOSED** at the universal-calculus level;
- intrinsic universal obstruction-scheme candidate: **PASS / CLOSED**, conditional on standard one-relator relation-module and completed Fox-calculus facts;
- fixed q=3 unique (3)-adic point: **PASS / CLOSED**;
- non-tautological exact characteristic-zero carrier: **PASS / CLOSED** in this new scheme-theoretic sense;
- finite two-component degree-(2,3) compression: **OPEN**;
- bounded finite-information carrier: still **FAIL / CLOSED**.

## 7. Important interpretation boundary

This result changes the previous endpoint.

We no longer need to say:

> “No non-tautological exact carrier has been found.”

That statement is now false.

The correct statement is:

> A non-tautological exact characteristic-zero carrier has been found, but its natural form is a universal projective Fox obstruction scheme, not a two-component filtered Lie jet.

The genuinely unresolved question is now whether this universal exact carrier admits a smaller intrinsic filtered/degree-(2,3) compression.
