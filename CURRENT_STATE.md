

## 2026-09-27 — PAPER 3 MIDPOINT SUMMARY / CURRENT MASTER CONTEXT

Paper 3 is now at a major conceptual checkpoint.

**Original goal:** determine whether canonical Demushkin orientation \(\chi:G\to\mathbf Z_p^\times\), or \(\chi\bmod p^k\), can be recovered from a finite unmarked Zassenhaus window
\[
W_n(G)=(G/D_n;D_1/D_n,\ldots,D_{n-1}/D_n).
\]

**First correction:** no universal threshold such as \(r_{\chi\bmod p^k}=p^{k-1}+1\) is to be asserted. Recognition depth is target/category/filtration dependent:
\[
r_T(\mathcal C;D_\bullet).
\]
Status: universal formula **CLOSED**.

**Second correction:** the attempted same-target factorization/recognition separation was definitionally invalid. If \(f_T\) means the least \(n\) such that \(T\) factors through \(W_n\), and \(r_T\) means the least \(n\) such that \(W_n\) determines \(T\), they express the same information condition. Status:
- same-target \(f_T\neq r_T\): **INVALID / CLOSED — DEFINITIONAL IDENTITY**
- genuine separation: richer carrier \(O\) versus coarser target \(T=\Phi(O)\), comparing \(f_O\) with \(r_T\): **OPEN / LOAD-BEARING**.

**Bockstein target:** 
\[
T_\beta(G)=[\beta_G],\qquad \beta_G:H^1(G,\mathbf F_p)\to H^2(G,\mathbf F_p)
\]
from \(0\to\mathbf F_p\to\mathbf Z/p^2\to\mathbf F_p\to0\). Target convention is locked to the isomorphism class of the linear map, with independent source/target isomorphisms. In fixed-rank Demushkin, \(\dim H^2=1\), so rank determines this target; basis-dependent map is not claimed to be determined.

**Bockstein theorem:** the lower-bound pair
\[
G_p=\langle x,y\mid x^p[x,y]=1\rangle,\quad
G_{p^2}=\langle x,y\mid x^{p^2}[x,y]=1\rangle
\]
has isomorphic \(W_p\) but different \(T_\beta\). For the upper bound,
\[
D_{p+1}(G)\subseteq G^{p^2}[G,G],
\]
so \(W_{p+1}\) determines
\[
G/[G^{p^2}[G,G]]\cong G_{\rm ab}/p^2G_{\rm ab}.
\]
The Bockstein kernel is exactly the mod-\(p\) characters liftable to \(\mathbf Z/p^2\):
\[
\ker\beta_G=
\operatorname{im}\bigl[\operatorname{Hom}(G,\mathbf Z/p^2)\to\operatorname{Hom}(G,\mathbf F_p)\bigr].
\]
Thus \(W_{p+1}\) determines the Bockstein rank and, under the locked target convention, \([\beta]\). Combined with the lower bound:
\[
\boxed{f_{T_\beta}=r_{T_\beta}=p+1}.
\]
Status: **PASS / CLOSED**. This is a consistency theorem, not a separation result.

**Bockstein limitation:** \(T_\beta\) compresses \(q=p^2,p^3,\ldots\) into the rank-zero class and therefore is not by itself a carrier for full canonical orientation.

**Candidate B:** 
\[
\mathcal B_{27}=
(H^1(G,\mathbf F_3),H^1(G,\mathbf Z/9),\mathrm{red},\iota,\beta_1,\beta_9).
\]
Exact object/functoriality: **PASS / CLOSED**. On
\[
G_q=\langle x_1,x_2,x_3,x_4\mid x_1^q[x_1,x_2][x_3,x_4]\rangle,\quad q=3^s,
\]
the carrier detects the three valuation classes \(v_3(q)=1,2,\ge3\):
\[
v_3(q)=1:\beta_1\ne0;\quad
v_3(q)=2:\beta_1=0,\bar\beta_9\ne0;\quad
v_3(q)\ge3:\beta_1=0,\bar\beta_9=0,
\]
with \(\beta_9\circ\iota=\beta_1\). Therefore finite \(q\)-layer detection is **PASS / LOCAL**.

The line-by-line literature audit found strong prior art: Simons (1989) already uses Bockstein constructions for Demushkin tower level subgroups; Efrat–Quadrelli and later 1-cyclotomic/Kummerian work connect coefficient-lift structures to canonical orientation; generalized/higher Bockstein ideas are also established. Hence:
- new mod-27 orientation carrier: **FAIL / CLOSED**
- coefficient-extension/Bockstein novelty: **FAIL / CLOSED**
- no further trivial-coefficient \(\beta_1,\beta_9\) scan authorized.

**Other branches:** F1 Level A = **PASS / CLOSED**, retained but not load-bearing; F1 Level B/Massey sharpness = **OPEN / DEFERRED / NOT LOAD-BEARING**; fixed-rank Demushkin triple-Massey target = **FAIL / CLOSED** because constant; \(T_\cup\) = **FAIL / CLOSED — TRIVIAL TARGET**.

**Current architecture:**
\[
\boxed{W_n(G)\longrightarrow O(G)\overset{\Phi}{\longrightarrow}T(G)}
\]
where \(O\) is richer intrinsic carrier and \(T\) is a coarser target. The load-bearing question is now the carrier-vs-target separation, not same-target factorization vs recognition.

**Next decisive target:** the intrinsic \(P_4/D_{10}\) higher power/relation residual observed in HA58 to distinguish \(q=9\) from \(27\mid q\). The computation alone is not sufficient. Four gates are mandatory:
1. intrinsic definition independent of presentation coordinates;
2. transport/functoriality under the declared morphisms/isomorphisms;
3. intrinsic projective direction \([R_G]\);
4. canonical scalar normalization, or a proof that scalar ambiguity is intrinsic.
Scalar normalization is currently the sharpest attack point.

**New ultimate goal:** not merely “can a finite window recover orientation?” but
\[
\boxed{\text{When, how much, and in what form does finite intrinsic filtered data determine the canonical \(p\)-adic orientation?}}
\]
More concretely:
\[
\boxed{W_n(G)\to O(G)\to\chi_G\bmod p^k}
\]
and a quantitative theory of necessary and sufficient filtered relation information. Final guiding question:
\[
\boxed{\text{How much filtered relation information is necessary and sufficient to recover the canonical \(p\)-adic orientation?}}
\]

Paper 1–2 supply the finite-window, sharpness/obstruction, affine/Kummer, and explicit witness toolkit; Paper 3 is now the abstraction asking how the required information depth depends on the object being reconstructed.

**Current final state:** orientation reconstruction theorem not yet obtained, but the invalid definitions and nonproductive carriers have been substantially eliminated. The load-bearing problem is now sharply localized at intrinsic filtered relation residual \(\to\) canonical orientation, with the four tests above. Next authorized action: full intrinsic definition/transport/projective-direction/scalar-normalization audit of the \(P_4/D_{10}\) residual.


## 2026-09-27 — PAPER 3 T_beta FACTORIZATION AUDIT CRITICAL CORRECTION

The T_beta factorization audit was critically reviewed and the record was tightened. The mathematical threshold remains closed, but the earlier audit overstated closure in two places.

Locked target convention:
\[
T_\beta(G)=[\beta_G]
\]
means the **isomorphism class of the linear map** \(\beta_G:H^1(G,\mathbf F_p)\to H^2(G,\mathbf F_p)\), with independent linear isomorphisms on source and target. Only under this convention does rank determine the target in the fixed-rank Demushkin category (\(\dim H^2=1\)). The actual basis-dependent map is not determined by rank.

The lower-bound pair \(G_p,G_{p^2}\) is explicitly locked to the same Paper 3 category and the same unmarked Zassenhaus-window convention; no marked/presentation structure is used in the separation argument.

Corrected classification:
- target convention: **LOCKED / PASS**
- \(W_{p+1}\Rightarrow G_{\mathrm{ab}}/p^2G_{\mathrm{ab}}\): **PASS / CLOSED**
- \(G_{\mathrm{ab}}/p^2G_{\mathrm{ab}}\Rightarrow[\beta]\): **PASS / CLOSED under target convention**
- \(f_{T_\beta}\le p+1\): **PASS / CLOSED**
- S1/S2 lower-bound pair under Paper 3 conventions: **PASS / CLOSED**
- \(f_{T_\beta}>p\): **PASS / CLOSED**
- \(f_{T_\beta}=p+1\): **PASS / CLOSED**
- same-target T_beta separation: **FAIL / CLOSED**
- novelty of the threshold/equality: **OPEN / NOT YET AUDITED**

Thus the mathematical equality
\[
\boxed{f_{T_\beta}=r_{T_\beta}=p+1}
\]
is retained under the declared conventions, but no novelty claim is attached to it until the exact literature antecedents are checked.

Detailed audit: research/PAPER3_T_BETA_FACTORIZATION_THRESHOLD_AUDIT_2026-09-27.md (corrected commit 0ac32319db372c8e420173a5c9904ca6227e0649).

## 2026-09-27 — PAPER 3 SEPARATION AXIS CORRECTION

A structural correction closes a definitional ambiguity in the factorization-vs-recognition program. If both quantities are defined for the same target T by "T factors through W_n" versus "W_n determines T", then they are the same information condition and cannot furnish a genuine numerical separation. Therefore the load-bearing separation problem must use a richer carrier/observation O and a coarser target T=Phi(O): compare f_O with r_T.

Status:
- same-target f_T versus r_T separation: **INVALID / CLOSED — DEFINITIONAL IDENTITY**
- richer-carrier O versus coarser-target T separation: **OPEN / LOAD-BEARING**
- T_beta branch: **CLOSED** as a consistency check, not a separation example
- next authorized gate: candidate carrier/target pair novelty + non-redundancy audit before computation

The finite Kummer/affine orientation carrier versus a coarser target remains the first candidate family, but no target is promoted until its compression map and independent thresholds are explicit.

## 2026-09-27 — CANDIDATE B MOD-27 BOCKSTEIN CARRIER CLOSED

Mathematical and literature audit complete. B_27 is retained as a finite q-layer detector: PASS/LOCAL. As a new non-tautological mod-27 orientation carrier: FAIL/CLOSED.

The full structured carrier is classified into the three valuation classes on the standard family; no independent orientation-sensitive rigidifier has been exhibited; and direct prior-art overlap exists with Bockstein-based Demushkin level constructions and the Kummerian/canonical-orientation framework. The earlier abstract-symmetry no-go is not used because group-realizability was not established.

No further trivial-coefficient Bockstein scan. Next decisive target: intrinsic P_4/D_10 higher power/relation residual and its scalar normalization/transport theorem.
