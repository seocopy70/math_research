# A3-4 구조적 교정 및 X2 방향 q-민감성 검사

## 2026-09-16 연구 기록

### 1. A3-3 결과의 구조적 해석

기존 A3-3에서

\[
d_4=[\operatorname{in}_3(s_q),X_1]
\]

를 계산했을 때 q=3과 q=∞의 차이가 나타나지 않았다.

이 결과는 Demuškin 관계식의 특수한 성질이라기보다 restricted Lie algebra의 공리에서 구조적으로 강제된다.

restricted Lie algebra의 공리

\[
\operatorname{ad}(a^{[p]})=\operatorname{ad}(a)^p
\]

에 \(b=a\)를 적용하면

\[
[a^{[p]},a]
=\operatorname{ad}(a)^p(a)
=\operatorname{ad}(a)^{p-1}[a,a]
=0.
\]

특히 p=3에서

\[
\boxed{[X_1^{[3]},X_1]=0}
\]

은 계산으로 발견한 현상이 아니라 모든 restricted Lie algebra에서 성립하는 항등식이다.

따라서 \(\operatorname{in}_3(s_3)\)과 \(\operatorname{in}_3(s_\infty)\)의 q-차이가 \(X_1^{[3]}\) 항에 들어 있다면, 이를 \(X_1\)과 bracket하는 방식으로는 q-정보를 검출할 수 없다.

### 2. 실험 설계의 교정

따라서 기존 \(X_1\)-방향 검사는 독립 검산으로 유지하되, q-민감성 탐색은 다른 생성원과의 bracket으로 전환한다.

첫 번째 새 검사는

\[
\boxed{
d_4^{(2)}(q):=[\operatorname{in}_3(s_q),X_2]
}
\]

이며 특히

\[
\boxed{
d_4^{(2)}(3)\quad\text{vs.}\quad d_4^{(2)}(\infty)}
\]

를 동일한 \(Q_4\)에서 비교한다.

q-차이가 \(X_1^{[3]}\) 항으로 나타난다면

\[
[X_1^{[3]},X_2]
=\operatorname{ad}(X_1)^3(X_2)
=[X_1,[X_1,[X_1,X_2]]]
\]

가 핵심 검출 항이 된다. 이는 \([X_1^{[3]},X_1]\)과 달리 restricted Lie algebra의 공리만으로 0이 되지 않는다.

### 3. 판정 기준

1. \([X_1^{[3]},X_2]\)가 \(Q_4\)에서 살아 있고 다른 q-의존 항과 상쇄되지 않으면 degree 4에서 이미 filtration의 q-기억이 검출된다.
2. 해당 항이 존재하지만 relation quotient에서 소거되면 degree 4 단순 bracket 검사는 실패하며 higher-degree 실험이 필요하다.
3. \(X_2\) 방향도 소거될 경우 필요에 따라 \(X_3,X_4\) 방향을 같은 방식으로 검사한다.

### 4. 현재 연구 상태

A3-4-1: \([\operatorname{in}_3(s_q),X_1]\) 독립 검산 — 유지.

A3-4-2: \([\operatorname{in}_3(s_3),X_2]\)와 \([\operatorname{in}_3(s_\infty),X_2]\)의 비교 — 다음 계산으로 진행.

이번 교정의 핵심 결론은 다음과 같다.

> A3-3에서 관찰된 q-insensitivity는 새로운 negative result라기보다, \(X_1^{[3]}\) 정보를 자기 자신 \(X_1\)과 bracket하는 검출 방식이 구조적으로 blind하다는 사실을 확인한 것이다.

따라서 degree 9 실험으로 즉시 올라가기 전에 degree 4의 다른 bracket 방향을 먼저 검사한다.
