# Paper 3 independent referee audit — 2026-09-26

## Scope
Audited the exact Paper 3 source after the initial CI build and before the final publication gate. Paper 2 was not modified.

## Referee findings

### 1. Uniform affine factorization
PASS/CLOSED as an application of the Paper 2 affine target-filtration theorem. The proof is presentation-independent: any homomorphism into
S_k=A_k\rtimes U_{1,k}
kills P_{p^{k-1}+1}(S_k), hence every affine crossed-cocycle factors through the stated quotient.

### 2. Free-product truncation
PASS/CLOSED. The functor T_n(G)=G/P_n(G) is the reflector onto pro-p groups with P_n=1, so the reflected free-product formula is legitimate. No separate mixed-commutator depth is needed.

### 3. f-collapse
PASS/LOCAL after wording repair. The power term x_1^{p^f} has Zassenhaus weight p^f. Thus f>=k makes the power relation disappear at the stated window. For f<k, the parameter remains visible in the marked finite abelianization. The manuscript now avoids claiming that an abstract quotient canonically labels the individual blocks.

### 4. Blockwise Kummer recognition
PASS/LOCAL after proof repair. The repaired proof explicitly uses Paper 2 arbitrary-candidate factorization to identify twisted H^1 on Q_k with H^1 on the free product, and P_n\subset Phi(G) for trivial coefficients. The standard degree-one free-product decomposition then reduces surjectivity to the factor maps.

### 5. Mathematical boundary
No new fatal mathematical error was found after the repair. The paper is correctly restricted to finite free pro-p products of the declared Demushkin blocks and does not claim the full ET_p class or absolute carrier minimality.

## Referee conclusion

**Mathematical application status: PASS / CLOSED.**

The manuscript is mathematically coherent as an application/synthesis paper. The decisive remaining question is not correctness but logical non-redundancy and publication novelty.
