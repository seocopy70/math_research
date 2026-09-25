# AI 협업 연구 방법론 사례 기록 초안 — 2026-09-25

## 0. 목적

이 문서는 2026년 9월 수행된 Demuškin 군 연구를 단순한 수학 결과가 아니라, AI와 비전문 연구자가 실제 연구수학을 수행한 과정 자체를 하나의 방법론적 사례로 보존하기 위한 초안이다.

주장하는 것은 “AI가 박사급 수학을 자동으로 해결했다”는 것이 아니다. 이 사례가 통계적으로 얼마나 희귀한지도 주장하지 않는다.

보존하려는 핵심은 다음이다.

> AI를 증명 생성기 하나로 사용하는 것이 아니라, 생성·공격·검산·문헌대조·기록·상태복원이라는 여러 역할로 분해하여 반복적으로 충돌시키고, 그 결과를 repository에 누적하는 연구 운영 방식.

---

## 1. 연구 질문의 변화

출발점은 다음과 같은 넓은 질문이었다.

> Demuškin 군의 filtration에서 canonical orientation을 복원할 수 있는가?

연구와 문헌대조가 진행되면서 이 질문 자체가 너무 넓다는 것이 드러났다. Demuškin canonical orientation의 존재와 유일성, Kummerian/cyclotomic characterization 자체는 기존 이론이기 때문이다.

따라서 질문을 다음 finite-window recognition problem으로 좁혔다.

고정된 rank-4, q=3 Demuškin group에 대해
Q_k = G/P_{k+1}(G)

를 두고 임의의 후보
rho : Q_k -> (Z/3^k)^×

에 대해 intrinsic Kummer lifting predicate

K_k(Q_k,rho):
H^1(Q_k,Z/3^k(rho)) -> H^1(Q_k,F_3)

의 surjectivity를 검사한다.

현재 수학적 연구의 핵심 정리는

K_k(Q_k,rho) iff rho = chi_G mod 3^k,  k >= 2

라는 finite-window recognition/factorization theorem이다.

여기서 canonical orientation 자체의 발견은 novelty claim에서 명시적으로 제외한다.

---

## 2. 핵심 방법론: 증명을 만드는 AI보다 증명을 공격하는 AI

일반적인 AI 수학 사용은

문제 -> AI 풀이 -> 정리

에 가깝다.

이번 연구에서는 다음 루프가 반복되었다.

생성
-> 공격
-> 재계산
-> 독립 검증
-> 문헌 대조
-> 범위 축소
-> 기록
-> 다음 가설

AI가 제시한 증명이나 계산을 결과로 취급하지 않고 우선 공격 대상으로 취급했다.

실제 repository에는 잘못된 finite-field rank 계산, Python/GAP transpose 오류, 차원만으로 subspace equality를 주장한 오류, 실행환경 실패와 수학적 실패를 혼동한 사례, Nielsen 변화에서 degree-3 Fox truncation이 intrinsic하지 않다는 반례, relator conjugation에서 raw t_2의 비자연성, graded information만으로 orientation을 복원하려는 시도의 실패 등이 남아 있다.

중요한 점은 이런 오류를 삭제하지 않았다는 것이다. 각각을 연구 경계와 재발 방지 자료로 보존했다.

---

## 3. 연구 계속성 원칙 — Continuity Principle

AI 연구에서 가장 위험한 문제는 계산 오류뿐 아니라 연구 상태의 손실이었다.

새로운 chat/window가 열릴 때마다 대화 기억을 권위 있는 연구 기록으로 취급하지 않고 repository를 권위로 삼았다.

현재 RESEARCH_CONTINUITY_PROTOCOL.md는 다음 복원 순서를 규정한다.

1. RESEARCH_MAP.md
2. CURRENT_STATE.md
3. research/00_RESEARCH_LOG.md
4. 해당 단계의 상세 audit 문서
5. 그 뒤에만 새로운 계산이나 논증 수행

핵심 원칙은 다음과 같다.

> 연구의 연속성은 AI의 기억력이 아니라 repository artifact와 상태 전이 기록에 의해 보장된다.

또한 후속 문서가 이전 결론을 수정하면 이전 기록을 삭제하지 않고 superseded 상태로 남긴다.

따라서 연구 계속성은 단순한 handover가 아니라 일종의 state discipline이 되었다.

---

## 4. 계속성 원칙의 실제 내용

연구가 복잡해지면서 단순한 “현재까지의 요약”으로는 부족했다.

같은 결과도

- theorem-level PASS인지,
- local computation인지,
- 조건부 결과인지,
- 완전히 폐쇄된 후보인지,
- 역사적이지만 현재는 superseded된 결론인지

를 구별해야 했다.

그래서 다음 표준 분류가 만들어졌다.

- PASS / CLOSED
- PASS / LOCAL
- FAIL / CLOSED
- OPEN
- CONDITIONAL
- HISTORICAL / SUPERSEDED

특히 later authoritative correction이 stale historical label보다 우선한다.

이것은 연구가 새로운 AI session으로 넘어가도 “무엇이 끝났고 무엇이 아직 열려 있는가”를 복원하게 한다.

---

## 5. 독창성 원칙 — Originality Principle

이번 연구에서 가장 중요한 방법론적 변화 중 하나는 “증명되었다”와 “새롭다”를 완전히 다른 질문으로 취급한 것이다.

초기에는 새로운 reconstruction 결과를 곧바로 novelty 후보로 볼 수 있었다. 그러나 문헌대조를 거치면서 다음은 명시적으로 prior art로 분리되었다.

- Demuškin canonical orientation의 존재
- canonical orientation의 유일성
- Kummerian/cyclotomic finite-level lifting criterion
- standard presentation의 orientation formula
- full-group finite-level uniqueness

따라서 다음 주장은 폐쇄했다.

> “Demuškin canonical orientation 자체를 새롭게 발견했다.”

대신 현재의 좁은 novelty candidate는

> bare finite quotient Q_k = G/P_{k+1}와 arbitrary candidate rho만을 입력으로 하여 intrinsic Kummer predicate가 canonical orientation의 reduction을 unique하게 recognize하는가?

로 정제되었다.

그리고 이것도 “최초의 정리”라고 선언하지 않는다.

현재 문헌감사의 안전한 표현은 다음과 같다.

> 감사한 문헌군에서 정확히 동일한 정리를 확인하지 못했다.

즉,

찾지 못했다 != 존재하지 않는다.

이 구분이 독창성 원칙의 핵심이다.

---

## 6. 독창성은 논문 마지막 단계가 아니라 연구 중간마다 검사한다

각 substantive branch마다 다음을 묻는다.

1. 이것은 기존 정리인가?
2. 기존 정리의 단순 재표현인가?
3. 기존 결과에서 즉시 따라오는가?
4. 기존 결과와 논리적 방향이 다른가?
5. input category가 다른가?
6. presentation-dependent calculation인가?
7. genuinely intrinsic construction인가?
8. novelty를 주장할 수 있는 가장 좁은 범위는 어디인가?

이 원칙 때문에 연구가 진행될수록 오히려 주장 범위가 좁아졌다.

이것은 연구의 후퇴가 아니라 독창성의 정밀화다.

---

## 7. 실패 보존 원칙 — Failure Preservation

실패한 접근을 삭제하지 않는다는 원칙이 이번 연구에서 매우 중요했다.

대표적인 경계는 다음과 같다.

### 7.1 Full associated graded

full mod-3 associated graded information만으로는 q-sensitive canonical orientation을 복원할 수 없다는 구조적 no-go가 기록되었다.

즉,

full mod-3 graded data does not determine chi mod 9.

### 7.2 Degree-3 Fox truncation

Nielsen-equivalent presentation에서 naive degree-3 Fox truncation이 presentation-independent intrinsic carrier가 되지 못함을 hard attack으로 확인했다.

결론:
presentation-independent degree-3 Fox truncation = FAIL / CLOSED.

### 7.3 Raw t_2

relator conjugation gauge test에서 raw t_2가 변하므로 단일 t_2를 canonical intrinsic secondary carrier로 사용하는 경로를 폐쇄했다.

### 7.4 Minimality

P_{k+1}이 충분하다는 것과 그것이 모든 admissible category에서 최소라는 것은 구별했다.

현재는

P_{k+1} sufficient = proved

이지만

P_{k+1} minimal = OPEN

이다.

따라서 manuscript에서는 “minimal finite window”가 아니라 “sufficient finite depth”라고 표현한다.

---

## 8. 정의가 계산보다 먼저라는 원칙

복잡한 수학 연구에서 계산부터 하고 나중에 의미를 찾는 방식은 위험했다.

그래서 substantive branch마다 계산 전에 다음을 확인한다.

1. Object — 정확히 무엇을 만드는가?
2. Input — 어떤 정보가 허용되고 무엇이 제외되는가?
3. Functoriality — 어떤 map/isomorphism에서 자연스럽게 움직이는가?
4. Gauge — presentation/lift/normalization 변화는 어떻게 처리되는가?
5. Orientation bridge — orientation data와 연결되는 정확한 map은 무엇인가?
6. q-blindness — q가 정의에 몰래 들어가지 않았는가?
7. Separation — 관련 사례를 실제로 구별할 수 있는가?
8. Novelty — 기존 정리의 재증명은 아닌가?

핵심 조건이 실패하면 계산을 중단하고 정의로 돌아간다.

따라서 이 연구에서 “계산을 많이 했다”보다 중요한 것은 “계산하기 전에 무엇을 계산해야 하는지와 무엇을 계산하면 안 되는지를 점점 더 명확히 했다”는 점이다.

---

## 9. 계산과 수학적 결론을 분리하는 원칙

repository의 운영 규칙은 다음과 같이 정리된다.

수학적 주장
-> 계산 설계
-> 독립 검증
-> CI 재현
-> 기록

실행 로그가 없는 결과는 공식 PASS로 부르지 않는다.

또한 오류를

- setup failure
- implementation failure
- invalid test
- mathematical failure
- mathematical pass

로 분리한다.

예를 들어 F_3 데이터를 real-field rank routine으로 계산해 얻은 숫자는 출력이 존재하더라도 수학적 결과가 아니다.

이런 사례는 antipattern으로 보존하여 재발을 막는다.

---

## 10. 문헌조사 원칙 — Literature as Methodology

문헌은 단순 bibliography가 아니었다.

각 중요한 논문에 대해 다음을 기록한다.

1. object
2. allowed input
3. invariance/naturality
4. obstruction mechanism
5. verification method
6. logical boundary
7. current project와의 possible factorization
8. direct implication 여부
9. novelty effect

이 방식은 “비슷한 키워드가 있으니 이미 알려졌다”는 식의 성급한 결론을 막았다.

예를 들어 기존 Kummerian literature가 이미 주어진 oriented pair (G,theta)에서 출발하는 것과, 현재 연구가 Q_k와 unknown candidate rho에서 출발하여 어떤 rho가 선택되는지를 묻는 것은 논리적으로 다른 문제다.

따라서 문헌과의 관계를 제목이나 키워드가 아니라 input-output 구조로 비교했다.

---

## 11. AI 역할 분해

이번 연구에서 AI는 하나의 역할이 아니었다.

### A. Generator
새로운 증명 후보, lemma, carrier, computation을 제안한다.

### B. Adversary
방금 만든 결과가 틀렸다고 가정하고 가장 강한 공격을 시도한다.

### C. Calculator
finite-field calculation, dimension check, exhaustive search 등을 수행한다.

### D. Auditor
코드와 수학적 주장이 일치하는지 확인한다.

### E. Literature analyst
existing theorem/proposition과 현재 결과의 논리적 관계를 비교한다.

### F. Recorder
PASS/FAIL/OPEN/HISTORICAL 상태를 기록한다.

### G. Continuity engine
다음 research session이 이전 상태를 복원할 수 있도록 state documents를 유지한다.

핵심은 같은 AI의 답변을 “증명”과 “검증”으로 동시에 취급하지 않는 것이다. 한 역할에서 나온 결과는 다른 역할의 공격 대상이 된다.

---

## 12. 인간의 역할

이번 사례에서 인간의 역할은 AI보다 계산을 더 빨리 하는 것이 아니었다.

핵심 판단은 다음이었다.

- 이 질문을 계속할 것인가?
- 이 계산을 믿어도 되는가?
- 이 결과는 정말 intrinsic한가?
- 이 실패가 단순 구현 오류인가, 구조적 no-go인가?
- 기존 문헌에 이미 있는가?
- 현재 가설을 폐쇄하고 다른 관점으로 넘어가야 하는가?
- 남은 open problem은 정확히 무엇인가?

특히 연구 방향을 바꾼 것은 단순한 계산 능력보다 “다른 관점에서 공격해 보라”는 요구를 반복한 것이었다.

따라서 이 사례를 “AI가 인간을 대신한 연구”로 표현하기보다,

> 인간이 연구 질문·공격 규칙·중단 규칙을 설정하고 AI가 대규모 생성·공격·계산·정리 작업을 반복 수행한 협업 구조

로 기록하는 것이 정확하다.

---

## 13. 연구가 발전한 실제 방식

연구는 직선적으로 진행되지 않았다.

초기에는 presentation, graded structure, module calculation, Fox expansion 등 여러 경로가 병렬적으로 탐색되었다.

그 과정에서 가능해 보이는 구조를 무조건 유지하지 않고 hard attack을 수행했다.

그 결과

graded -> insufficient

single t_2 -> non-intrinsic

naive Fox truncation -> non-natural

등의 경계가 형성되었다.

반대로

finite coefficient extension
-> arbitrary-candidate factorization
-> Kummer predicate
-> U5 variation
-> PD^2 uniqueness

경로가 살아남았다.

따라서 최종 정리는 처음부터 알고 있던 정리를 AI가 길게 써준 결과라기보다, 여러 후보를 폐쇄하면서 남은 구조를 재구성한 결과로 보는 것이 정확하다.

---

## 14. 연구 운영 원칙의 최종 목록

### 원칙 1 — Continuity
연구 상태의 권위는 대화 기억이 아니라 repository artifact에 둔다.

### 원칙 2 — Adversarial Verification
AI가 만든 결과는 우선 공격 대상이다.

### 원칙 3 — Definition Before Computation
계산 전에 object/input/invariance/gauge/bridge를 정의한다.

### 원칙 4 — Failure Preservation
실패한 경로와 오류를 삭제하지 않고 연구 경계로 보존한다.

### 원칙 5 — Claim Classification
모든 결과를 PASS/LOCAL/FAIL/OPEN/CONDITIONAL/HISTORICAL 등으로 분류한다.

### 원칙 6 — Independence
서로 다른 연구 track이나 검증 방법은 가능한 한 독립적으로 유지한다.

### 원칙 7 — Reproducibility
수학적 결과와 computational evidence를 분리하고 실행 ID와 검증 경로를 보존한다.

### 원칙 8 — Literature Before Novelty
새로운 정리라고 부르기 전에 기존 theorem의 정확한 input/output과 비교한다.

### 원칙 9 — Narrowest Defensible Claim
가장 넓은 주장이 아니라 증명 가능한 가장 좁은 주장을 발표한다.

### 원칙 10 — No Silent Revival
폐쇄된 접근은 새로운 정의나 근거 없이 다시 살리지 않는다.

### 원칙 11 — Scope Control
q-blind, intrinsic, presentation-free, sufficient, minimal 같은 용어는 정확한 정의 아래에서만 사용한다.

### 원칙 12 — Human-AI Role Separation
AI의 생성·공격·계산·감사를 서로 다른 검증 역할로 취급한다.

---

## 15. 이 사례의 핵심 방법론적 관찰

이번 경험에서 가장 중요한 것은 특정 AI 모델의 수학 능력만이 아니다.

오히려 다음 가설을 시험한 사례에 가깝다.

> 연구수학에서 AI의 유용성은 한 번에 올바른 증명을 생성하는 능력보다, 많은 후보를 빠르게 생성하고 서로 공격하게 하며, 실패한 경로를 보존하고, 살아남은 구조를 문헌과 대조하면서 연구 상태를 지속적으로 관리하는 능력에서 크게 증가할 수 있다.

이것은 이번 repository의 실제 연구 과정에서 관찰된 운영 패턴에 기반한 방법론적 가설이지, 일반적인 통계적 우월성의 주장으로 확대하지 않는다.

---

## 16. “열흘”의 의미

짧은 기간이라는 사실 자체보다 중요한 것은 연구 상태가 매일 축적되었다는 점이다.

하루의 결과가 다음날 사라지지 않도록

state -> audit -> correction -> next gate

의 형태로 기록했다.

따라서 “10일 만에 무엇을 했다”는 표현은 속도만 강조하면 오해의 소지가 있다.

더 정확한 표현은:

> 짧은 기간 동안 지속적인 기록·검증·공격·문헌대조가 누적된 연구 과정

이다.

---

## 17. 현재 기록으로 주장할 수 있는 것과 없는 것

### 주장할 수 있는 것

- AI와 비전문 연구자의 협업으로 실제 연구수학의 가설 생성·반증·검증·문헌대조·논문화 과정이 수행되었다.
- 연구 계속성을 위해 repository 기반의 명시적 continuity protocol이 만들어졌다.
- novelty를 연구 과정 중 지속적으로 하향조정하고 정확한 경계를 기록했다.
- 실패와 오류를 삭제하지 않고 재발 방지 및 구조적 no-go의 자료로 보존했다.
- 최종적으로 좁은 finite-window recognition theorem 형태의 수학적 초안까지 발전했다.
- 그 과정 전체를 Git history와 research documents로 재구성할 수 있다.

### 현재 주장하지 않는 것

- 이 사례가 통계적으로 세계 최초 또는 극히 희귀하다는 정량적 주장
- AI가 인간 수학자를 일반적으로 대체할 수 있다는 주장
- canonical Demuškin orientation 자체가 새로운 발견이라는 주장
- 현재 theorem이 모든 Demuškin family에 uniform하게 성립한다는 주장
- P_{k+1}이 절대적으로 minimal한 finite window이라는 주장
- 현재 문헌에 동등한 정리가 절대로 존재하지 않는다는 주장

---

## 18. 후속 검증 과제

이 문서는 방법론적 사례 기록의 초안이다.

후속 단계에서는 다음을 실제 Git history와 대조하여 보강할 필요가 있다.

1. 주요 연구 전환점을 시간순으로 복원한다.
2. 각 전환점에서 인간의 결정과 AI의 제안을 구분한다.
3. 주요 실패가 언제 발견되고 언제 폐쇄되었는지 commit과 연결한다.
4. 문헌대조 범위와 한계를 명시한다.
5. AI-assisted mathematics research라는 방법론적 해석이 실제 기록으로 충분히 뒷받침되는지 외부 관점에서 검토한다.
6. 수학적 성과와 AI 협업 방법론의 성과를 별개의 두 축으로 분리한다.

---

## 19. 잠정 결론

이번 Demuškin 연구의 가장 중요한 기록은 하나의 정리를 얻었다는 사실만이 아니다.

연구 과정에서 다음 운영체계가 실제로 형성되었다.

연구 질문
-> 정의/입력/범위 고정
-> AI 생성
-> AI 상호공격
-> 독립 계산/검증
-> 문헌 대조
-> PASS/FAIL/OPEN 분류
-> 즉시 기록
-> 다음 연구 세션에서 상태 복원

그리고 이를 지탱한 핵심 원칙은

Continuity
+
Adversarial Verification
+
Originality Discipline
+
Failure Preservation
+
Reproducibility

이다.

따라서 이 사례를 기록할 때 가장 중요한 것은 “AI가 열흘 만에 박사급 증명을 만들었다”는 식의 결과 중심 서술이 아니다.

더 정확한 기록은 다음과 같다.

> AI가 생성한 수학을 그대로 믿지 않고, AI를 생성자이자 공격자이자 계산자이자 감사자로 분해하여 반복적으로 충돌시키고, 그 과정에서 연구 계속성·독창성·재현성·실패 보존의 원칙을 repository 수준의 운영 규칙으로 발전시킨 실제 연구 사례.

이 문서는 이후 Git history와 dated research records를 대조하여 보강한다.

---

## 상태

- 문서 성격: 방법론적 사례 기록 초안
- 수학적 연구의 권위: RESEARCH_MAP.md / CURRENT_STATE.md / research/00_RESEARCH_LOG.md
- 문헌대조 권위: research/LITERATURE_AUDIT_DETAILED_2026-09-25.md
- 연구 계속성 규칙: research/RESEARCH_CONTINUITY_PROTOCOL.md
- novelty controlling record: research/N1_N5_CRITICAL_REVIEW_2026-09-24.md
- 현재 finite-window theorem: PASS / CLOSED
- exact publication-level novelty: OPEN / CONDITIONAL
- broad canonical-orientation novelty: CLOSED / NON-NOVEL
- finite-depth minimality: OPEN
