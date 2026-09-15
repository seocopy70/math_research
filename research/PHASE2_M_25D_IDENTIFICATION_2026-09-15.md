# Phase 2 — 25차원 중간층 M의 식별

날짜: 2026-09-15

## 1. 현재 계산으로 확정된 구조

\[
W=\langle Sp_4(\mathbb F_3)\cdot[T]\rangle,
\qquad \dim W=45.
\]

Phase 2-3에서
\[
\operatorname{End}_H(W)\cong \mathbb F_3[\varepsilon]/(\varepsilon^2)
\]
이고 비영 nilpotent \(N\)에 대해
\[
U=\operatorname{im}N,\qquad K=\ker N,
\]
\[
\dim U=10,\qquad \dim K=35,
\qquad M=K/U,\quad \dim M=25.
\]

Phase 2-6의 독립 intertwiner 계산으로
\[
U\cong \operatorname{Sym}^2(V)=L(2,0)
\]
을 확정했다.

Phase 2-8B에서는 M의 다섯 생성원에 의해 생성되는 결합대수가
\[
\langle A_1,\dots,A_5\rangle_{\rm alg}
=\operatorname{Mat}_{25}(\mathbb F_3)
\]
임을 계산 certificate로 확인했다. 따라서
\[
\boxed{M\text{은 }Sp_4(\mathbb F_3)\text{-module로 irreducible이다.}}
\]

또한 M은 degree-4의 subquotient이므로 중심원소 \(-I\in Sp_4(\mathbb F_3)\)가 항등으로 작용한다. 따라서 M은
\[
PSp_4(3)=Sp_4(3)/\{\pm I\}
\]
의 module로 내려간다.

## 2. 문헌 검증

Cabanes–Marin, *On Ternary Quotients of Cubic Hecke Algebras*, Comm. Math. Phys. 314 (2012), Proposition 4.10 및 그 앞의 논의에서 다음을 확인할 수 있다.

- characteristic 3에서 \(Sp_4(\mathbb F_3)\)의 25차원 irreducible representation이 \(\mathbb F_3\) 위에서 정의된다.
- \(\Lambda^2(\operatorname{Sym}^2\bar\rho_0)\)의 45차원 representation의 composition factors가 \(\operatorname{Sym}^2\bar\rho_0\) 두 개와 25차원 irreducible 하나임을 설명한다.
- Proposition 4.10은 중심 \(Z(Sp_4(3))\)을 소거하는 유일한 25차원 simple module이 존재하며, 이는 유일한 25차원 simple \(PSp_4(3)\)-module임을 명시한다.

따라서 우리 계산에서 이미
\[
\dim M=25,\qquad M\text{ simple},\qquad -I\text{ acts trivially}
\]
를 확정했으므로 문헌의 유일성 결과를 적용하면
\[
\boxed{
M\cong M_{25},
}
\]
여기서 \(M_{25}\)는 유일한 25차원 simple \(PSp_4(3)\)-module이다.

이는 단순히 '차원이 25라서' 얻은 결론이 아니다. 핵심은
\[
\text{25차원}+\text{irreducible}+\text{center trivial}
\]
이라는 세 조건과 문헌의 유일성 정리를 결합한 것이다.

## 3. 중요한 정정: M=L(2,1)이라고 아직 쓰지 않는다

이전 연구기록에서 \(M\cong L(2,1)\)을 강하게 예상한 부분은 현재 폐기한다.

표준적인 \(C_2\) highest-weight convention에서는 중심원소 \(-I\)의 작용이 highest weight의 적절한 parity와 연결되므로, \((2,1)\) 표기와 현재 M의 중심 작용이 충돌할 가능성이 있다. 따라서 highest-weight label을 직접 대응시키기 전에는
\[
M\cong L(2,1)
\]
을 주장하지 않는다.

현재 정확한 표현은
\[
\boxed{M\cong \text{the unique 25-dimensional simple }PSp_4(3)\text{-module}.}
\]

highest-weight 표기와의 대응은 별도의 검증 과제로 남긴다.

## 4. 현재까지의 구조 지도

이제 Track A에서 다음 사슬은 상당 부분 확정되었다.

\[
T
\longrightarrow
W_{45}
\longrightarrow
\operatorname{End}_H(W)
\longrightarrow
N
\longrightarrow
U_{10}
\longrightarrow
M_{25},
\]

\[
W\cong\Lambda^2(\operatorname{Sym}^2V),
\qquad
U\cong\operatorname{Sym}^2V,
\qquad
M\cong M_{25}(PSp_4(3)).
\]

남은 중요한 문제는 W 자체의 extension 구조를 정확히 식별하고, 이 구조가 T나 symplectic basis의 선택과 무관하게 filtration에서 canonical하게 발생하는지를 검증하는 것이다.

## 5. 다음 단계

다음 계산은 두 갈래 중 먼저 하나를 선택한다.

### A. 가장 우선
문헌의 25차원 module을 실제 생성원 행렬로 구현하여 M과의 full-rank intertwiner를 구한다. 이를 통해 문헌 유일성에 의존하는 식별을 explicit certificate로 강화한다.

### B. 그 다음
\[
W\cong\Lambda^2(\operatorname{Sym}^2V)
\]
의 characteristic-3 module 구조와
\[
0\subset U\subset K\subset W
\]
의 extension class를 직접 비교하여 W의 정확한 indecomposable 구조를 식별한다.

이 단계에서는 \(T(2,1)\) 같은 tilting-module 명칭을 차원/층 구조만으로 선언하지 않는다.

## 6. 연구 원칙

모든 식별은
\[
\boxed{\text{계산 발견}\to\text{명시적 certificate}\to\text{문헌 검증}\to\text{독립 검산}}
\]
순서를 유지한다.

Track B의 Hall–Petrescu/A2 문제는 본 기록의 식별과 독립적으로 유지한다.
