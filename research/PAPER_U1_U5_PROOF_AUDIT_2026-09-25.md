# PAPER U1-U5 PROOF AUDIT — 2026-09-25

## Scope

This audit checks the actual manuscript `paper/main.tex` against the controlling research artifacts and the current U1-U5 proof records. It is a proof audit, not a literature novelty audit.

Controlling sources checked:
- `RESEARCH_MAP.md`
- `CURRENT_STATE.md`
- `research/00_RESEARCH_LOG.md`
- `research/RESEARCH_CONTINUITY_PROTOCOL.md`
- `research/U1_UNIFORM_SEMIDIRECT_FINITE_DEPTH_LEMMA_2026-09-24.md`
- `research/U5_INTRINSIC_UNIQUENESS_INDUCTION_2026-09-24.md`
- `research/U5_INTRINSIC_FINITE_SELECTOR_AUDIT_2026-09-24.md`
- `paper/PAPER_STRUCTURE_BASELINE.md`
- `paper/MANUSCRIPT_STATUS_2026-09-25.md`
- `paper/main.tex`

## Executive verdict

The mathematical spine is coherent, but the manuscript is **not yet proof-complete**. The research project has closed the U1-U5 gates, while the paper still compresses several load-bearing arguments into assertions.

Current manuscript proof classification:
- U1: **PASS / LOCAL — manuscript underproved; research proof is CLOSED**
- U2: **PASS / LOCAL — logically correct but the H^1 identification should be stated as a lemma**
- U3: **OPEN / LOAD-BEARING — proof omitted in manuscript**
- U4: **PASS / LOCAL — base-level coordinate calculation is asserted, not shown**
- U5: **OPEN / LOAD-BEARING — variation and PD^2 lemmas are asserted, not proved**
- Assembly: **OPEN / LOAD-BEARING until U3 and U5 are written out**
- Overall manuscript proof audit: **OPEN / WORKING**

No closed research branch is reopened.

## U1 — finite semidirect-product filtration

### Claim in manuscript
For S_k=A_k semidirect U_1,
P_j(S_k)=3^{j-1}A_k semidirect U_j and P_{k+1}(S_k)=1.

### Research support
The dedicated U1 audit proves this by:
1. cube calculation;
2. U_j^3=U_{j+1};
3. commutator containment;
4. commutator generation of all 3^j A_k;
5. induction.

### Manuscript gap
The manuscript states the result but gives no proof. Because this lemma is the entire reason the arbitrary-candidate twisted cocycle problem factors through Q_k, it is load-bearing and cannot remain an unproved displayed assertion.

### Required repair
Add a compact lemma proving both inclusions in the induction. In particular, explicitly state the semidirect multiplication convention and the crossed-cocycle homomorphism convention.

### Classification
**PASS / LOCAL in manuscript; PASS / CLOSED in research.**

## U2 — arbitrary-candidate factorization

### Claim in manuscript
For z in Z^1(G,A_k(rho)), psi(g)=(z(g),rho(g)) is a homomorphism to S_k, hence P_{k+1}(G) is killed and H^1(Q_k,A_k(rho-bar)) is canonically isomorphic to H^1(G,A_k(rho)).

### Audit
The construction is correct provided:
- the semidirect product uses (a,u)(b,v)=(a+u b,uv);
- z is a left crossed cocycle for the same action;
- rho factors through Q_k, which follows because psi kills P_{k+1}.

Coboundaries also factor because a coboundary has the same semidirect-product form with trivial cocycle on the quotient kernel.

### Manuscript gap
The canonical H^1 isomorphism is stated without explicitly defining the quotient action or proving injectivity/surjectivity of inflation.

### Required repair
State U2 as a separate proposition: inflation is an isomorphism on Z^1 and B^1 because both cocycles and coboundaries factor through Q_k.

### Classification
**PASS / LOCAL.**

## U3 — finite Kummer/Fox criterion

### Claim in manuscript
For a one-relator pro-3 group, H^1 lifting is equivalent to vanishing of the twisted Fox row.

### Critical issue
The manuscript currently says this for a generic one-relator pro-3 group. The equivalence in the form “every prescribed mod-3 generator-value vector lifts” requires the presentation to be minimal (equivalently r in Phi(F)), so that H^1(G,F_3) is represented by arbitrary generator-value vectors.

This hypothesis is automatic for the fixed Demushkin group but is not automatic for an arbitrary one-relator pro-3 group.

### Second gap
The sentence “The proof is a finite Nakayama iteration” is not enough. The controlling research record explicitly superseded the old informal I subset 3I argument and requires the corrected valuation/matrix iteration.

### Required repair
Restrict the proposition to a minimal one-relator pro-3 presentation, or formulate it directly in terms of H^1(G,F_3) rather than arbitrary generator-value vectors.

Then prove:
1. twisted Fox evaluation gives the obstruction functional;
2. basis-vector lifts imply each row coefficient lies in 3A_k;
3. the resulting vector relation F=-3FA can be iterated to force F=0;
4. conversely F=0 gives lifts of every mod-3 class.

Also define the left/right Fox derivative and action convention once.

### Classification
**OPEN / LOAD-BEARING.**

## U4 — standard-presentation identification

### Claim in manuscript
For r=x_1^3[x_1,x_2][x_3,x_4], the standard calculation gives rho(x_1)=rho(x_3)=rho(x_4)=1 and rho(x_2)=(1-3)^{-1} mod 3^k.

### Audit
This is consistent with the controlling research record, but the manuscript currently gives no calculation. More importantly, U4 is only classified as PASS/LOCAL in the research record because it is presentation-dependent.

### Scope problem
The theorem only needs a base case k=2. The manuscript currently presents the all-k coordinate formula as if it were part of the proof of the intrinsic theorem.

### Required repair
Use U4 only for the base case:
- compute the mod-9 candidate explicitly;
- show the unique candidate is (1,4,1,1);
- state that this is a standard-presentation/local verification.

If the all-k formula is retained, give its derivation and explicitly mark it as auxiliary/local, not intrinsic.

### Classification
**PASS / LOCAL.**

## U5 — intrinsic uniqueness

### Claim in manuscript
For two candidates differing by rho'_k=rho_k(1+3^{k-1}nu),
delta_{rho'_k}-delta_{rho_k}=iota_{k-1}(nu cup -), and iota_{k-1} is injective on H^2 by PD^2 duality.

### Critical issue 1 — variation lemma is asserted
The manuscript calls this a “Yoneda variation formula” but supplies no actual proof. This identity is the central intrinsic step and must be shown either:
- by a short Yoneda-extension argument with the coefficient-extension classes, or
- by an explicit cochain calculation with sections, including why changing the section changes the result only by a coboundary.

### Critical issue 2 — exact coefficient maps
The manuscript writes the extension
0 -> A_{k-1}(rho_{k-1}) -> A_k(rho_k) -> F_3 -> 0
but says only “injection 3”. The map and the induced G-actions should be written explicitly.

For the variation identity, the target inclusion is the socle map
F_3 -> A_{k-1}(chi_{k-1}), 1 -> 3^{k-2}. These are different maps and must not be conflated.

### Critical issue 3 — PD^2 convention
The sentence “PD^2 duality makes H^2(G,F_3) -> H^2(G,A_{k-1}(chi)) injective: its dual is the surjective reduction map on H^0” is correct in substance, but the paper must specify the duality convention and dualizing module.

A safe formulation is:
H^2(G,M)^vee ~= Hom_G(M,D),
where D is the discrete dualizing module, and on the canonical branch D is Q_3/Z_3 with G-action through chi. Then identify the two Hom_G groups and verify that precomposition with the socle inclusion is reduction modulo 3.

### Critical issue 4 — induction reduction
The manuscript says “reduce a candidate successively to level 2” but does not prove that K_k implies K_{k-1}. This follows from the coefficient-extension sequence or, more simply, from the mod-3 lifting formulation together with reduction of a level-k lift. It should be a named lemma.

### Critical issue 5 — existence
The manuscript imports existence from classical Kummerianity. This is legitimate, but it must explicitly say:
- the canonical orientation at level k is a full-group Kummerian orientation;
- U1-U2 factor its relevant H^1 problem through Q_k;
- therefore its reduction satisfies the finite predicate on Q_k.

### Classification
**OPEN / LOAD-BEARING in manuscript; PASS / CLOSED in research.**

## Theorem assembly

The intended logical chain is:

U1 -> U2 -> finite predicate is well-defined on Q_k
U3 -> coordinate realization of the predicate
U4 -> unique base candidate at k=2
U5 -> uniqueness of each higher lift
classical Kummerianity -> existence at every level
therefore finite-window recognition.

This chain is valid in principle. The current manuscript, however, skips the proofs of U1, U3 and the two decisive U5 lemmas. Therefore the manuscript theorem should not yet be labeled submission-ready.

## Not proof defects

The following are not defects and should remain as-is:
- canonical orientation is explicitly treated as classical prior art;
- q-blindness is defined as absence of q from the selector input, not q-uniformity;
- P_{k+1} is claimed sufficient, not minimal;
- the fixed rank-four q=3 scope is explicit;
- Proposition 2.10 is used only for prior-art separation, not as a proof of the theorem.

## Required next manuscript pass

1. Expand U1 proof.
2. Replace generic U3 wording by a minimal one-relator statement and give the corrected iterative proof.
3. Replace all-k U4 assertion by a fully explicit k=2 base calculation, unless the all-k coordinate lemma is deliberately retained as a local appendix.
4. Write U5 variation lemma in full.
5. Write PD^2 socle-injectivity with exact dual modules and maps.
6. Add the reduction lemma K_k -> K_{k-1}.
7. Add a short existence-on-Q_k lemma.
8. Then run an independent line-by-line audit again before any novelty wording is finalized.

## Final classification

**PAPER U1-U5 PROOF AUDIT: OPEN / LOAD-BEARING.**

The underlying research theorem remains **PASS / CLOSED**. The manuscript has not yet earned that status because several proofs are still compressed into assertions.
