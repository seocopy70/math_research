# A3-4-10: Q4 내 배치(placement)와 좌표 의존성에 대한 해석 유보

## 2026-09-16 연구 기록

### 1. 현재까지 확정된 계산

참조 검증: `A3-4-TAU_H_EQUIVARIANCE_COORDSAFE_2026-09-16.py`

- `dim L4 = 60`
- `dim (R)_4 = 15` (true recursive relation)
- `dim Q4 = 45`
- `dim W45 = 45`
- `dim Wd = 45`
- `dim I = dim(W45 ∩ Wd) = 35`
- `pi|W45`와 `pi|Wd`는 각각 Q4로 가는 동형사상
- `tau = (pi|Wd)^(-1) o pi|W45`는 rank 45
- 5개 생성원에 대해 direct/induced Wd action residual rank = 0
- 5개 생성원에 대해 tau equivariance residual rank = 0
- I의 H-stability defect rank = 0
- D_i restricted to I rank = 0
- 따라서 `tau`는 `H = Sp4(F3)`-equivariant이고 W45와 Wd는 H-module로 동형이다.

### 2. 해석상 중요한 유보

위 결과만으로 다음 문장을 최종 결론으로 확정해서는 안 된다:

> “q는 degree 4에서 보이지 않는다.”

확정된 것은 **추상적인 H-module 동형류가 동일하다**는 사실이다.

실제로 W45와 Wd는 L4 안에서 같은 부분공간이라고 확인된 것이 아니다. 오히려

`dim(W45 ∩ Wd) = 35 < 45`

이므로 서로 다른 45차원 부분공간이며, 공통 부분공간은 35차원이다.

따라서 q의 정보가 module isomorphism class가 아니라 `Q4` 또는 `L4` 안에서 두 copy가 배치되는 방식에 남아 있을 가능성을 열어둔다.

### 3. 핵심 사영 구조

`pi : L4 -> Q4 = L4/(R)_4`는 H-equivariant projection이다. `(R)_4`가 H-invariant이기 때문이다.

따라서

`phi_W = pi|W45 : W45 -> Q4`

`phi_d = pi|Wd : Wd -> Q4`

는 각각 H-module isomorphism이다.

이 둘의 비교가 바로

`tau = phi_d^(-1) o phi_W`

이다.

현재 계산에서 tau가 H-equivariant임은 확인되었지만, 이것만으로 phi_W 또는 phi_d가 어떤 외부적으로 정해진 '표준 좌표계'와 일치하는지는 아직 말하지 않는다.

### 4. 다음 확인 항목

R5 계산과 병행 또는 그 직전에 다음을 별도 검토한다.

1. true `(R)_4`를 이용해 Q4의 canonical computational coordinate system을 명시한다.
   - canonical 15D R4 basis
   - 그 complement/quotient section
   - 또는 선택된 45 ambient coordinate rows를 이용한 quotient coordinate map

2. `phi_W`와 `phi_d`를 동일한 Q4 좌표계에서 명시적으로 행렬화한다.

3. 그 결과 두 사영 동형사상이 동일한지, 또는 Q4의 H-equivariant automorphism으로 서로 다른지를 확인한다.

4. 특히
   `A_Q = phi_d o phi_W^{-1}`
   를 계산하고
   - `A_Q = I`인지
   - `A_Q != I`이지만 H-equivariant인지
   를 구분한다.

5. `A_Q != I`이면 이것은 module isomorphism class의 차이가 아니라 Q4 안에서 두 realization이 서로 다른 위치/좌표를 갖는다는 증거가 된다. 이것이 q 정보인지 여부는 이후 R5/Filtration 데이터와 연결해서 판단한다.

### 5. 중요한 주의

현재의 `tau`는 W45 -> Wd 사이의 지도이고, `A_Q`는 Q4 -> Q4 사이의 지도이다. 둘은 식별을 통해 연결되지만 좌표계를 혼동해서는 안 된다.

또한 `tau|I = id`는 I가 tau의 fixed-point subspace에 포함됨을 뜻할 뿐이며, fixed-point subspace가 정확히 I라는 결론은 별도의 계산 없이는 내리지 않는다.

### 6. 연구 방향

따라서 현재의 안전한 결론은 다음과 같다.

> degree 4에서 W45와 Wd는 동일한 추상적인 `Sp4(F3)`-module 구조를 가지며, 두 realization 사이의 canonical map tau도 H-equivariant이다. 그러나 두 submodule이 Q4/L4 안에서 어떻게 배치되는지에 관한 정보까지 소거되었다고 결론내리지는 않는다. Q4의 공통 기준 좌표에서 두 사영 동형사상의 상대적 automorphism을 확인한 뒤 R5 단계로 넘어간다.

R5 단계의 핵심 검증인 `Im Phi ∩ (R5)^4`는 이 placement 정보와 별개로 계속 진행할 수 있으며, 최종적인 q-sensitive obstruction 여부는 R5/이후 층위에서 판단한다.
