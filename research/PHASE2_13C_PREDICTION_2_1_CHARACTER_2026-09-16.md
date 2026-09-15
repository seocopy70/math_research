# Phase 2-13C 사전 예측 — `(2,1)` highest weight와 torus character

## 핵심 예측

현재

\[
0\to M_{25}\to E_{35}\to \operatorname{Sym}^2(V)_{10}\to0
\]

라는 구조가 확정되어 있다.

WeylModules에서 직접 확인한

\[
0\to L(2,0)_{10}\to\Delta(2,1)_{35}\to L(2,1)_{25}\to0
\]

와 비교하면 부분모듈/몫 순서가 뒤집혀 있으므로, M이 해당 25차원 단순모듈이라는 추가 확인 아래 자연스러운 후보는

\[
E\stackrel{?}{\cong}\nabla(2,1).
\]

따라서 유일한 positive-unipotent fixed line의 highest-weight 후보도

\[
(2,1)
\]

으로 예측한다.

## finite-field torus pattern

Phase 2-13B 코드의 standard C2 basis는

\[
(e_1,e_2,f_1,f_2)
\]

이고 split torus는

\[
t(a,b)=\operatorname{diag}(a,b,a^{-1},b^{-1}).
\]

표준 C2 convention

\[
\omega_1=\varepsilon_1,
\qquad
\omega_2=\varepsilon_1+\varepsilon_2
\]

을 사용하면

\[
2\omega_1+\omega_2=3\varepsilon_1+\varepsilon_2.
\]

F_3에서는 a,b가 ±1이므로

\[
a^3b=ab.
\]

따라서 `(2,1)`이 유도하는 finite-field character는

\[
\chi_{(2,1)}(a,b)=ab.
\]

좌표 순서 `(1,1),(1,2),(2,1),(2,2)`에서

\[
\boxed{(1,2,2,1)}
\]

즉 네 character 중 `product` character가 예측된다.

## 엄격한 해석

이것은 **예측이지 증명이 아니다.**

특히 다음을 구분한다.

1. sanity check가 실제 계산된 character가 유효한 character인지 확인한다.
2. 유효한 character가 `(1,2,2,1)`인지 확인한다.
3. torus indexing과 C2 highest-weight convention이 정확히 일치하는지 certificate를 만든다.
4. 그 뒤 positive-root annihilation 및 추가 weight 정보로 `(2,1)`을 검증한다.
5. 마지막으로 E가 실제로 `nabla(2,1)`인지 독립적인 representation certificate를 만든다.

따라서 `product`가 나오더라도 곧바로 `E ~= nabla(2,1)`이라고 선언하지 않는다.

반대로 product가 아니라면 먼저 convention/indexing을 감사한 뒤 해석한다.

## 연구적 의미

이 예측이 실제 sanity check와 일치한다면, 다음 독립 계산들이 같은 표현론적 대상을 가리키게 된다.

- W의 45차원 orbit 구조
- nilpotent endomorphism에 의한 10/35/25 filtration
- U ~= Sym^2(V)
- E의 non-split 25+10 extension
- E != Sym^4(V)
- E의 unique U^+(F_3)-fixed line
- 그 fixed line의 torus character
- `(2,1)` highest-weight prediction

이는 단순 dimension matching보다 훨씬 강한 교차검증이 된다.

## 현재 상태

강화된 sanity-check의 성공 실행 로그는 아직 확보되지 않았다.
따라서 `(1,2,2,1)`도 아직 계산으로 확인된 사실이 아니라 **사전 예측값**이다.

다음 순서는

\[
\boxed{
\text{sanity audit}
\to
\text{character classification}
\to
\text{comparison with }(1,2,2,1)
\to
\text{highest-weight certificate}
\to
E\cong\nabla(2,1)\text{ verification}
}
\]

이다.
