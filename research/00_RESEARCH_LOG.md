## 2026-09-20 — HARD ATTACK 10: degree-3 Fox truncation FAIL / CLOSED under Nielsen change

A concrete Nielsen-equivalent presentation was used to attack the remaining idea that the fixed q=3 degree-3 Fox compression might itself be intrinsic.

Take
\[
x_1=y_1y_2,\quad x_2=y_2,\quad x_3=y_3,\quad x_4=y_4.
\]
The exact transformed Fox row is
\[
J'_1=Y_1^2Y_2+Y_1Y_2+1,
\]
\[
J'_2=Y_1(Y_1^2Y_2^2+Y_1^2Y_2+1),
\]
with the remaining rows rational in \(Y_3,Y_4\).

The transported canonical point is
\[
(Y_1,Y_2,Y_3,Y_4)=(-2,-1/2,1,1),
\]
which lies in the same \(1+3\mathbf Z_3\) neighborhood.

After writing \(Y_i=1+v_i\) and truncating to total degree \(\le3\), the second row evaluates at
\[
(v_1,v_2,v_3,v_4)=(-3,-3/2,0,0)
\]
to
\[
-243/2\neq0,
\]
although the full exact Fox row vanishes there.

Decision:
- full Fox scheme Nielsen covariance: PASS/CLOSED;
- fixed-normal-form degree-3 Fox compression: PASS/CLOSED;
- presentation-independent degree-3 Fox truncation: **FAIL/CLOSED**;
- intrinsic exact degree-(2,3) filtered carrier by another construction: **OPEN**.

This is a concrete counterexample to using the local degree bound of the frozen normal form as an intrinsic exact truncation theorem.

Record:
research/ORIENTATION_FOX_DEGREE3_NIELSEN_HARD_ATTACK_2026-09-20.md

## 2026-09-20 — HARD ATTACK 9: naive integral augmentation jet FAIL / CLOSED

The proposed next object \(\langle r-1\rangle\subset I^2/I^4\) in \(\mathbf Z_3[[F]]\), with ordinary augmentation ideal \(I\), was attacked before any computation.

For \(r=x_1^3[x_1,x_2][x_3,x_4]\) and \(X_i=x_i-1\),
\[
x_1^3-1=3X_1+3X_1^2+X_1^3.
\]
The commutator product begins in degree 2, so
\[
r-1=3X_1+[X_1,X_2]+[X_3,X_4]+O(I^3),
\]
and therefore \(r-1\notin I^2\).

This kills the proposed plain \(\mathbf Z_3\)-augmentation jet at the definition level. It is not a matter of missing gauge proof.

The correct distinction is:
- standard mod-3 Zassenhaus filtration: uses the completed \(\mathbf F_3[[F]]\) augmentation ideal and yields the degree-(2,3) restricted-Lie relation jet;
- ordinary \(\mathbf Z_3[[F]]\) augmentation filtration: is different and does not place the Demushkin relator in \(I^2\);
- mixed p-adic/Zassenhaus weighted filtrations: a legitimate possible direction, but finite associated graded pieces are residue-layer objects and do not automatically carry the full exact scalar \(-1/2\in\mathbf Z_3^\times\).

This is an independent structural confirmation of the previously closed “naive \(\mathbf Z_3\) restricted-Lie scalar extension” route.

Decision:
- plain \(\mathbf Z_3\)-augmentation \(I^2/I^4\) carrier: **FAIL / CLOSED**;
- mod-3 Zassenhaus degree-(2,3) carrier: **PASS / CLOSED**;
- mixed integral weighted jet: **OPEN**, but cannot be assumed to contain full 3-adic information;
- exact universal Fox scheme: **PASS / CLOSED** under the stated standard hypotheses;
- intrinsic exact two-component filtered compression: **OPEN**.

Literature check: standard Zassenhaus definitions use the augmentation ideal of \(\mathbf F_p[[G]]\), consistent with Jennings/Lazard and modern Demushkin/Koszul references.

Record:
research/ORIENTATION_INTEGRAL_AUGMENTATION_JET_HARD_ATTACK_2026-09-20.md



## 2026-09-19 — HARD ATTACK 2: exact Z_3 carrier identification reopened

A second theorem-level weakness was found. The fixed q=3 crossed-derivation calculation is algebraically sound, but the later claim that a concrete projective degree-(2,3) relation jet with exact Z_3 coefficients is itself an established carrier is too strong.

The mod-3 restricted Lie object uses a characteristic-3 p-operation. It cannot simply be scalar-extended to Z_3 as the same restricted-Lie structure. Therefore the exact pair (R,P_3) over Z_3 has not been independently defined in the required sense.

Correct status: fixed full relation + exact crossed derivation = PASS/CLOSED; intrinsic mod-9 projective degree-(2,3) carrier = PASS/CLOSED; concrete exact two-component degree-(2,3) carrier => full chi = OPEN; naive Z_3 restricted-Lie scalar extension = FAIL/CLOSED.

Detailed audit: research/ORIENTATION_EXACT_Z3_CARRIER_HARD_AUDIT_2026-09-19.md.


## 2026-09-19 — HARD ATTACK 3: universal exact Fox obstruction carrier

The exact-carrier search was reopened with a genuinely different object type rather than a scalar extension of the characteristic-3 restricted Lie carrier. For a fixed minimal one-relator presentation, define the universal Laurent coefficient ring A=Z_3[T_1^{±1},...,T_d^{±1}] and the unevaluated twisted Fox-Jacobian row J_r=(tau(partial r/partial x_i)), tau(x_i)=T_i. The carrier is defined independently of any candidate orientation; a character is recovered only after evaluating T_i at its values and solving J_r=0.

For r=x_1^3[x_1,x_2][x_3,x_4], the row is J_1=1+A+A^2/B, J_2=A^2(A-1)/B, J_3=A^3(D^{-1}-1)/C, J_4=A^3(1-C^{-1})/D. On 1+3Z_3 the zero locus is uniquely A=C=D=1, B=-1/2. Thus a fixed-presentation finite exact algebraic carrier recovering the full orientation has been obtained.

This does not yet solve intrinsicity: arbitrary minimal free-basis changes must be shown to induce the corresponding Laurent-torus coordinate change and transform the obstruction ideal covariantly. Relator conjugation/unit changes must also be checked. The object is not finite information; it contains exact 3-adic coefficient data in a finitely generated algebraic presentation.

Decision:
- fixed-presentation universal Fox carrier: PASS/CLOSED;
- non-circular input definition: PASS/CLOSED;
- q=3 full-orientation recovery: PASS/CLOSED;
- presentation-independent/intrinsic carrier: OPEN;
- two-component degree-(2,3) compression: OPEN.

Detailed record: research/ORIENTATION_EXACT_UNIVERSAL_FOX_CARRIER_AUDIT_2026-09-19.md.


## 2026-09-19 — HARD ATTACK 4: universal Fox carrier covariance CLOSED

The new universal exact Fox carrier was subjected to the presentation-change attack. The carrier is formulated over the completed local coefficient ring A=Z_3[[U_1,...,U_d]], T_i=1+U_i, and is projective under multiplication by units.

Relator conjugation gives J_{uru^{-1}}=tau(u)J_r, so the zero locus is unchanged. Relation-generator changes act by completed coefficient-ring units, conditional on the standard cyclic one-relator relation-module structure. A free-basis change is controlled by Fox's chain rule: the row transforms by induced formal torus substitution followed by an invertible evaluated Fox Jacobian. Hence the universal obstruction scheme is presentation-covariant and its character zero locus is preserved.

For the frozen q=3 relation the unique point in 1+3Z_3 is (1,-1/2,1,1). Therefore the exact carrier branch has a new positive endpoint:
- non-tautological exact characteristic-zero carrier in universal projective Fox-scheme form: PASS/CLOSED;
- presentation covariance: PASS/CLOSED at the universal Fox-calculus level, conditional on standard one-relator relation-module facts;
- fixed q=3 recovery: PASS/CLOSED;
- two-component degree-(2,3) compression: OPEN;
- bounded finite-information universal carrier: FAIL/CLOSED.

The research question is now sharpened: can the universal Fox obstruction scheme be compressed intrinsically to a smaller filtered object, ideally degree (2,3), without reintroducing the earlier circularity?

Detailed records: research/ORIENTATION_EXACT_UNIVERSAL_FOX_CARRIER_AUDIT_2026-09-19.md and research/ORIENTATION_EXACT_UNIVERSAL_FOX_COVARIANCE_AUDIT_2026-09-19.md.


## 2026-09-19 — HARD ATTACK 5: exact Fox degree-3 compression

A further structural reduction was found. In local coordinates T_i=1+u_i, the fixed q=3 universal Fox obstruction ideal is exactly equivalent on the 1+3Z_3 neighbourhood to
F_1=3+3u_1+u_1^2+u_1u_2+2u_2,
F_2=u_1,
F_3=u_4,
F_4=u_3.
Hence the zero locus is u_1=u_3=u_4=0 and 2u_2+3=0, giving chi(x_2)=-1/2. The unreduced second Fox coefficient has degree 3, so the full fixed-normal-form row has local degree at most 3.

The power-free control has projective ideal equivalent to (B-1,A-1,D-1,C-1), giving the trivial 1+3Z_3 character locus. Thus the exact carrier separates q=3 from the power-free control without using q as an input label.

Decision:
- fixed-normal-form degree-3 polynomial compression: PASS/CLOSED;
- intrinsic degree-3 truncation under arbitrary presentation change: OPEN;
- exact two-component (R,p)-type compression: OPEN.

Detailed record: research/ORIENTATION_EXACT_FOX_DEGREE3_COMPRESSION_AUDIT_2026-09-19.md.
