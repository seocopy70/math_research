# CURRENT_STATE — 수학증명

Last updated: 2026-09-19

> 목적: 새 창이 열려도 현재 연구의 작업 상태와 확정된 디테일을 즉시 복원하기 위한 live state. 상세 유도·계산은 별도 연구 문서가 정본이다.

## 0. 현재 위치

- 전체 지도: RESEARCH_MAP.md
- 현재 작업: Q3/Q9 — C-2c-2, degree-9 restricted relation ideal definition audit
- 상태: IN PROGRESS / DEFINITION GATE
- 연구 원칙: 정의 → 검증 → 계산 → 해석
- 지금은 D9, H-stability, q=9 검출 계산으로 넘어가지 않는다.

## 1. STABLE — 이미 닫힌 결과

### Q3/Q∞ baseline probe
- Q3/Q∞-J: CLOSED.
- 고정된 probe에서
  - J(N(d3)) = 40
  - J(N(d∞)) = 1
  - |ker(H→GL(U))| = 2
  - |H_U| = 25920
  - |Stab_H(N(d3))| = 1296
  - |Stab_HU(N(d3))| = 648
- first-isomorphism / orbit-stabilizer checks PASS.
- 해석 범위: 지정된 N/J probe가 q=3과 고정 q=∞ baseline을 구별한다는 것. canonical 3-adic orientation recovery는 주장하지 않는다.

### Q3/Q9 Gate A
- degree-3 q=9 probe: PASS / CLOSED.
- 독립 truncated-Magnus 검증에서 d9 = 0.
- 따라서 기존 degree-3 N/J Gate B는 BLOCKED / NOT OPENED.
- 다음은 degree-9에서 첫 비자명 q=9 source를 다루는 Gate C 계열이다.

### C-2a / C-2b / C-2c-1
- C-2a restricted-power identification: PASS.
  - X1^[3] ↔ X1^3 in the enveloping/tensor realization.
  - (X1^[3])^[3] = X1^9.
  - 이것은 restricted-power identification preflight일 뿐, D9/H-stability/NJ를 뜻하지 않는다.
- C-2b implementation/action audit: PASS.
- C-2c-1 restricted ambient certificate: PASS.
  - dim L9 = 29120.
  - dim L3 = 20, dim L1 = 4.
  - 프로젝트 convention에서 dim L9^res = 29120 + 20 + 4 = 29144.
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

## 3. C-2c-2의 핵심 문제

degree-9 restricted relation ideal R9를 먼저 정의해야 한다.

현재 repo에는 degree-9 restricted ideal의 완결된 정의가 아직 없다. 따라서 다음을 먼저 확정한다.

1. 기존 relation recursion의 정확한 의미 확인.
2. ordinary Lie ideal layer와 restricted ideal closure를 분리.
3. free restricted Lie ambient L9^res 안에서의 smallest restricted ideal의 degree-9 piece를 정의.
4. 그 정의를 basis/rank certificate로 검증.
5. 그 다음에만 H-stability를 검토.
6. 그 다음에만 D9 후보를 검토.

### 반드시 계승할 relation recursion
repo의 역사적 오류 및 재검증으로 다음은 LOCKED:
- (R)_3 = [L1,(R)_2]
- (R)_4 = [L1,(R)_3]
- (R)_5 = [L1,(R)_4]

과거의 [L2,R]을 full (R)_4로 사용한 계산은 잘못되었고 폐기됨.
- old dim [L2,R] = 5
- corrected dim (R)_4 = 15
- corrected dim (R)_5 = 60

따라서 degree 9에서도 shortcut으로 [Lk,R] 하나만 잡아 R9라고 하지 않는다.

## 4. Restricted ideal 정의에서 주의할 점

char = 3.

restricted ideal은 ordinary bracket closure만이 아니라 restricted p-map closure도 포함해야 한다.

따라서 degree 9에는 적어도 다음 종류의 기여 가능성을 열어 두고 정의부터 검토한다.
- ordinary recursive bracket closure;
- degree-3 relation piece의 [3] closure;
- degree-6에 생긴 restricted closure를 bracket으로 degree 9까지 올리는 경로;
- 그 밖의 restricted-ideal closure에서 생기는 degree-9 항.

특히 “R9 = ordinary (R)_9 + (R_3)^[3]” 같은 단순식을 아직 가정하지 않는다. 중복성/포함관계는 계산 또는 대수적 증명으로 확인한다.

가장 안전한 정의 후보는 homogeneous free restricted Lie algebra에서 initial relation을 포함하고 bracket 및 p-map에 대해 닫힌 최소 graded restricted ideal의 degree-9 piece다. 단, repo의 relation convention과 정확히 접합되는지 확인 후 채택한다.

## 5. 현재 금지된 해석

다음은 아직 주장하지 않는다.

- S9가 gr9(G)에서 nonzero라고 주장하지 않음.
- S9 = X1^[9]를 자동 동일시하지 않음.
- gr9(G) = L9/R9라고 쓰지 않음.
- R9가 H-stable이라고 가정하지 않음.
- D9를 [S9,X2]로 채택하지 않음.
- 기존 degree-3 N을 degree-9에 재사용하지 않음.
- q=9가 특정 invariant로 검출된다고 예상 결과를 넣지 않음.
- orientation recovery/canonicity를 주장하지 않음.

## 6. 다음 실제 작업

다음 한 단계: 기존 relation recursion과 restricted-power convention을 바탕으로, degree-9에서의 smallest restricted relation ideal 정의를 수학적으로 고정한다.

검증 순서:
1. repo convention 확인 완료 — 03_CONVENTIONS_AND_IMPLEMENTATION.md 및 relation audit 확인.
2. ordinary recursive relation layers와 restricted closure의 관계를 명시.
3. R9의 canonical recursive definition 작성.
4. 필요한 lower-degree pieces를 계산/검증.
5. degree-9 rank/basis certificate.
6. definition gate PASS 여부 판정.
7. 이후에만 H-stability.

## 7. 핵심 참조 문서

- RESEARCH_MAP.md — 전체 연구 지도.
- research/Q3_Q9_PROTOCOL_2026-09-18.md — Q3/Q9 전체 protocol.
- research/Q3_Q9_C2c0_definition_gate_2026-09-19.md — C-2c-0 고정 정의.
- research/Q3_Q9_C2c1_restricted_ambient_dimension_certificate_2026-09-19.md — L9^res = 29144 certificate.
- research/03_CONVENTIONS_AND_IMPLEMENTATION.md — authoritative conventions.
- research/RELATION_RECURSION_AUDIT_2026-09-16.py — corrected recursive relation audit.
- research/RELATION_LAYER_ERROR_AND_REVALIDATION_2026-09-16.md — [L2,R] 오류 및 R3/R4/R5 재검증 기록.
- research/Q3_Q9_GATE_C2a_restricted_power_2026-09-19.py — restricted-power identification preflight.

## 8. 새 창 복구 규칙

새 창에서는 이 파일을 먼저 읽고:

STABLE은 재검토하지 말고 계승 → LIVE/현재 Gate만 이어서 작업 → 필요한 상세 문서만 추가 확인.

이 파일에 없는 세부 계산은 임의로 기억해서 복원하지 말고, 해당 참조 문서를 확인한다.

---

## LIVE

현재 LIVE 질문은 하나다:

> C-2c-2: free restricted Lie degree-9 ambient 안에서 q=∞/finite-q relation으로부터 생성되는 degree-9 restricted ideal R9를 정확히 어떻게 정의할 것인가?

현재 답: 아직 정의 gate 미통과.
