# Track B A3-3 — degree-4 bridge preliminary result

날짜: 2026-09-16

## 1. 출발 class

A3-2에서 얻은 degree-3 correction은
\[
A_3=X_1^{[3]}-[[X_3,X_4],X_2].
\]

이를 degree 4로 올릴 수 있는 가장 직접적인 Lie bracket을 점검한다.

## 2. multidegree 검사

첫 성분은
\[
X_1^{[3]}
\]
으로 multidegree
\[
(3,0,0,0)
\]
이다.

둘째 성분은
\[
[[X_3,X_4],X_2]
\]
으로 multidegree
\[
(0,1,1,1)
\]
이다.

따라서
\[
[A_3,X_1]
\]
의 두 성분은 각각
\[
(4,0,0,0),
\qquad
(1,1,1,1)
\]
에 놓인다.

반면 target
\[
T=[[[X_3,X_4],X_1],X_1]
\]
의 multidegree는
\[
(2,0,1,1).
\]

따라서
\[
[A_3,X_1]
\]
에는 `T` 성분이 존재할 수 없다.

더구나 restricted identity에서
\[
[X_1^{[3]},X_1]=0
\]
이다.

## 3. 중요한 결론

현재 A3-2에서 얻은 degree-3 class만을 단순히 한 번 bracket하여 degree 4로 올리는 방식으로는 기존 target `T`에 도달하지 않는다.

이는 계산 실패가 아니라 구조적 정보이다.

즉,
\[
\boxed{
A_3=X_1^{[3]}-[[X_3,X_4],X_2]
\quad\text{와}\quad
T=[[[X_3,X_4],X_1],X_1]
}
\]
은 같은 degree-4 channel에서 직접 이어지는 두 class가 아니다.

## 4. 연구 방향 수정

따라서 A3-3의 다음 계산은 `A_3` 자체를 T로 억지로 연결하지 않고, 원래 group identity와 Hall–Petrescu 경로를 동시에 추적해야 한다.

특히 이미 확보된
\[
\operatorname{in}_4([v,u,u])=-T
\]
경로와 A3 conjugation correction 사이의 관계를 별도로 계산해야 한다.

필요한 질문은 다음과 같다.

1. `C(x_1)`의 degree-4 Magnus coefficient에서 `T`와 동일한 multidegree `(2,0,1,1)` 성분이 실제로 나타나는가?
2. 나타난다면 그것이 `-[v,u,u]`의 class와 어떤 관계를 갖는가?
3. 이 관계가 q=3 대 q=9 구별에 필요한 orientation-sensitive coefficient와 연결되는가?

## 5. 현재 판단

현재까지는 `T`의 생존 자체와 Hall–Petrescu coefficient는 확정되었지만, A3의 degree-3 correction이 그 coefficient를 직접 설명한다고 주장할 근거는 없다.

다음 계산은 `C(x_1)`의 degree-4 homogeneous Magnus component를 multidegree `(2,0,1,1)`로 투영하여 독립적으로 검사한다.

이는 기존 target을 먼저 가정하지 않는 가장 안전한 A3-3 검증 단계이다.
