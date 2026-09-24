# PAPER STRUCTURE BASELINE — Finite-Window Kummer Recognition

Date: 2026-09-24

## 0. Purpose and status

This document is the authoritative planning baseline for turning the closed U1–U5 research gates into a publication-style manuscript. It is a paper-construction document, not a research log and not a claim that publication-level novelty has been finally established.

Core mathematical result currently supported by the project:
\[
\boxed{\mathsf K_k(G/P_{k+1},\rho)\iff \rho=\chi_G\bmod 3^k,\qquad k\ge2}
\]
for the rank-4, q=3 Demuškin group under study, with the finite predicate defined intrinsically on the quotient.

Important epistemic distinction:
- Mathematical theorem: PASS / CLOSED.
- Existing global Kummerian characterization and canonical orientation: KNOWN.
- Exact publication-level novelty of the finite-window formulation: OPEN / STRONG CANDIDATE.
- The prior 2026-09-24 record saying “PASS / CONDITIONAL” for literature novelty is superseded by this more cautious assessment because the literature review was not a complete line-by-line audit of every potentially equivalent result.

## 1. Proposed title

**Finite-Window Kummer Recognition of the Canonical Orientation of Demuškin Groups**

The title describes the finite-window recognition result, not a claim that canonical orientation itself is new.

## 2. Central question

Classically, a torsion-free Demuškin group G has a canonical orientation chi_G characterized by Kummerian/cyclotomic lifting. The paper asks the narrower finite-information question:

Can the reduction chi_G mod 3^k be recognized using only
\[
Q_k=G/P_{k+1},
\]
via the intrinsic predicate
\[
\mathsf K_k(Q_k,\rho):
H^1(Q_k,\mathbf Z/3^k(\rho))
\longrightarrow H^1(Q_k,\mathbf F_3)
\quad\text{is surjective}?
\]

The selector input must not contain a presentation coordinate, q, the dualizing action, or a pre-supplied canonical orientation.

## 3. Main logical architecture

Information boundary (motivation / lower bound)
  -> graded data alone do not determine chi mod 9
  -> a single t_2 carrier does not determine chi
  -> motivates a function-valued lifting obstruction and a filtered finite quotient

Finite-window proof (main contribution)
  -> U1: compute P_j(A_k semidirect U_1), obtaining P_{k+1}=1
  -> U2: every twisted crossed cocycle factors through Q_k
  -> U3: finite Kummer lifting is equivalent to vanishing of the twisted Fox row
  -> U4: standard presentation identifies the canonical branch
  -> U5: coefficient-extension variation + PD^2 injectivity removes presentation dependence
  -> Main theorem: K_k(Q_k,rho) iff rho=chi_G mod 3^k

## 4. Recommended manuscript structure

### 1. Introduction
1.1 Demuškin orientations and known Kummerian characterization.
1.2 The finite-window recognition question.
1.3 Information boundary: graded no-go and single-carrier no-go, statements only.
1.4 Main theorem and precise contribution.
1.5 Relation to prior work and novelty boundary.

The Introduction should explicitly say that existence/uniqueness of the canonical orientation is classical. Avoid “what is not known” unless the literature audit supports that wording. Prefer “we investigate” / “we prove the following finite-window formulation.”

### 2. Finite coefficient extensions and the finite window
- Define A_k=Z/3^k, U_1=1+3Z/3^k, S_k=A_k semidirect U_1.
- Proposition: with U_j=1+3^jZ/3^k and T_j=3^{j-1}A_k semidirect U_j,
  P_j(S_k)=T_j and P_{k+1}(S_k)=1.
- Corollary: for every candidate rho:G->U_1 and z in Z^1(G,A_k(rho)), the associated homomorphism (z,rho):G->S_k kills P_{k+1}(G).
- Hence Z^1 and H^1 factor through Q_k.

Interpretation: the theorem does not say all information about G is contained in Q_k; it says the relevant twisted H^1 lifting obstruction factors through Q_k.

### 3. The finite Kummer criterion
- Define the intrinsic predicate K_k(Q_k,rho).
- In the standard one-relator setting, define the twisted Fox obstruction F_i(rho).
- Prove K_k(rho) iff F_i(rho)=0 for all i.
- Use the corrected iterative/Nakayama argument, not the superseded shorthand I subset 3I proof.

Presentation is allowed here as a proof device. The final recognition statement must remain intrinsic.

### 4. Identification in the standard presentation
- For r=x_1^3[x_1,x_2][x_3,x_4], calculate the coefficient forced by the Kummer condition.
- Obtain rho(x_2)=(1-q)^(-1), and for q=3:
  (1-3)^(-1)=1+3+3^2+... mod 3^k.
- Treat (1,40,1,1) mod 81 as the k=4 example, not as the general formula.
- State U4 as presentation-dependent/local identification, not as the intrinsic theorem.

### 5. Intrinsic uniqueness via PD^2
This is the load-bearing conceptual section.
- Lemma 5.1 (variation formula):
  delta_{rho'}-delta_rho=iota_{k-1} o (nu cup -).
- Lemma 5.2 (PD^2 injectivity): the socle inclusion F_3 -> A_{k-1}(chi) induces an injection on H^2, proved by PD^2 duality.
- Theorem 5.3: if two level-k candidates satisfy the Kummer lifting condition, then they coincide.
- Use cup-product nondegeneracy H^1 x H^1 -> H^2 to force nu=0.

Do not reuse the earlier incorrect “H^0 equals the socle” argument for general q.

### 6. Main finite-window recognition theorem
For the rank-4 q=3 Demuškin group:
\[
\mathsf K_k(Q_k,\rho)\iff\rho=\chi_G\bmod3^k,\quad k\ge2.
\]
Proof assembly:
(i) U1-U2 factorization;
(ii) known Kummerian existence of chi_G;
(iii) U3 finite Kummer criterion;
(iv) U4 standard identification;
(v) U5 intrinsic uniqueness.

Clarify that q is not an input to the predicate; “q-blind” means the selector itself does not take q as an input, not that the theorem has been proved uniformly for all q.

### 7. Relation to previous work and novelty boundary
Separate:
- KNOWN: canonical Demuškin orientation and global Kummerian/cyclotomic characterization.
- KNOWN: Kummerian criteria and quotient-inheritance results in the literature.
- PRESENT RESULT: exact finite-window selector on Q_k with arbitrary candidate rho and automatic factorization for arbitrary twisted cocycles.
- OPEN: whether an existing source contains an equivalent theorem/corollary in precisely this input category and depth.

Do not claim “no one has proved this” until a source-level audit establishes it.

### 8. Information boundary (brief)
Mention the earlier negative results only as motivation:
- gr(G) does not determine chi mod 9.
- A single t_2 carrier does not determine chi.
- The successful object is a function-valued lifting obstruction on the finite filtered quotient.
Do not reproduce the full no-go computations in the main paper. Those belong in a separate companion note if the minimal-carrier problem is completed.

## 5. Appendix policy

Do NOT paste research/U1.md–U5.md verbatim into the manuscript. Those are research records.

Instead create publication-style appendices:
A. Semidirect-product filtration calculation.
B. Twisted Fox/coefficient calculation.
C. PD^2 and coefficient-extension details.
D. Computational verification, if retained.

The research/U*.md files remain the audit trail and source history.

## 6. Claims that must be worded carefully

1. “q-blind” = q is absent from selector input.
2. “presentation-free” = final predicate/theorem is defined without choosing a presentation; intermediate verification may use the standard presentation.
3. “Q_k suffices” = the relevant twisted H^1/Kummer obstruction factors through Q_k; not that Q_k determines all structure of G.
4. “finite-window” = recognition modulo 3^k from G/P_{k+1}.
5. “canonical orientation is unique” is classical, not the novelty claim.
6. “novel” / “not known” remains conditional until the literature audit is sufficiently exhaustive.

## 7. Current gate table

| Component | Status |
|---|---|
| U1 semidirect finite-depth lemma | PASS / CLOSED |
| U2 H^1 factorization | PASS / CLOSED |
| U3 finite Fox–Kummer equivalence | PASS / CLOSED |
| U4 standard presentation identification | PASS / LOCAL |
| U5 intrinsic PD^2 uniqueness | PASS / CLOSED |
| Main finite-window theorem | PASS / CLOSED |
| Global canonical orientation | KNOWN |
| Exact literature novelty of finite-window formulation | OPEN / STRONG CANDIDATE |
| New broad mathematical attacks | CLOSED unless direct prior-equivalence evidence appears |

## 8. Immediate manuscript tasks

Before drafting full prose:
1. Fix theorem hypotheses and notation, especially k>=2 and the exact target U_1.
2. Write publication versions of U1-U5, removing research-log language.
3. Verify every citation against the actual source text before making priority/novelty claims.
4. Check whether P_{k+1} is genuinely the exact depth needed, rather than merely a sufficient depth.
5. State precisely which parts use the standard presentation and where presentation independence is recovered.
6. Only after these checks, build paper/main.tex.

## 9. Companion-note boundary

The earlier information-boundary project can become a separate paper:
**Information Boundaries for Intrinsic Reconstruction of Demuškin Orientations**.

Potential contents:
- graded no-go;
- bounded-information no-go;
- single t_2 failure;
- first extension datum;
- minimal-carrier question.

That companion paper should not be assumed complete while minimality remains open.


## 2026-09-24 — CRITICAL N1–N5 REVIEW: MANUSCRIPT CORRECTIONS

The following corrections are controlling for the manuscript.

### Novelty boundary

The paper must distinguish four layers:

1. **Classical prior art:** Kummerian cohomological lifting, finite-level generator lifting, and unique canonical Demuškin orientation.
2. **Project mathematics:** arbitrary-candidate factorization of twisted H^1 through Q_k=G/P_{k+1}, proved by the finite semidirect-product filtration.
3. **Project recognition theorem:** for the fixed rank-4 q=3 group, the intrinsic finite predicate on Q_k has unique solution chi mod 3^k.
4. **Publication novelty:** survives against the checked corpus, but remains conditional until peer-review-level exclusion of equivalent formulations.

Do not say that the project discovered the canonical orientation, or that finite-level lifting on G is new.

### Exact theorem scope

The manuscript theorem is currently for the fixed rank-4, q=3 Demuškin group. The phrase “q-blind” means that q is absent from the selector input. It does not mean the theorem has been proved uniformly for all Demuškin q.

### Depth wording

Q_k=G/P_{k+1} is a sufficient finite window established by the proof. Minimality is not established. Replace any phrase such as “minimal finite window” by “the finite window Q_k” or “a sufficient finite window.”

### U5 presentation

U5 must be written as:
- coefficient-extension variation/Yoneda lemma;
- PD² duality proof of socle-map injectivity with exact dual modules;
- cup-product nondegeneracy;
- induction from the established k=2 base case.

The older H^0/socle shortcut is superseded and must not appear.

### Literature section

The related-work section must explicitly compare:
- Labute Prop. 6/Theorem 4;
- Efrat–Quadrelli Prop. 7.3/Theorem 7.6;
- Quadrelli–Weigel 2022 Prop. 2.6;
- the quotient-inheritance results;
- Quadrelli 2024 Prop. 2.10.

The key distinction is direction: existing results start from an already given Kummerian orientation; the present selector starts from an arbitrary finite candidate rho and proves factorization through a specified finite quotient.

### Current status table

| Item | Status |
|---|---|
| Mathematical finite-window theorem | PASS / CLOSED |
| Classical canonical orientation | KNOWN |
| Exact novelty against checked literature | PASS / CONDITIONAL |
| Absolute priority claim | NOT ESTABLISHED |
| Minimality of P_{k+1} | OPEN |
| Broad orientation-discovery claim | CLOSED / NON-NOVEL |

