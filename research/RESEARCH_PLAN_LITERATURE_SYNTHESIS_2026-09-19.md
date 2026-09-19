# Literature and Research Plan Update — 2026-09-19

## Scope

This record consolidates the implications of the full-paper audits of:

1. Simone Blumer and Claudio Quadrelli, *Variations of Demuškin groups that are not absolute Galois groups and their Lie algebras*, arXiv:2603.15464v2.
2. Pál–Quick, *A_3-formality for Demushkin groups at odd primes*, arXiv:2601.07551v2.

The purpose is not to replace the existing Gates, but to refine the research center of gravity and record the literature-supported boundaries.

## 1. Direct relevance to the current project

### Blumer–Quadrelli

The paper gives the canonical Demuškin orientation in the form
[
\theta_G(y_1)=(1-q)^{-1}.
]
For (q=3),
[
\theta_G(y_1)=-1/2.
]
This independently matches the exact crossed-derivation reconstruction already obtained in the project:
[
\rho(x_2)=-1/2.
]

The paper also gives a concrete near-Demuškin family (mathcal F_1) for which the q-dependent power term disappears from the quadratic associated graded relation while q remains visible in the original/orientation-sensitive structure. This independently supports the project's negative boundary
[
\text{bare quadratic graded data}\not\Rightarrow\chi.
]

Its open-subgroup computation
[
U^{ab}\cong \mathbf Z_p^{2(d-1)p+1}\times(\mathbf Z/q)^p
]
also demonstrates that q-information can survive in richer subgroup-level data even when it is absent from a low-degree associated graded shadow.

Critical boundary: this paper does not prove the project's relation-jet reconstruction theorem and does not identify its invariants with the project's exact filtered relation-jet carrier.

### Pál–Quick

The paper proves a sharp higher-order distinction for Demuškin groups: q=3 is not A_3-formal, while the stated other q-ranges are A_3-formal. The proof uses the Benson–Krause–Schwede canonical class and Dwyer U_4(F_3) lifting.

This independently supports the structural principle
[
\text{quadratic data}\not\Rightarrow\text{all q-sensitive information},
]
and the pattern
[
\text{higher relation structure}
\to
\text{lifting obstruction}
\to
\text{cohomological invariant}.
]

Critical boundary: its higher invariant is not identified with the project's exact Z_3 relation-jet carrier and it does not reconstruct the full cyclotomic character
[
\chi:G\to\mathbf Z_3^\times.
]

## 2. Reassessment of existing project results

The literature strengthens, rather than weakens, the following hierarchy.

### Closed negative boundary

[
\boxed{\text{bare associated graded/quadratic object}\not\Rightarrow\chi\bmod 9}
]

and the broader universal finite-information bounded-degree obstruction remains CLOSED.

### Positive finite-level result

For the q=3 standard presentation, the projective degree-(2,3) filtered relation jet
[
J_3=[(R_2,P_3)]^{proj}
]
determines
[
\chi\bmod 9.
]

### Positive exact fixed-q result

With exact Z_3 coefficients, the same degree-(2,3) relation carrier determines the full q=3 orientation:
[
1+2\rho(x_2)=0,
\qquad
\rho(x_2)=-1/2=(1-3)^{-1}.
]

### Full tower

A compatible full filtered relation-jet tower determines the compatible finite-level characters and hence
[
\chi=\varprojlim_n\chi_n.
]
This is a completion theorem, not by itself the main novelty claim.

### Representation branch

The W/U/O representation computations remain useful structural work, but the literature review gives no justified identification
[
W_{45},U_{10},O_{10}\longrightarrow\chi.
]
Therefore they should not currently be presented as the orientation carrier. Further expansion of this branch is not the priority unless a mathematically independent bridge to the relation-jet invariant appears.

## 3. Revised research center

The main question should now be sharpened to:

> Which intrinsic enrichment of the quadratic filtered relation is exactly sufficient to recover the cyclotomic orientation?

The current information boundary is:

[
\boxed{
\text{bare graded}
<
\text{projective degree-(2,3) relation carrier}
\le
\text{full compatible relation-jet tower}.
}
]

The natural research target is therefore not merely “can orientation be reconstructed?”, but the structure and minimality of the carrier that makes reconstruction possible.

## 4. Authorized next research plan

### Phase A — consolidate the degree-(2,3) theorem

Make the following a single theorem chain:

1. intrinsic definition of the projective degree-(2,3) relation carrier;
2. presentation/lift/gauge invariance;
3. crossed-derivation coefficient functional;
4. uniqueness of the q=3 solution modulo 9;
5. exact Z_3 recovery for fixed q=3;
6. precise distinction between finite-level recovery and full 3-adic recovery.

No new large scan.

### Phase B — characterize the coarsest non-tautological carrier

The natural quotient-category audit already shows that the raw projective jet is not minimal in the natural mod-3 Theta-observable category: bracket components annihilated by all degree-one evaluations can be discarded, leaving the quadratic relation line together with the restricted-cubic component.

The next goal is to give this compressed carrier a clean, non-tautological definition and determine exactly which structure is necessary for recovery.

The exact Z_3 analogue remains open: restricted Lie algebra scalar extension is not a valid replacement. The exact compressed carrier must remain in the filtered relation/augmentation framework.

### Phase C — establish the strongest useful minimality statement

Distinguish three claims and never conflate them:

- relative minimality among specified quotients of the relation jet;
- universal/coarsest property in a precisely defined carrier category;
- absolute minimality among all conceivable invariants, which is ill-posed unless the admissible category is fixed.

The first two are the realistic theorem targets.

### Phase D — compare with higher cohomological invariants

Only after Phase A/B is stabilized, compare the relation-jet carrier with the Pál–Quick A_3 obstruction.

The target is a natural map, factorization, or precise obstruction to such a map. Do not claim the invariants are identical without proof.

### Phase E — use Blumer–Quadrelli as a structural comparison

Use their near-Demuškin examples to clarify the information hierarchy:
[
\text{presentation/orientation data}
\supset
\text{filtered data}
\supset
\text{quadratic graded shadow}.
]
Do not substitute their open-subgroup torsion invariant for the project's intrinsic relation-jet carrier.

### Phase F — defer broad representation scans

Do not expand the W/U/O or rank-4 IA branch merely because it contains higher-order structure. Continue it only if a rigorous bridge to the orientation-recovery functional is found. The relation-jet branch has the stronger currently verified link to \chi.

## 5. Frozen boundaries

Do not reopen without new evidence:

- bare F_3 associated graded \Rightarrow full \chi;
- naive Z_3 restricted-Lie scalar extension;
- universal finite bounded-degree finite-information \Rightarrow full \chi;
- arbitrary preferred Nielsen/free-group lift as an intrinsic orientation invariant.

The literature audits do not reopen any of these Gates.

## 6. Research thesis after the literature audit

The strongest defensible current thesis is:

[
\boxed{
\text{Quadratic graded information can erase cyclotomic orientation data,}
\\
\text{whereas a suitable intrinsic higher filtered relation carrier can restore it.}
}
]

The novelty question is now concentrated on identifying and proving the smallest natural carrier, not on merely exhibiting a sufficiently rich full tower.
