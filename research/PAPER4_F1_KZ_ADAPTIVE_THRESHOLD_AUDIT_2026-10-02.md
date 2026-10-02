# PAPER 4 — F1 ADAPTIVE THRESHOLD ON THE K–Z FAMILY — 2026-10-02

## Result

The K–Z family does not merely give a negative fixed-depth example. Its abelianization gives an explicit positive adaptive bound for the p-adic valuation truncation.

Let
\[
G_s^{ab}\simeq \mathbf Z_p^2\oplus \mathbf Z/p^s.
\]
For the Zassenhaus quotient
\[
Q_n^{(s)}=G_s/D_n(G_s),
\]
functoriality gives
\[
(Q_n^{(s)})^{ab}
\simeq
G_s^{ab}/D_n(G_s^{ab}).
\]

Since \(G_s^{ab}\) is abelian, if \(e=\lceil\log_p n\rceil\), then
\[
D_n(G_s^{ab})=(G_s^{ab})^{p^e},
\]
and hence
\[
(Q_n^{(s)})^{ab}
\simeq
(\mathbf Z/p^e)^2\oplus\mathbf Z/p^{\min(s,e)}.
\]

Take
\[
n=p^m.
\]
Then \(e=m\), so the torsion exponent in the finite-window abelianization is exactly
\[
p^{\min(s,m)}.
\]
Therefore the intrinsic quantity
\[
\tau_m(Q_{p^m})
:=
\min\{s,m\}
\]
is recoverable from the finite quotient itself.

Because E2 gives \(v_p(\epsilon_s)=s\), this recovers the truncated valuation
\[
\min(v_p(\epsilon_s),m).
\]
Equivalently, it determines whether \(\epsilon_s\equiv0\pmod{p^m}\), and if nonzero, determines its exact valuation below \(m\).

The calculation uses only intrinsic finite-group data (the abelianization and its exponent), not the presentation parameter \(s\).

## Sharpness within the K–Z family

The previous same-window lemma shows that a depth \(n\) cannot uniformly recover \(\epsilon_s\bmod p^m\) across all \(s\) if there exist
\[
s<t<m,qquad p^s\ge n.
\]
Thus any universal K–Z-family threshold for \(m\)-digit valuation information must satisfy, up to the integer boundary,
\[
n>p^{m-1}
\]
when \(m\ge2\).

The explicit construction \(n=p^m\) therefore gives the correct exponential scale, although this audit does not prove that \(p^m\) is the absolutely minimal threshold.

## Classification

- adaptive K–Z valuation recovery from a finite window: **PASS / LOCAL**;
- explicit intrinsic realization via \((G/D_{p^m}(G))^{ab}\): **PASS / LOCAL**;
- lower-bound scale \(n>p^{m-1}\) for uniform K–Z-family valuation recovery: **PASS / LOCAL**;
- exact minimal threshold \(n=p^{m-1}+1\) or similar: **OPEN**;
- general free-by-Demushkin finite-window factorization: **OPEN / LOAD-BEARING**;
- orientation recovery from the E2 class: **OPEN**.

This positive result prevents overclaiming the preceding F1 no-go: the K–Z family kills a fixed-depth/uniform-in-extension-depth detector, but it does not kill an \(m\)-dependent finite-window factorization.
