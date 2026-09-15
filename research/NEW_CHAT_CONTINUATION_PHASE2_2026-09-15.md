# 새창 연구 이어가기 핵심 요약 — 2026-09-15

## 연구 주제
Demuškin 군의 filtration에서 canonical orientation을 복원할 수 있는가.

저장소: `seocopy70/math_research`
마스터 보존본: `research/MASTER_RESEARCH_RECORD.md`
마스터 기준 커밋: `7b79ec611fdcd201d9ef84c68aee187a7f8deb4c`

## 현재 기본 세팅

\[
G=\langle x_1,x_2,x_3,x_4\mid x_1^3[x_1,x_2][x_3,x_4]=1\rangle,
\]
with \([a,b]=a^{-1}b^{-1}ab\).

관계식에서
\[
x_2^{-1}x_1x_2=x_1[x_1,x_2]=x_1^{-2}[x_3,x_4]^{-1}.
\]
\(u=x_1^{-2}\), \(v=[x_3,x_4]^{-1}\)로 두면
\[
x_2^{-1}x_1x_2=uv.
\]

Hall–Petrescu degree-4 분석에서
\[
(uv)^3\equiv u^3v^3[v,u]^3[v,u,u][v,u,v]
\pmod{\text{weight}\ge5},
\]
이고 핵심 degree-4 항은 \([v,u,u]\)이다.

## 자유 Lie 대수와 target

\[
L=\mathbb L_{\mathbb F_3}(X_1,X_2,X_3,X_4),
\]
quadratic initial relation
\[
R=[X_1,X_2]+[X_3,X_4].
\]

Target:
\[
T=[[X_3,X_4],X_1],X_1,
\]
multidegree \((2,0,1,1)\).

Theorem A: \(T\notin(R)_4\), where \((R)_4=[R,L_2]\). 따라서 degree-4 quotient에서 \(T\neq0\).

또한 \(u=x_1^{-2}\), \(v=[x_3,x_4]^{-1}\)이므로
\[
\operatorname{in}_4([v,u,u])=-T,
\]
따라서 기존 계산에서 \(\lambda_T=-1=2\pmod3\).

## Phase 1 — 완료

목적: 단일 원소 \(T\)를 canonical object로 볼 수 있는지 genuine symplectic transformation으로 검사.

사용한 symplectic form:
\[
J=\begin{pmatrix}
0&1&0&0\\
-1&0&0&0\\
0&0&0&1\\
0&0&-1&0
\end{pmatrix}.
\]

사용한 genuine symplectic transvection:
\[
g=\begin{pmatrix}
1&0&0&0\\
1&1&0&0\\
0&0&1&0\\
0&0&0&1
\end{pmatrix}\pmod3,
\]
즉
\[
X_1\mapsto X_1+X_2,
\quad X_2,X_3,X_4\mapsto\text{고정}.
\]
실제로
\[
g^TJg=J.
\]

### 독립 검산 결과
Colab용 최소 Python 계산기로 독립 재현했고 다음이 모두 확인됨:

- \(\dim L_4=60\)
- \(\dim(R)_4=5\)
- \(\dim Q_4=55\)
- \(g^TJg=J\)
- \(\operatorname{rank}(R_4)=5\)
- \(\operatorname{rank}([R_4\mid gT-T])=6\)
- 따라서
  \[
  gT-T\notin(R)_4,
  \qquad [gT]\neq[T]\text{ in }Q_4.
  \]

명시적 coefficient certificate도 확인:
\[
[X_1X_3X_4X_2](gT-T)=2\pmod3,
\]
반면 이 coefficient는 모든 \([R,L_2]\) 생성자에서 0.
따라서 rank 계산과 독립적인 직접 증명도 성립.

### Phase 1의 정확한 결론

\[
\boxed{[gT]\neq[T]\text{ in }Q_4}
\]

즉 **단일 원소 \(T\)를 고정된 canonical object로 삼을 수 없다.**

주의: 이것만으로 \(\lambda_T\) 전체가 동일한 의미에서 좌표 의존적이라고 일반화하지 않는다. 이번 Phase 1이 직접 증명한 것은 \(T\)의 degree-4 quotient class가 symplectic transvection 아래 이동한다는 사실이다.

또한 이것은 orientation 자체가 filtration에 없다는 뜻이 아니다.

## 기존 Phase 2 관련 계산

\[
W=\langle Sp_4(\mathbb F_3)\cdot[T]\rangle\subset Q_4.
\]
기존 계산에서
\[
\dim W=45.
\]
그리고
\[
W^{Sp_4(\mathbb F_3)}=0,
\qquad
W_{Sp_4(\mathbb F_3)}=0.
\]
따라서 단순 invariant/coinvariant 방식으로 canonical scalar를 뽑는 것은 실패.

또한
\[
|Sp_4(\mathbb F_3)|=51840,
\]
이 군은 perfect이고 abelianization이 trivial이다. 따라서
\[
\operatorname{Hom}(Sp_4(\mathbb F_3),\mathbb F_3^\times)=0.
\]

중요한 caveat: 실제 Demuškin orientation은
\[
\chi:G\to\mathbb Z_3^\times,
\qquad
\mathbb Z_3^\times\simeq\mu_2\times(1+3\mathbb Z_3).
\]
현재의 mod-3 표현만으로 orientation 부재를 결론내릴 수 없다. 특히 pro-3 군에서 \(\mathbb F_3^\times\cong C_2\)로 가는 연속 character가 trivial인 것은 자연스러운 현상이다.

## Phase 2의 확정 방향

핵심 질문:

> 45차원 \(W\) 안에 orientation을 식별할 수 있는 고유한 representation-theoretic structure가 존재하는가?

### 권장 순서

1. \(W\)의 45차원 basis를 확정.
2. \(Sp_4(\mathbb F_3)\)의 몇 개 생성 transvection에 대한 \(45\times45\) 작용 행렬을 구축.
3. invariant subspace 탐색.
4. composition series / composition factors 탐색.
5. 1차원 submodule 또는 quotient 존재 여부 확인.
6. \(\operatorname{End}_H(W)\), \(H=Sp_4(\mathbb F_3)\), 즉 commutant/intertwiner algebra 계산.
7. multiplicity-1 irreducible factor 또는 유일하게 정의되는 invariant submodule이 있는지 조사.
8. 그 결과에 따라 modular representation theory로 확장.

### Central idempotent에 대한 결정

사용자 제안: \(\mathbb F_3[Sp_4(\mathbb F_3)]\) 군환의 central idempotent나 projection operator 활용.

현재 판단: **첫 도구로 바로 사용하지 않는다.** 이유는
\[
3\mid |Sp_4(\mathbb F_3)|,
\]
따라서 \(\mathbb F_3[Sp_4(\mathbb F_3)]\)는 semisimple이 아니며 Maschke 정리가 적용되지 않는다. 따라서 characteristic 0의 단순한 central primitive idempotent 분해를 그대로 사용할 수 없다.

대신 먼저 invariant-subspace lattice, composition series, commutant를 계산한다. 이후 필요하면 modular representation theory의 block decomposition, Brauer character, projective indecomposable module, Jacobson radical, primitive idempotent 등을 검토한다.

## Phase 2에서 가능한 결과의 해석

- \(W\) irreducible: canonical proper submodule 없음.
- 여러 composition factor가 반복: canonical factor 선택이 어려움.
- 특정 irreducible factor가 multiplicity 1: 매우 중요한 후보.
- 유일한 invariant submodule/maximal submodule 등이 존재: orientation 관련 canonical structure 후보.
- 아무 특수 구조도 없음: 강한 negative result이며 higher filtration / 3-adic lifting / Massey products / \(A_\infty\) 구조로 넘어갈 근거가 됨.

## 연구 방법론

앞으로도
\[
\boxed{\text{컴퓨터 발견}\to\text{명시적 certificate}\to\text{수학적 설명}\to\text{독립 검산}}
\]
프로토콜을 유지한다.

단순 프로그램 출력만으로 결론을 확정하지 않는다.

또한 연구 결과가 성공이든 실패든 다음 단계가 명확해지는 순간 기록한다. 기존 MASTER 보존본은 조용히 덮어쓰지 않고 research log 또는 별도 phase 파일에 추가한다.

## 새창에서 바로 이어갈 첫 문장

“Phase 1은 독립 Colab 검산까지 완료되었다. 이제 \(W\)의 45차원 \(Sp_4(\mathbb F_3)\)-module 구조를 invariant subspace → composition series → commutant 순서로 분석하자. characteristic 3이므로 central-idempotent 분해는 첫 도구로 쓰지 않는다.”
