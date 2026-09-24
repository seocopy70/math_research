# Demuškin 논문 쉽게 이해하기 — 최신 연구결과 반영본

**2026-09-24 업데이트**

이 문서는 수학 논문의 기술적인 증명을 그대로 옮기는 문서가 아니라, **“이 논문이 실제로 무엇을 알아냈고, 기존 연구와 무엇이 다른가”**를 쉽게 설명하기 위한 해설 문서다.

이번 업데이트에서 논문의 중심을 기존의 “relation jet으로 orientation을 복원한다”는 설명에서, 현재 확정된 **finite-window Kummer recognition theorem**으로 바로잡았다.

---

## 1. 먼저, 우리가 풀려고 한 문제

연구 대상은 rank-4 Demuškin pro-3 군

[
G=
langle x_1,x_2,x_3,x_4
mid
x_1^3[x_1,x_2][x_3,x_4]=1
angle
]

이다.

이 군에는 canonical orientation

[
chi:G	omathbf Z_3^	imes
]

이라는 중요한 3-adic 정보가 있다.

표준 presentation에서는

[
chi(x_1)=chi(x_3)=chi(x_4)=1,
qquad
chi(x_2)=(1-3)^{-1}.
]

따라서

[
chi(x_2)
equiv4pmod9,qquad
13pmod{27},qquad
40pmod{81},ldots
]

가 된다.

### 중요한 점

**canonical orientation 자체는 새로운 발견이 아니다.**

Labute 이후 Demuškin 군의 orientation의 존재와 유일성은 알려져 있다.

우리가 묻는 새로운 질문은 이것이다.

> **전체 무한한 군 G를 직접 사용하거나, 이미 알려진 q나 dualizing action을 입력하지 않고, 유한한 filtered quotient만 보고도 그 orientation의 유한 정밀도 (chimod 3^k)를 intrinsic하게 알아낼 수 있는가?**

이것이 현재 논문의 중심 질문이다.

---

# 2. 왜 그냥 graded data를 보면 안 되는가?

가장 먼저 시도한 것은 Zassenhaus/Jennings–Lazard 같은 **associated graded 정보**였다.

문제는 graded 정보가 너무 많이 압축한다는 것이다.

예를 들어

[
G_3=
langle x_imid x_1^3[x_1,x_2][x_3,x_4]angle
]

와 power-free control

[
G_infty=
langle x_imid [x_1,x_2][x_3,x_4]angle
]

은 quadratic initial relation에서

[
R_2=[X_1,X_2]+[X_3,X_4]
]

라는 같은 정보를 갖는다.

하지만 orientation은 이미 mod 9에서 다르다.

[
chi_{G_3}(x_2)=4pmod9,
qquad
chi_{G_infty}(x_2)=1pmod9.
]

따라서

[
oxed{	ext{bare associated-graded quadratic data만으로는 }chimod9	ext{를 복원할 수 없다.}}
]

이것은 특정 계산 하나가 실패했다는 뜻이 아니다.

**애초에 입력 정보 자체가 부족하다**는 no-go 결과다.

---

# 3. 그러면 어떤 정보가 더 필요한가?

mod 9에서 처음 필요한 정보는 quadratic relation만이 아니라, 그 relation에 붙어 있는 degree-3 restricted-power 정보였다.

표준 presentation에서는

[
P_3=X_1^{[3]}
]

가 나타난다.

그래서 처음에는

[
J_3=[(R_2,P_3)]
]

이라는 projective degree-(2,3) relation jet을 연구했다.

그리고

[
Theta_J(lambda)(f)
=
f(P_3)+(lambdawedge f)(R_2)
]

라는 obstruction functional을 만들었다.

표준 (q=3) 경우에는 이 식의 zero가 유일하게

[
lambda=e_2^*
]

가 되고,

[
ho=1+3lambda
]

이므로

[
oxed{hoequiv(1,4,1,1)pmod9}
]

을 얻는다.

이것은 **mod 9에서 orientation을 복원할 수 있다는 최초의 구체적인 positive result**였다.

---

# 4. 그런데 여기서 한 단계 더 중요한 사실을 발견했다

처음에는 “degree-(2,3) jet 자체가 orientation carrier다”라고 생각하기 쉬웠다.

하지만 더 엄밀하게 조사해 보니 이것도 너무 강한 표현이었다.

실제로 degree-3 정보 전체가 필요한 것이 아니라, **우리가 사용하는 degree-one obstruction이 볼 수 있는 부분만 있으면 된다.**

degree-three bracket 부분은

[
[V,L_2(V)]
]

로 quotient할 수 있고, restricted-power 부분만 남긴

[
p(P_3)in V^{(1)}
]

만으로 같은 degree-one observable을 보존할 수 있다.

따라서 mod-9의 자연스러운 coarsest carrier는

[
oxed{
overline J_3=[(R_2,p(P_3))]
}
]

이다.

### 단, 여기서도 주의

이것을

> “세상에서 가능한 모든 방법 가운데 가장 작은 정보”

라고 주장하면 안 된다.

현재 증명하는 것은 **정해진 degree-one evaluation observable을 보존하는 자연스러운 quotient category 안에서 coarsest**라는 뜻이다.

즉, **absolute minimality가 아니다.**

---

# 5. 그리고 연구의 방향이 바뀌었다

mod 9 relation-jet 결과를 계속 higher jet으로 밀어 올리는 방법도 연구했지만, 논문의 중심으로 삼기에는 문제가 있었다.

특히:

- presentation 좌표에 의존하는 construction
- relator gauge 문제
- naive degree-3 Fox truncation
- 단일 (t_2) carrier의 intrinsicity 문제
- higher-digit carrier의 minimality 문제

등은 별도의 어려움을 만들었다.

여러 hard attack을 거친 뒤 이 경로들은 대부분 **FAIL/CLOSED** 또는 논문의 주된 증명으로는 사용하지 않기로 정리되었다.

대신 훨씬 자연스럽고 강한 방법이 발견되었다.

그것이 **Kummer lifting을 이용한 finite-window recognition**이다.

---

# 6. 핵심 아이디어: “후보 orientation을 하나씩 시험한다”

(kge2)에 대해

[
Q_k=G/P_{k+1}
]

를 생각한다.

여기서 (P_{k+1})은 lower 3-central filtration의 다음 단계다.

이제 어떤 후보 character

[
ho:Q_k	o(mathbf Z/3^k)^	imes
]

를 하나 잡는다.

이 후보가 정말 canonical orientation인지 직접 묻는 대신, 다음 질문을 한다.

[
H^1(Q_k,mathbf Z/3^k(ho))
longrightarrow
H^1(Q_k,mathbf F_3)
]

가 surjective인가?

즉,

> **mod 3에서 가능한 모든 1-cocycle이 이 후보 (ho)를 사용한 mod (3^k) 계수까지 실제로 lift되는가?**

를 검사한다.

이를

[
mathsf K_k(Q_k,ho)
]

라고 쓰자.

정의는

[
oxed{
mathsf K_k(Q_k,ho):
H^1(Q_k,mathbf Z/3^k(ho))
	o H^1(Q_k,mathbf F_3)
	ext{ is surjective}.
}
]

---

# 7. 이것이 중요한 이유

Kummerian property 자체는 기존 문헌에 알려진 개념이다.

따라서

> “Kummer lifting criterion을 발견했다”

는 것이 논문의 공헌이 아니다.

핵심은 **그 criterion을 finite quotient 위의 orientation selector로 바꾸는 것**이다.

현재 증명된 정리는 다음과 같다.

[
oxed{
mathsf K_k(G/P_{k+1},ho)
iff
ho=chi_Gmod3^k,
qquad kge2.
}
]

즉,

> **유한 quotient (Q_k=G/P_{k+1})와 후보 (ho)만 주어졌을 때, Kummer lifting 조건을 통과하는 후보가 정확히 canonical orientation의 mod (3^k) 값이다.**

이것이 현재 논문의 핵심 정리다.

---

# 8. “Q_k만 보면 된다”는 말의 정확한 뜻

여기서 자주 오해할 수 있는 부분이 있다.

“Q_k만 보면 G 전체가 필요 없다”라고 말하면 너무 강하다.

정확한 뜻은 다음이다.

[
oxed{
	ext{orientation recognition에 필요한 twisted }H^1
	ext{ obstruction이 }Q_k	ext{를 통해 factor한다.}
}
]

즉, G의 모든 정보를 Q_k가 가지고 있다는 뜻이 아니다.

단지 **이번 recognition problem에 필요한 정보가 Q_k에서 이미 계산 가능하다**는 뜻이다.

---

# 9. 이 finite factorization은 어떻게 증명했는가?

핵심은 후보 (ho)에 대해

[
A_k=mathbf Z/3^k
]

를 coefficient module로 놓고

[
A_ktimes U_1
]

이라는 semidirect product를 만든 뒤 그 lower 3-central filtration을 분석하는 것이다.

그 결과

[
P_j(A_ktimes U_1)
=
3^{j-1}A_ktimes U_j
]

가 모든 relevant (j)에 대해 성립한다.

특히 (j=k+1)에서 triviality가 생기므로, G에서 만든 crossed cocycle은

[
P_{k+1}
]

을 소거한다.

따라서

[
oxed{
	ext{임의의 후보 }ho	ext{에 대한 relevant crossed cocycle가 }Q_k=G/P_{k+1}	ext{를 통해 factor한다.}
}
]

이것이 논문의 중요한 structural step이다.

여기서 중요한 점은 **canonical (chi)를 미리 넣지 않았다는 것**이다.

후보 (ho)를 임의로 놓고 factorization을 증명한다.

---

# 10. Kummer 조건과 Fox 계산은 어떻게 연결되는가?

이 부분은 논문의 실제 계산을 이해하는 데 중요하다.

후보 (ho)에 대해

[
A_k=mathbf Z/3^k(ho)
]

를 사용한다.

모든 mod-3 cocycle가 lift된다고 가정하면 twisted Fox 조건이 생긴다.

이를 올바르게 반복 적용하면

[
F_iin3I
]

가 되고 다시 같은 논리를 적용해서

[
F_iin3^mA_k
]

를 모든 (m)에 대해 얻는다.

그런데

[
igcap_m3^mA_k=0
]

이므로

[
F_i=0.
]

반대로 twisted Fox row가 0이면 lifting criterion을 얻는다.

따라서

[
oxed{
mathsf K_k
iff
	ext{twisted Fox obstruction vanishes}.
}
]

Fox calculus는 여기서 **최종 invariant의 정의가 아니라 증명의 계산 도구**다.

이 구분이 중요하다.

---

# 11. 표준 presentation에서는 후보가 어떻게 결정되는가?

표준 relation

[
r=x_1^3[x_1,x_2][x_3,x_4]
]

을 사용하면 twisted Fox equation을 직접 풀 수 있다.

결과는

[
ho(x_1)=ho(x_3)=ho(x_4)=1
]

이고

[
1+2ho(x_2)=0pmod{3^k}.
]

따라서

[
oxed{
ho(x_2)=(-2)^{-1}
=(1-3)^{-1}
pmod{3^k}.
}
]

예를 들어

[
k=2:quad4pmod9,
]

[
k=3:quad13pmod{27},
]

[
k=4:quad40pmod{81}.
]

이 표준 presentation 계산은 **orientation selector의 unique solution을 확인하는 local/presentation-dependent 계산**이다.

최종 theorem 자체가 presentation-dependent라는 뜻은 아니다.

---

# 12. 가장 중요한 부분: U5의 intrinsic uniqueness

여기까지 하면 한 가지 의문이 남는다.

혹시 finite quotient 위에서 서로 다른 두 후보가 똑같이 Kummer 조건을 만족하는 것은 아닌가?

이것을 막는 것이 U5다.

두 level-(k) 후보가

[
ho_k'=ho_k(1+3^{k-1}
u)
]

관계라고 하자.

계수확장에 대한 connecting map을 비교하면

[
oxed{
delta_{ho_k'}-delta_{ho_k}
=
iota_{k-1}circ(
usmile-).
}
]

여기서 (iota_{k-1})은 coefficient extension에서 오는 socle inclusion이다.

PD(^2) duality를 사용하면 이 map이 (H^2)에서 필요한 injectivity를 갖는다는 것을 증명할 수 있다.

따라서 두 후보가 모두 전체 (H^1)에 대해 zero obstruction을 가진다면

[

usmile v=0
]

가 모든

[
vin H^1(G,mathbf F_3)
]

에 대해 성립한다.

그런데 Demuškin 군의 cup product는 nondegenerate이므로

[

u=0.
]

따라서 후보가 하나뿐이다.

이것이

[
oxed{	ext{intrinsic uniqueness}}
]

이다.

---

# 13. 존재성은 새로 발견한 것이 아니다

여기서 또 하나 중요한 선이 있다.

유일성은 위의 finite obstruction과 PD(^2) 논리로 증명한다.

하지만 canonical orientation이 실제로 Kummerian 조건을 만족한다는 사실 자체는 기존 Demuškin 이론에 의해 알려져 있다.

즉 논문의 논리는

[
	ext{기존 이론이 주는 existence}
+
	ext{우리의 finite factorization}
+
	ext{우리의 intrinsic uniqueness}
]

이다.

이렇게 해야 논문의 공헌 범위를 정확하게 표현할 수 있다.

---

# 14. 그러면 기존 연구와 무엇이 다른가?

기존 연구에는 이미 다음이 알려져 있다.

- Demuškin 군의 canonical orientation의 존재와 유일성
- Kummerian/cyclotomic orientation의 cohomological characterization
- (H^1(G,mathbf Z_p(	heta)/p^n)	o H^1(G,mathbf F_p))의 surjectivity criterion
- oriented group의 quotient inheritance와 관련된 여러 결과

따라서 논문의 주장을

> “우리가 처음으로 Demuškin orientation을 발견했다”

라고 쓰면 안 된다.

또

> “기존에는 전체 무한한 구조를 봐야만 했다”

라고 단정해서도 안 된다.

현재까지 확인한 문헌과 우리의 theorem을 비교하면, 핵심 차이는 훨씬 좁고 구체적이다.

### 현재 논문의 주장

[
Q_k=G/P_{k+1}
]

라는 특정 finite window 위에서,

1. 후보 (ho)를 미리 canonical orientation이라고 가정하지 않고,
2. (q), dualizing action을 selector의 입력으로 넣지 않고,
3. intrinsic한 Kummer lifting predicate를 정의하고,
4. 임의의 후보에 대한 crossed-cocycle factorization을 증명하여,
5. 그 predicate의 유일한 해가
   [
   chi_Gmod3^k
   ]
   임을 보인다.

따라서 novelty claim도 이 범위 안에서만 해야 한다.

---

# 15. “q-blind”는 무슨 뜻인가?

논문에서 q-blind라는 말을 사용할 때 조심해야 한다.

정확한 의미는

> **selector의 입력으로 q를 직접 넣지 않는다.**

라는 뜻이다.

q가 실제 군의 구조와 아무 관련이 없다는 뜻도 아니고,

> “모든 q에 대해 동일한 theorem이 증명되었다”

는 뜻도 아니다.

현재 주된 theorem은 **연구 대상인 rank-4 q=3 Demuškin 군**에 대해 증명되어 있다.

---

# 16. “presentation-free”도 정확하게 이해해야 한다

표준 presentation을 사용했다고 해서 theorem이 presentation-dependent인 것은 아니다.

논문에서는 실제 계산을 위해

[
x_1^3[x_1,x_2][x_3,x_4]
]

라는 표준 presentation을 사용할 수 있다.

그 계산은 후보의 값을 식별하는 데 쓰인다.

하지만 최종 selector

[
mathsf K_k(Q_k,ho)
]

는 quotient와 coefficient action으로 정의되는 intrinsic object다.

따라서 정확한 표현은

> **최종 predicate와 theorem은 intrinsic하며, 표준 presentation은 중간 계산 장치로 사용된다.**

이다.

---

# 17. “finite window”는 정확히 무엇인가?

각 (k)에 대해

[
Q_k=G/P_{k+1}
]

라는 유한 quotient를 본다.

그러면

[
Q_2=G/P_3
]

에서는 mod 9 orientation,

[
Q_3=G/P_4
]

에서는 mod 27 orientation,

일반적으로

[
Q_k=G/P_{k+1}
]

에서는 mod (3^k) orientation을 인식한다.

즉 정밀도가 한 단계 올라갈 때 필요한 filtration window도 한 단계 깊어진다.

이것이 논문의 “finite-window”라는 이름의 의미다.

---

# 18. full orientation은 어떻게 얻는가?

각 유한 단계에서

[
chi_k=chimod3^k
]

를 알아낸다고 하자.

그러면

[
chi_{k+1}equivchi_kpmod{3^k}
]

라는 compatibility가 있고,

[
mathbf Z_3^	imes
cong
arprojlim_k(mathbf Z/3^k)^	imes
]

이므로 inverse limit를 취하면

[
oxed{
chi:G	omathbf Z_3^	imes
}
]

를 얻는다.

따라서 중요한 구분은 다음이다.

### 하나의 finite quotient

[
Q_k
quadLongrightarrowquad
chimod3^k.
]

### 모든 compatible finite windows

[
(Q_k)_{kge2}
quadLongrightarrowquad
chi.
]

**하나의 mod-9 finite quotient가 full 3-adic orientation을 담는다는 주장은 아니다.**

---

# 19. 그러면 예전에 했던 “higher jet tower”는 틀렸나?

그렇게 볼 필요는 없다.

relation-jet 접근은 실제로 mod 9에서 orientation이 어디서 처음 보이기 시작하는지를 밝혀냈다.

즉,

[
	ext{graded data}
ightarrow
	ext{first extension information}
ightarrow
chimod9
]

이라는 정보 경계를 발견하는 데 매우 중요했다.

다만 현재 논문의 주된 theorem을 증명하는 데에는 그 전체 tower를 계속 구축할 필요가 없어졌다.

따라서 논문에서는 이를 **motivation / information-boundary**로 짧게 사용하고, U1–U5의 finite Kummer recognition proof를 중심으로 구성한다.

---

# 20. 연구에서 폐기된 것과 살아남은 것

현재 상태를 간단히 정리하면 다음과 같다.

| 내용 | 현재 상태 | 논문에서의 역할 |
|---|---|---|
| Bare quadratic graded data로 (chimod9) 복원 | FAIL / CLOSED | 정보 하한 |
| Degree-(2,3) relation jet의 mod-9 recovery | PASS / CLOSED | motivation 및 초기 positive result |
| Raw (J_3) absolute minimality | FAIL / CLOSED | 과장 방지 |
| (overline J_3=[(R,p(P))]) coarsest quotient | PASS / CLOSED | 보조 결과 |
| 임의 후보의 finite factorization through (Q_k) | PASS / CLOSED | 핵심 |
| Kummer lifting ↔ twisted Fox criterion | PASS / CLOSED | 핵심 보조정리 |
| 표준 presentation에서 후보 식별 | PASS / LOCAL | 계산적 식별 |
| U5 intrinsic uniqueness | PASS / CLOSED | 핵심 |
| finite-window recognition theorem | PASS / CLOSED | **논문의 중심 정리** |
| canonical orientation의 존재/유일성 자체 | KNOWN | 기존 이론 |
| exact publication novelty | OPEN / STRONG CANDIDATE | 제출 전 계속 정확히 검증 |

---

# 21. 논문의 핵심을 한 문장으로 말하면

가장 정확한 한 문장은 다음과 같다.

> **이 논문은 canonical Demuškin orientation의 존재나 유일성을 새로 발견하는 것이 아니라, Kummerian lifting을 이용한 orientation recognition이 특정 finite lower-3-central quotient (Q_k=G/P_{k+1})에서 intrinsic하게 factor하고, 그 finite quotient 위의 Kummer predicate가 (chi_Gmod3^k)를 유일하게 식별한다는 finite-window recognition theorem을 제시한다.**

조금 더 쉽게 말하면:

> **“Demuškin 군의 숨은 3-adic 방향성을 무한한 전체 구조를 한꺼번에 해석하는 대신, 깊이 (k+1)까지만 잘라낸 유한한 창 (Q_k)에서 후보들에게 Kummer lifting 시험을 해 보면, 정확히 canonical orientation의 (k)자리 값만 살아남는다.”**

---

# 22. 현재 논문이 실제로 말할 수 있는 것과 말하면 안 되는 것

### 말할 수 있다

- quadratic graded information만으로는 mod 9 orientation을 결정할 수 없다.
- mod 9에서는 degree-(2,3) relation information이 충분한 positive carrier가 된다.
- Kummer lifting은 알려진 이론이지만, 이를 finite quotient 위의 intrinsic selector로 조직할 수 있다.
- (Q_k=G/P_{k+1})에서 relevant twisted (H^1) obstruction이 factor한다.
- canonical orientation은 이 finite predicate의 유일한 해다.
- 이 결과는 (kge2)에 대해 uniform하게 정리된다.
- 표준 presentation에서는 (ho(x_2)=(1-3)^{-1}pmod{3^k})가 직접 계산된다.

### 말하면 안 된다

- “canonical orientation을 최초로 발견했다.”
- “기존에는 반드시 G 전체를 봐야 했다.”
- “Q_k가 G의 모든 정보를 담는다.”
- “q가 필요 없으므로 모든 q에 대해 동일한 theorem이다.”
- “논문의 모든 construction이 presentation-free이다.”
- “mod 9 하나만으로 full 3-adic orientation을 복원한다.”
- “absolute minimal carrier를 찾았다.”
- “세계 최초임이 완전히 확정되었다.”

---

# 23. 현재 논문의 구조

현재 확정된 publication architecture는 다음과 같다.

### 1. Introduction
- 기존 canonical/Kummerian orientation 이론
- finite-window 질문
- graded information의 한계
- main theorem
- 정확한 novelty boundary

### 2. Finite coefficient extensions and finite window
- (A_k=mathbf Z/3^k)
- semidirect product filtration
- arbitrary-candidate factorization

### 3. Finite Kummer criterion
- coefficient lifting
- corrected iterative/Nakayama argument
- twisted Fox criterion

### 4. Standard presentation
- 표준 relation에서 후보 (ho) 식별
- (1+2ho(x_2)=0)
- (k=4)에서 (40mod81)은 예시일 뿐

### 5. Intrinsic uniqueness
- coefficient-extension variation formula
- PD(^2) duality
- cup-product nondegeneracy

### 6. Main finite-window theorem

[
oxed{
mathsf K_k(G/P_{k+1},ho)
iff
ho=chi_Gmod3^k.
}
]

### 7. Previous work and novelty boundary

### 8. Information-boundary discussion

---

# 24. 마지막으로, 이 연구의 의미를 가장 쉽게 표현하면

처음 질문은

> “Demuškin 군의 orientation을 filtered/graded information만으로 복원할 수 있을까?”

였다.

연구가 진행되면서 답은 단순한 yes/no가 아니라 다음과 같이 정리되었다.

[
oxed{
	ext{graded information만으로는 부족하다.}
}
]

하지만

[
oxed{
	ext{적절한 finite filtered window에서는 충분하다.}
}
]

그리고 그 “적절한 방법”은 단순히 관계식을 더 많이 계산하는 것이 아니라

[
oxed{
	ext{후보 }ho
ightarrow
	ext{Kummer lifting test}
ightarrow
	ext{finite factorization}
ightarrow
	ext{intrinsic uniqueness}
}
]

라는 구조를 갖는다.

즉 이 논문의 핵심은

> **숨은 orientation을 직접 계산해서 집어내는 것이 아니라, 각 후보에게 “이 orientation이라면 모든 mod-3 cohomology class가 higher coefficient까지 lift되어야 한다”는 시험을 하고, 그 시험을 통과하는 유일한 후보를 orientation으로 식별하는 것**

이다.

이 관점에서 보면 논문의 진짜 주제는 단순한 Demuškin orientation 계산이 아니라,

[
oxed{
	ext{finite-window recognition of a known }p	ext{-adic invariant}
}
]

이라는 보다 구조적인 문제다.

---

## 부록: 현재 연구 상태 한눈에 보기

[
egin{array}{c|c}
	ext{항목}&	ext{상태}\
\hline
	ext{수학적 finite-window theorem}&mathbf{PASS/CLOSED}\
	ext{U1 factorization}&mathbf{PASS/CLOSED}\
	ext{U2 arbitrary-candidate factorization}&mathbf{PASS/CLOSED}\
	ext{U3 Kummer/Fox criterion}&mathbf{PASS/CLOSED}\
	ext{U4 standard presentation identification}&mathbf{PASS/LOCAL}\
	ext{U5 intrinsic uniqueness}&mathbf{PASS/CLOSED}\
	ext{canonical orientation existence}&mathbf{KNOWN}\
	ext{broad orientation-discovery claim}&mathbf{CLOSED/NON-NOVEL}\
	ext{exact publication novelty}&mathbf{OPEN/STRONG CANDIDATE}
end{array}
]

**현재 단계의 원칙:** 새로운 broad mathematical attack을 추가하기보다, U1–U5를 publication-style로 정리하고 문헌과 theorem statement를 source-level에서 정확히 대조한다.
