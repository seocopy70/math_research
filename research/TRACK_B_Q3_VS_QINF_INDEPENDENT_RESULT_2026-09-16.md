# Track B — independent q=3 vs q=∞ verification

## Purpose
Independently reproduce the degree-3 q-separation without importing any earlier research script or reusing the previous A3 implementation.

## Method
Work in the truncated noncommutative Magnus algebra over F_3 with

x_i = 1 + X_i,

truncated at total degree 3.  Compute the exact relation-derived expressions

C_3(x_1)=x_1x_2[x_3,x_4]x_1^3x_2^{-1},

and the q=∞ control

C_∞(x_1)=x_1x_2[x_3,x_4]x_2^{-1}.

Then set

s_q=C_q(x_1)x_1^{-1}[x_3,x_4]^{-1}.

No earlier research Python module is imported by the verifier.

## Independent calculation
The homogeneous degree-3 components are

in_3(s_3)
 = X_1^[3] + 2[[X_3,X_4],X_1] + 2[[X_3,X_4],X_2],

and

in_3(s_∞)
 = 2[[X_3,X_4],X_1] + 2[[X_3,X_4],X_2].

Therefore

\[
\boxed{\operatorname{in}_3(s_3)-\operatorname{in}_3(s_\infty)=X_1^{[3]}}.
\]

The independent implementation checks this equality directly as an equality of degree-3 word dictionaries over F_3.

## Degree-4 control
In the tensor realization, X_1^[3]=X_1^3, hence

\[
[X_1^{[3]},X_1]=[X_1^3,X_1]=0.
\]

The verifier checks this identity directly as well. Thus the previously studied A3 degree-4 bracket cannot transmit the q-sensitive difference.

## Conclusion
The clean q-sensitive signal is already present at restricted/Zassenhaus degree 3.  The A3 degree-4 correction is q-insensitive because the new degree-3 p-power class brackets trivially with X_1.

This establishes the intended primary comparison at the computational-certificate level: q=3 and q=∞ are distinguishable in degree 3, while the previously used degree-4 A3 probe is not the carrier of that distinction.

## Reproducibility
Verifier: `research/TRACK_B_Q3_VS_QINF_INDEPENDENT_2026-09-16.py`

CI workflow: `.github/workflows/track-b-q3-qinf-independent.yml`

The workflow was added immediately after the verifier so that the same self-contained calculation is independently executed by GitHub Actions. At the time of this record, the commit status endpoint has not yet reported a completed check; therefore the mathematical result above is recorded from the independent exact arithmetic, while CI completion remains a separate execution check.
