## 2026-09-20 — HARD ATTACK 13: full associated-graded no-go and minimal extension lower bound

The previous attack only established that bounded associated-graded windows cannot recover the full orientation. A stronger question was attacked: perhaps the entire infinite mod-3 Zassenhaus graded object could still encode (q) and hence (chi).

The literature boundary closes this loophole for the present odd-prime Demuškin setting. Mináč–Pasini–Quadrelli–Tân identify, for Demuškin groups, the complete graded group algebra
[
\operatorname{gr}\mathbf F_p[[G]]\cong U(L(G))
]
with the quadratic/PBW Demuškin graded algebra. For odd (p), its defining relation is the quadratic symplectic relation
[
[X_1,X_2]+[X_3,X_4]+\cdots,
]
independent of the Demuškin (q)-invariant. Thus the full mod-3 associated-graded object is (q)-blind, not merely finite truncations.

Consequently the rank-four family
[
G_{3^s}=\langle x_i\mid x_1^{3^s}[x_1,x_2][x_3,x_4]\rangle,
qquad
G_\infty=\langle x_i\mid [x_1,x_2][x_3,x_4]\rangle
]
has the same mod-3 graded Demuškin object while
[
\chi_{3^s}(x_2)=(1-3^s)^{-1}
]
varies with (s), and (\chi_\infty(x_2)=1).

This is a genuine project-specific lower bound:

[
\boxed{
\text{full mod-3 associated graded data}
\not\Rightarrow
q
\not\Rightarrow
\chi.
}
]

Therefore any successful q-blind carrier must add non-graded filtered/characteristic-zero extension information. At the first nontrivial level, the projective degree-3 power component (P_3) coupled to the quadratic relation (R_2) supplies such information and recovers (chi\bmod9).

A further precision was added: it would be false to infer that every higher (3)-adic digit requires a new independent extension class. For fixed (q=3), the exact equation (1+2B=0) compresses all digits into one exact (\mathbf Z_3)-coefficient equation. Thus the remaining question is not “how many digits/classes?” but whether this exact extension information admits a canonical intrinsic representation strictly smaller than the universal projective Fox obstruction scheme.

Decision:
- **full mod-3 associated-graded (	o q,chi): FAIL / CLOSED;**
- **minimal non-graded extension lower bound for mod-9: PASS / LOCAL;**
- **intrinsic exact intermediate carrier: OPEN.**

Record:
research/ORIENTATION_FULL_GRADED_NO_GO_MINIMAL_EXTENSION_2026-09-20.md

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


## 2026-09-20 — HARD ATTACK 11: higher Bockstein / p-adic digit tower

The proposed Bockstein/higher-obstruction bridge was attacked at the definition level. Candidate-dependent twisted coefficient criteria are exact orientation tests, but they cannot be the desired q-blind filtered input because the coefficient system already depends on the unknown character. Higher Bocksteins can detect p-power lifting depth, but their existence does not supply a canonical map to the next character digit. In the frozen q=3 Fox equations, after the mod-9 layer is fixed, all higher digits are forced recursively by the exact unit equation 1+2B=0; no independent higher geometric obstruction appears in that presentation.

Decision: **OPEN / STRUCTURAL** for a genuine higher-obstruction bridge; **FAIL / CLOSED** for the inference “higher Bockstein tower alone reconstructs full chi.”

Next attack: distinguish full filtered extension data from the bare associated graded tower, and test whether the former canonically reconstructs the exact Fox obstruction ideal. If not, seek an explicit same-graded/different-lift obstruction pair.

Record: `research/ORIENTATION_HIGHER_BOCKSTEIN_HARD_ATTACK_2026-09-20.md`.


## 2026-09-20 — HARD ATTACK 12: filtered extension vs associated graded

The phrase “full filtered tower” was split into (A) the full associated-graded tower and (B) an actual compatible tower of filtered extension quotients. (A) does not retain extension/gluing data; the $q=3^s$ family gives the finite-window obstruction to full $\chi$. (B), if it literally retains compatible residues of the relation in a complete separated filtration, reconstructs the completed relation by inverse limit, and completed Fox calculus then applies by continuity. This is mathematically valid but largely formal and does not by itself provide a smaller intrinsic carrier.

Decision: associated-graded full-$\chi$ claim **FAIL / CLOSED**; full filtered-extension-to-Fox implication **PASS / LOCAL**; genuine intermediate compression **OPEN**.

Record: `research/ORIENTATION_FILTERED_EXTENSION_VS_GRADED_HARD_ATTACK_2026-09-20.md`.
