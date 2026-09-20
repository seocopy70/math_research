# HARD ATTACK 33 — COKER ROUTE REOPENS AND SURVIVES THE RESTRICTION AUDIT

## 2026-09-20

### 1. Corrected target

Let
N=P_{k+1}(G), Q=G/N, M=N/(N^{3^k}[N,N]), E=G/(N^{3^k}[N,N]),
A=A_k(rho)=Z/3^k with candidate action rho:Q->U_k.

The finite extension gives the LHS transgression
delta_rho: Hom_Q(M,A) -> H^2(Q,A),
and
coker(delta_rho) = im(inf:H^2(Q,A)->H^2(G,A)) = ker(res:H^2(G,A)->H^2(N,A)).

Hard Attack 31 tried to close this by asserting res is nonzero on the canonical top class. That assertion was wrong. The corrected question is whether res is actually ZERO for all candidate rho.

### 2. Duality converts restriction into a finite norm problem

Let I be the dualizing module and B=Hom(A,I), a finite module of exponent 3^k. PD^2 duality identifies the Pontryagin dual of restriction
res:H^2(G,A)->H^2(N,A)
with the corestriction/norm
cor:H^0(N,B)->H^0(G,B).

Because rho factors through Q and chi mod 3^k also factors through Q, N acts trivially on B. Hence H^0(N,B)=B and cor is the norm operator
N_Q(b)=sum_{q in Q} q.b.

This is the exact place where the previous error is repaired: no top class is inserted; only the duality theorem is used after the finite carrier has already been defined.

### 3. Norm-zero estimate

The abelianization of Q contains the images of x_2,x_3,x_4 modulo 3^k, so |Q| is divisible by 3^{3k}. The image of the character delta=chi*rho^{-1}:Q->U_k has order at most 3^{k-1}.

Write C=im(delta), K=ker(delta). Then
N_Q = |K| N_C.

For a cyclic 3-group C of order 3^m acting through a nontrivial unit u in 1+3Z/3^k, the geometric norm coefficient
1+u+...+u^{3^m-1}
is divisible by 3^m (and is zero when m>=k). Since
v_3(|K|) >= 3k-(k-1)=2k+1,
the total norm coefficient is divisible by at least 3^{2k+1}, hence is zero on B=Z/3^k. In the trivial-character case m=0, N_Q is multiplication by |Q|, also zero on B.

Therefore:
\[
\boxed{\operatorname{cor}:H^0(N,B)\to H^0(G,B)=0.}
\]
Consequently
\[
\boxed{\operatorname{res}:H^2(G,A)\to H^2(N,A)=0.}
\]

### 4. The coker is therefore the entire twisted top cohomology

The inflation map is surjective for every candidate rho:
\[
H^2(Q,A)\twoheadrightarrow H^2(G,A).
\]
Hence
\[
\boxed{
\operatorname{coker}(\delta_\rho)
\cong H^2(G,A_k(\rho)).
}
\]

This is a major reversal of Hard Attack 31.

### 5. Orientation selector

PD^2 duality gives the standard exact criterion:
\[
rho=chi\pmod{3^k}
\iff
|H^2(G,A_k(rho))|=3^k.
\]
Therefore, combining with the finite coker identity:
\[
\boxed{
rho=chi\pmod{3^k}
\iff
|\operatorname{coker}(\delta_\rho)|=3^k.
}
\]

The right-hand side is computed entirely from the finite, q-blind extension
(Q_k,M_k,E_k) and the candidate rho. No chosen presentation, generator, relator, q, or known orientation formula is used in the carrier definition.

### 6. Critical admissibility check

This is not the forbidden tautology “append H^2(N,A)”:

- H^2(G,A) is NOT part of the carrier input.
- H^2(N,A) is NOT part of the carrier input.
- The carrier is the finite transgression cokernel built from the extension class.
- The identification with H^2(G,A) is a theorem derived after construction using PD^2 duality and the norm-zero lemma.
- The orientation formula q -> chi is not used.

Thus this passes the current non-tautological bridge requirement, subject to independent verification of the norm valuation and the precise duality/restriction-corestriction compatibility.

### 7. What remains to verify

The result is not yet promoted to PASS/CLOSED. Three points must be independently checked:

1. The lower bound |Q_k| divisible by 3^{3k} from the abelianization quotient.
2. The exact 3-adic valuation of the cyclic norm sum for every candidate image subgroup of U_k.
3. The duality identification of res^* with cor for finite p-primary coefficients in the pro-p PD^2 setting, including coefficient twists.

If all three pass, the Kummer recognition problem is solved at every finite level k.

### 8. Status

- Hard Attack 31 closure of coker route: HISTORICAL / SUPERSEDED.
- finite transgression coker carrier: OPEN / STRONG.
- inflation-surjectivity via norm-zero: OPEN / decisive.
- coker-size selector: OPEN / decisive.
- finite Kummer recognition through P_{k+1}: potentially PASS/LOCAL after independent verification.
- universal orientation reconstruction: still OPEN until verification and passage to all k are recorded.

No numerical scan is needed: the new result is symbolic and applies uniformly in k.
