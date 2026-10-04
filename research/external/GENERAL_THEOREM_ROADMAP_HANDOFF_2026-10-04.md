# 일반정리 로드맵 (핸드오프 문서) — 2026-10-04

업로드 위치 제안: `research/external/GENERAL_THEOREM_ROADMAP_HANDOFF_2026-10-04.md`
작성: Claude. 짝 문서: `CLAUDE_PAPER4_REVIEW_AND_DICHOTOMY_2026-10-04.md`

## 0. 이어받는 AI에게

- 상태 라벨: **PROVED-HAND**(손 증명, 독립 검산 전) / **VERIFY**(계산·문헌 확인 필요) / **CONJ**(추측) / **OPEN**.
- PROVED-HAND도 독립 재증명 또는 GAP 확인 전에는 논문에 PASS로 쓰지 말 것.
- 연구 원칙(레포와 동일): 컴퓨터 발견 → certificate → 수학적 설명 → 독립 검산. 계산은 증명을 대체하지 않는다.
- 문헌의 정리 번호·정확한 진술은 이 문서에 적지 않았다. 인용 전에 반드시 원문 확인(Labute, Anick, Forré, Mináč–Rogelstad–Tân 등).

## 1. 목표와 현재 위치

원래 목표: `z^{p^s} = r` 꼴 relator에 대한 유한 Zassenhaus 창 일반정리(어느 깊이에서 s가 보이는가) + 비강성(조대한 불변량이 s를 못 본다).

원고(Paper4_final)는 Demuškin 스트레스 가족만 다룬다. 이번 검토의 핵심 변화:

1. 원고 Thm 5.1(위수 점프에 의한 unmarked 분리)은 틀렸다. 위수는 같다.
2. 대신 **임의의 r에 대한 위수 수준 일반정리(Theorem OD)** 가 손으로 증명된다. 올바른 가설은 "차수"가 아니라 "z^{p^s}가 r-창에서 살아남는다(H_z)"이다.
3. 비자명한 모든 경우(S 영역)에서 위수로는 절대 안 갈리므로, 진짜 문제는 전부 확대이론(marked/unmarked)이다.

## 2. 설정과 표기

- p 홀수. F = 자유 pro-p군 (생성원 z, x_1..x_d). F_x = x들이 생성하는 부분. D_n = Zassenhaus 필트레이션.
- r ∈ Φ(F). G_{s,r} = F/<<z^{p^s} r^{-1}>>, ρ_s = z^{p^s} r^{-1}.
- m(r) = ord_Z(r) = max{k : r ∈ D_k(F)}.
- n = p^s + 1, Φ_n = F/D_n(F), c = z^{p^s} (Φ_n의 원소). t > s.
- R = <<r>> (Φ_n 안의 정규폐포 = <<r>>D_n/D_n), Q = Φ_n/(R·<c>).
- 가설 **H_z**: c ∉ R, 즉 z^{p^s} ∉ <<r>>D_n(F), 즉 c ≠ 1 in W_n(G_{t,r}) (t ≥ s+... 어떤 t>s든 같음).
  - r이 z를 포함하지 않으면(z-free) H_z는 항상 성립. witness: F → Z/p^{s+1}, z ↦ 1, x ↦ 0.
  - r = z^p 같은 경우는 H_z가 깨진다 (원고 Prop 8.1의 진짜 원인).

## 3. 증명된 사실 (PROVED-HAND)

**L1 지연 가시성.** n ≤ p^s이면 W_n(G_{s,r}) = F/(D_n(F), r). (원고 Lemma 3.1, r 무가설)

**L2 c는 중심.** c ∈ D_{p^s}(F), [D_{p^s}, D_1] ⊆ D_{p^s+1} = D_n 이므로 c는 Φ_n의 중심 원소. c^p = z^{p^{s+1}} ∈ D_n 이므로 위수 ≤ p.

**L3 공통 몫.** n ≤ p^t이므로 W_n(G_t) = Φ_n/R. 또 W_n(G_s)/<c> = Φ_n/<<ρ_s, c>> = Φ_n/(R·<c>) = Q = W_n(G_t)/<c>.
H_z 하에서 |<c>| = p in W_n(G_t), 따라서 |W_n(G_t)| = p|Q|.

**Theorem OD (위수 이분법).** H_z를 가정하고 m = m(r)이라 하자. n = p^s + 1에서:
- m ≥ p^s + 1 이면 (N): c가 W_n(G_s)에서 죽고 |W_n(G_t)| = p|W_n(G_s)|. 비동형. (사실 r ∈ D_n이라 relator가 창에서 사라지고 z^{p^s} = 1이 됨.)
- m ≤ p^s 이면 (S): c가 생존하고 |W_n(G_s)| = |W_n(G_t)| = p|Q|. 둘 다 같은 Q의 Z/p 중심확대. 위수로는 분리 불가.

증명 (핵심 단계):
1. M = <<ρ_s>>D_n/D_n, M' = R·<c>. M ⊆ M'.
2. c가 중심이므로 ρ^g ρ^{-1} = (r^{-1})^g r. 따라서 M ⊇ [R, Φ_n].
3. Φ_n/[R,Φ_n]에서 r, c는 중심. B := M'/[R,Φ_n] = <r̄> × <c̄> ≅ Z/p^e × Z/p. (교집합이 자명한 이유: c ∉ R, c 위수 p.)
4. M/[R,Φ_n] = <ρ̄> = <(-1, 1)>. c̄ = (0,1) ∈ <ρ̄> ⇔ e = 0. (e ≥ 1이면 k ≡ 0 mod p^e 이면서 k ≡ 1 mod p 불가능.)
5. 따라서 N ⇔ e = 0 ⇔ r ∈ [<<r>>, F]·D_n(F).
6. R ⊆ D_m이므로 [<<r>>, F] ⊆ D_{m+1}. m ≤ p^s이면 D_n ⊆ D_{m+1}이고 r ∉ D_{m+1}이므로 r ∉ [<<r>>,F]D_n, 즉 S. m ≥ p^s+1이면 r ∈ D_n, 즉 N. ∎

따름:
- Demuškin 가족(m = 2 ≤ p^s)은 전부 S. 원고의 위수 분리 주장은 철회.
- abelian 판별(원고 Thm 5.1 대체용): z-free r에서 r̄ ∉ p^{s+1}F_x^{ab} 이면 abelianization에서도 c가 생존.
- 원고 Prop 8.1: "차수만으로 부족"은 사실이지만 원인은 H_z 실패. z-free이면 위수 수준에서는 차수가 정확한 판별량이다.

**L4 (unmarked ↔ 궤도 문제).** S 영역에서 W_n(G_s) ≅ W_n(G_t) ⇔ 어떤 α ∈ Aut(Φ_n)에 대해 α(<<ρ_s>>D_n) = <<r>>D_n.
증명: 동형 β의 생성원 lift로 F → Φ_n을 만들면 D_n 함수성으로 Φ_n의 자기사상 α가 생기고, 전사(Frattini)라 자기동형. 위수가 같으므로 정규부분군이 일치. ∎
Aut(Φ_n) → GL_{d+1}(F_p)는 전사이고 핵은 p-군.

**(VERIFY) L5 (확대류 분해).** Ẽ = Φ_n/[R,Φ_n]는 Q의 중심확대(핵 B). W_n(G_t) = Ẽ/<r̄>, W_n(G_s) = Ẽ/<r̄^{-1}c̄>. 따라서 두 확대류는 e_s = e_t + κ_r (κ_r = relator r의 transgression 류, H^2(Q,F_p)). unmarked 분리 = e_s와 e_t가 Aut(Q)(및 스칼라) 궤도로 갈리는가.

## 4. 일반정리 후보 (목표 진술)

**Theorem A (위수, 일반 r).** Theorem OD. 상태: PROVED-HAND, GAP 검증 필요.

**Theorem B (marked, S 영역).** marked 몫 π: G_s → G_∞ = F/<<r>>(z 죽임)에 대해 n ≤ p^s에서 split, p^s+1에서 nonsplit이 되는 일반 가설 H_B를 찾기. 상태: OPEN.
- N 영역(r ∈ D_n)에서는 항상 split (x_i ↦ x_i가 섹션).
- S 영역에서 split 여부는 미묘하다. 예: r = x^p, s = 1은 섹션 x ↦ x z^{-1}이 (zx^{-1})-꼴 3차 교환자항(Hall–Petrescu의 c_3)에 좌우된다. 반드시 이런 작은 경우부터 계산하고 가설을 추측할 것.
- 원고 Thm 6.1은 Demuškin 가족의 특수 사례로 남기되 증명을 완전하게 다시 써야 함 (a ≥ 2 metabelian witness 명시, a = ∞ 별도 처리, 깨진 문장 복구).

**Theorem C (unmarked).** L4/L5를 이용해 e_s ≠ e_t (궤도 분리) 증명. 상태: OPEN. 아이디어:
- Demuškin: 형식 ρ_D의 radical이 정확히 <Z> 한 줄이므로 GL 안정화군이 <Z>를 보존한다. 이 canonical 직선 위에서 restricted p^s-제곱 사상 Z^{[p^s]}가 정의되고, N_s와 N_t의 필트레이션 차이가 이 직선의 p^s-power에 걸린다. 이를 gr 수준 불변량으로 만들 수 있는지 시험.
- 소형 사례(rank 2, p=3, s=1, r = x^3): 임의 원시원소 g의 g^3이 z^3x^{-3}와 일치할 수 없다는 Hall–Petrescu 3차항 논증으로 비동형이 나온다 (발견적, VERIFY). 이를 일반화하는 게 첫 목표.
- 보조: 큰 군의 Aut-궤도 계산은 불가능하므로 gr 불변량(레이어별 차원, GL-표현으로서의 gr N)으로 먼저 분리 시도.

**Theorem D (비강성, z-free r 일반).**
- (i) 2차 jet: in(ρ_s) = in(r)가 s와 무관. 조건 m(r) < p (p 홀수, 2차는 자동).
- (ii) abelianization: G^{ab} = Z_p^{d+1}/(p^s e_z − r̄). r̄ = p^a w (w 원시 또는 r̄ = 0, a = ∞)일 때 a < s이면 Z_p^d ⊕ Z/p^a (s-blind), a ≥ s이면 Z_p^d ⊕ Z/p^s (s-dependent). 즉 **a = ∞(G_{s,∞})에서는 abelianization이 s를 본다.** 원고 초록의 "s-독립" 주장은 a < s에만 맞다.
- (iii) 혼합 mod-p 코호몰로지 환: z-free r에서 cup product가 r의 교환자 부분만으로 정해져 s-blind. 단 Bockstein은 s = 1에서 z^p 항 때문에 달라질 수 있다 (VERIFY).
- (iv) 인용할 정리(one-relator cd 2, cup product 기술)의 정확한 진술을 문헌에서 확인해 증명에 박을 것. 현재 원고는 "the one-relator cohomology theorem"으로 얼버무림.

## 5. 단계별 계획 (순서대로)

**Phase 1 — 검증 (최우선).** Theorem OD를 GAP로 확인.
- 방법: PQuotient(F/[ρ], 3, n)으로 P_n 몫을 만든 뒤 JenningsSeries로 D_n을 나눠 W_n 구성 (P_k ⊆ D_k이므로 P_n 몫에서 D_n 나눠도 W_n과 같음).
- 사례(p=3): (a) s=1, n=4, F=<z,x>: r=x^3 (S 예상), r=x^9 (N 예상). (b) s=1, n=4, F=<z,x1,x2>: r=[x1,x2] (S 예상). (c) 가능하면 s=2, n=10.
- 확인 항목: |W_n(G_s)| vs |W_n(G_t)|, c의 위수, Q의 크기, Z/p 중심확대 구조.
- 합격 기준: N 사례에서만 위수 차이가 p배, S 사례에서는 위수 일치.
- (스크립트는 아직 실행해 보지 않았음. 문법 오류 가능.)

**Phase 2 — 원고 재구성.** Thm 5.1 삭제, Theorem OD 삽입. 초록·1절·Remark 5.2·9.2·12절의 PASS/CLOSED 상태 수정. Demuškin 가족은 "S 영역의 대표 예"로 위치 재설정. Prop 7.1은 a < s로 명시. 8절은 "H_z 실패" 설명으로 교체.

**Phase 3 — marked 일반화(Theorem B).** 소형 사례 계산으로 split/nonsplit 판별 규칙을 추측, 그다음 증명. Fox 계산(원고 a=1 witness)은 별도로 독립 검산.

**Phase 4 — unmarked(Theorem C).** L4/L5 기반. 소형 사례 비동형 증명 → 일반화. 안 되면 "e_s ∼ e_t 가능성"의 반례 탐색(동형이 실제로 존재할 수도 있음. 이 경우 정리는 'unmarked 임계값 > p^s+1'이 됨).

**Phase 5 — 비강성 일반화(Theorem D)** 문헌 확인과 함께.

**Phase 6 — 신규성 점검.** Quadrelli 계열, Mináč–Rogelstad–Tân 등에서 "relator의 p-제곱근 + Zassenhaus 창" 결과와 겹치는지 확인. Theorem OD는 기초적이라 기존 결과의 재표현일 위험이 있음. 새로움은 S 영역의 확대이론(B, C)에 있을 가능성이 크다.

## 6. 함정

- 원고 Thm 5.1의 전사 W(G_s) ↠ W(G_t)는 정의되지 않는다. 재사용 금지.
- marked(섹션, 확대류) ≠ unmarked(추상군 동형). 혼동 금지.
- z-free 가설 없이 차수만으로 말하지 말 것. 필요한 가설은 H_z.
- 관계식 부호(r vs r^{-1}) 규약을 문서 전체에서 통일.
- 계산 결과를 증명으로 쓰지 말 것. 5단계 프로토콜(SETUP FAILURE / IMPLEMENTATION FAILURE / INVALID TEST / MATHEMATICAL FAILURE / PASS)로 분류.
- "own-critical window가 s를 기억한다"는 창 깊이가 이미 s를 담고 있어 순환. 같은 창 비교만 의미 있음.

## 7. 열린 질문 (가치순)

1. S 영역에서 W_n(G_s) ≅ W_n(G_t)가 실제로 성립하는 사례가 있는가? (unmarked 임계값이 p^s+1보다 큰 경우)
2. marked 비분열의 일반 판별 규칙 H_B.
3. e_s − e_t = κ_r의 Aut(Q)-불변량 (Demuškin radical 직선 활용).
4. G_{s,s} vs G_{s,∞} 경계(s ≥ 2).
5. H_z가 깨지는 r에 대해 N/S 이분법의 대체 형태.
