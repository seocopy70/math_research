# 중간평가 — Orientation Reconstruction 연구 현황 (2026-09-19)

> 이 문서는 2026-09-19 현재까지의 연구를 한 시점에서 평가하고, 무엇이 닫혔고 무엇이 실제로 남았는지를 고정하기 위한 중간평가 기록이다.
> 상세 chronology는 \`research/00_RESEARCH_LOG.md\`, 전체 구조는 \`RESEARCH_MAP.md\`, 새 세션 복원용 최신 상태는 \`CURRENT_STATE.md\`를 권위 문서로 사용한다.

## 1. 원래 연구 질문

\[
\boxed{\text{Can the canonical orientation }\chi:G\to\mathbf Z_3^\times
\text{ be recovered intrinsically from filtered/graded data?}}
\]

핵심은 단순히 \(\chi\)를 계산하는 것이 아니라, **어느 정도의 enriched filtered/graded information이 있어야 orientation 정보가 살아남는지**, 그리고 그 정보가 실제로 \(\chi\)를 결정하는지를 밝히는 것이다.

## 2. 2026-09-19 현재의 핵심 지형

| 데이터 | 현재 판정 | 의미 |
|---|---|---|
| bare associated graded restricted Lie object | **FAIL / CLOSED** | \(\chi\bmod 9\)조차 결정하지 못함 |
| projective degree-(2,3) relation jet | **PASS / CLOSED** | \(\chi\bmod 9\) 복원 |
| compatible full filtered relation-jet tower | **PASS** | full \(3\)-adic \(\chi\) 복원 메커니즘 확보. 단, finite-level factorization/inverse-limit 표현은 명시해야 함 |
| 유한 bounded-degree jet 하나 \(\Rightarrow\) full \(\chi\) | **OPEN** | 핵심 미해결 질문 |
| projective jet의 categorical absolute minimality | **OPEN** | 핵심 미해결 질문 |

따라서 **“\(\chi\)를 복원할 수 있는가?”라는 질문 자체에는 긍정적인 답이 확보되었다.** 다만 “얼마나 약한 데이터로 가능한가?”라는 더 날카로운 질문은 아직 끝나지 않았다.

## 3. Bare graded data의 한계

\[
G_3=\langle x_1,x_2,x_3,x_4\mid x_1^3[x_1,x_2][x_3,x_4]\rangle
\]

와

\[
G_\infty=\langle x_1,x_2,x_3,x_4\mid [x_1,x_2][x_3,x_4]\rangle
\]

은 \(p=3\)에서 같은 초기 quadratic relation

\[
R_2=[X_1,X_2]+[X_3,X_4]
\]

을 갖는다. bare associated graded restricted Lie object는 이 초기 관계만으로 두 경우를 구별하지 못한다.

반면

\[
\chi_3(x_2)=4\pmod 9,\qquad
\chi_\infty(x_2)=1\pmod 9.
\]

따라서

\[
\boxed{\text{bare associated graded restricted Lie object }\not\Rightarrow\chi\bmod9.}
\]

이것은 단순 계산 실패가 아니라 **정보론적/구조적 obstruction**으로 CLOSED 되었다.

## 4. Projective degree-(2,3) relation jet

중요한 정보는 \(P_3\) 자체가 아니라 \(P_3\)가 **같은 filtered defining relation의 degree-3 component라는 coupling**이다.

\[
J_3=\langle(R_2,P_3)\rangle
\subset L_2\oplus L_3^{res}.
\]

복원 functional은

\[
\Theta_J(\lambda)(f)
=
f(P_3)+(\lambda\wedge f)(R_2).
\]

Frozen coordinates에서 정확히

\[
B_\lambda(f)
=
(1-a_2)f_1+a_1f_2-a_4f_3+a_3f_4.
\]

비퇴화성 때문에 zero가 유일하며,

\[
\lambda_\chi=e_2^*,
\qquad
\rho(x_1,x_2,x_3,x_4)=(1,4,1,1)\pmod9.
\]

Presentation/lift/relator-gauge/normalization 변화에서

\[
(R,P)\mapsto(uR,uP+[v,R])
\]

형태의 gauge가 나타나며, degree-one functional은 \(f([v,R])=0\)이므로 \(\Theta\)의 zero set은 보존된다.

현재 no-scan audit에서 확보된 상태:

- E1 Definition: PASS (recovery-functional/projective-gauge 수준)
- E2 Presentation/lift independence: PASS (표준 minimal one-relator 사실을 조건으로)
- E3 Functoriality: PASS
- E4 \(q=3\) vs \(q=\infty\): PASS
- E5 \(\chi\bmod9\) recovery: PASS

단, **projective jet 자체가 categorical하게 절대 최소라는 것은 아직 증명되지 않았다.**

## 5. Full 3-adic orientation

표준 commutator convention

\[
[x,y]=x^{-1}y^{-1}xy
\]

하에서 \(r=x_1^3[x_1,x_2][x_3,x_4]\)에 \(\rho\)-crossed derivation을 대입하면

\[
\rho(x_1)=\rho(x_3)=\rho(x_4)=1,
\qquad
1+2\rho(x_2)=0.
\]

따라서

\[
\boxed{
\chi(x_2)=(1-3)^{-1},\qquad
\chi(x_i)=1\;(i\ne2).
}
\]

즉,

\[
\chi(x_2)=4\pmod9,\quad
13\pmod{27},\quad
40\pmod{81},\quad
121\pmod{243},\ldots
\]

가 된다.

핵심은 매 단계마다 새로운 obstruction을 발명할 필요가 없다는 점이다. 동일한 식

\[
1+2\chi(x_2)=0
\]

이 모든 \(3^n\)에서 동시에 작동한다.

따라서 **compatible full filtered relation-jet tower가 충분한 경우 full \(3\)-adic character를 복원할 수 있다**는 구조가 확인되었다.

## 6. Full tower 결과의 논리적 경계

현재 손계산이 직접 증명한 것은 **full defining relation을 사용한 crossed-derivation characterization**이다.

이를 엄밀하게

\[
\text{compatible full filtered relation-jet tower}\Rightarrow\text{full }\chi
\]

라는 theorem으로 표현하려면 다음을 명시해야 한다.

1. 각 finite-level jet \(J_n\)이
   \[
   \chi_n=\chi\bmod3^n
   \]
   을 유일하게 결정한다.
2. 이 \(\chi_n\)들이
   \[
   \chi_{n+1}\equiv\chi_n\pmod{3^n}
   \]
   로 compatible함을 보인다.
3. 그 후
   \[
   \chi=\varprojlim_n\chi_n
   \]
   로 정리한다.

따라서 현재 결과를 과장하여 “finite-level factorization theorem까지 이미 증명했다”고 쓰면 안 된다.

## 7. 주요 실패/폐기 경로가 남긴 것

- linear-only rank-4 lift observable — lift independence FAIL
- preferred Nielsen lift repair — 금지
- naive q=9 relation-space route — H-stability FAIL
- artificial H-closure — presentation relation object로 부적절
- Q3/Q9 S9 orbit route — definition-level CLOSED
- D9-OBS universal p-layer candidate — universal shadow로 FAIL
- \(\Delta_q(g)\) cocycle — 실제로
  \[
  \Delta_q(g)=g[X_1^3]-[X_1^3]
  \]
  인 coboundary로 확인되어 **NO NEW INFORMATION / CLOSED**
- Rank-2 relator-unit scalar — 제안된 chosen-lift scalar의 lift-independence FAIL
- \(\mu\)-\(\chi\) bridge — \(\mu\)는 \(F_3^\times\)-valued automorphism/duality-line character이고 \(\chi\)는 \(Z_3^\times\)-valued group orientation이므로 동일하지 않음
- ordinary Bockstein — q=3 power direction은 보지만 \(\chi(x_2)=4\bmod9\)를 복원하지 못하여 candidate CLOSED

이 실패들은 단순한 시행착오가 아니라 **어떤 정보가 orientation을 잃어버리는지에 대한 경계 지도**를 제공한다.

## 8. 수학적 평가

### 8.1 당연한 부분

full filtered relation-jet tower는 defining relation의 상당 부분을 보존한다. 따라서 표준 Demuškin crossed-derivation characterization을 적용하여

\[
\chi(x_2)=(1-q)^{-1}
\]

을 얻는 것 자체는 기존 구조와 가깝다. 이를 완전히 새로운 reconstruction theorem이라고 과장해서는 안 된다.

### 8.2 실제 성과

1. bare associated graded로는 \(\chi\bmod9\)조차 복원되지 않는다는 것을 구조적으로 닫았다.
2. projective degree-(2,3) relation jet으로 \(\chi\bmod9\)를 복원하는 구체적 mechanism을 확보했다.
3. presentation/lift/gauge 변화에 대해 recovery zero set이 보존되는 구조를 확인했다.
4. 동일한 식이 모든 \(3^n\)에서 작동하여 higher obstruction을 새로 발명할 필요가 없음을 확인했다.
5. 여러 실패 경로를 통해 **orientation 정보가 사라지는 층과 살아남는 층의 경계**를 명확히 했다.

가장 정확한 평가는:

> **강한 데이터를 주면 복원된다는 사실 자체보다, bare graded와 enriched relation jet 사이에 실제 정보 경계가 존재하고 그 경계에서 \(\chi\bmod9\)가 복원된다는 것이 핵심 성취다.**

## 9. 논문 관점의 현재 위치

현재 상태만으로도 독립적인 연구 노트/논문으로 정리할 소재는 있다. 다만 중심 주장을 “full tower로 orientation을 복원한다”에 두면 새로움은 제한적이다.

더 강한 논문 구조는

\[
\boxed{
\text{necessary lower bound}
+
\text{explicit sufficient enriched carrier}
+
\text{reconstruction}
+
\text{minimality}
}
\]

이다.

현재 확보된 것은 앞의 세 요소 중 상당 부분이고, **categorical minimality가 핵심 미완성**이다.

## 10. 남은 핵심 문제

### Priority 1 — finite-level factorization / inverse-limit theorem

명시적으로

\[
J_n\longmapsto\chi_n\in(\mathbf Z/3^n)^\times
\]

을 정의하고,

\[
J_{n+1}\mapsto J_n
\quad\Longrightarrow\quad
\chi_{n+1}\mapsto\chi_n
\]

을 증명한 뒤

\[
\varprojlim_n\chi_n=\chi
\]

를 theorem으로 고정한다.

### Priority 2 — projective jet의 categorical minimality

현재 projective relation jet이 **충분하다**는 것은 확인되었지만,

> 이것보다 약한 자연스러운 carrier로는 \(\chi\bmod9\)를 복원할 수 없다.

를 categorical하게 증명하는 것은 아직 OPEN이다.

여기서 “minimal”이라는 표현은 실제 정의와 forgetful category를 먼저 고정한 뒤 사용해야 한다. 단순히 더 작은 벡터공간이라는 의미로 쓰면 안 된다.

### Priority 3 — finite bounded-degree jet으로 full \(\chi\)가 가능한가

가능하다면 훨씬 강한 결과가 되고, 불가능하다면 무한 tower의 본질적 필요성을 보여주는 obstruction theorem이 된다.

## 11. 이후 연구 원칙

- 이미 CLOSED된 \(\Delta_q\), failed lift-dependent scalar 등의 경로를 임의로 부활시키지 않는다.
- “q=3이라는 답을 datum 정의에 미리 넣는” 후보는 인정하지 않는다.
- 새로운 계산보다 먼저 **정의 → intrinsicity → factorization → q-separation → recovery** 순서를 확인한다.
- finite scan은 definition gate가 통과된 뒤에만 허용한다.
- full tower 결과와 finite-level theorem을 구별한다.
- projective jet의 “minimality”는 증명되기 전까지 후보/OPEN으로만 기록한다.

## 12. 중간평가 결론

\[
\boxed{
\begin{array}{c}
\text{bare graded data: insufficient}\\
\downarrow\\
\text{projective degree-(2,3) relation jet: }\chi\bmod9\text{ recoverable}\\
\downarrow\\
\text{compatible full filtered relation-jet tower: full }\chi\text{ recoverable}\\
\downarrow\\
\text{remaining problem: minimality + finite-level theorem}
\end{array}}
\]

**중간평가 한 문장 결론:**

> **“canonical orientation을 filtered data에서 복원할 수 있는가?”라는 핵심 재구성 질문에는 긍정적인 답이 확보되었지만, 그 결과의 진짜 수학적 무게를 결정할 ‘얼마나 적은 intrinsic enriched data가 충분한가?’라는 최소성 문제는 아직 열려 있다.**

이 문서는 2026-09-19 시점의 연구 중간평가이며, 이후 새 결과가 나오면 이 문서를 덮어쓰기보다 새로운 날짜의 평가/로그 항목으로 연속성을 유지한다.
