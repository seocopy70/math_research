# Paper 4 — literature audit: weighted-Schreier / transfer / finite-window novelty — 2026-10-05

## Verdict

**SC is not a safe standalone novelty claim.** The uploaded Ershov–Jaikin-Zapirain source directly contains the machinery needed to derive it for the Paper-4 free pro-p / index-p setting.

The downstream result remains substantially less threatened: this audit found no source matching the specific Paper-4 combination of the intrinsic torsion-line obstruction `epsilon_s`, the stress family (z^{p^s}=x_1^{p^a}r_2^{-1}), the unmarked separation (a=s) versus (a=\infty), and the exact finite-window threshold (p^s+1).

This is **not a proof of novelty**. It is a bounded negative literature search, and the downstream claims remain **CONDITIONAL / OPEN for publication novelty**.

## 1. Primary prior source

Ershov–Jaikin-Zapirain, *Groups of positive weighted deficiency and their applications*, J. Reine Angew. Math. 677 (2013), 71–134, DOI 10.1515/crelle.2012.013.

The arXiv record confirms the paper's subject and publication identity. The published/source text contains the weighted free-pro-(p) machinery used below.

Relevant chain:

- uniform weight / standard Zassenhaus degree;
- restriction of a weight function;
- explicit index-(p) Schreier generating set;
- W-optimality of that generating set in the free case;
- power-commutator characterization/no-cancellation.

The published text also contains Lemma 3.10 with the index-(p) Schreier generators and its proof via the free restricted Lie algebra. This independently confirms that the mechanism is not an artifact of the uploaded TeX version.

## 2. Independent corroboration of the underlying Zassenhaus/Magnus framework

The later literature continues to treat the Zassenhaus filtration as the standard augmentation/Magnus filtration of free pro-(p) groups. Mináč–Rogelstad–Nguyễn compute graded dimensions for free pro-(p), Demuškin, and related groups and explicitly use the Magnus isomorphism.

Efrat's 2023 JIMJ paper / 2024 NYJM paper develops further word-combinatorial and Magnus methods for the (p)-Zassenhaus filtration and (H^2). This confirms that Magnus/word methods are established infrastructure, not by themselves evidence of novelty.

## 3. Search for the exact Paper-4 downstream construction

Searches targeted:

- finite-window / Zassenhaus + transfer;
- (p^s)-torsion in abelianized index-(p) kernels;
- (D_{p^s+1}) transfer behavior;
- the stress relation (z^{p^s}=x_1^{p^a}r_2^{-1});
- exact threshold (p^s+1);
- intrinsic/unmarked finite-window transfer defects.

No retrieved source matched the complete construction.

The literature does contain important adjacent transfer/cohomological results. In particular, Efrat's work on the Zassenhaus filtration and representations, and later work on Magnus formations, studies finite quotients, cohomology, unitriangular representations, and transfer principles. These are relevant background and must be cited/positioned, but the retrieved material does not state the Paper-4 `epsilon_s) invariant or the exact (a=s) versus (a=\infty) separation at (p^s+1).

## 4. Important literature threat that must be acknowledged

Efrat's transfer/intersection framework is a real neighboring theory. His work explains that cohomological transfer principles can recover several intersection theorems for Zassenhaus-type filtrations and connects finite quotients with cohomology and representations.

Therefore the manuscript must **not** claim that Paper 4 is the first work to connect transfer, finite quotients, Magnus methods, or Zassenhaus filtration.

The defensible claim is narrower:

> the Paper-4 contribution is the specific intrinsic finite-window obstruction and the resulting sharp separation theorem for the declared stress family, if the full literature audit remains negative.

## 5. Novelty classification

| Object | Current classification |
|---|---|
| SC (D_n(F)\cap K\subseteq D_{\lceil n/p\rceil}(K)) | **PASS/CLOSED mathematically; not standalone novelty** |
| Magnus prefix-code proof of SC | **PASS/CLOSED; self-contained reproof/bridge** |
| TF_s | **PASS/CLOSED mathematically; novelty downstream** |
| intrinsic (epsilon_s) | **OPEN — strongest novelty candidate** |
| unmarked (a=s) vs (a=\infty) separation | **OPEN — strong theorem-level novelty candidate** |
| exact threshold (p^s+1) | **OPEN — strong sharpness/application candidate** |
| overall Paper-4 publication novelty | **CONDITIONAL / OPEN** |

## 6. Required next literature audit

The next search should be narrower rather than broader:

1. Search Efrat/Mináč/Matzri/Quadrelli literature for **transfer maps on (H^1) or (K^{ab})** attached to index-(p) kernels at a prescribed Zassenhaus depth.
2. Search for **Bockstein + cup-product / relation-class combinations** producing a one-dimensional (p^s)-torsion line.
3. Search for **finite quotient separation by transfer**, especially where lower windows are provably identical and only a critical window separates two presentations.
4. Search citations to Ershov–Jaikin-Zapirain and to the relevant Zassenhaus intersection/transfer papers for any later use of the exact inequality or an equivalent finite-window form.
5. Only after these searches remain negative should the manuscript use language such as “apparently new” or “to the best of our knowledge”.

## 7. Bottom line

The literature audit strengthens, rather than weakens, the current Paper-4 strategy:

**remove SC from the novelty headline; retain it as the established filtration-comparison input; concentrate the novelty claim on the intrinsic transfer obstruction and the sharp finite-window separation.**

No mathematical Paper-4 result is reopened by this audit.
