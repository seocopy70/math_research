# 필터 관계 제트로부터 Demuškin pro-3 군의 3진 방향성 복원

**논문 초안 — 2026-09-19**

## 초록

본 논문에서는 rank-four Demuškin pro-\(3\) 군의 canonical orientation character
\[
\chi:G\to\mathbf Z_3^\times
\]
가 filtered 및 graded relation data로부터 어느 정도까지 복원될 수 있는지를 연구한다. 표준 presentation
\[
G_3=\langle x_1,x_2,x_3,x_4\mid x_1^3[x_1,x_2][x_3,x_4]=1\rangle
\]
에서 quadratic initial relation
\[
R_2=[X_1,X_2]+[X_3,X_4]
\]
만으로는 \(q=3\)과 \(q=\infty\)의 orientation을 구별하기에 충분한 정보가 남아 있지 않다. 최초의 유효한 보강은 projective degree-\((2,3)\) relation jet
\[
J_3=[(R_2,P_3)],\qquad P_3=X_1^{[3]}
\]
이다. 이 jet으로부터 자연스러운 degree-one crossed-derivation functional
\[
\Theta_J(\lambda)(f)=f(P_3)+(\lambda\wedge f)(R_2)
\]
을 얻는다. 이 functional의 zero set은 관련된 presentation, lift, relator-gauge 및 normalization 변화에 대해 intrinsic하며, \(q=3\)에서는 유일한 zero가 \(\lambda=e_2^*\)이다. 따라서 \(J_3\)는 canonical orientation을 modulo \(9\)까지 복원한다.

이 construction이 실제로 보존하는 정보를 더 정확히 분석하면, raw jet 자체는 degree-one evaluation observable 전체가 정하는 자연스러운 quotient category에서 minimal하지 않다. 그 coarsest quotient는
\[
\overline J_3=[(R_2,p(P_3))]
\]
이며,
\[
p:L_3^{res}(V)\to L_3^{res}(V)/[V,L_2(V)]\cong V^{(1)}
\]
로 정의된다. 이 quotient는 모든 degree-one evaluation family를 보존하는 functorial quotient들 가운데 terminal, 즉 coarsest carrier이다.

full \(3\)-adic character에 대해서는 compatible filtered relation-jet tower \(J_n\)으로부터 유일한 finite-level character
\[
\chi_n:G\to(\mathbf Z/3^n)^\times,
\qquad
\chi_n(x_2)=(-2)^{-1}\pmod{3^n}
\]
를 얻고, inverse limit를 통해
\[
\chi(x_2)=(1-3)^{-1}
\]
을 얻는다. 동시에
\[
G_{3^s}=\langle x_i\mid x_1^{3^s}[x_1,x_2][x_3,x_4]\rangle
\]
라는 family는 filtration degree와 \(3\)-adic coefficient precision을 모두 유한하게 제한한 universal carrier로는 full orientation을 복원할 수 없음을 보여준다. \(q\)-dependent power term이 degree \(3^s\)에서 처음 나타나기 때문이다. 따라서 본 연구의 결과는 하나의 유한한 \(\mathbf F_3\)-jet이 보편적으로 전체 \(3\)-adic character를 담는다는 주장이 아니라, orientation recovery에 필요한 정보의 계층과 그 한계를 명확히 제시한다.

본 논문은 다음과 같은 일반적 reconstruction pattern을 분리해낸다. 어떤 invariant가 associated graded object에서는 보이지 않을 때, 숨은 parameter가 leading relation과 처음 결합하는 filtered relation jet을 보존하고, 관련 observable이 보지 못하는 정보는 정확히 quotient하는 것이다.

---

## 1. 서론

Filtered algebraic problem에서 반복해서 나타나는 어려움 중 하나는 associated graded object로 넘어가는 과정에서 원래 대상의 invariant를 복원하는 데 필요한 extension information이 사라질 수 있다는 점이다. Graded object는 leading term을 기록하지만, 실제 relation 내부에서 서로 다른 filtered piece가 어떻게 결합되어 있는지는 반드시 보존하지 않는다.

이 문제는 Demuškin pro-\(p\) 군에서 자연스럽게 나타난다. 이들의 associated graded restricted Lie algebra는 defining relation의 quadratic initial form에 의해 통제되지만, canonical orientation character는 본질적으로 \(p\)-adic인 invariant이다. 본 논문이 다루는 질문은 다음과 같다.

> **canonical orientation character를 복원하기 위해 필요한 filtered relation information은 정확히 어느 정도인가?**

rank-four pro-\(3\) model에서 얻은 답은 세 층으로 구성된다.

첫째, bare quadratic graded relation만으로는 충분하지 않다. \(q=3\)과 \(q=\infty\) presentation은 동일한 quadratic initial relation
\[
R_2=[X_1,X_2]+[X_3,X_4]
\]
을 가지지만, orientation은 이미 modulo \(9\)에서 다르다.

둘째, 사라진 정보는 quadratic relation과 degree-three restricted-power component 사이의 결합에 나타난다. 이것이 projective relation jet
\[
J_3=[(R_2,P_3)]
\]
와 intrinsic recovery equation
\[
f(P_3)+(\lambda\wedge f)(R_2)=0
\]
을 준다. 표준 \(q=3\) presentation에서는 유일한 해가
\[
\lambda=e_2^*
\]
이므로
\[
\chi(x_1),\chi(x_2),\chi(x_3),\chi(x_4)
\equiv(1,4,1,1)\pmod9.
\]

셋째, full \(3\)-adic 문제는 논리적으로 서로 다른 두 질문으로 나뉜다. Compatible finite-level filtered relation jets의 sequence는 모든 \(\chi\bmod3^n\)을 결정하고, 따라서 inverse limit로 full character를 결정한다. 그러나 \(q=3^s\) 전체 family에 대해 bounded-degree와 finite-precision을 동시에 갖는 universal carrier로는 이를 수행할 수 없다. 반면 fixed \(q=3\)에서 exact \(\mathbf Z_3\)-coefficients는 무한히 많은 \(3\)-adic digit을 포함하므로 bounded filtration degree에서도 full character를 복원할 수 있다.

따라서 본 논문의 목적은 모든 가능한 category에서 absolute “minimal jet”을 주장하는 것이 아니다. 대신 자연스러운 observable category에서 정확한 coarsest carrier를 식별하고, positive와 negative information result를 함께 확립하는 것이다.

---

## 2. 모형과 기본 convention

다음을 고정한다.
\[
G_3=
\left\langle
x_1,x_2,x_3,x_4
\mid
r=x_1^3[x_1,x_2][x_3,x_4]=1
\right\rangle
\]
이며 group commutator는
\[
[x,y]=x^{-1}y^{-1}xy
\]
이다.

이에 대응하는 \(q=\infty\) model은
\[
G_\infty=
\left\langle
x_1,x_2,x_3,x_4
\mid
[x_1,x_2][x_3,x_4]=1
\right\rangle
\]
이다.

\(V\)를 degree-one \(\mathbf F_3\)-space라 하자. 표준 좌표에서
\[
V=\langle e_1,e_2,e_3,e_4\rangle.
\]

Quadratic initial relation은
\[
R_2=e_1\wedge e_2+e_3\wedge e_4.
\]

\(q=3\)에서는 동일한 filtered relation의 degree-three restricted-power contribution이
\[
P_3=X_1^{[3]}
\]
이고, \(q=\infty\)에서는 해당 degree-three component가 0이다.

Canonical orientation은 표준 Demuškin crossed-derivation characterization에서 유일하게 결정되는 orientation이다. Frozen \(q=3\) normal form에서는
\[
\chi(x_1)=\chi(x_3)=\chi(x_4)=1,
\qquad
\chi(x_2)=(1-3)^{-1}.
\]

이하 모든 명제는 위의 frozen commutator convention을 사용한다.

---

## 3. Quadratic graded level에서의 정보 손실

첫 번째 obstruction은 즉시 나타난다.

\(G_3\)와 \(G_\infty\) 모두 defining relation의 degree-two initial term은
\[
R_2=[X_1,X_2]+[X_3,X_4]
\]
로 동일하다.

\(q=3\) relation의 \(x_1^3\) term은 Zassenhaus degree \(3\)에서 나타나므로 quadratic initial form에는 포함되지 않는다.

그럼에도
\[
\chi_3(x_2)=4\pmod9,
\qquad
\chi_\infty(x_2)=1\pmod9.
\]

따라서 bare quadratic graded relation만으로는 \(\chi\bmod9\)조차 결정할 수 없다.

이는 특정한 하나의 formula가 실패했다는 뜻이 아니다. 동일한 quadratic relation을 가지면서 서로 다른 orientation character를 갖는 두 group이 존재한다는 information-level obstruction이다.

따라서 필요한 missing datum은 \(R_2\)의 또 다른 함수가 아니라, degree-three filtered relation component가 \(R_2\)와 어떻게 결합되는지를 보존하는 정보여야 한다.

---

## 4. Projective degree-\((2,3)\) relation jet

### 4.1 정의

Minimal free pro-\(3\) presentation에서 filtered defining relation을 degree 3까지
\[
r=(R_2,P_3)+O(4)
\]
로 쓴다.

관련된 object는 projective relation jet
\[
J_3=[(R_2,P_3)]
\]
이다.

Projectivization은 본질적이다. Relation generator를 바꾸면 두 component가 공통 unit만큼 곱해질 수 있고, relator conjugation은 degree-three bracket term을 추가할 수 있기 때문이다.

\(\lambda,f\in V^*\)에 대해
\[
\Theta_J(\lambda)(f)
=
f(P_3)+(\lambda\wedge f)(R_2)
\]
를 정의한다.

Canonical orientation modulo \(9\)는 이 functional의 unique zero로 encoding된다.

### 4.2 명시적 계산

\[
\lambda=a_1e_1^*+a_2e_2^*+a_3e_3^*+a_4e_4^*
\]
및
\[
f=f_1e_1^*+f_2e_2^*+f_3e_3^*+f_4e_4^*
\]
로 쓴다.

\[
R_2=e_1\wedge e_2+e_3\wedge e_4,
\qquad
P_3=e_1^{[3]}
\]
이면
\[
\Theta_J(\lambda)(f)
=
(1-a_2)f_1+a_1f_2-a_4f_3+a_3f_4.
\]

이 식이 모든 \(f\)에 대해 0이어야 하므로
\[
a_1=a_3=a_4=0,
\qquad
a_2=1.
\]

따라서
\[
\boxed{\lambda_\chi=e_2^*.}
\]

\[
\rho=1+3\lambda\pmod9
\]
로 쓰면
\[
\boxed{
\rho(x_1),\rho(x_2),\rho(x_3),\rho(x_4)
=(1,4,1,1)\pmod9.
}
\]

따라서 degree-\((2,3)\) relation jet은
\[
\boxed{\chi\pmod9}
\]
를 복원한다.

\(q=\infty\)에서는 \(P_3=0\)이고 \(R_2\)의 nondegeneracy로부터 unique zero가
\[
\lambda=0
\]
이다. 따라서 동일한 carrier가 definition에 \(q\)를 직접 삽입하지 않고도 \(q=3\)과 \(q=\infty\)를 구별한다.

---

## 5. Intrinsicity: presentation, lift 및 gauge 변화

선택한 defining relator 자체는 canonical하지 않다. 따라서 중요한 질문은 허용된 변화 아래 recovery zero set이 보존되는가이다.

\(G\)에서 identity를 유도하는 free automorphism이 degree-two correction
\[
\alpha(X_i)=X_i+Q_i+O(3)
\]
를 가진다고 하자. Minimality와 one-dimensional quadratic initial relation으로부터
\[
Q_i=c_iR_2
\]
이다.

Degree 3에서 relation jet의 induced change는
\[
(R_2,P_3)
\longmapsto
(uR_2,uP_3+[v,R_2])
\]
꼴이며, \(u\)는 unit이고 \(v\in V\)이다.

모든 degree-one functional \(f\)에 대해
\[
f([v,R_2])=0.
\]

따라서
\[
\Theta'(\lambda)=u\,\Theta(\lambda).
\]

Scalar \(u\)는 zero set을 바꾸지 않는다. 따라서 계산에서 사용한 degree-\((2,3)\) presentation/lift/relator gauge 아래에서 recovered covector는 invariant이다.

### Proposition 5.1

표준 minimal one-relator pro-\(3\) presentation 가정과 frozen filtration convention 아래에서
\[
Z(\Theta_J)
=
\{\lambda\in V^*:\Theta_J(\lambda)=0\}
\]
는 degree-\((2,3)\) presentation 및 relator gauge에 대해 invariant이다.

이 명제는 recovery observable에 관한 것이다. **전체 relation module의 선택된 generator 자체가 canonical하다는 뜻은 아니다.**

Automorphism naturality는 \(V\), exterior power 및 동일한 bracket gauge cancellation에 유도되는 작용의 functoriality로부터 따른다.

---

## 6. Coarsest natural carrier

Raw \(J_3\)는 recovery functional이 실제로 사용하는 것보다 많은 정보를 담고 있다.

다음의 canonical quotient가 있다.
\[
p:
L_3^{res}(V)
\longrightarrow
L_3^{res}(V)/[V,L_2(V)].
\]

Characteristic \(3\)에서 이 quotient는 restricted-cube component
\[
V^{(1)}
\]
이다.

모든 degree-one \(f\)에 대해
\[
f(P_3)=f(p(P_3)),
\]
그리고
\[
f([v,R_2])=0.
\]

따라서
\[
\boxed{
\overline J_3=[(R_2,p(P_3))]
\subset
\mathbf P\bigl(\Lambda^2V\oplus V^{(1)}\bigr).
}
\]

표준 examples에서는
\[
\overline J_3(3)
=
[(R_2,e_1^{(1)})],
\qquad
\overline J_3(\infty)
=
[(R_2,0)].
\]

### Theorem 6.1 — Coarsest quotient theorem

Projective degree-\((2,3)\) relation jet의 functorial quotient 가운데 모든 degree-one observable
\[
\Theta_{R,P}(\lambda)(f)
=
f(P)+(\lambda\wedge f)(R)
\]
를 보존하는 category를 생각하자.

그러면 모든 그러한 quotient는
\[
J_3\twoheadrightarrow\overline J_3
\]
를 통해 unique하게 factor한다.

따라서 \(\overline J_3\)는 이 category에서 terminal, 동치로 coarsest admissible quotient이다.

#### 증명

두 jet의 \(p(P)\)가 다르면
\[
f(p(P)-p(P'))\neq0
\]
인 \(f\)를 선택할 수 있다. 그러면 \(\lambda=0\)에서 이미 대응하는 observable들이 달라지므로 모든 observable을 보존하는 quotient는 이들을 identify할 수 없다.

마찬가지로 서로 다른 projective quadratic relation line은 nondegenerate pairing
\[
(\lambda,f)\mapsto(\lambda\wedge f)(R)
\]
으로 검출된다.

따라서 admissible quotient는 반드시 \([R]\)과 \(p(P)\)를 보존해야 한다. 반대로 bracket component는 degree-one evaluation에 의해 소거되므로 전체 observable family는 이 두 부분을 통해 factor한다. 따라서 \(\overline J_3\)를 통한 factorization은 unique하다.

\(\square\)

이는 raw \(J_3\) 자체가 categorical minimal이라는 더 강한 주장이 잘못되었음을 바로잡는다.

이 결과가 의미 있는 이유는 이 carrier가 이미 복원된 orientation covector를 단순히 저장하는 것이 아니라 relation jet의 canonical algebraic quotient로 얻어지기 때문이다.

---

## 7. Full 3-adic reconstruction

Mod-\(9\) 결과는 첫 번째 nontrivial finite-level recovery이다. Full character를 복원하기 위해 compatible filtered relation-jet tower
\[
(J_n)_{n\ge2}
\]
를 생각한다. 여기서 \(J_n\)은 이미 확인된 projective/gauge ambiguity를 quotient한 뒤 \(3^n\) modulo crossed-derivation calculation에 필요한 filtered relation information을 보존한다.

후보
\[
\rho:G\to(\mathbf Z/3^n)^\times
\]
에 대해 crossed-derivation condition
\[
D(gh)=D(g)+\rho(g)D(h)
\]
을 filtered relation에 평가하면 coefficient functional
\[
\mathcal C_n(J_n,\rho)
\]
를 얻는다.

\[
\Phi_n(J_n)
=
\{\rho:\mathcal C_n(J_n,\rho)=0\}
\]
로 둔다.

Frozen \(q=3\) relation에서는 coefficient equations가
\[
\rho_n(x_1)=\rho_n(x_3)=\rho_n(x_4)=1
\]
및
\[
1+2\rho_n(x_2)=0\pmod{3^n}
\]
을 강제한다.

\(2\)는 modulo \(3^n\)에서 unit이므로
\[
\boxed{
\rho_n(x_2)=(-2)^{-1}=(1-3)^{-1}\pmod{3^n}.
}
\]

따라서
\[
\Phi_n(J_n)=\{\chi_n\}.
\]

Reduction은 compatible하다:
\[
\chi_{n+1}\equiv\chi_n\pmod{3^n}.
\]

또한
\[
\mathbf Z_3^\times
\cong
\varprojlim_n(\mathbf Z/3^n)^\times
\]
이므로 compatible family는 unique한
\[
\boxed{
\chi:G\to\mathbf Z_3^\times
}
\]
를 결정한다.

특히
\[
\chi(x_2)
=
-\frac12
=
(1-3)^{-1}
\]
이고
\[
\chi(x_2)\equiv4\pmod9,\quad
13\pmod{27},\quad
40\pmod{81},\quad
121\pmod{243},\ldots
\]
이다.

### Theorem 7.1 — Finite-level factorization 및 inverse limit

Frozen rank-four \(q=3\) Demuškin presentation에서 compatible projective filtered relation-jet tower는 finite-level crossed-derivation coefficient equation을 통해
\[
\chi_n:G\to(\mathbf Z/3^n)^\times
\]
를 유일하게 결정하며, compatible family \((\chi_n)_n\)는 full canonical orientation
\[
\chi:G\to\mathbf Z_3^\times
\]
를 결정한다.

이 정리는 mod-\(9\) jet \(J_3\) 하나만으로 모든 higher digit이 결정된다는 것을 주장하지 않는다.

---

## 8. 날카로운 불가능성 결과

앞선 positive theorem에서 “finite information”의 의미를 정확히 구분할 필요가 있다.

다음 family를 생각한다.
\[
G_{3^s}
=
\left\langle
x_1,x_2,x_3,x_4
\mid
x_1^{3^s}[x_1,x_2][x_3,x_4]=1
\right\rangle
\]
및 \(G_\infty\).

모든 member는 동일한 quadratic initial relation
\[
R_2=[X_1,X_2]+[X_3,X_4]
\]
을 가진다.

그들의 orientation은
\[
\chi_{3^s}(x_2)=(1-3^s)^{-1},
\qquad
\chi_\infty(x_2)=1
\]
이다.

그런데 power term
\[
x_1^{3^s}
\]
은 Zassenhaus degree \(3^s\)에서 처음 나타난다.

Degree bound \(d\)를 고정하고
\[
3^s>d
\]
인 \(s\)를 택한다.

그러면 bounded-degree filtered data는 \(q\)-dependent power term을 볼 수 없지만 full orientation은 서로 다르다.

Coefficient precision도 modulo \(3^N\)으로 유한하게 제한한다면
\[
s\ge N
\]
을 택할 수 있고,
\[
(1-3^s)^{-1}\equiv1\pmod{3^N}
\]
이지만 full \(3\)-adic unit은 서로 다르다.

### Theorem 8.1 — Finite-information obstruction

고정된 finite Zassenhaus-degree bound와 고정된 finite \(3\)-adic coefficient precision을 동시에 갖는 carrier로부터 \(q=3^s\) family 전체의 full orientation을 복원하는 universal reconstruction procedure는 존재하지 않는다.

이는 특정 candidate construction의 실패가 아니라 information obstruction이다.

Fixed \(q=3\) exact result와 모순되지 않는다. Exact \(\mathbf Z_3\)-coefficients는 무한히 많은 \(3\)-adic digit을 포함하므로 finite-information carrier가 아니기 때문이다.

---

## 9. Characteristic-zero 경계

Mod-\(3\) compressed carrier는 다음과 같은 유혹적인 대체를 제안한다.
\[
L_3^{res}(V)/[V,L_2(V)]
\cong V^{(1)}
\]
에서 \(\mathbf F_3\) 대신 \(\mathbf Z_3\)를 넣는 것이다.

그러나 이는 정당하지 않다.

Restricted Lie algebra는 characteristic-\(p\) 구조이다. 따라서 characteristic-three quotient를 단순히 scalar extension하여 “\(\mathbf Z_3\) 위의 restricted Lie algebra”를 자동으로 얻을 수 없다.

따라서 exact full-\(\chi\) construction은 restricted-Lie quotient를 형식적으로 lift하는 방식이 아니라 filtered relation/augmentation 및 coefficient-evaluation framework로 정식화되어야 한다.

Crossed-derivation evaluation family
\[
\mathcal C_n
\]
이 독립적으로 고정되어 있다면 exact evaluation quotient를 정의할 수 있다. 그러나
\[
[(R,p(P))]
\]
와 직접 대응하는 구체적이고 non-tautological한 finite exact characteristic-zero carrier는 아직 얻지 못했다.

이는 빠뜨린 계산이 아니라 현재 방법의 실제 경계이다.

---

## 10. 결과가 확립하는 것

결과는 다음 information hierarchy로 요약할 수 있다.

\[
\boxed{
\begin{array}{ccl}
\text{bare quadratic graded relation}
&\Longrightarrow&
\text{orientation information lost}
\\[2mm]
\downarrow && \\
\text{projective degree-(2,3) relation jet}
&\Longrightarrow&
\chi\bmod9
\\[2mm]
\downarrow && \\
\text{coarsest natural quotient }[(R,p(P))]
&\Longrightarrow&
\text{same recovery observables}
\\[2mm]
\downarrow && \\
\text{compatible finite-level filtered tower}
&\Longrightarrow&
\chi\bmod3^n\ \forall n
\\[2mm]
\downarrow && \\
\text{inverse limit}
&\Longrightarrow&
\chi:G\to\mathbf Z_3^\times.
\end{array}
}
\]

대응하는 negative boundary는
\[
\boxed{
\text{bounded degree + finite precision}
\not\Longrightarrow
\text{universal full }3\text{-adic orientation}.
}
\]

이 구분은 필수적이다. 다음 세 가지 서로 다른 주장이 혼동되는 것을 막아준다.

1. modulo \(9\) recovery;
2. full compatible tower로부터의 recovery;
3. 하나의 bounded finite-information carrier로부터 full character를 recovery.

현재 설정에서 처음 두 가지가 확립되며, 세 번째는 universal finite-information setting에서 obstruction을 받는다.

---

## 11. 더 넓은 reconstruction principle과의 관계

계산 결과는 filtered algebraic reconstruction에 대한 다음과 같은 일반적 pattern을 시사한다.

어떤 object \(X\)가 filtered relation
\[
r=r_d+r_{d+1}+\cdots
\]
을 가지고 있고 invariant \(I(X)\)가 leading graded data \(r_d\)만으로는 결정되지 않는다고 하자.

전체 graded calculation의 차수를 무작정 올리는 대신 다음을 묻는다.

1. 숨은 parameter가 최초로 등장하는 filtration degree는 어디인가?
2. 그것이 동일한 filtered relation의 component로 들어오는가?
3. 그 component를 평가하는 observable은 무엇인가?
4. 관련 observable 모두가 annihilate하는 higher-jet 정보는 무엇인가?
5. 모든 observable을 보존하는 coarsest quotient는 무엇인가?

본 연구에서는
\[
r_2=R_2,
\qquad
r_3=P_3
\]
이고 relevant observable은 degree-one crossed-derivation evaluation
\[
f(P_3)+(\lambda\wedge f)(R_2)
\]
이다.

따라서 얻어지는 carrier는 전체 degree-three Lie component가 아니라 observable quotient
\[
[(R_2,p(P_3))]
\]
이다.

이로부터 다음과 같은 연구 관점을 제안할 수 있다.

> **Filtered invariant recovery를 observability problem으로 다룰 수 있다. 즉 숨은 invariant가 처음으로 보이는 relation jet을 식별하고, recovery observable이 annihilate하는 정보를 quotient하는 것이다.**

본 논문은 이 원리를 구체적인 Demuškin setting에서 확립한다. 더 넓은 filtered object class에서의 타당성은 후속 연구 과제이다.

---

## 12. 한계와 열린 방향

다음과 같은 더 강한 명제는 의도적으로 주장하지 않는다.

### 12.1 Absolute minimality

\(\overline J_3\)가 모든 conceivable construction 가운데 가장 작은 carrier라는 정리는 없다. 그러한 주장을 위해서는 더 큰 carrier category를 독립적으로 정당화해야 한다.

현재 증명된 것은 full degree-one evaluation family를 보존하는 natural degree-\((2,3)\) relation-jet quotient category 안에서의 coarsest-quotient property이다.

### 12.2 Universal exact finite compression

Fixed \(q=3\) exact relation/evaluation data는 full character를 결정하지만, \(\overline J_3\)와 유사한 concrete finite characteristic-zero carrier는 아직 식별되지 않았다.

### 12.3 Higher rank와 general \(q\)

현재 증명은 frozen rank-four \(q=3\) normal form과 comparison family \(q=3^s\)에 대해 이루어졌다. 임의의 rank와 arbitrary \(q\)에 대한 general theorem은 open이다.

### 12.4 Other filtrations

논증은 여기서 사용한 Zassenhaus/restricted-power filtration 구조에 의존한다. 다른 filtration에서도 analogous first-informative jet이 존재하는지는 open이다.

---

## 13. 결론

핵심 결과는 하나의 작은 graded object가 마치 마법처럼 full \(3\)-adic orientation을 담고 있다는 것이 아니다.

오히려 본 연구는 orientation information이 정확히 어디서 사라지고, 어떤 filtered relation information이 그것을 복원하는지를 식별한다.

Rank-four Demuškin pro-\(3\) 군에서는

\[
\boxed{
\text{quadratic graded data는 불충분하다;}
}
\]

\[
\boxed{
\text{projective degree-(2,3) relation jet은 }\chi\bmod9\text{를 복원한다;}
}
\]

\[
\boxed{
\text{compatible filtered relation-jet tower는 full }\chi\text{를 복원한다;}
}
\]

그리고
\[
\boxed{
\text{universal bounded-degree finite-information carrier로는 full character를 복원할 수 없다.}
}
\]

이와 함께 categorical result는 raw degree-\((2,3)\) jet에 불필요한 정보가 있음을 보여준다. Degree-three layer에서 degree-one evaluation에 보이지 않는 bracket subspace를 quotient하면 coarsest natural carrier
\[
\boxed{\overline J_3=[(R,p(P))]}
\]
를 얻는다.

보다 넓은 방법론적 메시지는 다음과 같이 정확히 표현할 수 있다.

\[
\boxed{
\text{Graded data가 invariant를 잃는다면, hidden parameter가 leading relation과 결합하는 최초의 filtered relation jet을 조사하라.}
}
\]

이 모형에서는 이 원리가 겉보기에는 보이지 않는 \(3\)-adic orientation을 명시적으로 복원 가능한 observable로 바꾸며, 동시에 bounded finite data가 더 이상 충분할 수 없는 information-theoretic boundary도 밝혀준다.

---

## 부록 A. 핵심 공식

### A.1 Relation

\[
r=x_1^3[x_1,x_2][x_3,x_4].
\]

### A.2 Quadratic component

\[
R_2=[X_1,X_2]+[X_3,X_4].
\]

### A.3 Degree-three component

\[
P_3=X_1^{[3]}.
\]

### A.4 Recovery functional

\[
\Theta_J(\lambda)(f)
=
f(P_3)+(\lambda\wedge f)(R_2).
\]

### A.5 Coordinate form

\[
\Theta_J(\lambda)(f)
=
(1-a_2)f_1+a_1f_2-a_4f_3+a_3f_4.
\]

### A.6 Recovered mod-\(9\) orientation

\[
\lambda_\chi=e_2^*,
\qquad
\chi\equiv(1,4,1,1)\pmod9.
\]

### A.7 Gauge

\[
(R,P)\mapsto(uR,uP+[v,R]).
\]

### A.8 Coarsest carrier

\[
\overline J_3=[(R,p(P))].
\]

### A.9 Finite-level equation

\[
1+2\rho_n(x_2)=0\pmod{3^n}.
\]

### A.10 Full orientation

\[
\chi(x_2)=(1-3)^{-1},
\qquad
\chi(x_i)=1\quad(i\ne2).
\]

---

## 부록 B. 논문 상태표

| 주장 / branch | 상태 |
|---|---|
| Bare quadratic graded data가 \(\chi\bmod9\)를 복원 | **FAIL / CLOSED** |
| Projective degree-\((2,3)\) jet이 \(\chi\bmod9\)를 복원 | **PASS / CLOSED** |
| Presentation/lift/gauge에 대한 recovery zero set의 불변성 | **PASS**, 명시된 표준 가정 아래 |
| Raw \(J_3\)의 absolute minimality | 자연스러운 quotient category에서 **FAIL / CLOSED** |
| \(\overline J_3=[(R,p(P))]\)의 coarsest natural quotient 성질 | **PASS / CLOSED** |
| Compatible finite-level tower가 full \(\chi\)를 복원 | **PASS / CLOSED** |
| Fixed \(q=3\) exact \(\mathbf Z_3\) relation/evaluation data가 full \(\chi\)를 복원 | **PASS / CLOSED** |
| Universal bounded-degree + finite-precision full-\(\chi\) carrier | **FAIL / CLOSED** |
| Naive \(\mathbf Z_3\) restricted-Lie scalar extension | **FAIL / CLOSED** |
| \(\overline J_3\)와 유사한 concrete non-tautological finite exact compression | **OPEN / NOT PROVED** |
| General rank / general \(q\) theorem | **OPEN** |
| Other filtrations | **OPEN** |
