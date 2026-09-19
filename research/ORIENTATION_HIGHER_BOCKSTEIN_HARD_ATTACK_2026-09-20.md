# HARD ATTACK 11 — HIGHER BOCKSTEIN / p-ADIC DIGIT TOWER — 2026-09-20

## Target

Attack the proposed next bridge
\[
J_3\to J_4\to J_5\to\cdots
\]
by asking whether successive Bockstein/higher-obstruction layers genuinely provide intrinsic new information that can be identified with the successive $3$-adic digits of the exact Fox orientation, rather than merely repackaging the exact coefficient-level orientation criterion.

## 1. First definition attack: the Serre/Labute orientation criterion is candidate-dependent

For a candidate character $\rho:G\to\mathbf Z_3^\times$, the standard Demuškin orientation criterion can be formulated through the coefficient modules $I_m(\rho)$ and the lifting behavior of
\[
H^1(G,I_{m+1}(\rho))\to H^1(G,I_m(\rho)).
\]
This is a legitimate intrinsic cohomological characterization of the canonical orientation once $\rho$ is supplied, and the literature describes the canonical orientation in precisely this coefficient-module/cohomological form. However, the coefficient system itself depends on the unknown $\rho$.

Therefore this criterion is **not**, by itself, a filtered relation object from which $\rho$ is reconstructed. It is an exact characteristic-zero candidate-test, analogous in logical role to the Fox row. Treating the family of $\rho$-twisted lifting obstructions as the sought filtered carrier would merely move the unknown character into the input.

Decision: **PASS / LOCAL** as an exact orientation test; **FAIL / CLOSED** as a non-circular definition of the desired filtered input.

## 2. Second attack: higher Bocksteins of trivial $\mathbf F_3$-cohomology do not automatically equal higher orientation digits

Higher Bockstein operations are successive obstruction operations associated with coefficient extensions. They can detect higher $3$-power divisibility/lifting phenomena, and in the standard Demuškin family they can distinguish the valuation level of the parameter $q=3^f$ in situations where the first Bockstein vanishes.

But the desired output is stronger:
\[
\text{intrinsic filtered data}\longrightarrow\chi\bmod 3^n
\]
as a character-valued, presentation-natural object.

A higher Bockstein class lives in mod-$3$ cohomology. To turn it into the actual next character digit one still needs:
1. a canonical coefficient/lift identification;
2. a normalization of the $H^2$ line compatible across levels;
3. a map from the obstruction class to a specific covector in $H^1(G,\mathbf F_3)^*$;
4. compatibility of those identifications under $n\mapsto n+1$.

None of these follows merely from the existence of higher Bockstein operations.

Thus “higher Bockstein exists” does **not** close the tower-to-$\chi$ bridge.

Decision: **OPEN**, with the missing maps explicitly identified.

## 3. Frozen q=3 calculation: there is no evidence of an independent new digit obstruction after mod 9

For the exact Fox equations
\[
F_1=B(1+A)+A^2,\quad F_2=A-1,\quad F_3=D-1,\quad F_4=C-1
\]
with $A=1+3a$, $B=1+3b$, $C=1+3c$, $D=1+3d$, one has
\[
F_1=3+6b+9a+9a^2+9ab,\quad F_2=3a,\quad F_3=3d,\quad F_4=3c.
\]
Hence the mod-9 layer gives
\[
a=c=d=0,\qquad 1+2b\equiv0\pmod3.
\]

Once $a=c=d=0$ are imposed, the exact remaining equation is simply
\[
1+2B=0,
\]
so every higher digit of $B$ is uniquely forced by the same unit coefficient $2$. There is no new independent geometric obstruction appearing at each higher digit in this frozen q=3 presentation.

This is important: a proposed hierarchy of “new higher obstruction classes” must explain what genuinely new filtered information supplies the coefficient-level data of the exact equation $2B+1=0$. Merely iterating the already-known mod-3 Bockstein obstruction does not establish that.

Decision: **PASS / LOCAL** for the recursive uniqueness mechanism; **OPEN** for an intrinsic filtered source of the exact coefficient equation.

## 4. Classification attack: detecting q is not the same as reconstructing chi

For standard odd-prime Demuškin groups, the relation parameter $q$ is a $3$-power (or $0$), and the canonical orientation has image controlled by $q$. Literature also identifies the orientation as a canonical dualizing/cohomological character. Therefore a hierarchy that merely recovers the valuation $f$ in $q=3^f$ would at most recover the image-level invariant without yet proving the requested natural character-valued factorization.

The project must not silently replace
\[
\chi:G\to\mathbf Z_3^\times
\]
by the scalar invariant $q$ or by its valuation.

Decision: **FAIL / CLOSED** for the weaker claim “higher Bocksteins alone have therefore reconstructed the orientation character.”

## 5. What survives

The attack does not rule out a genuine tower. A viable tower must contain, at each stage, an intrinsic obstruction with a canonical target in the $H^2$ line and a natural identification of its next lift with a digit of a character. The definition must not use the candidate $\chi$ or $q$.

The most promising precise formulation is therefore not “higher Bockstein classes recover digits” but:

\[
\boxed{
\text{intrinsic filtered relation extension}
\;\longrightarrow\;
\text{successive normalized obstruction class}
\;\longrightarrow\;
\text{unique character lift}.
}
\]

The missing theorem is the first arrow.

## 6. Stronger boundary

There are now three logically distinct towers:

1. **Exact candidate-test tower:** $\rho\mapsto J_r(\rho)\bmod 3^n$. Exact and presentation-covariant, but character-dependent input.
2. **Cohomological Bockstein tower:** intrinsic mod-$3$ operations/lifts. Potentially detects $3$-power depth, but no character-valued reconstruction map has been proved.
3. **Filtered relation tower:** desired input. Its successive extension data have not yet been shown to determine the exact Fox coefficient tower.

Only (1) is currently exact at all $3$-adic levels. The central research gap is precisely the map
\[
(3)\longrightarrow(1)
\]
without defining (3) from (1).

## Decision

**HIGHER BOCKSTEIN BRIDGE: OPEN / STRUCTURAL.**

**No-go established:** the existence of higher Bockstein operations, or recovery of the $q$-valuation, is insufficient by itself to claim full $\chi$ reconstruction.

**Next authorized attack:** test whether the full filtered relation class (as an inverse system of actual filtered quotients, not merely its associated graded pieces) canonically reconstructs the exact Fox obstruction ideal. If it does, the result must be proved as a non-circular functorial reconstruction theorem. If it does not, construct a pair of filtered extensions with identical graded data but different Fox coefficient lifts.

## Literature boundary

The literature check confirms that Demuškin orientation is a canonical dualizing/cohomological character and that the standard Demuškin parameter $q$ controls its image; higher Bockstein operations are standard higher lifting obstructions. These facts are methodological support, not a proof of the missing filtered-to-Fox factorization.

