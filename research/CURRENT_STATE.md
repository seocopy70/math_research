# CURRENT_STATE — 수학증명

Last updated: 2026-09-19 (S9 preflight)

> 목적: 새 창이 열려도 현재 연구의 작업 상태와 확정된 디테일을 즉시 복원하기 위한 live state. 상세 유도·계산은 별도 연구 문서가 정본이다.

## 0. 현재 위치

- 전체 지도: RESEARCH_MAP.md
- 현재 작업: Q3/Q9 — S9 degree-9 source-map route의 D9-OBS definition gate 후속 정리
- 상태: **D9-OBS natural p-layer shadow = FAIL / CLOSED**
- 연구 원칙: **정의 → 검증 → 계산 → 해석**
- 현재는 새로운 4D orbit 계산이나 인위적 observable 발명을 하지 않는다. presentation-derived structure가 p-layer shadow 밖에서 남는지 먼저 검토한다.

## 1. STABLE — 이미 닫힌 결과

### Q3/Q∞ baseline probe
- Q3/Q∞-J: CLOSED.
- 고정된 probe에서 J(N(d3)) = 40, J(N(d∞)) = 1.
- |ker(H→GL(U))| = 2, |H_U| = 25920.
- |Stab_H(N(d3))| = 1296, |Stab_HU(N(d3))| = 648.
- first-isomorphism / orbit-stabilizer checks PASS.
- 해석 범위: 지정된 N/J probe가 q=3과 고정 q=∞ baseline을 구별한다는 것. canonical 3-adic orientation recovery는 주장하지 않는다.

### Q3/Q9 Gate A
- degree-3 q=9 probe: PASS / CLOSED.
- 독립 truncated-Magnus 검증에서 d9 = 0.
- 기존 degree-3 N/J Gate B는 BLOCKED / NOT OPENED.
- 다음은 degree-9에서 첫 비자명 q=9 source를 다루는 Gate C 계열이다.

### C-2a / C-2b / C-2c-1
- C-2a restricted-power identification: PASS.
- C-2b implementation/action audit: PASS.
- C-2c-1 restricted ambient certificate: PASS.
  - dim L9 = 29120.
  - dim L3 = 20, dim L1 = 4.
  - dim L9^res = 29144 under the project's established F3 convention.
  - gr9(G)와 R9는 아직 미정.

## 2. C-2c-0에서 고정된 정의

- x_i = 1 + X_i.
- C_q = x1 x2 [x3,x4] x1^q x2^{-1}.
- C_∞ = x1 x2 [x3,x4] x2^{-1}.
- s_q = C_q x1^{-1} [x3,x4]^{-1}.
- s_∞ = C_∞ x1^{-1} [x3,x4]^{-1}.
- Δ_d(q) := in_d(s_q - s_∞).
- S9 := Δ_9(9).
- 기존 C-1a/C-1b 입력: Δ_d(9)=0 for d=1,…,8; Δ_9(9)=X1^9 ≠ 0.

### 절대적 구분
- S9 = X1^9는 우선 associative Magnus word의 등식이다.
- 이를 자동으로 X1^[9]라는 restricted-Lie 원소와 동일시하지 않는다.
- A9, L9, L9^res, gr9(G)는 서로 다른 층위다.
- 아직 D9를 정의하지 않았다.

## 3. C-2c-2에서 새로 정리된 정의 후보

- q=∞ baseline과 q=9를 하나의 R9로 뭉개지 않는다.
- I_∞ := smallest graded restricted ideal containing R2 = [X1,X2]+[X3,X4].
- I_∞,9 := degree-9 piece of I_∞.
- q=9 source S9는 아직 associative Magnus word로만 확정.
- S9를 restricted ambient의 원소로 별도 인정할 수 있을 때에만 조건부로 I_9 := <R2, s9^res>_res를 정의하고 I_9,9를 취한다.
- 이것은 **definition draft**이며 아직 gate PASS가 아니다.

### Restricted closure candidate
graded closure에서 degree n piece는 bracket closure와 p-map closure를 모두 포함해야 한다.
- bracket: [L_i^res, I_{n-i}]
- p-map: (I_{n/3})^[3] when 3 divides n
- 모든 항은 exact F3 span에서 중복성을 확인한다.
- 특히 R9를 ordinary relation layer 하나나 [Lk,R2] shortcut으로 정의하지 않는다.

### 기존 relation recursion은 LOCKED
- (R)_3 = [L1,(R)_2]
- (R)_4 = [L1,(R)_3]
- (R)_5 = [L1,(R)_4]
- old [L2,R] full-R4 construction은 폐기.
- old dim [L2,R] = 5.
- corrected dim (R)_4 = 15.
- corrected dim (R)_5 = 60.

## 4. 현재 금지된 해석

- S9가 gr9(G)에서 nonzero라고 주장하지 않음.
- S9 = X1^[9]를 자동 동일시하지 않음.
- gr9(G) = L9/R9라고 쓰지 않음.
- R9가 H-stable이라고 가정하지 않음.
- D9를 [S9,X2]로 채택하지 않음.
- 기존 degree-3 N을 degree-9에 재사용하지 않음.
- q=9가 특정 invariant로 검출된다고 예상 결과를 넣지 않음.
- orientation recovery/canonicity를 주장하지 않음.

## 5. C-2c-2 exact baseline closure through degree 9 — PASS

2026-09-19 exact closure certificate로 baseline restricted ideal I_∞의 degree 9까지를 닫았다.

- dim L1..L9 = 4, 6, 20, 60, 204, 670, 2340, 8160, 29120.
- dim L3^res = 24, dim L6^res = 676, dim L9^res = 29144.
- restricted quotient g_n dimensions = 4, 5, 20, 45, 144, 445, 1440, 4680, 15620.
- baseline restricted ideal:
  - I2=1, I3=4, I4=15, I5=60,
  - I6=231, I7=900, I8=3480, I9=13524.
- ordinary relation dimensions:
  - I2^ord=1, I3^ord=4, I4^ord=15, I5^ord=60,
  - I6^ord=230, I7^ord=900, I8^ord=3480, I9^ord=13520.
- restricted increment: degree 6 = +1, degree 9 = +4; all other degrees ≤9 = 0.
- degree ≤5의 restricted-ideal 신규 p contribution은 0을 명시적으로 확인.
- degree 9의 +4는 유일한 신규 relation p-source인 I3^[3]에 해당. I2^[3]의 degree-9 bracket descendants는 ordinary ideal 안에 들어간다.
- degree 9 certificate는 direct huge matrix 대신 u(g)=T(V)/(R2)의 Hilbert series 1/(1-4t+t^2)와 restricted PBW의 exact coefficient inversion으로 수행했다.
- Actions run 35409723512 = SUCCESS.

상세 정본: `research/Q3_Q9_C2c2_exact_degree9_restricted_closure_result_2026-09-19.md`

**현재 다음 단계:** baseline closure는 닫혔다. 이제 S9의 restricted-Lie admissibility를 독립적으로 다룬다. 아직 S9를 I_∞,9에 넣지 않는다.

그 다음:
1. S9 = X1^9의 quotient-level restricted-Lie admissibility 확인;
2. S9가 I_∞,9에 이미 포함되는지 별도로 판정;
3. admissible하면 q=9 restricted ideal I_9 정의 및 degree-9 변화 계산;
4. 그 후 H-stability;
5. 마지막으로 D9 후보 검토.

## 6. 핵심 참조 문서

- RESEARCH_MAP.md — 전체 연구 지도.
- research/Q3_Q9_PROTOCOL_2026-09-18.md
- research/Q3_Q9_C2c0_definition_gate_2026-09-19.md
- research/Q3_Q9_C2c1_restricted_ambient_dimension_certificate_2026-09-19.md
- research/Q3_Q9_C2c2_restricted_relation_ideal_definition_draft_2026-09-19.md
- research/03_CONVENTIONS_AND_IMPLEMENTATION.md
- research/RELATION_RECURSION_AUDIT_2026-09-16.py
- research/RELATION_LAYER_ERROR_AND_REVALIDATION_2026-09-16.md
- research/Q3_Q9_GATE_C2a_restricted_power_2026-09-19.py

## 7. 기록 구조 / 중복 방지 규칙

현재 저장소에는 이미 **역사 기록 문서가 존재한다**: `research/00_RESEARCH_LOG.md`.
따라서 별도의 `RESEARCH_LOG.md`를 새로 만들지 않는다.

### 역할 분리

- `RESEARCH_MAP.md` — 전체 연구 지도와 현재의 큰 수학적 상태. 현재 상태의 최상위 지도.
- `research/CURRENT_STATE.md` — **새 창에서 즉시 재개하기 위한 live state**. 현재 Gate, 확정 입력, 금지된 해석, 바로 다음 작업만 유지한다.
- `research/00_RESEARCH_LOG.md` — **연구의 시간적 역사**. 중요한 결정, 방향 전환, 정의 변경, 폐기된 가설, 주요 오류/수정만 누적한다. 이미 존재하므로 중복 로그를 만들지 않는다.
- 개별 `research/*_RESULT_*.md`, 정의/계산 문서 — **수학적 증거와 세부 과정의 정본**. 계산·유도 자체를 다른 문서에 복사하지 않는다.
- `ANTIPATTERNS.md` — **재발 방지용 실패 패턴**. 단순 실패 이력을 중복 기록하지 않고, 다시 발생하면 안 되는 일반 규칙만 둔다.

### 기록 최소화 원칙

모든 작업을 기록하지 않는다.

다음 중 하나일 때만 `CURRENT_STATE` 또는 `00_RESEARCH_LOG`를 갱신한다.

1. Gate의 PASS / FAIL / BLOCK 상태가 바뀜.
2. 정의·가정·해석 범위가 확정 또는 변경됨.
3. 중요한 가설을 폐기하거나 연구 방향을 바꿈.
4. 오류가 발견되어 이후 계산의 기준이 바뀜.
5. 다음 단계가 바뀔 정도의 중요한 결과가 나옴.

그 밖의 실행 로그, 사소한 코드 수정, 중간 숫자는 해당 상세 문서/Actions artifact에만 남긴다.

**원칙: 한 사실은 한 정본에만 상세히 기록하고, 다른 문서는 필요한 경우 한 줄 요약과 참조만 둔다.**

## 8. 새 창 복구 규칙

새 창에서는 이 파일을 먼저 읽는다.

**STABLE은 계승 → 현재 Gate/LIVE만 이어서 작업 → 필요한 상세 문서만 확인.**

이 파일에 없는 세부 계산은 추측으로 복원하지 않고 해당 상세 문서를 확인한다.

---

## 9. S9 admissibility preflight — 2026-09-19

- Prerequisite audit is complete; the S9 admissibility experiment itself has **not** been executed.
- Gate C-2a independently supports the ambient restricted-power identity X_1^[9] = X_1^9 in the one-generator enveloping realization.
- C-2c-1 independently validates the degree-9 ambient layer separation in rank 2 using exact F_3 rank.
- The mandatory implementation invariants for the actual S9 run are frozen: complete H-closure, one common coordinate system, exact F_3 rank, and sanity/rank-nullity checks.
- This does **not** authorize S9 insertion into I_infty,9.
- Baseline remains frozen at dim I_infty,9 = 13524 and dim I_3^[3] = 4.
- Detailed preflight record: research/Q3_Q9_S9_admissibility_preflight_2026-09-19.md

## 9. S9 admissibility / quotient survival — CLOSED

- S9-A: **PASS / CLOSED**.
- S9-B: **PASS / CLOSED** after the required structural lemma.
- Structural lemma:
  \[
  (I_\infty)_9=(I^{ord})_9\oplus I_3^{[3]},\qquad
  (I_\infty)_9\cap L_1^{[9]}=0.
  \]
- Therefore, with \(S_9=X_1^{[9]}\neq0\in L_1^{[9]}\),
  \[
  S_9\notin I_{\infty,9}.
  \]
- Frozen baseline remains \(\dim I_{\infty,9}=13524\); S9 has not been inserted into it.
- Structural lemma record: `research/Q3_Q9_S9_B_STRUCTURAL_LEMMA_RESULT_2026-09-19.md`.
- S9-B result record: `research/Q3_Q9_S9_B_QUOTIENT_SURVIVAL_RESULT_2026-09-19.md`.

## 10. NEXT GATE — q=9 restricted relation space

The next authorized object is
\[
I_9:=\langle R_2,S_9\rangle_{res},
\qquad I_{9,9}:=I_9\cap L_9^{res}.
\]

Execution requirements:
1. Keep the frozen baseline \(I_\infty\) separate.
2. Use \(S_9=X_1^{[9]}\) only under the already-closed S9-A convention.
3. At degree 9 include the complete restricted closure generated by both sources; do not replace the definition by an unexplained “R9”.
4. Use exact \(\mathbb F_3\) rank / one common coordinate system for any coordinate computation.
5. Verify the degree-9 consequence independently of the baseline dimension count.
6. H-stability and D9 are downstream and remain closed/blocked until separately gated.

## 10. q=9 degree-9 relation space — PASS / CLOSED

The new restricted ideal is
\[
I_9:=\langle R_2,S_9\rangle_{res},
\qquad S_9=X_1^{[9]}.
\]

Because S9 has degree 9, its brackets have degree at least 10 and its restricted powers have degree 27. Thus at degree 9,
\[
I_{9,9}=I_{\infty,9}+\langle S_9\rangle.
\]

S9-B gives
\[
(I_\infty)_9\cap L_1^{[9]}=0,
\]
while S9 is nonzero in L1^[9]. Therefore
\[
I_{9,9}=I_{\infty,9}\oplus\langle S_9\rangle,
\]
and
\[
\boxed{\dim I_{9,9}=13525}
\]
versus frozen baseline 13524.

Exact F3 rank check of the new S9 direction: rank 1.

Result record:
research/Q3_Q9_S9_q9_degree9_relation_space_RESULT_2026-09-19.md

Script:
research/Q3_Q9_S9_q9_degree9_relation_space_2026-09-19.py

Workflow:
.github/workflows/q3-q9-s9-degree9-relation-space.yml

## 11. S9 source-map target-action audit — PASS / CLOSED

The target-side source map is
\[
Q_9^\infty=L_9^{res}/(I_\infty)_9,
\qquad
\phi_9(S_9)=[S_9].
\]

The earlier target-action audit checked all 80 nonzero-vector symplectic
transvections and verified (g^T Jg=J), then used the frozen coefficient-matrix
convention to infer (g(R_2)=R_2).

A dedicated explicit implementation bridge audit has now closed that small gap:
the repository's authoritative five generators and authoritative
associative action were imported directly, (R_2) was constructed explicitly,
and for every generator
\[
\boxed{g\cdot R_2=R_2}
\]
was checked exactly over (\mathbf F_3).

The same audit also passed multiplicativity and first restricted-power
compatibility on the authoritative action. Together with the existing C-2b
audit, this closes the implementation chain
\[
g^TJg=J\Rightarrow gR_2=R_2\Rightarrow h(I_\infty)=I_\infty.
\]

Therefore the baseline quotient (Q_9^\infty) has a well-defined induced
H-action. This is now **structural + explicit implementation-bridge PASS**.

Result:
research/Q3_Q9_S9_SOURCE_MAP_H_STABILITY_ACTION_BRIDGE_RESULT_2026-09-19.md

CI:
run 35414448355 / job 105820186019 = SUCCESS.

## 12. S9 target-side orbit — PASS / CLOSED

\[
\boxed{
\mathcal O_9=\langle H\cdot[S_9]\rangle
\cong L_1^{[9]},
\qquad
\dim\mathcal O_9=4.
}
\]

Reason: C3.1 gives (\langle H\cdot S_9\rangle=L_1^{[9]}), and
S9-B gives ((I_\infty)_9\cap L_1^{[9]}=0), so the quotient map is
injective on this p-layer.

This is a target-side H-module only. It is not the q=9 relation space and
does not repair the q=9 H-stability FAIL.

## 13. Rank-4 D4 lifting definition gate — FAIL / CLOSED

The rank-2 D4 control passed, but the proposed rank-4 observable failed the required lift-independence audit before any rank-4 q-comparison.

Two free-group lifts of the same identity linear action on V were tested: the identity lift and the IA-modified lift x1 -> x1[x1,x2]. The first is admissible; the second is not. Its degree-3 difference lies outside the ordinary conjugation correction span.

Therefore the candidate A_4^rel(q) is not intrinsic to g in GSp_4(F3) under the current allowed-lift definition.

Result: research/RANK4_D4_LIFT_INDEPENDENCE_AUDIT_RESULT_2026-09-19.md
CI: run 35415237341 / job 105822474022 = SUCCESS.

Consequence: no rank-4 q-comparison is authorized from this candidate. The failure shows that IA/lift data is active at degree 3 and cannot be discarded if the object is to be intrinsic to the linear map.

## 13A. CURRENT LIVE GATE — post-lifting failure direction

The Q3/Q9 S9 target-orbit route is **CLOSED at definition level** after D9-OBS natural p-layer shadow failure and the post-D9 structure census.

The next authorized continuation is the already-audited low-cost rank-2 lifting/relator-preservation control.

### Rank-2 D4 control — PASS / CLOSED

For
[
G_q^{(2)}=langle x_1,x_2mid x_1^q[x_1,x_2]=1angle
]
at the first q-sensitive Zassenhaus level (D_4), the selected representative lift tests passed the frozen expectations:

- q=3: identity and the selected vector-fixing unipotent are admissible.
- q=3: (-I) fails although it stabilizes the line (ell=langlear x_1angle); it reverses the degree-3 restricted-power contribution.
- q=3: the selected transvection moving (ell) fails.
- q=(infty): all four selected representatives pass.
- exact F3 arithmetic and the degree-3 conjugation-span rank-2 audit passed.
- CI run 35415080640 / job 105822020636 = SUCCESS.

Detailed result:
research/RANK2_D4_LIFTING_CONTROL_RESULT_2026-09-19.md

### Interpretation boundary

This validates only the **rank-2 n=4 control pipeline**. It does not establish the full (A_4(q)), does not prove equality with a line stabilizer, and does not constitute a rank-4 theorem.

### Next authorized step

The rank-4 D4 lifting candidate is closed as FAIL. The next continuation must explicitly retain or canonically quotient the IA/lift data; do not select a hand-picked lift convention and call it intrinsic.

## 14. Frozen downstream boundaries

- naive ((I_9)_9) H-stability: **FAIL / CLOSED**.
- C3.2 H-closure provenance: **FAIL / CLOSED**.
- ((I_9)_9) dimension 13525 remains valid as a fixed-presentation degree-9 relation-space calculation, but must not be treated as an H-module.
- (mathcal O_9) is target-side only.
- D9-OBS via natural p-layer shadow: **FAIL / CLOSED**.
- post-D9 presentation-derived structure census: **CLOSED**.
- no q=3/q=9 distinction has been established by the 4D orbit.
- no D9.
- no orientation recovery.

## 15. Research-wide continuation boundary

The original research question remains OPEN:
[
	ext{Can prescribed weak filtered/graded or higher structure recover information about }chi_G?
]

The Q3/Q9 S9 orbit branch is closed, but the following research directions remain authorized in the roadmap:

- degree-4 module structure;
- Track B group/filtration calculations;
- higher-operation / extension structure;
- primary-source literature verification;
- the newly validated rank-2 lifting control followed by a separately gated rank-4 lifting experiment.

The rank-2 result is a **control validation**, not a proof of the rank-4 claim.


## 16. CURRENT LIVE GATE — IA / filtered extension datum

The rank-4 D4 linear-map lifting candidate is **FAIL / CLOSED** and is not to be revived by selecting a preferred lift.

A new definition gate is opened:
`plans/RANK4_D4_IA_EXTENSION_DATUM_GATE_2026-09-19.md`

The next authorized object is the degree-3 defect carried by the lift fibre over a fixed linear action, modulo only the already verified ordinary conjugation correction space. The purpose is to determine whether the IA/lift dependence can be organized canonically as a quotient, orbit/torsor, or extension datum without destroying the q-sensitive restricted-power signal.

### Immediate next step

Perform only a small IA defect-action audit:
1. identify the exact degree-3 defect target;
2. compute the degree-1 IA action on that target;
3. verify the lift-fibre torsor/change law;
4. test canonical quotient/orbit/extension candidates;
5. check whether q=3 information survives.

No rank-4 representative scan or new q-comparison is authorized before this gate closes.

Frozen boundaries: no hand-picked Nielsen lift as an intrinsic invariant; no reuse of the failed condition g e1 = mu(g)e1; no degree-3 N/J reuse; no q=9 H-closure rescue.


## 17. IA / filtered extension gate — first defect-action sub-gate result

The first authorized IA defect-action audit has been executed without a rank-4 group scan.

Frozen degree-3 associative target:
A_3 ≅ F_3^{4⊗3}, dim A_3=64, with ordinary conjugation correction space C_3 of rank 4. The first IA layer has dimension dim Hom(V,L_2)=24.

For identity, -I, and one standard transvection e_1 -> e_1+e_2, the IA defect-change map has rank 20 for both q=3 and q=infinity and the two variation maps agree exactly. Pairwise additivity over the 24 IA directions was checked. Hence the first-layer change law is linear in the tested degree-2 IA parameters.

The combined span C_3 + Delta_IA has rank 20, giving a 44-dimensional candidate quotient. For -I and the transvection, the q=3 versus q=infinity defect is nonzero and survives this quotient. Thus the mandatory nontriviality test passes locally: quotienting by the tested first-layer IA gauge does not automatically erase the q-sensitive restricted-power signal.

This is NOT a main-gate PASS. Canonicality/equivariance remains open.

Result: research/RANK4_D4_IA_DEFECT_ACTION_AUDIT_RESULT_2026-09-19.md
Script: research/rank4_D4_ia_extension_audit_2026-09-19.py

### Next authorized step

Perform quotient-legitimacy / equivariance audit: prove that the IA variation subspace is canonically defined, determine its transformation law under change of linear representative, and test whether the 44-dimensional quotient can carry the required compatible filtered/extension structure. No full rank-4 representative scan is authorized yet.


## 18. IA quotient equivariance sub-gate — PASS locally, main gate OPEN

The candidate gauge space G_3 = C_3 + Delta_IA was tested under the frozen degree-3 tensor action. All 80 nonzero-vector Sp_4(F_3) transvections preserve C_3, Delta_IA, and G_3. A multiplier-2 GSp_4(F_3) representative diag(1,2,1,2) also preserves the corresponding ranks 4, 20, and 20.

Thus the 44-dimensional candidate quotient A_3/G_3 is equivariant for the tested complete transvection family and tested GSp multiplier direction. This is a local structural PASS, not a proof of coordinate-free canonicity.

Result: research/RANK4_D4_IA_EQUIVARIANCE_AUDIT_RESULT_2026-09-19.md
Script: research/rank4_D4_ia_equivariance_audit_2026-09-19.py

### Next authorized step

Verify the graded lift-fibre composition/change law and determine whether the q-sensitive defect descends independently of a chosen base lift to an intrinsic orbit/torsor/extension class. No full rank-4 scan is authorized yet.
