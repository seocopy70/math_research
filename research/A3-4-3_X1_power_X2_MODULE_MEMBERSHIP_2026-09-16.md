# A3-4-3 — [X1^[3], X2]의 W45 module membership

## 목적

A3-4-2에서 확인한 restricted-power contribution

\[
d=[X_1^{[3]},X_2]=\operatorname{ad}(X_1)^3(X_2)
\]

이 degree-4 class가 기존의

\[
W_{45}=\langle Sp_4(\mathbb F_3)\cdot T\rangle
\subset Q_4=L_4/(R)_4
\]

안에 실제로 들어가는지를 판정한다.

단순히

\[
\operatorname{rank}((R)_4+W_{45}+\langle d\rangle)=50
\]

만 검사하지 않는다. 그 조건은 $d\in (R)_4+W_{45}$만 보장할 뿐, $d\in W_{45}$를 단독으로 보장하지 않는다.

## Certificate

1. Relation ideal 밖:

\[
\operatorname{rank}((R)_4+\langle d\rangle)=6.
\]

2. Combined space membership:

\[
\operatorname{rank}((R)_4+W_{45}+\langle d\rangle)
\stackrel{?}{=}
\operatorname{rank}((R)_4+W_{45})=50.
\]

3. Direct W-membership:

\[
\operatorname{rank}(W_{45}+\langle d\rangle)
\stackrel{?}{=}
\operatorname{rank}(W_{45})=45.
\]

세 번째 조건이 직접적으로

\[
\boxed{d\in W_{45}}
\]

를 판정한다.

## 구현 원칙

- Phase 2-1의 동일한 Q4 / W45 infrastructure를 `runpy`로 재사용한다.
- 동일한 $\mathbb F_3$ word-basis와 commutator convention을 사용한다.
- 새로운 quotient나 좌표계를 임의로 만들지 않는다.
- restricted-Lie sanity check
  \[
  [X_1^{[3]},X_2]=\operatorname{ad}(X_1)^3(X_2)\neq0
  \]
  를 assertion으로 유지한다.

## 해석 분기

- `rank(R4+d)=6`, `rank(R4+W45+d)=50`, `rank(W45+d)=45`이면:
  \[
  d\in W_{45}\setminus(R)_4.
  \]
  즉 surviving $q=3$ contribution이 기존 $W_{45}$ module 내부에 있다.

- `rank(R4+d)=6`, `rank(R4+W45+d)=50`, `rank(W45+d)=46`이면:
  \[
  d\in (R)_4+W_{45},\qquad d\notin W_{45}.
  \]
  즉 relation component와 W component가 섞이는 현상이 존재한다.

- `rank(R4+W45+d)=51`이면 새로운 degree-4 direction이 $R_4+W_{45}$ 밖에서 살아난다.

## 주의

계산 실행 전에는 위 세 결과 중 어느 것도 가정하지 않는다. 특히 rank 50만으로 `$d\in W_{45}$`라고 결론내리지 않는다.
