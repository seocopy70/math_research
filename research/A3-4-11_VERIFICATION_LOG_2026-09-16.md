# A3-4-11 검증 기록 — 2026-09-16

## 1. 최초 실패 실행

GitHub Actions 실행 `35059808169` 및 `35060090291`을 확인했다.

두 실행 모두 `research/phase2_24_A3_4_11_L5_obstruction_compression_2026-09-16.py`를 실행했고 실패했다.

`35060090291`은 commit `cbad01e8f586272955de87c27924ed615719d91e`를 checkout했으며, 기존 코드가

`np.column_stack([D_L5, R5_L5])`

를 직접 수행하면서 `D_L5 = 816 x 45`, `R5_L5 = 204 x 20`의 row dimension 불일치로 `ValueError`가 발생했다.

이는 수학적 반례가 아니라 `L5^4` 안으로 관계 벡터를 embedding하지 않은 구현 오류였다.

## 2. 수정 내용

수정된 구현에서는 각 `[(R)_4, X_i]` 벡터를 `L5^4`의 해당 generator block에 삽입한다.

생성된 행렬은

`R5_L5_4.shape = (816, 20)`

이며, 이것을 `D_L5 (816 x 45)`와 결합하도록 수정했다.

또한 `(R)_4`의 표시된 6개 column 중 실제 독립 basis 5개를 먼저 선택하도록 했다.

## 3. 수정 코드의 독립 실행 성공

GitHub Actions run `35060519753` (`TEMP A3-4-11 verify`, run number 6)을 확인했다.

- event: push
- head SHA: `6def50834f8f50770db3e4d0074fca1eb335e1b3`
- conclusion: **success**
- 실제 실행 step: `python research/phase2_24_A3_4_11_L5_obstruction_compression_2026-09-16.py`
- 실행 시간: 약 64초

즉 수정된 `816 x 20` embedding 코드는 실제 GitHub Actions에서 오류 없이 끝까지 실행되었다.

코드 자체에서 다음 assertion들이 통과했다.

- `dim L5 = 204`
- `D_L5.shape = (816,45)`
- `rank_D_associative == rank_D_L5`
- L5 projection의 lossless reconstruction
- 5개 generator에 대한 H-equivariance
- obstruction image rank = 45
- 독립적인 `(R)_4` basis 5개 선택
- `R5_L5_4.shape = (816,20)`
- obstruction image와 local degree-5 relation span의 intersection dimension이 허용 범위 안에 있음

따라서 **A3-4-11 L5 compression 구현 오류는 해결되었고, 수정된 계산 자체는 재현 가능한 성공 상태**이다.

## 4. 그러나 아직 확정하지 않은 것

이번 성공 실행은 A3-4-11의 'L5 obstruction compression 및 local relation span' 검증이다.

다음 명제들은 별도 계산이 필요하며 아직 이 로그로 확정하지 않는다.

1. `[L2,(R)_3] ⊂ [L1,(R)_4]`
2. `[L3,R] ⊂ [L1,(R)_4]`
3. 세 공간을 합친 rank가 정확히 `20`
4. `(R)_4`의 두 다른 독립 basis 선택 `[0,1,2,3,4]`, `[1,2,3,4,5]`에서도 동일하게 rank `20`
5. `(R)_5 = [L1,(R)_4]`의 정확한 차원/동일성 확인
6. `Im Phi ∩ (R)_5^4 = 0`

특히 현재 성공한 run의 `ALL A3-4-11 CHECKS COMPLETED`는 위 1~6 전체를 의미하는 것이 아니라, **해당 phase2_24 스크립트에 구현된 체크들이 모두 통과했다는 뜻**으로 제한해서 해석한다.

## 5. 현재 연구 상태

- 코드 차원 오류: **해결**
- L5 compression: **검증 성공**
- obstruction image의 rank 45 및 H-equivariance: **검증 성공**
- 사용자가 지정한 rank-20 / 두 basis / `(R)_5` / intersection-zero 최종 묶음: **다음 단계**

따라서 다음 단계는 이 성공한 기반 위에서 위 1~6을 직접 계산하는 `phase2_25`를 실행하고, 그 로그에서 각 조건을 개별적으로 판정하는 것이다.
