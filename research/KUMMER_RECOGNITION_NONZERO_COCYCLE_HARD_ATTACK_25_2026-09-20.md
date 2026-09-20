# HARD ATTACK 25 — Nonzero Kummer cocycles cannot select the orientation — 2026-09-20

## Objective

Attack the most obvious repair of the vacuous criterion
\[
\exists f\in Z^1(Q,A_k(\rho))
\]
by replacing it with
\[
\exists f\ne0.
\]

The goal is to determine whether nontrivial twisted 1-cocycles can possibly characterize the canonical orientation on the rank-four one-relator Demuškin family.

## 1. One-relator cocycle equation

Fix a candidate
\[
\rho:G\to U_k,
\qquad A_k(\rho)=\mathbf Z/3^k
\]
with the corresponding scalar action.

For the free pro-3 group
\[
F=\langle x_1,x_2,x_3,x_4\rangle,
\]
a crossed homomorphism is determined freely by the four values
\[
a_i=f(x_i)\in A_k.
\]

Imposing the single relator
\[
r=x_1^q[x_1,x_2][x_3,x_4]
\]
gives exactly one linear obstruction
\[
\mathrm{Obs}_\rho(a_1,a_2,a_3,a_4)=f(r)\in A_k.
\]

For fixed \(\rho\), the map
\[
\mathrm{Obs}_\rho:A_k^4\to A_k
\]
is additive in the four cocycle variables. Its coefficients depend on \(\rho\), but the obstruction is still a single homomorphism of finite abelian groups.

Therefore
\[
Z^1(G,A_k(\rho))=\ker(\mathrm{Obs}_\rho).
\]

Since a homomorphism from \(A_k^4\) to \(A_k\) has image of cardinality at most \(|A_k|\),
\[
|Z^1(G,A_k(\rho))|
\ge |A_k|^3.
\]
In particular,
\[
Z^1(G,A_k(\rho))\ne0
\]
for every candidate \(\rho\), including candidates different from the canonical orientation.

This argument does not use the value of \(q\) and does not assume the canonical orientation.

## 2. Consequence

The criterion
\[
\exists f\ne0
\]
is therefore not merely unproved as a selector. On the standard one-relator family it is **provably non-discriminating**: every candidate coefficient action has nonzero crossed homomorphisms.

Likewise, any criterion depending only on the fact that the first twisted cohomology group is nontrivial cannot recover \(\chi\).

The obstruction is structural: four generator values are constrained by only one relator equation. A nonzero kernel is unavoidable.

## 3. What this does and does not close

Closed:

- existence of a crossed homomorphism as a selector;
- existence of a nonzero crossed homomorphism as a selector;
- any selector whose only input is the Boolean property
  \[
  H^1(G,A_k(\rho))\ne0.
  \]

Not closed:

- richer invariants of the entire twisted module \(H^1(G,A_k(\rho))\);
- dimensions/cardinalities of twisted cohomology, if those vary with \(\rho\);
- cup products, Bocksteins, extension classes, or higher operations with the twisted coefficients;
- a genuinely group-sensitive universal obstruction built from the finite filtered quotient.

Those remain subject to the q-blindness and non-tautology gates.

## 4. Important strengthening

The result shows that the missing ingredient is not simply “require a nontrivial Kummer class.”

The finite recognition problem requires a property that depends on **how the candidate coefficient action interacts with additional intrinsic finite group structure**, rather than merely on the existence of twisted 1-cocycles.

Thus the next meaningful candidate must use an interaction such as:
\[
\text{filtered extension class}
\quad+\quad
\text{twisted coefficient action},
\]
or another independently defined group-sensitive obstruction.

## Decision

- \(\exists f\): **FAIL / CLOSED**.
- \(\exists f\ne0\): **FAIL / CLOSED** on the standard one-relator family.
- Boolean nonvanishing of \(H^1(G,A_k(\rho))\): **FAIL / CLOSED** as an orientation selector.
- richer twisted-cohomological selector: **OPEN**.
- genuinely group-sensitive finite obstruction: **OPEN**.
- universal same-carrier/different-orientation no-go: **OPEN**.

No numerical scan is authorized merely to test nonzero-cocycle existence; the structural argument already closes that branch.
