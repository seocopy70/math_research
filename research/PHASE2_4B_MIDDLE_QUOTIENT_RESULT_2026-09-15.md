# Phase 2-4B — 중간층 M = ker(N)/im(N) 계산 결과

## 1. 실행 정보

- Repository: `seocopy70/math_research`
- Workflow: `Phase 2-4B — middle quotient M=ker(N)/im(N)`
- GitHub Actions run: `34930410294`
- Job: `analyze-middle-quotient`
- Head commit: `3c72c1007716038055b209166d08c95ae21281d8`
- Python: 3.11.16
- NumPy: 2.4.6
- 실행 결과: **success**
- Artifact: `phase2-4B-result` (artifact ID `10381706035`)

## 2. 입력 구조

Phase 2-3에서 얻은 `W`와 비영 square-zero endomorphism `N`을 사용한다.

\[
\dim W=45,
\qquad
N^2=0,
\qquad
\operatorname{rank}N=10.
\]

따라서

\[
U=\operatorname{im}N,
\qquad
K=\ker N,
\qquad
M=K/U.
\]

계산 결과:

\[
\boxed{\dim U=10},
\]

\[
\boxed{\dim K=35},
\]

\[
\boxed{\dim M=35-10=25}.
\]

즉 현재 확정된 filtration은

\[
\boxed{0\subset U_{10}\subset K_{35}\subset W_{45}}.
\]

## 3. Quotient action

`Phase 2-4B` 코드는 `K/U`의 정확한 25차원 quotient 좌표계를 구성하고, Phase 2-3에서 사용한 5개의 `Sp_4(F_3)` 생성자 작용을 유도했다.

확인 결과:

- quotient generator matrices = 5
- quotient action matrix shape = `(25,25)`
- quotient action ranks = `[25,25,25,25,25]`

따라서 다섯 생성자의 quotient 작용은 모두 가역이다.

## 4. End_H(M) 계산

\[
H=Sp_4(\mathbb F_3)
\]

로 두고

\[
B=A_2+A_3+A_4+A_5
\]

를 구성했다.

Krylov 행렬

\[
[I,B,B^2,\ldots,B^{24}]
\]

의 rank는

\[
\boxed{25}
\]

이었다.

따라서 `B`는 cyclic하고, `B`의 centralizer를 이용하여 `End_H(M)` 계산을 625개의 미지수에서 25개의 미지수로 정확히 축소했다.

최종 결과:

\[
\boxed{\operatorname{rank}(E)=24},
\]

\[
\boxed{\dim_{\mathbb F_3}\operatorname{End}_H(M)=1}.
\]

즉

\[
\boxed{\operatorname{End}_H(M)=\mathbb F_3 I}.
\]

이것은 계산적으로 정확한 결과이다.

## 5. Cyclic-submodule probes

총 74개의 probe vector에 대해 각 vector가 생성하는 `H`-cyclic submodule의 차원을 계산했다.

결과:

\[
\boxed{\{25:74\}}
\]

즉

\[
\boxed{\text{74/74 probes generate all of }M}.
\]

따라서 관찰된 최소/최대 생성 차원 모두 25이다.

그러나 **이 유한한 probe 결과만으로 irreducibility를 증명했다고 주장하지 않는다.**

## 6. 현재 수학적 판정

확정된 사실:

1. \(\dim M=25\).
2. \(M\)은 정확한 `Sp_4(F_3)`-module이다.
3. \(\operatorname{End}_H(M)=\mathbb F_3\).
4. 74개의 결정론적/구성된 probe가 모두 전체 25차원 모듈을 생성한다.

따라서 `M`은 **매우 강하게 irreducible로 지지되지만**, 현재 기록에서는 아직 `M`의 irreducibility를 정리/증명으로 확정하지 않는다.

특히 modular representation theory에서는

\[
\operatorname{End}_H(M)=\mathbb F_3
\]

만으로 일반적인 irreducibility를 자동 결론내릴 수 없으므로, 다음 단계에서 독립적인 invariant-submodule 탐색 또는 충분조건을 갖춘 계산을 추가해야 한다.

## 7. 현재 전체 구조

현재까지의 계산 결과는

\[
0\subset U_{10}\subset K_{35}\subset W_{45}
\]

이며

\[
U=\operatorname{im}N
\]

은 Phase 2-4A에서 모든 59,048개의 nonzero vector를 검사하여 irreducible임이 완전 검증되었다.

또한

\[
W/K\cong U
\]

이다.

따라서 현재 가장 중요한 미확정 부분은 25차원 중간층

\[
\boxed{M=K/U}
\]

의 정확한 module structure이다.

## 8. 다음 단계

우선순위는 다음과 같다.

1. `M`의 proper nonzero `H`-invariant submodule 존재 여부를 정확히 탐색한다.
2. 가능하면 MeatAxe 계열 알고리즘 또는 그에 준하는 exact finite-field invariant-subspace algorithm을 사용한다.
3. irreducibility가 증명되면
   \[
   0\subset U_{10}\subset K_{35}\subset W_{45}
   \]
   에서 10–25–10의 세 층이 실제 단순층인지 확정한다.
4. 그 다음 이 모듈 구조가 canonical orientation을 복원하는 문제에 어떤 정보를 제공하는지 분석한다.

## 9. 재현성

GitHub Actions 로그에서 Phase 1, Phase 2-1, Phase 2-3의 검증도 함께 재실행되었으며 모두 통과했다. Phase 2-4B의 핵심 출력은 다음과 같다.

```text
dim W = 45
rank(N) = 10
dim U=im(N) = 10
dim K=ker(N) = 35
dim M=K/U = 25
quotient generator matrices = 5
quotient action matrix shape = (25, 25)
quotient action ranks = [25, 25, 25, 25, 25]
Krylov rank for B=A2+A3+A4+A5 on M = 25
End_H(M) rank = 24
dim End_H(M) = 1
probe count = 74
probe dimension distribution = {25: 74}
probe minimum dimension = 25
probe maximum dimension = 25
NOTE: finite probes do NOT establish irreducibility.
```

**결론:** Phase 2-4B의 계산은 성공적으로 완료되었으며, 45차원 `W`의 10–25–10 구조에서 25차원 중간층 `M`이 발견되었다. `End_H(M)=F_3`이라는 강한 결과와 74/74 cyclic generation이 확인되었지만, irreducibility는 다음 exact invariant-submodule 검증에서 최종 확정한다.
