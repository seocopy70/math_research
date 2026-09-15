# Phase 2-1: W의 Sp_4(F_3)-불변부분 검증

## 1. 목적

Phase 1에서

\[
Q_4=L_4/(R)_4,\qquad \dim L_4=60,\quad \dim(R)_4=5,\quad \dim Q_4=55
\]

를 확인했고,

\[
T=[[X_3,X_4],X_1],X_1
\]

가 symplectic transvection에 대해 invariant가 아님을 확인했다.

Phase 2-1의 목적은

\[
W=\langle Sp_4(\mathbb F_3)\cdot[T]\rangle\subset Q_4
\]

에 대해 정확히

\[
W^{Sp_4(\mathbb F_3)}
=\{w\in W:gw=w\ \forall g\in Sp_4(\mathbb F_3)\}
\]

의 차원을 독립적으로 계산하는 것이다.

---

## 2. 사용한 기준

모든 계산은 \(\mathbb F_3\) 위에서 수행한다.

symplectic form은 반드시 다음 행렬을 사용한다.

\[
J=
\begin{pmatrix}
0&1&0&0\\
-1&0&0&0\\
0&0&0&1\\
0&0&-1&0
\end{pmatrix}\pmod3.
\]

비영 벡터 \(v\in\mathbb F_3^4\)에 대한 transvection은

\[
t_v=I+v(Jv)^T\pmod3.
\]

\(v\)와 \(-v\)는 같은 transvection을 주므로 distinct transvection은 총 40개이다.

Phase 2-1에서는 다음 다섯 transvection을 생성자로 사용한다.

\[
v=e_1,e_2,e_3,e_4,e_1+e_3.
\]

각 생성자는 직접 \(g^TJg=J\)를 검사하고, 이 다섯 생성자로 생성되는 행렬군의 크기를 직접 열거하여

\[
|\langle g_1,\ldots,g_5\rangle|=51840
\]

임을 확인한다. 이는

\[
|Sp_4(\mathbb F_3)|=51840
\]

과 일치하므로 이들이 전체 symplectic group을 생성한다는 계산적 certificate가 된다.

---

## 3. 계산 과정

### 3.1 orbit span

정확한 Phase 1의 associative-word 구현을 그대로 사용한다.

각 생성자 \(g_i\)에 대해 degree-4 associative algebra에서 generator의 선형 치환을 수행하여 \(T\)와 그 orbit을 계산한다.

orbit 원소를 순차적으로 추가하면서

\[
\operatorname{rank}[R_4\mid W_{\rm basis}]
\]

가 증가할 때만 새로운 W basis vector로 채택한다.

계산 결과:

\[
\boxed{\dim W=45}
\]

이며

\[
\operatorname{rank}[R_4\mid W_{\rm basis}]=50.
\]

여기서 \(\operatorname{rank}(R_4)=5\)이므로 quotient에서 W의 차원은 45이다.

### 3.2 W의 생성자 작용

\(R_4\)에서 독립인 5개 열을 선택하고 W의 45개 basis와 합쳐

\[
B=[R_{4,\mathrm{ind}}\mid W_{\rm basis}]
\]

라는 \(256\times50\) 행렬을 만든다.

그 rank는 50이다.

독립인 50개 행을 선택하여 50×50 부분행렬을 만들고 \(\mathbb F_3\)에서 역행렬을 구한다. 이를 이용하여 각 transformed W basis vector를

\[
R_4\text{-좌표}\oplus W\text{-좌표}
\]

로 복원한다.

각 generator에 대해 마지막 45개 좌표만 취하면

\[
A_i\in GL(W)\simeq GL_{45}(\mathbb F_3)
\]

를 얻는다.

### 3.3 invariant space

\(w\in W\)가 전체 group에서 invariant이면 생성자 각각에 대해

\[
(A_i-I)w=0
\]

이어야 한다.

따라서

\[
M=
\begin{pmatrix}
A_1-I\\
A_2-I\\
A_3-I\\
A_4-I\\
A_5-I
\end{pmatrix}
\]

라는 \(225\times45\) 행렬을 만든다.

계산 결과:

\[
\boxed{\operatorname{rank}_{\mathbb F_3}M=45}.
\]

따라서 rank-nullity에 의해

\[
\dim W^{Sp_4(\mathbb F_3)}
=45-45
=\boxed{0}.
\]

즉

\[
\boxed{W^{Sp_4(\mathbb F_3)}=0.}
\]

---

## 4. 검증 결과 전체 목록

| 항목 | 계산 결과 |
|---|---:|
| \(\dim L_4\) | 60 |
| \(\dim(R)_4\) | 5 |
| \(\dim Q_4\) | 55 |
| Phase 1 transvection의 symplectic 여부 | PASS |
| \(\operatorname{rank}(R_4)\) | 5 |
| \(\operatorname{rank}[R_4\mid gT-T]\) | 6 |
| distinct transvections | 40 |
| 사용한 group generators | 5 |
| 생성 group order | 51840 |
| \(\dim W\) | 45 |
| \(\operatorname{rank}[R_{4,ind}\mid W]\) | 50 |
| W action matrix | 45×45 |
| \(\operatorname{rank}M\) | 45 |
| \(\dim W^{Sp_4(\mathbb F_3)}\) | **0** |

---

## 5. 해석상 주의

이 결과는 다음을 의미한다.

> \(T\)의 symplectic orbit가 생성하는 45차원 representation \(W\) 안에는 nonzero global invariant vector가 없다.

따라서 \(T\)의 orbit span 전체에서 단순히 "group invariant vector 하나를 찾는 것"으로 canonical orientation을 복원하는 방법은 실패한다.

그러나 이것이 orientation 정보가 filtration에 전혀 없다는 뜻은 아니다. 특히 현재 연구의 다음 단계는

\[
W^H\to\text{invariant submodules}\to\text{composition factors}\to\operatorname{End}_H(W)
\]

순으로 진행해야 한다.

특성 3이 group order 51840을 나누므로 modular representation은 일반적으로 semisimple하지 않다. 따라서 central-idempotent 방식으로 시작하지 않고 invariant submodule / composition structure를 먼저 조사한다.

---

## 6. 재현 코드

완전한 재현 코드는 같은 디렉터리의

`phase2_1_invariant_space_verification_2026-09-15.py`

에 보존한다.

이 파일은 Phase 1의 핵심 정의를 다시 포함하고 있으며 Phase 2-1 계산을 이어서 수행한다. 즉 다음 항목을 한 번에 재검산할 수 있다.

1. \(L_4,(R)_4,Q_4\) 차원
2. Phase 1 transvection 검사
3. 40개 distinct transvection
4. 5개 생성자의 symplectic 여부
5. 생성 group order 51840
6. orbit span \(W\)의 차원 45
7. \(R_4\oplus W\) 좌표계
8. 45×45 generator action matrices
9. stacked \((A_i-I)\)의 rank 45
10. \(W^{Sp_4(\mathbb F_3)}=0\)

---

## 7. 상태

**Phase 2-1 계산 검증 완료.**

다음 연구 단계는 invariant vector가 아니라 W의 내부 submodule 구조를 조사하는 것이다.

권장 순서:

\[
W\supsetneq M\supsetneq\cdots
\]

형태의 invariant submodule 탐색 → composition factors → 각 factor의 multiplicity → 필요할 경우

\[
\operatorname{End}_{Sp_4(\mathbb F_3)}(W)
\]

계산.

단, composition series 계산에 들어가기 전에 현재의 45차원 W action matrices를 독립적으로 한 번 더 저장/재현하여 이후 모든 계산의 기준점으로 삼는다.

---

## 8. Git 기록

- Repository: `seocopy70/math_research`
- Branch: `main`
- Commit: `1e3516349b1f5ac575bdadd8cb79c9bb87852f4a`
- Python reproduction script: `research/phase2_1_invariant_space_verification_2026-09-15.py`
- This record: `research/PHASE2_1_INVARIANT_SPACE_VERIFICATION_2026-09-15.md`
