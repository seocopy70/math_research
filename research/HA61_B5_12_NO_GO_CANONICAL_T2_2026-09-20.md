# HA61-B5-12 — NO-GO FOR A CANONICAL VECTOR t2 — 2026-09-20

## Verdict

**FAIL / CLOSED for the proposed single presentation-independent vector (t_2) realization of the secondary obstruction.**

This is a structural counterattack, not a numerical failure.

## 1. Input already established

At the secondary stage, the exact intrinsic object is the connecting-obstruction family
[
ho_3longmapstodelta_{3,ho_3}.
]
Pure relator conjugation preserves this family exactly.

In a chosen relation-jet coordinate, the degree-three residual transforms under
[
rmapsto v r v^{-1}
]
through the degree-three bracket change
[
Pmapsto P+[v,R].
]

The audited crossed-word calculation gives for the isolated residual
[
T([v,R])=lambda(v)f(p)
]
on the primary-zero locus.

## 2. The decisive contradiction

For the frozen q=3 case,
[
lambda=e_2^*,qquad p=e_1
eq0.
]

Choose (v) with (lambda(v)=1). Then the coordinate residual changes by
[
t_2mapsto t_2+p.
]

Choose instead (v) with (lambda(v)=0). The residual is unchanged.

These two relator presentations define the same abstract group and have the same intrinsic:
- primary coefficient character (ho_2);
- primary class (f);
- relation pairing (R) up to the common projective normalization;
- coefficient lift (ho_3);
- connecting-obstruction family (delta_3).

Therefore the raw vector (t_2) cannot be a presentation-independent natural transformation of the intrinsic filtered input when (p
eq0).

This is stronger than saying “we have not found a definition”: the already verified conjugation law supplies an explicit same-object / different-coordinate witness.

## 3. Why quotienting (t_2) by (langle pangle) does not repair the secondary formula

One might replace (t_2) by
[
[t_2]in V^{(2)}/langle pangle.
]

This quotient is indeed invariant under the displayed shift. But the secondary obstruction contains evaluation by arbitrary (f):
[
f(t_2),
]
and (f(p)) is not zero in general. The primary-zero condition is
[
f(p)+(lambdawedge f)(R)=0,
]
not (f(p)=0).

Hence (f(t_2)) does not descend to (V^{(2)}/langle pangle) by itself. The missing compensating term belongs to the full prefix/suffix / lift-gauge ledger. Consequently the quotient ([t_2]) is insufficient to produce the claimed scalar obstruction formula.

## 4. What this kills

The following stronger statement is now closed:

> There is a canonical presentation-independent vector (t_2in V^{(2)}) whose evaluation, together with the fixed ((muwedge f)(R)) term, gives the full secondary connecting obstruction for all admissible presentations.

**FAIL / CLOSED.**

This also kills the immediate plan “define (t_2) from the (P_3/P_4) residual and then open HA61-C.”

## 5. What survives

This is not a failure of the secondary cohomology itself.

The intrinsic family
[
{delta_{3,ho_3}}_{ho_3	ext{ lifting }ho_2}
]
remains **PASS / CLOSED**.

The finite source audit also remains valid:
- (F^9) is the genuinely new power source;
- (gamma_2^3) is the old (lambdawedge f) sector;
- (gamma_3^3,gamma_4) do not survive the /9 mod-3 normalization.

Thus the failure is precisely at the attempted compression
[
	ext{intrinsic }delta_3
;
otRightarrow;
	ext{single vector }t_2.
]

## 6. Logical boundary

The affine quotient
[
(t_2,mu)/langle(p,lambda)angle
]
was already rejected because it identifies distinct coefficient actions.

The new (t_2/langle pangle) repair is also insufficient because evaluation (f(t_2)) does not descend.

Therefore the two obvious finite-dimensional repairs are both closed.

The remaining intrinsic object is necessarily richer: an affine/torsor-valued secondary obstruction or the full function-valued connecting family. Any further compression must preserve its dependence on the coefficient-lift parameter and the primary-zero condition simultaneously.

## 7. Classification

- finite-depth source exhaustion: **PASS / LOCAL**;
- intrinsic (delta_3) family: **PASS / CLOSED**;
- raw (t_2) intrinsicity: **FAIL / CLOSED**;
- (t_2/langle pangle) as a scalar obstruction carrier: **FAIL / CLOSED**;
- diagonal ((t_2,mu)) quotient: **FAIL / CLOSED**;
- single-vector P_4 realization: **FAIL / CLOSED**;
- HA61-B as the (t_2)-compression route: **FAIL / CLOSED**;
- alternative intrinsic secondary carrier: **OPEN / DECISIVE**;
- HA61-C via the single-vector (t_2) route: **NOT OPENED**.

## Immediate consequence

The B door did not remain half-open.

It is now **structurally broken in the proposed (t_2) form**: the obstruction is not lack of computation but a concrete naturality contradiction.

The next permissible step is not to resurrect (t_2). It is to ask whether the surviving intrinsic connecting family itself admits a different compression that preserves the coefficient-lift parameter without identifying distinct (ho_3)'s.

Record: `research/HA61_B5_12_NO_GO_CANONICAL_T2_2026-09-20.md`.
