# HA61-B5-13 — INTRINSIC ZERO-SELECTOR ATTACK ON THE SURVIVING DELTA3 FAMILY — 2026-09-20

## Verdict

**OPEN / DECISIVE.**

The single-vector (t_2) route is closed. The surviving object
[
ho_3longmapsto delta_{3,ho_3}
]
should now be attacked directly as an intrinsic **zero-selector on the coefficient-lift torsor**, rather than compressed to a presentation-independent vector.

This is a new target, not a resurrection of (t_2).

## 1. Exact surviving object

For fixed intrinsic (ho_2:G	o(mathbf Z/9)^	imes), let
[
L(ho_2)={ho_3:G	o(mathbf Z/27)^	imes:ho_3mod9=ho_2}.
]
Each (ho_3in L(ho_2)) gives
[
0	omathbf F_3	o mathbf Z/27(ho_3)	omathbf Z/9(ho_2)	o0
]
and hence
[
delta_{3,ho_3}:H^1(G,mathbf Z/9(ho_2))	o H^2(G,mathbf F_3).
]

The whole family is already **PASS / CLOSED** as an intrinsic cohomological object.

## 2. New compression target: zero-selector, not vector

For a primary-zero class (f) admitting an (A_2)-lift, define formally
[
Z_3(f)={ho_3in L(ho_2):delta_{3,ho_3}(f)=0}.
]

The decisive question is:

> Can (Z_3(f)) be proved to be a singleton intrinsically, with no presentation, (q), (chi), (t_2), or chosen (H^2)-generator?

If yes, the next digit is recovered directly from the surviving obstruction family and no (t_2) is needed.

If no, the failure itself gives the next logical boundary.

## 3. Torsor structure

Any two lifts differ by a mod-3 character:
[
ho_3'=ho_3(1+9
u),qquad

uin H^1(G,mathbf F_3).
]

Thus (L(ho_2)) is an affine (H^1(G,mathbf F_3))-torsor.

The coordinate computations already give the expected first-order variation:
[
delta_{3,ho_3'}(f)-delta_{3,ho_3}(f)
quad	ext{is represented by}quad
(
usmile f)in H^2(G,mathbf F_3),
]
up to the single global sign convention already synchronized at the mod-9 stage.

This identity is **not yet promoted to PASS**. It is the next theorem to prove intrinsically, preferably by comparing the two coefficient extensions/Yoneda extension classes rather than by returning to a relator normal form.

## 4. Why uniqueness could be forced

For a Demuškin group the mod-3 cup pairing
[
H^1(G,mathbf F_3)	imes H^1(G,mathbf F_3)
	o H^2(G,mathbf F_3)
]
is nondegenerate.

Therefore, for (f
e0),
[

ulongmapsto 
usmile f
]
is a nonzero linear functional.

If the variation identity in §3 is proved intrinsically, then the secondary obstruction varies nontrivially along every nonzero torsor direction. Consequently (Z_3(f)) contains **at most one** point.

Existence remains a separate theorem: one must show that the obstruction-free lift exists for the relevant primary-zero datum.

This splits the old problem cleanly into:

[
oxed{	ext{uniqueness = cup-pairing nondegeneracy}}
]
and
[
oxed{	ext{existence = filtered/coefficient lifting}}
]

rather than trying to encode both inside (t_2).

## 5. Frozen-family sanity checks

The already audited exact branches give:

- (q=3): (ho_3(x_2)=13+9a), and
  [
  delta_3(f)=-a f_1,
  ]
  so the unique zero is (a=0), i.e. (13pmod{27}).

- (q=9): (ho_3(x_2)=1+9a), and
  [
  delta_3(f)=(1-a)f_1,
  ]
  so the unique zero is (a=1), i.e. (10pmod{27}).

- (27mid q): the same standard relation calculation predicts the zero at (a=0), i.e. the control value (1pmod{27}).

These are **PASS / LOCAL sanity checks only**. They do not prove presentation-independence.

## 6. Crucial novelty/q-blindness warning

There is a serious conceptual boundary.

The classical characterization of the Demuškin orientation is itself by successive surjectivity of
[
H^1(G,I/p^{j+1}I)	o H^1(G,I/p^jI).
]
Thus “the unique coefficient lift for which the connecting obstruction vanishes” is closely related to the defining Serre lifting characterization of the canonical orientation.

Therefore the zero-selector is **not automatically a new theorem**.

The project must prove a stronger statement:

[
	ext{declared intrinsic filtered/relation input}
longrightarrow
{delta_{3,ho_3}}_{ho_3}
longrightarrow
	ext{unique zero}
]

without first importing the dualizing module/orientation itself.

Only that factorization would make the surviving family a genuine filtered carrier rather than a restatement of the known orientation definition.

## 7. Pre-check status

- **Object:** function-valued secondary connecting family — PASS / CLOSED.
- **Input:** candidate coefficient lifts plus declared filtered data — admissible, but factorization from finite filtered data remains OPEN.
- **Functoriality:** connecting-family naturality — PASS / CLOSED.
- **Gauge:** representative gauge removed; coefficient-lift points are NOT quotiented — PASS / CLOSED.
- **Orientation bridge:** zero-selector — OPEN / DECISIVE.
- **q-blindness:** definition contains no (q) or (chi) — PASS / LOCAL; novelty still unresolved.
- **Separation:** q=3, q=9, and (27mid q) separate locally — PASS / LOCAL.
- **Novelty:** not established; must beat the classical Serre characterization.
- **Stop:** no all-(n) induction and no (t_2) resurrection.

## 8. Immediate next attack

Prove, intrinsically and without a presentation:

[
oxed{
delta_{3,ho_3(1+9
u)}(f)
-
delta_{3,ho_3}(f)
=

usmile f
}
]

with the common (H^2)-normalization handled only up to the already-fixed mod-9 convention.

Then test:

1. nonzero (f) (Rightarrow) injectivity of the lift-to-obstruction map;
2. existence of a zero from the finite filtered/relation input;
3. whether that existence proof uses anything equivalent to the canonical orientation;
4. whether the construction factors through (G/P_4) or the equivalent (D_{10}) finite information window.

A proof of (1)+(2)+(3-free filtered factorization) would replace the dead (t_2) door with a genuinely intrinsic secondary selector. Failure at any point is itself a sharp boundary.

## Classification

- single-vector (t_2): **FAIL / CLOSED**.
- (t_2/langle pangle): **FAIL / CLOSED**.
- diagonal ((t_2,mu))-quotient: **FAIL / CLOSED**.
- intrinsic (delta_3)-family: **PASS / CLOSED**.
- intrinsic torsor zero-selector: **OPEN / DECISIVE**.
- all-digit tower: **OPEN / DECISIVE** but not yet authorized.
