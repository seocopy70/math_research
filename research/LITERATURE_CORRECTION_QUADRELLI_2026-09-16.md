# 문헌 귀속 정정 및 Zassenhaus–orientation 검증 — 2026-09-16

## 1. 정정 사항

이전 연구 기록/대화에서 다음 문구를 Simone Blumer의 박사학위논문에 귀속한 것은 **잘못된 귀속**이다.

> “It is worth to stress that the Zassenhaus filtration loses completely the information about the image of the orientation θ — as it happens for Demuškin groups, see (2.19).”

Simone Blumer의 실제 박사학위논문은 **On Quadratically Defined Lie Algebras and Their Subalgebras**이며, 2024년경 공개된 논문/학위논문으로, quadratic Lie algebras와 Bloch–Kato 관련 Lie algebra 구조를 다룬다. 해당 논문의 초록은 위의 Zassenhaus-orientation Remark 3.25의 출처가 아니다.

## 2. 정확한 출처 확인

위 문구가 실제로 확인된 출처는 다음이다.

**Claudio Quadrelli, Cohomology of Absolute Galois Groups, Ph.D. thesis, Università degli Studi di Milano-Bicocca / Western University, December 2014.**

Bicocca 기관 저장소의 서지정보는 저자를 Claudio Quadrelli로 명시하고, 논문의 주제가 pro-p Galois groups, cyclotomic orientations, Zassenhaus restricted Lie algebra, Koszul duality임을 확인한다.

PDF의 첫 페이지에도 다음이 확인된다.

- Claudio Quadrelli
- December 2014
- Advisors: Thomas S. Weigel, Ján Mináč

## 3. 실제 Remark 3.25

해당 논문의 §3.5, “The Zassenhaus filtration for θ-abelian groups”에서 다음이 명시되어 있다.

> “Remark 3.25. It is worth to stress that the Zassenhaus filtration loses completely the information about the image of the orientation θ — as it happens for Demuškin groups, see (2.19).”

같은 절에서 θ-abelian pro-p group의 경우

\[
D_n(G)=G^{p^\ell},
\qquad p^{\ell-1}<n\le p^\ell,
\]

및

\[
L_i(G)=D_i(G)/D_{i+1}(G)
\]

가 p-거듭제곱 차수에서만 나타나는 abelian restricted Lie algebra 구조를 갖는다는 계산이 제시된다.

따라서 Remark 3.25의 의미는 적어도 **θ-abelian 계열에서는 서로 다른 orientation image가 Zassenhaus filtration 자체에서 사라질 수 있음**을 강조하는 것이다.

## 4. 중요한 범위 제한

이 문구만으로 다음의 강한 명제를 바로 결론내려서는 안 된다.

\[
\operatorname{gr}(G)\text{가 모든 Demuškin orientation 정보를 항상 잃는다.}
\]

현재 확인된 것은 다음 두 사실이다.

1. Quadrelli의 2014년 박사논문에 위 문구가 실제로 존재한다.
2. 그 문구는 θ-abelian pro-p group의 Zassenhaus 계산을 논의하는 문맥에서 제시되며, Demuškin groups를 사례로 언급한다.

그러므로 우리의 rank-4 pro-3 Demuškin group에 대해 **어떤 데이터가 정확히 사라지는지**는 별도로 확인해야 한다.

특히 구분해야 할 대상은

\[
G \quad\text{vs.}\quad (G,\chi_G)
\]

및

\[
\operatorname{gr}(G)
\quad\text{vs.}\quad
\bigl(\operatorname{gr}(G),\text{restricted structure},\text{additional operations}\bigr).
\]

## 5. Labute / 현대 문헌과의 교차검증

현대 문헌은 다음을 독립적으로 확인한다.

### 5.1 Canonical orientation

무한 Demuškin pro-p group에는 canonical orientation

\[
\chi_G:G\to 1+p\mathbb Z_p
\]

이 존재하며, 이는 dualizing module에서 유도되는 orientation이다.

또한 Quadrelli의 최근 논문에서는 이 orientation이 해당 Demuškin group을 1-cyclotomic/Kummerian oriented pro-p group으로 만드는 유일한 orientation임을 명시한다.

### 5.2 우리의 rank-4, p=3 모델

우리의 관계식

\[
G=\langle x_1,x_2,x_3,x_4\mid x_1^3[x_1,x_2][x_3,x_4]=1\rangle
\]

은 Demuškin classification의

\[
r=x_1^{p^f}[x_1,x_2][x_3,x_4]\cdots
\]

형태에서 p=3, f=1인 경우에 해당한다.

따라서 canonical orientation은 문헌상 별도의 숨은 선택이 아니라 G의 dualizing structure에 의해 정해진다.

### 5.3 Zassenhaus graded relation

Mináč–Pasini–Quadrelli–Tân의 문헌은 Demuškin group에 대해 Zassenhaus filtration에서 얻는 graded algebra가 quadratic duality/PBW 구조를 갖고, 우리의 presentation (4.1)에서 initial relator가

\[
[X_1,X_2]+[X_3,X_4]+\cdots
\]

임을 명시한다.

따라서 현재 연구에서 사용하는

\[
R=[X_1,X_2]+[X_3,X_4]
\]

은 문헌상 정당한 Demuškin Zassenhaus initial relation이다.

## 6. 연구 질문에 대한 현재 결론

따라서 현재는 다음처럼 기록한다.

### 확정

\[
G\Rightarrow \chi_G
\]

는 기존 Demuškin theory에서 해결된 문제다.

### 강한 주의가 필요한 부분

\[
\operatorname{gr}(G)\Rightarrow \chi_G
\]

가 가능한지 여부는 아직 우리의 특정 rank-4 pro-3 상황에서 최종 판정하지 않았다.

Quadrelli의 2014년 Remark 3.25는 **orientation image loss에 대한 강력한 문헌적 경고**이지만, 이를 곧바로 우리의 정확한 연구 대상에 대한 완결된 impossibility theorem으로 사용하지 않는다.

### 현재 연구의 안전한 위치

따라서 연구는 다음 세 방향을 병렬로 유지한다.

1. Phase 2: 45차원 \(Sp_4(\mathbb F_3)\)-module 구조의 완성.
2. Track B: Hall–Petrescu 및 restricted/Zassenhaus 고차 구조 계산.
3. Literature track: Quadrelli Remark 3.25의 정확한 (2.19) 및 적용 범위를 직접 대조하고, 필요하면 관련 전문가에게 확인.

## 7. 핵심 방법론적 정정

이전의

> “Zassenhaus associated graded는 orientation을 잃으므로 orientation recovery는 불가능하다.”

라는 식의 단정은 현재 연구 기록에서 **삭제해야 할 강한 결론**이다.

대신 다음으로 유지한다.

\[
\boxed{
\text{Zassenhaus filtration은 orientation-image loss를 일으킬 수 있다는 문헌적 증거가 있다.}
}
\]

그리고 우리의 특정 Demuškin group에서

\[
\boxed{
\text{정확히 어느 수준의 orientation 정보가 남는가?}
}
\]

를 직접 검증한다.

## 8. 주요 출처

- Claudio Quadrelli, *Cohomology of Absolute Galois Groups*, Ph.D. thesis, 2014, Università degli Studi di Milano-Bicocca / Western University.
- John P. Labute, *Classification of Demushkin Groups*, Canadian Journal of Mathematics 19 (1967), 106–132, DOI 10.4153/CJM-1967-007-8.
- Jan Mináč, Federico Pasini, Claudio Quadrelli, Nguyễn Duy Tân, *Koszul algebras and quadratic duals in Galois cohomology*, DOI 10.1016/j.aim.2021.107569.
- Claudio Quadrelli, *Chasing Maximal Pro-p Galois Groups via 1-Cyclotomicity*, Mediterranean Journal of Mathematics 21 (2024), article 56, DOI 10.1007/s00009-024-02598-0.

## 9. 한 줄 결론

**이전의 Simone Blumer 귀속은 틀렸고, 실제 출처는 Claudio Quadrelli의 2014년 박사학위논문임을 확인했다. 또한 문구 자체는 실재하지만, 이를 우리의 rank-4 pro-3 Demuškin 연구에 대한 최종적인 orientation 불가능성 정리로 확대해석해서는 안 된다.**
