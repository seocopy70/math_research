# Track B — A3-2: Degree-3 restricted/Zassenhaus class

Date: 2026-09-16

## 1. Goal

A3-1에서 얻은 정확한 항등식과 degree-3 Magnus 전개를 바탕으로, 단순한 Magnus homogeneous component와 실제 Zassenhaus quotient \(D_3/D_4\)의 restricted Lie class를 구별한다.

기본 설정:
\[
G=\langle x_1,x_2,x_3,x_4\mid x_1^3[x_1,x_2][x_3,x_4]=1\rangle,
\]
\[
C(x_1):=x_2x_1x_2^{-1},\qquad
C(x_1)=x_1x_2[x_3,x_4]x_1^3x_2^{-1}.
\]

## 2. 먼저 degree-2 부분을 제거

\[
r:=C(x_1)x_1^{-1}.
\]
그러면 \(r\in D_2\)이고
\[
\operatorname{in}_2(r)=[X_3,X_4].
\]

이제
\[
c:=[x_3,x_4]
\]
로 두고
\[
s:=r c^{-1}=C(x_1)x_1^{-1}[x_3,x_4]^{-1}.
\]
그러면
\[
s\in D_3.
\]
따라서 degree-3 Magnus component를 이제 실제 \(D_3/D_4\) class로 해석할 수 있다.

## 3. 정확한 계산 결과

비가환 Magnus 전개를 \(\mathbb F_3\)에서 degree 4까지 수행하고 \(s\)의 homogeneous degree-3 부분을 추출했다.

그 결과:
\[
\begin{aligned}
\operatorname{Magnus}_3(s)= {}&X_1^3
+2X_3X_4X_1+X_4X_3X_1\\
&+2X_1X_3X_4+X_1X_4X_3\\
&+2X_3X_4X_2+X_4X_3X_2\\
&+X_2X_3X_4+2X_2X_4X_3.
\end{aligned}
\]

여기서
\[
[[X_3,X_4],X_1]
=X_3X_4X_1- X_4X_3X_1- X_1X_3X_4+X_1X_4X_3
\]
이고 \(\mathbb F_3\)에서 \(-1=2\)이므로
\[
2[[X_3,X_4],X_1]
=2X_3X_4X_1+X_4X_3X_1+X_1X_3X_4+2X_1X_4X_3.
\]

또한
\[
[[X_3,X_4],X_2]
=X_3X_4X_2-X_4X_3X_2-X_2X_3X_4+X_2X_4X_3,
\]
따라서
\[
2[[X_3,X_4],X_2]
=2X_3X_4X_2+X_4X_3X_2+X_2X_3X_4+2X_2X_4X_3.
\]

그리고 degree-3 associative tensor monomial \(X_1^3\)은 restricted Lie algebra의 p-power에 해당하는
\[
X_1^{[3]}
\]
이다.

따라서 정확히
\[
\boxed{
\operatorname{in}_3(s)
=X_1^{[3]}+2[[X_3,X_4],X_1]+2[[X_3,X_4],X_2]
}
\]
를 얻는다.

동치로
\[
\boxed{
\operatorname{in}_3(s)
=X_1^{[3]}+2[[X_3,X_4],X_1+X_2]
}
\]
이다.

## 4. 중요한 해석

이것은 A3-1의 단순 degree-3 Magnus component를 그대로 restricted Lie class라고 부르는 것과 다르다.

핵심은 먼저
\[
C(x_1)x_1^{-1}
\]
에서 degree-2 class \([X_3,X_4]\)를 제거하기 위해 오른쪽에서 \([x_3,x_4]^{-1}\)를 곱했다는 점이다. 그 결과 얻어진
\[
C(x_1)x_1^{-1}[x_3,x_4]^{-1}\in D_3
\]
의 degree-3 class가 위 식이다.

즉 A3에서 실제로 관찰되는 degree-3 구조는 단순한
\(X_1^{[3]}\)가 아니라
\[
X_1^{[3]}+\text{Lie correction}
\]
형태이다.

## 5. 무엇이 확정되었고 무엇이 아직 아닌가

### 확정

- \(s=C(x_1)x_1^{-1}[x_3,x_4]^{-1}\in D_3\).
- 그 degree-3 restricted/Lie class는 위의 정확한 식이다.
- 특히 \(X_1^{[3]}\)만 남는 것이 아니며 \([X_3,X_4]\)와 \(x_2\)에 의한 conjugation/product correction이 함께 남는다.

### 아직 주장하지 않음

- 이 식 자체가 orientation character \(\chi\) 또는 \(q(G)\)를 복원한다는 주장.
- degree-4에서 이 correction이 정확히 \(T\), \(W_{45}\), 또는 \(Q_4/W\) 중 어디에 투영되는지.
- \(q=3\)과 \(q=9\)가 degree 3 또는 4에서 실제로 구별된다는 결론.

## 6. 다음 단계 A3-3

다음은 이 degree-3 correction을 다시 group-level product/conjugation 공식에 넣어 degree 4 correction을 정확히 계산하는 것이다.

특히
\[
T=[[[X_3,X_4],X_1],X_1]
\]
와의 관계를 확인하고,
\[
Q_4=L_4/(R)_4,
\qquad W=\langle Sp_4(\mathbb F_3)\cdot T\rangle
\]
에서 이 correction의 projection이 어느 부분에 놓이는지 확인한다.

그 후에야
\[
q=3\quad\text{vs.}\quad q=9
\]
비교로 넘어간다.

## 7. 검산 원칙

이번 계산은 raw Magnus 출력 자체를 증명으로 취급하지 않는다. 위 결과는 출력된 monomial들을 명시적인 Lie bracket 및 restricted p-power의 associative embedding과 항별로 대조하여 확인했다. 다음 단계에서도
\[
\text{계산}\to\text{certificate}\to\text{수학적 정리}\to\text{독립 검산}
\]
순서를 유지한다.
