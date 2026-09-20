# HARD ATTACK 44 — Q_2 LOW-DEGREE COHOMOLOGY: STRUCTURAL REDUCTION BEFORE COMPUTATION

Date: 2026-09-20

## Target
Hard Attack 43 fixed the next target: understand H^*(Q_2,F_3) in degrees 2 and 3 well enough to control beta_rho^2 without a broad rho-scan.

## 1. Finite quotient structure

For the lower 3-central series P_1=G, P_2=G^3[G,G], P_3=P_2^3[P_2,G], the quotient Q_2=G/P_3 is class-2. Modulo P_3, commutators and cubes from P_2 are central.

For the frozen relation x_1^3[x_1,x_2][x_3,x_4]=1, the degree-two central relation identifies the cube direction of x_1 with the symplectic commutator combination. Thus Q_2 is not an arbitrary class-2 3-group: it is a central extension of V=G/P_2 ≅ F_3^4 by W=P_2/P_3, with the extension class carrying the quadratic commutator form together with the p-power map.

The key point is that the q=3 information is already visible in the extension law of Q_2, even though the selected finite quotient is q-blind at the level relevant to the earlier information-boundary theorem. Therefore one must distinguish the abstract group Q_2 from the pointed extension data (Q_2,M_2,E_2).

## 2. Cohomological consequence

The central extension
0 -> W -> Q_2 -> V -> 0
gives an LHS spectral sequence
E_2^{i,j}=H^i(V,H^j(W,F_3)) => H^{i+j}(Q_2,F_3).

Since W is central, the V-action on H^j(W,F_3) is trivial. The differentials are nevertheless nontrivial and are controlled by the extension class. Consequently, H^2(Q_2,F_3) and H^3(Q_2,F_3) cannot be recovered from the vector spaces V and W alone; the extension class is essential.

This is important for the selector program: the ambient coefficient term is not merely an unrelated finite-group invariant. At low degree it is already sensitive to the same central-extension geometry that underlies e_2.

## 3. Bockstein-twist interpretation

For rho mod 9, put lambda=(rho-1)/3 in H^1(Q_2,F_3). The twisted connecting operator is
d_lambda = beta + lambda cup(-)
on mod-3 cohomology.

Because rho itself is a character Q_2 -> (Z/9)^×, lambda lifts through Z/9. Hence beta(lambda)=0. For odd p, lambda cup lambda=0 in mod-3 cohomology. Therefore d_lambda^2=0, as required for the connecting construction.

This gives a useful structural reinterpretation:
the ambient H^2(A_2(rho)) calculation is the degree-two cohomology of the twisted Bockstein complex (H^*(Q_2,F_3),d_lambda), together with the exact-sequence indexing already established in HA42.

Thus beta_rho^2 is not an arbitrary second matrix. It is the degree-two component of the same square-zero differential whose degree-one component is the intrinsic Theta_(R,p).

## 4. New boundary and new possibility

The central-extension spectral sequence shows why beta_rho^2 might eventually be controllable from e_2, but it does NOT yet prove that it is determined by the degree-(2,3) shadow (R,p).

There are two distinct levels:

(A) e_2 controls the LHS differentials and hence the full low-degree cohomology of Q_2.

(B) (R,p) is only the scalar transgression shadow of e_2.

Therefore a theorem of the form beta_rho^2=F(R,p,lambda) would be a genuine compression theorem. It cannot be assumed from HA41.

## 5. Strongest next calculation

The next attack should not enumerate rho. It should compute the LHS transgression data for the central extension Q_2 at the minimal degrees contributing to total degrees 2 and 3.

Concretely:
- identify the extension map / k-invariant W -> H^2(V,F_3);
- determine d_2 on E_2^{0,1} and E_2^{1,1};
- determine which degree-three classes survive;
- express beta_rho^2 in those surviving generators.

The desired outcome is one of three:

1. **Collapse:** beta_rho^2 is forced by the same scalar pair (R,p). This would sharply strengthen the selector program.

2. **Controlled enrichment:** beta_rho^2 needs an additional but still intrinsic low-degree invariant of e_2. This gives the true minimal ambient layer.

3. **Independence:** beta_rho^2 contains genuinely new finite-quotient information not recoverable from the extension shadow used for mod 9. Then the coker selector requires a richer carrier.

No broad rho-scan is authorized.

## 6. Decision

**PASS / STRUCTURAL REDUCTION:** Q_2 should be attacked as a central extension V <- Q_2 -> W, not as a black-box finite group.

**PASS / STRUCTURAL:** the twisted Bockstein is a square-zero differential d_lambda=beta+lambda cup(-) for the admissible lambda.

**OPEN / LOAD-BEARING:** explicit LHS low-degree calculation and determination of beta_rho^2.

**OPEN / DECISIVE:** whether the resulting beta_rho^2 is determined by (R,p) or requires a richer intrinsic shadow of e_2.

No selector claim and no numerical rho-scan follows from this attack.
