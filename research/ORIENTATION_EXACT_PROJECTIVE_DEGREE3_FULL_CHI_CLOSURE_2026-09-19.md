> **2026-09-19 supersession note.** The mathematical recovery result in this document remains valid: fixed q=3 exact filtered relation/evaluation data determine the full orientation. However, the notation \\(\mathbb J^{ex}_3=\\langle(R_2,P_3)\\rangle^{proj}_{\\mathbf Z_3}\\) should not be read as a literal characteristic-zero restricted-Lie scalar extension of the mod-3 carrier. The subsequent audit \`research/ORIENTATION_EXACT_Z3_CARRIER_BRANCH_ENDPOINT_2026-09-19.md\` establishes the correct boundary: the exact carrier must be understood through the filtered relation/evaluation framework; a concrete non-tautological finite pair analogous to \\(([R],p(P])\\) has not been proved. The PASS for full \\(\\chi\\) is retained; only the overly literal characteristic-zero carrier notation is superseded.\n\n# ORIENTATION — EXACT PROJECTIVE DEGREE-3 CARRIER: CLOSURE AUDIT — 2026-09-19

## Target

Determine whether the fixed q=3 group admits a single bounded-filtration-degree carrier, with exact (mathbf Z_3)-coefficients, that determines the full orientation (chi).

## Result

At the fixed q=3 normal form, **YES at the level of a projective exact degree-(2,3) relation carrier**. The arithmetic reconstruction is finite-degree because the exact q=3 power term occurs in degree 3 and the resulting crossed-derivation equation is an exact (mathbf Z_3)-equation.

This does not contradict the universal finite-information obstruction: the latter varies q=3^s and asks for one fixed degree bound working uniformly in s. For s>1, the q-dependent power term moves to degree 3^s.

## 1. Exact carrier

Use the minimal free pro-3 presentation
[
1	o R	o F	o G_3	o1
]
and the completed group algebra (Lambda=mathbf Z_3[[F]]), with augmentation ideal (I).

Retain the relation line through filtration degree 3:
[
mathbb J^{mathrm{ex}}_3
=
igllangle (R_2,P_3)igrangle_{mathbf Z_3}^{mathrm{proj}},
]
where the degree-2 and degree-3 coefficients are retained over (mathbf Z_3), rather than reduced to (mathbf F_3).

For the frozen normal form,
[
R_2=[X_1,X_2]+[X_3,X_4],
qquad
P_3=X_1^{[3]}.
]

The carrier remembers that the same filtered defining relation has both components. This common-line coupling is essential.

## 2. Exact recovery

The intrinsic crossed-derivation characterization gives, for
[
ho:G_3	omathbf Z_3^	imes,
]
the exact equations
[
ho(x_1)=ho(x_3)=ho(x_4)=1,
qquad
1+2ho(x_2)=0.
]

Because (2inmathbf Z_3^	imes), the solution is unique:
[
ho(x_2)=-rac12=(1-3)^{-1}.
]

Therefore the single exact degree-(2,3) carrier determines the complete inverse-limit value, not merely a finite reduction:
[
chi(x_2)= -rac12
=4pmod9
=13pmod{27}
=40pmod{81}
=121pmod{243}
=cdots.
]

No higher filtration degree is needed for this fixed q=3 normal form once the coefficient ring is exact.

## 3. Why the mod-9 carrier could not make this claim

The earlier
[
J_3subset L_2oplus L_3^{res}
]
was an (mathbf F_3)-level object. It sees only the first nontrivial digit and gives
[
ho(x_2)=4pmod9.
]

The exact carrier changes the coefficient category. It is not a finite-information object in the relevant information-theoretic sense: an exact (mathbf Z_3)-valued equation has access to the whole 3-adic coefficient system.

Thus there is no logical implication
[
J_3(mathbf F_3)Rightarrowchi
]
but there is
[
mathbb J^{ex}_3(mathbf Z_3)Rightarrowchi
]
for the fixed q=3 normal form.

## 4. Presentation-change / gauge check

At degree (le3), a change of minimal free cover inducing the identity on G acts on the relation jet by the same residual form as in the mod-9 audit:
[
(R,P)longmapsto (uR,uP+[v,R]).
]

Over (mathbf Z_3), the argument is identical at the truncated degree level: the IA correction to generators starts in degree 2; applying it to the quadratic relation contributes a degree-3 bracket correction; a change of relation generator contributes a common unit (u).

For any degree-one functional (f),
[
f([v,R])=0.
]
Consequently
[
Theta_{uR,uP+[v,R]}(lambda)
=
u,Theta_{R,P}(lambda),
]
so its zero set is unchanged.

Automorphisms of G act functorially on the same projective carrier and on the crossed-derivation equation. Hence the carrier/recovery construction is natural.

This closes the only additional gauge issue introduced by replacing (mathbf F_3) by exact (mathbf Z_3)-coefficients, subject to the frozen minimal one-relator pro-3 presentation facts already used by the mod-9 E1-E5 closure.

## 5. Precise theorem boundary

The result should be stated as:

> **Exact bounded-degree recovery theorem (fixed q=3).**
> For the standard rank-4 q=3 Demuškin presentation, the projective degree-(2,3) filtered relation jet with exact (mathbf Z_3)-coefficients determines the canonical orientation character uniquely.

This is a theorem about the **exact filtered** carrier, not about the bare associated graded restricted Lie object.

It also does not imply a universal bounded-degree theorem for the family q=3^s.

Indeed, for every fixed d there are s with 3^s>d, and the q-dependent term is then outside degree d.

## 6. Final B verdict

The stronger branch has a split but now complete answer:

1. **Universal finite-information bounded-degree carrier:** FAIL / CLOSED.
2. **Fixed q=3, exact (mathbf Z_3)-coefficient bounded-degree projective relation carrier:** PASS / CLOSED at the stated presentation/gauge level.
3. **Bare (mathbf F_3) associated graded carrier:** FAIL / CLOSED for full (chi).
4. **Full compatible filtered tower:** PASS / CLOSED.
5. **No higher-degree scan is needed.**

The remaining conceptual distinction is only whether one wants to call the exact (mathbf Z_3)-coefficient carrier “finite information.” It should not be: one exact p-adic coefficient represents infinitely many finite digits.

No computational scan is warranted.
