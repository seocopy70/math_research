# A3-4-8 — I = K 실제 부분공간 동일성 검증

## 0. 목적

A3-4-5에서
\[
I:=W_{45}\cap W_d
\]
와 기존
\[
K:=\ker N
\]
에 대해 35차원 모듈 동형
\[
I\cong K
\]
만 확인했다. A3-4-8의 목적은 이 동형이 단순한 추상적 표현론적 동형이 아니라, degree-4 ambient word space 안에서 실제로 같은 부분공간인지 검증하는 것이다.

## 1. 입력 구조

A3-4-5의 검증된 construction을 재사용했다.

\[
\dim W_{45}=45,
\qquad
\dim I=35,
\qquad
\dim K=35.
\]

`I_W`와 `K_coord`를 각각 W45의 좌표로 표현하고, 동일한 256차원 ambient degree-4 word space로 올려
\[
I_{amb}=W I_W,
\qquad
K_{amb}=W K_{coord}
\]
를 구성했다.

## 2. 정확한 동일성 판정

각각의 rank는
\[
\operatorname{rank}(I_{amb})=35,
\qquad
\operatorname{rank}(K_{amb})=35
\]
이다.

두 공간을 합친 행렬의 rank를 계산한 결과
\[
\boxed{\operatorname{rank}[I\mid K]=35}.
\]

따라서
\[
\boxed{I=K}
\]
가 ambient degree-4 space 안의 실제 부분공간으로 성립한다.

즉,
\[
\boxed{W_{45}\cap W_d=\ker N}.
\]

이는 A3-4-5의
\[
I\cong K
\]
보다 강한 결과이다.

## 3. A3-4-8 실행 인증

GitHub Actions workflow:
`Phase 2-21 A3-4-8 I equals K`

Run:
`35052720587`

Job:
`verify` — success

Head commit checked out by runner:
`babace5aa4cdebdc550ea991c3218d7e3f15cb34`

Python 3.11 / NumPy 2.4.6.

핵심 로그:

```text
PHASE 2-21 / A3-4-8 ACTUAL SUBSPACE EQUALITY
dim W45 = 45
dim I = dim(W45 intersect Wd) = 35
dim K = dim ker(N) = 35
rank([I | K]) = 35
I_EQUALS_K_AS_ACTUAL_SUBSPACES = True
RESULT: I = K as actual subspaces of W45 in the ambient degree-4 space.
ALL A3-4-8 CHECKS PASSED
```

## 4. 구조적 결론

A3-4-4, A3-4-5, A3-4-8을 합치면
\[
Q_4=W_{45}+W_d,
\]
\[
\dim W_{45}=\dim W_d=45,
\]
\[
W_{45}\cap W_d=K=\ker N,
\]
\[
\dim K=35.
\]

또한
\[
W_{45}/K\cong \operatorname{Sym}^2(V)=L(2,0),
\]
그리고 A3-4-6에서
\[
W_d/K\cong W_{45}/K\cong \operatorname{Sym}^2(V).
\]

따라서 현재 구조는
\[
\boxed{
Q_4=W_{45}+W_d,
\qquad
W_{45}\cap W_d=K,
\qquad
W_{45}/K\cong W_d/K\cong \operatorname{Sym}^2(V)
}
\]
이다.

## 5. 해석상 주의

이 결과만으로 canonical orientation recovery가 증명되는 것은 아니다. 다음 핵심 문제는 두 extension
\[
0\to K\to W_{45}\to \operatorname{Sym}^2(V)\to0,
\]
\[
0\to K\to W_d\to \operatorname{Sym}^2(V)\to0
\]
가 동일한지 또는 서로 다른지를 판정하는 것이다.

특히 q=3 restricted class가 새로운 quotient representation을 만들지 않는다는 A3-4-6 결과와 결합하면, q-sensitive information이 quotient 자체가 아니라 extension/embedding 구조에 존재하는지를 다음 단계에서 직접 검사해야 한다.

## 6. 판정

\[
\boxed{\textbf{A3-4-8: I=K 실제 부분공간 동일성 계산적으로 인증.}}
\]
