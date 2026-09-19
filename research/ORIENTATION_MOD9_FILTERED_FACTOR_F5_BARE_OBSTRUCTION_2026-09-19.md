# ORIENTATION MOD-9 FILTERED FACTOR — F5-BARE STRUCTURAL OBSTRUCTION — 2026-09-19

## Scope

This audit addresses the remaining exact question after the critical narrowing of F5:

> Does the **bare associated graded restricted Lie object** canonically determine the degree-3 relation jet needed for the twisted mod-9 orientation obstruction?

No finite scan is used.

The conclusion is negative for the bare Zassenhaus graded object in the present q=3 versus q=infinity comparison. The earlier F5-A result that the class X_1^{[3]} exists in degree 3 is retained, but that class is not a distinguished component of the graded relation data.

## 1. Two groups with the same quadratic initial relation

Consider the two standard rank-4 Demushkin presentations

G_3 = <x_1,x_2,x_3,x_4 | x_1^3 [x_1,x_2][x_3,x_4] = 1>

and

G_infty = <x_1,x_2,x_3,x_4 | [x_1,x_2][x_3,x_4] = 1>.

For the p-Zassenhaus filtration at p=3,

- x_1^3 has degree 3;
- each commutator [x_i,x_j] has degree 2.

Hence the initial form of the defining relator in both groups is the same quadratic element

R_2 = [X_1,X_2] + [X_3,X_4].

For Demushkin groups with q != 2, standard graded-presentation results identify the associated graded group-algebra/restricted-Lie object from the initial form of the relator. In particular, the q=3 and q=infinity cases have the same graded defining relation R_2.

This agrees with the repository's frozen quadratic relation and with the standard Demushkin graded presentation theorem.

## 2. The crucial distinction: P_3 exists, but is not marked by gr(G)

The q=3 relator contains the degree-3 term

P_3 = X_1^{[3]}

in addition to R_2.

However, passing to the associated graded object records the initial homogeneous relation R_2. The degree-3 term of the original filtered relator is a higher component of the filtered defining relation; it is not, by itself, a distinguished element of the bare graded quotient.

In particular, the bare graded restricted Lie algebra contains many degree-3 restricted-power classes, including X_1^{[3]}. What is missing is the **coupling datum** saying that this particular P_3 is the degree-3 component of the same filtered relation whose degree-2 component is R_2.

This is exactly the common-scaling coupling that the marked relation jet

J_3 = <(R_2,P_3)> subset L_2 direct-sum L_3^res

retains.

Thus F5-A must be interpreted narrowly:

- PASS: a q-sensitive degree-3 class exists in a common ambient restricted model;
- FAIL as an intrinsic bare-carrier claim: the bare associated graded object does not canonically mark that class as the higher component of R_2.

## 3. Same bare graded datum, different mod-9 orientation

The two groups have different canonical orientations.

For G_3,

chi_3(x_2) = (1-3)^(-1) = 4 mod 9.

For G_infinity (q=infinity),

chi_infinity is trivial on the x_2 direction, hence

chi_infinity(x_2) = 1 mod 9.

Therefore

chi_3 mod 9 != chi_infinity mod 9,

while the bare p-Zassenhaus associated graded restricted Lie objects are the same graded object determined by R_2.

Consequently no invariant depending only on the isomorphism class of the bare associated graded restricted Lie object can recover chi mod 9 in this class.

This is an information-theoretic obstruction, not a failure of a particular formula.

## 4. Consequence for the relation-jet construction

The marked construction remains mathematically valid:

Theta_{R,P}(lambda)(f) = f(P) + (lambda wedge f)(R).

For the marked jet J_3 it has the unique zero lambda_chi and therefore recovers chi mod 9.

But the preceding comparison proves that J_3 is strictly additional structure relative to the bare associated graded object. The bare object cannot reconstruct the needed coupling, because it is identical for the q=3 and q=infinity examples while the target orientation digit differs.

Thus the implication

bare gr(G) -> J_3

is false in the present category.

## 5. Exact gate decision

The defensible gate status is now:

- F1-F4: PASS at the canonical finite-filtered-quotient level.
- F5-A: PASS only for existence of a q-sensitive ambient degree-3 carrier.
- F5-marked: PASS, conditional on the marked relation jet J_3 being supplied.
- **F5-bare: FAIL / CLOSED** for recovery from the bare p-Zassenhaus associated graded restricted Lie object.

This does not rule out recovery from a richer filtered/graded datum that explicitly retains the filtered relation jet, extension class, or an equivalent coupling invariant.

It does rule out the stronger claim that the bare associated graded restricted Lie object alone determines chi mod 9.

## 6. Research consequence

The project should no longer spend computation on trying to reconstruct J_3 from the bare graded object: the q=3 versus q=infinity comparison gives a structural obstruction.

The viable statement is now conditional:

    enriched filtered/graded datum carrying J_3
        -> Theta
        -> unique lambda_chi
        -> chi mod 9.

The bare associated graded route is closed.

No finite scan is authorized or needed.

## External mathematical support

Standard Demushkin classification gives, for q != 2, a relator of the form

x_1^q [x_1,x_2][x_3,x_4]...

and the associated graded presentation is determined by the initial form of the relator. Since the q-power term has Zassenhaus degree 3 at p=3 while the commutator part has degree 2, the initial form is R_2 in both q=3 and q=infinity cases.

References consulted for this audit:
- Mináč–Pasini–Quadrelli–Tân, *Koszul algebras and quadratic duals in Galois cohomology* (Theorem 4.5 and the Demushkin graded presentation discussion).
- Standard Demushkin orientation/duality characterization as recorded in the project’s mod-9 twisted-surjectivity gate.

## Final decision

\[
\boxed{
F5\text{-bare}=\mathrm{FAIL/CLOSED},
\qquad
F5\text{-marked}=\mathrm{PASS}.
}
\]

The original recovery theorem is therefore **not true for the bare associated graded restricted Lie object**, but remains valid at the enriched relation-jet level.
