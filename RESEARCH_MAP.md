# RESEARCH MAP — compact canonical map
Last reviewed: 2026-10-06

> This is a map, not a diary. It records dependency structure and evidence locations. Historical detail stays in research/00_RESEARCH_LOG.md and research/archive/.

## 1. Research chain
Paper 1 -> Paper 2 -> Paper 3 -> Paper 4 -> Paper 5

- Paper 1: finite Kummer-selector recognition in the declared rank-4 pro-3 Demushkin setting.
- Paper 2: affine successor/selector threshold results and corrected cyclotomic data.
- Paper 3: finite-window recognition, selector minimality, and 1D cup carrier. FROZEN/COMPLETE.
- Paper 4: delayed visibility of z^(p^s)=r, exact critical separation for quadratic initial relations, and stress-family non-rigidity. The certified stress-family boundary is now CLOSED at n=p^s+1 by the Magnus prefix-code transfer proof; broader arbitrary-r degree-only claims remain CLOSED/FAIL.
- Paper 5: concrete finite-group automorphism structure of Zassenhaus windows. The active target is the Frattini/GL image and its intrinsic relation-jet factorization; the former compression/realization-groupoid programme is HISTORICAL/SUPERSEDED as the main line.

## 2. Paper 4 dependency
n<=p^s -> s-blind lower window.
r in D_2\D_3 -> marked critical-layer visibility at n=p^s+1 in the certified scope; unmarked same-window separation remains OPEN.
Stress family -> same abelianization/H*/gr_Z across s in declared scope, while critical filtered windows retain information.
ord_Z(r)>=2 alone -> insufficient for an unconditional general theorem.

## 3. Paper 5 dependency
Aut(W_n) -> GL(W_n/Phi(W_n)), with IA(W_n) as kernel -> intrinsic relation-jet factorization target.

Established / corrected:
- p=3,n=4 actual IA order is constant 3^27 across the audited split/non-split cases;
- the observed p^2 order gap is localized to the Frattini/GL image in the audited p=3 and p=5 cases;
- the corrected n=p theorem is PASS/CLOSED/GENERAL with D_p(W_p) ≅ F_p^3, IA ≅ F_p^9, Im=S'_11(p), and |Aut(W_p)|=p^11(p-1)^2;
- W_{p+1}=W_p gives the same boundary theorem at n=p+1;
- Run 37381098677 is PASS/LOCAL confirmation only.

Current load-bearing boundary:
- arbitrary-n uniform control of the U_n-action in the B,theta equations is OPEN;
- the submitted arbitrary-n B,theta proof is FAIL/CLOSED;
- no uniform arbitrary-n Frattini-image or p^2 automorphism-order theorem is promoted.

## 4. Source-of-truth table
| Question | Canonical home |
| What is current? | CURRENT_STATE.md |
| How does the programme fit together? | RESEARCH_MAP.md |
| What proves a claim? | research/02_EVIDENCE_INDEX.md |
| What happened and when? | research/00_RESEARCH_LOG.md |
| Why did a route fail/change? | dated audit in archive + log |
| What are calculation conventions? | research/03_CONVENTIONS_AND_IMPLEMENTATION.md |
| Where are explanation/learning/evaluation records collected? | research/90_RESEARCH_GUIDE/README.md |
| What is old AI/session context? | research/archive/ |
| What is only a plan? | plans/ |

One concept, one live home. Cross-link; do not duplicate.

## 2026-10-04 correction — critical same-window boundary

The previous claim that W_(p^s+1)(G_s) and W_(p^s+1)(G_t) are separated by an order jump is superseded. The normal closures defining the two quotients are not nested, so the proposed canonical epimorphism and p-factor order jump are false. The exact critical boundary threshold n_sep(s)=p^s+1 was OPEN at this 2026-10-04 checkpoint; this statement is now HISTORICAL/SUPERSEDED by the 2026-10-05 Magnus proof closure below. Group-level non-isomorphism G_{s,a} \\not\\cong G_{t,a} is also OPEN.


## 2026-10-04 — active post-core generalization challenge

Paper 4 remains PASS/CLOSED in its certified core, while a bounded generalization challenge is now the active research branch. The branch tests whether the critical relative-window mechanism survives from the Demushkin control relation to a broader nonzero quadratic initial relation r_2 in
G_{s,a}(r_2)=<z,x_1,...,x_d | z^{p^s}=x_1^{p^a}r_2>, s>a>=2.

This does not reopen the failed arbitrary-r degree-only theorem or the universal E_psi construction. The latter remains a future branch pending an intrinsic E_psi/functoriality pre-check. First task: Object/Input/Functoriality/Gauge/Orientation bridge/q-blindness/Separation/Novelty/Stop pre-check, followed by the smallest genuinely non-control quadratic test.


## 2026-10-04 — universal E_psi exploratory branch reopened

The project deliberately opens a high-risk generalization branch: seek an intrinsic twisted-character test object E_psi for broad relations r and test whether the critical p^s+1 mechanism extends beyond the Demushkin/quadratic control families. This is an exploratory Paper 5/generalization branch, not a revision of the certified Paper 4 core.

Governance distinction: the continuity protocol blocks silent scope drift and invalid theorem promotion; it does not block deliberate high-risk exploration. The universal branch must therefore be explicitly labeled OPEN/ACTIVE and must pass the same Object/Input/Functoriality/Gauge/Orientation bridge/q-blindness/Separation/Novelty checks. The bounded quadratic family remains the benchmark/control family, while arbitrary-r degree-only remains FAIL/CLOSED.


## 2026-10-04 — E_psi marked quadratic closure

The active E_psi branch has crossed its first theorem gate. For every nonzero quadratic initial relation r in D_2\D_3, the affine test object E_s admits a marked critical lift with v_p(delta(r))=s; the proof explicitly controls the D_3-tail, including its p-power contribution. Thus the marked critical-window threshold p^s+1 is PASS/CLOSED for the quadratic class.

This does not change the global boundary: abstract unmarked same-window separation remains OPEN because the orientation/character bridge from an abstract finite window to the affine package is not intrinsic yet. The old arbitrary-degree degree-only theorem remains FAIL/CLOSED.

Active dependency is now:
marked quadratic E_psi theorem -> intrinsic orientation bridge -> abstract finite-window separation.


## 2026-10-04 — E_psi orientation bridge: symmetry boundary

The marked quadratic E_psi theorem is now closed, but the first proposed unmarked bridge is also closed negatively. In the rank-two control relation r=[x_1,x_2], the automorphism group acts transitively on the nonzero order-p character directions used by the affine separator. Hence no individual character psi can be intrinsically selected from the abstract window.

The surviving structural target is an **orbit-valued affine defect/groupoid**, not a distinguished orientation character. The abstract same-window separation question remains OPEN until such an orbit-level invariant is constructed or ruled out.


## 2026-10-04 — E_psi carrier refinement

The orientation-bridge no-go for a distinguished character is now refined. The abstract critical window has a canonical character carrier
\[
\mathcal A(W)=\operatorname{Ann}_{H^1(W,\mathbf F_p)}(\operatorname{Tor}(W^{ab})),
\]
and the marked quadratic affine separator can be chosen inside it. Thus the correct intrinsic bridge is not a single orientation character.

The remaining target is the orbit-invariant extension defect on this carrier. The carrier alone is redundant as a separator; it supplies the intrinsic domain on which the defect functional should live.


## 2026-10-04 — correction: E_psi carrier proposal closed

The previously proposed torsion-annihilator carrier
\(\operatorname{Ann}_{H^1(W,\mathbf F_p)}(\operatorname{Tor}(W^{ab}))\)
is **FAIL/CLOSED**: for a finite p-group window, W^{ab} is entirely torsion, so the annihilator is zero.

Therefore no intrinsic nonzero character carrier has yet been established. The active E_psi boundary is:
marked quadratic theorem PASS/CLOSED -> single-character bridge FAIL/CLOSED -> intrinsic carrier OPEN -> orbit-invariant extension defect OPEN.


## 2026-10-04 — E_psi Sp-orbit claim rejected

The proposed Sp-orbit closure of the unmarked orientation bridge is **FAIL/CLOSED as stated**. Nonzero quadratic initial form does not imply nondegeneracy; rank-4 r_2=[x_1,x_2] is an explicit degenerate counterexample. The exponent parameter s is also unrelated to quadratic-form rank. Even in the nondegenerate symplectic subcase, transitivity only removes representative choice and does not provide an intrinsic defect separating s,t, while recovery of B from the abstract finite window remains unproved.

Therefore abstract same-window separation remains **OPEN**. The correct next gate is an intrinsic filtration/extension/groupoid object of the abstract window, tested first on the degenerate rank-4 example.


## 2026-10-04 — Direction 2 closed: ordinary cohomology blindness

Direction 2 is now **PASS / CLOSED** at theorem level for the declared odd-p stress family. For every s>=1, finite a>=1, and a=infinity, the defining power terms lie in the third p-Zassenhaus term, so the quadratic commutator initial form is unchanged. Quadrelli, arXiv:2011.03233v3, Proposition 2.1 gives the full ordinary mod-p cohomology algebra: it is quadratic, H^k=0 for k>=3, and the H^1 cup product is determined entirely by the common commutator form. Thus ordinary H^bullet(-,F_p) is completely blind to s and a, including the a=s versus a=infinity boundary. This closes only the ordinary-cohomology route; group/window separation and higher filtered operations remain separate questions.


## 2026-10-04 — strategic shift after Direction 2 closure

Ordinary mod-p cohomology is now **PASS / CLOSED as a blind invariant** for the declared stress family and is no longer an active research route. The next structural layer is the **filtered extension/lift package** of the Zassenhaus tower.

The active candidate is the intrinsic one-step filtered lift
\[
1\to D_n/D_{n+1}\to W_{n+1}\to W_n\to1,
\]
with its kernel, filtration position, p-power/commutator lifting data, and gauge-equivalence retained. The target is not merely the associated ordinary H^2-class: the full filtered lift package is the object to test.

The immediate gate is:
Object -> Input -> Functoriality -> Gauge -> Orientation bridge -> q-blindness -> Separation -> Novelty -> Stop.

The research question is whether this filtered extension/lift layer detects the hidden p^s-power relation that ordinary H^\bullet(-,\mathbf F_p) provably misses. No further ordinary-cohomology calculation is authorized unless a later structural result explicitly shows that it is needed to identify an extension/lift obstruction.


## 2026-10-04 — filtered-extension extraction boundary

The post-cohomology filtered-extension branch has been structurally audited. The one-step Zassenhaus extension is the correct intrinsic next layer, but an unmarked p-power/commutator defect does not survive section/lift gauge as a canonical scalar or orientation carrier. After gauge quotient, the full extension-equivalence class is simply the structured finite-window extension-isomorphism problem itself. Therefore the branch is **FAIL / CLOSED as an extraction/compression method**; the exact critical finite-window classification remains a separate **OPEN** boundary. No new candidate hunt is authorized to replace this result.


## 2026-10-04 — Paper 5 architecture correction

Paper 5 is no longer centered on abstract compression. The active program is concrete finite-group automorphism theory of W_n:

Aut(W_n) -> GL(W_n/Phi(W_n)), with IA(W_n) as kernel,
and, for admissible realizations, Aut(W_n) -> Aut(Q_n), together with radical/shear subgroups and kernel orbits.

The former compression/trichotomy work remains historical boundary material: it showed why minimality/compression is category-dependent or tautological without a declared preserved-information package. It is not the main Paper 5 contribution.

Current candidate contribution: identify the structural source of the observed p^2 automorphism-order gap between split and non-split windows. User-reported computations show the same p^2 gap at p=3,n=4 and p=5,n=6. This is PASS / LOCAL only until the IA/GL decomposition is independently reproduced.

Next gate: p=3,n=4 IA kernel and GL-image decomposition; then fixed-quotient Aut(W)->Aut(Q) image/kernel; then cross-prime p=5,n=6 replication. Orientation-recovery dichotomy is deferred until this concrete theorem is obtained.


## 2026-10-05 — Paper 5 relation-jet boundary refined

The two-level relation-jet stabilizer mechanism is now split cleanly into two layers: the abstract projective stabilizer formulas for odd p are PASS / CLOSED, while realization of the actual finite-window Frattini image as that stabilizer remains OPEN / LOAD-BEARING. The p=3 and p=5 computations are local equality certificates, not the general theorem. The p^2 gap therefore has a closed abstract linear-stabilizer explanation candidate, but no p-uniform automorphism-order theorem yet.


## 2026-10-05 — Paper 5 Step 3 equality correction

The Step 2 filtered/J-adic gate is now CLOSED/GENERAL in the Paper 5 current record. The proposed Step 3 lower-bound construction was then audited. The congruence \(\tilde g_{a,b}(\rho)\equiv\rho^a\pmod{RD_{p+1}}\) is useful, but the asserted pro-p induction from \(\tilde g(R)\subseteq RD_{p+1}\) to \(\tilde g(R)\subseteq R\) is not proved. Hence the actual Frattini-image equality \(\operatorname{Im}=S_{11}(p)\) remains OPEN/LOAD-BEARING. The \(p^2(p-1)\) automorphism-order formula remains CONDITIONAL. Detailed audit: `research/PAPER5_STEP3_EQUALITY_AUDIT_2026-10-05.md`.


## 2026-10-05 — GATE P5-JET correction

The previous general abstract relation-jet closure is superseded at the proof level. The existing GAP S11 candidate is hard-coded rather than derived from the restricted-power transformation. An independent p=3 calculation gives 48 for the naive additive Lambda^2V plus V^(1) model, but 6 after retaining the degree-3 Jacobson terms modulo the ideal generated by [x,y]. Hence the observed S11=6 survives locally, while the general odd-p derivation is OPEN / LOAD-BEARING. See `research/PAPER5_JET_S11_JACOBSON_CORRECTION_AUDIT_2026-10-05.md`.


## 2026-10-05 — Paper 4 all-s transfer boundary closed

The new Magnus prefix-code audit proves the index-p subgroup comparison
\[
D_n(F)\cap K\subseteq D_{\lceil n/p\rceil}(K)
\]
for free F and index-p kernel K. Therefore (SC_s) and the abelianized transfer bound (TF_s) are PASS / CLOSED. The corrected intrinsic transfer invariant, defined using the canonical line im(W^{ab}[p^s] -> W^{ab}/pW^{ab}) and evaluated in K^{ab}/p^sK^{ab}, closes the a=s versus a=infinity boundary in the declared stress-family scope. Hence the exact critical-boundary threshold is now PASS / CLOSED: n_sep(s)=p^s+1.

Evidence: research/PAPER4_MAGNUS_PREFIX_CODE_AUDIT_2026-10-05.md. The old order-jump proof remains FAIL/CLOSED/SUPERSEDED and is not revived.


## 2026-10-05 — Paper 5 Step 2 audit correction

The Hall–Petrescu p-power sublemma for odd p passes: for u∈D_2, (xu)^p≡x^p mod D_{p+1}. But this controls only the p-power component. Under x'=xu, y'=yv, the commutator [x,y] changes by D_3, and there is no canonical projection D_3→D_p/D_{p+1}. Therefore the proposed θ:J_2→D_p/D_{p+1} is not yet shown well-defined. Step 2 remains **OPEN / LOAD-BEARING**; no equality or uniform p^2(p−1) theorem is promoted.


## 2026-10-05 — Step 2 D_3-ambiguity correction

The proposed final split “p=3 PASS / p≥5 FAIL” is **not established**. Two errors were found: (i) D_3 is not equal to γ_3 for p≥5; it contains p-power factors such as G^p and γ_2^p, and (ii) for u=[r,s]∈γ_2 the leading correction [[r,s],y] is in γ_3, not γ_4. Hence the proposed negative witness is invalid. The p=3 claim also needs a direct Zassenhaus calculation of [x,D_2] and [D_2,y] modulo D_4. Current status: **OPEN / LOAD-BEARING**. Next gate is the exact lift-change map D_2×D_2→D_3/D_{p+1} and its interaction with the relation constraint.


## 2026-10-05 — Step 3 second-order closure superseded

The proposed second-order lifting/BCH closure is **FAIL / CLOSED as submitted proof**. The equality of degree-(k) initial forms gives only a residual in (D_{k+1}); the asserted (D_{k+2}) upgrade used an undefined (in_{k+1}) for elements still in (D_k\setminus D_{k+1}) and an unjustified exponential/BCH splitting. Hence the strengthened (L_m), kernel preservation, and general (\operatorname{Im}=S_{11}(p)) equality remain **OPEN / LOAD-BEARING**. The (p^2(p-1)) theorem remains **CONDITIONAL**.

Authoritative audit: `research/PAPER5_STEP3_SECOND_ORDER_LIFTING_AUDIT_2026-10-05.md`.


## 2026-10-06 — Paper 5 Step 3 corrected second-jet closure

The substitution-order correction is closed in the declared mod-(p) Magnus layer: (C_{a,b,k}=T_{a,b,k}\circ L), with the degree-2 witness giving (ab) rather than (b) on (XYX). Raw derivation/ideal preservation plus the explicit (p)-power exceptional-layer calculation give (C(gr_kR)\subseteq gr_{k+1}R). The finite-stage residual factorization then yields (widetilde g(R)\subseteq R) without any strong Zassenhaus-layer product equality. This closes the corrected Step-3 kernel-preservation subgate, but the global equality (operatorname{Im}(Aut(W_n)\to GL(V))=S_{11}(p)) remains OPEN / LOAD-BEARING.

## 2026-10-06 — S11 equality re-audit: proposed upper bound rejected

The proposed proof of
\[
\operatorname{Im}(\operatorname{Aut}(W_n)\to GL(V))\subseteq S_{11}(p)
\]
does **not** close the load-bearing gate.

The decisive defect is the passage from an arbitrary
\[
g\in\operatorname{Aut}(W_n),\qquad W_n=F/RD_{n+1},
\]
to statements in the full quotient (F/R), such as “(z) is central in (F/R)” and
\[
[g(x),g(y)]=[x,y]^{\det_{xy}},\qquad
[g(x),g(z)]=[g(y),g(z)]=1
]
as identities in (F/R). An automorphism of the finite window (W_n) does not automatically lift to an automorphism of (F/R); that is precisely part of the unresolved finite-window identification/lifting problem. Thus these (F/R)-identities cannot be used as an upper-bound argument without an independent lifting theorem.

A second independent gap is the assertion that (m_{z,x}=0) is a “representative choice.” The coefficient (m_{z,x}) is part of the actual linear map on
\[
V=F/D_2,
\]
and the relation (p(e_x-e_z)=0) in the abelianized relation subgroup does not permit changing an arbitrary (\mathbf F_p)-coefficient in (V) by a representative choice. No prior result currently establishes (m_{z,x}=0).

Therefore the proposed upper bound
\[
\operatorname{Im}\subseteq S_{11}(p)
\]
is **OPEN / LOAD-BEARING**, and consequently the equality
\[
\operatorname{Im}(\operatorname{Aut}(W_n)\to GL(V))=S_{11}(p)
\]
and the (p^2(p-1)) theorem remain **OPEN / CONDITIONAL**, respectively.

The lower-bound construction is different: the already-closed kernel-preservation result
\[
\widetilde g_{a,b}(R)\subseteq R
\]
does give genuine induced automorphisms of (F/R) and (W_n), with matrices
\[
M_{a,b}=\begin{pmatrix}a&b&0\\0&1&0\\0&0&a\end{pmatrix},
\qquad a\in\mathbf F_p^\times, b\in\mathbf F_p.
\]
Hence
\[
S_{11}(p)\subseteq\operatorname{Im}(\operatorname{Aut}(W_n)\to GL(V))
\]
is **CLOSED / GENERAL**, assuming the already-closed (\widetilde g(R)\subseteq R) gate. Equality is not established.

This supersedes the immediately preceding 2026-10-06 claim that the (S_{11}(p)) upper bound and equality were CLOSED/GENERAL.


## 2026-10-06 — Paper 5 stabilization boundary corrected

The previous open all-\(n\) stabilization boundary is now closed negatively. For
\[
R=\langle[x,z],[y,z],[x,y]^{-1}x^pz^{-p}\rangle^F,
\]
the explicit map \(\phi:F\to\mathbf Z_p\), \(x,z\mapsto t\), \(y\mapsto1\), gives
\[
x^{p^2}\in RD_{p+1}\setminus RD_{p^2+1},
\]
hence
\[
RD_{p^2+1}\subsetneq RD_{p+1}.
\]
Therefore \(W_{p^2}\to W_p=W_{p+1}\) is a strict canonical epimorphism, and the claim \(W_n=W_p\) for all \(n\ge p\) is **FAIL / CLOSED**. The term “strict shrinkage” refers to the defining denominator, not to a quotient inclusion.

The restricted-\(p\)-power obstruction and the rejected Lie-induction route remain closed historical boundaries. The active Paper 5 load-bearing questions now concern the intrinsic automorphism/Frattini-image structure for general \(n\), not an all-\(n\) stabilization theorem.


## 2026-10-06 — Paper 5 stabilization route superseded by persistence/global-image route

The explicit (p^k) denominator chain is strictly descending, and the audited unipotent (b:xmapsto xy) satisfies
[
bin G_psetminus G_{p^2}.
]
Therefore the former stabilization target (G_n=G_p) is **FAIL / CLOSED** and is no longer an active theorem route.

The new active conceptual target is the persistence spectrum of finite-window automorphism images:
[
H_n=operatorname{Aut}(W_n),qquad
P_n=operatorname{Im}(H_n	o GL(H^1(W_n,mathbf F_p))),
]
with the stable image identified, under the cofinal inverse-limit hypotheses, with
[
G_infty=operatorname{Im}(operatorname{Aut}(G)	o GL(H^1(G,mathbf F_p))).
]
The inverse-limit/Mittag-Leffler identification is **PASS / CLOSED** as an auxiliary lemma.

A critical model distinction is now authoritative: the corrected central-boundary (W_p) theorem with
[
|S'_{11}(p)|=p^2(p-1)^2
]
is not to be silently identified with the audited ((s,a)) family gates. The ((s,a)=(1,1)) values (6) for (p=3) and (20) for (p=5) arise from a different recorded presentation/model unless an explicit correspondence is proved. The model/index correspondence is **OPEN**.

The intrinsic cohomological candidate for the global ((1,1)) image is
[
omega=x^*wedge y^*,qquad
eta(lambda)=(lambda(x)-lambda(z))eta,
]
with (operatorname{rad}(omega)=langle zangle) and
[
|operatorname{Stab}(omega,eta)|=p(p-1).
]
The proposed theorem is an upper bound
[
operatorname{Im}(operatorname{Aut}(G)	o GL(H^1(G,mathbf F_p)))
subseteqoperatorname{Stab}(omega,eta),
]
not equality yet. This gate is **OPEN / LOAD-BEARING**.

Because (W_{p+1}=W_p), the first genuinely new window is (p+2). Future persistence tests must respect this indexing.

Next authorized gates: **P5-MODEL-1** (presentation/index correspondence table), then **P5-COH-1** (intrinsic stabilizer upper bound and independent calculation). No blind prime/window sweep.


## 2026-10-06 — Paper 5 persistence correction

The denominator strictness theorem and the automorphism-image chain are distinct. A direct Gate 0/1 certificate shows that the central model's b-unipotent is x -> x, y -> xy, z -> z and survives the tested p=3 windows n=4 and n=10, both with image order 36. The historical central-model G_{p^2} subsetneq G_p claim via b is therefore superseded.

For the actual G_{1,1} family, exact scans give p=3: 864 -> 6 -> 6 at n=3,4,5, and p=5: 48000 -> 20 at n=5,6. The active question is now whether the p(p-1) cohomological stabilizer is the uniform image for all n >= p+1, not whether the central model exhibits image shrinkage. See research/PAPER5_GATE0_GATE3_PERSISTENCE_AUDIT_2026-10-06.md.


## 2026-10-07 — Paper 5 P5-COH-1 closure and indexing correction

GAP n means G/D_n; free-presentation W_m=F/(RD_{m+1}) equals G/D_{m+1}. The relator r=z^p x^{-p}[x,y]^{-1} directly gives omega=x* wedge y* and beta(lambda)=(lambda(x)-lambda(z))eta for odd p, hence Im Aut(G) is contained in S_coh(p)={[[a,b,0],[0,1,0],[0,0,a]]}, order p(p-1): PASS/CLOSED/GENERAL. The remaining load-bearing gates are the intrinsic upper bound at W_p and diagonal realization; no further blind n-scan is needed once those close.