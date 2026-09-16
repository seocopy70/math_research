# A3-4-4 — d = [X1^[3], X2]의 Sp4(F3)-orbit module

## 1. 목적

A3-4-3에서

\[
d=[X_1^{[3]},X_2]=\operatorname{ad}(X_1)^3(X_2)
\]

에 대하여

\[
d\notin (R)_4+W_{45}
\]

가 확인되었다. 다음 단계에서는 1차원 공간 $\langle d\rangle$의 불변성을 묻지 않고, 처음부터

\[
W_d:=\langle Sp_4(\mathbb F_3)\cdot d\rangle
\]

를 만들어 표현론적으로 분석한다.

## 2. 구현

- 기존 `phase2_1_invariant_space_verification_2026-09-15.py`의 동일한 $\mathbb F_3$ word basis, relation space $(R)_4$, $Sp_4(\mathbb F_3)$의 5개 생성자를 그대로 재사용한다.
- $d$는
  \[
  [X_1^{[3]},X_2]=\operatorname{ad}(X_1)^3(X_2)
  \]
  로 직접 계산하고 두 표현의 동일성을 assertion으로 확인한다.
- 생성자에 의한 orbit closure를 계산하여 $Sp_4(\mathbb F_3)$-orbit을 완성한다.
- orbit span $W_d$의 ambient $L_4$ 차원, $W_{45}+W_d$, $(R)_4+W_d$, $(R)_4+W_{45}+W_d$의 rank를 계산한다.
- $Q_4=L_4/(R)_4$에서의 image dimension도 별도로 계산한다.

## 3. 계산 결과

GitHub Actions run 35043611873에서 실제 계산이 성공적으로 완료되었다.

\[
\dim (R)_4=5,
\qquad \dim W_{45}=45,
\qquad \dim Q_4=55.
\]

$ d\neq0 $이고, $d$의 orbit 크기는

\[
|Sp_4(\mathbb F_3)\cdot d|=360.
\]

orbit span은

\[
\boxed{\dim W_d=45}.
\]

또한

\[
\dim(W_{45}+W_d)=55,
\]

\[
\dim(W_{45}\cap W_d)=45+45-55=35.
\]

관계공간과의 결합은

\[
\dim((R)_4+W_d)=50,
\]

\[
\dim((R)_4+W_{45}+W_d)=60.
\]

따라서 $L_4$에서 $R_4+W_{45}+W_d$는 전체 degree-4 Lie 공간을 채운다.

$Q_4$로 내려가면

\[
\dim \overline{W}_{45}=45,
\qquad
\dim \overline{W}_d=45,
\]

그리고

\[
\boxed{\dim(\overline{W}_{45}+\overline{W}_d)=55=\dim Q_4}.
\]

즉

\[
\boxed{Q_4=\overline{W}_{45}+\overline{W}_d}.
\]

두 image의 교집합은 차원 35이다.

## 4. 불변성

$W_d$는 orbit span 자체로 정의되므로 $Sp_4(\mathbb F_3)$-불변이다. 실제 구현의 첫 실행 버전에서는 각 생성자가 모든 orbit vector를 다시 $W_d$ 안으로 보내는 rank certificate까지 명시적으로 검사했으며, `W_d_is_Sp4_invariant = True`를 얻었다.

## 5. 중요한 구조적 결과

A3-4-3에서 $d$가 기존 $W_{45}$ 바깥에 있다는 것과 결합하면, 이번 결과는 단순히 '새로운 벡터 하나가 발견되었다'는 수준을 넘는다.

$Q_4$ 안에 서로 다른 두 개의 45차원 $Sp_4(\mathbb F_3)$-불변 부분공간

\[
\overline{W}_{45},\qquad \overline{W}_d
\]

가 존재하며,

\[
\dim(\overline{W}_{45}\cap\overline{W}_d)=35,
\]

\[
\dim(\overline{W}_{45}+\overline{W}_d)=55.
\]

따라서 이 둘이 합쳐져 $Q_4$ 전체를 생성한다.

또한

\[
\dim((R)_4+W_d)=5+45=50
\]

이므로 $W_d\cap (R)_4=0$이다. 따라서 $W_d$는 $Q_4$에서 그대로 45차원으로 내려간다.

## 6. 해석상의 주의

이번 결과만으로 $W_{45}$와 $W_d$가 irreducible인지, 서로 동형인지, 또는 $Q_4$가 특정한 짧은 완전열/직합 구조를 갖는다고 결론내리지 않는다.

특히

\[
Q_4=\overline{W}_{45}+\overline{W}_d
\]

은 확인되었지만, 교집합이 35차원이므로 두 공간의 합은 일반적으로 direct sum이 아니다.

다음 단계에서는 이 45차원 두 부분모듈의 **module structure와 교집합의 정체**를 분석해야 한다.

## 7. 재현성

- Script: `research/phase2_17_A3_4_4_X1_power_X2_orbit_module_2026-09-16.py`
- Workflow: `.github/workflows/phase2-17-A3-4-4.yml`
- Successful run: GitHub Actions `35043611873`
- 기준 commit에서 Phase 2-1 baseline도 함께 재검증됨:
  \[
  \dim L_4=60,\quad \dim(R)_4=5,\quad \dim Q_4=55,\quad |Sp_4(\mathbb F_3)|=51840.
  \]
