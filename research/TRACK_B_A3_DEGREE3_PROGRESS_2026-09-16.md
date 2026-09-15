# Track B A3 — degree-3 정확화 진행 기록

날짜: 2026-09-16

## 목적

A3의 목표는
\[
C(x_1)=x_2x_1x_2^{-1}
\]
의 degree-3 정보를 정확히 계산하여, 이후 degree-4 correction 및 q=3 대 q=9 비교의 기반을 만드는 것이다.

중요한 원칙은
\[
\operatorname{gr}_3([x_1,x_2])=-X_1^{[3]}
\]
라고 단순 가정하지 않는 것이다. \([x_3,x_4]^{-1}\)에서 오는 degree-3 성분과 conjugation/product correction을 모두 포함해야 한다.

## 1. 정확한 군론적 항등식

기본 관계는
\[
x_2^{-1}x_1x_2=x_1[x_1,x_2]
=x_1^{-2}[x_3,x_4]^{-1}.
\]
따라서
\[
[x_1,x_2]=x_1^{-3}[x_3,x_4]^{-1}.
\]
또한
\[
[x_1,x_2^{-1}]
=x_2[x_1,x_2]^{-1}x_2^{-1}.
\]
그러므로
\[
C(x_1)=x_1[x_1,x_2^{-1}]
=x_1x_2[x_1,x_2]^{-1}x_2^{-1}
\]
이고
\[
[x_1,x_2]^{-1}=[x_3,x_4]x_1^3
\]
이므로 정확히
\[
\boxed{
C(x_1)=x_1x_2[x_3,x_4]x_1^3x_2^{-1}.
}
\]

이 항등식은 A3의 계산을 크게 단순화한다.

## 2. degree 1 및 degree 2

Magnus 변수에서
\[
x_i\mapsto1+X_i
\]
로 두면
\[
\operatorname{gr}_1(C(x_1))=X_1.
\]
또한
\[
[x_3,x_4]
\]
의 degree-2 initial form은
\[
B=[X_3,X_4]
\]
이다. 따라서
\[
C(x_1)=X_1+[X_3,X_4]+O(D_3)
\]
라는 기존 결과가 다시 확인된다.

## 3. degree-3 Magnus certificate

\(\mathbb F_3\)에서
\[
(1+X_1)^3=1+X_1^3
\]
이므로
\[
(1+X_1)^{-3}=1-X_1^3+O(X_1^6)
\]
이다. 특히 degree 3에서는 계수가
\[
-X_1^3=2X_1^3
\]
이다.

또한 \([x_3,x_4]\)의 Magnus 전개를 직접 곱셈으로 계산하면 degree 3 부분은
\[
X_4X_3X_4-X_4^2X_3-X_3X_4X_3+X_3^2X_4.
\]
따라서 \([x_1,x_2]=x_1^{-3}[x_3,x_4]^{-1}\)의 degree-3 성분에는 반드시
\[
-X_1^3
\]
뿐 아니라 \([x_3,x_4]^{-1}\)에서 오는 degree-3 성분도 포함된다.

정확한 군론적 항등식
\[
C(x_1)=x_1x_2[x_3,x_4]x_1^3x_2^{-1}
\]
을 Magnus 전개하여 degree 3까지 계산한 결과는 다음과 같다.

\[
\begin{aligned}
\operatorname{Magnus}_3(C(x_1))={}&X_1^3\\
&+X_4X_3X_2-X_4X_3X_4+2X_4^2X_3\\
&+2X_3X_4X_2+X_3X_4X_3+2X_3^2X_4\\
&+2X_2X_4X_3+X_2X_3X_4\\
&+2X_1X_4X_3+X_1X_3X_4.
\end{aligned}
\]
여기서 모든 계수는 \(\mathbb F_3\)에서 해석한다.

이는 'degree-3에 \(X_1^{[3]}\) 하나만 있다'는 단순화가 정확하지 않음을 명시적으로 보여주는 certificate다.

## 4. 해석상의 주의점

위 식은 Magnus의 비가환 거듭제곱급수에서 얻은 degree-3 coefficient이다. 이것을 그대로 restricted Lie algebra의 한 원소라고 명명해서는 안 된다.

특히 다음 둘을 구별해야 한다.

1. Magnus expansion에서의 homogeneous degree-3 성분.
2. Zassenhaus filtration의 quotient \(D_3/D_4\) 또는 필요한 restricted graded object에서의 class.

다음 단계에서는 이 degree-3 Magnus 성분을 적절한 filtration quotient로 투영하여, Lie/restricted Lie 관점에서 정확히 어떤 class가 남는지를 계산해야 한다.

## 5. 현재까지의 결론

A3에서 가장 중요한 진전은 다음이다.

\[
\boxed{
C(x_1)=x_1x_2[x_3,x_4]x_1^3x_2^{-1}
}
\]
라는 정확한 항등식을 확보했고, degree-3 계산을 실제 비가환 Magnus 전개로 확인했다.

따라서 q-sensitive한 \(X_1^{[3]}\) 항과 \([X_3,X_4]\)의 higher-degree correction을 분리해서 추적해야 한다는 점이 확정되었다.

## 6. 다음 계산

다음 단계는 세 부분이다.

### A3-2
위 Magnus degree-3 성분을 \(D_3/D_4\)의 restricted Lie class로 정확히 투영한다.

### A3-3
그 결과를 사용하여 degree-4 correction을 계산하고, 기존
\[
T=[[[X_3,X_4],X_1],X_1]
\]
및
\[
W=\langle Sp_4(\mathbb F_3)\cdot[T]\rangle
\]
와의 관계를 결정한다.

### A3-4
그 후에야
\[
q=3\quad\text{vs.}\quad q=9
\]
비교를 수행한다.

현재는 아직 orientation 복원이나 q의 검출을 주장하지 않는다.

## 검증 원칙

이번 계산은 '컴퓨터가 찾았다'에서 끝내지 않고, 정확한 군론적 항등식과 명시적인 Magnus certificate를 함께 보존한다.

\[
\boxed{\text{계산}\to\text{certificate}\to\text{filtration quotient 해석}\to\text{독립 검산}}
\]
