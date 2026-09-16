# A3-4-11 검증 기록 — 2026-09-16

## 1. 최초 실패 실행

GitHub Actions 실행 `35059808169` 및 `35060090291`을 확인했다.

두 실행 모두 `research/phase2_24_A3-4-11_L5_obstruction_compression_2026-09-16.py`를 실행했고 실패했다.

`35060090291`은 commit `cbad01e8f586272955de87c27924ed615719d91e`를 checkout했으며, 기존 코드가 `np.column_stack([D_L5, R5_L5])`를 직접 수행하면서 `D_L5 = 816 x 45`, `R5_L5 = 204 x 20`의 row dimension 불일치로 `ValueError`가 발생했다.

이는 수학적 반례가 아니라 `L5^4` 안으로 관계 벡터를 embedding하지 않은 구현 오류였다.

## 2. 수정 내용

수정된 구현에서는 각 `[(R)_4, X_i]` 벡터를 `L5^4`의 해당 generator block에 삽입한다.

생성된 행렬은 `R5_L5_4.shape = (816,20)`이며, 이것을 `D_L5 (816 x 45)`와 결합하도록 수정했다.

또한 `(R)_4`의 표시된 6개 column 중 실제 독립 basis 5개를 먼저 선택하도록 했다.

## 3. 수정 코드의 독립 실행 성공

GitHub Actions run `35060519753` (`TEMP A3-4-11 verify`, run number 6)을 확인했다.

- event: push
- head SHA: `6def50834f8f50770db3e4d0074fca1eb335e1b3`
- conclusion: **success**
- 실제 실행 step: `python research/phase2_24_A3-4-11_L5_obstruction_compression_2026-09-16.py`
- 실행 시간: 약 64초

즉 수정된 `816 x 20` embedding 코드는 실제 GitHub Actions에서 오류 없이 끝까지 실행되었다.

코드 자체에서 `dim L5 = 204`, `D_L5.shape = (816,45)`, rank 보존, lossless reconstruction, H-equivariance, obstruction image rank 45, 독립적인 `(R)_4` basis 5개 선택, `R5_L5_4.shape = (816,20)` 등의 assertion이 통과했다.

따라서 **A3-4-11 L5 compression 구현 오류는 해결되었고, 수정된 계산 자체는 재현 가능한 성공 상태**이다.

## 4. Phase 2-25A 첫 시도와 실패 원인

새 파일 `research/phase2_25_A3-4-11_L5_relation_span_2026-09-16.py`의 첫 설계에서는 다음 포함관계를 assertion으로 강제했다.

- `[L2,(R)_3] ⊂ [L1,(R)_4]`
- `[L3,R] ⊂ [L1,(R)_4]`

실제 Actions 실행 `35061769617` 및 `35061765256`에서 첫 assertion이 실패했다.

이 실패를 코드 버그로 분류하지 않는다. 선행 대수적 논증 자체에 문제가 있었다. 특히 Jacobi 항등식을 이용해

`[[a,b],c] = [a,[b,c]] - [b,[a,c]]`

를 전개할 때 `c in (R)_3`이고 `c=[a',r]`인 경우

`[a,[a',r]] = [[a,a'],r] + [a',[a,r]]`

가 되어 `[L2,R]` 형태의 추가 항이 나타난다. 따라서 이전 논증은 `[L2,R] ⊂ [L1,(R)_4]`에 해당하는 추가 사실을 암묵적으로 필요로 했으며, 그것을 증명하지 않았다.

결론적으로:

- `dim [L1,(R)_4] = 20`이라는 기존 독립 계산은 유지한다.
- `[L2,(R)_3] ⊂ [L1,(R)_4]`는 현재 증명된 사실로 취급하지 않는다.
- 같은 이유로 degree-5 후보 공간들 사이의 다른 포함도 사전에 가정하지 않는다.
- 기존에 사용했던 `20`이라는 목표 차원도 선험적으로 강제하지 않는다.

## 5. Phase 2-25A 재설계 — 세 조각 직접 생성 및 concatenate

사용자의 수학적 수정에 따라 Phase 2-25A를 정공법으로 재설계했다.

`(R)_2 = <R>`이고 `(R)_1 = 0`이므로 degree-5에서 실질적으로 살아있는 후보는

`[L1,(R)_4]`, `[L2,(R)_3]`, `[L3,R]`

세 조각이다. `[L4,(R)_1]`은 0이므로 계산에서 제외한다.

핵심 원칙은 **어느 세 조각도 서로에게 포함된다고 가정하지 않는 것**이다. 세 공간을 모두 실제로 구성하여 동일한 `L5` 좌표계로 옮긴 다음 하나의 행렬로 concatenate하고 rank를 계산한다.

따라서 combined rank가 20이든 40이든, 또는 다른 값이든 그것 자체를 계산 결과로 받아들인다. 이전의 잘못된 포함관계 때문에 특정 값과 모순된다고 판단하지 않는다.

실제 `(R)_5^4`는 이 combined rank가 확정된 뒤 그 basis를 4개의 독립 block으로 복제하여 `L5^4` 안에 구성한다. 그 다음 `Im(Phi)`와 합공간 rank를 계산하여

`dim(Im(Phi) intersection (R)_5^4)`

를 직접 산출한다.

## 6. 최종 교정 검증 — true recursive R5

GitHub Actions run `35071437950`, job `104713654784`가 **success**로 완료되었다. checkout된 head SHA는 `2b0a80b7d8484c863d206cb85bd16ab59c836606`이다.

실제 실행에서 true recursive relation을 처음부터 재구성했고 다음을 확인했다.

- `dim L4 = 60`
- `dim (R)_3 = 4`
- `dim (R)_4 = 15`
- `dim Q4 = 45`
- `rank(R4) = 15`
- `rank([R4 | gT-T]) = 16`
- `dim L5 = 204`
- `dim TRUE (R)_5 = 60`

A3-4-10 obstruction은 corrected calculation에서 다시 생성되었으며:

- `A3-4-10 obstruction rank in L5^4 = 45`
- `dim Hom(V,(R)_5) = 240`
- `rank(obstruction + Hom(V,R5)) = 285`
- `dim(Im(Delta) intersect Hom(V,R5)) = 0`

이다.

따라서

`45 + 240 - 285 = 0`

으로도 교집합 차원이 독립적으로 확인된다.

또한 `(R)_5`의 H-stability defects는 `[0, 0, 0, 0, 0]`으로, 사용한 5개 `Sp_4(F_3)` 생성자에 대해 H-stability가 확인되었다.

최종 출력:

`SANITY CHECK PASSED: intersection dimension is compatible with the known W45 submodule dimensions.`

`ALL A3-4-11 TRUE-R5 CHECKS PASSED`

## 7. 최종 수학적 결론

이번 검증에서 확정된 것은 다음이다.

\[
\boxed{\dim\bigl(\operatorname{Im}\Delta\cap\operatorname{Hom}(V,(R)_5)\bigr)=0.}
\]

즉 degree-5로 올라간 ambient bracket obstruction의 45차원 부분은 true relation space `(R)_5`에 의해 하나도 소거되지 않는다.

이는 단순한 associative word-space 계산이 아니다. degree-5 Lie space `L5`를 실제로 구성하여 204차원으로 압축한 뒤, true recursive relation `(R)_5`의 60차원 공간과 비교한 결과이다.

또한 A3-4-10에서 확인된

\[
\operatorname{Im}\Delta\cong W_{45}
\]

는 `Sp_4(F_3)`-module 관점의 사실이고, 이번 A3-4-11은 그 image가 degree-5 relation space에 묻히는지를 검사한다. 결과는 그렇지 않음(교집합 0)이다.

따라서 현재 단계의 정확한 표현은:

> degree 4에서 `W45`와 `Wd`는 추상적인 `Sp_4(F_3)`-module로 동형이지만, 그 동형을 ambient Lie bracket과 호환시키려 할 때 생기는 45차원 degree-5 obstruction은 true relation space `(R)_5` 안으로 하나도 들어가지 않는다.

이 결과만으로 곧바로 “q가 검출된다” 또는 “canonical orientation이 복원된다”고 결론내리지 않는다. 다음 단계에서는 이 45차원 obstruction이 `L5/(R)_5` 안에서 어떤 `Sp_4(F_3)`-module 구조와 위치를 갖는지 분석해야 한다.

## 8. 다음 단계

다음 계산의 목표는

\[
\operatorname{Im}\Delta\subset L_5^4
\]

를 relation quotient 관점에서 분석하는 것이다. 특히 다음을 확인한다.

1. `Im(Delta)`가 H-stable한 45차원 module이라는 사실의 독립 확인.
2. `(R)_5`를 quotient하여 얻는 `L5/(R)_5`에서 obstruction image의 module 구조 확인.
3. obstruction의 composition factors 또는 자연스러운 filtration 위치 확인.
4. 가능하면 degree-5 obstruction이 `q`에 의해 어떻게 달라지는지 직접 비교.

### 해석상의 주의

이전 단계에서 얻은

`0 ⊂ im(N) ⊂ ker(N) ⊂ W45`

의 차원 `0,10,35,45`만으로 W45의 모든 H-submodule이 이 네 차원뿐이라고 단정하지 않는다. `End_H(W45) ≅ F_3[epsilon]/(epsilon^2)` 역시 endomorphism algebra에 관한 결과이지 전체 submodule lattice를 자동으로 결정하지 않는다.

따라서 이번 교집합 차원 0은 실제 계산 결과로 기록하되, 그 결과를 submodule-lattice에 관한 선험적 가정으로 정당화하지 않는다.
