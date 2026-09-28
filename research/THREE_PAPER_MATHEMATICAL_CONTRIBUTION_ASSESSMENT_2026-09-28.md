# 세 편의 논문: 수학적 성과와 전체 기여 평가
## 2026-09-28 — 연구자 관점 종합 평가

> 이 문서는 개별 정리의 authoritative proof record가 아니라, Paper 1–3의 수학적 의미·난이도·전체 기여를 다시 보기 위한 종합 해설이다. 개별 수학적 판정은 각 논문과 research/ audit 문서를 우선한다.

## 1. 전체 그림

핵심 질문은 다음과 같다.

> Demuškin 군의 global canonical orientation χ:G→Z_p^×를 G 전체가 아니라 유한한 filtered data만으로 intrinsic하게 인식할 수 있는가? 그렇다면 필요한 정보량은 정확히 얼마인가?

세 편은

Recognition → Sharp information threshold → Recognition at the sharp window

이라는 하나의 연구 프로그램으로 읽는다.

- Paper 1: finite filtered quotient에서 global invariant를 인식하는 finite recognition/factorization 기반을 세운다.
- Paper 2: affine crossed-cocycle 관측 범주에서 정확한 depth n_aff(k)=p^(k−1)+1을 sharp하게 결정한다.
- Paper 3: 그 sharp scale의 finite window에서 Kummer selector가 canonical orientation χ_G mod p^k를 유일하게 선택함을 증명하고, fixed rank-4, p=3에서 selector threshold n_selector(k)=3^(k−1)+1을 선언된 linear selector-carrier 범위에서 sharp하게 닫는다.

중요한 경계: canonical Demuškin orientation, Kummerianity, PD² cup-pairing 자체는 고전 이론이다. 현재 연구의 novelty boundary는 이를 finite filtered data 안의 natural recognition/factorization mechanism으로 조립하는 데 있다. 출판 novelty는 OPEN / CONDITIONAL이며 priority claim은 하지 않는다.

## 2. Paper 1

질문: '유한한 filtered quotient만 보고도 global invariant를 인식할 수 있는가?'

핵심 역할은 무한 pro-p 군 G에서의 Kummer/orientation 문제를 Q_k=G/P_{k+1} 같은 finite window로 내리는 것이다. 따라서 Paper 1은 finite recognition/factorization principle의 출발점이다.

난이도 평가: 고급 박사과정 후반~전문 분야 초입 연구자 수준. 이미 분야를 아는 연구자에게 수개월, 강한 박사과정생이 처음 들어가면 대략 6–18개월 규모의 연구 프로젝트로 보는 것이 합리적이다.

## 3. Paper 2

질문: 'finite window를 얼마나 작게 줄일 수 있는가?'

Affine crossed-cocycle representation을 관측 범주로 잡고

n_aff(k)=p^(k−1)+1

을 얻는다. P_{p^(k−1)+1}에서는 모든 해당 affine representation이 사라지고, P_{p^(k−1)}에서는 surviving witness가 존재하므로 이 범주에서는 정확한 sharp threshold다.

또한 factorization threshold, orientation recognition threshold, absolute minimum information을 서로 다른 문제로 분리했다.

난이도 평가: 전문 분야의 강한 박사과정 연구 수준. 실제 연구 프로젝트로 수개월~1년+, 처음 분야에 들어오는 박사과정생에게는 1–2년급 난이도로 평가한다.

## 4. Paper 3

질문: '그 sharp window에서 실제 canonical orientation을 유일하게 골라낼 수 있는가?'

fixed rank-4, p=3 Demuškin 군에서 Q_k=G/P_{3^(k−1)+1}를 사용하고, 후보 ρ에 대해 finite Kummer lifting predicate를 적용한다.

K_k(Q_k,ρ) ⇔ ρ=χ_G mod 3^k.

핵심 proof architecture:

1. arbitrary candidate ρ의 twisted crossed cocycle가 finite quotient를 통해 factor한다.
2. 잘못된 bare-Q_k H²-inflation injectivity route는 FAIL / CLOSED로 폐기했다.
3. 대신 finite central extension E_k→Q_k와 transgression quotient O_k=H²(Q_k,F_p)/im(tra_k)를 finite obstruction carrier로 사용한다.
4. 후보의 첫 p-adic digit 차이를 ν∈H¹(G,F_p)로 내리고, variation을 ν∪−로 표현한다.
5. Demuškin PD²의 nondegenerate cup pairing으로 ν=0을 강제하여 uniqueness를 얻는다.
6. fixed rank-4, p=3에서 n_selector(k)=3^(k−1)+1을 selector category에서 sharp하게 닫는다.
7. relation-module/cup-product duality로 finite cup image C_k의 dim=1을 증명하고, 선언된 linear selector-carrier category에서 1D minimality를 닫는다.

단, 이는 절대적인 모든 encoding의 최소성 주장이 아니다. E_k→Q_k만으로 더 강한 canonical functional을 직접 재구성하는 문제는 OPEN / NOT LOAD-BEARING이다.

난이도 평가: 세 편 중 가장 proof-sensitive. finite quotient factorization, twisted cohomology, Fox calculus, coefficient variation, finite extension/transgression, PD² duality, p-adic induction, LTE가 한 논리 사슬에 들어간다. 강한 박사과정 후반~초기 전문 연구자 수준이며, 처음 분야에 들어오는 연구자라면 1–2년 이상 규모로 볼 수 있다.

## 5. 세 편을 합친 기여

| 논문 | 질문 | 핵심 답 |
|---|---|---|
| Paper 1 | finite data로 global invariant를 인식할 수 있는가? | finite recognition/factorization 기반 |
| Paper 2 | 정확한 affine information threshold는? | p^(k−1)+1, sharp |
| Paper 3 | 그 scale에서 canonical orientation을 유일하게 인식할 수 있는가? | finite Kummer selector로 χ_G mod p^k 인식; fixed p=3에서 selector threshold sharp |

가장 좋은 압축은:

finite data → exact information threshold → intrinsic unique reconstruction.

## 6. 종합적인 수학적 평가

높게 평가하는 점:
- 연구 질문 자체가 명확하고 정보량 관점의 독립적인 문제를 만든다.
- 단순 existence가 아니라 sharp threshold를 확보했다.
- upper/lower bound와 recognition/factorization을 구분한다.
- arbitrary candidate를 다루어 canonical orientation에 맞춘 계산만으로 끝내지 않는다.
- PD² cup-product 구조가 실제 uniqueness detector로 사용된다.
- 잘못된 강한 주장들을 감사 과정에서 폐기하고 더 정확한 transgression-quotient 구조로 교체했다.

제한점:
- Paper 3의 구체적 selector 결과는 fixed rank-4, p=3에서 출발한다.
- selector minimality는 선언된 linear carrier category에 상대적이다.
- canonical orientation 자체는 새 발견이 아니다.
- 출판 novelty는 아직 OPEN / CONDITIONAL이다.

따라서 현재 가장 정확한 전체 평가는:

**전문적인 pro-p group/cohomology 영역에서 실제 연구급으로 볼 수 있는 coherent한 finite-recognition 연구 프로그램.**

이를 역사적 대발견이라고 부를 근거는 없지만, 기존 정리의 단순 조합이나 계산만으로 보는 것도 지나치게 낮은 평가다.

## 7. 연구 연속성용 한 문장

> Paper 1은 finite recognition의 가능성을 열었고, Paper 2는 affine observation의 sharp information threshold p^(k−1)+1을 정했으며, Paper 3는 그 sharp scale의 finite Kummer data가 canonical Demuškin orientation을 유일하게 선택한다는 것을 증명했다.

## 8. 관련 authoritative 기록

- CURRENT_STATE.md — 최신 수학적 상태와 Gate 분류
- RESEARCH_MAP.md — 전체 연구 구조와 누적 의사결정
- research/PAPER3_D2_TRANSGRESSION_QUOTIENT_CARRIER_RESULT_2026-09-28.md
- research/PAPER3_D3_SELECTOR_PROMOTION_D4_BOUNDARY_2026-09-28.md
- research/PAPER3_FINITE_CUP_LINE_COMPRESSION_2026-09-28.md
- research/PAPER3_FINAL_FRONTIER_AUDIT_2026-09-28.md
- research/PAPER3_MANUSCRIPT_MANIFEST_2026-09-28.md