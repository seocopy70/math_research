# A3-4-20S — Direct MeatAxe socle vs Q-kernel/image comparison

## 목적
A3-4-20R에서 확인한 `Q`-defined simple submodules가 실제 Jacobson socle과 동일한 공간인지 직접 검증한다. A3-4-18의 MeatAxe `BasisSocle` 계산을 다시 독립적으로 수행하고, 그 실제 socle의 **벡터공간**을 A3-4-20R에서 복원한 `ker(Q)` 및 `im(Q)`와 비교한다.

## 배경
A3-4-20은
\[
\operatorname{rad}(M):=\sum_g\operatorname{im}(g-I),\qquad
\operatorname{soc}(M):=\bigcap_g\ker(g-I)
\]
를 radical/socle로 잘못 사용하여 INVALID 처리했다. 후자는 일반적으로 invariant space이고 실제 socle과 같지 않다.

A3-4-20R은 이 정의를 버리고 `ker(Q)`, `im(Q)`와 대응 quotient의 단순성을 직접 검사하여
\[
0\to S_{25}\to B/A\to S_{10}\to0,
\qquad
0\to S_{10}\to K\to S_{25}\to0
\]
를 확정했다.

## 이번 검증
GAP/MeatAxe의 `MTX.BasisSocle`을 실제 socle 계산기로 사용한다.

1. A3-4-16의 동일한 35×35 generator matrices를 재사용한다.
2. A3-4-17과 동일한 선형계에서 유일한 intertwiner `Q`를 정확히 복원한다.
3. `ker(Q)`의 차원 25, `im(Q)`의 차원 10을 독립적으로 확인한다.
4. GAP/MeatAxe에서 `BasisSocle(B/A)`와 `BasisSocle(K)`를 계산한다.
5. 다음 네 가지를 **벡터공간 equality**로 직접 검사한다.
   - `Soc(B/A) = ker(Q)`
   - `Soc(K) = im(Q)`
   - 차원도 각각 25, 10인지 확인
6. 추가로 socle이 전체 module이 아닌지 확인하여 genuine proper socle인지 기록한다.

## 판정 기준
`SOCLE_BA_EQUALS_KER_Q = True` 및 `SOCLE_K_EQUALS_IMAGE_Q = True`이고, 예상 차원(25, 10)이 맞으면 PASS.

이번 검증은 단순성 검사보다 강하다. 단순하다는 사실만 확인하는 것이 아니라, MeatAxe가 계산한 실제 socle과 `Q`가 정의하는 구체적인 부분공간이 동일한지를 직접 비교한다.

## 해석상 주의
이 테스트가 PASS하면 `Q`의 kernel/image가 각각 실제 socle layer임을 계산적으로 확정할 수 있다. 이것은 extension의 방향을 더욱 직접적으로 고정한다. 다만 Ext 군의 차원이나 extension class 자체를 계산하는 것은 별도 A3-4-21의 과제로 남긴다.

## 실행 상태
- 설계 기록: 2026-09-17
- 계산: GitHub Actions에서 수행
- PASS/FAIL: 실행 결과로 결정
