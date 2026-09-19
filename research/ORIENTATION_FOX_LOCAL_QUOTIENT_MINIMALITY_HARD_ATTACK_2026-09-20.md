# HARD ATTACK 14 — NO NONTRIVIAL LOCAL QUOTIENT OF THE FROZEN EXACT FOX CARRIER — 2026-09-20

## Target

The remaining plausible shortcut was:

> start from the intrinsic universal Fox obstruction scheme and quotient it by a canonical kernel, hoping to obtain a strictly smaller exact carrier that still determines the full (3)-adic orientation.

This can be attacked completely for the frozen rank-four (q=3) model.

## 1. Exact local Fox equations

Write
[
A=1+u_1,quad B=1+u_2,quad C=1+u_3,quad D=1+u_4
]
in the (1+3mathbf Z_3) neighborhood.

The exact fixed-normal-form Fox equations are
[
F_1=B(1+A)+A^2,
qquad
F_2=A-1,
qquad
F_3=D-1,
qquad
F_4=C-1.
]

Therefore
[
F_2=u_1,qquad F_3=u_4,qquad F_4=u_3,
]
and after imposing these three equations,
[
F_1=2u_2+3.
]

Hence the completed local obstruction algebra is
[
mathcal A_{mathrm{Fox}}
=
mathbf Z_3[[u_1,u_2,u_3,u_4]]
/
(u_1,u_3,u_4,2u_2+3).
]

Since (2inmathbf Z_3^	imes),
[
mathcal A_{mathrm{Fox}}congmathbf Z_3.
]

Thus the local Fox obstruction scheme is already the reduced characteristic-zero point
[
u_1=u_3=u_4=0,qquad u_2=-3/2,
]
equivalently
[
(A,B,C,D)=(1,-1/2,1,1).
]

## 2. Consequence for quotient-based compression

Suppose a candidate smaller exact carrier is obtained by a quotient
[
mathcal A_{mathrm{Fox}}	woheadrightarrow Q
]
and is required to retain the full (3)-adic orientation.

Because
[
mathcal A_{mathrm{Fox}}congmathbf Z_3,
]
a unital quotient of this local coefficient algebra is either (mathbf Z_3) itself or a quotient of finite (3)-power characteristic (or the zero ring).

Any finite-characteristic quotient loses higher (3)-adic digits. The zero quotient loses the orientation point entirely.

Therefore, within the natural category of local coefficient-algebra quotients preserving the full (3)-adic point, there is no proper quotient of the frozen exact Fox carrier.

In this precise category:

[
oxed{
	ext{exact local Fox carrier is already minimal under quotients.}
}
]

This is stronger than saying that no smaller formula has been found.

## 3. Why this does not close every possible compression

The result does **not** prove that no different mathematical object can compress the same information.

A non-quotient construction could, in principle, encode the same exact point through a different intrinsic extension invariant. Such an object would have to be defined before applying Fox calculus and would have to prove a natural factorization into the Fox carrier.

Therefore the remaining open problem is now sharply separated:

[
oxed{
	ext{non-quotient intrinsic exact compression}
}
]

rather than

[
	ext{quotient of the Fox scheme}.
]

## 4. Relation to earlier failures

This result also explains why the previous degree-3 truncation attack matters.

The full local Fox equations collapse to a one-dimensional exact characteristic-zero point only *after* the exact coefficient equations are known. The Nielsen attack showed that simply truncating the presentation-dependent Fox row does not produce an intrinsic carrier.

Likewise, the failed (mathbf Z_3)-augmentation jet showed that there is no automatic integral restricted-Lie lift supplying this point.

Thus the obstruction is no longer lack of algebraic compression inside the Fox scheme. The missing object, if it exists, must be an independently defined intrinsic characteristic-zero extension structure.

## Decision

- quotient-of-local-Fox-scheme compression: **FAIL / CLOSED**;
- exact local Fox carrier minimality under full-(3)-adic-preserving quotients: **PASS / CLOSED**;
- independent intrinsic non-quotient exact compression: **OPEN**;
- broad claim that no alternative carrier can ever exist: **not proved**.
