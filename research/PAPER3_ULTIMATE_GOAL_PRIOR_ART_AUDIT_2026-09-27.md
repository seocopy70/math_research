# Paper 3 Ultimate-Goal Prior-Art Audit — 2026-09-27

## Scope

Before opening N3 target selection, the project-level ultimate goal was screened against prior literature:

> Develop a general theory of finite filtered observation and recognition thresholds for global invariants of filtered algebraic/pro-p objects, including finite recognizability, sharp thresholds, and information-loss obstructions.

This audit is a prior-art boundary check, not a priority claim.

## Key findings

### 1. Finite determinacy is established prior art

Finite determinacy studies when a finite jet determines an object up to an equivalence relation, and the minimal such jet order is commonly called a degree/order of determinacy. This is well established in singularity theory and filtered-module settings.

This is conceptually adjacent to the proposed threshold language, but the usual setup is object-level:
fixed object + equivalence orbit + finite jet.

The present program is intended to be category-level:
all G,H in an admissible class + a fixed target T + a prescribed filtration/window.

Conclusion: the phrase "finite determinacy" cannot be claimed as a new general concept.

### 2. Profinite recognition / finite-quotient recognition is established prior art

There is a large literature on whether group properties or structures are visible in finite quotients/profinite completions ("profinite rigidity", recognition from finite quotients, etc.). This includes recognition of decompositions, central extensions, cohomology, and other structure.

Conclusion: "recognition from finite quotients" is not new terminology or a new general problem.

### 3. Strongest near-match: Efrat–Mináč, Galois groups and cohomological functors

Efrat–Mináč (TAMS 2017; arXiv:1103.1508) explicitly asks how much group-theoretic information is needed to determine a cohomological target and characterizes a minimal quotient. Their Theorem A gives a canonical minimal quotient determining the relevant cohomology, and their general "cohomological duality triple" framework treats other target/cohomological constructions.

This is the most important prior-art warning for Paper 3.

It is substantially close in philosophy to "finite information needed to recognize a target", and any Paper 3 target involving cohomology/Bockstein must explicitly separate itself from this framework.

Logical difference still available:
- Efrat–Mináč: minimal quotient for a fixed group/target and a cohomological determination property;
- Paper 3 proposal: a uniform threshold across an admissible category, indexed by a prescribed filtration, with explicit recognition-vs-factorization distinction and separation lower bounds between different objects sharing the same finite window.

Conclusion: the category-level uniform threshold is NOT established as new by this audit; it remains OPEN and requires a targeted equivalence/non-equivalence analysis against the Efrat–Mináč framework.

### 4. Zassenhaus + cohomological finite-level determination is also established

Efrat and related literature connect Zassenhaus quotients with cohomology, Massey products, representations, and finite quotient structure. Efrat–Mináč in particular gives a Zassenhaus-level quotient determining mod-p cohomology in the relevant Galois setting.

Therefore a Paper 3 whose sole contribution is "a finite Zassenhaus quotient determines a cohomological/Bockstein target" is not sufficient novelty.

### 5. Finite quotient determining an infinite filtered/graded object also occurs elsewhere

There are examples in graded Lie/pro-p theory where an infinite object or structural type is uniquely determined by a suitable finite-dimensional quotient. For example, Avitabile–Mattarei prove that certain Nottingham algebras are uniquely determined by finite-dimensional quotients.

Conclusion: finite truncation/finite quotient recognition itself is not new.

## What remains potentially distinct

The current defensible novelty candidate is narrower:

> For a declared category C and natural filtration D_bullet, study the uniform category-relative threshold
> r_T(C;D_bullet)
> at which the finite window W_n becomes sufficient to recognize a target T across all objects of C, together with sharp separation lower bounds and a systematic comparison between recognition threshold and factorization threshold.

Potentially distinctive ingredients are therefore:
1. uniformity across a category rather than one fixed object;
2. the filtration-indexed threshold as the primary object of study;
3. explicit distinction between factorization depth and recognition depth;
4. sharp lower bounds obtained by pairs with identical windows but different targets;
5. comparison across targets/categories/filtrations;
6. information-loss obstructions as part of the threshold theory.

No exact theorem with this full combination was located in the present search.

## Immediate consequence for N3

Do NOT select Bockstein merely because it is naturally finite-level.

Bockstein/cohomological targets are high-risk for redundancy because Efrat–Mináč and the Zassenhaus/cohomology literature already contain minimal-quotient determination results.

N3 must first perform a direct framework-level comparison:
- Can r_T(C;D_bullet) be recovered as a special case of an existing minimal-quotient/cohomological-duality framework?
- If yes, is the uniform category threshold genuinely additional?
- If no, what exact theorem/definition is missing?
- Does the recognition-vs-factorization split add a theorem rather than notation?
- Is the lower-bound/separation theory genuinely absent?

## Current classification

- Broad "finite determinacy": HISTORICAL / KNOWN
- Broad "recognition from finite quotients": HISTORICAL / KNOWN
- Minimal quotient determining cohomology/related targets: KNOWN
- Zassenhaus finite-level cohomological determination: KNOWN
- Exact category-relative filtration threshold r_T as a general framework: OPEN
- Ultimate general theory: OPEN / CONDITIONAL
- Bockstein as first target: NOT SELECTED; prior-art risk HIGH
- N3: OPEN / LOAD-BEARING

## Sources checked

- Efrat–Mináč, *Galois groups and cohomological functors*, TAMS 369 (2017), 2697–2720, arXiv:1103.1508.
- Efrat, *The Zassenhaus filtration, Massey products, and representations of profinite groups*, Advances in Mathematics 263 (2014), 389–411.
- Efrat, *The p-Zassenhaus filtration of a free profinite group and shuffle relations* (2021/2022 publication trail).
- Avitabile–Mattarei, *The earliest diamond of finite type in Nottingham algebras*, J. Lie Theory 32 (2022), 771–796, arXiv:2106.14796.
- Recent profinite-recognition literature, including Morales, *Profinite properties of residually free groups* (2024/2025 publication trail), and related profinite rigidity work.
- Finite-determinacy literature for jets/filtered modules, including Kerner et al., *Finite determinacy of matrices over local rings* (J. Pure Appl. Algebra 223 (2019), 1288–1321).

## Decision

Before any substantial N3 computation, perform a framework-level prior-art audit centered on Efrat–Mináč and finite-determinacy/minimal-quotient theory. Only if the category-uniform filtration threshold survives that comparison should a concrete target be selected.
