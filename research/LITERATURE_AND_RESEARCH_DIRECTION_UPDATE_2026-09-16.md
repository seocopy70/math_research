# 문헌검증 및 연구 방향 재정립 — 2026-09-16

## 1. 기록 목적

본 문서는 2026-09-16 문헌검증 결과를 기록한다. 기존 마스터 기록을 덮어쓰지 않고, 기존 결과에 대한 **LITERATURE / CORRECTION / OPEN** 성격의 추가 기록으로 남긴다.

핵심 변화는 다음과 같다.

1. Demuškin 군의 canonical orientation 자체는 Labute의 결과에 의해 군 \(G\)로부터 유일하게 결정되는 것으로 알려져 있다.
2. 따라서 본 연구의 질문을 단순히 "군 \(G\)에서 orientation을 복원할 수 있는가"로 서술해서는 안 된다.
3. 더 약한 데이터인 associated graded/Zassenhaus 데이터만으로 orientation의 image를 복원할 수 있는지는 별개의 문제이며, 기존 문헌에는 Zassenhaus filtration이 orientation의 image 정보를 잃는다는 취지의 결과가 있다.
4. 따라서 현재 연구의 \(45\)-차원 \(Sp_4(\mathbb F_3)\)-module과 \(10-25-10\) 구조는 orientation 그 자체의 복원보다는 **orientation-independent graded shadow에서 나타나는 비자명한 표현론적 구조의 realization**로 보는 것이 현재 더 안전하다.
5. Track B의 \(p\)-power / restricted / Zassenhaus 구조가 다시 중요해졌다. 단순 quadratic Lie shadow에서 잃는 정보를 더 정밀한 filtration 구조가 얼마나 보존하는지 조사할 필요가 있다.

---

## 2. 문헌검증 결과

### 2.1 Labute: canonical orientation

Demuškin 군 \(G\)에 대해 Kummerian oriented pro-\(p\) group 구조를 만드는 orientation은 유일하며, dualizing module에서 유도되는 canonical orientation이라는 결과가 기존 문헌에 존재한다.

따라서

\[
G \longrightarrow \chi_G:G\to \mathbb Z_3^\times
\]

의 유일성 자체는 새로운 주장으로 제시하지 않는다.

**연구상 의미:**

본 연구가 새롭게 물어야 할 대상은 \(G\) 자체가 아니라

\[
G \longrightarrow \operatorname{gr}(G)
\]

라는 정보 손실 이후에도 orientation의 일부 또는 전체가 복원 가능한가이다.

---

### 2.2 Zassenhaus associated graded와 orientation 정보

문헌 조사에서 Demuškin 군의 Zassenhaus filtration이 orientation의 image 정보를 잃는다는 취지의 명시적인 서술을 확인했다.

따라서 다음 명제는 현재 연구에서 반드시 구분해야 한다.

\[
G\text{로부터 }\chi_G\text{ 결정}
\]

과

\[
\operatorname{gr}(G)\text{로부터 }\chi_G\text{ 결정}
\]

은 전혀 같은 문제가 아니다.

후자는 일반적으로 불가능할 가능성을 먼저 검증해야 한다.

따라서 기존의 최종 목표

> filtration만으로 canonical orientation을 복원한다.

는 현재 단계에서 **증명 목표가 아니라 검증 대상 가설**로 낮춘다.

---

### 2.3 \(Sp_4(\mathbb F_3)\) 표현론

Andersen–Kaneda의 \(B_2=C_2\) characteristic-3 Weyl/tilting module 연구를 통해 관련 \(Sp_4\) 표현론은 이미 깊게 연구된 영역임을 확인했다.

따라서 본 연구의 \(10-25-10\) 구조를 "새로운 tilting module을 발견했다"고 표현하지 않는다.

반면 Cabanes–Marin의 \(Sp_4(3)\) 관련 연구에는

\[
\Lambda^2(S^2\bar\rho_0)
\]

라는 45차원 표현의 composition-factor 구조와 25차원 irreducible module이 명시적으로 등장한다.

이는 본 연구에서 독립 계산으로 얻은

\[
W\cong \Lambda^2(\operatorname{Sym}^2 V),
\qquad \dim W=45,
\]

및

\[
0\subset U\subset K\subset W,
\]

\[
\dim U=10,
\quad \dim(K/U)=25,
\quad \dim(W/K)=10
\]

와 강하게 연결된다.

다만 다음은 여전히 구별한다.

- **확립:** \(W\cong\Lambda^2(\operatorname{Sym}^2V)\).
- **확립:** \(U\cong\operatorname{Sym}^2V\).
- **확립:** \(M=K/U\)는 25차원 irreducible \(Sp_4(3)\)-module.
- **문헌과의 식별 근거:** \(PSp_4(3)\)의 관련 25차원 simple module과 일치.
- **아직 별도 증명이 필요한 주장:** \(W\cong T(2,1)\)이라는 정확한 tilting-module identification.

---

## 3. 연구 질문의 현재 형태

현재 연구 질문은 다음 세 층으로 분리한다.

### Q1. 군 수준

\[
G\Rightarrow \chi_G?
\]

**기존 결과로 해결됨:** Labute의 canonical orientation.

### Q2. graded 수준

\[
\operatorname{gr}(G)\Rightarrow \chi_G?
\]

**현재 상태:** 일반적으로 orientation image 정보가 사라질 가능성이 매우 높음. 기존 문헌의 관련 결과를 정밀하게 대조해야 한다.

### Q3. graded shadow의 고차 구조

\[
\operatorname{gr}(G)
\Longrightarrow
\text{비자명한 고차 representation-theoretic structure}?
\]

**현재 연구의 실질적 기여 후보:**

\[
T
\longrightarrow
W_{45}
\longrightarrow
10-25-10.
\]

즉 orientation 자체가 아니라, orientation이 사라진 뒤에도 남는 구조와 원래 Demuškin 데이터 사이의 bridge를 찾는다.

---

## 4. Phase 2의 현재 위치

Phase 2에서 이미 확보한 핵심 결과:

\[
W\cong\Lambda^2(\operatorname{Sym}^2V),
\quad \dim W=45,
\]

\[
W^H=0,
\quad \dim\operatorname{End}_H(W)=2,
\]

\[
0\subset U\subset K\subset W,
\]

\[
\dim U=10,
\quad \dim K=35,
\quad \dim(K/U)=25,
\]

\[
U\cong\operatorname{Sym}^2V,
\]

\[
M=K/U\text{ irreducible},
\]

그리고

\[
0\to M_{25}\to E_{35}:=W/U\to \operatorname{Sym}^2V_{10}\to0
\]

가 **non-split**임을 계산으로 확인했다.

또한

\[
E\not\cong\operatorname{Sym}^4V.
\]

Phase 2-13B에서는

\[
\dim E^{U^+(\mathbb F_3)}=1
\]

을 확인했다.

Phase 2-13C에서는 torus character sanity check가 통과하여

\[
\chi(a,b)=ab=a^3b
\]

라는 characteristic-3 torus character가 정확히 확인되었다.

이는 \(C_2\) highest-weight \((2,1)\)의 finite-field character와 일치하지만, 이것만으로 \(E\) 또는 \(W\)를 특정 algebraic-group module과 동일시하지 않는다.

---

## 5. Track B의 새로운 중요성

기존 quadratic Lie shadow만으로 orientation 정보를 복원하기 어렵다면, 다음 층을 조사해야 한다.

\[
\boxed{
\text{quadratic graded Lie algebra}
\rightarrow
\text{restricted / Zassenhaus }p\text{-structure}
\rightarrow
\text{higher operations}
}
\]

현재 Track B에서는

\[
u=x_1^{-2},\qquad v=[x_3,x_4]^{-1}
\]

에 대해 Hall–Petrescu 전개를 이용하여 실제 군의 \(p\)-power 정보가 degree-4 obstruction에 어떻게 들어오는지 계산 중이다.

이미 A1/A2를 닫았고, A3의 degree-1/2 부분을 확보했다.

특히

\[
HP_4((uv)^{-3})=-T\neq0
\]

라는 결과가 있다.

다음 목표는 A3의 degree-3 및 degree-4 항을 완성하여, 서로 다른 conjugation/\(p\)-power 경로에서 나타나는 degree-4 class가

\[
W,
\qquad Q_4/W,
\qquad \text{또는 기타 canonical subquotient}
\]

중 어디에 위치하는지 비교하는 것이다.

---

## 6. 앞으로의 연구 지도

### Stage 0 — 문헌 경계선 확정

- Labute의 canonical orientation 결과를 원문 수준으로 확인.
- Zassenhaus filtration이 orientation image를 잃는다는 문헌의 정확한 명제와 가정을 확인.
- Quadrelli–Weigel 및 관련 Kummerian/cyclotomic orientation 문헌에서 우리의 rank-4 pro-3 상황과 정확히 겹치는 부분을 분리.
- Cabanes–Marin, Andersen–Kaneda에서 45차원/25차원/tilting 구조의 정확한 위치 확인.

**목표:** novelty claim의 범위를 안전하게 고정.

### Stage 1 — Phase 2 표현 구조 완성

1. \(W\cong\Lambda^2(\operatorname{Sym}^2V)\)의 의미를 정리.
2. \(10-25-10\) filtration과 non-split extension을 정리.
3. \(M_{25}\)의 정확한 \(PSp_4(3)\) module identification을 명시적 certificate와 함께 고정.
4. \(W\cong T(2,1)\) 여부는 별도의 증명으로만 결정.
5. Phase 2-14의 F9 algebraic extension은 구현 오류를 먼저 해결한 뒤, positive-root fixed vector와 torus character를 독립적으로 검증.

### Stage 2 — Track B 완성

1. A3 degree-3 계산.
2. A3 degree-4 계산.
3. A1/A2/A3의 degree-4 classes 비교.
4. \(W\)와 \(Q_4/W\)에서의 위치 계산.
5. 필요한 경우 restricted \(p\)-operation을 포함한 presentation으로 확장.

### Stage 3 — orientation 정보의 실제 검증

여기서는 더 이상 orientation recovery를 가정하지 않는다.

두 경쟁 가설을 직접 비교한다.

**H1.** graded/restricted data가 orientation의 일부를 canonical하게 결정한다.

**H2.** graded/restricted data가 orientation image를 완전히 잃으며, 우리가 발견한 45차원 구조는 orientation-independent realization이다.

필요하다면 같은 graded data를 갖는 서로 다른 oriented structures의 존재 여부를 찾는 방식으로 H2를 검증한다.

### Stage 4 — 최종 논문 구조

가능한 논문 구조는 다음과 같다.

1. Demuškin background 및 orientation의 기존 정리.
2. 문제의 재정의: \(G\)가 아니라 graded/restricted shadow에서 무엇이 남는가.
3. degree-4 obstruction \(T\)와 mildness bridge.
4. \(Sp_4(\mathbb F_3)\)-orbit span \(W\).
5. \(45=10+25+10\)의 구조 및 non-split extension.
6. 문헌과의 representation-theoretic identification.
7. Track B의 \(p\)-power / Zassenhaus 정보.
8. orientation recovery 가능성 또는 불가능성에 대한 최종 판정.

---

## 7. 현재 연구의 가장 중요한 원칙

앞으로는 다음 네 가지를 절대 혼동하지 않는다.

\[
\boxed{
\text{계산이 맞다}
\neq
\text{새롭다}
\neq
\text{orientation을 복원한다}
\neq
\text{논문 기여가 없다}
}
\]

현재 가장 안전한 기여 후보는

\[
\boxed{
\text{Demuškin의 degree-4 graded obstruction이}
Sp_4(\mathbb F_3)
\text{의 기존 45차원 표현 구조를 어떻게 실현하는가}
}
\]

이며, Track B는 이 표현 구조가 실제 \(p\)-power/Zassenhaus filtration의 더 깊은 정보와 어떻게 연결되는지를 결정하는 역할을 한다.

---

## 8. 다음 한 걸음

가장 먼저 할 일은 거대한 계산을 새로 시작하는 것이 아니다.

**첫 번째 실제 연구 작업:**

\[
\boxed{\text{Labute/Blumer의 "orientation이 graded에서 얼마나 사라지는가"를 원문 명제 단위로 확정}}
\]

그 다음 즉시

\[
\boxed{\text{Track B A3 degree-3}\to\text{degree-4 계산}}
\]

으로 돌아간다.

Phase 2-14 F9 계산은 별도 구현 오류를 수정한 뒤 계속한다.

이 순서가 좋은 이유는 "무엇을 계산해야 하는가"를 문헌 경계선이 먼저 결정해 주기 때문이다.
