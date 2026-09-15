# Phase 2-11-A 결과 — 2026-09-15

## 질문

Track A에서

\[
E=W/U,\qquad \dim W=45,\quad \dim U=10,
\]

및

\[
0\to M=K/U\to E\to W/K\cong \operatorname{Sym}^2(V)\to0
\]

라는 정확열을 얻었다. 이 extension이 split인지 확인하기 위해
\(
\operatorname{Hom}_H(\operatorname{Sym}^2(V),E)
\)
을 계산했다.

## 계산

- \(\dim E=35\)
- \(\dim \operatorname{Sym}^2(V)=10\)
- intertwiner system: \(1750\times350\)
- rank = 350
- 따라서
  \[
  \dim_{\mathbb F_3}\operatorname{Hom}_H(\operatorname{Sym}^2(V),E)=0.
  \]

계산은 F_3 위 exact row reduction으로 수행되었다.

## 결론

정확열

\[
0\to M_{25}\to E_{35}\to \operatorname{Sym}^2(V)_{10}\to0
\]

에는 H-equivariant section이 존재할 수 없다. 따라서

\[
\boxed{E\text{ 는 }M_{25}\text{ 와 }\operatorname{Sym}^2(V)\text{ 의 비분할(non-split) extension이다.}}
\]

즉 25차원 층과 10차원 층은 단순히 나란히 놓여 있는 것이 아니라, H-module 구조상 실제로 서로 얽혀 있다.

## 해석상의 주의

이 결과만으로 extension의 동형류가 유일하다고 말할 수는 없다. 또한 아직 E의 정확한 표준 모듈 명칭을 확정하지 않았다. 다음 단계에서는 자연 4차원 표현 V의 4차 대칭곱
\(
\operatorname{Sym}^4(V)
\)
(차원 35)을 직접 구성하여 E와 비교한다. 이는 C_2의 highest weight \(4\omega_1\)에 해당하는 Weyl module \(\Delta(4,0)\) 후보를 문헌 의존 없이 검증하기 위한 단계다.
