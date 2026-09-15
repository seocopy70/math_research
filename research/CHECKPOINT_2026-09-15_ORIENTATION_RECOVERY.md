# 연구 중간 체크포인트 — 2026-09-15

## 제목

**Demuškin 군의 filtration에서 canonical orientation을 복원할 수 있는가**

이 문서는 2026-09-15 현재 연구의 진행 상황과, 현재까지의 해석 및 향후 수학적 의미에 대한 설명을 보존하기 위한 중간 체크포인트이다. 이후 실제 연구가 예상대로 진행되는지, 또는 전혀 다른 구조가 나타나는지를 비교할 때 기준점으로 사용한다.

---

## 1. 연구 질문을 쉽게 표현하면

출발 질문은 다음과 같다.

> Demuškin 군의 presentation에서 생성원과 좌표를 미리 지정하지 않고, 군의 filtration과 그 자연스러운 대칭만 관찰하더라도 orientation에 대응하는 구조를 다시 복원할 수 있는가?

쉽게 비유하면, 사진에서 화살표를 지운 뒤 사진 자체의 내부 구조만 보고 원래 화살표의 방향을 복원할 수 있는가를 묻는 것과 같다.

중요한 점은 특정 degree-4 원소 하나를 orientation 자체라고 주장하는 것이 아니라, 그 원소가 자연스러운 대칭 아래에서 만들어내는 전체 구조가 orientation 정보를 보존하는지를 조사한다는 것이다.

---

## 2. 지금까지의 핵심 진행

대상 군은

\[
G=\langle x_1,x_2,x_3,x_4\mid x_1^3[x_1,x_2][x_3,x_4]=1\rangle
\]

이고, associated graded의 관련 자유 Lie algebra는

\[
L=\mathbb L_{\mathbb F_3}(X_1,X_2,X_3,X_4)
\]

이다.

초기 quadratic relation은

\[
R=[X_1,X_2]+[X_3,X_4]
\]

이다.

Degree 4에서 orientation 후보로 조사한 원소는

\[
T=[[X_3,X_4],X_1],X_1.
\]

그러나 symplectic coordinate change를 적용한 결과

\[
[gT]\neq[T]\quad\text{in }Q_4=L_4/(R)_4
\]

임을 정확한 선형대수 계산으로 확인했다.

따라서 **T 자체는 canonical object가 아니다.**

이것은 실패가 아니라 연구 질문을 더 정확하게 바꾸는 계기가 되었다.

---

## 3. T 하나가 아니라 전체 대칭 orbit를 조사

\[
W=\langle Sp_4(\mathbb F_3)\cdot[T]\rangle
\]

를 정의하고 전체 표현론적 구조를 조사했다.

확인된 결과:

\[
\dim W=45,
\qquad W^{Sp_4(\mathbb F_3)}=0.
\]

즉 W 안에는 모든 자연스러운 symplectic 대칭에 의해 고정되는 단순한 하나의 vector가 없다.

따라서 orientation이 W 안의 한 canonical vector로 존재한다는 단순한 그림은 성립하지 않는다.

---

## 4. W 안에서 발견된 핵심 구조

정확한 modular representation 계산에서

\[
\dim_{\mathbb F_3}\operatorname{End}_H(W)=2,
\qquad H=Sp_4(\mathbb F_3)
\]

이고, 비스칼라 endomorphism N을 선택하면

\[
N^2=0,
\qquad \operatorname{rank}N=10.
\]

따라서

\[
0\subset U=\operatorname{im}N\subset K=\ker N\subset W
\]

이라는 구조가 생기며

\[
\dim U=10,\qquad \dim K=35,\qquad \dim W=45.
\]

또한

\[
W/K\cong U
\]

이므로 구조는

\[
\boxed{10-25-10}
\]

으로 정리된다.

즉 가운데 quotient

\[
M=K/U
\]

는 25차원이다.

---

## 5. 10차원 층은 실제 기약임을 증명

\(U=\operatorname{im}N\)에 대해서는 단순한 무작위 표본 검사가 아니라 모든 비영벡터를 검사했다.

\[
3^{10}-1=59048
\]

개의 모든 nonzero vector에 대해 cyclic submodule의 차원을 계산했고, 전부 10이었다.

따라서

\[
\boxed{U\text{는 irreducible }\mathbb F_3[Sp_4(\mathbb F_3)]\text{-module}}
\]

임을 exhaustive finite computation으로 확인했다.

또한

\[
W/K\cong U
\]

이므로 위쪽 10차원 층도 같은 simple module이다.

---

## 6. 현재 핵심 미결 문제: 25차원 중간층 M

\[
M=K/U,
\qquad \dim M=25.
\]

정확한 계산에서

\[
\operatorname{End}_H(M)=\mathbb F_3
\]

가 나왔고, 준비된 74개의 deterministic cyclic probes도 모두 25차원을 생성했다.

그러나

\[
\operatorname{End}_H(M)=\mathbb F_3
\]

만으로 M의 기약성을 단정하지 않는다.

이유는

\[
\operatorname{char}\mathbb F_3=3\mid |Sp_4(\mathbb F_3)|=51840
\]

인 modular representation 환경이기 때문이다. 이 환경에서는 Schur 보조정리의 역방향을 사용할 수 없다.

따라서 현재는 **강한 증거이지만 아직 기약성 증명은 아니다.**

---

## 7. 현재 실행 중인 Phase 2-4C

현재는

\[
\mathcal A=\mathbb F_3[A_1,\ldots,A_5]\subseteq M_{25}(\mathbb F_3)
\]

라는 생성 행렬대수의 차원을 정확히 계산하고 있다.

25차원 공간의 전체 행렬대수 차원은

\[
25^2=625
\]

이다.

따라서

\[
\dim\mathcal A=625
\]

가 나오면

\[
\mathcal A=M_{25}(\mathbb F_3)
\]

이므로 M의 irreducibility, 더 강하게 absolute irreducibility를 증명할 수 있다.

반대로

\[
\dim\mathcal A<625
\]

가 나와도 즉시 가약이라고 결론내리지 않는다. 그 경우 MeatAxe 방식의 invariant-submodule 탐색으로 넘어가 실제 proper invariant submodule의 존재 또는 부재를 결정한다.

---

## 8. 앞으로의 논리적 분기

### 경우 A: \(\dim\mathcal A=625\)

\[
\mathcal A=M_{25}(\mathbb F_3)
\]

을 얻고 M의 절대기약성을 확정한다.

### 경우 B: \(\dim\mathcal A<625\)

다음 순서로 진행한다.

1. 무작위/결정론적 cyclic-submodule 탐색으로 후보 구조를 진단한다.
2. MeatAxe식 splitter 또는 primary decomposition을 이용해 후보 invariant subspace를 찾는다.
3. 찾은 공간 \(V\)에 대해 모든 생성원에 대해
   \[
   A_iV\subseteq V
   \]
   를 정확히 검사한다.
4. 실제 proper invariant submodule이면 가약성을 증명한다.
5. 필요하면 quotient에 다시 같은 분석을 적용하여 M의 정확한 filtration을 결정한다.

무작위 탐색은 증명 자체가 아니라 구조 발견을 위한 진단 수단으로 취급한다.

---

## 9. 현재 연구의 가장 쉬운 전체 그림

\[
\text{Demuškin 군}
\rightarrow
\text{filtration}
\rightarrow
\text{degree-4 후보 }T
\rightarrow
Sp_4(\mathbb F_3)\text{-orbit}
\rightarrow
W(45)
\rightarrow
N^2=0
\rightarrow
10-25-10
\rightarrow
M(25)\text{의 정확한 구조}
\]

여기까지는 실제 계산으로 상당 부분 확정되었다.

최종적으로 돌아가야 할 질문은

\[
\boxed{\text{filtration 자체에서 orientation을 canonical하게 복원할 수 있는가?}}
\]

이다.

---

## 10. 만약 최종 canonical recovery까지 성공한다면

그 의미는 단순히 특정 presentation에서 orientation을 읽어낼 수 있다는 것이 아니다.

보다 강한 명제는 다음과 같다.

> Demuškin 군의 orientation은 생성원이나 presentation에 붙어 있는 외부적 표식이 아니라, 군의 filtration과 그 자연스러운 대칭 구조에 내재한 intrinsic invariant로부터 canonical하게 복원될 수 있다.

즉

\[
\text{presentation-dependent data}
\longrightarrow
\text{intrinsic group-theoretic data}
\]

라는 전환이 일어난다.

가능하다면 이는 Demuškin 군의 duality/orientation 구조를 associated graded 또는 representation-theoretic 관점에서 이해하는 새로운 방법이 될 수 있다.

더 일반적인 Demuškin 군으로 확장된다면 filtration의 representation-theoretic 구조로부터 orientation을 복원하는 일반 정리로 발전할 가능성도 있다.

Demuškin 군이 local Galois theory의 중요한 예들과 연결된다는 점 때문에 장기적으로는 Galois-theoretic orientation data를 graded Lie structure에서 읽는 방향과도 연결될 가능성이 있다. 단, 이 마지막 연결은 별도의 일반화와 증명이 필요하며 현재 결과에서 자동으로 따라오는 결론은 아니다.

---

## 11. 현재 시점에서의 냉정한 평가

현재는 **orientation recovery를 증명한 단계가 아니다.**

현재까지 확정된 것은 다음에 가깝다.

> 특정 degree-4 원소 T 자체는 canonical하지 않지만, 그 전체 symplectic orbit가 생성하는 45차원 modular representation에는 비자명한 10-25-10 구조가 존재하고, 그 아래 10차원 층은 irreducible임이 증명되었다. 가운데 25차원 층의 정확한 표현론적 구조를 현재 결정하고 있다.

그리고 최종적으로는 이 구조가 실제 Demuškin orientation과 어떻게 연결되는지를 별도의 canonicality/functoriality 논증으로 증명해야 한다.

---

## 12. 이 문서의 역할

이 기록은 결과를 미리 정해놓은 결론문이 아니다.

앞으로 연구가

- 예상대로 25차원 층이 기약으로 판명되는지,
- 예상과 달리 더 깊은 submodule 구조가 발견되는지,
- 10-25-10 구조가 orientation recovery와 실제로 연결되는지,
- 또는 현재의 가설 자체를 수정해야 하는지

를 나중에 되돌아볼 수 있도록 **2026-09-15 현재의 중간 체크포인트**를 보존한다.

따라서 이후 결과가 예상과 달라도 이 문서의 현재 표현을 소급하여 바꾸지 않고, 새로운 결과를 별도의 기록으로 추가하는 것을 원칙으로 한다.
