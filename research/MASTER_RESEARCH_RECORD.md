# Demuškin 군의 filtration에서 canonical orientation을 복원할 수 있는가

## 연구 마스터 보존본 — 2026-09-15

> **사용법**: 새 연구 창에서는 이 문서 전체를 붙여 넣고 “이 기록을 기준으로 연구를 이어가자”라고 하면 된다.

---

## 0. 연구의 최종 목표

rank-4 Demuškin pro-3 군의 내부적인 Zassenhaus/Jennings–Lazard filtration 및 associated graded Lie 구조만을 이용하여, 외부에서 미리 주어진 orientation character를 얼마나 본질적으로 복원할 수 있는지를 연구한다.

궁극적인 목표는 filtration으로부터 canonical filtered orientation

\[
\chi_{\mathrm{filt}}:G\to\mathbb Z_3^\times
\]

을 복원하는 것이다.

**현재는 이 최종 목표를 아직 달성하지 않았다.**

---

## I. 기본 설정

연구 대상은 rank-4 Demuškin pro-3 군

\[
G=
\langle x_1,x_2,x_3,x_4
\mid
x_1^3[x_1,x_2][x_3,x_4]=1\rangle
\]

이다.

사용하는 군 commutator convention은

\[
[a,b]=a^{-1}b^{-1}ab.
\]

관계식에서

\[
x_1^3[x_1,x_2][x_3,x_4]=1
\]

이므로

\[
x_2^{-1}x_1x_2
=x_1[x_1,x_2]
=x_1^{-2}[x_3,x_4]^{-1}.
\]

따라서

\[
u=x_1^{-2},\qquad v=[x_3,x_4]^{-1}
\]

라고 놓으면

\[
x_2^{-1}x_1x_2=uv.
\]

따라서

\[
(uv)^3=x_2^{-1}x_1^3x_2.
\]

---

## II. Zassenhaus filtration

Zassenhaus filtration을

\[
D_1\supset D_2\supset D_3\supset\cdots
\]

라 한다.

필요한 기본 성질:

\[
[D_i,D_j]\subseteq D_{i+j}
\]

및 \(p=3\)에서

\[
g\in D_m,\quad v_3(a)=s
\quad\Longrightarrow\quad
g^a\in D_{3^s m}.
\]

현재 원소들의 filtration degree는

\[
u\in D_1,
\qquad
v\in D_2,
\]

따라서

\[
[v,u]\in D_3,
\]

\[
[v,u,u]\in D_4,
\]

\[
[v,u,v]\in D_5.
\]

또한

\[
v^3\in D_6,
\qquad
[v,u]^3\in D_9.
\]

주의:

\[
u^3\in D_3
\]

이므로 degree-4 분석에서 처음부터 버리면 안 된다. \(x_1^3\)에서 나오는 degree-3 부분과 먼저 비교한 뒤 degree-4 residual을 분석해야 한다.

---

## III. Hall–Petrescu 계산

고정된 commutator convention 아래에서 필요한 전개는

\[
(uv)^3
=
u^3v^3[v,u]^3[v,u,u][v,u,v]
\pmod{\text{weight}\ge5}.
\]

따라서 degree-4에서 핵심적으로 남는 항은

\[
[v,u,u]
\]

이며 그 Hall–Petrescu 계수는

\[
\boxed{\lambda_{\mathrm{HP}}=1\pmod3}.
\]

---

## IV. Associated graded Lie algebra

associated graded Lie algebra의 degree-1 부분을

\[
X_1,X_2,X_3,X_4
\]

로 두고

\[
L=\mathbb L_{\mathbb F_3}(X_1,X_2,X_3,X_4)
\]

를 자유 Lie algebra로 본다.

degree-2의 중요한 원소:

\[
e_1=[X_1,X_2],
\quad e_2=[X_1,X_3],
\quad e_3=[X_1,X_4],
\]

\[
e_4=[X_2,X_3],
\quad e_5=[X_2,X_4],
\quad e_6=[X_3,X_4].
\]

관계식의 quadratic initial form은

\[
\boxed{R=e_1+e_6=[X_1,X_2]+[X_3,X_4].}
\]

이 \(R\)은 이후 symplectic 구조와 연결된다.

---

## V. 핵심 degree-4 obstruction \(T\)

연구에서 선택한 target은

\[
\boxed{T=[[X_3,X_4],X_1],X_1}
\]

이다.

즉

\[
T=[e_6,X_1,X_1].
\]

multidegree는

\[
(2,0,1,1).
\]

degree-4 relation ideal은

\[
(R)_4=[R,L_2].
\]

---

## VI. Theorem A: \(T\notin(R)_4\)

multidegree를 이용하면 \(T\)의 multidegree \((2,0,1,1)\) 성분에서 relation ideal이 사라진다.

### \(e_1\) 부분

\(e_1\)의 multidegree는

\[
(1,1,0,0).
\]

따라서 \(T\)와 같은 multidegree를 만들려면 두 번째 factor가

\[
(1,-1,1,1)
\]

이어야 하는데 불가능하다.

### \(e_6\) 부분

\(e_6\)의 multidegree는

\[
(0,0,1,1).
\]

두 번째 factor는

\[
(2,0,0,0)
\]

이어야 하지만

\[
L_2^{(2,0,0,0)}
=\mathbb F_3[X_1,X_1]=0.
\]

따라서

\[
(R)_4^{(2,0,1,1)}=0.
\]

한편 free associative algebra에 embedding하여 계산하면

\[
\begin{aligned}
T={}&
X_3X_4X_1^2-X_4X_3X_1^2\\
&-X_1X_3X_4X_1+X_1X_4X_3X_1\\
&+X_1^2X_3X_4-X_1^2X_4X_3
\pmod3,
\end{aligned}
\]

이고 여섯 단어가 서로 다르므로

\[
T\neq0.
\]

따라서

\[
\boxed{T\notin(R)_4}.
\]

이것이 첫 번째 핵심 증명이다.

---

## VII. 부호와 \([v,u,u]\)

\[
u=x_1^{-2}
\]

이므로 degree-1에서

\[
\bar u=-2X_1=X_1
\quad(\mathbb F_3).
\]

또한

\[
v=[x_3,x_4]^{-1}
\]

이므로

\[
\bar v=-[X_3,X_4]=-e_6.
\]

따라서

\[
[v,u,u]
\mapsto
[[-e_6,X_1],X_1]
=-T.
\]

즉

\[
\boxed{\operatorname{in}_4([v,u,u])=-T}
\]

이고

\[
\lambda_T=-1=2\pmod3.
\]

---

## VIII. Group-level bridge: mildness

단순히 free Lie algebra에서 \(T\neq0\)이라고 한 것으로 끝내면 안 된다.

실제 군 \(G\)의 associated graded에 \(T\)가 살아 있는지를 확인해야 한다.

현재 군의 Zassenhaus invariant는

\[
z(G)=2
\]

이다.

관계식에는 degree-2 commutator가 존재하고 \(x_1^3\in F_3\)이므로 initial degree가 2이다.

그리고

\[
\gcd(2,3)=1.
\]

따라서 one-relator pro-\(p\) group에 대한 mildness theorem을 적용할 수 있다.

관련 문헌으로 확인한 자료:

- Labute, *Mild pro-p-groups and Galois groups of p-extensions of \(\mathbb Q\)*.
- mild pro-p groups 관련 theorem 자료.
- graded group algebra presentation 및 Jennings/Lazard 이론 관련 자료.

mildness로 인해

\[
\operatorname{gr}G
\simeq
L_{\mathrm{res}}/\langle R\rangle_{\mathrm{res}}.
\]

\(R\)의 degree가 2이고 \(p=3\)이므로 restricted powers of \(R\)는 최초 degree 6에서 등장한다.

따라서 degree 4에서는

\[
(\langle R\rangle_{\mathrm{res}})_4
=(R)_4.
\]

그러므로

\[
\ker(L_4\to\operatorname{gr}_4G)
=(R)_4.
\]

앞서

\[
T\notin(R)_4
\]

였으므로

\[
T\neq0\in\operatorname{gr}_4G.
\]

따라서

\[
\boxed{[v,u,u]\in D_4(G)\setminus D_5(G).}
\]

이것이 free Lie algebra의 계산을 실제 Demuškin 군으로 연결하는 핵심 bridge이다.

---

## IX. 중요한 개념적 수정

초기에는 \(T\) 자체가 canonical orientation을 제공할 가능성을 생각했다.

그러나 이것은 일반적으로 정당화되지 않는다.

\(T\)는 특정 좌표계와 multidegree

\[
(2,0,1,1)
\]

에 의존한다.

일반 automorphism은 \(X_i\)들을 섞을 수 있기 때문이다.

따라서 canonical한 저차원 구조는 오히려

\[
\mathbb F_3R
\]

라는 relation line 및 이에 대응하는

\[
H^2(G,\mathbb F_3)
\]

의 1차원 구조와 symplectic/cup-product pairing이다.

따라서 연구 질문은

> “\(T\)가 곧 orientation인가?”

에서

> “\(T\)가 생성하는 전체 대칭 표현 안에서 orientation에 해당하는 canonical factor를 추출할 수 있는가?”

로 수정되었다.

---

## X. \(Sp_4(\mathbb F_3)\) 표현으로의 확장

\(R\)은

\[
[X_1,X_2]+[X_3,X_4]
\]

형태이므로 symplectic form을

\[
J=
\begin{pmatrix}
0&1&0&0\\
-1&0&0&0\\
0&0&0&1\\
0&0&-1&0
\end{pmatrix}
\]

로 잡는다.

### 중요한 교정

초기 계산에서 다른 pairing을 주는 잘못된 \(J\)를 사용했을 때 orbit span이 잘못 계산되었다.

현재의 기준 \(J\)는 반드시 위 행렬이다.

---

## XI. \(T\)의 orbit span

\(Sp_4(\mathbb F_3)\)의 symplectic transvection

\[
t_v(x)=x+\omega(x,v)v
\]

를 이용했다.

비영 \(v\in\mathbb F_3^4\)에 대해 \(v\)와 \(-v\)가 같은 transvection을 주므로 총

\[
40
\]

개의 distinct transvection을 얻는다.

degree-4 tensor action

\[
g^{\otimes4}
\]

을 이용하여 \(T\)의 orbit을 생성하고 \((R)_4\)로 quotient했다.

orbit-span dimension은

- 첫 pass: 24
- 두 번째 pass: 45
- 세 번째 pass: 45

로 안정화되었다.

따라서

\[
\boxed{\dim W=45}.
\]

여기서

\[
W=\langle Sp_4(\mathbb F_3)\cdot[T]\rangle
\subset Q_4,
\]

\[
Q_4=L_4/(R)_4.
\]

참고로 독립적으로 계산한 차원:

\[
\dim L_4=60,
\]

\[
\dim(R)_4=5,
\]

따라서

\[
\dim Q_4=55.
\]

즉

\[
W
\]

는 \(Q_4\)의 55차원 전체가 아니라 45차원의 submodule이다.

---

## XII. 현재까지의 representation-theoretic 결과

\(G=Sp_4(\mathbb F_3)\)의 \(W\)-작용에 대해 실제 계산으로

\[
\boxed{W^{Sp_4(\mathbb F_3)}=0}
\]

을 얻었다.

즉 nonzero invariant vector가 없다.

또한

\[
W_G=W/\langle gw-w\rangle
\]

를 계산한 결과

\[
\boxed{\dim W_G=0}.
\]

실제로

\[
D=\operatorname{span}\{gw-w:g\in Sp_4,\ w\in W\}
\]

의 차원이

\[
\boxed{\dim D=45}
\]

였다.

따라서

\[
W_G=W/D=0.
\]

즉

\[
\boxed{W^{Sp_4}=0,\qquad W_{Sp_4}=0.}
\]

---

## XIII. 이것이 의미하는 것

현재 확인된 것은 다음과 같다.

### 고정벡터 없음

\[
W^{Sp_4}=0
\]

이므로 trivial representation \(\mathbf1\)이 submodule로 직접 나타나지는 않는다.

### trivial quotient 없음

\[
W_{Sp_4}=0
\]

이므로

\[
W\twoheadrightarrow\mathbf1
\]

이라는 비영 \(Sp_4\)-equivariant quotient도 없다.

따라서 가장 단순한 형태의

\[
T\rightarrow W\rightarrow\mathbf1
\]

경로는 막혀 있다.

---

## XIV. 매우 중요한 논리적 주의

다음 명제는 아직 증명되지 않았다.

\[
W^{Sp_4}=0
\quad\text{및}\quad
W_{Sp_4}=0
\]

이라고 해서

\[
[\mathbf1:W]=0
\]

이라고 결론내릴 수 없다.

왜냐하면 현재 characteristic이

\[
\operatorname{char}\mathbb F_3=3
\]

이고

\[
3\mid |Sp_4(\mathbb F_3)|
\]

이므로 Maschke 정리가 적용되지 않기 때문이다.

따라서 \(W\)는 non-semisimple일 수 있다.

trivial representation이 composition series의 중간 층에 존재할 가능성은 아직 열려 있다.

이것이 현재 연구의 핵심 미지수다.

---

## XV. 현재 핵심 미지수

다음 세 가지를 조사해야 한다.

1. Socle

\[
\operatorname{soc}(W)
\]

최소 submodule들의 합.

2. Head

\[
W/\operatorname{rad}(W).
\]

3. Composition multiplicity

\[
\boxed{[\mathbf1:W]}
\]

즉 composition series에서 trivial simple module이 몇 번 등장하는지.

---

## XVI. 왜 이것이 중요한가

### 경우 A

\[
[\mathbf1:W]=0.
\]

그러면

> \(T\)의 전체 \(Sp_4\)-orbit가 생성하는 45차원 구조에는 trivial composition factor 자체가 없다.

따라서 이 \(T\)-probe는 mod-3 orientation carrier가 아닐 가능성이 매우 높다.

그 경우 \(T\)를 orientation이 아니라 higher-order obstruction/probe로 재해석한다.

### 경우 B

\[
[\mathbf1:W]>0
\]

인데도

\[
W^{Sp_4}=W_{Sp_4}=0.
\]

그렇다면 trivial factor가

- submodule도 아니고
- quotient도 아니며
- 중간 extension layer에 존재한다.

이 경우 modular representation theory에서 상당히 흥미로운 현상이 발생한다.

---

## XVII. \(GSp_4\)와 orientation

실제 automorphism 구조에서는 \(Sp_4\)보다

\[
GSp_4(\mathbb F_3)
\]

가 더 자연스러울 가능성이 있다.

similitude character:

\[
\mu:GSp_4(\mathbb F_3)\to\mathbb F_3^\times.
\]

\[
\mathbb F_3^\times\cong C_2.
\]

따라서 mod-3에서 고려할 1차원 character는 적어도

\[
\mathbf1,\qquad\mu
\]

가 핵심이다.

그리고

\[
\mu|_{Sp_4}=1.
\]

따라서 \(GSp_4\)-representation에서 \(\mu\)가 등장하면 \(Sp_4\)에 restriction했을 때 trivial factor처럼 보인다.

하지만 현재는 아직 \(GSp_4\) 분석을 시작할 단계가 아니다.

먼저 \(W\)의 \(Sp_4\)-module 구조를 완전히 파악한다.

---

## XVIII. 최종적인 3-adic 문제

mod-3 단계에서 어떤 orientation 관련 character를 발견한다고 해도 최종 목표는

\[
\chi_{\mathrm{filt}}:G\to\mathbb Z_3^\times
\]

이다.

따라서 장기적으로는

\[
\mathbb F_3
\longrightarrow
\mathbb Z/9
\longrightarrow
\mathbb Z/27
\longrightarrow\cdots
\longrightarrow
\mathbb Z_3
\]

같은 lifting 문제가 발생한다.

이것은 아직 해결하지 않은 장기 과제이며 현재 단계에서 성급하게 주장해서는 안 된다.

---

## XIX. 현재 연구의 학술적 평가

현재 결과를 과장하지 않고 평가한다.

### 확정적으로 의미 있는 부분

1. 특정 degree-4 Lie obstruction \(T\).
2. 정확한 multidegree argument로
   \[
   T\notin(R)_4.
   \]
3. mildness bridge를 통해
   \[
   [v,u,u]\in D_4\setminus D_5.
   \]
4. \(T\)의 symplectic orbit가 생성하는 모듈의 차원이
   \[
   45.
   \]
5. 그 모듈에서
   \[
   W^{Sp_4}=0,\qquad W_{Sp_4}=0.
   \]

### 아직 주장해서는 안 되는 것

- \(T\)가 canonical orientation이라고 주장할 수 없다.
- \(W\)에 trivial composition factor가 없다고 아직 주장할 수 없다.
- orientation이 filtration으로부터 복원된다고 아직 주장할 수 없다.
- 새로운 대정리를 발견했다고 주장할 수 없다.
- 논문 게재 가능성을 현재 결과만으로 단정할 수 없다.

또한 기존 문헌에서 동일하거나 유사한 degree-4 module 및 45차원 representation이 이미 연구되었는지 확인하는 작업이 필요하다.

---

## XX. 다음 연구의 정확한 실행 순서

현재 연구를 여기서 동결한다.

다음에 재개할 때는 아래 순서를 따른다.

### Step 0 — 재현성 확보

45×45 representation을 다시 생성하고 저장한다.

### Step 1 — 생성원 고정

\[
\rho(g_1),\ldots,\rho(g_k)
\]

를 명시한다.

### Step 2 — commutant

\[
\operatorname{End}_G(W)
=
\{A:A\rho(g_i)=\rho(g_i)A\}
\]

계산.

### Step 3 — minimal invariant submodules

\[
\operatorname{soc}(W)
\]

계산.

### Step 4 — maximal submodules / head

\[
W/\operatorname{rad}(W)
\]

계산.

### Step 5 — radical series

\[
W\supset\operatorname{rad}W
\supset\operatorname{rad}^2W
\supset\cdots
\]

계산.

### Step 6 — composition factors

각 simple module의 multiplicity를 결정한다.

특히

\[
\boxed{[\mathbf1:W]}
\]

를 확정한다.

### Step 7 — 그 결과에 따라 분기

\[
[\mathbf1:W]=0
\]

이면 \(T\)-orbit가 orientation carrier가 아니라는 방향으로 정리한다.

반대로

\[
[\mathbf1:W]>0
\]

이면 해당 factor가 어느 radical/socle layer에 존재하는지 조사한다.

### Step 8 — 그 이후에만

\[
GSp_4(\mathbb F_3)
\]

로 확장.

### Step 9 — 마지막으로 필요할 경우

3-adic lifting 및

\[
\chi_{\mathrm{filt}}
\]

복원 문제를 연구한다.

---

## XXI. 계산상의 원칙

가능하면 처음부터 거대한

\[
\mathbb F_3[Sp_4(\mathbb F_3)]
\]

군 대수를 직접 구성하지 않는다.

군의 크기는

\[
|Sp_4(\mathbb F_3)|=51840
\]

이고 characteristic 3이 군의 위수를 나누므로 modular group algebra는 상당히 복잡하다.

우선 우리가 이미 확보한

\[
45\times45
\]

representation과 그 생성원만 사용한다.

권장 순서는

\[
\boxed{
45\times45\text{ matrices}
\rightarrow
\operatorname{End}_G(W)
\rightarrow
\operatorname{soc/head}
\rightarrow
\operatorname{radical/socle\ series}
\rightarrow
\text{composition factors}
}
\]

이다.

SageMath 등을 이용할 수 있지만, Sage의 특정 함수가 자동으로 이 문제를 완벽하게 해결한다고 가정해서는 안 된다. 필요하면 직접 선형대수 기반 알고리즘을 구현한다.

---

## XXII. 연구의 현재 위치를 한 장으로 압축

\[
\boxed{
G=
\langle x_1,x_2,x_3,x_4
\mid
x_1^3[x_1,x_2][x_3,x_4]=1\rangle
}
\]

↓

Zassenhaus filtration

\[
D_1\supset D_2\supset\cdots
\]

↓

associated graded Lie algebra

\[
L=\mathbb L_{\mathbb F_3}(X_1,X_2,X_3,X_4)
\]

↓

quadratic relation

\[
R=[X_1,X_2]+[X_3,X_4]
\]

↓

degree-4 obstruction

\[
T=[[X_3,X_4],X_1],X_1
\]

↓

\[
\boxed{T\notin(R)_4}
\]

↓

mildness bridge

\[
\boxed{[v,u,u]\in D_4\setminus D_5}
\]

↓

symplectic orbit

\[
\boxed{\dim W=45}
\]

↓

현재까지의 representation 결과

\[
\boxed{W^{Sp_4}=0}
\]

\[
\boxed{W_{Sp_4}=0}
\]

↓

아직 미해결

\[
\boxed{
\operatorname{soc}(W),\
W/\operatorname{rad}(W),\
[\mathbf1:W]
}
\]

↓

그 결과에 따라

\[
GSp_4
\]

↓

필요하다면

\[
\mathbb Z_3^\times
\]

↓

최종 목표

\[
\boxed{\chi_{\mathrm{filt}}}
\]

---

## 새 창에서 바로 이어갈 때 사용할 문장

> “아래는 지금까지의 Demuškin orientation 연구 마스터 보존본이다. 여기에 적힌 [확정된 사실]은 다시 의심 없이 전제로 사용하되, [미해결]과 [가설]은 확정된 사실처럼 취급하지 말고, 마지막에 명시된 다음 단계부터 엄밀하게 연구를 이어가자.”

---

## 보존 원칙

이 문서를 **연구의 기준선(baseline)**으로 삼는다.

이후 계산에서 새로운 결과가 나오면 기존 내용을 임의로 덮어쓰지 않고 다음 중 하나로 명시적으로 기록한다.

- **ADDITION** — 새로운 확인 결과
- **CORRECTION** — 기존 내용의 수정
- **RETRACTION** — 기존 가설/결과의 폐기
- **VERIFICATION** — 기존 계산의 독립 재검증
- **LITERATURE** — 외부 문헌에서 확인된 결과
- **OPEN** — 아직 해결되지 않은 문제

특히 문헌에서 알려진 사실, 우리가 직접 계산한 사실, 그 계산으로부터 추론한 사실, 아직 검증되지 않은 가설을 명확히 구분한다.
