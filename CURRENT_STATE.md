# CURRENT STATE — canonical live research state
Last reviewed: 2026-10-04

> This file is the only canonical live-state summary. Historical detail belongs in the research log or archive. If another document conflicts with this file, check the evidence index and dated log.

## 1. Current research frontier

### Paper 4 — finite-window visibility / non-rigidity
**Mathematical core: CLOSED within the certified scope.**

- For G_s(r)=F/<<z^(p^s)r^(-1)>>, every n<=p^s is s-blind:
  W_n(G_s(r)) is independent of s.
- If p is odd and r in D_2(F)\D_3(F), the critical window N=p^s+1 separates G_s(r) from G_t(r), t>s; the natural kernel has exact order p.
- The old unconditional claim “initial degree >=2 is enough” is FALSE / CLOSED. Degree alone is insufficient; the distinguished z-direction can cause cancellation.
- Stress family G_{s,a}=<z,x_1,...,x_d | z^(p^s)=x_1^(p^a)[x_1,x_2]...[x_{d-1},x_d]>, s>a, has s-independent abelianization, full mod-p cohomology algebra, and full Zassenhaus graded restricted Lie algebra under the declared odd-p, even-rank symplectic/mild scope, while the critical window separates the parameter in the certified theorem.
- Conceptual result: same H* + same gr_Z does not imply the same filtered finite window.

### Paper 4 — remaining boundary / intrinsic questions
- Exact stress-family same-window separation/recovery outside the certified scope: OPEN where not covered above.
- Marked quotient reconstruction from an abstract W_n: OPEN.
- Coarsest intrinsic realization/compression: OPEN as a separate structural program.
- Do not silently promote a local/base-case calculation to a general theorem.

### Paper 5
Paper 5 is a structural compression/realization program, downstream of Paper 4. The admissible realization groupoid and compression trichotomy/boundary are established in the declared class; a nontrivial further compression requires an independently specified preserved-information package. No universal minimality theorem is claimed.

## 2. Closed routes
- Paper 1–3 frozen mathematical cores.
- Rejected blind-carrier searches and closed scalar/norm shortcuts.
- Closed characteristic-kernel constructions and the rejected orbit-category minimality formulation.
- Historical RAAG/orientation branches unless a genuinely new theorem requires reopening.
- Superseded results remain in the log/archive with their correction chain.

## 3. Status vocabulary
- CLOSED = settled for stated scope.
- OPEN = unresolved.
- FAILED = proposed claim/route is false or tested construction failed.
- HISTORICAL = retained for provenance only.

Evidence quality is separate in research/02_EVIDENCE_INDEX.md: PASS, LOCAL, NONE.

## 4. Where to look
1. This file — what is true/live now.
2. research/02_EVIDENCE_INDEX.md — claim-to-evidence map.
3. RESEARCH_MAP.md — dependency map.
4. research/00_RESEARCH_LOG.md — chronological history and corrections.
5. research/archive/ — preserved old state documents and audits.
6. research/03_CONVENTIONS_AND_IMPLEMENTATION.md — computational conventions.

Rule: never reconstruct current state by reading the entire research log.

## 2026-10-04 Paper 4 status correction
- **Mathematical core:** CLOSED only for the explicitly certified claims: universal (n\le p^s) delayed-window blindness; quadratic critical-layer survival in the declared scope; stress-family coarse-package non-rigidity in the declared mild/odd-(p) scope; and own-critical-window ((s,a)) recovery for (1\le a<s).
- **OPEN / LOAD-BEARING:** same numerical-window separation (W_{p^s+1}(G_s)\) vs. (W_{p^s+1}(G_t)); the (a=s) boundary; and any exact relative threshold statement requiring a non-splitting argument beyond survival.
- **Scope rule:** survival is not non-splitting; own-critical recovery is not same-window (s\) vs. (t) separation; relative results do not become unmarked results by omission of the quotient map.
- **Publication status:** Paper 4 is not yet FINAL. The next work is evidence-level packaging and resolution of the load-bearing OPEN questions, followed by manuscript freeze.

## 2026-10-04 Paper 4 boundary attack completion
- **CLOSED:** direct same-window separation for the stress family \(G_{s,a}\), \(1\le a<s<t\): at \(n=p^s+1\), there is a canonical epimorphism \(W_n(G_{s,a})\twoheadrightarrow W_n(G_{t,a})\) with kernel of exact order \(p\). Hence the two windows are non-isomorphic.
- **CLOSED:** combining lower-window blindness with the direct order jump gives the exact unmarked stress-family threshold \(n_{\mathrm{sep}}(s)=p^s+1\) within the certified scope.
- **CLOSED:** the boundary \(a=s\) versus \(a=\infty\) for \((p,s)=(3,1)\), via the \(A_3\)-formality obstruction factoring through \(W_4\).
- **OPEN / LOAD-BEARING:** \(W_{p^s+1}(G_{s,s})\stackrel{?}{\cong}W_{p^s+1}(G_{s,\infty})\) for \(s\ge2\). Ordinary \(gr_Z\), mod-\(p\) cohomology, naive \(p^s\)-power tests, and scalar coinvariant defects have been closed as non-load-bearing routes.
- The earlier relative-extension/non-splitting formulation is no longer load-bearing for the exact unmarked threshold; direct same-window order separation suffices.
- Full dated audit: `research/PAPER4_FINAL_BOUNDARY_ATTACK_2026-10-04.md`.

## 2026-10-04 Research governance correction
- Previous audit-era restrictions were too rigid when treated as permanent research rules: phrases such as “next authorized attack is singular,” “stop if...,” or blanket no-reopening instructions are now **historical guidance**, not standing prohibitions.
- **No artificial deadline:** OPEN mathematical questions have no time limit unless explicitly chosen for project management.
- **LOAD-BEARING means priority, not exclusive permission.** Exploratory side attacks, literature checks, counterexamples, and alternative formulations remain allowed when plausibly informative.
- CLOSED/FAILED routes should not be repeated mechanically, but may be reopened when a new invariant, changed hypothesis, new literature, new computation, or other material change alters the premises. Such reopening must cite the earlier closure and state what changed.
- Discovery and certification are separated: exploratory work may remain LOCAL/provisional; only certified results change the authoritative CLOSED/PASS state.
- Full policy: `research/RESEARCH_GOVERNANCE.md`.


## 2026-10-04 — Paper 4 a=s boundary: transfer-defect reduction
- New candidate: for the intrinsic radical kernel K and canonical short torsion line T=W^{ab}[p^s], the transfer defect p^{s-1}V(T) in K^{ab} is an unmarked, functorial candidate for separating a=s from a=infinity.
- Reduction: in the a=s case the candidate reduces to the critical norm/Jacobson term p^{s-1}(p-N_sigma)[x_1]; the (sigma-1)^{p-1} component occurs at degree p^s.
- OPEN / LOAD-BEARING: nonvanishing of this transfer defect in the actual K^{ab} for a=s. The a=infinity side is locally zero after passing to K^{ab}, but the full invariant proof requires the same intrinsic normalization.
- This is a genuine new filtered-extension candidate, not a repeat of the closed scalar/coinvariant or ordinary graded routes.
- Audit: research/PAPER4_A_S_TRANSFER_DEFECT_ATTACK_2026-10-04.md.



## 2026-10-04 — CRITICAL CORRECTION: the proposed intrinsic w_a-line argument uses a superseded W10 module

A proposed continuation argued from
M=K^{ab}/3K^{ab} \cong F_3^5, M \simeq J_3(1)\oplus J_1(1)\oplus J_1(1),
with delta^2 M=<w_a>, and concluded that w_a defines an intrinsic/functorial line.

This is not compatible with the corrected intrinsic-radical W10 calculation already certified locally in research/PAPER4_A_S_TRANSFER_SCHREIER_W10_AUDIT_2026-10-04.md. For G_{2,2}=<z,x,y | z^9=x^9[x,y]> the intrinsic cup-radical character is chi=z^*, so K=ker chi. The corrected Schreier calculation gives M=K^{ab}/3K^{ab} \cong F_3^7, with one trivial u-line and two 3-cycles, on the a_i- and b_i-triples. Consequently
im(sigma-1)^2 = <a_0+a_1+a_2, b_0+b_1+b_2>,
so dim_{F_3} delta^2 M=2, not 1.

Therefore the following claims are rejected/superseded for the corrected W10 base case:
- M \cong J_3\oplus J_1\oplus J_1;
- delta^2M=<w_a>;
- w_a is intrinsically determined as the unique nonzero line delta^2M;
- “canonical generator of a 1-dimensional delta^2M” and the resulting functorial w_a-line.

The individual line <a_0+a_1+a_2> is not selected by the module structure alone, because the a- and b-cycle summands are both present. Any attempt to distinguish the a-line therefore needs additional intrinsic structure (for example the defining symplectic/relator data) and must pass the gauge/functoriality tests. The transfer witness 3(a_0+a_1+a_2) != 0 in K^{ab} remains PASS / LOCAL as an explicit base-case witness, but it is not thereby an unmarked intrinsic line invariant.

Classification:
- corrected W10 module M \cong F_3^7: PASS / LOCAL;
- dim delta^2M=2: PASS / LOCAL;
- unique intrinsic w_a-line: FAIL / CLOSED for the corrected W10 module;
- base-case transfer/Jacobson nonvanishing: PASS / LOCAL;
- all-s intrinsic transfer-defect separation: OPEN / LOAD-BEARING.

This correction controls over the earlier 5-dimensional/J_3\oplus J_1\oplus J_1 argument.


## 2026-10-04 — intrinsic χ=z* Schreier SNF discrepancy RESOLVED

Direct recomputation resolves the claimed (p,s)=(3,2) discrepancy. For χ(z)=1, χ(x)=χ(y)=0, the p-index kernel has generators u=z^p, a_i=z^i x z^{-i}, b_i=z^i y z^{-i}. In K^{ab}, the p conjugate relators give exactly p^{s-1}U-p^sA_i=0. Thus the relation matrix on (U,A_0,...,A_{p-1}) is [p^{s-1} | -p^s I_p], whose Smith factors are p^{s-1}, followed by p^s repeated p-1 times. Hence K^{ab} ≅ Z^{p+1} ⊕ Z/p^{s-1} ⊕ (Z/p^s)^{p-1}. In particular, (p,s)=(3,2) gives Z^4 ⊕ Z/3 ⊕ (Z/9)^2. This agrees with the already recorded SNF diag(3,9,9) in the corrected W10 audit. Therefore the alternative Z^4 ⊕ Z/3 ⊕ Z/9 is superseded; the supposed missing-Z/9 discrepancy is FAIL/CLOSED as a mathematical issue. The all-s transfer-defect separation remains OPEN/LOAD-BEARING.

## 2026-10-04 — intrinsic transfer-defect boundary CLOSED

The load-bearing identification is exact. In the a=s boundary, the canonical torsion-line generator is τ_s=zx_1^{-1}; the relevant transfer is V(τ_s), not V(a_0). Up to a unit from the choice of torsion generator,
\[
p^{s-1}V(τ_s)=p^{s-1}(p-N_σ)[A_0].
\]
With δ=σ−1,
\[
N_σ=p+\binom p2δ+\cdots+\binom p{p-1}δ^{p-2}+δ^{p-1}.
\]
For 1≤k≤p−2, p divides \(\binom pk\), while δ^k[A_0] is p^s-torsion; hence all intermediate terms vanish after multiplication by p^{s−1}. Thus
\[
p^{s-1}V(τ_s)=-p^{s-1}δ^{p-1}[A_0].
\]
The exact Schreier/SNF computation gives ord(δ^{p−1}[A_0])=p^s, so the defect is nonzero of order p. For a=∞, τ_∞=z and z^{p^s}∈[K,K], so the normalized transfer class vanishes in K^{ab}. Therefore the intrinsic transfer-defect predicate separates a=s from a=∞ in the declared stress-family scope s≥2.

Classification: PASS/LOCAL for the boundary separator; H^3 secondary lift remains UNPROVEN and is not asserted. Do not identify V(τ_s) with V(a_0).
