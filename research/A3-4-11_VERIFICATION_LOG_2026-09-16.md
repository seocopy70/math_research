# A3-4-11 검증 기록 — 2026-09-16

## 1. 최초 실패 실행

GitHub Actions 실행 `35059808169` 및 `35060090291`을 확인했다.

두 실행 모두 `research/phase2_24_A3_4_11_L5_obstruction_compression_2026-09-16.py`를 실행했고 실패했다.

`35060090291`은 commit `cbad01e8f586272955de87c27924ed615719d91e`를 checkout했으며, 기존 코드가 `np.column_stack([D_L5, R5_L5])`를 직접 수행하면서 `D_L5 = 816 x 45`, `R5_L5 = 204 x 20`의 row dimension 불일치로 `ValueError`가 발생했다.

이는 수학적 반례가 아니라 `L5^4` 안으로 관계 벡터를 embedding하지 않은 구현 오류였다.

## 2. 수정 내용

수정된 구현에서는 각 `[(R)_4, X_i]` 벡터를 `L5^4`의 해당 generator block에 삽입한다.

생성된 행렬은 `R5_L5_4.shape = (816, 20)`이며, 이것을 `D_L5 (816 x 45)`와 결합하도록 수정했다.

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

## 4. 아직 확정하지 않은 것

이번 성공 실행은 A3-4-11의 'L5 obstruction compression 및 local relation span' 검증이다. 다음 명제들은 별도 계산이 필요하며 아직 이 로그로 확정하지 않는다.

1. `[L2,(R)_3] ⊂ [L1,(R)_4]`
2. `[L3,R] ⊂ [L1,(R)_4]`
3. 세 공간을 합친 rank가 정확히 `20`
4. `(R)_4`의 두 다른 독립 basis 선택 `[0,1,2,3,4]`, `[1,2,3,4,5]`에서도 동일하게 rank `20`
5. `(R)_5 = [L1,(R)_4]`의 정확한 차원/동일성 확인
6. `Im Phi ∩ (R)_5^4 = 0`

특히 기존 성공 run의 `ALL A3-4-11 CHECKS COMPLETED`는 위 1~6 전체를 의미하는 것이 아니라, **해당 phase2_24 스크립트에 구현된 체크들이 모두 통과했다는 뜻**으로 제한해서 해석한다.

## 5. Phase 2-25 실험 재설계 — 2026-09-16

위 차원 불일치를 계기로 다음 단계는 두 층으로 분리하기로 했다.

### Phase 2-25A: 순수 `L5` 내부에서 `(R)_5` 확정

`L5`는 차원 204이므로, 먼저 모든 degree-5 관계 후보를 동일한 `L5` 좌표계로 옮겨 비교한다. `(R)_5`의 차원을 20 또는 40 등으로 사전에 가정하지 않는다.

새 실행 파일:

`research/phase2_25_A3_4_11_L5_relation_span_2026-09-16.py`

계산 항목:

- `(R)_3 = [L1,R]`의 rank
- `[L2,(R)_3]`의 rank 및 `[L1,(R)_4]` 안으로의 포함 여부
- `L3 = [L1,L2]`의 rank
- `[L3,R]`의 rank 및 `[L1,(R)_4]` 안으로의 포함 여부
- `[L1,(R)_4]`의 rank
- 세 공간의 combined rank
- 두 개의 명시적 `(R)_4` basis 선택 `[0,1,2,3,4]`, `[1,2,3,4,5]`에 대한 독립성 및 생성 rank

### Phase 2-25B: `L5^4`에서 obstruction과 `(R)_5^4` 비교

Phase 2-25A에서 `(R)_5`의 실제 rank를 확정한 뒤에만

`(R)_5^4 = (R)_5 ⊕ (R)_5 ⊕ (R)_5 ⊕ (R)_5 ⊂ L5^4`

를 구성한다. 그 후 `Im Phi`와 같은 816차원 ambient space에서 합공간 rank와 교집합 차원을 계산한다.

목표 검증식은 `dim(Im Phi ∩ (R)_5^4) = 0`이다.

## 6. Phase 2-25 코드/워크플로 기록

새 순수 L5 계산 코드가 commit `a392cd0b3d586204fcecdd514c240e9ffbad5095`에 추가되었다.

Actions entrypoint는 commit `9329bf20e24a43fe2cc4dc4b259cb60ad7eb91b1`에서 기존 phase2_24 wrapper가 아니라 새 순수 L5 검증 파일을 실행하도록 수정했다.

Workflow는 commit `e58338370efe7affe083d7f29c02322a7cbd47eb`에서 새 Phase 2-25 파일을 trigger 대상으로 명시했다.

**중요:** 현재 이 기록 시점에는 Phase 2-25의 실제 Actions 계산 결과를 아직 수치적으로 판정하지 않았다. 코드 작성/워크플로 연결과 기록까지만 완료된 상태이며, 다음 단계는 실제 Actions 실행 로그를 확인하는 것이다.
