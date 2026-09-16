# Research Operating System — 2026-09-17

## 목적

Demuškin/A3-4 연구에서 반복적으로 발생한 좌표·체·실행환경 오류를 연구 자산으로 전환하고, AI를 포함한 어떤 보조 시스템이 연구를 이어받더라도 동일한 검증 규칙을 적용할 수 있도록 운영 체계를 고정한다.

## 구현된 층

### 1. CI Gate

`research/FINITE_FIELD_RANK_AUDIT_2026-09-17.py`가 AST로 tracked research Python 파일의 실제 `numpy.linalg` 호출을 검사한다. `matrix_rank`와 `det`는 \(\mathbb F_3\) 계산에서 금지된다.

검증된 audit run:

- Run `35158243283` — repository-wide finite-field rank audit: PASS.
- Run `35158243308` — B1-1 W45 workflow: success.

주의: B1-1 run `35158243308`의 GAP sanity probe에는 field mismatch가 있었지만 pipeline이 fail-open되어 step이 success로 남았다. 이는 AP-009로 기록했고 이후 workflow를 `set -euo pipefail` + 명시적 GF(3) 행렬로 수정했다. 따라서 그 run의 **수학적 B1-1 출력은 유효한 exact-F3 부분과 분리하여 읽어야 하며, sanity probe 자체는 PASS 증거로 사용하지 않는다.**

### 2. Living SOP

`research/03_CONVENTIONS_AND_IMPLEMENTATION.md`에 다음을 공식화했다.

- \(\mathbb F_3\) 고정
- Python column action
- GAP row/right action
- Python→GAP transpose 규칙
- 검증된 `rank3()` 재사용
- forbidden numerical rank/determinant
- sanity invariants
- three-layer verification
- result classification
- 연구 진행 순서

### 3. AI Context

루트의 `AI_CONTEXT_BRIEF.md`는 새 AI 세션이 연구를 이어받을 때 읽는 짧은 기준 문서다. 연구 목표, 권위 차원, q 계층, A3-4 module chain, B1-1 현재 위치, 좌표/체 규약, 실행 원칙을 담는다.

### 4. Antipattern Log

루트의 `ANTIPATTERNS.md`는 오류를 삭제하지 않고 보존한다.

현재 주요 항목:

- AP-001: real-field rank on F3 data
- AP-002: Python/GAP transpose omission
- AP-003: equality inferred from dimensions
- AP-004: End_H(W) misused as an outside-submodule generator
- AP-005: missing package mistaken for mathematical failure
- AP-006: sanity invariant violation not treated as immediate invalid-test trigger
- AP-007: unverified result promoted to theorem
- AP-008: stale historical dimensions
- AP-009: CI pipeline allowed a failed sanity probe to pass

## 결과 분류

\[
\boxed{
\text{SETUP FAILURE}
\to\text{IMPLEMENTATION FAILURE}
\to\text{INVALID TEST}
\to\text{MATHEMATICAL FAILURE}
\to\text{PASS}}
\]

이는 순차 단계가 아니라 공통 상태/원인 분류이다.

## 현재 수학적 기준선

현재 authoritative degree-4 dimensions:

\[
\dim L_4=60,\quad\dim(R)_4=15,\quad\dim Q_4=45.
\]

B1-1에서 authoritative exact-F3 computation은 다음을 확인했다.

\[
\dim W=45,
\quad \dim End_H(W)=2,
\quad rank(N)=10,
\quad \dim ker N=35,
\quad N^2=0,
\]

그리고 GAP에서 올바른 transpose \(N^T\)를 사용하여

\[
\dim Soc(W)=10,
\quad \dim im(N)=10,
\quad Soc(W)=im(N)
\]

를 확인했다. 다만 이것만으로 W가 uniserial이라고 결론내리지 않는다. 다음 단계는 35차원 H-submodule의 유일성과 그에 따른 45차원 H-stable lift의 유일성을 직접 검증하는 것이다.

## 다음 단계

1. 수정된 B1-1 workflow가 실제 실행되었는지와 sanity probe가 이제 정상 PASS하는지 확인.
2. B1-1에서 \(Soc(W)=im(N)\) 이후의 **35차원 H-submodule uniqueness**를 직접 검증.
3. uniqueness가 확보되면 45차원 H-stable lift의 유일성(B1-2)으로 이동.
4. q=9의 exact size detection은 별도 degree-9 track으로 유지.

## 운영 원칙

\[
\boxed{
\text{수학적 주장}
\rightarrow
\text{계산 설계}
\rightarrow
\text{독립 검증}
\rightarrow
\text{CI 재현}
\rightarrow
\text{기록}}
\]

실행 로그가 없는 결과는 공식 PASS로 부르지 않는다. 오류가 발견되면 삭제하지 않고 원인·무효 범위·정정·재발 방지책을 함께 기록한다.
