# 연구 중간 총정리 — 2026-09-21

> 본 문서는 2026-09-21 현재까지의 Demuškin 연구 전체 흐름을, 연구 시작점부터 현재의 문헌 대조·평가·향후 계획까지 하나의 독립적인 중간 총정리로 묶은 기록이다.  
> 범용적인 “canonical orientation 발견” 주장은 이미 알려진 결과와 중복되므로 폐쇄하고, 현재의 핵심 연구대상을 intrinsic Zassenhaus/Jennings–Lazard finite-window에서의 orientation recognition/factorization 문제로 재정의한다.

---

# 0. 연구의 출발점

대상은 rank-4 pro-3 Demuškin 군

\[
G=
\left\langle
x_1,x_2,x_3,x_4
\mid
x_1^3[x_1,x_2][x_3,x_4]=1
\right\rangle
\]

이고

\[
[a,b]=a^{-1}b^{-1}ab
\]

이다.

초기의 궁극적 관심은 단순히 이 presentation에서 \(\chi\)를 계산하는 것이 아니었다.

목표는

\[
\text{intrinsic filtration}
\longrightarrow
\chi_{\mathrm{filt}}:G\to\mathbf Z_3^\times
\]

라는 구조를 만드는 것이었다.

즉 presentation basis를 선택하지 않고, \(q\)를 먼저 알려주지 않고, canonical orientation 자체를 입력으로 넣지 않고, Zassenhaus/Jennings–Lazard filtration 또는 그로부터 나오는 intrinsic object만 사용해서 canonical \(3\)-adic orientation을 복원할 수 있는지를 묻는 연구였다.

---

# 1. 1차 목표: filtration에서 q-정보가 보이는가?

초기에는 Demuškin relation의

\[
x_1^3
\]

이라는 power term이 Zassenhaus filtration의 더 깊은 층에 들어가므로, 단순한 quadratic graded Lie algebra를 넘어 더 깊은 filtration information을 보면 \(q=3\)이라는 정보가 나타날 수 있지 않겠느냐는 생각에서 시작했다.

특히

\[
R=[X_1,X_2]+[X_3,X_4]
\]

를 quadratic initial relation으로 놓고 degree-3 restricted/power 정보를 함께 보면 \(q=3\)과 orientation의 첫 번째 \(3\)-adic digit을 구분할 수 있을 가능성을 탐색했다.

---

# 2. 첫 번째 중요한 성과: \(D_4\setminus D_5\)의 explicit witness

초기 연구에서

\[
u=x_1^{-2},
\qquad
v=[x_3,x_4]^{-1}
\]

를 놓고

\[
(uv)^3=x_2^{-1}x_1^3x_2
\]

를 계산했다.

그리고

\[
u\in D_1,\qquad v\in D_2
\]

에서 출발하여

\[
[v,u,u]\in D_4
\]

를 얻었다.

그러나 \(D_4\)에 있다는 것만으로는 충분하지 않았다. 실제로

\[
[v,u,u]\notin D_5
\]

인지가 중요했다.

associated graded에서

\[
R=[X_1,X_2]+[X_3,X_4]
\]

를 놓고

\[
T=[e_6,X_1,X_1]
\]

이라는 multidegree

\[
(2,0,1,1)
\]

의 항을 선택했고,

\[
T\notin(R)_4
\]

를 보이는 방향으로 진행했다.

이 단계의 중요한 의미는

\[
\text{filtered group calculation}
\longrightarrow
\text{graded Lie obstruction}
\]

이라는 구조를 실제 계산으로 만들었다는 것이다.

다만 이후 연구 원칙에 따라 당시의 rank 계산과 좌표 증명 중 충분히 엄밀하지 않았던 부분은 다시 audit했고, 계산 결과와 논리적 결론을 분리해 관리했다.

---

# 3. 표현론 단계: \(W\)의 구조를 해부

다음에는 \(Sp_4(\mathbf F_3)\)-representation으로서의 \(W\)를 분석했다.

중요한 교정이 있었다. 처음에는 잘못된 symplectic matrix를 사용했으나, 올바른 것은

\[
J=
\begin{pmatrix}
0&1&0&0\\
-1&0&0&0\\
0&0&0&1\\
0&0&-1&0
\end{pmatrix}.
\]

잘못된 \(J\)는 orbit 계산을 오염시킬 수 있으므로 올바른 \(J\)로 재검증했다.

그 결과

\[
\operatorname{End}_H(W)=\mathbf F_3[I,N],
\qquad N^2=0
\]

를 얻었고,

\[
U=\operatorname{Im}N,\quad \dim U=10,
\]

\[
K=\ker N,\quad \dim K=35,
\]

\[
M=K/U,\quad \dim M=25
\]

를 얻었다.

또

\[
\operatorname{End}_H(M)=\mathbf F_3
\]

및

\[
\Delta O\simeq_H U
\]

등을 확인했다.

Lübeck/GAP/Doty 계열 독립 검산과 Brauer degree 자료도 이용했다.

---

# 4. 표현론만으로는 충분하지 않다는 교훈

예를 들어

\[
W^{Sp_4}=0,\qquad W_{Sp_4}=0
\]

이라는 결과는 유용하지만 characteristic 3에서 trivial composition factor의 존재를 완전히 배제하지는 못한다.

따라서

“invariants가 0이다 → 원하는 canonical line이 없다”

와 같은 식의 비약은 금지했다.

이 경험 이후 계산 결과와 그로부터 가능한 논리적 결론을 별도의 Gate로 검증하는 연구 방식이 정착했다.

---

# 5. rank-4 \(D_4\) cocycle 방향

다음에는 rank-4 \(D_4\) extension에서 \(q\)-sensitive observable을 만들려고 했다.

특히

\[
\Delta_q(g)
=
[F_g(X_1^3)-X_1^3]_3
\]

같은 양을 생각했다.

정확한 계산 결과

\[
\Delta_q(g)
=
g\cdot[X_1^3]-[X_1^3]
\]

였고,

\[
\Delta_q=\delta([X_1^3])
\]

인 ordinary coboundary임을 확인했다.

따라서 cocycle law는 맞지만 새로운 cohomology class가 아니다.

이 branch는

\[
\boxed{\text{FAIL/CLOSED}}
\]

이다.

중요한 교훈은 “계산상 cocycle”과 “새로운 \(H^1\) class”가 다르다는 것이다.

---

# 6. quadratic graded object는 충분하지 않다

다음으로

\[
G_3=
\langle x_i\mid x_1^3[x_1,x_2][x_3,x_4]\rangle
\]

와

\[
G_\infty=
\langle x_i\mid[x_1,x_2][x_3,x_4]\rangle
\]

를 비교했다.

두 군의 quadratic initial relation은 동일하다.

\[
R_2=[X_1,X_2]+[X_3,X_4].
\]

하지만

\[
\chi_3(x_2)=(1-3)^{-1}=4\pmod9
\]

이고 power-free control에서는

\[
\chi_\infty(x_2)=1\pmod9.
\]

따라서

\[
\boxed{
\text{bare mod-3 associated graded}
\not\Rightarrow
\chi\bmod9
}
\]

이다.

---

# 7. full mod-3 graded object도 q-blind

더 강하게 complete mod-3 Zassenhaus/Jennings graded object 자체가 \(q\)-information을 잃는다는 방향을 확인했다.

따라서

\[
\boxed{
\text{full mod-3 associated graded}
\not\Rightarrow q
\not\Rightarrow\chi
}
\]

이다.

단, 이것은 “모든 higher cohomological structure가 q-blind”라는 뜻은 아니다. 뒤에서 Pál–Quick과 대조하면서 이 구분이 중요해졌다.

---

# 8. bounded degree + bounded precision no-go

가족

\[
G_{3^s}
=
\langle x_i\mid
x_1^{3^s}[x_1,x_2][x_3,x_4]
\rangle
\]

를 사용했다.

\[
\chi_{3^s}(x_2)=(1-3^s)^{-1}
\]

이고 \(x_1^{3^s}\)는 Zassenhaus degree \(3^s\)에서 처음 등장한다.

따라서 고정된 degree bound \(d\)에 대해 \(3^s>d\)인 \(s\)를 선택하면 bounded filtration data가 \(q=3^s\)와 power-free control을 구별하지 못한다.

또 coefficient precision을 \(\bmod3^N\)로 제한하면 \(s\ge N\)에서 같은 현상이 발생한다.

따라서

\[
\boxed{
\text{bounded filtration degree}
+
\text{bounded }3\text{-adic precision}
\not\Rightarrow
\text{full }\chi
}
\]

이다.

이것은 연구 범위를 크게 좁혔다.

---

# 9. fixed \(q=3\)에서는 상황이 다르다

위의 no-go는 family 전체에 대한 것이다.

고정된 \(q=3\)에서는 exact \(\mathbf Z_3\)-coefficient relation data를 사용하면

\[
1+2\chi(x_2)=0
\]

에서

\[
\chi(x_2)=-\frac12=(1-3)^{-1}
\]

을 얻는다.

따라서 “bounded degree이면 full \(\chi\)를 절대 못 얻는다”는 명제는 틀리다.

정확한 no-go는

> bounded filtration degree + bounded \(3\)-adic precision으로는 universal full-\(\chi\) recovery가 불가능하다.

이다.

---

# 10. 첫 번째 성공적인 carrier: \((R,P_3)\)

mod 9 수준에서는 quadratic relation만으로는 부족하지만 degree-3 power component \(P_3\)를 함께 사용하면 된다.

projective relation jet

\[
J_3=\langle(R_2,P_3)\rangle
\subset L_2\oplus L_3^{res}
\]

를 구성하고,

\[
\Theta_J(\lambda)(f)
=
f(P_3)+(\lambda\wedge f)(R_2)
\]

를 정의했다.

표준 relation에서

\[
P_3\sim e_1^{(1)}
\]

이고 유일한 zero가

\[
\lambda=e_2^*
\]

가 되어

\[
\chi\bmod9=(1,4,1,1)
\]

을 얻었다.

즉

\[
\boxed{
[(R,P_3)]
\longrightarrow
\chi\bmod9
}
\]

라는 첫 번째 성공적인 carrier가 나왔다.

---

# 11. cup + Bockstein으로 intrinsic carrier 만들기

\((R,P_3)\)가 presentation coordinate처럼 보이는 문제를 해결하기 위해

\[
V=H^1(G,\mathbf F_3)^*
\]

에서

\[
\smile:H^1\times H^1\to H^2
\]

와

\[
\beta:H^1\to H^2
\]

를 사용했다.

\(H^2\)가 1차원이므로 임시로 \(\omega\neq0\)를 잡으면

\[
f\smile g=(f\wedge g)(R)\omega,
\]

\[
\beta(f)=f(p)\omega.
\]

\(\omega\)를 바꾸면 \(R,p\)가 같은 scalar로 변하므로

\[
\boxed{
\overline J_3(G)=[(R,p)]
}
\]

는 canonical projective object가 된다.

Bockstein과 relation-jet의 identification은 standard one-relator transgression/relation-Bockstein formula와 frozen relator에 대한 직접 \(\mathbf Z/9\)-lifting 계산으로 독립 확인했다.

absolute \(H^2\)-normalization은 gauge-dependent이므로 projective level에서만 canonical하다고 유지했다.

---

# 12. presentation/gauge invariance

degree \(\le3\)에서 residual transformation은

\[
(R,P)\mapsto(uR,uP+[v,R])
\]

형태이다.

recovery functional에서 \(P\)에 추가되는 \([v,R]\) 부분은 degree-one functional에 의해 사라진다.

따라서 recovery zero set은 presentation/gauge change에 대해 불변이다.

결과:

\[
\boxed{
\text{projective degree-(2,3) carrier}
\to
\chi\bmod9
}
\]

는 mod 9에서 presentation/gauge invariant이다.

---

# 13. Pál–Quick 2601.07551 문헌 대조

Pál–Quick, “A_3-formality for Demushkin groups at odd primes”는 odd-p Demuškin group의 continuous cochain DGA에 대해 \(A_3\)-formality를 연구한다.

핵심은

- \(q\neq3\): \(A_3\)-formal
- \(q=3\): \(A_3\)-formal하지 않음

이며 Benson–Krause–Schwede canonical Hochschild class를 계산한다.

우리 연구의 Bockstein/\(P_3\) carrier와 Pál–Quick의 \(A_3\)/Hochschild class는 모두 표준 p=3 family에서 q=3의 first power layer를 검출한다.

그러나 두 object가 동일하다고 아직 증명하지 않았다.

따라서

\[
\boxed{\text{PASS/LOCAL}}
\]

이며 equality/factorization theorem은 OPEN이다.

중요한 경계:

\[
\text{mod-3 graded filtration alone is q-blind}
\]

이지

\[
\text{every higher cohomological structure is q-blind}
\]

가 아니다.

---

# 14. exact \(Z_3\) carrier와 Fox 방향

fixed \(q=3\)에서는

\[
1+2\rho(x_2)=0
\]

으로 full \(3\)-adic value를 얻을 수 있다.

그러나 universal family에서 bounded finite information no-go가 있기 때문에 이것을 universal finite theorem으로 확대할 수 없다.

exact local Fox scheme은

\[
\mathbf Z_3[[u_1,u_2,u_3,u_4]]
/
(u_1,u_3,u_4,2u_2+3)
\cong\mathbf Z_3
\]

라는 reduced characteristic-zero point로 collapse한다.

따라서 full \(\mathbf Z_3\)-orientation을 보존하는 nontrivial finite quotient compression은 불가능하다.

판정:

- quotient-of-local-Fox-scheme compression: FAIL/CLOSED
- exact local Fox carrier minimality: PASS/CLOSED
- independent intrinsic non-quotient exact compression: OPEN

---

# 15. degree-3 Fox truncation 실패

Nielsen-equivalent presentation

\[
x_1=y_1y_2,\quad
x_2=y_2,\quad
x_3=y_3,\quad
x_4=y_4
\]

을 사용했다.

full exact Fox row는 transported canonical point에서 0이어야 하지만 degree \(\le3\) truncation을 취하면 second row가

\[
-\frac{243}{2}\neq0
\]

가 된다.

따라서

\[
\boxed{
\text{presentation-independent degree-3 Fox truncation}
=
\text{FAIL/CLOSED}
}
\]

이다.

이는 Fox 전체를 폐기하는 것이 아니라 naive fixed-degree truncation을 intrinsic carrier로 동일시할 수 없다는 뜻이다.

---

# 16. ordinary integral augmentation jet 실패

plain integral augmentation carrier

\[
\langle r-1\rangle\subset I^2/I^4
\]

는

\[
x_1^3-1=3X_1+3X_1^2+X_1^3
\]

때문에

\[
r-1=3X_1+R+O(I^3)
\]

이고

\[
r-1\notin I^2.
\]

따라서 ordinary integral augmentation jet은 원하는 object가 아니다.

\[
\boxed{\text{FAIL/CLOSED}}
\]

mixed \((3,I)\)-adic filtration은 nearby candidate로 남겨두었다.

---

# 17. HA61: mod 27로 올라가면서 생긴 문제

mod 27에서는

\[
0\to\mathbf F_3
\to\mathbf Z/27(\rho_3)
\to\mathbf Z/9(\rho_2)
\to0
\]

의 connecting map

\[
\delta_{3,\rho_3}
\]

를 사용한다.

초기의 목표는 단일 presentation-independent \(t_2\)를 찾아 secondary orientation carrier로 만드는 것이었다.

그러나 raw \(t_2\)는 intrinsic하지 않다는 것이 드러났다.

---

# 18. HA61-B: intrinsic secondary family는 살아남음

각 \(\rho_3\) lift마다

\[
\delta_{3,\rho_3}
\]

가 canonical하게 정의된다.

따라서

\[
\boxed{
\rho_3\longmapsto\delta_{3,\rho_3}
}
\]

라는 function-valued family는 intrinsic이다.

또 pure relator conjugation

\[
r'=vrv^{-1}
\]

에서 full crossed-cocycle calculation을 하면 모든 추가항이 정확히 cancellation되어 intrinsic obstruction family가 유지된다.

판정:

- intrinsic secondary family: PASS/CLOSED
- pure-conjugation invariance: PASS/CLOSED

---

# 19. raw \(t_2\)와 affine quotient는 폐쇄

relator conjugation에 의해 coordinate residual \(t_2\)는 변하지만 intrinsic \(\rho_3,\mu\)와 full obstruction family는 변하지 않는다.

따라서 raw \(t_2\)는 natural transformation이 아니다.

\[
\boxed{t_2\text{ alone}=FAIL/CLOSED}
\]

또

\[
(t_2,\mu)/\mathbf F_3(p,\lambda)
\]

형태의 affine quotient도 orientation carrier로는 실패한다. 서로 다른 coefficient actions를 quotienting하여 구별하지 못하게 하기 때문이다.

---

# 20. fixed-\(f\) zero uniqueness의 오류와 수정

처음에는 variation formula

\[
\delta_{3,\rho_3'}(f)-\delta_{3,\rho_3}(f)
=
\nu\smile f
\]

를 이용해 fixed \(f\)에 대해 unique zero를 생각했다.

그러나

\[
\nu\mapsto\nu\smile f
\]

는 rank 4에서 nonzero linear functional이므로 kernel은 3차원이다.

따라서 fixed \(f\)에서는 최대

\[
3^3=27
\]

개의 zero가 가능하다.

\[
\boxed{\text{fixed-}f\text{ zero selector uniqueness}=FAIL/CLOSED}
\]

그러나 실제 selector 문제는 fixed \(f\)가 아니라

\[
\delta_{3,\rho_3}\equiv0
\]

라는 global zero-map이다.

variation identity, mod-9-to-mod-3 \(H^1\) surjectivity, Demuškin cup nondegeneracy가 성립한다면 global zero-map uniqueness는

\[
\boxed{\text{PASS/LOCAL conditional}}
\]

이다.

존재성과 finite filtered factorization은 별도 OPEN이다.

---

# 21. B2: finite Kummer selector 프로그램

연구의 핵심 질문을

\[
Q_k=G/P_{k+1}(G)
\]

만을 사용해서

\[
\chi\bmod3^k
\]

를 자연스럽게 인식할 수 있는가?

로 좁혔다.

조건은 다음과 같다.

- \(\chi\) 자체를 input으로 넣지 않는다.
- \(q\)를 먼저 알려주지 않는다.
- dualizing action을 input으로 넣지 않는다.
- presentation basis에 의존하지 않는다.
- Kummer lifting obstruction을 intrinsic하게 구성한다.

---

# 22. B2의 finite crossed-cocycle factorization

\[
A_k=\mathbf Z/3^k,
\qquad
U_j=1+3^j\mathbf Z/3^k
\]

와

\[
S_k=A_k\rtimes U_1
\]

를 구성했다.

\[
T_j=3^{j-1}A_k\rtimes U_j
\]

에 대해

\[
P_j(S_k)=T_j
\]

를 induction으로 증명했다.

따라서

\[
P_{k+1}(S_k)=1.
\]

crossed cocycle와 coefficient character를 합친

\[
\psi=(z,\rho):G\to S_k
\]

는

\[
\psi(P_{k+1}(G))=1
\]

이므로

\[
Q_k=G/P_{k+1}(G)
\]

로 factor된다.

따라서

\[
\boxed{\text{finite crossed-cochain factorization = PASS}}
\]

이다.

---

# 23. Fox–Kummer equivalence

Fox coefficients

\[
F_i(\rho)
\]

를 놓고 ideal

\[
I=(F_i(\rho))
\]

를 생각했다.

finite Kummer lifting surjectivity를 basis-vector별로 적용하면

\[
I\subseteq3I
\]

가 되고 Nakayama로

\[
I=0
\]

을 얻는다.

역방향은 직접적이다.

따라서

\[
\boxed{
\text{Kummer lifting predicate}
\iff
\text{twisted Fox row vanishing}
}
\]

이다.

---

# 24. standard odd-p Demuškin에서 직접 소거

standard relation에 대해 twisted Fox equation을 직접 풀면

\[
\rho_{2i-1}=1
\]

및 나머지 좌표가 trivial이고,

\[
\rho_2=(1-q)^{-1}
\]

이 된다.

따라서

\[
\rho=\chi\bmod3^k.
\]

Hensel은 proof dependency에서 제거했다.

standard odd-p 존재/유일성은 PASS/LOCAL이고, arbitrary odd-p 확장은 Labute classification을 사용한다.

---

# 25. B2 \(k=2\): 실제 finite-window 성공

\[
Q_2=G/P_3
\]

에서 universal Kummer lifting predicate를 평가했다.

그 결과

\[
\rho=(1,4,1,1)\pmod9
\]

가 유일한 solution이었다.

또

- q-blind
- natural
- unique
- \(P_3\)-annihilation verified

가 확인되었다.

따라서

\[
\boxed{
G/P_3\to\chi\bmod9
}
\]

라는 genuine finite-window factorization이 성립한다.

현재 판정:

\[
\boxed{\text{B2/}k=2=\text{PASS/LOCAL}}
\]

---

# 26. B2 general \(k\)

general \(k\)에 대해

\[
P_{k+1}(S_k)=1
\]

이 증명되어 finite quotient factorization의 algebraic part는 닫혔다.

하지만 이것만으로

\[
Q_k\Rightarrow\chi\bmod3^k
\]

라는 novel recognition theorem이 완성되는 것은 아니다.

핵심은 기존 문헌이 같은 construction을 이미 포함하는지 여부이다.

---

# 27. one-relator stress test

standard rank-4 Demuškin relation에서는

\[
k=2:\ (1,4,1,1),
\]

\[
k=3:\ (1,13,1,1)
\]

이라는 unique finite Kummer selector가 유지된다.

반면 degenerate quadratic one-relator에서는 3→9 candidates가 나타나고,

power+degenerate relation에서는 candidate가 없는 경우도 나타났다.

이는

\[
\boxed{
\text{Demuškin-type nondegeneracy}
\Rightarrow
\text{Kummer selector rigidity}
}
\]

라는 diagnostic을 제공한다.

그러나 아직 general theorem은 아니다.

다음 authorized target은

\[
r=[x_1,x_2][x_1,x_3]
\]

에서 실제 higher obstruction을 계산하는 것이다.

---

# 28. Labute 문헌 대조

Labute의 “Classification of Demushkin Groups”는 canonical orientation의 존재·유일성을 이미 다룬다.

Serre가 도입한 unique continuous

\[
\chi:G\to U_p
\]

가 있고, \(I_j(\chi)\)에 대한

\[
H^1(G,I_j(\chi))\to H^1(G,I_1(\chi))
\]

surjectivity가 모든 \(j>1\)에 대해 성립하는 조건으로 orientation을 characterization한다.

Theorem 4는 모든 Demuškin group에 대해 그러한 unique \(\chi\)가 존재함을 보인다.

또

\[
\chi(x_2)=(1-q)^{-1}
\]

등의 explicit formula가 standard presentation에서 나온다.

따라서

> Demuškin group의 canonical orientation을 새롭게 발견한다

는 주장은

\[
\boxed{\text{KNOWN / CLOSED}}
\]

이다.

---

# 29. Labute와 filtration

Labute는 descending q-central series와 associated graded Lie algebra도 사용한다.

따라서

\[
\text{Demuškin + filtration + graded Lie algebra}
\]

자체도 신규 claim으로 사용할 수 없다.

이 부분은

\[
\boxed{\text{FAIL/CLOSED as novelty}}
\]

이다.

---

# 30. 현대 Blumer–Quadrelli 대조

Blumer–Quadrelli 2026 논문은 Demuškin-like pro-p families, Kummerian/cyclotomic orientation, p-Zassenhaus filtration, associated graded restricted Lie structure, completed group algebra/Jennings-type structures 등을 함께 연구한다.

따라서

\[
\text{Demuškin}
+
\text{canonical orientation}
+
\text{Zassenhaus/graded structure}
\]

이라는 broad combination 역시 새롭다고 할 수 없다.

그러나 현재까지 대조한 범위에서 정확히 확인되지 않은 것은

\[
\boxed{
\operatorname{Fil}_{intr}(G)
\longrightarrow
\chi_G
}
\]

를 orientation을 input으로 주지 않고 natural factorization으로 만드는 것, 특히

\[
\boxed{
G/P_{k+1}\longrightarrow\chi_G\bmod3^k
}
\]

라는 finite-window recognition theorem이다.

---

# 31. Pál–Quick과 Blumer–Quadrelli를 함께 대조한 결과

문헌 대조의 최종 경계는 다음과 같다.

이미 알려진 것:

1. canonical orientation의 존재·유일성
2. Kummerian/oriented characterization
3. Demuškin classification
4. filtration/graded Lie structure
5. q와 orientation의 standard relation
6. higher cohomological structure를 통한 q=3 detection

아직 명확히 중복되었다고 결론내리지 못한 것:

\[
\boxed{
Q_k=G/P_{k+1}
\text{ 자체에서 }
\chi\bmod3^k
\text{를 finite predicate로 recognition}
}
\]

단, finite-coefficient version의 기존 Kummerian quotient inheritance theorem이 존재한다면 이 novelty도 사라질 수 있다.

---

# 32. quotient correction

이전에는

\[
P_{k+1}\not\subseteq K_\theta
\]

같은 non-inclusion 방향을 생각했지만 이는 잘못된 방향이다.

실제로 finite coefficient character에 대해서는

\[
P_{k+1}
\subseteq
\ker(\theta\bmod3^k)
\]

가 성립한다.

따라서 “\(P_{k+1}\)이 kernel에 들어가지 않는다”는 주장은 폐기한다.

그러나 기존 quotient inheritance theorem이 이미 주어진 infinite orientation \(\theta\)를 전제로 한다면, 그것이 우리가 원하는 finite recognition theorem을 이미 제공한다고 볼 수는 없다.

정확한 문헌 Gate는:

> finite-coefficient \(K_{\theta\bmod3^k}\) 또는 equivalent quotient inheritance theorem이 현재의 construction을 이미 포함하는가?

이다.

현재 판정:

\[
\boxed{\text{NOVELTY OPEN / LITERATURE VERIFICATION REQUIRED}}
\]

---

# 33. 현재까지 폐쇄된 주요 경로

1. canonical orientation 자체가 새로운 발견 → FAIL/CLOSED
2. Demuškin + filtration/graded Lie 자체가 새로운 조합 → FAIL/CLOSED
3. bare graded \(\Rightarrow\chi\bmod9\) → FAIL/CLOSED
4. full mod-3 graded \(\Rightarrow q\) → FAIL/CLOSED
5. bounded degree + bounded precision \(\Rightarrow\) full \(\chi\) → FAIL/CLOSED
6. \(\Delta_q\)가 새로운 \(H^1\) class → FAIL/CLOSED; coboundary
7. ordinary integral augmentation jet → FAIL/CLOSED
8. degree-3 Fox truncation → FAIL/CLOSED
9. raw \(t_2\) carrier → FAIL/CLOSED
10. affine \((t_2,\mu)\) quotient carrier → FAIL/CLOSED
11. fixed-\(f\) zero uniqueness → FAIL/CLOSED

---

# 34. 현재까지 살아남은 주요 결과

\[
\boxed{T\notin(R)_4}
\]

계열의 filtration obstruction.

\[
\boxed{[(R,P_3)]\to\chi\bmod9}
\]

mod-9 projective carrier.

\[
\boxed{(H^1,H^2,\smile,\beta)\to[(R,p)]}
\]

intrinsic cup+Bockstein carrier.

\[
\boxed{G/P_3\to\chi\bmod9}
\]

finite-window local success.

\[
\boxed{P_{k+1}(A_k\rtimes U_k)=1}
\]

general finite crossed-cochain factorization.

\[
\boxed{\text{Kummer lifting}\iff\text{twisted Fox vanishing}}
\]

finite Kummer–Fox equivalence.

\[
\boxed{\rho_3\mapsto\delta_{3,\rho_3}}
\]

intrinsic secondary obstruction family.

\[
\boxed{\text{global zero-map uniqueness}}
\]

conditional PASS/LOCAL.

---

# 35. 현재 연구의 핵심 열린 문제

가장 중요한 문제는

\[
\boxed{
G/P_{k+1}
\quad\stackrel{?}{\Longrightarrow}\quad
\chi\bmod3^k
}
\]

이다.

단,

- \(\chi\)를 input으로 넣지 않고,
- \(q\)를 input으로 넣지 않고,
- dualizing action을 input으로 넣지 않고,
- presentation basis를 선택하지 않고,
- 이미 알려진 Serre orientation criterion을 단순히 다시 쓰지 않아야 한다.

현재 \(k=2\)는 PASS/LOCAL이고 general \(k\)의 algebraic factorization은 상당 부분 닫혔지만 novelty gate는 OPEN/DECISIVE이다.

---

# 36. HA61-B의 현재 위치

HA61-B:

\[
\rho_2
\to
\{\rho_3\text{ lifts}\}
\to
\delta_{3,\rho_3}
\]

라는 secondary obstruction family를 다룬다.

현재:

- intrinsic family: PASS/CLOSED
- total connecting obstruction gauge invariance: PASS/CLOSED
- raw \(t_2\): FAIL/CLOSED
- affine quotient: FAIL/CLOSED
- global zero-map uniqueness: PASS/LOCAL conditional
- universal variation identity: OPEN/DECISIVE
- finite filtered existence: OPEN/DECISIVE
- \(G/P_4\) factorization: OPEN/DECISIVE
- HA61-C: 아직 열지 않음

이다.

---

# 37. 전체 연구의 논리적 구조

\[
G
\]

에서 출발하여:

### Level 0 — classical knowledge

\[
G\to\chi_G
\]

는 이미 알려짐.

### Level 1 — bare graded

\[
G\to\operatorname{gr}_D(G)
\]

는 q-blind.

### Level 2 — first extension/power datum

\[
\operatorname{gr}_D(G)+P_3
\]

또는

\[
[(R,P_3)]
\]

에서

\[
\chi\bmod9
\]

복원.

### Level 3 — finite coefficient window

\[
Q_k=G/P_{k+1}
\]

에서 Kummer lifting predicate 구성.

\(k=2\) 성공.

### Level 4 — higher digits

\[
Q_3=G/P_4\to\chi\bmod27
\]

및 \(\delta_{3,\rho_3}\) family.

현재 OPEN/DECISIVE.

### Level infinity

\[
\{J_n\}_{n\ge1}
\to
\{\chi_n\}_{n\ge1}
\to
\chi.
\]

이것이 궁극적인 filtered tower reconstruction 방향이다.

---

# 38. 논문으로 쓴다면 현재 적절한 주제

“Canonical orientation of Demuškin groups from filtration” 같은 제목은 피해야 한다.

가능한 방향은:

### A
**Finite-window reconstruction of the canonical orientation of Demuškin pro-3 groups**

핵심:

\[
G/P_{k+1}\to\chi\bmod3^k.
\]

### B
**Filtered Kummer recognition of the canonical orientation**

Kummer lifting predicate를 finite filtered quotient에 내려 orientation을 recognition.

### C
**The first extension datum beyond the graded Demuškin Lie algebra**

핵심:

\[
\operatorname{gr}(G)\not\Rightarrow\chi\bmod9
\]

이지만

\[
[(R,P_3)]\Rightarrow\chi\bmod9.
\]

이 경우 논문의 중심은 “orientation 발견”이 아니라 “graded information의 insufficiency와 first sufficient extension datum”이다.

---

# 39. 논문에 포함해야 할 negative results

연구의 가치를 높이는 중요한 negative results:

### Negative theorem 1

\[
\operatorname{gr}_{D}(G)\not\Rightarrow\chi\bmod9.
\]

### Negative theorem 2

full mod-3 graded object도 q-blind.

### Negative theorem 3

bounded filtration + bounded \(3\)-adic precision은 full \(\chi\)를 결정하지 못함.

### Negative theorem 4

degree-3 Fox truncation은 Nielsen invariant가 아님.

### Negative theorem 5

raw \(t_2\)는 intrinsic하지 않음.

이렇게 하면 논문의 메시지는 “여러 가지를 시도했다”가 아니라

> 정보의 경계를 단계적으로 결정했고, 그 경계에서 처음 필요한 extension datum을 찾았다

가 된다.

---

# 40. 현재 전체 판정표

| 연구 대상 | 현재 판정 |
|---|---|
| Demuškin canonical orientation 존재 | KNOWN / CLOSED |
| canonical orientation 유일성 | KNOWN / CLOSED |
| filtration/graded Lie 사용 자체의 신규성 | FAIL/CLOSED |
| bare graded \(\Rightarrow\chi\bmod9\) | FAIL/CLOSED |
| full mod-3 graded \(\Rightarrow q\) | FAIL/CLOSED |
| bounded degree + bounded precision \(\Rightarrow\chi\) | FAIL/CLOSED |
| \(D_4\setminus D_5\) explicit obstruction | PASS |
| projective \((R,P_3)\Rightarrow\chi\bmod9\) | PASS/CLOSED |
| cup+Bockstein intrinsic carrier | PASS/CLOSED |
| Pál–Quick \(A_3\)와 detection compatibility | PASS/LOCAL |
| equality with Pál–Quick class | OPEN |
| exact fixed-\(q=3\) carrier | PASS/CLOSED |
| universal finite exact compression | FAIL/CLOSED |
| naive Fox degree-3 truncation | FAIL/CLOSED |
| raw \(t_2\) carrier | FAIL/CLOSED |
| \(\delta_{3,\rho_3}\) family intrinsicity | PASS/CLOSED |
| fixed-\(f\) zero uniqueness | FAIL/CLOSED |
| global zero-map uniqueness | PASS/LOCAL conditional |
| finite crossed-cocycle factorization | PASS |
| Fox–Kummer equivalence | PASS |
| B2 \(k=2\), \(G/P_3\to\chi\bmod9\) | PASS/LOCAL |
| B2 general \(k\), mathematical factorization | PASS 상당 부분 |
| B2 general \(k\), novelty | OPEN/DECISIVE |
| \(G/P_4\to\chi\bmod27\) | OPEN/DECISIVE |
| HA61-B | OPEN/LOAD-BEARING |
| overall publication-level novelty | OPEN/CONDITIONAL |

---

# 41. 현재 연구의 가장 정확한 평가

“우리가 canonical orientation을 발견했다”는 것은 아니다. Labute가 이미 존재·유일성을 증명했다.

“우리가 Demuškin filtration에서 q를 처음 발견했다”도 아니다. Labute classification이 이미 q, image chi, relation form을 연결한다.

“우리가 graded Lie algebra에서 orientation을 복원했다”도 아니다. 오히려 bare graded Lie data는 충분하지 않다는 것이 연구 결과다.

현재 살아 있는 질문은:

\[
\boxed{
\text{How much finite filtered extension information is necessary and sufficient to recognize }\chi\bmod3^k?
}
\]

그리고 가장 구체적인 후보는

\[
\boxed{
G/P_{k+1}
\quad\text{+ finite Kummer lifting obstruction}
}
\]

이다.

이 부분은 아직 선행문헌과 동일하다고 최종 판정되지 않았다.

---

# 42. 향후 연구 플랜 1 — 문헌 Gate를 먼저 닫는다

가장 먼저 확인할 질문:

\[
\boxed{
\text{Is there already a finite-coefficient theorem }
Q_k=G/P_{k+1}\Rightarrow\chi\bmod3^k?
}
\]

특히

- \(K_\theta\)
- \(K_{\theta\bmod3^k}\)
- quotient inheritance
- Kummerianity
- finite coefficient lifting
- Frattini cover
- \(G/N\) orientation inheritance

를 line-by-line 비교한다.

결과가 동일하면 HISTORICAL/SUPERSEDED, 약한 reformulation이면 CONDITIONAL, infinite \(\chi\)를 input으로 요구하면서 finite recognition을 제공하지 않으면 B2가 살아남는다.

---

# 43. 향후 연구 플랜 2 — \(k=3\)

문헌 Gate 통과 후

\[
Q_3=G/P_4
\]

를 직접 공격한다.

첫 작업은

\[
P_4\subseteq\ker(\rho\bmod27)
\]

의 direct verification이다.

그 뒤

\[
Q_3\to\chi\bmod27
\]

을 theorem으로 올린다.

---

# 44. 향후 연구 플랜 3 — one-relator boundary

\[
r=[x_1,x_2][x_1,x_3]
\]

에서

\[
\bar\delta_4\circ\iota_1
\]

를 직접 계산한다.

목적은 multiple-selector 상황에서 higher coefficient-extension obstruction이 실제로 selector를 좁히는지 확인하는 것이다.

성공하면

\[
\text{primary finite selector}
+
\text{secondary obstruction}
\to
\text{higher rigidity}
\]

라는 구조가 나온다.

실패해도 중요한 boundary theorem이 된다.

---

# 45. 향후 연구 플랜 4 — HA61-B variation identity

핵심 식:

\[
\delta_{3,\rho_3'}(f)
-
\delta_{3,\rho_3}(f)
=
\nu\cup f.
\]

이를 완전히 증명해 global zero-map uniqueness를 theorem으로 올린다.

단,

- coefficient lift source
- representative gauge
- relator gauge
- \(D_4\)/higher terms
- filtration cutoff

를 모두 분리 검증해야 한다.

---

# 46. 향후 연구 플랜 5 — \(n\to n+1\) induction

장기적으로

\[
\rho_n\to\rho_{n+1}
\]

에서 obstruction을 정의하고

\[
\chi_n\to\chi_{n+1}
\]

을 canonical하게 결정하는 induction을 만든다.

그러면

\[
\{\chi_n\}_{n\ge1}
\]

의 inverse limit로

\[
\chi=\varprojlim_n\chi_n
\]

을 얻을 수 있다.

이것이 진짜 “filtered tower → \(3\)-adic orientation” theorem이다.

---

# 47. 향후 연구 플랜 6 — representation branch의 위치

초기의 \(Sp_4\) representation 계산은 폐기할 필요는 없다.

다만 최종 orientation theorem의 주된 input으로 두기보다는

- extension structure,
- obstruction module,
- \(U,K,M,\Delta O\)

등을 설명하는 보조 결과로 위치시키는 것이 적절하다.

현재 full ambient \(Sp_4(\mathbf F_3)\)의 actual automorphism lift는 torsion line 때문에 FAIL/CLOSED이다.

---

# 48. 향후 연구 플랜 7 — Pál–Quick과의 연결

현재는

\[
[(R,p)]
\]

와 Pál–Quick의 BKS/Hochschild \(A_3\) class가 모두 q=3 first power layer를 detect한다는 수준이다.

동일성을 주장하려면 자연스러운 map

\[
[(R,p)]\to\gamma_{A_3}
\]

을 정의하고

1. well-defined
2. functorial
3. presentation-independent
4. gauge-independent

를 증명해야 한다.

그 전까지는

\[
\boxed{\text{detection compatibility only}}
\]

이다.

---

# 49. 연구 전체를 압축한 최종 구조

\[
\boxed{
\begin{aligned}
\text{classical orientation}
&\quad\text{known}\\
\downarrow\\
\text{bare graded}
&\quad\text{insufficient}\\
\downarrow\\
\text{full mod-3 graded}
&\quad\text{still insufficient}\\
\downarrow\\
\text{first extension/power datum}
&\quad\text{sufficient for mod 9}\\
\downarrow\\
\text{finite Kummer window}
&\quad\text{works locally}\\
\downarrow\\
\text{general finite window}
&\quad\text{mathematical gate mostly closed}\\
\downarrow\\
\text{literature/newness}
&\quad\text{still decisive}\\
\downarrow\\
\text{mod 27 / higher obstruction}
&\quad\text{open}
\end{aligned}
}
\]

---

# 50. 최종 평가와 전망

현재 연구는 아직 완성된 새로운 theorem이라고 부를 단계는 아니다.

그러나 실패한 연구라고 평가할 단계도 아니다.

가장 중요한 성과는 세 가지다.

## 첫째
이미 알려진 것을 새 발견으로 주장하지 않도록 classical orientation, classification, filtration usage의 경계를 명확히 했다.

## 둘째
무엇이 정보적으로 부족한지를 no-go와 반례로 단계적으로 밝혔다.

\[
\text{graded}\not\Rightarrow\chi,
\]

\[
\text{bounded degree + bounded precision}\not\Rightarrow\chi.
\]

## 셋째
실제로 성공하는 첫 finite-window mechanism을 확보했다.

\[
\boxed{
G/P_3\to\chi\bmod9
}
\]

및

\[
\boxed{
P_{k+1}(A_k\rtimes U_k)=1
}
\]

이라는 구조적 factorization은 현재 연구의 가장 강한 구체적 성과다.

---

# 51. 가장 큰 위험

현재 가장 큰 위험은 계산 부족이 아니라 novelty duplication이다.

즉

> “우리가 만든 finite Kummer predicate가 사실 Serre/Labute의 기존 orientation characterization을 finite notation으로 다시 쓴 것뿐인가?”

를 반드시 해결해야 한다.

기존 theorem이

- infinite orientation을 먼저 주고,
- \(K_\theta\) 또는 Kummerian condition을 사용하고,
- quotient inheritance를 이용하는 것

에 머물고,

우리의 theorem이

\[
Q_k
\]

만을 input으로 하여

\[
\chi\bmod3^k
\]

를 constructively and naturally recognize한다면 그 차이는 중요하다.

---

# 52. 최종 결론

현재 연구를 가장 정확하게 한 문장으로 표현하면:

> **“Demuškin 군의 canonical orientation을 발견하는 연구”는 이미 알려진 결과이므로 종료되었지만, 그 orientation이 intrinsic Zassenhaus/Jennings–Lazard filtration의 유한 창 \(G/P_{k+1}\)에서 Kummer lifting obstruction을 통해 자연스럽게 factorization되는지, 그리고 그 과정에서 graded information만으로는 부족한 첫 extension datum이 무엇인지를 밝히는 연구는 여전히 열려 있다.**

현재 손에 쥔 가장 강한 구체적 결과는

\[
\boxed{
G/P_3\to\chi\bmod9
}
\]

의 PASS/LOCAL과

\[
\boxed{
P_{k+1}(A_k\rtimes U_k)=1
}
\]

에 의한 general finite crossed-cochain factorization이다.

반면 최종 논문의 생사를 결정할 문은

\[
\boxed{
\text{이 finite-window Kummer recognition이 기존 Serre/Labute/Kummerian quotient theorem의 단순 재서술인가?}
}
\]

이다.

이 문을 먼저 정확히 연다. 기존 결과와 동일하면 닫고, genuine new factorization이면 \(k=3\), \(n\to n+1\), inverse-limit까지 확장한다.

---

## 문헌 대조의 핵심 출처

- John P. Labute, *Classification of Demushkin Groups* — canonical orientation, uniqueness, standard presentations, q-invariant, descending q-central/graded structure.
- Ambrus Pál, Gereon Quick, *A_3-formality for Demushkin groups at odd primes* (arXiv:2601.07551v2) — q=3 higher cohomological/A_3 obstruction.
- Simone Blumer, Claudio Quadrelli, *Variations of Demushkin Groups that are not Absolute Galois Groups* (arXiv:2603.15464v2) — modern Kummerian/cyclotomic orientation, Zassenhaus/graded/Jennings structures and Demushkin variations.
- Pál–Quick, *A_3-formality for pro-2 Demushkin groups* (arXiv:2607.01028v2) — pro-2 methodological comparison; not the main p=3 novelty boundary.

---

## 기록 상태

작성일: **2026-09-21**

성격: **연구 중간 총정리 / authoritative continuity support**

현재 핵심 분류:

\[
\boxed{
\text{B2/}k=2=\text{PASS/LOCAL}
}
\]

\[
\boxed{
\text{B2 general finite-window novelty}=\text{OPEN/DECISIVE}
}
\]

\[
\boxed{
G/P_4\to\chi\bmod27=\text{OPEN/DECISIVE}
}
\]

\[
\boxed{
\text{overall publication-level novelty}=\text{OPEN/CONDITIONAL}
}
\]

이 문서는 기존 세부 연구기록을 대체하지 않으며, RESEARCH_MAP / CURRENT_STATE / 00_RESEARCH_LOG 및 각 stage document를 읽기 전에 연구 전체 흐름을 빠르게 복원하기 위한 중간 총정리이다.


---

# 53. 2026-09-26 — 중간 평가 업데이트: 첫 논문과 후속 연구의 역할을 분리해서 본 현재 평가

이번 중간 평가에서는 지금까지의 연구 기록과 현재 후속 연구의 상태를 **“실제로 수학적으로 무엇을 얻었는가”**와 **“논문으로서 무엇을 주장할 수 있는가”**를 분리해서 정리한다.

한 줄 요약:

> 첫 논문은 “무한한 군 전체를 보지 않고도, 정확히 정해진 유한한 Zassenhaus window 안에서 canonical orientation을 Kummer 조건으로 찾아낼 수 있다”는 인식 정리를 만든 것이고, 후속 연구는 그 window가 왜 필요한지, 얼마나 날카로운지, 그리고 \(q=p^f\) 변화에 따라 정보가 어디까지 보존되는지를 파고드는 방향이다.

다만 후속논문은 현재 아이디어와 결과는 상당히 좋아졌지만, 처음 작성된 sharp_finite_window.tex 자체는 아직 논문으로 제출할 상태가 아니다. 그 차이를 정확히 분리한다.

## 53.1 첫 논문의 핵심 기여

첫 논문의 핵심 정리는 현재 다음과 같이 정리된다.

\[
G=\langle x_1,x_2,x_3,x_4\mid x_1^3[x_1,x_2][x_3,x_4]=1\rangle
\]

에 대해 실제 Zassenhaus filtration을 사용하여

\[
Q_k=G/P_{3^{k-1}+1}
\]

라는 유한 quotient를 취하고,

\[
\rho:Q_k\to U_{1,k}=1+3\mathbf Z/3^k
\]

후보들과 finite Kummer lifting predicate

\[
\mathsf K_k(Q_k,\rho):
H^1(Q_k,\mathbf Z/3^k(\rho))
\longrightarrow H^1(Q_k,\mathbf F_3)
\]

의 surjectivity를 검사한다.

현재 U1–U5가 닫혔으므로, \(k\ge2\)에 대해

\[
\boxed{
\mathsf K_k(Q_k,\rho)
\iff
\rho=\chi_G\pmod{3^k}
}
\]

가 성립한다.

쉽게 말하면 기존 이론이

\[
G+\chi\Longrightarrow\text{Kummerian}
\]

이라는 방향이었다면, 이번 연구는

\[
Q_k+\text{arbitrary candidate }\rho+\mathsf K_k
\Longrightarrow
\rho=\chi\pmod{3^k}
\]

라는 방향으로 문제를 뒤집었다.

따라서 첫 논문의 정확한 표현은 **“canonical orientation을 발견했다”가 아니라 “canonical orientation을 finite information으로 recognition하는 theorem을 만들었다”**이다.

## 53.2 첫 논문의 수학적 구조 U1–U5

### U1 — 유한 window가 실제로 충분한 이유

후보 \(\rho\)와 crossed cocycle \(z\)를 합치면

\[
G\to A_k\rtimes U_{1,k}
\]

라는 affine representation을 만든다.

현재의 올바른 Zassenhaus 계산은

\[
P_n(A_k\rtimes U_1)
=
3^{e(n)}A_k\rtimes U_{e(n)+1},
\qquad e(n)=\lceil\log_3 n\rceil,
\]

따라서

\[
P_{3^{k-1}}\neq1,
\qquad
P_{3^{k-1}+1}=1.
\]

그러므로 relevant affine/Kummer information은 정확히

\[
Q_k=G/P_{3^{k-1}+1}
\]

에서 끝난다.

즉 “무한히 깊은 group structure가 필요하지 않다”는 것이 첫 번째 큰 결과다.

### U2 — 임의의 후보에 대해서도 factorization

canonical \(\chi\)에 대해서만 factorization을 보인 것이 아니다. 임의의 후보 \(\rho\)에 대해서도 crossed cocycle와 coefficient action이 corrected finite quotient를 통해 factorization한다.

따라서 정답을 미리 가정하지 않는 recognition theorem의 논리적 기반이 된다.

### U3 — cohomology와 one-relator Fox obstruction의 연결

crossed cocycle 조건은 one-relator presentation에서

\[
\sum_iF_i(\rho)z(x_i)=0
\]

형태의 식으로 바뀌고, Kummer lifting surjectivity와 결합하여 twisted Fox row vanishing과 동치가 된다.

초기의 Nakayama식 설명은 valuation induction으로 교정되었다. 따라서 이것은 단순한 brute-force search가 아니라

\[
\text{cohomological lifting property}
\Longleftrightarrow
\text{one-relator Fox obstruction}
\]

이라는 연결이다.

### U4 — \(k=2\) base selector

mod \(9\)에서는

\[
\rho_2=(1,4,1,1)
\]

이 유일한 후보가 된다.

이는 이후 U5 induction의 시작점이다.

### U5 — 모든 \(k\)에서의 intrinsic uniqueness

두 후보가 같은 이전 단계로 내려가면

\[
\rho_k'=\rho_k(1+3^{k-1}\nu)
\]

로 쓸 수 있고 coefficient-extension variation formula가

\[
\delta_{\rho_k'}-\delta_{\rho_k}
=
\iota_{k-1}\circ(\nu\smile-)
\]

를 준다.

PD² duality에 의한 socle-injectivity와 Demuškin cup-product nondegeneracy를 결합하면 두 후보가 모두 Kummerian일 경우

\[
\nu=0
\]

이므로 후보는 유일하다.

따라서

\[
\text{mod }9
\to
\text{mod }27
\to
\text{mod }81
\to\cdots
\]

를 매 단계 brute force할 필요 없이 하나의 구조적 uniqueness theorem으로 닫는다.

## 53.3 첫 논문의 진짜 의미

기존에 알려진 것은 canonical orientation의 존재·유일성, Kummerian characterization, Demuškin classification 등이다. 이것들은 신규 발견으로 주장하지 않는다.

이번 연구의 살아 있는 주장은

\[
\boxed{
Q_k=G/P_{3^{k-1}+1}
\quad+\quad
\text{q-blind finite Kummer predicate}
\Longrightarrow
\chi\bmod3^k
}
\]

라는 finite-window recognition 구조다.

현재 이 theorem 자체의 publication-level novelty는 여전히 문헌 Gate가 결정한다. 즉 “이미 알려진 finite-coefficient quotient inheritance/Kummerian theorem의 즉각적인 corollary 또는 동치 재서술인가?”를 line-by-line으로 닫아야 한다.

## 53.4 후속 연구가 묻는 질문

첫 논문이

\[
Q_k=G/P_{3^{k-1}+1}
\]

이면 충분하다고 했다면, 자연스러운 다음 질문은

> 정말 이만큼 깊어야 하는가?

이다.

또 일반 Demuškin relation의

\[
q=p^f
\]

변화에 따라 finite window가 q-information을 언제까지 기억하는지도 묻는다.

따라서 후속 연구의 중심은

\[
\boxed{\text{Boundary / Sharpness / Information loss}}
\]

이다.

첫 논문이 sufficiency를 닫았다면 후속 연구는 lower bound/sharpness와 information boundary를 붙이는 방향이다.

## 53.5 현재 확보한 sharpness의 의미

현재 후속 연구에서 확보한 중요한 강화는 **affine category에서의 sharpness**다.

특히 odd \(p\)에서 실제로 surjective한 affine orientation character

\[
\rho(G)=U_{1,k}
\]

를 허용해도

\[
\boxed{n_{\mathrm{aff}}(k)=p^{k-1}+1}
\]

이라는 depth boundary가 sharp하다.

즉 단순한 trivial/퇴화 representation만으로 생기는 인공적인 현상이 아니라, coefficient action이 실제로 \(U_{1,k}\) 전체를 움직이는 affine representation에서도 같은 경계가 남는다.

단, 이 결과는 정확히 **affine category에서 sharp**하다는 뜻이다.

\[
\boxed{
\text{affine sharpness}
\neq
\text{absolute intrinsic minimality}
}
\]

전혀 다른 carrier/invariant category가 더 얕은 quotient에서 orientation을 recognition할 가능성까지 배제한 것은 아니다. 따라서 absolute minimality는 아직 OPEN이다.

## 53.6 \(q=p^f\)와 information collapse

후속 연구에서 중요한 또 하나의 현상은 finite precision에서 q-information이 사라지는 구간이다.

\[
\chi_f(x_2)=(1-p^f)^{-1}
\]

이고 \(f\ge k\)이면 mod \(p^k\)에서

\[
p^f\equiv0\pmod{p^k},
\]

따라서

\[
\chi_f\bmod p^k
=
\chi_\infty\bmod p^k.
\]

즉 finite window가 모든 q-information을 기억하는 것은 아니다.

이것은

> finite filtered data가 canonical orientation의 어느 부분까지 기억할 수 있는가?

라는 더 큰 정보경계 문제로 연결된다.

## 53.7 후속 draft의 치명적인 교정 사항

처음 작성된 sharp_finite_window.tex에는 crossed-cocycle commutator 공식에

\[
\rho(a)^{-1}\rho(b)^{-1}
\]

prefactor가 빠져 있었다.

정확한 공식은

\[
z([a,b])=
\rho(a)^{-1}\rho(b)^{-1}
\bigl((1-\rho(b))z(a)+(\rho(a)-1)z(b)\bigr).
\]

따라서 당시 draft의 all-\(k\) selector 계산은 잘못되었고, 정상적인 zero condition은

\[
\boxed{\rho(x_2)=(1-p^f)^{-1}\pmod{p^k}}
\]

이다.

예를 들어

\[
p=3,\ f=1,\ k=3
\]

이면 canonical value는

\[
(1-3)^{-1}=13\pmod{27}
\]

이고, 잘못된 draft formula는 \(4\pmod{27}\)을 주었다.

따라서 기존 sharp_finite_window.tex는 그대로는

\[
\boxed{\text{FAIL/CLOSED as written}}
\]

이다.

이것은 연구 아이디어 전체의 붕괴가 아니라 중심 계산식 하나의 오류가 후속 계산 전체에 전파된 경우다. 현재 원칙은 이 오류를 인정한 상태에서 corrected finite-window mechanism과 sharpness 결과를 별도로 보존하는 것이다.

## 53.8 “수학적 성과”와 “논문 상태”의 분리

### 첫 논문

수학적 상태:

\[
\boxed{\text{U1--U5/theorem chain = PASS/CLOSED}}
\]

원고 상태:

publication preparation 단계. 2026-09-25 corrected manuscript build도 독립 검증되었고, 현재 publication-working version이 있다.

다만 publication-level novelty는 여전히

\[
\boxed{\text{OPEN/CONDITIONAL}}
\]

이다.

### 후속 논문

연구 상태:

\[
\boxed{\text{좋은 수학적 결과들이 이미 확보된 연구 프로그램}}
\]

원고 상태:

\[
\boxed{\text{아직 제출 불가}}
\]

특히 다음은 살아 있는 뼈대다.

- general \(p^f\) family
- finite-window information boundary
- q-collapse
- affine factorization threshold
- odd-\(p\) surjective-affine sharpness
- affine-category minimality

반대로 다음은 폐기/수정 대상이다.

- 잘못된 crossed-cocycle commutator formula
- 그 formula에 의존한 기존 all-\(k\) selector 계산
- 잘못된 Newton recurrence
- absolute minimality를 의미하는 과도한 표현

## 53.9 두 논문의 역할

첫 논문:

\[
\boxed{\text{Recognition / Sufficiency}}
\]

후속 연구:

\[
\boxed{\text{Sharpness / Boundary / Information loss}}
\]

두 논문을 이어 놓으면

\[
\text{Full infinite group}
\to
\text{finite Zassenhaus window}
\to
\text{Kummer selector}
\to
\chi\bmod p^k
\]

그리고 후속 연구에서

\[
\text{How small can the window be?}
\to
\text{affine sharpness}
\to
\text{surjective-affine sharpness}
\to
q\text{-information collapse}
\]

라는 구조가 생긴다.

## 53.10 현재 연구 전체의 가장 정확한 표현

> **Classical theory:** canonical orientation exists and is Kummerian.
>
> **Paper 1:** a specific finite Zassenhaus window already recognizes it by a q-blind Kummer lifting predicate.
>
> **Follow-up:** the finite window has a sharp affine boundary, even for surjective affine characters in odd characteristic, while deeper q-information eventually collapses at finite precision.

그리고 아직 주장하지 않는 것은

\[
\boxed{
\text{“따라서 모든 가능한 intrinsic carrier에서 절대 최소다.”}
}
\]

이다.

현재까지의 가장 정확한 연구 분류는:

\[
\boxed{
\text{Paper 1: theorem-level mathematics CLOSED; publication novelty OPEN/CONDITIONAL}
}
\]

\[
\boxed{
\text{Follow-up: affine sharpness PASS/CLOSED; absolute minimality OPEN; manuscript FAIL/CLOSED as written}
}
\]

이 기록은 2026-09-26 현재의 중간 평가로 추가한다. 기존 2026-09-21 중간 총정리의 역사적 기록은 수정하지 않고, 이후의 authoritative research map/current state/log와 충돌할 경우 더 최신 기록을 따른다.

작성일: **2026-09-26**
