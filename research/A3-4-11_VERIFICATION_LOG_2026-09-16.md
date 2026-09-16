# A3-4-11 검증 기록 — 2026-09-16

## 1. 최초 실패 실행

GitHub Actions 실행 `35059808169` 및 `35060090291`을 확인했다.

두 실행 모두 `research/phase2_24_A3_4_11_L5_obstruction_compression_2026-09-16.py`를 실행했고 실패했다.

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
- 실제 실행 step: `python research/phase2_24_A3_4_11_L5_obstruction_compression_2026-09-16.py`
- 실행 시간: 약 64초

즉 수정된 `816 x 20` embedding 코드는 실제 GitHub Actions에서 오류 없이 끝까지 실행되었다.

코드 자체에서 `dim L5 = 204`, `D_L5.shape = (816,45)`, rank 보존, lossless reconstruction, H-equivariance, obstruction image rank 45, 독립적인 `(R)_4` basis 5개 선택, `R5_L5_4.shape = (816,20)` 등의 assertion이 통과했다.

따라서 **A3-4-11 L5 compression 구현 오류는 해결되었고, 수정된 계산 자체는 재현 가능한 성공 상태**이다.

## 4. Phase 2-25A 첫 시도와 실패 원인

새 파일 `research/phase2_25_A3_4_11_L5_relation_span_2026-09-16.py`의 첫 설계에서는 다음 포함관계를 assertion으로 강제했다.

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

## 6. 현재 코드 상태

재설계된 파일:

`research/phase2_25_A3_4_11_L5_relation_span_2026-09-16.py`

새 commit:

`91e95052290b2383f077bc0b956874fd36a7bfce`

변경 핵심:

1. `[L2,(R)_3]` 및 `[L3,R]`에 대한 inclusion assertion 제거.
2. 세 조각을 독립적으로 계산.
3. 세 행렬을 concatenate하여 `DIM_R5_FROM_GENERATORS`를 직접 계산.
4. 그 값이 무엇이든 사전 목표값과 비교하여 실패시키지 않음.
5. combined basis를 이용해 `(R)_5^4`를 구성.
6. `Im(Phi)`와의 교집합 차원을 계산.
7. 두 명시적 `(R)_4` basis 후보 `[0,1,2,3,4]`, `[1,2,3,4,5]`는 독립성 및 생성 rank를 별도로 보고하되 canonical 계산을 변경하지 않음.

## 7. 다음 검증

다음은 수정된 commit에 대한 GitHub Actions 실제 실행이다. 특히 다음 수치를 그대로 기록해야 한다.

- `dim [L1,(R)_4]`
- `dim [L2,(R)_3]`
- `dim [L3,R]`
- 세 조각의 combined rank = 계산된 `dim (R)_5`
- `(R)_5^4` rank
- `rank(ImPhi + (R)_5^4)`
- `dim(ImPhi intersection (R)_5^4)`

**중요:** combined rank가 20/40/기타 값으로 나오더라도, 그 자체를 버그의 증거로 간주하지 않는다. 먼저 실제 선형대수 결과를 확정하고, 그 다음 수학적 의미를 분석한다.
