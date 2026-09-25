# EXTENDED SHARP FINITE-WINDOW CORRECTED AUDIT — 2026-09-26

## Object
Uploaded manuscript `sharp_finite_window_corrected.tex`, proposed as a follow-up paper extending the finite-window Kummer recognition work.

## Independent source/PDF check
The uploaded source was materialized and compiled locally with three `pdflatex` passes. Exit status was 0. No LaTeX errors, undefined references, or fatal errors occurred. Two hyperref PDF-string warnings remain because mathematical title/author metadata is not sanitized; these are cosmetic and should be removed before submission.

The generated PDF is only 3 pages. The short length is not itself a defect, but it exposes that several theorem dependencies are currently asserted by reference to U2/U3/U5 without being proved or cited in this standalone manuscript.

## Critical mathematical findings

### 1. Sharpness theorem has an incorrect quantifier
The manuscript states Theorem 3.1 for “all odd p, all d, all f”, but the displayed sharpness witness explicitly says “For rank d >= 4” and then uses x_3 in ker(rho) with F_3=0 to obtain a unit translation.

For d=2 there is no x_3. In the f >= k case with rho(x_1)=1 and rho(x_2)=1+p, the relation obstruction forces p z(x_1)=0, so the displayed construction cannot make z(ker rho)=A_k. Thus the claimed surjective affine representation witness is not established for d=2.

**Classification: FAIL/CLOSED as stated.**
Safe repair: restrict the sharp factorization-depth theorem to d >= 4, or separately prove the d=2 case. Do not retain the all-even-rank quantifier without a new proof.

### 2. Standalone theorem proof is not publication-grade
The main theorem proof is currently:
“U2 transfers to G_f, U3 F_i=0, above solving gives unique rho, U5 gives induction.”
These are research-internal labels, not a self-contained proof. The follow-up paper must either:
- reproduce the required U1/U2/U3/U5 lemmas with hypotheses and proofs; or
- explicitly cite a prior companion theorem and state exactly which hypotheses are imported.

In particular U5 cannot be treated as a black box if the paper claims a new recognition theorem.

**Classification: OPEN / publication-critical.**

### 3. The manuscript does not define all principal objects
The text uses K_k, P_n, S_k, A_k, U_{1,k}, chi_{G_f}, H^1(Q,A_k(rho)), and the finite-window coefficient reduction without standalone definitions.

**Classification: OPEN / publication-critical.**

### 4. The finite-window theorem and the sharpness theorem are logically different contributions
The recognition theorem concerns a q-blind predicate on Q_k. The sharpness theorem concerns the minimal depth required for **all affine crossed-cocycle representations**. This is a legitimate and potentially useful new theorem, but the admissible category must be stated exactly.

Do not call n(k)=p^{k-1}+1 “the minimal finite window” without the qualifier:
“minimal depth for factorization of all affine crossed-cocycle representations into S_k=A_k⋊U_{1,k}” (and with the corrected rank hypothesis).

**Classification: PASS/CONDITIONAL after scope correction.**

### 5. The Newton algorithm is not q-blind
The Newton section is a coordinate algorithm for the explicit Fox equations F_i, and those equations contain q=p^f. Therefore it is not an algorithm that reconstructs orientation from the bare finite quotient without q/presentation data.

This is not a contradiction, but the paper must label it correctly as an explicit computational realization of the known-coordinate selector, not as part of the intrinsic q-blind recognition theorem.

**Classification: PASS/LOCAL, after wording correction.**

### 6. q-collapse needs a sharper statement
The calculation that f >= k implies Q_k^{(f)} is isomorphic to Q_k^{(infty)} is structurally useful. It should be stated together with the equally important fact that chi_{G_f} mod p^k is also trivial for f >= k. Thus the collapse is compatible with the target orientation residue.

For f < k, the abelianization distinguishes the standard family by the factor Z/p^f. This is a classification-family statement, not a general intrinsic reconstruction theorem for arbitrary Demushkin groups.

**Classification: PASS/LOCAL.**

### 7. Bibliography/novelty boundary is missing from the uploaded manuscript
The source has no bibliography or citations. This is fatal for submission of a research paper whose main formula explicitly invokes Labute's canonical orientation and whose Kummer criterion is known in the literature.

At minimum the follow-up paper must discuss:
- Labute (1967), including the canonical orientation and standard presentation;
- Efrat–Quadrelli / Quadrelli–Weigel Kummerian/1-cyclotomic criteria;
- Quadrelli (2024), Proposition 2.10 and why its quotient-inheritance hypotheses do not directly give the present theorem;
- the current main finite-window paper, if this is a genuine follow-up;
- relevant 2026 work of Blumer–Quadrelli and Pál–Quick, with a precise “what is and is not used” comparison.

Labute's classification and canonical orientation are established prior art, and Quadrelli (2024) explicitly states the finite-level Kummerian criterion and a quotient-inheritance proposition requiring restriction-surjectivity. citeturn0search2turn2search1

**Classification: OPEN / publication-critical.**

### 8. Title/abstract overstate the contribution unless narrowed
The title should not suggest discovery of canonical Demushkin orientations. A safer framing is around:
- finite-window Kummer recognition;
- sharp factorization depth for affine crossed-cocycle targets;
- q-collapse of the finite quotient.

The abstract should explicitly separate:
(i) intrinsic recognition theorem;
(ii) representation-theoretic sharpness;
(iii) q-collapse;
(iv) Newton computation.

## Current verdict

- Local LaTeX build: **PASS / CLOSED**
- Corrected cocycle formula: **PASS / CLOSED**
- Explicit orientation value (1-p^f)^(-1): **PASS / CLOSED**
- q-collapse calculation: **PASS / LOCAL**
- Newton calculation: **PASS / LOCAL / q-dependent**
- Main recognition theorem as a mathematical result: **PASS / CONDITIONAL** pending standalone proof/hypothesis expansion
- Sharp factorization depth theorem as currently quantified: **FAIL / CLOSED**
- Sharp factorization depth theorem after restricting/proving the d=2 case: **OPEN**
- Recognition minimality among arbitrary intrinsic carriers: **OPEN**
- Publication-level novelty: **OPEN / CONDITIONAL**
- Submission readiness of this uploaded draft: **NOT READY**

## Required repair order

1. Correct Theorem 3.1 quantifier: either d >= 4 or prove d=2 separately.
2. Give standalone definitions of all objects and the exact admissible representation category.
3. Expand U1/U2/U3/U5 into publication-grade lemmas/proofs or cite a completed companion theorem.
4. Separate intrinsic q-blind recognition from q-dependent Newton/Fox computation.
5. Add a literature section with exact theorem/proposition comparisons.
6. Add a complete bibliography and reproducibility appendix.
7. Re-run an independent algebraic audit specifically on the repaired d=2 boundary and on the Zassenhaus sharpness witness.
8. Only then decide whether this is best submitted as a separate follow-up paper or merged into the main manuscript.

This audit supersedes any informal claim that the uploaded corrected draft is already submission-ready.
