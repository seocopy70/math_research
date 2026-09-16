# AI Context Brief — Demuškin / A3-4 Research

> 목적: 새 AI 세션이나 공동 연구자가 수학적·계산적 맥락을 빠르게 이어받을 수 있도록 하는 짧은 기준 문서입니다.

## 1. 연구 목표

대상은

\[
G=\langle x_1,x_2,x_3,x_4\mid x_1^3[x_1,x_2][x_3,x_4]=1\rangle
\]

인 Demuškin 군입니다. 핵심 질문은 Zassenhaus/graded Lie 구조와 유한체 \(\mathbb F_3\)의 표현론적 구조에서 관계식의 정보, 특히 \(q\) 및 orientation 관련 정보를 얼마나 **정준적으로 복원할 수 있는가**입니다.

현재 연구는 하나의 수치값을 맞히는 것보다, 재현 가능한 중간 구조와 독립 검증을 확보하는 데 초점을 둡니다.

## 2. 권위 있는 기본 규약

- 모든 유한체 계산: \(\mathbb F_3\).
- Python의 권위적 행렬 작용: **column action** \(v\mapsto Av\).
- GAP `GModuleByMats`: **row vectors/right action**.
- 따라서 Python 행렬을 GAP에 넘길 때는 반드시 transpose.
- 이 transpose 규칙은 생성자뿐 아니라 endomorphism \(N\), kernel/image/socle의 기저에도 적용.
- 부분공간 equality는 차원만으로 판단하지 않고 동일 좌표계에서 span/rank로 직접 확인.
- \(\mathbb F_3\) rank는 검증된 `rank3()`를 재사용. `numpy.linalg.matrix_rank`, `numpy.linalg.det`는 금지.
- 필수 sanity invariant가 깨지면 수학적 발견으로 해석하지 말고 먼저 **INVALID TEST**로 분류.

세부 규약은 `research/03_CONVENTIONS_AND_IMPLEMENTATION.md`가 권위 문서입니다.

## 3. 핵심 수학적 기준선

\[
R=[X_1,X_2]+[X_3,X_4],\qquad (R)_4=[R,L_2].
\]

현재 권위 차원:

\[
\dim L_4=60,\quad \dim(R)_4=15,\quad \dim Q_4=45.
\]

목표 원소:

\[
T=[[X_3,X_4],X_1],X_1],
\]

이며 \(T\notin(R)_4\), 따라서 degree 4에서 살아남습니다.

Sp\(_4(\mathbb F_3)\) 기준:

- \(|Sp_4(\mathbb F_3)|=51840\)
- 40개 symplectic transvection으로 생성
- 현재 사용 중인 \(J\)는
\[
\begin{pmatrix}0&1&0&0\\-1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix}.
\]

## 4. q 민감도 기준선

독립 Magnus 계산에서

\[
\operatorname{in}_3(s_3)-\operatorname{in}_3(s_\infty)=X_1^{[3]}.
\]

또

\[
[X_1^{[3]},X_1]=0,
\qquad
[X_1^{[3]},X_2]\ne0.
\]

정확한 degree-4 quotient 계산에서

\[
\operatorname{rank}((R)_4)=5,
\quad\operatorname{rank}((R)_4+[X_1^{[3]},X_2])=6.
\]

따라서 현재까지는 degree 3에서 finite/infinite \(q\)를 구별하고, degree 4에서 구조가 증폭되며, 정확한 \(q\) 크기 판별은 degree 9가 필요한 계층으로 이해합니다.

## 5. A3-4 module 기준선

현재 핵심 결과:

- \(\dim I=35,\ \dim K=35\).
- \(B/A\not\cong_H K\), 그러나 composition factors는 양쪽 모두 \([10,1],[25,1]\).
- 둘 다 Loewy length 2이고 indecomposable.
- 유일한 nonzero intertwiner \(Q:B/A\to K\)의 rank는 10.
- 정확한 Loewy 정렬:
\[
\ker Q=Soc(B/A),\qquad \operatorname{im}Q=Soc(K).
\]
- extension 방향은
\[
[B/A]\in Ext^1_H(S_{10},S_{25}),\qquad
[K]\in Ext^1_H(S_{25},S_{10}),
\]
각각 non-split임만 기록되어 있습니다. Ext 차원이나 유일성은 아직 주장하지 않습니다.

## 6. 현재 연구 위치: B1-1

목표는
\[
\mathcal C(W)=\{M\le L_4:M\text{ is }H\text{-stable},\dim M=45,\dim(M\cap W)=35\}
\]
에서 \(W_d\)가 구조적으로 유일하게 복원되는지 조사하는 것입니다.

현재 분해 관점은
\[
M\cap W=I',\quad \dim I'=35,
\qquad \dim(M/I')=10.
\]

따라서 먼저 45차원 \(W\)의 35차원 H-submodule 구조를 조사하고, 그 다음 45차원 H-stable lift의 유일성을 조사합니다.

중요: `End_H(W)`가 2차원이고 \(N^2=0\), rank \(N=10\)이라는 사실만으로 W가 uniserial이라고 가정하지 않습니다.

현재 B1-1의 직접적인 socle 비교에서는 GAP row-action에 맞는 \(N^T\)를 사용해야 합니다. 과거 Python `numpy.linalg.matrix_rank(N)`의 출력 24는 실수체 rank라서 무효입니다. 올바른 \(\mathbb F_3\) rank는 10이며, 이후 계산은 `rank3()`와 GAP \(GF(3)\) 계산을 기준으로 합니다.

## 7. CI 신뢰성 상태

2026-09-17에 저장소 전체의 GitHub Actions workflow 73개를 대상으로 shell pipeline audit를 수행했습니다.

- `| gap`, `| python`, `| bash`, `| sh` 계열 위험 pipeline: **2건**
- 대상: A3-4-20R, B1-1 GAP sanity probe
- 두 건 모두 현재는 `set -euo pipefail`로 보호됨
- 다른 workflow에서 같은 패턴은 발견되지 않음
- audit run: **35160653591**, job **105010389018**, 결과 **PASS**

따라서 AP-009의 저장소 전체 감사 결과는 **PASS**입니다. 다만 과거 fail-open 구조로 실행된 A3-4-20R/B1-1의 오래된 sanity-probe 증거는 `success` 표시만으로 충분한 인증으로 간주하지 않습니다. 해당 계산 자체를 자동으로 무효화하는 것은 아니며, 실제 수학 계산이 그 probe의 성공에 의존했는지를 따로 판단합니다.

새로운 pipeline은 `.github/workflows/workflow-pipeline-audit.yml`이 차단합니다.

## 8. 연구 절차

항상 다음 순서를 지킵니다.

1. 수학적 주장 명시
2. 계산 설계 및 좌표/체 규약 명시
3. 구현
4. 실제 실행
5. 로그 및 sanity invariant 검사
6. 독립 검증
7. GitHub 기록
8. 다음 단계로 이동

실행 로그가 없는 결과는 공식 PASS로 부르지 않습니다.

## 9. 결과 분류

모든 실험은 다음 중 하나로 분류합니다.

\[
\boxed{\text{SETUP FAILURE}\to\text{IMPLEMENTATION FAILURE}\to\text{INVALID TEST}\to\text{MATHEMATICAL FAILURE}\to\text{PASS}}
\]

단, 이는 순차적 진행을 뜻하는 것이 아니라 실패 원인의 종류를 구분하는 공통 분류 체계입니다.

## 10. 새 세션에서 반드시 확인할 것

- 현재 `main`의 최신 commit
- 해당 실험의 정확한 script/workflow/commit
- GitHub Actions 실제 run/job 결과
- coordinate convention과 transpose 여부
- \(\mathbb F_3\) rank 사용 여부
- sanity invariant 통과 여부
- 이전의 INVALID 결과를 재사용하고 있지 않은지
- workflow pipeline audit가 PASS인지

**핵심 원칙:** AI가 계산을 대신하는 것이 아니라, 사람이 통제하는 재현 가능한 수학 연구 인프라 위에서 AI를 연구 보조자로 사용합니다.
