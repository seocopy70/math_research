# Phase 2-13C 현재 진행 기록 — 2026-09-16

## 1. 현재 연구 단계의 쉬운 설명

현재 연구의 핵심 질문은 다음과 같다.

> 35차원 공간 E 안에서 발견된 1차원 방향이 정말로 표현론적으로 특별한 방향인지, 그리고 그 방향이 어떤 weight/character를 갖는지를 정확히 판정할 수 있는가?

현재까지 다음 구조가 계산으로 확립되어 있다.

\[
W\cong \Lambda^2(\operatorname{Sym}^2 V),\qquad \dim W=45,
\]

그리고 H=Sp_4(F_3)-stable한 10차원 부분모듈

\[
U\cong \operatorname{Sym}^2 V,
\qquad \dim U=10
\]

을 얻어

\[
E=W/U,
\qquad \dim E=35
\]

를 정의했다.

Phase 2-11-A에서

\[
0\to M_{25}\to E_{35}\to \operatorname{Sym}^2(V)_{10}\to0
\]

가 비분할(non-split)임을 확인했다.

Phase 2-12에서는 자연스러운 차원 후보였던 \(\operatorname{Sym}^4(V)\)와 E가 동형이 아님을 확인했다.

그 다음 Phase 2-13B에서 C2의 positive-unipotent subgroup \(U^+(F_3)\)를 정확히 구성했고

\[
|U^+(F_3)|=81,
\qquad
\dim E^{U^+(F_3)}=1
\]

을 확인했다.

즉 E 안에는 positive-unipotent 작용으로 고정되는 방향이 정확히 하나 있다. 이것은 '최고중량 벡터(highest-weight vector)'가 있을 가능성을 강하게 시사하는 신호지만, 이것만으로 어떤 표현인지 확정할 수는 없다.

따라서 다음 단계는 이 1차원 고정선에 split torus

\[
T(F_3)\cong(F_3^\times)^2\cong(Z/2)^2
\]

가 어떻게 작용하는지를 측정하는 것이다.

---

## 2. 왜 지금 sanity check가 필요한가

기존 Phase 2-13C 계산은 torus가 fixed line을 보존한다는 사실까지는 확인했지만, 출력된 character table

\[
(1,1)\mapsto2,\quad
(1,2)\mapsto1,\quad
(2,1)\mapsto1,\quad
(2,2)\mapsto2
\]

는 수학적으로 불가능했다.

이유는 간단하다.

identity \((1,1)\)은 반드시 1로 작용해야 하며, character는 곱셈을 보존해야 한다.

더 강하게는

\[
T(F_3)\cong(Z/2)^2
\]

이므로 \(\operatorname{Hom}(T(F_3),F_3^\times)\)에는 정확히 네 개의 character밖에 없다.

좌표 순서를

\[
(1,1),(1,2),(2,1),(2,2)
\]

로 고정하면 가능한 네 character는 정확히

| character | (1,1) | (1,2) | (2,1) | (2,2) |
|---|---:|---:|---:|---:|
| trivial | 1 | 1 | 1 | 1 |
| first coordinate | 1 | 1 | 2 | 2 |
| second coordinate | 1 | 2 | 1 | 2 |
| product | 1 | 2 | 2 | 1 |

뿐이다.

따라서 현재 sanity check는 단순히 identity와 multiplicativity만 확인하는 것이 아니라, 최종적으로 계산된 character tuple이 **위 네 가지 중 정확히 하나와 일치하는지**까지 강제한다.

---

## 3. 현재 구현 상태

`research/phase2_13C_torus_character_2026-09-16.py`는 실제로 다음 symbol을 제공한다.

- `torus`
- `quotient_action_single`
- `fixed`

따라서 강화된 sanity-check script의 source-interface 가정은 현재 파일과 일치한다.

현재 sanity-check script:

`research/phase2_13C_sanity_check_2026-09-16.py`

현재 SHA:

`a687ce1efde5a26d33ba7fc69570c1e44cf608a3`

검사 내용:

1. \(t(1,1)=I_4\)
2. torus의 16개 곱셈법칙 전부 확인
3. \(\rho(1,1)=I_{35}\)
4. torus representation law의 16개 경우 전부 확인
5. fixed line basis vector가 정확히 하나이고 nonzero인지 확인
6. torus가 그 line을 보존하는지 정확한 F_3 rank 계산으로 확인
7. 각 torus 원소의 scalar를 정확히 추출
8. \(\chi(1,1)=1\) 확인
9. character multiplicativity의 16개 경우 전부 확인
10. 추출된 character가 위의 네 character 중 **정확히 하나**인지 exhaustive classification으로 확인

마지막 조건을 통과하지 못하면 script는 강제로 실패한다.

---

## 4. 현재 상태의 엄격한 판정

중요하게도, **강화된 sanity-check workflow의 성공 실행 로그는 아직 확보되지 않았다.**

따라서 현재 단계에서 다음을 주장해서는 안 된다.

- 특정 torus character가 확정되었다.
- 특정 highest weight가 확정되었다.
- E가 특정 Weyl/simple/tilting module이라고 확정되었다.

현재 확정된 것은 다음까지다.

\[
\boxed{\dim E^{U^+(F_3)}=1}
\]

그리고 torus character sanity check가 위의 네 가능한 character 중 정확히 하나를 선택하도록 구현되어 있다는 사실이다.

---

## 5. 다음 연구 단계

### Step 1 — Phase 2-13C sanity check 실제 실행

강화된 script를 GitHub Actions에서 실행하여 실제 출력값을 확인한다.

반드시 다음 형태의 결과가 있어야 한다.

\[
\chi\in\{(1,1,1,1),(1,1,2,2),(1,2,1,2),(1,2,2,1)\}
\]

그리고 정확히 하나가 `MATCHED_CHARACTER`로 출력되어야 한다.

### Step 2 — character에서 finite-field weight 정보 추출

sanity check가 통과하면 해당 character를 C2 torus의 weight 정보와 대응시킨다.

다만 F_3에서는 torus가 각 좌표별로 order 2밖에 가지지 않으므로 서로 다른 algebraic highest weights가 같은 mod-3 character로 내려갈 수 있다는 점을 명시적으로 고려한다.

따라서 finite-field character 하나만으로 곧바로 full algebraic highest weight를 선언하지 않는다.

### Step 3 — highest-weight candidate 검증

\(U^+\)-fixed line과 torus character를 함께 이용하여 후보 highest-weight를 좁힌다.

필요하면 negative-root action, Weyl conjugates, weight multiplicity 등을 추가 계산한다.

### Step 4 — E의 정확한 표현론적 정체 확인

최종적으로는

\[
E=W/U
\]

가 어떤 정확한 \(Sp_4(F_3)\) 또는 \(PSp_4(F_3)\) 모듈인지 독립적인 certificate로 확인한다.

이 단계 역시 단순한 dimension matching으로 결론내리지 않는다.

---

## 6. 연구 전체에서의 위치

현재 연구는 두 독립 트랙으로 진행된다.

### Track A — 표현론적 구조

\[
T
\to W_{45}
\to U_{10}\n\to E_{35}
\to U^+(F_3)\text{-fixed line}
\to T(F_3)\text{-character}
\to \text{highest-weight 후보}
\]

현재 위치는 **torus character sanity audit**이다.

### Track B — 군론/산술적 bridge

\[
uv
\to(uv)^3
\to gr_3,gr_4
\to A1/A2/A3
\]

현재 A1, A2는 closed이고 A3가 진행 중이다. A3에서는

\[
C(x_1)=x_2x_1x_2^{-1}
=x_1[x_1,x_2^{-1}]
\]

에 대해

\[
gr_1(C(x_1))=X_1,
\qquad
gr_2(C(x_1))=[X_3,X_4]
\]

까지 정확히 확인되었으며, degree 3과 degree 4의 완전한 계산이 다음 목표다.

---

## 7. 보존 원칙

이 연구에서는 다음 원칙을 계속 유지한다.

\[
\boxed{\text{컴퓨터 발견}\to\text{명시적 certificate}\to\text{수학적 설명}\to\text{독립 검산}}
\]

특히 이번 Phase 2-13C에서는 이전의 불가능한 character table을 발견한 것을 실패가 아니라 **검증 장치가 실제로 작동한 사례**로 기록한다.

연구의 최종 질문인 filtration으로부터 canonical orientation을 복원할 수 있는지는 여전히 OPEN이다.
