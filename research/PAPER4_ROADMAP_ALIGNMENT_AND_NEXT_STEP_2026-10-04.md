# Paper 4 — Roadmap Alignment and Next-Step Decision — 2026-10-04

## 1. 목적

외부 핸드오프 로드맵
`research/external/GENERAL_THEOREM_ROADMAP_HANDOFF_2026-10-04.md`
과 현재 authoritative 상태를 대조하여 다음 Paper 4 연구 작업을 결정한다.

## 2. 비교 대상

- `RESEARCH_MAP.md`
- `CURRENT_STATE.md`
- `research/00_RESEARCH_LOG.md`
- `research/RESEARCH_CONTINUITY_PROTOCOL.md`
- `research/external/GENERAL_THEOREM_ROADMAP_HANDOFF_2026-10-04.md`

## 3. 외부 로드맵의 핵심

외부 로드맵은 다음 순서를 제안한다.

1. Theorem OD: 일반 r에 대한 위수 이분법
2. marked 일반화
3. **unmarked 문제(Theorem C): L4/L5 확대류 궤도 분리**
4. 비강성 일반화
5. 신규성 점검

특히 Theorem C의 첫 목표는 p=3, s=1, r=x^3 같은 작은 사례에서 비동형을 증명하고 이를 일반화하는 것이다.

## 4. 현재 Paper 4의 실제 상태

현재 authoritative 상태에서는 다음이 이미 확정되었다.

- arbitrary-degree degree-only 일반화: **FAIL / CLOSED**
- marked quadratic affine/E_psi detector: **PASS / CLOSED**
- ordinary mod-p cohomology route: **PASS / CLOSED / STOPPED**
- one-step filtered-extension에서 canonical scalar/orientation defect 추출: **FAIL / CLOSED**
- distinguished single-psi bridge: **FAIL / CLOSED**
- naive Sp-orbit bridge: **FAIL / CLOSED**
- two-step representation layer: **PASS / CLOSED as reformulation**
- exact unmarked same-window separation: **OPEN / LOAD-BEARING**
- all-s a=s versus a=infinity boundary: **OPEN / LOAD-BEARING**
- transfer/Schreier route: **PASS / LOCAL** witnesses only; all-s theorem remains OPEN

따라서 현재 문제는 로드맵이 말한 'unmarked separation'과 동일하지만, L4/L5 자체를 그대로 밀어붙이는 단계는 이미 지나갔다.

## 5. 현재 새로 확보된 Q 방향

현재 연구에서 다음 abstract finite-group invariant을 사용한다.

Q(W): 존재하는 생성쌍/생성분해 (g,H)가
  <g,H>=W, 1 != g^{p^s} in H
를 만족하는가.

확인된 evidence:

- p=3, s=1, r=x^3: W_s에서 Q-positive generating pairs가 52,488개, W_t에서는 0. 이는 exhaustive finite computation.
- p=5, s=1, r=x^5, n=6, rank 2: |W_s|=|W_t|=5^15; 200,000 random pairs에서 W_s는 10,226 Q-positive, W_t는 0. 이는 sample evidence일 뿐 exhaustive/proof가 아니다.

현재 Q의 핵심 증명 장애는 다음과 같이 정확히 국소화되었다.

Q-positive pair를 Frattini lift하여 자유군 automorphism alpha와 transformed relator r'=alpha^{-1}(r)로 바꾸는 접근은 자연스럽다. z를 죽이는 quotient에서 z-exponent epsilon(r')에 대한 필요조건 v_p(epsilon)<=s를 얻을 수 있으며, 이는 high-valuation abelian obstruction과 일치한다.

그러나 a=s와 같은 hard region에서는 abelian information만으로 부족하다. 남은 핵심은 모든 relevant alpha에 대해 transformed relator r'의 **nonabelian Magnus/PBW obstruction**을 증명하는 것이다.

이 과정에서 기존 restricted-Lie root-capture 시도는 일반적으로
D_j(H)=H∩D_j(W)
를 보장하지 않는다는 이유로 실패했다. 따라서 필요한 것은
H∩D_k(W)
의 induced filtration에서 직접 작동하는 Root-Capture lemma 또는 동등한 Frattini-lift/Magnus formulation이다.

## 6. 로드맵과 현재 상태의 일치/불일치

### 일치

로드맵의 가장 중요한 판단은 맞다.

- 다음 핵심 문제는 marked detector가 아니라 **unmarked finite-window separation**이다.
- 작은 control case에서 비동형을 먼저 설명하고 일반화하는 전략이 맞다.
- 계산은 발견용이고, 최종적으로 invariant와 수학적 증명이 필요하다.
- p=3, s=1, r=x^3은 여전히 가장 좋은 첫 laboratory이다.

### 불일치

로드맵의 구체적 구현 경로인 L4/L5 확대류 궤도 분리는 현재 최우선 경로로 볼 수 없다.

이미 one-step extension extraction과 representation-layer gate에서 확인된 것은:
- 전체 extension/tower를 intrinsic하게 구성할 수는 있지만,
- 그것에서 더 작은 canonical scalar/carrier를 뽑는 것은 실패했고,
- affine orbit/groupoid는 원래 structured finite-window 문제의 재표현에 머문다.

따라서 L4/L5를 그대로 다시 계산하는 것은 이미 닫힌 방법론적 경계를 반복할 위험이 있다.

## 7. 결정

**로드맵 수준의 다음 목표:** PASS / 적합
> unmarked same-window separation을 작은 사례에서 설명하고 일반화한다.

**로드맵의 원래 구현 방식 L4/L5:** FAIL / 우선순위 낮음
> 현재 상태에서 그대로 재개하는 것은 중복 가능성이 높다.

**수정된 판단:** 현재 기록된 unrestricted Q는 nonabelian detector로 부적합하므로 위 계획을 즉시 실행하지 않는다. 먼저 Q의 H에 대한 intrinsic restriction을 복원해야 하며, 복원되지 않으면 Q는 폐쇄하고 L4/L5 또는 다른 genuinely nonabelian invariant로 돌아간다.

즉, Q는 로드맵의 Theorem C를 폐기하는 것이 아니라 **현재까지의 실패를 반영해 Theorem C를 더 정확한 finite-group formulation으로 재구성한 것**이다.

## 8. 다음 한 단계

첫 실행은 다음으로 고정한다.

1. p=3, s=1, r=x^3의 W_4에서 Q-positive pair를 분류한다.
2. 각 pair를 GL/Aut-orbit 및 Frattini lift 관점에서 압축한다.
3. transformed relator r'=alpha^{-1}(x^3)를 Magnus/PBW의 최소 필요한 차수까지 계산한다.
4. W_t에서 Q가 불가능해지는 공통 nonabelian obstruction을 추출한다.
5. 그 obstruction이 induced filtration H∩D_k(W)에 대해 일반화 가능한지 판정한다.
6. 가능하면 Root-Capture/Magnus lemma로 정리하고, 불가능하면 정확한 FAIL/CLOSED 경계를 기록한다.

**Stop rule:** 단순 orbit census가 새로운 invariant를 제공하지 않거나, transformed-relator obstruction이 presentation-dependent임이 확인되면 Q 경로를 더 확대하지 않는다.

## 9. 최종 분류

- Paper 4 certified core: **PASS / CLOSED**
- marked quadratic affine detector: **PASS / CLOSED**
- unmarked same-window separation: **OPEN / LOAD-BEARING**
- Q invariant: **PASS / LOCAL as computation; FAIL / CLOSED as intended nonabelian separator under current unrestricted H definition**
- Q nonabelian obstruction / Root-Capture: **OPEN / LOAD-BEARING**
- external roadmap's unmarked Theorem C direction: **VALID at strategic level, superseded at implementation level**
- next action: **Q definition audit; if no intrinsic H restriction exists, close Q and resume genuinely nonabelian extension/orbit route**

This document is a dated alignment record; it does not promote any local computation to theorem status.


## 2026-10-04 — Q definition pre-check correction

The planned transformed-tuple computation was stopped before execution. Under the current definition, Q-positive already implies an element of order greater than p^s, while H is otherwise unrestricted. Hence Q does not force a nonabelian obstruction and may collapse to coarse exponent information. The current Q is therefore FAIL / CLOSED as a nonabelian separator unless an intrinsic restriction on H is recovered. This correction supersedes the earlier immediate-Q execution plan.
