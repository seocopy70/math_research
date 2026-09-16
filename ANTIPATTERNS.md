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

## AP-009 — CI sanity probe allowed to fail open through a pipeline

**상태:** IMPLEMENTATION FAILURE / CI GAP

B1-1의 GAP sanity step은 `printf ... | gap -q` 형태였는데 Bash의 기본 pipeline 상태가 마지막 명령의 exit code만 반영하는 환경에서는 GAP 내부 오류가 있어도 `printf`가 성공하면 step이 통과할 수 있습니다. 실제 run 35158243308에서 `GModuleByMats`의 field mismatch 오류가 출력되었지만 workflow step 자체는 success로 남았습니다.

**정정:** `set -euo pipefail`을 사용하고, `IdentityMat(1,F)`처럼 명시적으로 \(GF(3)\) field를 붙인 행렬을 `GModuleByMats`에 전달하도록 수정했습니다.

**재발 방지:** 외부 프로그램 sanity probe는 반드시 실패가 CI status에 전달되는지 확인하고, probe 자체의 성공 조건도 명시합니다.

---

## AP-010 — Inline GAP probe quoting / newline fragility

**상태:** SETUP / CI RELIABILITY FAILURE

B1-1-2의 GAP probe 수정 과정에서 `printf '... Print(...,"\\n") ...' | gap -q`처럼 Bash 문자열 안에 GAP 코드와 newline escape를 함께 넣는 방식이 다시 문제를 일으켰습니다. `\\n`의 해석 층위가 Bash/GAP 사이에서 어긋나면서 GAP에 실제 줄바꿈이 들어가 `Syntax error: String must not include <newline>`가 발생했습니다. run `35162932916`에서 확인되었고, 실제 B1-1-2 수학 계산은 실행되지 않았습니다.

**핵심:** 이것은 일회성 오타라기보다 **외부 인터프리터(GAP) 코드를 shell inline string으로 주입하는 구조 자체가 재발 가능한 CI 패턴**입니다.

**정정:** GAP sanity probe는 shell 문자열/`printf`/command substitution으로 작성하지 않습니다. 반드시 다음 형태를 사용합니다.

```bash
set -euo pipefail
cat > /tmp/gap_probe.g <<'GAP'
F := GF(3);;
A := IdentityMat(1,F);;
M := GModuleByMats([A],F);;
if not MTX.IsIrreducible(M) then
  Error("GAP MeatAxe sanity probe failed");
fi;
Print("GAP_PROBE_OK\n");
QUIT;
GAP
gap -q /tmp/gap_probe.g
```

또는 저장소의 `.g` 파일을 직접 실행합니다. **Bash → GAP 다중 해석층을 제거**하고 GAP 코드 자체를 heredoc/file로 검증합니다.

**재발 방지 프로토콜:**
1. CI에서 GAP 코드를 inline `printf`/`echo`/`$()` 문자열로 전달하지 않는다.
2. `GModuleByMats`를 사용하는 probe는 반드시 field를 명시한다: `GModuleByMats([...],F)`.
3. probe는 성공 조건을 명시적으로 출력하고, 실패 시 GAP가 nonzero exit를 내도록 `Error(...)`를 사용한다.
4. shell step에는 `set -euo pipefail`을 유지한다.
5. GAP probe를 새로 만들거나 수정하면 **probe 자체 실행을 먼저 확인한 뒤** 본 계산을 실행한다.
6. workflow audit에서 GAP sanity probe의 inline-string 패턴을 금지 대상으로 추가한다.

---

## 운영 원칙

새로운 오류가 발견되면 삭제하지 않고 이 문서에 추가합니다.

각 항목은 가능한 한 다음 네 가지를 포함합니다.

1. 무엇이 잘못되었는가
2. 왜 잘못되었는가
3. 어떤 결과가 무효가 되었는가
4. CI/SOP/검증 절차로 어떻게 재발을 막는가
