# Phase 2-2 — W의 submodule 구조 1차 검산

Date: 2026-09-15

## 목적

Phase 2-1에서 확인한

\[
W=\langle Sp_4(\mathbb F_3)\cdot[T]\rangle,\qquad \dim W=45
\]

및

\[
W^{Sp_4(\mathbb F_3)}=0
\]

을 바탕으로, 다음 단계인 submodule 구조 탐색에 들어가기 전 45차원 W가 실제로 생성자들에 의해 얼마나 강하게 연결되는지 검산한다.

## 고정된 계산 설정

\[
J=\begin{pmatrix}
0&1&0&0\\
-1&0&0&0\\
0&0&0&1\\
0&0&-1&0
\end{pmatrix}\pmod 3.
\]

사용한 5개 symplectic transvection의 벡터는

\[
e_1,e_2,e_3,e_4,e_1+e_3.
\]

각 transvection은

\[
t_v=I+v(Jv)^T\pmod3
\]

으로 정의하였다.

Degree-4 associative-word 모델에서 R_4의 독립 기저 5개를 먼저 선택하고, T의 생성자 orbit을 추가하여 quotient W의 기저를 구성하였다.

## 계산 과정

1. 자유 associative algebra의 길이 4 단어 256개를 표준 좌표로 사용.
2. \(R_4=[R,L_2]\)의 rank를 5로 계산하고 독립한 5개 열을 quotient 기준으로 사용.
3. T에서 시작하여 5개 transvection의 작용을 반복 적용하고, \([R_4\mid W]\)의 rank 증가 여부로 W의 독립 기저를 유지.
4. 결과:

\[
\operatorname{rank}[R_4\mid W]=50,
\]

따라서

\[
\boxed{\dim W=50-5=45}.
\]

5. 50개의 독립적인 associative-word 좌표 행을 골라 좌표변환을 구성하고, 각 generator의 W 위 작용행렬 \(A_i\in M_{45}(\mathbb F_3)\)를 계산.
6. 다음 invariant-space 행렬을 구성:

\[
M=\begin{pmatrix}
A_1-I\\
A_2-I\\
A_3-I\\
A_4-I\\
A_5-I
\end{pmatrix}.
\]

실제 계산 결과:

\[
\operatorname{rank}_{\mathbb F_3}M=45,
\]

따라서

\[
\boxed{\dim W^{Sp_4(\mathbb F_3)}=0}.
\]

## Cyclic-submodule probe

W의 좌표기저 벡터 45개 중 대표적으로 다음 index를 선택하여 각각이 생성하는 cyclic submodule을 계산했다:

\[
0,1,2,3,4,5,10,20,30,40,44.
\]

각 벡터 v에 대해

\[
\langle H\cdot v\rangle
\]

을 5개 생성자 작용만으로 닫고 rank를 계산했다.

모든 선택점에서 결과는

\[
\boxed{\dim\langle H\cdot v\rangle=45}.
\]

즉 적어도 이 11개의 독립적인 방향에서는 하나의 벡터만으로 W 전체가 생성된다.

## 현재 해석

이 결과는 W가 매우 강하게 연결된 H-module임을 보여준다. 특히 W 내부에 작은 invariant submodule이 쉽게 드러나는 상황은 아니다.

그러나 이것만으로

\[
\boxed{W\text{가 irreducible이다}}
\]

라고 결론내려서는 안 된다. 임의의 nonzero vector 전체에 대한 exhaustive 검사가 아니기 때문이다. Cyclic probe는 강한 계산적 증거이지 irreducibility의 최종 증명은 아니다.

## 다음 단계

다음으로는 다음 중 더 엄밀한 방향을 진행한다.

1. H-module endomorphism algebra
\[
\operatorname{End}_H(W)=\{X\in M_{45}(\mathbb F_3):XA_i=A_iX\ \forall i\}
\]
을 계산한다.

2. 가능하면 invariant subspace lattice 또는 maximal submodule 탐색을 수행한다.

3. composition factors를 계산하여 W가 irreducible인지, 혹은 비자명한 extension인지 판별한다.

### 주의

이번 기록에는 실제 실행된 계산 결과만 기록한다. End_H(W)의 대규모 선형계산은 이번 실행에서 시간 제한으로 완료되지 않았으므로 결과를 추정하지 않는다.
