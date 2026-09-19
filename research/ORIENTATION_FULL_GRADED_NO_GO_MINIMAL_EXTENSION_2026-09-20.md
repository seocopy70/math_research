# HARD ATTACK 13 — FULL ASSOCIATED-GRADED NO-GO / MINIMAL EXTENSION LOWER BOUND — 2026-09-20

## Target

The previous attack distinguished the associated-graded tower from an actual compatible filtered lift. The stronger question is whether the *entire* associated-graded Zassenhaus object, with no degree cutoff, might nevertheless determine the Demushkin orientation.

This must be attacked before speaking about a lower bound on extension data.

## 1. The decisive literature-level check

For an infinite Demushkin pro-(p) group with (p) odd, the complete graded group algebra associated with the (p)-Zassenhaus filtration is determined by the quadratic initial relation. In the standard rank-(d) case its defining graded relation is

[
[X_1,X_2]+[X_3,X_4]+cdots+[X_{d-1},X_d],
]

independently of the Demushkin invariant (q).

Mináč–Pasini–Quadrelli–Tân prove that for Demushkin groups

[
operatorname{gr}mathbf F_p[[G]]cong U(L(G))
]

is quadratic/PBW and give precisely this quadratic presentation for odd (p). The same source recalls that (q) is a separate invariant encoded by the canonical orientation. citeturn3search0turn2search0

Thus, in the present rank-four odd-prime setting,

[
G_3, G_9, G_{27},ldots, G_infty
]

have the same type of full (mathbf F_3)-associated graded object, while

[
chi_{3^s}(x_2)=(1-3^s)^{-1}
]

varies with (s), and (chi_infty(x_2)=1).

This is substantially stronger than the previous finite-window argument.

## 2. Important correction to the conceptual wording

The earlier statement

> “associated graded data loses extension/gluing information”

was correct as a general filtered-algebra slogan, but too weak for this project.

The project-specific statement can now be sharpened to:

[
oxed{
	ext{For odd-prime Demuškin groups, the full mod-}3
	ext{ Zassenhaus graded object is already }q	ext{-blind.}
}
]

So there is no need to rely only on a bounded-degree counterexample.

In particular, no construction whose input is *only* the full mod-3 associated graded Demuškin object can recover even the invariant (q), hence cannot recover the canonical (mathbf Z_3^	imes)-valued orientation.

## 3. Minimal extension lower bound at the first nontrivial level

This gives a genuine lower bound.

Any q-blind carrier (C) satisfying

[
C=C(operatorname{gr}_{!3}G)
]

cannot distinguish (G_3) from (G_infty). Therefore

[
CLongrightarrowchimod9
]

is impossible.

Consequently, any successful carrier must add information not contained in the full mod-3 graded object.

At the first level, the project already has an explicit sufficient extension datum:

[
P_3=X_1^{[3]}
]

coupled to the quadratic relation

[
R_2=[X_1,X_2]+[X_3,X_4].
]

The projective pair

[
[(R_2,P_3)]
]

and, after the observable quotient,

[
[(R_2,p(P_3))]
]

recovers (chimod9).

Thus the first lower/upper bound is now precise:

[
oxed{
	ext{graded object alone}
;<;
	ext{graded object + first filtered extension}
;Longrightarrow;
chimod9.
}
]

This is not yet an absolute information-theoretic minimality theorem, because “extension datum” has not been given a category-independent definition. But it is a genuine structural lower bound: some non-graded lift information is mandatory.

## 4. Full (3)-adic level: exact scalar compression remains possible in principle

A crucial subtlety survives.

It would be incorrect to claim that the infinitely many (3)-adic digits require infinitely many independent extension classes.

For the frozen (q=3) presentation the exact Fox equation

[
1+2B=0
]

compresses all higher digits into one exact (mathbf Z_3)-coefficient equation. Hence an exact carrier may contain infinitely many digits without containing infinitely many independent pieces of extension data.

Therefore the correct lower bound is not:

[
	ext{“one new extension class per }3	ext{-adic digit.”}
]

The defensible statement is:

[
oxed{
	ext{full }chi
	ext{ requires either exact characteristic-zero extension data
or an unbounded compatible system of finite extensions.}
}
]

A finite mod-(3) graded object cannot suffice.

## 5. Hard attack on the tempting shortcut

Could the exact scalar already be extracted canonically from the mod-3 graded object by a hidden normalization?

No.

The failed plain (mathbf Z_3)-augmentation jet shows that there is no automatic integral lift of the characteristic-3 restricted-Lie jet:

[
r-1=3X_1+[X_1,X_2]+[X_3,X_4]+O(I^3),
]

so (r-1
otin I^2).

The failed fixed-coordinate degree-3 Fox truncation further shows that a bounded local polynomial expression is not automatically presentation-independent.

Hence the missing characteristic-zero extension datum cannot simply be declared to be “the same (P_3) over (mathbf Z_3).”

## 6. What is now proved and what remains

### PASS / CLOSED

1. Full mod-3 associated graded Demuškin data is insufficient for (q), hence for (chi).
2. The first nontrivial mod-9 recovery necessarily uses information beyond that graded object.
3. The projective degree-((2,3)) extension (P_3), coupled with (R_2), is sufficient for (chimod9).
4. Full compatible filtered extension data can recover the completed relation and hence the exact Fox obstruction.

### OPEN

A genuinely intrinsic exact intermediate carrier

[
J^{mathrm{mid}}
]

strictly smaller than the completed universal Fox obstruction scheme but stronger than the mod-3 graded object.

## 7. Next attack

The next attack should therefore not search blindly for another formula.

It should test the only remaining plausible loophole:

> Can the universal Fox obstruction scheme itself be quotiented by a canonical kernel, defined before choosing (chi), so that the quotient still determines the orientation but is strictly smaller?

The required test is:

1. define a candidate kernel intrinsically;
2. prove it is invariant under relator gauge and Nielsen change;
3. prove the quotient still separates all admissible orientation points;
4. prove it is strictly smaller than the full Fox scheme;
5. if impossible, exhibit the precise reason that every such kernel would identify two orientation-distinct points.

This is the sharpest remaining carrier attack.

## Decision

[
oxed{	ext{FULL ASSOCIATED-GRADED NO-GO: PASS / CLOSED}}
]

[
oxed{	ext{MINIMAL EXTENSION LOWER BOUND: PASS / LOCAL}}
]

[
oxed{	ext{INTRINSIC EXACT INTERMEDIATE CARRIER: OPEN}}
]

The first two statements are now substantially stronger than the previous finite-window formulation.
