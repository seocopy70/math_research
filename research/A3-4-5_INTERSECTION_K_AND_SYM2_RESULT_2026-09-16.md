# A3-4-5 — 교집합 I의 모듈 구조 검증

## 0. 목적

A3-4-4에서

\[
W_{45}=\langle Sp_4(\mathbb F_3)\cdot T\rangle,
\qquad
W_d=\langle Sp_4(\mathbb F_3)\cdot d\rangle,
\qquad d=[X_1^{[3]},X_2]
\]

에 대해

\[
\dim W_{45}=\dim W_d=45,
\qquad
\dim(W_{45}\cap W_d)=35,
\qquad
\dim(W_{45}+W_d)=55
\]

를 확인했다.

이번 단계에서는 새로운 표현론적 대상을 무작정 분해하지 않고, 기존에 이미 확보된 35차원 모듈 K와 10차원 \(\operatorname{Sym}^2V\)를 직접 비교한다.

두 가설:

1. \(I:=W_{45}\cap W_d\)가 기존의 \(K=\ker N\)과 동형인가?
2. \(W_{45}/I\)가 \(\operatorname{Sym}^2(V)=L(2,0)\)과 동형인가?

---

## 1. 정확한 계산 대상

Phase 2-1의 authoritative construction을 그대로 재사용하여

\[
\dim W_{45}=45,
\qquad
\dim Q_4=55,
\qquad
|Sp_4(\mathbb F_3)|=51840
\]

을 재확인했다.

A3-4-4에서 얻은 \(d\)의 전체 orbit은

\[
|Sp_4(\mathbb F_3)\cdot d|=360
\]

이고, orbit span은 45차원이다.

교집합은 \(W_{45}\)와 \(W_d\)의 독립적인 45차원 basis를 사용하여 ambient degree-4 word space에서 kernel로 계산했다. 이때 kernel 벡터는 90개의 좌표를 가지며, 앞 45개 좌표를 \(W_{45}\) 쪽 계수로 취해 \(I\)를 복원했다.

계산 결과:

\[
\boxed{\dim I=35}.
\]

---

## 2. Test 1 — \(I\cong K\)

기존 Phase 2-3의 비영 square-zero endomorphism \(N\)에 대해

\[
N^2=0,
\qquad
\operatorname{rank}N=10,
\qquad
\dim\ker N=35.
\]

따라서

\[
K:=\ker N
\]

은 35차원이다.

A3-4-5에서는 \(K\)와 \(I\) 각각에 대해 동일한 다섯 개의 \(Sp_4(\mathbb F_3)\) 생성자 작용을 제한하고, 정확한 intertwiner 방정식

\[
P A_i^{(K)}=A_i^{(I)}P
\qquad (i=1,\dots,5)
\]

을 \(\mathbb F_3\)에서 풀었다.

결과:

\[
\boxed{\dim \operatorname{Hom}_{Sp_4}(K,I)=1}
\]

이며 그 Hom-space에서

\[
\boxed{\operatorname{rank}P=35}
\]

인 전단사 intertwiner가 발견되었다.

따라서 계산적으로 정확하게

\[
\boxed{I\cong K}
\]

가 인증되었다.

이는 단순히 차원이 같은 것을 비교한 것이 아니라, 다섯 생성자의 작용을 모두 보존하는 명시적 모듈 동형의 존재를 확인한 것이다.

---

## 3. Test 2 — \(W_{45}/I\cong \operatorname{Sym}^2(V)\)

\[
\dim W_{45}=45,
\qquad
\dim I=35
\]

이므로

\[
\dim(W_{45}/I)=10.
\]

이 quotient에 동일한 다섯 생성자의 작용을 유도하고, 자연 4차원 모듈 \(V\)에서 직접 구성한

\[
\operatorname{Sym}^2(V)
\]

의 10차원 작용과 비교했다.

정확한 intertwiner 계산 결과:

\[
\boxed{\dim\operatorname{Hom}_{Sp_4}(W_{45}/I,\operatorname{Sym}^2V)=1}
\]

이며 Hom-space 안에

\[
\boxed{\operatorname{rank}P=10}
\]

인 전단사 intertwiner가 존재했다.

따라서

\[
\boxed{W_{45}/I\cong\operatorname{Sym}^2(V)=L(2,0)}.
\]

---

## 4. A3-4-5 최종 구조

이번 결과와 A3-4-4 결과를 합치면 \(Q_4\) 안에 다음 구조가 생긴다.

\[
\boxed{
\dim W_{45}=45,
\quad
\dim W_d=45,
\quad
\dim I=35,
\quad
\dim(W_{45}+W_d)=55.
}
\]

그리고

\[
\boxed{I\cong K}
\]

및

\[
\boxed{W_{45}/I\cong L(2,0)=\operatorname{Sym}^2(V)}.
\]

또한 A3-4-4에서

\[
\dim(W_d/I)=45-35=10
\]

이다.

따라서 제2동형정리에 의해

\[
W_{45}/I\cong Q_4/W_d,
\]

\[
W_d/I\cong Q_4/W_{45}
\]

도 자동으로 성립하며, 양쪽 모두 10차원이다.

다만 이번 계산 자체에서는

\[
W_d/I\cong W_{45}/I
\]

를 별도의 intertwiner로 확인하지 않았다. 이 동형은 다음 선택적 symmetry test로 남겨둔다.

---

## 5. 현재까지의 가장 압축된 구조

현재 계산적으로 확보된 그림은

\[
\boxed{
\begin{array}{ccccc}
&&Q_4\;(55)&&\\
&\nearrow&&\nwarrow&\\
W_{45}\;(45)&&&&W_d\;(45)\\
&\searrow&&\swarrow&\\
&&I\cong K\;(35)&&
\end{array}}
\]

이며

\[
W_{45}/I\cong L(2,0),
\qquad
W_d/I\cong Q_4/W_{45}.
\]

즉 두 45차원 부분모듈의 공통 35차원 핵심이 기존 Track A의 \(K\)와 같은 모듈이고, 그 위에 각각 10차원 quotient가 놓인다.

---

## 6. Track A / Track B 연결의 의미

A3-4-3에서는 restricted structure가 만든

\[
d=[X_1^{[3]},X_2]
\]

가

\[
d\notin R_4+W_{45}
\]

임을 정확히 확인했다.

A3-4-4에서는 이 하나의 restricted class의 전체 \(Sp_4\)-orbit span \(W_d\)가 45차원이고, 기존 \(W_{45}\)와 함께 정확히 55차원 \(Q_4\) 전체를 생성한다는 사실을 얻었다.

A3-4-5에서는 그 교집합이 기존 Track A의 35차원 \(K\)와 모듈 동형이고, 기존 10차원 \(\operatorname{Sym}^2V\)가 quotient로 다시 나타남을 직접 인증했다.

따라서 현재 시점에서 처음으로 다음 두 구조가 같은 표현론적 대상으로 연결되었다:

- Track A: \(W_{45}\) 내부의 \(K_{35}\)와 10차원 단순층
- Track B: \(q=3\) restricted class가 생성하는 \(W_d\)

단, 이것이 곧바로 canonical orientation recovery의 최종 증명을 의미하는 것은 아니다. 아직 이 모듈 구조가 원래 Demuškin 관계식의 orientation 데이터와 어떤 정확한 자연성/정준성을 갖는지 별도의 논증이 필요하다.

---

## 7. 재현성

GitHub Actions:

- Workflow: `Phase 2-18 A3-4-5 Intersection Module Tests`
- Successful run: `35044091752`
- Head commit: `2add0545b42d42c0768f1c26c49ab9630694d5da`
- Python 3.11 / NumPy 2.4.6

핵심 로그:

```text
dim W45 = 45
dim Wd = 45
orbit size of d = 360
dim I = dim(W45 intersect Wd) = 35
dim K = dim ker(N) = 35
rank([W45 | Wd]) = 55

TEST 1: I ~= K
dim Hom_H(K,I) = 1
maximum intertwiner rank = 35
FULL_RANK_INTERTWINER_FOUND = True

TEST 2: W45/I ~= Sym^2(V)
dim(W45/I) = 10
dim Hom_H(W45/I, Sym^2(V)) = 1
maximum intertwiner rank = 10
FULL_RANK_INTERTWINER_FOUND = True

I_EQUALS_K_UP_TO_H_MODULE_ISOMORPHISM = True
W45_OVER_I_EQUALS_SYM2 = True
ALL A3-4-5 HYPOTHESIS TESTS PASSED
```

## 8. 판정

\[
\boxed{\textbf{A3-4-5 두 가설 모두 계산적으로 인증됨.}}
\]

이번 단계는 차원 일치가 아니라 정확한 \(Sp_4(\mathbb F_3)\)-intertwiner를 통한 모듈 동형 검증이다.
