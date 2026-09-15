# Track B A3-2 — D3/D4 projection

날짜: 2026-09-16

## 목적

A3 degree-3 Magnus certificate를 Zassenhaus filtration의 `D_3/D_4` class로 정확히 투영한다.

기준 커밋:
`97322f7dce153fafa397b88841fcd9f617115859`

## 1. 출발점

이전 단계에서 정확한 항등식
\[
C(x_1)=x_2x_1x_2^{-1}=x_1x_2[x_3,x_4]x_1^3x_2^{-1}
\]
을 얻었다.

Magnus expansion `x_i -> 1+X_i`를 `F_3`에서 계산하면
\[
C=1+X_1+B+C_3+O(4),
\qquad B=[X_3,X_4],
\]
이고 degree-3 coefficient는 이전 certificate와 같다.

## 2. lower-degree part를 정확히 제거

degree 1과 degree 2를 제거하기 위해
\[
R=[x_3,x_4]^{-1}x_1^{-1}C(x_1)
\]
를 정의한다.

직접 Magnus 곱셈을 수행하면
\[
R=1+R_3+O(4)
\]
이며 degree 1, 2 항은 정확히 소거된다.

계산 결과
\[
\begin{aligned}
R_3={}&X_1^3
+X_4X_3X_2
+2X_3X_4X_2
+2X_2X_4X_3
+X_2X_3X_4.
\end{aligned}
\]
모든 계수는 `F_3`에서 해석한다.

## 3. Lie bracket으로 재조합

\[
B=[X_3,X_4]=X_3X_4-X_4X_3.
\]
따라서
\[
[B,X_2]
=X_3X_4X_2-X_4X_3X_2-X_2X_3X_4+X_2X_4X_3.
\]
`F_3`에서 부호를 반영하면
\[
-[B,X_2]
=X_4X_3X_2+2X_3X_4X_2+X_2X_3X_4+2X_2X_4X_3.
\]
이는 정확히 위의 네 개 혼합 monomial과 일치한다.

따라서
\[
\boxed{
R_3=X_1^3-[[X_3,X_4],X_2].
}
\]

## 4. D3/D4에서의 해석

`R`은 Magnus expansion의 degree 3에서 처음 비자명하므로 `R in D_3`이고, 그 degree-3 initial form이 `D_3/D_4` class를 결정한다.

자유 pro-3/p-군의 Zassenhaus graded object를 restricted Lie algebra로 식별하는 표준 Magnus 대응 아래에서
\[
X_1^3=X_1^{[3]}
\]
로 해석된다.

따라서
\[
\boxed{
[R]_{D_3/D_4}
=
X_1^{[3]}-[[X_3,X_4],X_2].
}
\]

즉 degree-3 correction은 `X_1^{[3]}` 하나가 아니라, 명시적인 Lie bracket correction을 함께 포함한다.

## 5. 독립적인 monomial certificate

basis monomial 순서를
\[
X_1^3,\ X_4X_3X_2,\ X_3X_4X_2,
\ X_2X_4X_3,\ X_2X_3X_4
\]
로 잡으면 `R_3`의 좌표는
\[
(1,1,2,2,1).
\]

반면
\[
X_1^3-[[X_3,X_4],X_2]
\]
의 좌표도
\[
(1,1,2,2,1)
\]
이므로 두 표현은 정확히 일치한다.

## 6. 현재 결론

A3-2가 완료되었다.

핵심 결과:
\[
\boxed{
[x_3,x_4]^{-1}x_1^{-1}C(x_1)
\equiv
1+X_1^{[3]}-[[X_3,X_4],X_2]
\pmod{D_4}.
}
\]

따라서
\[
\boxed{
[C(x_1)]_{\text{degree-3 correction}}
=
X_1^{[3]}-[[X_3,X_4],X_2].
}
\]

이는 다음 단계의 degree-4 계산에서 `X_1^{[3]}` 성분과 bracket correction을 동시에 추적해야 함을 정확히 보여준다.

아직 `q=3` 또는 `q=9` 어느 쪽도 결론내리지 않는다.

## 다음 단계

A3-3:
\[
D_3/D_4\longrightarrow D_4/D_5
\]
에서 위 class의 bracket/restricted operation이 기존 타깃
\[
T=[[[X_3,X_4],X_1],X_1]
\]
및 그 `Sp_4(F_3)` orbit span과 어떻게 연결되는지 계산한다.

검증 원칙:
\[
\text{Magnus certificate}
\to
\text{lower-degree 제거}
\to
\text{restricted-Lie class}
\to
\text{degree-4 독립 검산}.
\]
