# Paper 4 — Literature / novelty audit — 2026-10-05

## Classification

**Literature audit status: CONDITIONAL / no prior source located that directly states the full Paper-4 theorem.**

The audit confirms that the ingredients used by Paper 4 are classical or closely related in the literature, while the exact combination below was not located in the searched literature:

1. for a free pro-p group F and an index-p kernel K,
   D_n(F) ∩ K ⊆ D_{ceil(n/p)}(K);
2. the resulting all-s critical transfer-boundary consequence;
3. the intrinsic torsion-line predicate ε_s on the finite Zassenhaus window;
4. the exact unmarked separation threshold n_sep(s)=p^s+1 for the declared stress family.

This is **not a publication-level novelty proof**. It is a strong negative-search result within the searched literature and terminology.

## 1. Directly relevant classical literature

### Zassenhaus/Jennings/Lazard filtration

Efrat's 2023 JIMJ paper recalls the p-Zassenhaus filtration and its product formula, and records the inductive formula
D_n(G)=D_{ceil(n/p)}(G)^p · product_{i+j=n}[D_i(G),D_j(G)].
It also develops Magnus-coefficient restrictions for elements of the Zassenhaus filtration.

Relevant source: I. Efrat, *The p-Zassenhaus filtration of a free profinite group and shuffle relations*, J. Inst. Math. Jussieu 22 (2023), 961–983, DOI 10.1017/S1474748021000426.

### Magnus expansion / initial forms

The standard identification of the completed group algebra of a free pro-p group with a noncommutative formal power-series algebra, and the use of Magnus expansions and initial forms, are classical and appear throughout the pro-p Zassenhaus literature.

### Weighted valuations and index-p Schreier generators

Jaikin-Zapirain et al., *Groups of positive weighted deficiency and their applications*, develops weight functions on free pro-p groups and proves an index-p weighted Schreier result: for an index-p subgroup H, a Schreier generating set consisting of
y, [y,x], ..., [y,x,...,x], x^p
is W-optimal when W is a weight function. It also proves the weighted Schreier formula.

This is the closest conceptual precedent found for the present subgroup-comparison argument.

## 2. Important near-precedent

The weighted-Schreier literature shows that index-p passage changes generator weights in precisely the pattern relevant here: iterated commutators acquire weights up to p-1 and the distinguished p-th power has weight p.

However, the searched source does **not** state the Paper-4 comparison
D_n(F)∩K ⊆ D_{ceil(n/p)}(K)
as a theorem, nor does it state the corresponding all-s transfer-kernel bound used here.

Therefore the Paper-4 Magnus prefix-code proof should be presented as an explicit derivation, while citing weighted Schreier theory as background/precedent.

## 3. Cohomology / intrinsic radical precedent

The pro-p literature standardly identifies the degree-2 cup product with the quadratic/initial-form data of the defining relations. For one-relator groups with commutator-type initial relation, the radical of the cup pairing is therefore a standard intrinsic object.

The Mináč–Pasini–Quadrelli–Tân literature on mild pro-p groups and Koszul duality gives explicit formulas relating Demushkin/one-relator initial forms, cup products, and the Zassenhaus graded algebra.

This validates the use of the cup-radical line as an intrinsic construction in the declared nondegenerate scope, but no source located in the audit defines the Paper-4 ε_s invariant.

## 4. Finite-quotient recognition precedent

Quadrelli's 2015 *Finite quotients of Galois pro-p groups and rigid fields* proves that equality of certain canonical finite quotients can force strong structural conclusions for finitely generated Bloch–Kato pro-p groups. This is conceptually close to the Paper-4 philosophy that finite canonical quotients can detect structure.

However, that theorem concerns different canonical quotients and a different structural target. It does not give the Paper-4 finite-window separation theorem or the p^s+1 threshold.

Efrat's work on the Zassenhaus filtration and Massey products likewise establishes deep finite-quotient/cohomological recognition results, but not the present stress-family invariant.

## 5. Transfer literature

Classical transfer/Schreier theory is of course extensive. The search also located Efrat's cohomological transfer/intersection-theorem program, where transfer principles connect Zassenhaus layers with cohomological kernels.

No searched source was found that uses the specific finite-window invariant
ε_s(W) = p^{s-1}V(t) mod p^s K^ab
or the a=s versus a=∞ comparison in the present family.

The word “transfer” should therefore not be presented as a new invention. The novelty claim should instead concern the particular filtered finite-window obstruction and its intrinsic normalization.

## 6. Closest potential threat to novelty

The main threat is **not** a paper stating the final theorem verbatim. It is that the general subgroup-comparison theorem might be derivable quickly from existing weighted-Schreier/valuation machinery.

The strongest precedent found is the weighted-Schreier result for index-p subgroups of free pro-p groups. It constructs optimal generators with exactly the commutator/p-power pattern used by Paper 4.

Accordingly, the manuscript must not claim that the Magnus prefix-code argument is novel merely because no exact sentence was found. A publication-level novelty claim should first compare the Paper-4 SC proof line-by-line against the weighted-Schreier machinery and determine whether SC follows as a short corollary.

## 7. Current novelty assessment

- Basic Zassenhaus/Jennings/Lazard facts: **HISTORICAL / STANDARD**.
- Magnus embedding and leading-term methods: **HISTORICAL / STANDARD**.
- Index-p Schreier and transfer formulas: **HISTORICAL / STANDARD**.
- Weighted-Schreier treatment of index-p subgroups: **HISTORICAL / CLOSE PRECEDENT**.
- Exact SC theorem in Paper-4 form: **OPEN as a novelty question; not located directly**.
- TF_s consequence: **OPEN as a novelty question, but structurally close to standard Jennings + SC**.
- ε_s intrinsic finite-window invariant: **OPEN / strongest apparent novelty candidate**.
- a=s versus a=∞ finite-window non-isomorphism: **OPEN / strongest apparent application-level novelty candidate**.
- exact threshold n_sep(s)=p^s+1: **OPEN / candidate theorem-level novelty, conditional on no stronger derivation in the weighted-Schreier literature**.

## 8. Required next literature check before a strong novelty claim

The next audit should inspect the full weighted-Schreier paper around Lemmas 3.10, 3.16 and Theorem 3.12, and explicitly test whether the standard Zassenhaus weight valuation yields SC immediately.

If it does, SC should be cited as a corollary/rediscovery rather than claimed as the novel contribution.

The novelty candidate would then move upward to the intrinsic ε_s construction and the exact finite-window separation theorem.

## Sources checked

- Efrat, *The p-Zassenhaus Filtration of a Free Profinite Group and Shuffle Relations*, JIMJ 22 (2023), 961–983.
- Efrat, *The Zassenhaus Filtration, Massey Products, and Representations of Profinite Groups*, Advances in Mathematics 263 (2014), 389–411.
- Chapman–Efrat, *Filtrations of free groups arising from the lower central series* (2016).
- Mináč–Rogelstad–Tân, *Dimensions of Zassenhaus filtration subquotients of some pro-p-groups* (2014/2016).
- Jaikin-Zapirain et al., *Groups of positive weighted deficiency and their applications*.
- Mináč–Pasini–Quadrelli–Tân, *Koszul algebras and quadratic duals in Galois cohomology*, Advances in Mathematics 380 (2021), 107569.
- Quadrelli, *Finite quotients of Galois pro-p groups and rigid fields*, Ann. Math. Québec 39 (2015), 113–120.

## Bottom line

The search did **not** find the Paper-4 final theorem in the literature. But it did find a sufficiently close weighted-Schreier framework that prevents an unconditional novelty claim for SC itself until that framework is checked as a possible derivation.

The safest current classification is:

**Paper-4 mathematical result: PASS / CLOSED in the declared scope.**

**Publication novelty: CONDITIONAL / OPEN pending the weighted-Schreier derivation check and a broader database-level literature search.**
