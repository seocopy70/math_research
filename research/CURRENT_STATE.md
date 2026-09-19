# CURRENT_STATE — 수학증명

Last updated: 2026-09-19

> 목적: 새 창이 열려도 현재 연구의 작업 상태와 확정된 디테일을 즉시 복원하기 위한 live state. 상세 유도·계산은 별도 연구 문서가 정본이다.

## 0. 현재 위치

- 전체 지도: RESEARCH_MAP.md
- 현재 작업: Q3/Q9 — C-2c-2, degree-9 restricted relation ideal definition audit
- 상태: **C-2c-2 baseline closure certificate PASS / S9 admission still OPEN**
- 연구 원칙: **정의 → 검증 → 계산 → 해석**
- 지금은 D9, H-stability, q=9 검출 계산으로 넘어가지 않는다.

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

## LIVE

현재 LIVE 질문:

> baseline restricted ideal I_∞의 degree-9 closure를 끝낸 상태에서, S9 = X1^9를 restricted-Lie source로 인정할 수 있는가?

현재 답:

> **I_∞,9 = 13524는 exact certificate로 닫혔다. S9 admissibility와 I_∞,9 내부 여부는 아직 미결이다.**
