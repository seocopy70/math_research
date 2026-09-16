# A3-4-11 검증 기록 — 2026-09-16

## 1. GitHub Actions 확인

2026-09-16에 GitHub Actions 실행 `35059808169` 및 `35060090291`을 직접 확인했다.

두 실행 모두 실제 checkout 후 실행된 파일은

`research/phase2_24_A3_4_11_L5_obstruction_compression_2026-09-16.py`

이며 둘 다 `failure`로 종료되었다.

특히 run `35060090291`은 commit `cbad01e8f586272955de87c27924ed615719d91e`를 checkout했다.

## 2. 실패 원인

실행 로그에서 다음 차원 오류가 발생했다.

- `D_L5`: 816 rows = `L5^4`의 4개 204차원 block
- `R5_L5`: 204 rows = `L5` 하나의 공간

기존 코드가

`np.column_stack([D_L5, R5_L5])`

를 수행하면서 `816 != 204`로 `ValueError`가 발생했다.

따라서 이 실행은 A3-4-11의 최종 수학적 판정을 내릴 수 있는 실행이 아니다. 이는 수학적 반례가 아니라 검증 코드의 차원 embedding 오류이다.

## 3. 실행에서 확인된 선행 결과

실패 전까지 다음은 정상적으로 계산되었다.

- `dim L5 = 204`
- obstruction의 L5 압축 rank = 45
- L5 basis construction 완료
- L5 left inverse construction 완료
- L5 action matrices construction 완료

또한 이전 단계의 검증 로그에서 `dim W = 45`, `W^{Sp4(F3)} = 0`, `dim End_H(W)=2` 및 A3-4-10의 ambient bracket compatibility 결과가 계산되었으나, 이번 A3-4-11 최종 검증과는 별도로 취급한다.

## 4. 중요한 상태 차이

현재 GitHub main의 `phase2_24_A3_4_11_L5_obstruction_compression_2026-09-16.py`에는 이미 수정된 embedding 코드가 존재한다.

수정 내용은 각 `[(R)_4, X_i]` 관계 벡터를 `L5^4`의 해당 generator block에 삽입하여 `R5_L5_4`라는 `(4*dim_L5) x 20 = 816 x 20` 행렬을 구성한 뒤 `D_L5`와 결합하는 것이다.

하지만 실패한 Actions 실행은 수정 이전 commit을 checkout했기 때문에 이 수정 코드를 실행하지 않았다.

## 5. 다음 검증 절차

1. 수정된 코드를 명시적으로 phase2_25 검증 실행으로 고정한다.
2. GitHub Actions에서 phase2_25가 실제 checkout되어 실행되는지 먼저 확인한다.
3. 다음을 순서대로 확인한다.
   - `[L2,(R)_3] subset [L1,(R)_4]`
   - `[L3,R] subset [L1,(R)_4]`
   - 세 공간의 합 rank = 20
   - 두 independent `(R)_4` basis 선택에서도 rank = 20
   - `(R)_5 = [L1,(R)_4]`
   - `Im Phi intersect (R)_5^4 = 0`
4. 각 결과를 로그와 함께 연구 마스터 기록에 반영한다.

## 6. 현재 결론

**A3-4-11의 최종 수학적 결론은 아직 보류한다.**

현재까지 확정된 것은 '이전 Actions 실행은 코드 차원 오류로 최종 검증에 도달하지 못했다'는 사실과, 수정 코드가 이미 main에 존재한다는 사실이다.
