# PAPER 3 — δ3 / Mazur deformation / Massey embedding prior-art audit — 2026-09-28

## Scope

Before any new computation, compare the surviving secondary object
\[
\rho_3\longmapsto \delta_{3,\rho_3},
\qquad
\delta_{3,\rho_3}:H^1(G,\mathbf Z/9(\rho_2))\to H^2(G,\mathbf F_3),
\]
with three established mechanisms:

1. Mazur-style deformation-theoretic lifting obstructions;
2. Efrat's Zassenhaus/Massey/unipotent embedding-problem mechanism;
3. recent A_3-formality / strong Massey-vanishing work for Demushkin groups.

This is a prior-art identity check, not a novelty claim.

## 1. Exact project object

For fixed $(G,\rho_2)$ let
\[
L(\rho_2)=\{\rho_3:G\to(\mathbf Z/27)^\times:\rho_3\bmod 9=\rho_2\}.
\]
For each $\rho_3\in L(\rho_2)$, the coefficient extension
\[
0\to\mathbf F_3\to\mathbf Z/27(\rho_3)
\to\mathbf Z/9(\rho_2)\to0
\]
gives
\[
\delta_{3,\rho_3}:H^1(G,\mathbf Z/9(\rho_2))
\to H^2(G,\mathbf F_3).
\]
Thus $\delta_{3,\rho_3}(f)=0$ iff the cohomology class $f$ lifts through this coefficient extension.

Repository status before this audit: the family is PROVED as a cohomological object/natural family at fixed $(G,\rho_2)$; deriving the family from a finite filtered window remains OPEN.

## 2. Mazur comparison

### What is genuinely the same

Mazur's deformation theory uses small extensions of coefficient rings and places the obstruction to lifting a representation in an $H^2$-group. The general pattern is:

- a lift/deformation problem over a small extension;
- an obstruction class in $H^2$;
- vanishing of that class iff the specified lift exists.

This is the same abstract obstruction-theoretic mechanism.

### What is not the same

The project $\delta_{3,\rho_3}$ is not, as currently defined, the obstruction to lifting the coefficient character $\rho_2$ to $\rho_3$.

Instead:

- $\rho_3$ is already fixed as the coefficient action;
- the extension $0\to F_3\to Z/27(\rho_3)\to Z/9(\rho_2)\to0$ is then fixed;
- $\delta_{3,\rho_3}$ obstructs lifting a class
  $f\in H^1(G,Z/9(\rho_2))$ to $H^1(G,Z/27(\rho_3))$.

So the variable being lifted is the **1-cocycle/cohomology class $f$**, not the representation/coefficient character $\rho_2$.

Therefore:

- “$\delta_3$ is a standard small-extension $H^2$ obstruction mechanism”: **PASS / CLOSED (KNOWN)**.
- “$\delta_{3,\rho_3}$ is literally Mazur's deformation obstruction for $\rho_2\rightsquigarrow\rho_3$”: **FAIL / CLOSED**.
- “Mazur supplies a prior-art identity theorem eliminating the project’s $\delta_3$ object”: **NO**.

Mazur is therefore **methodological prior art, not object-level identity**.

## 3. Efrat / Massey / unipotent embedding comparison

Efrat (2014) relates the p-Zassenhaus filtration to higher Massey products and upper-triangular unipotent representations. The relevant obstruction is whether a representation into a unipotent group $U_n(F_p)$ extends to the next embedding problem; this is equivalent to a higher Massey/representation-theoretic lifting condition.

The project object differs at the input level:

- Massey embedding problem: the lifted object is a **unipotent representation** / defining system, with obstruction tied to a higher Massey product.
- $\delta_{3,\rho_3}$: the lifted object is a **degree-one cohomology class with coefficients in a twisted cyclic module**, after the coefficient character $\rho_3$ has already been chosen.

Both land in $H^2$, but the source data and extension problem are different.

Hence:

- “the same abstract obstruction theory occurs”: **PASS / CLOSED (KNOWN)**.
- “$\delta_3$ is exactly the U_4/F_3 Massey embedding obstruction”: **FAIL / CLOSED**.
- “strong Massey vanishing makes the whole $\delta_3$ family zero”: **NOT IMPLIED**.

In particular, vanishing of higher Massey products concerns the existence/vanishing of Massey classes under specified cup/defining-system conditions. It does not say that every connecting map
$H^1(G,Z/9(\rho_2))\to H^2(G,F_3)$ arising from every coefficient lift $\rho_3$ is zero.

## 4. Demushkin strong Massey vanishing

The literature does establish strong higher-Massey vanishing for pro-p Demushkin groups (with the relevant odd-prime results attributed in the modern Pál–Quick treatment to Mináč–Tân and Pál–Szabó). Therefore any target defined solely as “Demuškin higher Massey vanishing” is constant in the fixed Demuškin category and is not a useful orientation carrier.

This reproduces an already-closed project boundary:

- fixed-category Massey vanishing target: **FAIL / CLOSED — trivial/constant target**.

But that theorem does **not** identify the coefficient-extension family $\{\delta_{3,\rho_3}\}$ with the Massey target.

## 5. A_3-formality comparison

Pál–Quick's 2026 A_3-formality work for odd primes detects a q-dependent higher cohomological distinction: for odd p, Demuškin groups with q-invariant not equal to 3 are A_3-formal, while q=3 is not. Their pro-2 paper develops a related canonical-class/defining-system interpretation.

This is important prior art against any broad claim that “higher cohomology has not detected the q-layer.”

However, the input is the continuous-cochain DGA/Hochschild canonical class and its defining-system interpretation, not the finite filtered group window $W_n$ and not the coefficient-extension family $\rho_3\mapsto\delta_{3,\rho_3}$.

Thus:

- higher cohomological q-detection: **KNOWN**;
- exact identity with the project $\delta_3$ family: **OPEN / not established**;
- finite filtered reconstruction of the $\delta_3$ family: **OPEN**.

## 6. Critical logical boundary

The proposed “Novelty-first” move is therefore only partially confirmed.

Confirmed:
- the $H^2$ obstruction mechanism itself is classical;
- unipotent/Massey lifting obstructions are classical;
- Demuškin strong Massey vanishing is known;
- A_3-formality gives independent higher-cohomological q-detection.

Not confirmed:
- that the project's $\delta_{3,\rho_3}$ is the same mathematical object as a Massey embedding obstruction;
- that strong Massey vanishing trivializes the $\delta_3$ family;
- that Mazur deformation theory already contains the exact finite-window factorization question.

The decisive novelty gate remains:
\[
W_n(G)\longrightarrow
\{\delta_{3,\rho_3}\}_{\rho_3\in L(\rho_2)}
\]
without importing $\chi$, $q$, or an external orientation.

## 7. Result classification

| Claim | Classification |
|---|---|
| $\delta_{3,\rho_3}$ is a connecting obstruction in $H^2$ | **KNOWN / PASS-CLOSED** |
| Mazur supplies the general small-extension obstruction template | **KNOWN / PASS-CLOSED** |
| $\delta_{3,\rho_3}$ is literally Mazur's deformation obstruction for $\rho_2\to\rho_3$ | **FAIL / CLOSED** |
| $\delta_3$ is literally the Efrat $U_4$ / Massey embedding obstruction | **FAIL / CLOSED** |
| Demuškin strong Massey vanishing is known | **PASS / CLOSED** |
| strong Massey vanishing forces $\delta_3\equiv0$ | **NOT ESTABLISHED; do not infer** |
| A_3-formality gives q-sensitive higher cohomological information | **KNOWN / PASS-CLOSED** |
| A_3-formality = the project $\delta_3$ family | **OPEN / not found** |
| finite filtered $W_n$ factorization to $\delta_3$ | **OPEN / LOAD-BEARING** |
| novelty of the finite-window factorization theorem | **OPEN / CONDITIONAL** |

## 8. Next authorized action

Do **not** compute the carrier yet.

The next literature check should be narrower: determine whether any existing Kummerian/1-cyclotomic theorem explicitly constructs the coefficient-lift torsor
$L(\rho_2)$ or an equivalent family of connecting maps from a finite quotient/finite Zassenhaus data, rather than merely assuming the orientation and proving lifting consequences.

Only if that comparison is negative should the finite-window carrier construction resume.

## Sources

- I. Efrat, *The Zassenhaus filtration, Massey products, and representations of profinite groups*, Adv. Math. 263 (2014), 389–411.
- J. Mináč and N. D. Tân, *Triple Massey products and Galois theory*, JEMS 19 (2017), 255–284.
- A. Pál and G. Quick, *A_3-formality for Demushkin groups at odd primes*, arXiv:2601.07551v2.
- A. Pál and G. Quick, *A_3-formality for pro-2 Demushkin groups*, arXiv:2607.01028v2.
- B. Mazur, *Deforming Galois representations*, 1989.

## Audit status

**PASS / LOCAL**: the proposed Mazur/Massey identity check was completed at the level needed to decide whether the current $\delta_3$ carrier should be immediately closed as a rediscovery. It should not be closed on that basis. The remaining finite-window novelty gate is still OPEN.
