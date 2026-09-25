# LITERATURE_AUDIT_DETAILED_2026-09-25

## 0. 문서 목적

이 문서는 지금까지 수행한 Demuškin 유한-window 연구의 **문헌 대조 과정을 재현 가능한 형태로 보존하기 위한 상세 감사 기록**이다.

기존의 `research/00_RESEARCH_LOG.md`, `research/U5_INTRINSIC_FINITE_SELECTOR_AUDIT_2026-09-24.md`, `research/N1_N5_CRITICAL_REVIEW_2026-09-24.md`는 연구 chronology와 최종 판정을 보존한다. 본 문서는 그 위에 다음 정보를 별도로 정리한다.

1. 어떤 문헌을 검토했는가.
2. 각 문헌의 정확한 정리/명제/예제가 무엇을 제공하는가.
3. 그 결과가 현재 연구의 U1–U5 중 어디와 겹치는가.
4. 무엇이 이미 알려진 결과이고 무엇이 직접 함의되지 않는가.
5. 어떤 novelty claim을 폐기했는가.
6. 현재 남아 있는 finite-window recognition theorem의 novelty boundary가 정확히 어디인가.
7. 이후 추가 문헌조사에서 무엇을 확인해야 하는가.

**중요:** 이 문서는 '문헌에 없음을 증명하는 문서'가 아니다. 현재까지 감사한 문헌군에서 **정확한 동일 정리 또는 즉시적 함의가 확인되지 않았음**을 기록하는 문서다. 따라서 novelty의 최종 표현은 계속 **CONDITIONAL**로 유지한다.

---

# 1. 현재 연구의 정확한 주장

고정된 rank-4, q=3 Demuškin group

\[
G=\langle x_1,x_2,x_3,x_4\mid x_1^3[x_1,x_2][x_3,x_4]=1\rangle
\]

에 대해 Zassenhaus filtration \(P_i(G)\)를 사용하고

\[
Q_k=G/P_{k+1}(G)
\]

를 둔다.

후보 character

\[
\rho:Q_k\to(\mathbf Z/3^k)^\times
\]

에 대해

\[
\mathsf K_k(Q_k,\rho):
H^1(Q_k,\mathbf Z/3^k(\rho))
\longrightarrow H^1(Q_k,\mathbf F_3)
\]

가 surjective인지 검사한다.

현재 연구의 finite-window theorem은 다음 형태이다.

\[
\boxed{
\mathsf K_k(Q_k,\rho)
\Longleftrightarrow
\rho=\chi_G\pmod{3^k},
\qquad k\ge2.
}
\]

여기서 중요한 것은 다음 네 가지를 분리하는 것이다.

- canonical Demuškin orientation \(\chi_G\)의 존재 자체: **고전적으로 알려짐**.
- full-group Kummerian lifting criterion: **알려짐**.
- full-group에서 canonical orientation의 유일성: **알려짐**.
- 위의 성질을 **bare finite quotient \(Q_k=G/P_{k+1}\)** 와 **임의의 candidate \(\rho\)** 만을 입력으로 하는 finite selector로 정식화하고, arbitrary candidate의 factorization까지 포함해 인식하는 것: 현재 연구의 핵심 후보.

따라서 논문의 novelty claim은 첫 세 항목이 아니라 마지막 항목에 한정한다.

---

# 2. 문헌대조의 최종 분류 체계

| Gate | 질문 | 현재 판정 | 논문에서의 역할 |
|---|---|---|---|
| N1 | Kummerian/cyclotomic orientation theory가 이미 알려져 있는가? | **KNOWN / CLOSED** | 강한 prior art |
| N2 | 기존 quotient/inheritance theorem이 finite selector를 직접 함의하는가? | **NO DIRECT IMPLICATION IDENTIFIED / CLOSED** | 주요 novelty objection 해소 |
| N3 | full-group finite-level uniqueness가 새로운가? | **HISTORICAL / NOT NOVEL** | 기존 이론으로 명시 |
| N4 | 임의 candidate \(\rho\)의 twisted cocycle가 \(Q_k\)로 factor하는가? | **MATHEMATICAL PASS / CLOSED** | finite-window theorem의 기초 |
| N5 | 정확한 bare-\(Q_k\), q-blind selector theorem이 이미 발표되었는가? | **NOT IDENTIFIED IN AUDITED CORPUS / CONDITIONAL NOVELTY** | 현재 novelty boundary |

N4는 novelty 자체가 아니다. N4는 finite predicate가 실제로 \(Q_k\)에서 정의될 수 있다는 수학적 foundation이다.

---

# 3. Labute 1967 — Classification of Demushkin Groups

## 서지

J. Labute, **Classification of Demushkin Groups**, Canadian Journal of Mathematics 19 (1967), 106–132.

DOI: 10.4153/CJM-1967-007-8.

## 확인한 핵심

Labute의 고전적 Demuškin theory에는 현재 연구와 직접적으로 관련되는 두 종류의 내용이 있다.

### 3.1 canonical orientation 자체

Demuškin group의 표준 presentation/classification을 통해 orientation character가 어떻게 나타나는지가 고전적으로 결정된다.

현재 frozen family에서는

\[
\chi(x_2)=(1-3)^{-1},
\qquad
\chi(x_i)=1\;(i\ne2)
\]

이고 finite reduction은

\[
\chi(x_2)\equiv
4\pmod9,
\quad
13\pmod{27},
\quad
40\pmod{81},
\ldots
\]

이다.

**판정:** 이것을 우리 연구의 발견으로 주장할 수 없다.

### 3.2 crossed-derivation / finite lifting criterion

Labute의 Proposition 6 및 Theorem 4는 Demuškin orientation과 crossed derivation/cocycle lifting의 관계를 제공한다.

현재 연구에서 이것은 다음에 해당한다.

- full-group finite-level Kummer criterion;
- canonical orientation의 existence/uniqueness;
- 표준 presentation에서 orientation을 확인하는 U4의 역사적 기반.

### 3.3 현재 정리와의 차이

Labute의 결과는 현재의 주장과 다음 점에서 다르다.

현재 연구는

\[
Q_k=G/P_{k+1}
\]

라는 finite quotient를 **입력 객체로 먼저 고정하고**, arbitrary candidate

\[
\rho:Q_k\to(\mathbf Z/3^k)^\times
\]

를 넣은 뒤 intrinsic Kummer predicate로 candidate를 선택한다.

즉 논리적 방향이

> 이미 주어진 Demuškin group/orientation theory → orientation 결정

이 아니라

> finite filtered quotient + arbitrary candidate → Kummer predicate → canonical orientation reduction

이다.

**N3 판정:** full-group uniqueness는 NOT NOVEL.

**N5 판정:** Labute의 결과만으로 현재 exact bare-\(Q_k\) selector theorem이 직접 함의된다고 판정하지 않았다.

---

# 4. Efrat–Quadrelli 2019

## 서지

E. Efrat and M. Quadrelli, **The Kummerian Property and Maximal Pro-p Galois Groups**, Journal of Algebra 525 (2019), 284–310.

DOI: 10.1016/j.jalgebra.2019.01.015.

## 핵심 Proposition

### Proposition 7.3

이 명제는 현재 연구에서 매우 중요하다.

cyclotomic pro-p pair의 Kummerian property를 finite coefficient lifting과 연결한다. 핵심 형태는

\[
H^1(G,\mathbf Z_p(\theta)/p^n)
\to
H^1(G,\mathbf F_p)
\]

의 surjectivity와 finite generator-value lifting의 동치이다.

즉 현재 연구의 predicate

\[
\mathsf K_k
\]

가 임의의 ad hoc 조건이 아니라 이미 알려진 Kummerian cohomological mechanism에 뿌리를 두고 있음을 확인한다.

### Theorem 7.6

torsion-free Demuškin pro-p group에 대해 Kummerian하게 만드는 canonical orientation의 존재와 유일성이 주어진다.

## 현재 연구와의 관계

이 문헌은 다음을 **직접적으로 선행**한다.

- Kummerianity의 finite-coefficient formulation.
- finite H^1 lifting criterion.
- Demuškin canonical orientation의 uniqueness.
- full-group level에서의 orientation recognition.

따라서 다음 주장은 폐기한다.

> “Kummer lifting으로 Demuškin orientation을 유일하게 결정한다” 자체가 새로운 정리다.

그것은 기존 문헌에 속한다.

## 그러나 남는 차이

현재 finite-window theorem은

\[
H^1(Q_k,A_k(\rho))
\to H^1(Q_k,\mathbf F_3)
\]

라는 **finite quotient 자체의 predicate**를 사용한다.

따라서 핵심 질문은 Efrat–Quadrelli의 full-group criterion을 단순히 \(G\)에서 \(Q_k\)로 notation만 바꾼 것인가, 아니면

1. arbitrary candidate \(\rho\)에 대해,
2. 해당 twisted cocycle가 실제로 \(P_{k+1}\)을 죽여,
3. 모든 lifting information이 \(Q_k\)에서 재구성되고,
4. 그 predicate가 unique candidate를 recognize한다

는 별도의 factorization/recognition theorem이 필요한가이다.

현재 연구에서는 이 부분을 U1–U3 및 U5로 별도로 증명했다.

**판정:** N1/N3 = KNOWN/CLOSED. N5 = 직접 동일 정리로 확인되지 않음.

---

# 5. Quadrelli–Weigel 2020

## 서지

M. Quadrelli and T. Weigel, **Profinite Groups with a Cyclotomic p-Orientation**, Documenta Mathematica 25 (2020), 1881–1916.

DOI: 10.4171/DM/788.

## 확인한 역할

이 문헌은 cyclotomic p-oriented profinite groups의 cohomological characterization과 finite coefficient maps를 체계화한다.

현재 연구에 주는 방법론적 input은 다음과 같다.

- orientation을 단순한 presentation parameter가 아니라 cohomological datum으로 다룬다.
- finite coefficient lifting을 orientation property의 핵심으로 사용한다.
- restriction/inheritance 및 subgroup behavior를 구조적으로 다룬다.

## 현재 연구와의 차이

이 문헌에서 orientation은 대체로 **이미 주어진 oriented pair**의 구조를 분석하기 위한 입력이다.

현재 연구의 selector 문제에서는

\[
\rho
\]

가 unknown candidate이다.

즉

> given \((G,\theta)\), what follows from Kummerianity?

와

> given \(Q_k\), which candidate \(\rho\) is selected by Kummerianity?

는 논리적으로 동일하지 않다.

**판정:** 관련 prior art이지만 exact finite-window selector theorem으로 식별하지 않음.

---

# 6. Quadrelli–Weigel 2022

## 서지

M. Quadrelli and T. Weigel, **Oriented pro-\ell groups with the Bogomolov–Positselski property**, Research in Number Theory 8 (2022), 21.

DOI: 10.1007/s40993-022-00318-9.

## 핵심

Proposition 2.6 등에서 Kummerianity에 대한 cohomological equivalences를 정리한다.

또한 theta-abelian quotient 및 oriented structure를 통해 Kummerian pair의 구조적 특성을 설명한다.

## 현재 연구에 제공하는 것

이 문헌은 다음을 강화한다.

- Kummerian property는 단순한 presentation calculation이 아니다.
- finite coefficient lifting과 structural characterization이 서로 연결된다.
- orientation과 cohomological obstruction을 intrinsic하게 다룰 수 있다.

## 현재 selector와의 차이

그러나 audited statement에서는

\[
Q_k=G/P_{k+1}
\]

만을 입력으로 받아 arbitrary finite candidate \(\rho\) 중 canonical reduction을 unique selector로 고르는 정리는 발견되지 않았다.

특히 현재 연구의 다음 두 요소가 별도로 필요하다.

1. arbitrary candidate에 대한 finite-depth factorization;
2. 두 candidate 사이의 차이를 coefficient-extension/Yoneda variation으로 측정하여 uniqueness를 증명하는 U5.

**판정:** KNOWN related theory, exact N5 theorem은 미확인.

---

# 7. Quadrelli 2022 — 1-smooth / cyclotomic characterization

## 서지

M. Quadrelli, **Galois-theoretic features for 1-smooth pro-p groups**, Canadian Mathematical Bulletin 65(2) (2022), 525–541.

## 핵심 확인

Demuškin group에 대해 1-smoothness/cyclotomicity가 canonical Labute orientation과 연결된다.

표준 presentation에서

\[
\theta(x_2)=(1-p^f)^{-1},
\]

다른 generator에서는 1인 형태가 나타난다.

## 현재 연구와의 관계

이 결과는 U4의 presentation-level orientation formula가 임의의 계산 결과가 아니라 기존 Demuškin/cyclotomic theory와 일치함을 확인한다.

하지만 이 문헌 역시 canonical orientation을 **이미 존재하는 structural/cyclotomic object로 사용**한다.

현재 연구의 N5는 orientation을 input으로 넣지 않고 candidate selector로 복원하는 것이다.

**판정:** canonical orientation theory = KNOWN/CLOSED. finite bare-quotient selector = 직접 확인되지 않음.

---

# 8. 2024년 1-cyclotomicity / quotient-inheritance 문헌

## 조사 목적

문헌대조에서 가장 중요한 반론 후보였다.

질문:

> 기존의 quotient/inheritance theorem을 \(N=P_{k+1}\)에 적용하면 이미 우리의 finite-window theorem이 나오는 것 아닌가?

## 확인한 Proposition 2.10 계열 결과

해당 결과는 이미 Kummerian/1-cyclotomic oriented pair

\[
(G,\theta)
\]

에서 시작한다.

또한 normal subgroup \(N\subseteq\ker(\theta)\) 및 restriction map에 대한 추가 조건, 특히

\[
H^1(G,\mathbf F_p)
\to
H^1(N,\mathbf F_p)^G
\]

의 surjectivity와 같은 가정을 사용한다.

## 결정적인 차이

우리의 문제에서는

\[
\rho:Q_k\to(\mathbf Z/3^k)^\times
\]

가 **이미 주어진 canonical orientation이 아니다.**

우리는 arbitrary candidate \(\rho\)에 대해

\[
H^1(G,A_k(\rho))
\to H^1(G,\mathbf F_3)
\]

의 lifting problem 자체가 \(P_{k+1}\)에서 factor되는 것을 증명해야 한다.

따라서 기존 quotient-inheritance theorem은

> known oriented pair → quotient inherits a property

에 가깝고,

현재 정리는

> arbitrary finite candidate → factorization → intrinsic predicate → unique orientation

이다.

둘 사이에는 논리적 gap이 있다.

## 판정

**N2 = NO DIRECT IMPLICATION IDENTIFIED / CLOSED.**

다만 이 판정은 “절대로 함의하지 않는다”는 뜻이 아니다. 논문 제출 전에는 해당 Proposition의 정확한 가정과 \(N=P_{k+1}\)의 특수화를 다시 line-by-line 확인해야 한다.

---

# 9. Blumer–Quadrelli, arXiv:2603.15464v2

## 조사 이유

2026년 최신 Demuškin/1-cyclotomic obstruction 관련 결과이므로 현재 연구의 novelty boundary에 직접적인 영향을 줄 가능성이 있어 확인했다.

## 확인 결과

이 문헌은 Demuškin variation 및 1-cyclotomic obstruction에 관한 구조를 다룬다.

현재 연구와 매우 가까운 키워드가 등장하지만, 감사한 범위에서는 다음 exact theorem은 발견되지 않았다.

\[
Q_k=G/P_{k+1}
\]

를 bare finite input으로 두고 arbitrary candidate \(\rho\)를 입력하여

\[
\mathsf K_k(Q_k,\rho)
\]

가 canonical \(\chi\bmod3^k\)를 유일하게 select한다는 theorem.

## 판정

**RELATED / NOT EXACT.**

따라서 novelty를 무너뜨리는 직접 선행정리로 분류하지 않았다.

---

# 10. Pál–Quick 2026 / A_3-formality 계열

## 조사 이유

Demuškin-type pro-p groups와 finite/formality/cohomological information의 관계를 다루는 최신 결과이므로, finite filtered quotient가 orientation 정보를 이미 encode한다는 기존 theorem이 있는지 확인했다.

## 결과

A_3-formality 및 관련 cohomological/formal structure가 주요 대상이다.

그러나 감사한 범위에서는

\[
Q_k=G/P_{k+1}
\]

와 arbitrary finite orientation candidate를 결합하여 Kummer lifting predicate로 canonical orientation을 unique하게 recognize하는 theorem은 확인되지 않았다.

## 판정

**RELATED / NOT EXACT.**

A_3-formality와 현재 finite Kummer selector를 동일시하지 않는다.

---

# 11. 문헌에서 이미 알려진 것 / 우리 연구가 별도로 증명하는 것

## 11.1 이미 알려진 것

다음은 novelty claim에서 제외한다.

### A. Demuškin canonical orientation의 존재

KNOWN.

### B. Demuškin canonical orientation의 uniqueness

KNOWN.

### C. Kummerian finite-level H^1 lifting criterion

KNOWN.

### D. standard presentation에서

\[
\chi(x_2)=(1-p^f)^{-1}
\]

형태의 formula

KNOWN.

### E. full-group finite coefficient lifting으로 orientation을 characterize하는 것

KNOWN.

---

## 11.2 현재 연구가 별도로 증명하는 부분

### A. arbitrary candidate factorization

임의의

\[
\rho:Q_k\to(\mathbf Z/3^k)^\times
\]

에 대해 twisted crossed cocycle가

\[
P_{k+1}
\]

을 죽이고 finite quotient로 factor되는 것을 U1–U2에서 증명한다.

### B. finite quotient predicate

따라서

\[
\mathsf K_k(Q_k,\rho)
\]

를 실제 finite quotient의 intrinsic predicate로 정의할 수 있다.

### C. U5 variation identity

두 lift

\[
\rho_k'=\rho_k(1+3^{k-1}\nu)
\]

사이에서

\[
\delta_{\rho_k'}-\delta_{\rho_k}
=
\iota_{k-1}\circ(\nu\smile-)
\]

라는 coefficient-extension/Yoneda identity를 사용한다.

### D. PD² injectivity

canonical branch에서 socle inclusion이 \(H^2\)에서 injective임을 PD² duality로 확인한다.

### E. finite selector recognition

결과적으로 finite predicate의 unique solution이 canonical orientation의 reduction임을 inductively recognize한다.

이것이 현재 연구에서 가장 중요한 논리적 구별이다.

---

# 12. N2 objection을 왜 별도로 기록하는가

가장 위험한 잘못된 논리는 다음이다.

1. Demuškin canonical orientation은 Kummerian이다.
2. Kummerian property는 quotient로 내려간다.
3. 따라서 finite quotient에서 Kummer predicate가 canonical orientation을 recognize한다.

2에서 3으로 넘어가는 데 추가적인 논증이 필요하다.

특히:

- arbitrary \(\rho\)가 필요하다.
- \(\rho\)-twisted coefficient module이 finite quotient에서 정확히 정의되어야 한다.
- G-level cocycle가 quotient로 factor되어야 한다.
- 반대로 Q-level lifting이 G-level lifting과 정확히 일치해야 한다.
- uniqueness가 finite level에서 별도로 증명되어야 한다.

현재 연구는 이 부분을 U1–U5로 분해한다.

따라서 “quotient inheritance가 있으니 이미 알려진 것”이라는 objection은 현재 감사 범위에서 **직접 함의가 확인되지 않아 CLOSED**로 분류했다.

---

# 13. N4와 N5를 혼동하지 말 것

## N4

질문:

> arbitrary candidate의 cocycle가 \(Q_k\)에서 factor하는가?

현재 판정:

**MATHEMATICAL PASS / CLOSED.**

이것은 finite predicate가 실제로 의미 있다는 것을 증명한다.

## N5

질문:

> 그렇게 만들어진 predicate가 canonical orientation을 unique하게 recognize한다는 정확한 정리가 기존 문헌에 이미 있는가?

현재 판정:

**NO EXACT PRIOR THEOREM IDENTIFIED / CONDITIONAL NOVELTY.**

N4가 참이라고 해서 N5가 자동으로 새 정리가 되는 것은 아니다.

---

# 14. q-blindness에 대한 정확한 문헌대조 결론

현재 predicate의 정의는

\[
\mathsf K_k(Q_k,\rho)
\]

뿐이며 q를 입력으로 사용하지 않는다.

따라서

**definitional q-blindness = PASS/CLOSED.**

그러나 이것을

> 모든 q에 대해 uniform한 orientation reconstruction theorem

이라고 확대하면 안 된다.

현재 manuscript의 theorem scope는 **fixed rank-4, q=3 family**이다.

따라서

- q가 selector input에 없다: YES.
- q를 몰라도 현재 frozen object에서 selector를 계산할 수 있다: YES.
- 모든 Demuškin q에 대해 같은 theorem을 이미 증명했다: NO.
- q-uniformity를 주장할 수 있다: NO.

이 구분은 novelty와 theorem scope 모두에서 load-bearing이다.

---

# 15. minimality에 대한 문헌대조 결론

현재 사용하는

\[
Q_k=G/P_{k+1}
\]

가 충분하다는 것은 증명했다.

그러나

> \(P_{k+1}\)이 가능한 모든 intrinsic category에서 최소 깊이다

라고 주장하지 않는다.

문헌대조에서도 finite quotient depth의 절대적 minimality를 뒷받침할 기존 정리를 찾은 것이 아니다.

따라서 manuscript에서는

**sufficient finite depth**

라고 표현하고

**minimal finite window**

이라는 표현은 피한다.

Minimality = **OPEN**.

---

# 16. 이전 novelty claim 중 폐기된 것

다음은 이미 연구 기록에서 폐쇄/폐기되었으며 되살리지 않는다.

### 폐기 1
“Demuškin canonical orientation 자체를 intrinsic하게 발견한다.”

→ **NON-NOVEL / CLOSED.**

### 폐기 2
“full-group finite-level Kummer uniqueness 자체가 새로운 정리다.”

→ **HISTORICAL / NOT NOVEL.**

### 폐기 3
“standard Fox calculation으로 canonical orientation을 복원한다.”

→ presentation-dependent proof, novelty carrier가 아님.

### 폐기 4
“degree-3 Fox truncation 자체가 presentation-independent intrinsic carrier다.”

→ Nielsen-change hard attack에서 **FAIL/CLOSED**.

### 폐기 5
“raw t_2 하나가 canonical intrinsic secondary carrier다.”

→ relator-conjugation gauge test에서 **FAIL/CLOSED**.

### 폐기 6
“q를 group-theoretic classification invariant로 먼저 복원한 뒤 orientation formula를 적용하면 새로운 q-blind filtered selector가 된다.”

→ category-adequacy test에서 **HISTORICAL/SUPERSEDED**.

이 negative results는 현재 novelty claim의 범위를 좁히는 데 중요하다.

---

# 17. 문헌에서 가져온 방법론적 자산

이 프로젝트의 문헌조사는 단순 bibliography가 아니다.

## Labute

object:
- Demuškin group / relation / crossed derivation

input:
- standard classification presentation

obstruction:
- cocycle/derivation lifting

verification:
- explicit relation calculation

logical boundary:
- canonical orientation theory is classical.

## Efrat–Quadrelli

object:
- cyclotomic pro-p pair

input:
- orientation + finite coefficient module

obstruction:
- H^1 lifting

verification:
- finite-to-p-adic equivalence

logical boundary:
- orientation is already part of the oriented pair.

## Quadrelli–Weigel

object:
- oriented profinite/pro-p pair

input:
- given cyclotomic orientation

obstruction:
- Kummerian/cohomological conditions

logical boundary:
- not an arbitrary finite candidate selector.

## Current project

object:
- finite filtered quotient \(Q_k\) + candidate \(\rho\)

input:
- no q, no presentation, no chi

obstruction:
- intrinsic finite Kummer lifting predicate

verification:
- U1–U5

logical boundary:
- fixed rank-4, q=3 theorem; P_{k+1} sufficient, not claimed minimal.

이 방법론적 대응은 이후 논문에서 “related work”를 단순 나열하지 않고 **왜 현재 정리가 기존 결과의 단순 재진술이 아닌지를 설명하는 구조**로 사용할 수 있다.

---

# 18. 현재 novelty statement의 안전한 형태

논문에서는 다음 정도가 가장 안전하다.

> To the best of our audited literature search, we did not identify a published theorem that formulates the canonical Demuškin orientation modulo (3^k) as the unique candidate selected by the Kummer lifting predicate on the bare finite quotient (G/P_{k+1}), with arbitrary finite candidate orientation and with the corresponding finite-depth factorization proved independently of a preassigned canonical orientation.

이 문장도 **absolute priority claim이 아니다.**

보다 강한 표현인

> “This is the first theorem…”

또는

> “No one has previously…”

는 현재 기록만으로는 사용하지 않는다.

---

# 19. 제출 전 최종 literature gate

현재까지의 감사로 충분히 정리되었지만, publication gate에서는 다음을 한 번 더 확인한다.

### Gate L1 — Labute exact statement

- Proposition 6
- Theorem 4
- finite crossed-derivation criterion
- exact relation to current U3/U4

### Gate L2 — Efrat–Quadrelli

- Proposition 7.3
- Theorem 7.6
- current \(\mathsf K_k\)와 notation-level equivalence인지 확인

### Gate L3 — Quadrelli–Weigel 2020/2022

- finite coefficient formulation
- quotient/inheritance
- theta-abelian quotient
- current finite selector의 direct corollary 여부

### Gate L4 — quotient/inheritance literature

특히 Proposition 2.10 계열:

- \(N=P_{k+1}\) 대입 가능 여부
- \(N\subseteq\ker\theta\)가 candidate \(\rho\)에 대해 어떻게 해석되는지
- restriction-surjectivity hypothesis가 자동인지 여부
- 자동이라면 현재 theorem이 existing corollary인지 여부

### Gate L5 — 2025–2026 literature

검색 범위를 다음 키워드 조합으로 확장:

- Demushkin + finite quotient + Kummerian
- Demushkin + Zassenhaus + orientation
- Demushkin + \(G/P_{n}\) + cyclotomic
- finite quotient + cyclotomic orientation
- Kummerian + quotient + finite coefficients
- crossed derivation + finite quotient + Demushkin
- 1-cyclotomic + Demushkin + quotient
- orientation reconstruction + Demushkin
- finite recognition + Demushkin orientation

### Gate L6 — equivalent reformulation test

정확히 같은 theorem이 아니라도 다음 형태의 기존 결과가 현재 theorem을 즉시 함의할 수 있는지 확인한다.

\[
\text{existing structural theorem}
\Longrightarrow
\mathsf K_k(Q_k,\rho)
\Longleftrightarrow
\rho=\chi\bmod3^k.
\]

이 경우 novelty는 “new theorem”에서 “new finite reformulation/corollary”로 조정해야 한다.

---

# 20. 현재 최종 판정

### Prior art

- canonical Demuškin orientation: **KNOWN**
- full-group Kummerian criterion: **KNOWN**
- full-group finite-level uniqueness: **KNOWN**
- standard presentation formula: **KNOWN**

### Mathematical contribution candidate

- arbitrary-candidate finite-depth factorization: **PASS/CLOSED**
- intrinsic finite predicate on \(Q_k\): **PASS/CLOSED**
- U5 intrinsic uniqueness: **PASS/CLOSED**
- finite-window recognition theorem: **PASS/CLOSED**

### Novelty

- exact published identical theorem found: **NO, in audited corpus**
- direct implication from known quotient inheritance: **NOT IDENTIFIED**
- absolute priority: **NOT ESTABLISHED**
- current novelty status: **PASS / CONDITIONAL**

### Scope

- fixed rank-4, q=3: **YES**
- q-blind selector input: **YES**
- q-uniform theorem: **NOT CLAIMED**
- \(P_{k+1}\) sufficient: **YES**
- \(P_{k+1}\) minimal: **OPEN**

---

# 21. 관계 문서

이 문서는 다음 authoritative artifacts와 함께 읽는다.

1. `RESEARCH_MAP.md` — global research structure
2. `CURRENT_STATE.md` — current theorem/status
3. `research/00_RESEARCH_LOG.md` — chronological audit trail
4. `research/RESEARCH_CONTINUITY_PROTOCOL.md` — execution/validation rules
5. `research/U5_INTRINSIC_FINITE_SELECTOR_AUDIT_2026-09-24.md` — U5 detailed audit
6. `research/N1_N5_CRITICAL_REVIEW_2026-09-24.md` — controlling N1–N5 final review
7. `paper/main.tex` — manuscript
8. `paper/MANUSCRIPT_STATUS_2026-09-25.md` — publication readiness status

---

# 22. 기록 원칙

이 문서에서 앞으로 새로운 문헌을 확인하면 단순히 bibliography만 추가하지 않는다.

반드시 다음 형식으로 append한다.

**[Date] — [Paper] — [Exact location]**

1. claim of the paper
2. exact mathematical object
3. allowed input
4. invariance/naturality
5. obstruction/verification mechanism
6. relation to U1–U5
7. direct implication? YES/NO/UNCLEAR
8. novelty effect
9. classification
10. next verification required

이 원칙을 유지하면 연구가 실제 논문 단계로 넘어가도 “우리가 왜 이 정리를 새롭다고 생각하는가”의 근거가 대화 기억이 아니라 repository의 재현 가능한 audit trail로 남는다.

---

## Final note

현재 문헌대조의 가장 중요한 결론은 **“기존 문헌이 canonical orientation을 다루지 않았다”가 아니다. 오히려 정반대이다. canonical orientation과 full-group Kummerian uniqueness는 확실히 기존 이론이다.**

현재 남은 질문은 훨씬 좁고 정확하다.

\[
\boxed{
\text{Does the intrinsic Kummer predicate on }
Q_k=G/P_{k+1}
\text{ itself constitute a new finite recognition theorem?}
}
\]

현재까지의 감사 결과는 **“exact theorem not identified; novelty survives conditionally”**이다.

이 경계보다 넓게 주장하지 않는다.
