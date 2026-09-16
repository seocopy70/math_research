# A3-4-22 — q-control experiment design

## 목적

A3-4-17~21에서 확정한 \(B/A\)와 \(K\)의 구조가 원래 연구 질문인 \(q=3\) 대 \(q=\infty\) 구별과 실제로 연결되는지를 검증한다.

## A3-4-17~21 기준선

두 35차원 \(H=Sp_4(\mathbb F_3)\)-module은 같은 두 단순인자를 가지지만 서로 반대 방향의 비분할 확장을 갖는다.

\[
0\to S_{25}\to B/A\to S_{10}\to0,
\]

\[
0\to S_{10}\to K\to S_{25}\to0.
\]

A3-4-20S에서는 실제 35차원 ambient 좌표에서

\[
\operatorname{Soc}(B/A)=\ker Q,
\qquad
\operatorname{Soc}(K)=\operatorname{im}Q
\]

를 엄밀하게 확인했다. 따라서 이 '10/25 socle 방향의 반전'은 계산상 확정된 구조적 사실이다.

## 아직 남은 핵심 질문

이 반대 방향성이 단지 특정한 두 대상 \(B/A\), \(K\)의 고유한 모듈 구조인지, 아니면 원래의 매개변수 \(q\)와 관련된 현상인지 아직 확인하지 않았다.

특히 현재까지의 계산만으로는

\[
\boxed{\text{opposite extension direction}\ \Longrightarrow\ q\text{-sensitivity}}
\]

를 주장할 수 없다.

## 다음 통제실험

q=3에서 사용한 construction과 가능한 한 동일한 절차를 q=\infty 쪽에 적용한다. 구체적으로는 q=\infty의 대응하는 \(B/A\), \(K\) 대상이 정의될 수 있는지 먼저 확인하고, 정의된다면 다음 불변량을 동일한 순서로 비교한다.

1. 차원과 generator action.
2. 단순 composition factors \(S_{10},S_{25}\) 또는 그에 대응하는 실제 단순인자.
3. Loewy length 및 indecomposability.
4. socle/head의 방향.
5. 가능하면 동일한 방식의 non-split extension 여부.

핵심 판별량은 단순히 '비슷한가'가 아니라, q=3과 q=\infty에서 **extension direction / socle placement가 달라지는가**이다.

## 설계 원칙

- 기존 A3-4-16의 정확한 35×35 generator matrices와 q=3 기준선을 재사용한다.
- 새로운 계산은 production 구조를 변경하지 않는 독립 검증으로 만든다.
- 차원 일치만으로 PASS하지 않는다. 실제 subspace/span 또는 module isomorphism 수준의 검증을 우선한다.
- q=\infty 쪽에서 대상 자체가 자연스럽게 정의되지 않는다면 억지로 대응시키지 않는다. 그 경우 '현재의 B/A, K extension 구조는 q=3 특유의 construction에서 나온 것'이라는 제한을 명시하고, 더 적절한 q-공통 construction을 다시 설계한다.

## 상태

**A3-4-22 = DESIGN / NOT YET COMPUTED**

이 기록은 A3-4-21의 결론을 q-sensitivity 문제로 연결하기 위한 통제실험 설계 기록이다. 아직 q=\infty 계산 결과나 q 판별을 주장하지 않는다.
