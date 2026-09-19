# HARD ATTACK 5 — EXACT FOX CARRIER: DEGREE-3 POLYNOMIAL COMPRESSION — 2026-09-19

## New observation

The universal Fox obstruction scheme is intrinsically defined by the full projective Fox row. For the frozen q=3 normal form, however, its defining ideal admits an unexpectedly small exact presentation in the local coordinates
[
A=1+u_1,quad B=1+u_2,quad C=1+u_3,quad D=1+u_4.
]

This is a new fact distinct from the invalid (mathbf Z_3)-restricted-Lie lift.

## 1. Exact projective Fox ideal

From the universal row
[
J_1=1+A+A^2B^{-1},quad
J_2=A^2(A-1)B^{-1},
]
[
J_3=A^3C^{-1}(D^{-1}-1),quad
J_4=A^3D^{-1}(1-C^{-1}),
]
all denominators and the factors (A^2,A^3,C^{-1},D^{-1}) are units on the (1+3mathbf Z_3) neighbourhood.

Therefore the zero locus is equivalently defined by
[
F_1=B(1+A)+A^2,
quad
F_2=A-1,
quad
F_3=D-1,
quad
F_4=C-1.
]

In local variables,
[
F_1=3+3u_1+u_1^2+u_1u_2+2u_2,
]
while
[
F_2=u_1,qquad F_3=u_4,qquad F_4=u_3.
]

Thus the exact q=3 obstruction ideal has a presentation whose non-linear part has degree at most 2.

Even before using (F_2=0), the raw (J_2) numerator is
[
A^2(A-1)=u_1+2u_1^2+u_1^3,
]
so the unreduced universal Fox row has degree at most 3 in the local variables.

## 2. Exact solution

Since (F_2=u_1),
[
F_1equiv 3+2u_2pmod{u_1}.
]
Hence
[
u_1=u_3=u_4=0,qquad 2u_2+3=0,
]
so
[
u_2=-3/2,qquad B=1+u_2=-1/2.
]

This recovers the exact orientation.

## 3. Power-free control

For
[
r_0=[x_1,x_2][x_3,x_4],
]
the universal Fox row is projectively equivalent to
[
(B-1, A-1, D-1, C-1)
]
up to units and signs.

Hence its (1+3mathbf Z_3) zero locus is
[
A=B=C=D=1.
]

The q=3 and power-free cases therefore remain separated by the exact universal Fox scheme, not merely by an external q label.

## 4. What this does and does not prove

It proves a strong new fixed-normal-form statement:

> The intrinsic universal exact Fox obstruction scheme has a finite local polynomial presentation of degree at most 3 for the frozen q=3 Demushkin normal form.

This is stronger than the earlier “fixed relation/evaluation data” statement and is genuinely non-circular at the input-definition level.

But it does **not** yet prove that the truncated degree-(le3) polynomial presentation itself is an intrinsic filtered carrier under arbitrary presentation changes. A nonlinear formal coordinate substitution can raise polynomial degree. The intrinsic object is the full projective Fox scheme; the degree-3 description is currently a normal-form compression of that intrinsic object.

Therefore we must not yet relabel this as an intrinsic degree-(2,3) carrier.

## 5. New sharp boundary

The old question

[
	ext{Does a non-tautological exact finite carrier exist?}
]

is now answered **YES**, in universal Fox-scheme form.

The remaining, more precise question is

[
oxed{
	ext{Does the intrinsic universal Fox scheme admit an
intrinsic filtered degree-3 presentation?}
}
]

This is substantially narrower than the old exact-carrier problem.

## Status

- exact universal Fox scheme: PASS / CLOSED;
- fixed q=3 local polynomial compression degree (le3): PASS / CLOSED;
- q=3 vs power-free separation in this carrier: PASS / CLOSED;
- intrinsicity of the degree-(le3) truncation itself: OPEN;
- two-component ((R,p))-type exact carrier: OPEN;
- bounded finite-information universal carrier: FAIL / CLOSED.
