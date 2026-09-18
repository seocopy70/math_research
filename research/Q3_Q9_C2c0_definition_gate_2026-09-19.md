# C-2c-0: Definition gate (2026-09-19)

**상태:** 정의만 고정. 계산 없음.

## 0. 금지 사항

- (d_3=[X_1^{[3]},X_2]) 패턴을 degree 9로 외삽하지 않는다.
- (S_9=X_1^9) (associative word)를 (X_1^{[9]}) (restricted-Lie 원소)로 승격하지 않는다.
- C-2b의 free associative/enveloping-level action 감사를 (mathrm{gr}(G)) 위의 결과로 승격하지 않는다.
- (d_9^{(9)}) 또는 (D_9)를 채택하지 않는다.
- H-stability를 계산하지 않는다.
- 본 문서에는 새로운 계산 결과를 추가하지 않는다.

## 1. 확정된 정의 (repo: C-1b / Gate-A)

다음은 repo의 기존 Gate-A/C-1b 정의를 그대로 따른다.

[
x_i=1+X_i,
]

[
C_q=x_1x_2[x_3,x_4]x_1^q x_2^{-1},
qquad
C_infty=x_1x_2[x_3,x_4]x_2^{-1},
]

[
s_q=C_qx_1^{-1}[x_3,x_4]^{-1},
qquad
s_infty=C_infty x_1^{-1}[x_3,x_4]^{-1},
]

[
Delta_d(q)=operatorname{in}_d(s_q-s_infty).
]

**Degree-9 source의 정의:**

[
oxed{S_9:=Delta_9(9)}.
]

기존 C-1a/C-1b 기록에서 확정된 입력은

[
Delta_d(9)=0quad(1le dle8),
qquad
Delta_9(9)=X_1^9
e0.
]

여기서 마지막 식은 (x_1^9=1+X_1^9)라는 characteristic-3 산술과 baseline-relative 정의에서 나오는 것이다. 따라서 이 결과를 새로운 독립적 수학 정리로 과대 해석하지 않는다.

중요한 구별:

[
S_9=X_1^9
]

는 우선 **associative Magnus word**로서의 등식이다. 이것만으로

[
S_9=X_1^{[9]}
]

라는 restricted-Lie 해석을 확정하지 않는다.

## 2. 공간 구분: 네 층위

Zassenhaus filtration의 associated graded는 (mathbb F_3) 위 restricted Lie 구조를 가지므로 degree 9의 ambient를 단순한 free Lie degree-9 공간으로 취급하지 않는다.

| 기호 | 의미 | 차원/상태 |
|---|---|---|
| (A_9) | free associative degree-9 word space | (4^9) |
| (L_9) | free Lie degree-9 component | (29120) |
| (L_9^{mathrm{res}}) | free restricted-Lie degree-9 component | (29144) [확인] |
| (mathrm{gr}_9(G)) | (L_9^{mathrm{res}})를 degree-9 관계의 initial/restricted ideal로 quotient한 실제 associated-graded component | 미정 |

### 2.1 Restricted degree-9 구성

후보적인 free restricted-Lie degree-9 분해는 다음 구조를 따른다.

- ordinary free-Lie degree 9: (L_9), dimension (29120)
- degree-3 Lie basis elements의 first restricted cube: (L_3^{[3]}), dimension (20)
- degree-1 generators의 second restricted cube: (L_1^{[9]}), dimension (4)

따라서

[
29120+20+4=29144.
]

**[확인]** 이 (L_9^{mathrm{res}})의 정확한 의미/기저 분해와 차원이 프로젝트가 기존 degree 3, 4에서 사용해 온 restricted-Lie 규약과 정확히 일치하는지는 별도 repo audit에서 확인한다. 이 문서에서는 이를 계산 결과로 확정하지 않는다.

특히

[
X_1^{[9]}
]

는 ordinary (L_9)의 원소라고 취급하지 않고 restricted (p)-power 부분의 원소로 취급한다.

따라서 다음 표기는 사용하지 않는다:

[
mathrm{gr}_9(G)cong L_9/R_9.
]

정확한 관계 quotient는 restricted ambient와 그에 맞는 degree-9 relation ideal을 먼저 정의한 뒤에 쓴다.

또한 (29120)을 degree-9 relation-ideal (R_9)의 안정성 계산에서 자동으로 ambient dimension으로 사용하지 않는다.

## 3. 이름 규칙

Gate-A의 degree-3 baseline 객체와 degree-9 source 관련 후보를 분리한다.

[
oxed{d_9^{mathrm{base}}:=[Delta_3(9),X_2]}
]

Gate-A에서 (Delta_3(9)=0)이므로 이 객체는 0이다.

반면 degree-9 source (S_9)와 관련하여 앞으로 검토할 후보에는 아직 이름만 예약한다:

[
oxed{D_9:=	ext{degree-9 source }S_9	ext{와 관련된 후보}}
]

현재 (D_9)는 정의되지 않았다.

두 객체를 모두 단순히 (d_9)라고 부르지 않는다.

## 4. (D_9) 후보 등록 조건

[
[S_9,X_2]
]

를 (D_9) 후보로 등록하려면 다음 조건을 모두 별도 검증해야 한다.

1. (S_9)가 (mathrm{gr}_9(G))의 원소로 정의되어야 하며, (L_9^{mathrm{res}}) 안에서의 위치가 명확해야 한다.
2. restricted (p)-operation
   [
   mathrm{gr}_3(G)	omathrm{gr}_9(G)
   ]
   와 (S_9)의 관계가 정의되어야 한다. 특히 (X_1^{[3]})의 반복 (p)-power가 (X_1^{[9]})와 어떻게 연결되는지는 별도 정의/검증 대상으로 둔다.
3. degree-9 관계 quotient에서 (S_9)가 0이 아닌지 확인해야 한다.
4. q=3에서 실제로 사용된 relation-theoretic derivation
   [
   d=[X_1^{[3]},X_2]
   ]
   이 degree 9에서 같은 이유로 재현되는지 확인해야 한다.
5. 위 조건을 충족하기 전에는 ([S_9,X_2])를 (D_9)라고 채택하지 않는다.

## 5. Admissibility 기준

### A1. q-sensitive

degree (<9)에서는 q=9 control이 q=(infty) baseline과 일치해야 한다.

현재 이 항목은 기존 C-1a/C-1b 입력을 전제로 한다.

### A2. nonzero / filtration degree

후보가 실제 (mathrm{gr}_9(G))에서 0이 아니며 올바른 filtration degree에 있어야 한다.

### A3. quotient-level H-equivariance

후보는 authoritative H-action에 대해 실제 (mathrm{gr}(G)) quotient에서 equivariant여야 한다.

따라서 degree-9 relation ideal의 H-stability가 선행 조건이다. 현재 프로젝트에서 확정된 relation 구조가 degree (le5)에 머물러 있으므로 degree-9 quotient-level 주장은 별도 gate로 둔다.

### A4. allowed automorphism family

허용 automorphism family를 사전에 명시한다. 현재 기준은

[
{aI+bN}
]

를 대상으로 하며, 전체 허용 family에서의 불변성을 요구한다.

일부 subgroup에서만 불변이면 전체 불변으로 승격하지 않고 그 자유도/선택 의존성을 그대로 기록한다. O2-9의 transport dependence 결과를 이 기준에 반영한다.

### A5. q=3 / q=9 / q=(infty) 구별

세 경우의 source와 quotient-level 객체를 동일시하지 않는다. 이 구별은 별도 gate에서 판정한다.

## 6. 판정 등급 (실행 전 고정)

- **DEFINITION PASS:** (D_9)의 후보 등록 조건 1–5와 A1–A4가 모두 충족되어 정의가 고정될 수 있음.
- **AMBIGUOUS:** 정의 후보는 가능하지만 A4의 선택 의존성 등 자유도가 남음. 자유도를 명시하여 기록.
- **NOT ADMISSIBLE:** 후보 등록 조건 또는 A3가 실패함. 이는 유효한 연구 결과로 보존하며 실패를 숨기지 않는다.

이 문서 자체에서는 위 등급을 판정하지 않는다.

## 7. 열린 항목

1. (L_9^{mathrm{res}})의 정확한 restricted-Lie 규약 및 (29144) 차원 분해를 repo의 기존 degree-3/4 규약과 대조.
2. degree 3의 (X_1^{[3]}) 및 degree 4에서의 restricted-power 취급이 degree 9에서도 동일한 ambient convention을 사용하는지 확인.
3. Demuškin (q=infty) convention의 구체적 문헌 인용.
4. degree-9 restricted relation ideal (R_9)의 정확한 정의.
5. 그 (R_9)의 H-stability.
6. 위 항목들이 정리된 뒤에만 (D_9) 후보의 quotient-level admissibility를 조사.

## 8. 다음 Gate

다음 계산/검증 단계는 곧바로 (D_9)를 계산하는 것이 아니다.

먼저:

[
oxed{	ext{restricted ambient }L_9^{mathrm{res}}
;longrightarrow;
	ext{degree-9 relation ideal }R_9
;longrightarrow;
H	ext{-stability}}
]

의 순서로 정의와 quotient 구조를 확정한다.

**C-2c-0 자체에는 계산 결과를 추가하지 않는다.**
