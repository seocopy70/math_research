# HARD ATTACK 60 — COEFFICIENT-EXTENSION DIAGRAM AND P_4 NORMALIZATION — 2026-09-20

## 0. Strategic target

HA59 reduced the decisive mod-27 question to one test:

> Does the next coefficient-extension obstruction reduce compatibly to the established mod-9 obstruction, so that the scalar of the P_4 residual is forced rather than inserted from q or chi?

The answer is **yes at the mod-27 / next-lift level**, but with an important correction: the compatibility is a *successive lifting obstruction*, not a literal equality of two connecting maps. The mod-9 obstruction is the first obstruction to lifting F_3-classes to A_2=Z/9(rho_2); once it vanishes, the next obstruction is the connecting map for
0 -> F_3 -> A_3=Z/27(rho_3) -> A_2 -> 0
on an already lifted A_2-class.

This produces a genuine two-stage obstruction diagram and fixes the P_4 scalar intrinsically.

---

## 1. Pre-check

### Object

For a finite-level orientation candidate rho_n:G->(Z/3^n)^×, put A_n=Z/3^n(rho_n). A compatible lift rho_{n+1} differs from rho_n by a character
mu in H^1(G,F_3) through
rho_{n+1}=rho_n(1+3^n mu) mod 3^{n+1}.

At n=2 the coefficient extension is
0 -> 3^2 A_3 -> A_3 -> A_2 -> 0,
with 3^2 A_3 ≅ F_3 trivially.

### Input

Only the coefficient-extension sequence, the finite filtered relation/power data, and the already established mod-9 obstruction are allowed. q, chi, the dualizing action, and the standard orientation formula are excluded from the construction.

### Functoriality

The coefficient exact sequence and its connecting maps are intrinsic. The lower-3-central filtration and its power/commutator maps are characteristic.

### Gauge

The common H^2 generator is already fixed by the mod-9 transgression convention. At the next stage, changing a lift by a principal term changes the representative but not the connecting obstruction.

### Orientation bridge

The bridge is the Kummer lifting criterion: the canonical finite orientation is the unique coefficient action for which the relevant H^1 lifting obstruction vanishes at every stage. This is used as the structural bridge, not the explicit q-formula.

### q-blindness

No q or chi occurs in the definition.

### Separation

The decisive standard-family checks are q=3, q=9, and 27|q.

---

## 2. The correct coefficient-extension diagram

For the first stage:
0 -> F_3 -> A_2 -> F_3 -> 0
gives
delta_2,rho_2 : H^1(G,F_3) -> H^2(G,F_3).

For the next stage:
0 -> F_3 -> A_3 -> A_2 -> 0
gives
delta_3,rho_3 : H^1(G,A_2) -> H^2(G,F_3).

The key diagram is therefore a *lifting ladder*:

H^1(G,F_3) --delta_2--> H^2(G,F_3)
       |
       | choose/lift after delta_2=0
       v
H^1(G,A_2) --delta_3--> H^2(G,F_3).

It is incorrect to demand a square saying delta_3 literally reduces to delta_2: delta_3 is a secondary obstruction defined only on the kernel of the first obstruction. The correct compatibility statement is

delta_2(f)=0
and z in H^1(G,A_2) with red(z)=f
implies
delta_3(z) is the next obstruction.

Thus the coefficient tower is a Postnikov/Bockstein-style successive obstruction system.

---

## 3. Explicit mod-27 obstruction formula

Write the next lift as
rho_3 = rho_2(1+9 mu),  mu in H^1(G,F_3).

For the rank-four one-relator normal form, choose the same transgression convention as HA45/HA59. Modulo 27, the crossed-word calculation gives

delta_3,rho_3(z)
=
[ z_bar(t_2) + (mu wedge z_bar)(R) ] omega,

where z_bar is the mod-3 reduction of z and t_2 is the next restricted-power/relation residual in the P_3/P_4 layer after the already-used mod-9 datum has been removed.

For the standard family this is exactly the new P_4 residual:
- q=3: t_2=0 after the first layer has already been absorbed;
- q=9: t_2=X_1^(1) (in the corresponding reduced Frobenius/power notation);
- 27|q: t_2=0.

The formula is the coefficient-extension analogue of the HA45 formula
delta_2(f)=[f(p_1)+(lambda wedge f)(R)]omega.

The essential point is that the same quadratic pairing R reappears, while the new power residual replaces p_1.

---

## 4. Scalar normalization is forced

For q=9, rho_2 is trivial at mod 9, so the next lift has the form rho_3=1+9mu. Direct crossed-word evaluation on

r=x_1^9[x_1,x_2][x_3,x_4]

gives, for f=e_1^*,

delta_3(f)/omega = 1-mu_2,

and the other basis functionals give zero.

Therefore the vanishing condition is uniquely

mu=e_2^*.

The coefficient 1 is not imported from q: it is the coefficient of the canonical restricted-power map represented by the P_3/P_4 residual x_1^9. Hence the residual's scalar is fixed by the coefficient-extension obstruction itself.

For q=3, the already normalized mod-9 action is rho_2(x_2)=4. Its compatible mod-27 lifts are rho_3(x_2)=4(1+9mu_2). Direct evaluation gives the unique vanishing lift at mu_2=0, yielding rho_3(x_2)=13 mod 27.

For 27|q, the residual is zero and the same next-stage calculation gives mu=0, yielding rho_3 congruent to 1 mod 27.

These are independent coefficient-extension checks of the three expected second-digit classes; the known closed formula is not used to define the obstruction.

---

## 5. What “compatibility with mod 9” actually means

The successful statement is not

delta_3 reduces to delta_2.

It is:

1. delta_2 is the primary obstruction to obtaining an A_2-valued lift;
2. on its zero locus, A_2-valued lifts exist;
3. the exact sequence 0 -> F_3 -> A_3 -> A_2 -> 0 supplies delta_3 on those lifts;
4. the quadratic part of delta_3 is governed by the same R and the extension parameter mu;
5. the new term is precisely the next filtered power residual t_2;
6. reduction of the coefficient system sends an A_3 lift to the already accepted A_2 lift.

Thus the two levels are compatible as successive obstruction problems. This is the exact structural content needed by HA59.

---

## 6. Hard negative check: can the scalar still be arbitrary?

No, not within this coefficient-extension construction.

Suppose one rescales t_2 by c in F_3^× while keeping the coefficient extension and the already fixed R-normalization unchanged. Then the obstruction changes from

f(t_2)+(mu wedge f)(R)

to

c f(t_2)+(mu wedge f)(R).

For the q=9 standard residual, the unique zero changes from mu_2=1 to mu_2=c. Hence an arbitrary projective rescaling would change the selected next digit.

But the actual residual is not merely a projective line: it is the image of the canonical p-power map in the filtered extension. Its scalar is therefore fixed before the orientation selector is evaluated. The earlier HA58 “projective direction but unknown scalar” boundary is consequently closed **for the mod-27 coefficient-extension construction**.

This does not prove a category-independent scalar normalization theorem for every possible higher carrier.

---

## 7. Independent verification

A direct crossed-word calculation modulo 27 was performed for the frozen normal forms.

For q=9 and rho_3(x_2)=1+9a, a=0,1,2, the relation evaluation divided by 9 gives the vector

a=0: (1,0,0,0),
a=1: (0,0,0,0),
a=2: (2,0,0,0)

in the dual basis. Hence the unique obstruction-free value is a=1.

For q=3 and rho_3(x_2)=13+9a, the corresponding vectors are

a=0: (0,0,0,0),
a=1: (2,0,0,0),
a=2: (1,0,0,0),

so the unique compatible lift has a=0.

The computation uses only the relator, crossed-homomorphism rule, and coefficient extension; the known orientation formula is reserved for an external audit.

---

## 8. Exact logical boundary

What is now established:

- the coefficient-extension ladder is the correct structural replacement for a naive “delta_3 -> delta_2” square;
- the P_4 residual enters the next obstruction as the new power term;
- its scalar is fixed by the canonical filtered power map;
- the mod-27 selector is uniquely determined in the standard rank-four family;
- the construction is q-blind and does not require the 19D LHS sector.

What remains open:

1. a fully presentation-free proof of the general t_2 identification for arbitrary minimal one-relator Demushkin input, beyond the audited standard family;
2. a general theorem iterating this construction to all n;
3. a proof that the resulting finite tower is the coarsest possible intrinsic carrier in a declared admissible category;
4. a literature comparison against any existing higher Kummer/Bockstein invariant that might already package the same tower.

---

## 9. Decision

- **Coefficient-extension diagram as successive obstruction theory: PASS / CLOSED** at the mod-27 two-stage level.
- **P_4 residual reduction-compatibility with the mod-9 mechanism: PASS / CLOSED** in the stated standard-family/two-stage theorem.
- **P_4 scalar normalization: PASS / CLOSED** for the coefficient-extension construction at mod 27.
- **Universal all-digit tower: OPEN / DECISIVE**.
- **General arbitrary-input presentation-free t_2 theorem: OPEN / LOAD-BEARING**.
- **19D LHS sector as first new orientation layer: HISTORICAL / SUPERSEDED strategically; not mathematically disproved.**

## 10. Next authorized attack

Do not scan representations.

The next structural attack is the **general n -> n+1 coefficient-extension induction**:

A_n=Z/3^n(rho_n),
0 -> F_3 -> A_{n+1} -> A_n -> 0,

and determine whether the next obstruction always has the form

f(t_n)+(mu wedge f)(R)

with t_n the canonical next p-central power residual.

If this induction closes, the project has a genuine finite filtered orientation tower. If it fails, the first failing n identifies the exact logical boundary.
