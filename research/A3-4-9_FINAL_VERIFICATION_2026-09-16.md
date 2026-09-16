# A3-4-9 Final Verification — 2026-09-16

## Question
Does the 45-dimensional invariant space W45 survive the true degree-4 relation quotient
\[
L_4/[L_1,(R)_3]?
\]
with \((R)_3=[L_1,R]\) and \(S=[L_1,(R)_3]\)?

## Primary CI certificate
Run #3: `35065467549`, commit `8fa36314637ac582f098820a97616cbf4ebf5529`.

- dim (R)_3 = 4
- dim S = dim [L1,(R)_3] = 15
- dim W45 = 45
- rank([W45 | S]) = 60
- dim(W45 ∩ S) = 0
- dim pi(W45) = 45
- dim [L2,R] = 5
- dim ker(L4/[L2,R] -> L4/[L1,(R)_3]) = 10
- [L2,R] subset S = True
- ALL CHECKS PASSED

## Independent determinant + reconstruction check
Run #7: `35065891385`, commit `47c832caf3b62e9a3c944090e42d24a000033a0f`.

The 16 natural generators of S were reduced independently to a genuine 15-column basis. Then 60 independent ambient coordinate rows were selected, giving a literal 60x60 maximal minor of [W45 | S_basis].

- independent rank(W45) = 45
- independent rank(S) = 15
- selected S basis columns = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,15]
- independent rank([W45 | S_basis]) = 60
- independent dim(W45 ∩ S) = 0
- independent rank([S | [L2,R]]) = 15
- [L2,R] subset S = True
- selected independent ambient rows = 60
- det(60x60 maximal minor of [W45 | S_basis]) mod 3 = 2
- test vector = [[X1,X2],[X3,X4]]
- reconstruction exact over F_3 = True
- reconstruction residual nonzero entries = 0
- INDEPENDENT DETERMINANT + RECONSTRUCTION CHECK PASSED

## Conclusion
The primary rank certificate and an independent sparse-elimination/determinant/reconstruction path agree. In particular,
\[
W_{45}\cap [L_1,(R)_3]=0,
\qquad \dim \pi(W_{45})=45.
\]
Thus A3-4-9 is fixed as a verified computational result. The intermediate failed sanity runs (#2–#6) were implementation-coordinate errors in the auxiliary check and did not alter the primary certificate; the final independent check passes on the corrected implementation.
