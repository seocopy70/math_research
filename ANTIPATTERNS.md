# Antipatterns / Failure Log

이 문서는 계산 결과를 빠르게 얻는 것보다 **왜 틀릴 수 있었는지와 어떻게 재발을 막는지**를 보존하기 위한 연구 인프라 문서입니다.

## AP-001 — Real-field rank on F3 data

**상태:** INVALID TEST

`numpy.linalg.matrix_rank`를 \(\mathbb F_3\) 행렬에 적용하면 실수체 수치 rank를 계산합니다. B1-1에서 출력된 `24`는 이런 잘못된 진단값이었으며 \(\mathbb F_3\) rank가 아닙니다.

**정정:** 검증된 `rank3()` 및 GAP `GF(3)` rank 사용.

**재발 방지:** repository-wide AST audit와 CI gate에서 `numpy.linalg.matrix_rank`, `numpy.linalg.det`를 금지.

---

## AP-002 — Python column action passed to GAP without transpose

**상태:** INVALID TEST

Python은 \(v\mapsto Av\) column action인데 GAP `GModuleByMats`는 row/right action입니다. 따라서 Python 행렬을 그대로 GAP에 넘기면 같은 수학적 작용을 표현하지 않습니다.

A3-4-20S 및 B1-1에서 이 문제가 실제로 드러났습니다. 특히 B1-1의 `Soc(W) != im(N)`라는 초기 결과는 `N^T` 대신 `N`을 사용한 좌표 불일치 때문에 무효였습니다.

**정정:** 생성자뿐 아니라 endomorphism \(N\), kernel/image/socle basis에도 동일한 transpose 규칙 적용.

**재발 방지:** 모든 실험 기록에 action direction, matrix convention, transpose rule을 명시.

---

## AP-003 — Dimensions used as subspace equality

**상태:** INVALID METHODOLOGY

두 부분공간의 차원이 같다는 사실만으로 동일성을 주장할 수 없습니다.

**정정:** 같은 ambient coordinates에서 joined-span rank를 계산하여 equality를 확인합니다.

대표적인 올바른 형태:
\[
\dim U=\dim V=\dim\langle U,V\rangle
\Rightarrow U=V.
\]

---

## AP-004 — End_H(W) treated as a generator of outside submodules

**상태:** CONCEPTUAL ERROR

\(End_H(W)\)의 원소는 W에서 W로 가는 H-endomorphism이므로 그 image는 항상 W 안에 있습니다. 따라서 End_H(W) 자체만으로 W 바깥의 45차원 후보를 생성할 수 없습니다.

**정정:** End_H(W)는 W 내부의 submodule/Loewy 구조를 분석하는 도구로 사용하고, 외부 lift는 별도의 H-stable extension/lift 문제로 다룹니다.

---

## AP-005 — Missing package interpreted as mathematical failure

**상태:** SETUP FAILURE

Ubuntu 환경에서 `gap-meataxe` 패키지를 직접 설치하려다 package-not-found가 발생했습니다. 실제 수학 계산이 실행되지 않았으므로 이는 수학적 실패가 아닙니다.

**정정:** A3-4-20R에서 이미 검증된 GAP 설치 절차를 재사용.

---

## AP-006 — Necessary module invariant violated without stopping

**상태:** INVALID TEST TRIGGER

예를 들어
\[
N^2=0\Rightarrow im(N)\subseteq ker(N)
\]
인데 계산이 이를 위반한다면 먼저 field/coordinate/implementation을 점검해야 합니다. 유사하게 비영 유한차원 module의 socle이 0으로 나오거나 rank-nullity가 깨지는 경우도 즉시 검증을 중단합니다.

**정정:** sanity invariant를 CI/실험의 선행 조건으로 취급.

---

## AP-007 — Unverified result promoted to theorem

**상태:** PROCESS FAILURE

실행 로그 없이 수치 결과를 PASS나 수학적 사실로 기록하지 않습니다. 특히 strong identification claims는 가능한 한 독립 계산 또는 certificate가 필요합니다.

**정정:** 각 실험에 goal/input/method/decision criterion/actual result/interpretation/open issue와 정확한 commit/run/job을 기록합니다.

---

## AP-008 — Stale historical dimension reused

**상태:** INVALID DATA SOURCE

과거 master record에 남은 `dim(R)_4=5`, `dim(Q_4)=55`는 현재 A3-4의 authoritative 계산과 충돌합니다. 현재 기준은
\[
\dim L_4=60,\quad\dim(R)_4=15,\quad\dim Q_4=45.
\]

**정정:** 최신 검증된 A3-4 계산과 정확한 commit/run을 authoritative source로 지정하고, 오래된 값은 역사적 기록으로만 취급합니다.

---

## 운영 원칙

새로운 오류가 발견되면 삭제하지 않고 이 문서에 추가합니다.

각 항목은 가능한 한 다음 네 가지를 포함합니다.

1. 무엇이 잘못되었는가
2. 왜 잘못되었는가
3. 어떤 결과가 무효가 되었는가
4. CI/SOP/검증 절차로 어떻게 재발을 막는가
