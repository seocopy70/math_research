# Track B — q=3 vs q=∞: degree-3/4 comparison

## Setup
Use
G_q = <x1,x2,x3,x4 | x1^q [x1,x2][x3,x4] = 1>,
with q=3, and the q=∞ control obtained by deleting the x1^q term.

The common quadratic relation is
R=[X1,X2]+[X3,X4].

## Exact truncated Magnus comparison
Using the exact relation-derived identity
C(x1)=x2 x1 x2^{-1}=x1 x2 [x3,x4] x1^q x2^{-1}
for finite q, and
C_∞(x1)=x1 x2 [x3,x4] x2^{-1}
for the pure-commutator control, define
s_q=C_q(x1)x1^{-1}[x3,x4]^{-1}.

The homogeneous degree-3 Magnus components satisfy

in_3(s_3) = X1^[3] + 2[[X3,X4],X1] + 2[[X3,X4],X2],

while

in_3(s_∞) = 2[[X3,X4],X1] + 2[[X3,X4],X2].

Therefore the exact difference is

in_3(s_3)-in_3(s_∞)=X1^[3].

This is the cleanest possible degree-3 separation: the q=3 relation contributes precisely the restricted p-power class, while the common Lie/conjugation correction is identical.

## Degree-4 consequence
Bracketing with X1 gives
[X1^[3],X1]=0.
Hence the q-dependent difference disappears under the A3 degree-4 operation used previously.

Consequently the induced degree-4 correction is the same in both controls:

d4 = 2[[[X3,X4],X1],X1] + 2[[[X3,X4],X2],X1]
   = -(T + [[[X3,X4],X2],X1])  in F3.

Thus this A3 degree-4 probe does NOT distinguish q=3 from q=∞, even though the restricted degree-3 classes do distinguish them.

## Interpretation
1. Degree 3 already detects the presence of the p-power relation through X1^[3].
2. The degree-4 A3 correction studied so far is insensitive to that difference because [X1^[3],X1]=0.
3. Therefore the previously observed nonzero d4 in W45 should not be interpreted as the q-sensitive signal itself.
4. The q-sensitive signal is the restricted degree-3 class, not its bracket with X1.
5. This also validates the structural objection to using q=3 vs q=9 at degree 4: q=9 has no x1^9 contribution before degree 9.

## Verification status
The comparison above was checked by exact truncated noncommutative Magnus arithmetic over F3. It should next be independently reproduced by a committed script/workflow before being promoted from computational result to research certificate.
