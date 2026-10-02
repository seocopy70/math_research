# PAPER 4 — F1 FINITE-WINDOW FACTORIZATION STRESS TEST FOR THE K–Z p-ADIC EXTENSION CLASS — 2026-10-02

## 1. Target

For the K–Z family
\[
G_s=\langle x,y,z\mid z^{p^s}=[x,y]\rangle,
\qquad
N_s=\overline{\langle z\rangle}^{G_s},
\qquad
D\simeq \mathbf Z_p^2,
\]
E2 gives a full-extension p-adic transgression class \(\epsilon_s\) whose valuation is
\[
v_p(\epsilon_s)=s
\]
up to the unit ambiguity from the choice of generator of \(H_2(D,\mathbf Z_p)\).

The F1 question is whether a finite Zassenhaus window can determine finite truncations of this class.

## 2. Pre-check

- **Object:** finite truncation \(\epsilon_s\bmod p^m\), with intrinsic content at least its valuation when nonzero.
- **Input:** the bare finite Zassenhaus quotient \(G/D_n(G)\); no presentation, lift, or hidden parameter \(s\).
- **Functoriality:** the quotient is functorial under pro-p homomorphisms preserving the filtration.
- **Gauge:** the scalar representative is only defined up to a \(\mathbf Z_p^\times\)-unit; valuation is the invariant tested here.
- **Orientation bridge:** none is assumed. This is a test of the E2 extension object itself.
- **q-blindness:** the K–Z family has fixed quotient \(D\simeq\mathbf Z_p^2\); no q-parameter is inserted.
- **Separation:** test whether distinct \(s\) can have the same finite window but different \(\epsilon_s\bmod p^m\).
- **Novelty:** this is not a new homological calculation; the possible new content is the finite-window non-factorization boundary.
- **Stop:** if the same finite window supports different E2 valuations, factorization at that depth is impossible.

## 3. Exact same-window lemma

Let \(F=F(x,y,z)\) be the free pro-p group and let \(D_n(F)\) be its Zassenhaus filtration. For
\[
r_s=z^{p^s}[x,y]^{-1},
\qquad
G_s=F/\overline{\langle\!\langle r_s\rangle\!\rangle},
\]
functoriality gives
\[
D_n(G_s)=D_n(F)\,\overline{\langle\!\langle r_s\rangle\!\rangle}/\overline{\langle\!\langle r_s\rangle\!\rangle}.
\]
If \(p^s\ge n\), then
\[
z^{p^s}\in D_{p^s}(F)\subseteq D_n(F).
\]
Therefore, modulo \(D_n(F)\), the relator \(r_s\) reduces to \([x,y]^{-1}\). Hence
\[
\boxed{
G_s/D_n(G_s)
\cong
F/\bigl(D_n(F),[x,y]\bigr)
}
\qquad(p^s\ge n).
\]
In particular, for any \(s,t\) satisfying \(p^s\ge n\) and \(p^t\ge n\),
\[
\boxed{G_s/D_n(G_s)\cong G_t/D_n(G_t).}
\]

This is the correct K–Z same-window statement. It does **not** identify the quotient with \(\mathbf Z_p^3/D_n\); the surviving commutators \([x,z]\), \([y,z]\) remain, exactly as found in the earlier critical correction.

## 4. Separation of the E2 invariant

E2 independently gives
\[
v_p(\epsilon_s)=s.
\]
Thus for \(s\ne t\), the full-extension p-adic invariants have different valuations.

More strongly, if
\[
1\le s<t<m
\]
and \(p^s\ge n\), then
\[
\epsilon_s\not\equiv0\pmod{p^m},
\qquad
\epsilon_t\equiv0\pmod{p^m},
\]
up to the harmless unit ambiguity. Yet the same finite window occurs:
\[
G_s/D_n(G_s)\cong G_t/D_n(G_t).
\]

Therefore no map
\[
F_{n,m}\colon G/D_n(G)\longrightarrow
\text{(finite data determining }\epsilon_G\bmod p^m)
\]
can exist uniformly on the K–Z family at a fixed depth \(n\) whenever the family contains two such parameters \(s,t<m\) with \(p^s\ge n\).

Equivalently: **there is no uniform finite depth, independent of the hidden extension-depth parameter, that recovers the E2 p-adic class on the whole K–Z family.**

## 5. Exact logical boundary

This is deliberately weaker than the previously withdrawn cd=2/cd=3 matched-window theorem.

It proves:

- fixed-depth factorization uniformly across the K–Z family: **FAIL / CLOSED**;
- uniform bound \(n=n(p,d,m)\) for recovering \(\epsilon\bmod p^m\) across all such extensions: **FAIL / CLOSED**;
- a group-dependent depth \(n=n(G,m)\): **OPEN**;
- the possibility that \(n=p^m\) (or another relation-depth bound) suffices for this particular family: **OPEN**;
- a bare finite window canonically identifying the extension decomposition \(1\to N\to G\to D\to1\): **OPEN**;
- orientation recovery from the E2 object: **OPEN**.

The counterexample does not show that an individual \(G_s\) lacks a finite detecting window. Indeed, once the window reaches the relation depth, the tail may become visible.

## 6. Independent check against the withdrawn argument

The proof uses only the free presentation and functoriality of the Zassenhaus filtration. It never compares \(G_s\) with \(\mathbf Z_p^3\). Thus the earlier error involving surviving \([x,z]\) and \([y,z]\) cannot enter.

The correct conceptual picture is:

\[
\text{same finite window for all }s\text{ with }p^s\ge n
\quad\not\Rightarrow\quad
\text{same full extension class}.
\]

The deep-tail parameter is genuinely invisible to any fixed lower window, even though the ambient nonabelian quotient itself changes relative to the abelian control.

## 7. Consequence for Paper 4

E2 is now a genuine negative finite-window boundary, but not yet a full Paper-4 theorem about cd=3 or orientation.

The remaining load-bearing question is adaptive thresholding:
\[
\boxed{
\text{Can an intrinsic finite window of depth controlled by }m
\text{ recover }\epsilon\bmod p^m
\text{ for each individual extension?}
}
\]

No carrier computation is authorized before that question is answered. In particular, do not return to the withdrawn \(\mathbf Z_p^3\) matched pair.

## Classification

- E2 full-extension p-adic valuation \(v_p(\epsilon_s)=s\): **PASS / LOCAL**.
- K–Z same-window lemma for \(p^s\ge n\): **PASS / CLOSED**.
- uniform finite-depth factorization of E2 across the K–Z family: **FAIL / CLOSED**.
- group-dependent/adaptive finite-window factorization: **OPEN / LOAD-BEARING**.
- orientation recovery from E2: **OPEN**.
- previous K–Z vs \(\mathbf Z_p^3\) matched-window no-go: **HISTORICAL / SUPERSEDED**.

