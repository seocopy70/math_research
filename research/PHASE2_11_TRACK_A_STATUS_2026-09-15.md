# Track A — Phase 2-11 시작 기록

## 2026-09-15

### 1. 문헌 검증에 관한 정리

Cabanes–Marin, *On Ternary Quotients of Cubic Hecke Algebras*, Comm. Math. Phys. 314 (2012), 57–92, arXiv:1010.1465는 실제 존재하는 논문이다. 제목상 cubic Hecke algebra가 주제이지만 논문 §4.3.2에는 characteristic 3의 \(Sp_4(3)\) 표현과
\(Λ^2(S^2\bar\rho_0)\)의 45차원 표현, 25차원 irreducible composition factor가 실제로 등장한다. Proposition 4.10도 25차원 simple \(kSp_4(3)/Z(Sp_4(3))\)-module의 유일성을 명시한다.

다만 현재 연구의 핵심 논증은 이 문헌에 의존하지 않는다. 문헌은 외부 corroboration으로만 취급한다.

우리의 독립 계산으로 이미 다음을 확보했다.

- \(\dim M=25\)
- \(M\)은 irreducible
- \(-I\)가 degree 4에서 자명하게 작용하므로 \(M\)은 \(PSp_4(3)\)의 모듈
- 별도 GAP 계산의 3-modular simple dimension 목록에서 25차원 simple이 유일함을 독립적으로 확인할 수 있음

따라서 이후 문서에서는

\[
M \cong \text{the unique 25-dimensional simple }PSp_4(3)\text{-module}
\]

을 자체 계산을 주된 근거로 삼는다. Cabanes–Marin은 보조 문헌 확인으로만 둔다.

### 2. Phase 2-10의 핵심 확정 결과

독립 계산으로

\[
W\cong \Lambda^2(\operatorname{Sym}^2V)
\]

를 확정했다.

구체적으로:

- \(\dim W=45\)
- model \(\dim \Lambda^2(\operatorname{Sym}^2V)=45\)
- intertwiner system 크기 \(10125\times2025\)
- 독립 elimination과 RREF에서 모두 rank \(2023\)
- 따라서 \(\dim\operatorname{Hom}_H(W,\Lambda^2(\operatorname{Sym}^2V))=2\)
- nullspace의 8개 비영 homomorphism를 전수 검사하여 6개가 rank 45
- 실제 full-rank intertwiner의 존재 확인
- witness SHA256: `1c4276a930acda5e1c33996beee59467fd197ebd5bbe0f04d94bae7b0d314843`
- 모든 5개 generator intertwining equation 확인

동시에 이전 단계에서

\[
\dim\operatorname{End}_H(W)=2,
\qquad
\operatorname{End}_H(W)\cong\mathbb F_3[\varepsilon]/(\varepsilon^2)
\]

를 독립적으로 확보했다. 두 차원의 일치는 Phase 2-10 식별 결과에 대한 중요한 교차검증이다.

### 3. 현재 filtration/submodule 구조

이미 다음 exact chain을 확보했다.

\[
0\subsetneq U\subsetneq K\subsetneq W,
\]

\[
\dim U=10,\qquad \dim K=35,\qquad \dim W=45.
\]

또

\[
U\cong \operatorname{Sym}^2V,
\]

그리고

\[
M:=K/U,
\qquad \dim M=25,
\]

이며 Phase 2-8B의 certificate

\[
\langle A_1,\ldots,A_5\rangle_{\rm alg}=\operatorname{Mat}_{25}(\mathbb F_3)
\]

로부터 \(M\)의 irreducibility를 직접 증명했다.

### 4. Phase 2-11의 대상


\[
E:=W/U
\]

로 놓는다. 그러면

\[
\dim E=35
\]

이고 자연스러운 exact sequence

\[
\boxed{
0\longrightarrow M_{25}
\longrightarrow E_{35}
\longrightarrow S^2V_{10}
\longrightarrow0
}
\]

가 생긴다.

Phase 2-11의 핵심 질문은 이 extension이 split인지 non-split인지이다.

즉

\[
E\stackrel{?}{\cong}M_{25}\oplus S^2V
\]

인가, 아니면

\[
0\to M_{25}\to E\to S^2V\to0
\]

가 비분해 extension인가를 결정한다.

### 5. Phase 2-11의 권장 순서

처음부터 Ext를 직접 계산하지 않는다.

#### Phase 2-11-A — 10차원 complement 탐색

split이라면 \(E\) 안에 \(S^2V\)와 동형인 10차원 \(H\)-stable submodule이 존재해야 한다.

따라서 먼저

> \(E\) 안에 10차원 \(H\)-submodule이 존재하는가?

를 계산한다.

존재하지 않으면 즉시 extension non-split이다.

#### Phase 2-11-B — \(\operatorname{End}_H(E)\) 계산

그 다음

\[
\operatorname{End}_H(E)
\]

을 계산하여 extension 구조의 독립적인 fingerprint를 확보한다.

#### Phase 2-11-C — 필요할 경우 Ext 계산

마지막으로 필요하면

\[
\operatorname{Ext}^1_H(S^2V,M_{25})
\]

를 직접 계산하여 extension class를 분석한다.

따라서 권장 순서는

\[
\boxed{
\text{10차원 submodule 탐색}
\rightarrow
\operatorname{End}_H(E)
\rightarrow
\operatorname{Ext}^1
}
\]

이다.

### 6. 연구 방법론 원칙

계속해서 다음 기준을 유지한다.

\[
\boxed{\text{컴퓨터 발견}\to\text{명시적 certificate}\to\text{수학적 설명}\to\text{독립 검산}}
\]

raw output을 proof로 간주하지 않는다. 문헌 인용은 반드시 실제 논문과 해당 proposition/section을 확인한 뒤 사용한다.

### 7. Track 분리

Track A는 위의 representation-theoretic extension 문제를 독립적으로 진행한다.

Track B의 Hall–Petrescu / filtration 계산(A1, A2, A3)은 Track A의 계산에 섞지 않는다.

현재 Track A의 다음 실제 계산은 Phase 2-11-A이다.
