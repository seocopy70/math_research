# 00. START HERE — 연구 입문·전체 그림·수학적 기여 안내서
## 2026-09-28

> 이 문서는 연구를 처음 다시 볼 때 가장 먼저 읽는 안내서다.
> 기존 authoritative proof/audit 문서와 실제 연구기록을 대체하거나 합치지 않는다.

## 1. 이 연구를 한 문장으로

> 무한한 Demuškin 군에서 전역적으로 존재하는 canonical orientation을, 얼마나 작은 유한한 filtered data만으로 intrinsic하게 알아낼 수 있는가?

쉽게 말하면:

> 무한한 미로에서 진짜 방향표지판을 찾기 위해, 미로의 유한한 지도 조각만 가지고 어디까지 볼 필요가 있으며, 그 지도에서 진짜 표지판을 어떻게 골라낼 것인가?

## 2. 핵심 비유

| 이야기 | 수학 |
|---|---|
| 무한한 미로 | Demuškin pro-p group G |
| 진짜 방향표지판 | canonical orientation χ_G |
| 후보 표지판 | candidate orientation ρ |
| 유한한 지도 | finite quotient / filtered window Q_k |
| 지도 깊이 | filtration depth |
| 표지판 시험 | finite Kummer recognition predicate |
| 잘못된 표지판의 실패 | obstruction / Kummer failure |
| 진짜 표지판만 통과 | uniqueness |
| 정확한 지도 깊이 | p^(k−1)+1 |
| 증명용 obstruction carrier | transgression quotient O_k |
| selector의 최종 1차 신호 | finite cup-product line C_k |

핵심은 **유한한 지도 그 자체가 답이 아니라, 유한한 지도 + 그 지도 위에서 작동하는 판별법**이라는 점이다.

## 3. 세 논문을 하나의 이야기로

### Paper 1 — 찾을 수 있는가?

무한한 대상을 전부 보지 않고도 global orientation을 finite data로 인식할 수 있는가?

→ **finite recognition/factorization의 가능성**을 세운다.

### Paper 2 — 어디까지 봐야 하는가?

관련 affine crossed-cocycle 정보가 사라지지 않으려면 지도를 얼마나 깊게 만들어야 하는가?

→ 선언된 affine crossed-cocycle 관측 범주에서

p^(k−1)+1

이라는 정확한 sharp depth를 얻는다.

### Paper 3 — 실제로 골라낼 수 있는가?

그 finite window에서 arbitrary candidate ρ를 Kummer predicate로 시험한다.

K_k(Q_k, ρ) ⇔ ρ = χ_G mod p^k

→ canonical orientation을 유일하게 인식한다.

또한 selector가 사용하는 정보를 선언된 linear selector-carrier 범위에서 1차원 finite cup-product line으로 압축하고 그 범주 안의 minimality를 닫는다.

## 4. 전체 흐름도

```text
무한한 Demuškin group G
        │
        ▼
  global orientation χ
        │
        ▼
Paper 1: finite recognition 가능?
        │  YES
        ▼
Paper 2: 필요한 정확한 정보 깊이는?
        │  p^(k−1)+1
        ▼
Q_k = G / P_(p^(k−1)+1)(G)
        │
        ▼
Paper 3: finite Kummer recognition
        │
        ├── false candidate → obstruction
        │
        └── true candidate  → 통과
                    │
                    ▼
              유일한 canonical χ
                    │
                    ▼
       selector 정보의 압축
                    │
                    ▼
       finite cup-product line C_k
       (선언된 linear category에서 1차원)
```

## 5. 수학적으로 한 단계 더

finite window는

Q_k = G / P_(p^(k−1)+1)(G)

이다.

Paper 2는 관련 affine crossed-cocycle 정보가 이 quotient를 통해 factor한다는 것을 sharp하게 보인다.

Paper 3는 finite central extension E_k → Q_k와 transgression quotient

O_k = H²(Q_k,F_p) / im(tra_k)

를 proof carrier로 사용한다.

false candidate의 첫 p-adic 차이를

ρ'_k = χ_k(1 + p^(k−1)ν)

로 보고, variation을 ν ∪ f̄로 내려 Demuškin PD²의 nondegenerate cup pairing으로 false candidate를 분리한다.

최종 selector 쪽에서는

C_k = im(H¹(Q_k,F_p) ⊗ H¹(Q_k,F_p) → H²(Q_k,F_p))

라는 finite cup-product image를 사용한다.

## 6. 세 논문의 수학적 기여를 한 줄씩

- **Paper 1:** finite recognition이 가능하다는 구조.
- **Paper 2:** 관련 affine 관측 범주에서 필요한 정보의 깊이를 정확히 p^(k−1)+1로 결정하고 sharpness를 보인 것.
- **Paper 3:** 그 finite window에서 Kummer selector가 canonical orientation을 유일하게 인식하고, 선언된 linear selector-carrier 범위에서 결정적 1차 정보를 1차원으로 압축한 것.

전체를 압축하면:

**finite data → exact information threshold → intrinsic unique recognition**

## 7. 기여도를 평가해서 보고 싶다면

가장 먼저 읽을 평가 문서는:

**research/THREE_PAPER_MATHEMATICAL_CONTRIBUTION_ASSESSMENT_2026-09-28.md**

이 문서는 세 논문의 질문, 핵심 결과, 난이도, 전체 기여, 강점과 제한점, novelty boundary를 종합한다.

특히 다음 구조를 중심으로 평가한다:

Recognition → Sharp information threshold → Recognition at the sharp window

주의: 이 문서는 authoritative theorem/proof record가 아니라 종합 평가 문서다.

## 8. 쉽게 설명한 문서는 여기

**research/THREE_PAPER_STORY_AND_MATH_EXPLANATION_2026-09-28.md**

- 무한 미로 / 유한 지도 / 진짜 방향표지판 이야기
- 비유 ↔ 수학 대응표
- 용어집
- 쉬운 수학적 설명
- 세 논문의 연결 구조

## 9. 연구가 왜 시작됐는지

**research/01_MATHEMATICAL_MOTIVATION.md**

초기 연구 질문, filtration을 보게 된 이유, degree-4 probe와 symplectic orbit가 왜 등장했는지를 설명한다.

이 문서는 연구동기용이다. 최신 판정의 권위 문서가 아니다.

## 10. 기술적 전체 로드맵

**research/02_GLOBAL_ROADMAP.md**

Phase 0 → Phase 1 → Phase 2 → Track B → orientation reconstruction으로 이어지는 기술적 경로를 보여준다.

## 11. 현재 상태를 정확히 확인할 때

여기부터는 authoritative 영역이다.

1. **CURRENT_STATE.md** — 최신 수학적 상태와 PASS/FAIL/CLOSED/OPEN 분류
2. **RESEARCH_MAP.md** — 전체 연구 구조와 문서 지도
3. **research/00_RESEARCH_LOG.md** — 날짜순 실제 연구기록
4. **개별 audit/proof 문서** — 특정 주장에 대한 실제 증명·감사

설명 문서와 authoritative 상태가 다르게 보이면 authoritative 문서를 따른다.

## 12. 권장 읽기 순서

```text
① 00_START_HERE.md
       ↓
② THREE_PAPER_STORY_AND_MATH_EXPLANATION
       ↓
③ THREE_PAPER_MATHEMATICAL_CONTRIBUTION_ASSESSMENT
       ↓
④ PAPER3_MIDPOINT_SUMMARY
       ↓
⑤ CURRENT_STATE
       ↓
⑥ RESEARCH_MAP
       ↓
⑦ 00_RESEARCH_LOG + 개별 proof/audit
```

연구의 역사와 시행착오를 따라가려면:

```text
01_MATHEMATICAL_MOTIVATION
       ↓
02_GLOBAL_ROADMAP
       ↓
00_RESEARCH_LOG
       ↓
개별 Phase / Gate / Audit
       ↓
현재 authoritative state
```

## 13. 문서 역할을 섞지 않는 원칙

이 START HERE는 기존 문서를 한 파일로 합친 것이 아니다.

| 문서 | 역할 |
|---|---|
| 00_START_HERE.md | 입문·전체 그림·읽기 안내 |
| THREE_PAPER_STORY_AND_MATH_EXPLANATION | 쉬운 비유 + 수학 번역 |
| THREE_PAPER_MATHEMATICAL_CONTRIBUTION_ASSESSMENT | 세 논문의 수학적 성과·기여 종합 평가 |
| 01_MATHEMATICAL_MOTIVATION | 연구동기 |
| 02_GLOBAL_ROADMAP | 기술적 전체 로드맵 |
| CURRENT_STATE | 최신 authoritative 상태 |
| RESEARCH_MAP | 전체 연구 구조·문서 지도 |
| 00_RESEARCH_LOG | 실제 연구 과정의 시간순 기록 |
| 개별 audit/proof 문서 | 특정 주장에 대한 실제 검증 |
| paper/, paper3/ | 원고·출판 artifact의 구조와 상태 |

따라서 **기존 권위 문서와 실제 연구기록은 이동·삭제·통합하지 않는다.**

이 문서는 그 문서들을 위에서 내려다보는 **목차이자 학습 경로**다.

## 14. 한 문장으로 기억하기

> **Paper 1은 “찾을 수 있다”, Paper 2는 “어디까지 봐야 하는가”, Paper 3은 “그만큼 보면 실제로 골라낼 수 있다”.**

그리고 전체 연구를 한 장면으로 기억하면:

> **무한한 미로 전체를 돌아다니지 않고, 충분하지만 필요 이상으로 크지 않은 유한한 지도 조각을 만든 뒤, 그 지도 위에서 진짜 방향표지판만 통과하는 판별법을 찾아낸다.**

## 문서 상태

이 문서는 **학습·탐색용 START HERE**다.

- 연구 판정의 권위: CURRENT_STATE.md, RESEARCH_MAP.md, research/00_RESEARCH_LOG.md, 개별 authoritative proof/audit
- 수학적 기여 종합 평가: research/THREE_PAPER_MATHEMATICAL_CONTRIBUTION_ASSESSMENT_2026-09-28.md
- 쉬운 설명: research/THREE_PAPER_STORY_AND_MATH_EXPLANATION_2026-09-28.md

마지막 업데이트: 2026-09-28