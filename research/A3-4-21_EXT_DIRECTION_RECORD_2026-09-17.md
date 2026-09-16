# A3-4-21 — Ext 방향과 비분할 확장 기록

## 상태

**A3-4-21 = CLOSED / PASS (구조 분류 단계)**

2026-09-17 기준으로, A3-4-17부터 A3-4-20S까지의 정확한 계산 결과를 이용하여 \(B/A\)와 \(K\) 사이의 비분할 확장 방향을 확정한다.

단, **전체 \(\operatorname{Ext}^1\) 공간의 차원은 계산하지 않는다.** 이는 별도의 후속 단계로 보류한다.

---

## 1. A3-4-17: Hom 검증

동일한 \(H=Sp_4(\mathbb F_3)\) 작용행렬에 대해

\[
\dim \operatorname{Hom}_H(B/A,K)=1.
\]

유일한 비영 intertwiner의 rank는

\[
\operatorname{rank}Q=10.
\]

따라서

\[
\max\{\operatorname{rank}P:P\in\operatorname{Hom}_H(B/A,K)\}=10<35,
\]

즉

\[
B/A\not\cong_H K.
\]

---

## 2. A3-4-18: Loewy 구조

두 모듈 모두 indecomposable이며 Loewy length 2이다.

두 층의 차원은 10과 25이다.

---

## 3. A3-4-19: 단순 인자

GAP/MeatAxe의 `CollectedFactors` 및 `MTX.Isomorphism`으로 두 모듈의 composition factors를 정확히 비교했다.

양쪽 모두 단순 인자는

\[
\{S_{10},S_{25}\}
\]

이며 각각 multiplicity 1이다.

또한

\[
S_{10}^{B/A}\cong S_{10}^{K},
\qquad
S_{25}^{B/A}\cong S_{25}^{K}.
\]

A3-4-19 = PASS.

---

## 4. A3-4-20R: 정확한 확장 방향

유일한 nonzero intertwiner \(Q:B/A\to K\)를 이용하여 다음을 정확히 확인했다.

\[
0\longrightarrow \ker Q\longrightarrow B/A\longrightarrow (B/A)/\ker Q\longrightarrow0,
\]

그리고

\[
0\longrightarrow \operatorname{im}Q\longrightarrow K\longrightarrow K/\operatorname{im}Q\longrightarrow0.
\]

A3-4-20R의 네 irreducibility test가 모두 PASS하여

\[
\ker Q\cong S_{25},
\qquad
(B/A)/\ker Q\cong S_{10},
\]

\[
\operatorname{im}Q\cong S_{10},
\qquad
K/\operatorname{im}Q\cong S_{25}.
\]

따라서 정확한 구조는

\[
\boxed{0\to S_{25}\to B/A\to S_{10}\to0}
\]

및

\[
\boxed{0\to S_{10}\to K\to S_{25}\to0}.
\]

A3-4-18의 indecomposability와 함께 두 확장은 split되지 않는다.

따라서 Ext class 수준에서

\[
[B/A]\in \operatorname{Ext}^1_H(S_{10},S_{25}),
\qquad [B/A]\ne0,
\]

\[
[K]\in \operatorname{Ext}^1_H(S_{25},S_{10}),
\qquad [K]\ne0.
\]

**주의:** 여기서는 Ext 공간의 차원을 주장하지 않는다.

---

## 5. A3-4-20S: socle의 실제 부분공간 정렬

A3-4-20S에서는 A3-4-16의 동일한 35×35 작용행렬과 A3-4-20R에서 복원한 동일한 \(Q\)를 사용했다.

정확한 basis orientation을 수정한 뒤 GAP/MeatAxe의 실제 socle basis와 Python에서 계산한 \(\ker Q\), \(\operatorname{im}Q\)를 동일한 35차원 ambient coordinate system에서 직접 비교했다.

결과:

\[
\dim\operatorname{Soc}(B/A)=25,
\qquad
\dim\operatorname{Soc}(K)=10,
\]

\[
\dim\ker Q=25,
\qquad
\dim\operatorname{im}Q=10.
\]

그리고 단순한 차원 일치가 아니라 span equality를 직접 확인했다:

\[
\boxed{\operatorname{Soc}(B/A)=\ker Q},
\]

\[
\boxed{\operatorname{Soc}(K)=\operatorname{im}Q}.
\]

교차 비교는 모두 false였다:

\[
\operatorname{Soc}(B/A)\ne\operatorname{im}Q,
\qquad
\operatorname{Soc}(K)\ne\ker Q.
\]

따라서 Q가 두 모듈의 실제 Loewy/socle 층을 정확히 정렬한다는 것이 확인되었다.

A3-4-20S = PASS.

---

## 6. A3-4-21의 결론

현재 계산으로 확정할 수 있는 것은 다음이다.

\[
\boxed{B/A\text{는 }S_{10}\text{ 위에 }S_{25}\text{가 놓인 비분할 확장}}
\]

\[
\boxed{K\text{는 }S_{25}\text{ 위에 }S_{10}\text{이 놓인 비분할 확장}}
\]

즉 두 모듈은 **동일한 두 단순 인자를 가지지만 extension direction이 서로 반대**이다.

이는 A3-4-17의 비동형성, A3-4-18의 indecomposability, A3-4-19의 simple-factor matching, A3-4-20R의 정확한 extension sequence, A3-4-20S의 실제 socle-subspace equality가 서로 독립적인 층에서 일치하는 구조적 확인이다.

---

## 7. 의도적으로 보류한 계산

다음 명제들은 아직 계산하지 않았으므로 주장하지 않는다.

\[
\dim\operatorname{Ext}^1_H(S_{10},S_{25})=?
\]

\[
\dim\operatorname{Ext}^1_H(S_{25},S_{10})=?
\]

특히 어느 Ext 공간이 1차원이라는 주장, Cartan matrix의 특정 entry와 동일하다는 주장, 또는 해당 비분할 확장이 유일하다는 주장은 현재 결과만으로는 하지 않는다.

전체 Ext 차원 계산은 projective resolution/cohomological computation이 필요할 수 있으므로 별도 단계로 분리한다.

---

## 8. 다음 연구 단계의 원칙

다음 단계에서는 먼저 **이 반대 방향의 비분할 확장이 orientation/q-sensitive 구조와 어떤 관계를 갖는지**를 조사한다.

즉 곧바로 Ext 차원을 계산하기보다, 이미 확보된

\[
S_{10}\leftrightarrow S_{25}
\]

의 반대 extension 방향이 기존의 \(q=3\) 대 \(q=\infty\) 판별 문제에서 실제로 정보를 제공하는지 확인하는 쪽을 우선한다.

전체 Ext 계산은 그 구조적 연결이 확인되거나, 이후 별도로 필요한 경우에만 수행한다.

---

## 9. 관련 실행 기록

- A3-4-17: GitHub Actions run `35111549911`, Job `104846262041`
- A3-4-18: GitHub Actions run `35112986819`
- A3-4-19: GitHub Actions run `35114438796`, Job `104856145601`
- A3-4-20R: successful run `35116761852`, Job `104864042643`
- A3-4-20S: strict final run `35148511536`, Job `104970564246`

