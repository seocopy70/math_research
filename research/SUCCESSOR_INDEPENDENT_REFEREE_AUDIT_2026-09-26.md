# SUCCESSOR INDEPENDENT REFEREE AUDIT — 2026-09-26

## Scope

Independent referee-style audit of the publication-candidate manuscript `paper/successor_main.tex` on branch `successor-publication-candidate-2026-09-26`, commit `730b1bf815e0c30cd46d0803cf1b72482df970a8`. The audit is intentionally separated from the author-side build audit.

## Overall assessment

**Classification: CONDITIONAL / minor-to-moderate revision before submission.**

No fatal mathematical contradiction was found in the main affine finite-window theorem after the corrected sharpness witnesses are used. The central formula
[
n_{\mathrm{aff}}(k)=p^{k-1}+1
]
is mathematically coherent for the explicitly declared category of continuous affine crossed-cocycle representations into
(S_k=A_k\rtimes U_{1,k}), with odd (p), (f\ge1), even (d\ge2), (k\ge2).

The main remaining publication risks are not the core calculation but theorem-definition precision, exposition, novelty positioning, and a few statements that are correct in spirit but should be made more exact.

## 1. Load-bearing theorem audit

### 1.1 Finite affine filtration

The claimed formula
[
P_n(S_k)=p^{e(n)}A_k\rtimes U_{e(n)+1},qquad e(n)=\lceil\log_p n\rceil
]
is consistent with the lower central/power calculation for the affine semidirect product. The endpoint
(P_{p^{k-1}+1}(S_k)=1) follows.

**Classification: PASS / LOCAL.**

Referee request: expand the proof by one sentence clarifying that the product formula is the pro-(p) Zassenhaus/Jennings formula and that the displayed power subgroups generate the stated semidirect product. This is routine but currently compressed.

### 1.2 Universal factorization

The implication
[
P_{p^{k-1}+1}(S_k)=1
Longrightarrow
P_{p^{k-1}+1}(G)\subseteq\ker\psi
]
is immediate from functoriality of the Zassenhaus filtration.

**Classification: PASS / CLOSED.**

The phrase “associated twisted (H^1) lifting problem factors” is acceptable, but should explicitly say that inflation along the quotient identifies cocycles and coboundaries because the coefficient action itself factors through the same quotient.

### 1.3 Sharpness

The two witness regimes are correct in the stated category:

* (f<k): canonical orientation with (z(x_1)=1), giving
  (z(x_1^{p^{k-1}})=p^{k-1}\ne0pmod{p^k}).
* (f\ge k): (ho(x_2)=1+p), (z(x_2)=1), giving the geometric sum of valuation (k-1).

The second witness does not require surjectivity of the orientation component, and works already in rank two. This is exactly the repaired boundary and supersedes the earlier erroneous d=2/f>1 concern.

**Classification: PASS / CLOSED.**

Important referee wording point: the paper should define the admissible depth formally before stating (n_{\mathrm{aff}}(k)). At present the notation is introduced by assertion rather than definition.

Recommended formal definition:
[
n_{\mathrm{aff}}(k;G):=
min\{n:\text{every continuous }\psi:G\to S_k
\text{ kills }P_n(G)\},
]
or the equivalent largest surviving depth convention, with the indexing convention stated explicitly.

### 1.4 Category-relative minimality

The lower-bound argument establishes minimality only for the full category of all continuous crossed-cocycle representations into the fixed (S_k). It does not establish minimality for arbitrary intrinsic carriers.

The manuscript already says this, which is essential.

**Classification: PASS / CLOSED.**

## 2. q-collapse audit

The finite-depth collapse for (f\ge k) is sound at the level claimed: the power relation lies beyond the retained Zassenhaus window, while the canonical orientation has the same reduction modulo (p^k).

For (f<k), the statement that the (p^f)-torsion relation remains visible in the abelianized quotient is reasonable, but “retains” should be replaced by an explicit lemma or a short argument identifying the image/order of (x_1) in the relevant finite quotient.

**Classification: PASS / LOCAL.**

The paper must not suggest that the full groups for different (f) are isomorphic; the current limitations section correctly avoids this.

## 3. Factorization versus recognition

This conceptual separation is one of the strongest aspects of the manuscript and is correctly maintained.

The free-pro-(p) example is valid for showing that the Kummer lifting predicate is not a universal uniqueness selector on arbitrary input classes. Since free pro-(p) groups have cohomological dimension one, the finite-level lifting map is surjective for every orientation.

However, the manuscript must keep the exact logical target explicit: it rules out uniqueness of this predicate on that class, not all possible natural selectors on all possible quotient categories.

**Classification: PASS / CLOSED after wording qualification.**

The current remark already supplies the necessary limitation.

## 4. Free-product section

The truncation/coproduct lemma is mathematically natural:
(T_n(G)=G/P_n(G)) is the reflector onto pro-(p) groups satisfying (P_n=1), so it preserves finite coproducts.

The resulting uniform factorization theorem for finite free pro-(p) products of Demushkin blocks is therefore credible and correctly restricted.

**Classification: PASS / CLOSED.**

The lower-bound sentence should be made slightly more formal: embed the chosen factor through the coproduct and compose its sharp witness with the canonical inclusion. This avoids making the universal-property inheritance sound hand-wavy.

The manuscript correctly avoids extending the theorem to the broader elementary-type class.

## 5. Terminology / statement precision

### 5.1 Theorem 1 wording defect

The sentence currently has the grammatical form

“every (psi) ... be continuous, with ...”

It should read “for every continuous (psi=(z,ho):...), with ...”.

This is not mathematical, but it is visible in a theorem statement and should be corrected.

### 5.2 Define (n_{\mathrm{aff}}(k))

This is the clearest mathematical exposition defect. The quantity is central enough that its definition cannot be left implicit.

**Required before submission.**

### 5.3 “Kummerian at every finite coefficient level”

Prefer “the finite-level Kummer lifting map is surjective for every (k)” or state that this is equivalent to Kummerianity in the free pro-(p), cd=1 setting. This avoids conflating a finite-level predicate with the standard all-level Kummerian definition.

### 5.4 “Recognition” in the title

The manuscript proves a factorization theorem and a negative separation result; it does not present a new positive orientation-recognition theorem. The title is defensible because recognition is explicitly treated as the second question, but a referee may regard “Recognition” as slightly stronger than the main positive theorem.

This is not a mandatory title change, but the introduction should state immediately that the paper's principal theorem is a factorization theorem, while the recognition component is a boundary result.

## 6. Novelty / prior-art audit

The literature boundary is currently defensible but should remain deliberately modest.

Established prior art includes:
- Labute's canonical Demushkin orientation and its uniqueness;
- Efrat–Quadrelli's Kummerian framework;
- Quadrelli–Weigel's oriented elementary-type/Kummerian results;
- Efrat's Zassenhaus-filtration/representation framework;
- Mináč–Rogelstad–Tân's Zassenhaus information for Demushkin groups and free pro-(p) products.

The targeted search did not locate the exact theorem
“all affine crossed-cocycle maps into (A_k\rtimes U_{1,k}) factor through (P_{p^{k-1}+1}), with equality sharp”
stated in this precise category and with these witnesses.

That supports a **conditional novelty claim**, not a priority claim.

The manuscript's current wording is appropriately cautious. Do not strengthen it to “first”, “new”, or “previously unknown” without broader literature verification.

Relevant literature checks:
Efrat 2014 explicitly concerns Zassenhaus filtrations and representations; Mináč–Rogelstad–Tân 2016 covers Demushkin groups and their free pro-(p) products; Quadrelli 2024 treats Kummerian/1-cyclotomic structure and free/amalgamated constructions. citeturn3search0turn1academia44turn2search3

## 7. Hidden referee attack: is the main theorem too tautological?

This is the most important conceptual question.

The upper bound is formally forced once one computes the Zassenhaus depth at which the fixed target (S_k) becomes trivial. Thus the novelty is not the categorical factorization principle itself; it is the **exact target-filtration calculation plus sharpness for the Demushkin family**.

The manuscript should say this explicitly. Otherwise a referee may reasonably respond that “factorization through the quotient” is an immediate consequence of standard functoriality.

The paper survives this objection because the sharp lower bound is nontrivial and uniform in (f,d), including rank two. But the contribution should be framed as:

> an exact and sharp representation-theoretic window theorem for the affine target, rather than a new general principle of Zassenhaus factorization.

## 8. Hidden referee attack: dependence on the standard presentation

The main upper-bound theorem is presentation-free because it applies to arbitrary pro-(p) (G).

The lower-bound witness is presentation-dependent by necessity, but the theorem only needs existence of a witness for the specified standard Demushkin family. This is legitimate.

The paper should distinguish these two levels explicitly:
- upper bound: intrinsic and functorial;
- sharpness: verified on the standard presentation of (G_{f,d}).

**Classification: PASS / CLOSED.**

## 9. Hidden referee attack: continuity

The publication candidate now says “continuous” consistently in the key statements. This is correct and necessary for pro-(p) cohomology and filtration functoriality.

The proof should use “continuous homomorphism” consistently rather than switching between abstract and profinite language.

## 10. Publication readiness

### Must fix
1. Define (n_{\mathrm{aff}}(k)) formally.
2. Correct the malformed Theorem 1 sentence.
3. Add one or two sentences making the exact novelty mechanism explicit: target filtration calculation + sharp Demushkin witnesses.
4. Tighten the q-collapse (f<k) statement with a short abelianization lemma/argument.
5. Clarify the finite-level Kummer terminology.

### Strongly recommended
6. Expand the affine-filtration proof slightly.
7. Make the free-product lower-bound inheritance explicit.
8. State at the beginning that no positive recognition theorem is claimed here.
9. Keep the novelty language conditional.

### Not required
- reopening the closed Fox/t2 routes;
- broader elementary-type generalization;
- absolute carrier minimality;
- additional computational experiments before submission.

## Final referee classification

**MATHEMATICAL CORE: PASS / CLOSED.**

**CATEGORY-RELATIVE SHARPNESS: PASS / CLOSED.**

**FREE-PRODUCT EXTENSION: PASS / CLOSED for finite free products of Demushkin blocks.**

**q-COLLAPSE / INFORMATION-LOSS BOUNDARY: PASS / LOCAL.**

**ABSOLUTE MINIMALITY: OPEN / CATEGORY-DEPENDENT — correctly not claimed.**

**NOVELTY: OPEN / CONDITIONAL — defensible, but not a proven priority claim.**

**PUBLICATION READINESS: CONDITIONAL — suitable for submission after the small precision/exposition repairs above.**

No new mathematical obstruction comparable to the earlier sharpness error was found in the current publication-candidate manuscript.
