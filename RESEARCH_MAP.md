# RESEARCH MAP — compact canonical map
Last reviewed: 2026-10-04

> This is a map, not a diary. It records dependency structure and evidence locations. Historical detail stays in research/00_RESEARCH_LOG.md and research/archive/.

## 1. Research chain
Paper 1 -> Paper 2 -> Paper 3 -> Paper 4 -> Paper 5

- Paper 1: finite Kummer-selector recognition in the declared rank-4 pro-3 Demushkin setting.
- Paper 2: affine successor/selector threshold results and corrected cyclotomic data.
- Paper 3: finite-window recognition, selector minimality, and 1D cup carrier. FROZEN/COMPLETE.
- Paper 4: delayed visibility of z^(p^s)=r, exact critical separation for quadratic initial relations, and stress-family non-rigidity. Core is CLOSED in the certified scope; the all-s a=s vs. a=∞ boundary remains OPEN/LOAD-BEARING.
- Paper 5: intrinsic realization/compression question built on Paper 4. Structural boundary established; further nontrivial compression remains a separate OPEN problem.

## 2. Paper 4 dependency
n<=p^s -> s-blind lower window.
r in D_2\D_3 -> W_(p^s+1)(G_s) not isomorphic to W_(p^s+1)(G_t), t>s.
Stress family -> same abelianization/H*/gr_Z across s in declared scope, while critical filtered windows retain information.
ord_Z(r)>=2 alone -> insufficient for an unconditional general theorem.

## 3. Paper 5 dependency
W_n -> admissible realization groupoid -> compression order -> trichotomy/boundary.

Established:
- target class intrinsic in declared class;
- realization groupoid is the gauge-invariant relative object;
- literal canonical marked-map reconstruction is not available in tested class;
- absolute coarsest/minimality is not meaningful until a preserved-information package is declared.

## 4. Source-of-truth table
| Question | Canonical home |
| What is current? | CURRENT_STATE.md |
| How does the programme fit together? | RESEARCH_MAP.md |
| What proves a claim? | research/02_EVIDENCE_INDEX.md |
| What happened and when? | research/00_RESEARCH_LOG.md |
| Why did a route fail/change? | dated audit in archive + log |
| What are calculation conventions? | research/03_CONVENTIONS_AND_IMPLEMENTATION.md |
| What is old AI/session context? | research/archive/ |
| What is only a plan? | plans/ |

One concept, one live home. Cross-link; do not duplicate.

## 2026-10-04 correction — critical same-window boundary

The previous claim that W_(p^s+1)(G_s) and W_(p^s+1)(G_t) are separated by an order jump is superseded. The normal closures defining the two quotients are not nested, so the proposed canonical epimorphism and p-factor order jump are false. The exact threshold n_sep(s)=p^s+1 is OPEN. Only n_sep(s)>=p^s+1 is certified. Group-level non-isomorphism G_{s,a} \\not\\cong G_{t,a} is also OPEN.


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
