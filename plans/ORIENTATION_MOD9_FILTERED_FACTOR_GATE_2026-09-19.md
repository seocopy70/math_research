# ORIENTATION MOD-9 FILTERED FACTOR GATE — 2026-09-19

## Objective

The twisted-coefficient calculation has recovered
\[
\chi\bmod9
\]
intrinsically from the group. The remaining question is stricter:

> Can the same recovery condition be expressed using only the prescribed filtered/graded data, without importing the full pro-3 group or a preferred free lift?

This gate is deliberately definition-first. No finite scan is authorized.

## 1. First-order character parameter

Every candidate
\[
\rho:G\to1+3\mathbf Z/9
\]
has the form
\[
\rho(g)=1+3\lambda(\bar g)\pmod9,
\]
where
\[
\lambda\in V^*=H^1(G,\mathbf F_3),
\qquad
V=G/\Phi(G).
\]

Thus the first orientation digit is equivalently a linear functional
\[
\lambda=(a_1,a_2,a_3,a_4).
\]

For the canonical orientation,
\[
\lambda_\chi=(0,1,0,0).
\]

## 2. Frozen-coordinate obstruction

The twisted H^1 lifting calculation already proved that a mod-3 cocycle with generator values
\[
f=(f_1,f_2,f_3,f_4)
\]
lifts to the twisted mod-9 coefficient module exactly when
\[
B_\lambda(f)
=
(1-a_2)f_1+a_1f_2-a_4f_3+a_3f_4
=0.
\]

Therefore the canonical \(\lambda\) is the unique solution of
\[
B_\lambda=0.
\]

The key structural observation is that this obstruction is **first-order**: it uses only the mod-3 character parameter \(\lambda\), the degree-2 commutator pairing, and the first q=3 power contribution. No 3-adic quantity beyond the first digit is used.

## 3. Candidate graded carrier

The natural candidate carrier is the first non-quadratic/restricted layer of the Zassenhaus object:

- \(V=L_1=G/\Phi(G)\);
- the degree-2 alternating pairing encoded by the Demuškin relation;
- the degree-3 restricted/power contribution associated to the q=3 term;
- the induced extension/obstruction map obtained by evaluating a \(\lambda\)-twisted degree-one derivation on that degree-3 relation data.

In the frozen basis this carrier must reproduce
\[
B_\lambda(f)
=
(1-a_2)f_1+a_1f_2-a_4f_3+a_3f_4.
\]

The important distinction is that the carrier is not the trivial-coefficient Bockstein. The Bockstein forgets the \(\lambda\)-action. Here the candidate explicitly retains the first-order twist \(\lambda\).

## 4. What remains to prove

### F1 — Definition

Construct the obstruction map directly from the restricted/filtered object, with no reference to a chosen free presentation.

### F2 — Presentation/lift independence

Prove that changing a minimal presentation or free lift changes the coordinate formula but not the intrinsic zero set
\[
\{\lambda\in V^*:B_\lambda=0\}.
\]

This is mandatory because earlier lift-dependent scalar constructions failed precisely here.

### F3 — Automorphism naturality

Show the zero set is functorial under automorphisms of the filtered/graded object.

### F4 — Uniqueness

Show that the zero set consists of exactly one \(\lambda\), namely
\[
\lambda_\chi=(0,1,0,0)
\]
in the frozen coordinates.

### F5 — Factorization

Only after F1–F4 pass may we claim:

\[
\boxed{\chi\bmod9\text{ is recoverable from the prescribed filtered/graded datum}.}
\]

## 5. Current status

**F0: PASS / strong candidate.**

The full-group twisted cohomology criterion has an explicit first-order formula whose variables are exactly the degree-one character parameter and the q=3 relation/power data.

**F1–F5: OPEN.**

No scan is authorized. The next task is a hand proof that the obstruction zero set is an intrinsic construction on the allowed filtered/graded object, not merely a coordinate rewrite of the full-group twisted cohomology calculation.

## 6. Critical warning

Do not silently identify:

1. the ordinary Bockstein,
2. the twisted H^1 surjectivity criterion,
3. the associated graded restricted relation,
4. the full filtered group.

They are different objects. The present gate succeeds only if (2) can be factored through (3), with the exact invariance demanded by F1–F5.
