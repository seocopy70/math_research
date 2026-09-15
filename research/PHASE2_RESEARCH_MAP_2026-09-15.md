# Phase 2 연구 지도 — 2026-09-15

## 목적

이 문서는 다른 AI/연구자가 저장소의 개별 스크립트만 읽지 않고 Phase 2의 전체 논리 흐름을 한 번에 복원할 수 있도록 만든 공개 연구 지도다.

## 궁극적 질문

Demuškin 군

\[
G=\langle x_1,x_2,x_3,x_4\mid x_1^3[x_1,x_2][x_3,x_4]=1\rangle
\]

의 filtration/associated graded 정보만으로 Demuškin orientation
\(\chi:G\to\mathbb Z_3^\times\)의 일부 또는 전부를 canonical하게 복원할 수 있는가?

현재 이 질문은 미해결 상태다. 아래 결과는 orientation 복원 자체의 증명이 아니다.

## Track A — 표현론적 구조 탐사

출발점:

\[
L=\mathbb L_{\mathbb F_3}(X_1,X_2,X_3,X_4),
\quad R=[X_1,X_2]+[X_3,X_4],
\]

\[
T=[[[X_3,X_4],X_1],X_1].
\]

Theorem A 계산 certificate:

\[
T\notin(R)_4,
\qquad \dim Q_4=55.
\]

### Phase 2-1: orbit module

\[
H=Sp_4(\mathbb F_3),\qquad W=\langle H\cdot[T]\rangle.
\]

확정:

- \(|H|=51840\)
- \(\dim W=45\)
- \(W^H=0\)

주요 파일:
`phase2_1_invariant_space_verification_2026-09-15.py`

### Phase 2-3: endomorphism algebra

확정:

\[
\dim End_H(W)=2.
\]

비자명한 \(N\)에 대해

\[
N^2=0,\quad rank(N)=10.
\]

따라서

\[
U=im(N),\quad K=ker(N),
\]

\[
0\subset U_{10}\subset K_{35}\subset W_{45}.
\]

또한

\[
End_H(W)\cong\mathbb F_3[\varepsilon]/(\varepsilon^2).
\]

### Phase 2-6-A: U 식별

독립적인 intertwiner 계산으로

\[
U\cong Sym^2(V),\qquad \dim U=10.
\]

### Phase 2-7/2-8B: M 식별 수준

\[
M=K/U,\qquad \dim M=25.
\]

직접 계산으로

\[
\langle A_1,\dots,A_5\rangle_{alg}=Mat_{25}(\mathbb F_3),
\]

따라서

\[
M\text{은 irreducible이다.}
\]

표준 highest-weight 이름 \(L(2,1)\)은 아직 채택하지 않는다. 특히 \(-I\)가 degree-4 quotient에서 자명하게 작용하므로 중심작용과 충돌 가능성이 있어 이름을 성급히 붙이지 않는다.

### Phase 2-10: W 전체 식별

독립 검증으로

\[
W\cong \Lambda^2(Sym^2(V)).
\]

독립 certificate:

- intertwiner system rank = 2023
- nullity = 2
- full-rank witness rank = 45
- witness SHA256 = `1c4276a930acda5e1c33996beee59467fd197ebd5bbe0f04d94bae7b0d314843`
- 모든 intertwining equation 통과

결과 파일:
`PHASE2_10_INDEPENDENT_VERIFICATION_RESULT_2026-09-15.md`

### Phase 2-11-A: extension이 split인가?

\[
E=W/U,\qquad \dim E=35.
\]

정확열:

\[
0\to M_{25}\to E_{35}\to Sym^2(V)_{10}\to0.
\]

계산:

\[
\dim Hom_H(Sym^2(V),E)=0.
\]

따라서 E에는 H-equivariant section이 없고 extension은 non-split이다.

즉 25차원 층과 10차원 층은 단순 direct sum이 아니다.

### Phase 2-12: Sym^4(V) 후보 검사 — NEGATIVE RESULT

차원 때문에 자연스럽게

\[
\dim Sym^4(V)=35
\]

이므로 후보로 검사했다.

그러나

\[
Hom_H(Sym^4(V),E)=0.
\]

따라서

\[
\boxed{E\not\cong Sym^4(V).}
\]

이 후보는 폐기한다. 이것은 코드 오류가 아니라 실제 수학적 음성 결과다.

## 현재 확정 그림

\[
T
\longrightarrow
W_{45}
\cong\Lambda^2(Sym^2V)
\]

및

\[
0\subset U_{10}\subset K_{35}\subset W_{45},
\]

\[
U\cong Sym^2(V),
\qquad M=K/U\text{ irreducible of dimension }25,
\]

\[
0\to M_{25}\to E_{35}=W/U\to Sym^2(V)_{10}\to0
\]

이며 마지막 정확열은 non-split이다.

단,

\[
E\not\cong Sym^4(V).
\]

## 현재 모르는 것

1. 35차원 \(E\)의 정확한 표준 표현론적 정체
2. non-split extension의 동형류/extension class의 정확한 성격
3. 이 구조가 Demuškin orientation \(\chi\)와 어떤 필연적 연결을 갖는지
4. Track A의 표현론적 구조가 Track B의 Hall–Petrescu/filtration 계산과 어떻게 만나는지

## 다음 단계 원칙

35라는 차원만 보고 후보를 정하지 않는다.

먼저 E의 실제 action에서 highest/maximal-vector 구조와 submodule lattice를 계산하고, 그 결과가 가리키는 후보만 intertwiner로 검증한다.

## Track B와의 분리

Track B는 독립적으로 진행한다.

현재 확정된 A2 결과:

\[
HP_4((uv)^{-3})=-T=2T\neq0
\]

in \(Q_4\).

A1/A3는 별도 검증 대상이며 Track A의 표현론적 식별에 선입견을 주지 않는다.

## 방법론적 규칙

모든 강한 주장에는 다음 순서를 적용한다.

\[
\boxed{\text{계산 발견}\to\text{certificate}\to\text{수학적 설명}\to\text{독립 검산}}
\]

차원 일치만으로 동형을 주장하지 않는다. 프로그램 출력만으로 증명이라 부르지 않는다. orientation 복원은 아직 주장하지 않는다.
