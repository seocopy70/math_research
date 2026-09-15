# 연구 방향 변화와 현재까지의 발견

## 1. 원래 질문

연구의 출발점은 다음 질문이었다.

> Demuškin 군의 filtration만으로 canonical orientation을 복원할 수 있는가?

구체적으로
\[
G=\langle x_1,x_2,x_3,x_4\mid x_1^3[x_1,x_2][x_3,x_4]=1\rangle
\]
에서 filtration의 저차 층, 특히 degree-4 정보가 Demuškin orientation의 흔적을 얼마나 보존하는지 조사하는 것이 목표였다.

핵심 관심은 '관계식에 orientation 정보가 들어 있다'는 사실과 '그 정보가 filtration의 군론적/표현론적 불변량만으로 다시 복원 가능한가'를 구별하는 데 있다.

---

## 2. 처음 기대했던 경로

초기에는 비교적 직접적인 경로를 기대했다.

1. Demuškin 관계식에서 특정 degree-4 class를 추출한다.
2. 그 class가 symplectic automorphism 아래에서 변하는지 확인한다.
3. 변한다면 filtration만으로 canonical orientation을 복원하기 어렵다는 방향의 obstruction을 얻는다.
4. 변하지 않는 구조 또는 orientation을 표시하는 별도의 canonical object가 있는지를 찾는다.

이 단계에서 핵심 target은
\[
T=[[[X_3,X_4],X_1],X_1]
\]
이고, quadratic relation
\[
R=[X_1,X_2]+[X_3,X_4]
\]
에 대해
\[
Q_4=L_4/(R)_4
\]
에서 T의 class를 조사했다.

---

## 3. 예상했던 첫 결과: degree-4 obstruction

계산과 독립 검산을 통해
\[
\dim L_4=60,\quad \dim(R)_4=5,\quad \dim Q_4=55
\]
이고
\[
T\notin(R)_4
\]
를 확인했다.

또한 genuine symplectic transvection g에 대해
\[
[gT]\ne[T]\quad\text{in }Q_4
\]
를 확인했다. 실제 rank certificate는
\[
\operatorname{rank}(R_4)=5,
\qquad
\operatorname{rank}[R_4\mid gT-T]=6
\]
였다.

따라서 적어도 이 특정 degree-4 class는 canonical symplectic invariant가 아니다.

이는 원래 질문에 대한 중요한 음의 신호였지만, 이것만으로 'orientation이 filtration에서 복원 불가능하다'고 결론낼 수는 없었다. 하나의 class가 invariant가 아니라는 것과 전체 filtration이 orientation을 결정하지 못한다는 것은 다른 주장이다.

---

## 4. 연구가 예상보다 크게 확장된 지점

여기서 연구 질문이 다음과 같이 한 단계 확장되었다.

\[
W=\langle Sp_4(\mathbb F_3)\cdot[T]\rangle\subset Q_4
\]
를 만들고, 단순히 T 하나의 변환만 보는 대신 T가 생성하는 전체 symplectic representation의 구조를 조사하기로 했다.

실제 계산에서
\[
\boxed{\dim W=45}
\]
를 얻었고,
\[
W^{Sp_4(\mathbb F_3)}=0,
\qquad
W_{Sp_4(\mathbb F_3)}=0
\]
도 확인했다.

즉 'orientation을 나타낼 것 같은 한 개의 canonical vector'를 찾는 문제에서 '그 정보가 45차원 모듈 안에서 어떤 representation-theoretic 구조로 저장되는가'라는 문제로 이동했다.

---

## 5. 가장 예상 밖이었던 발견: endomorphism algebra

Phase 2-3에서
\[
\dim\operatorname{End}_H(W)=2
\]
를 얻었다. 더 나아가 비스칼라 endomorphism N에 대해
\[
N^2=0,\qquad \operatorname{rank}N=10
\]
이었다.

따라서
\[
U=\operatorname{im}N,\quad K=\ker N
\]
에 대해
\[
\dim U=10,\qquad \dim K=35
\]
이고
\[
0\subsetneq U\subsetneq K\subsetneq W
\]
라는 자연스러운 filtration이 생겼다.

이는 처음부터 예상했던 결과가 아니었다. 특히
\[
\operatorname{End}_H(W)\cong \mathbb F_3[\varepsilon]/(\varepsilon^2)
\]
형태가 나타난 것은 단순한 비불변성 계산을 넘어 W 자체가 characteristic 3에서 매우 구체적인 비완전가약 구조를 가진다는 것을 보여주는 중요한 발견이다.

또한 W는 reducible이지만 indecomposable인 것으로 확인되었다.

---

## 6. 또 하나의 예상 밖 발견: Weyl module과 정확히 맞아떨어지는 구조

중간층
\[
M=K/U
\]
의 차원은
\[
\dim M=25
\]
이다.

독립적인 WeylModules 계산에서는 characteristic 3의 \(Sp_4\) Weyl module
\[
\Delta(2,1)
\]
이
\[
0\to L(2,0)\to\Delta(2,1)\to L(2,1)\to0
\]
형태의 구조를 가지며
\[
\dim L(2,0)=10,\qquad \dim L(2,1)=25
\]
임을 확인했다.

특히
\[
\Delta(2,0)=L(2,0)
\]
도 직접 확인되었다.

이 때문에 다음과 같은 강한 가설이 자연스럽게 등장했다.
\[
\boxed{W\stackrel{?}{\cong}T(2,1)}
\]
또는 적어도 W의 구조가 characteristic 3의 \((2,1)\) Weyl/tilting 구조와 깊은 관계를 가진다는 가설이다.

중요하게도 이 단계에서는 '차원과 층의 모양이 같으니 같을 것'이라고 주장하지 않았다.

---

## 7. A단계에서 실제로 증명된 것

\[
U=\operatorname{im}N
\]
에 대해 동일한 다섯 개의 symplectic transvection을 사용하여 자연 4차원 모듈의 대칭제곱
\[
\operatorname{Sym}^2(V)
\]
을 독립 모델로 구성했다.

동시 intertwiner 방정식
\[
PA_i^U=A_i^{\operatorname{Sym}^2(V)}P
\]
을 실제로 풀어
\[
\dim\operatorname{Hom}_H(U,L(2,0))=1
\]
이고 full-rank intertwiner가 존재함을 확인했다.

따라서
\[
\boxed{U\cong L(2,0)=\operatorname{Sym}^2(V)}
\]
가 실제 계산 certificate를 갖춘 상태가 되었다.

이것은 단순한 '10차원이므로 L(2,0)'이 아니라, 같은 H의 생성자에 대한 실제 행렬을 비교한 결과라는 점이 중요하다.

---

## 8. 현재 B단계의 의미

현재
\[
M=K/U
\]
에 대해 실제로
\[
\dim M=25,
\qquad
\dim\operatorname{End}_H(M)=1
\]
을 계산했고, 여러 cyclic-span 검사를 통해 25차원 구조가 매우 강하게 cyclic임을 확인했다.

그러나 이것만으로
\[
M\cong L(2,1)
\]
을 선언하지 않았다.

현재 진행 중인 Phase 2-8에서는 ATLAS의 characteristic-3, dimension-25 representation을 독립 모델로 가져와 동일한 다섯 개의 \(Sp_4(\mathbb F_3)\) transvection을 대응시킨 뒤
\[
PA_i^M=A_i^{L(2,1)}P
\]
를 직접 풀고 있다.

full-rank
\[
\operatorname{rank}P=25
\]
가 확인되면
\[
\boxed{M\cong L(2,1)}
\]
를 certificate와 함께 확정한다.

---

## 9. '원래 연구'와 '현재 연구'의 차이

### 원래 연구

질문은 essentially 이었다.

> filtration만 보고 Demuškin orientation을 복원할 수 있는가?

따라서 주된 목표는 orientation의 **식별 가능성/불가능성**이었다.

### 현재 연구

현재는 그 질문을 바로 공격하기보다, filtration에서 실제로 나타나는 representation-theoretic 정보를 먼저 해부하고 있다.

즉
\[
\text{orientation 복원 문제}
\]
를
\[
\text{저차 filtration의 canonical representation 구조는 무엇인가?}
\]
라는 중간 문제로 분해했다.

그 결과
\[
T\to W\to End_H(W)\to U\to M
\]
라는 구조적 사슬이 생겼다.

이것은 연구가 주제에서 벗어난 것이 아니라, 원래 질문에 답하기 위해 필요한 '내부 구조 지도'를 만드는 과정이다.

---

## 10. 기대했던 결과와 기대하지 않았던 결과

### 처음부터 어느 정도 기대했던 것

- 특정 degree-4 class가 symplectic 변환에 대해 비불변일 가능성.
- 따라서 naive한 canonical orientation candidate가 실패할 가능성.
- 그 실패를 rank certificate로 엄밀하게 보일 가능성.

### 처음에는 기대하지 않았던 것

1. T의 orbit span이 정확히 45차원이 되는 것.
2. 그 45차원 모듈의 invariant와 coinvariant가 모두 0인 것.
3. End_H(W)가 정확히 2차원인 것.
4. 그 안에서 square-zero rank-10 endomorphism N이 자연스럽게 나타난 것.
5. 그 결과로 정확한 10-35-25 filtration
   \[
   0<U<K<W
   \]
   이 생긴 것.
6. 10차원 층이 정확히 \(L(2,0)\cong Sym^2(V)\)와 일치한 것.
7. 25차원 중간층이 \(L(2,1)\)일 가능성이 매우 강하게 떠오른 것.
8. 전체 W가 characteristic 3의 tilting/Weyl-module 구조와 닮은 형태를 보이는 것.

이 중 특히 3~7은 원래 질문에서 직접 예상한 산출물이 아니라 계산 과정에서 구조가 스스로 드러난 것이다.

---

## 11. 현재 가장 주목할 만한 새로운 시도

가장 주목할 만한 방법론적 변화는 'orientation을 직접 찾으려는 것'에서 'orientation을 포함할 수 있는 filtration의 representation category를 먼저 완전히 해부하는 것'으로 바뀐 점이다.

특히
\[
\operatorname{End}_H(W)
\]
를 먼저 계산하고 그 안의 nilpotent endomorphism N을 이용해
\[
\operatorname{im}N,\ker N,\ker N/\operatorname{im}N
\]
라는 canonical-looking 층을 얻은 것은 중요한 연구 아이디어이다.

이것이 정말 canonical인지, 즉 생성자 선택이나 target T의 선택에 의존하지 않는지는 아직 미해결이다. 따라서 현재는 '발견된 구조'이지 '최종 canonical invariant'라고 부르지 않는다.

---

## 12. 현재 연구의 의미

현재 단계에서 원래 질문에 대한 최종 답은 아직 없다.

그러나 연구는 단순한 계산 실험을 넘어 다음 수준까지 진행되었다.

\[
\boxed{
\text{Demuškin relation}
\to Q_4
\to T
\to W\;(45)
\to End_H(W)\;(2)
\to N
\to U\;(10)
\to M\;(25)
}
\]

그리고 A단계에서
\[
U\cong L(2,0)
\]
까지 실제 intertwiner certificate가 확보되었다.

따라서 현재 가장 중요한 질문은 단순히 'T가 invariant인가?'가 아니라,

> filtration에서 자연스럽게 생성되는 representation-theoretic 구조가 Demuškin orientation과 어떤 관계를 갖는가?

이다.

B단계에서 \(M\cong L(2,1)\)까지 확정되면, 다음 핵심 문제는
\[
0\to L(2,0)\to W/U\to L(2,1)\to0
\]
및 전체 W의 extension class를 분석하여 W가 실제로 \(T(2,1)\)와 동형인지, 그리고 그 구조가 filtration에서 canonical한 것인지 검증하는 것이다.

그 후에야 이 representation structure가 original Demuškin orientation을 복원하거나, 반대로 orientation을 잃어버린 filtration에서도 반드시 남는 비방향적 구조인지 판단할 수 있다.

---

## 기록 원칙

이 문서는 연구의 방향 변화와 발견의 의미를 기록하는 해설 기록이다. 최종 결론으로 취급하지 않는다.

특히 다음을 구분한다.

- 계산으로 확인된 사실
- 강한 구조적 가설
- 문헌으로 뒷받침되는 representation-theoretic 사실
- 아직 증명되지 않은 canonicality 및 orientation 복원 주장

연구의 기본 검증 원칙은 계속 유지한다.

\[
\boxed{\text{컴퓨터 발견}\to\text{명시적 certificate}\to\text{수학적 설명}\to\text{독립 검산}}
\]
