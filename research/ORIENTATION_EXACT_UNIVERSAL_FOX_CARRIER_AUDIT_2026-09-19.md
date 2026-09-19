# HARD ATTACK 3 — UNIVERSAL EXACT FOX OBSTRUCTION CARRIER — 2026-09-19

## Executive finding

The previous exact-carrier branch was stopped because a finite augmentation truncation had not been shown to factor the exact crossed-derivation law, while the naive \\mathbf Z_3-restricted-Lie lift was invalid.

A genuinely different characteristic-zero object survives that attack:

\\[
\\boxed{
\\mathfrak F_r :=
\\bigl(\\mathcal A^{d},\\,J_r\\bigr),
\\qquad
\\mathcal A=\\mathbf Z_3[T_1^{\\pm1},\\dots,T_d^{\\pm1}],
}
\\]

where (J_r) is the universal twisted Fox-Jacobian row of the defining relator (r), obtained by applying the universal character
(x_i\\mapsto T_i) to the ordinary Fox derivatives
((\\partial r/\\partial x_i)).

This is **not** obtained by inserting the desired orientation into the input. The variables (T_i) are formal coefficient variables, and the row is computed directly from the defining relation.

The carrier is therefore a finite exact characteristic-zero algebraic object, but it is not a two-component linear jet. Its natural output is a Laurent-polynomial obstruction scheme.

## 1. Universal construction

For a minimal one-relator presentation
[
1\\to N\\to F=F(x_1,\\ldots,x_d)\\to G\\to1,
]
let
[
A=\\mathbf Z_3[T_1^{\\pm1},\\ldots,T_d^{\\pm1}]
]
and let
[
\\tau:F\\to A^\\times,qquad \\tau(x_i)=T_i.
]

For each generator define the universal twisted Fox coefficient
[
J_i(r):=\\tau\\left(\\frac{\\partial r}{\\partial x_i}\\right)\\in A.
]

Collect them as
[
J_r=(J_1(r),\\ldots,J_d(r)).
]

For a candidate character (ho:F	o\\mathbf Z_3^\\times), evaluation (T_i\\mapstoho(x_i)) gives the coefficient row of the (ho)-crossed derivation obstruction. Thus the exact descent condition is
[
J_r(ho)=0.
]

The crucial logical point is that (J_r) is defined **before** choosing (ho). The orientation is recovered as a solution of the universal obstruction equations, rather than being placed inside the carrier definition.

## 2. Frozen rank-4 q=3 computation

For
[
r=x_1^3[x_1,x_2][x_3,x_4],
qquad [a,b]=a^{-1}b^{-1}ab,
]
write
[
A=T_1, B=T_2, C=T_3, D=T_4.
]

The crossed-derivation coefficient calculation gives the universal row
[
egin{aligned}
J_1&=1+A+A^2+A^2(B^{-1}-1)
      =1+A+A^2B^{-1},\\
J_2&=A^2(A-1)B^{-1},\\
J_3&=A^3C^{-1}(D^{-1}-1),\\
J_4&=A^3D^{-1}(1-C^{-1}).
end{aligned}
]

Multiplying by the harmless units (B,C,D) where convenient gives polynomial equations equivalent on the torus:
[
egin{aligned}
B J_1&=B(1+A)+A^2,\\
B J_2&=A^2(A-1),\\
CD J_3&=A^3(1-D),\\
CD J_4&=A^3(C-1).
end{aligned}
]

Hence the universal obstruction ideal is
[
I_r=(B(1+A+A^2), A^2(A-1), A^3(1-D), A^3(C-1)).
]

On the (3)-adic neighbourhood (A,B,C,D\\in1+3\\mathbf Z_3), the equations force
[
A=C=D=1,qquad 2+B^{-1}=0,
]
so
[
B=-\\frac12=(1-3)^{-1}.
]

Thus the exact full orientation is recovered from a finite Laurent-polynomial carrier.

## 3. Why this is not the old tautological tower

The old tower defined (J_n) as “whatever filtered relation data is required for the crossed-derivation evaluation” and then extracted the same evaluation.

Here the order is reversed:

1. choose the universal coefficient ring (A);
2. compute the ordinary Fox Jacobian of the relator;
3. universally abelianize the coefficient action (x_i\\mapsto T_i);
4. only afterwards evaluate (T_i) at candidate (3)-adic units.

No (chi), no (chi_n), and no phrase such as “the data needed to recover (chi)” occurs in the definition.

The carrier is finite for a fixed finite relator, although its coefficient ring is infinite as a set and it carries arbitrarily many (3)-adic digits. Therefore it does **not** contradict the previously proved bounded-degree + bounded-precision no-go theorem.

## 4. Relation to standard Fox calculus

The construction is classical in spirit: Fox derivatives form the Jacobian of a presentation, and after evaluation through a character they give the linear coefficient row governing crossed derivations. This exact evaluation mechanism is standard; the present research contribution, if any, is the proposed use of the **universal unevaluated Fox row as the characteristic-zero carrier** for orientation reconstruction.

This distinction must be preserved in the manuscript: the Fox-calculus identity is not claimed as new mathematics.

## 5. The hard remaining gate: intrinsicity

The construction is unquestionably intrinsic to a **chosen presentation**, but the research question asks for an intrinsic filtered object.

The next proof obligation is therefore:

[
oxed{
	ext{presentation change}
Longrightarrow
	ext{natural equivalence of universal Fox obstruction schemes}.
}
]

For relator multiplication by a unit and relator conjugation, this should follow from standard Fox identities and produces the same zero set. For a change of minimal free basis, the universal character torus changes by the induced Laurent monomial substitution, and the Fox chain rule should transform the obstruction ideal covariantly.

This must be proved, not assumed.

Accordingly this audit does **not** yet declare full intrinsicity CLOSED.

## 6. New status

- Universal exact Fox obstruction carrier exists for a fixed finite presentation: **PASS / CLOSED**.
- It is independently defined and non-circular at the input-definition level: **PASS / CLOSED**.
- It recovers the frozen q=3 full orientation: **PASS / CLOSED**.
- It is a finite exact characteristic-zero carrier: **PASS / CLOSED**, with the explicit caveat that “finite” means finitely generated algebraic data, not finite information.
- Naive restricted-Lie scalar extension: **FAIL / CLOSED**.
- Intrinsicity under arbitrary minimal presentation change: **OPEN**.
- Reduction to a two-component degree-(2,3) object: **OPEN / NOT SHOWN**.

## 7. Next authorized attack

Do not scan representations.

Prove the presentation-change covariance of the universal Fox obstruction ideal using:

1. relator conjugation;
2. relator multiplication by a unit in the pro-3 relation module;
3. Nielsen/free-basis changes via the Fox chain rule;
4. induced Laurent-torus coordinate change;
5. invariance of the (1+3\\mathbf Z_3) solution locus.

Only after this gate should the object be promoted from “fixed-presentation exact carrier” to “intrinsic exact carrier candidate”.

This is the first genuinely new characteristic-zero carrier since the exact-Z_3 branch was closed, because it changes the object type rather than attempting to scalar-extend the characteristic-3 restricted Lie structure.
