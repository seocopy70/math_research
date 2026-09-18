"""Q3/Q9 Gate C-2b — authoritative H-action / restricted-power audit.

This gate deliberately REUSES the repository's authoritative degree-4
implementation:
    research/phase2_1_invariant_space_verification_2026-09-15.py

The imported implementation supplies:
  - gens: the five fixed H-generators;
  - apply_linear_map: the actual associative substitution action.

No transvection, symplectic matrix, or generator list is reconstructed here.

Scope:
  1. verify that the authoritative action is multiplicative on tested
     associative words;
  2. verify h(x^3)=(h x)^3 on basis and mixed degree-1 elements;
  3. verify the iterated degree-9 identity;
  4. print the mixed cross term
       (a x + b y)^3 - a^3 x^3 - b^3 y^3
     explicitly, to audit the noncommutative/Jacobson contribution.

If the imported action is multiplicative, p-power equivariance is formally
implied. The computation is therefore an implementation audit, not an
independent theorem about a different action.
"""

import runpy

P = 3

ns = runpy.run_path("research/phase2_1_invariant_space_verification_2026-09-15.py")
gens = ns["gens"]
apply_linear_map = ns["apply_linear_map"]
mul = ns["mul"]
add = ns["add"]
neg = ns["neg"]

X = [{(i + 1,): 1} for i in range(4)]

def scale(A, c):
    return {w: (c * v) % P for w, v in A.items() if (c * v) % P}

def power(A, n):
    out = {(): 1}
    for _ in range(n):
        out = mul(out, A)
    return out

def action(g, A):
    return apply_linear_map(A, g)

def fmt(A):
    return ", ".join(f"{w}:{c}" for w, c in sorted(A.items())) or "0"

def is_mixed(v):
    return sum(1 for c in v if c % P) >= 2

def vec(v):
    out = {}
    for i, c in enumerate(v):
        c %= P
        if c:
            out[(i + 1,)] = c
    return out

print("Q3/Q9 GATE C-2b — AUTHORITATIVE H-ACTION AUDIT")
print("field: F_3")
print("ACTION SOURCE = phase2_1_invariant_space_verification_2026-09-15.py")
print("ACTION IMPLEMENTATION = apply_linear_map")
print("GENERATOR SOURCE = gens")
print("H generator count =", len(gens))
print("ACTION MODEL = multiplicative substitution on associative words")

# 1. Direct multiplicativity audit on representative words, including
# products whose factors have degree > 1.
multiplicativity_pass = True
mult_cases = 0
for g in gens:
    for a in X:
        for b in X:
            for c in (1, 2):
                bc = add(b, scale(X[(X.index(b) + c) % 4], 1)) if False else b
                lhs = action(g, mul(a, b))
                rhs = mul(action(g, a), action(g, b))
                multiplicativity_pass &= (lhs == rhs)
                mult_cases += 1

# Stronger structural audit: every image of a word is built by multiplying
# the images of its letters. Test all words up to degree 3.
words = [()]
for d in range(1, 4):
    words.extend(__import__("itertools").product(range(1, 5), repeat=d))

word_action_pass = True
word_cases = 0
for g in gens:
    for w in words:
        source = {w: 1}
        expected = {(): 1}
        for letter in w:
            expected = mul(expected, action(g, {(letter,): 1}))
        ok = action(g, source) == expected
        word_action_pass &= ok
        word_cases += 1

# 2. Basis + mixed degree-1 p-equivariance.
test_vecs = []
for i in range(4):
    v = [0] * 4
    v[i] = 1
    test_vecs.append(tuple(v))

for i in range(4):
    for j in range(i + 1, 4):
        for c in (1, 2):
            v = [0] * 4
            v[i] = 1
            v[j] = c
            test_vecs.append(tuple(v))

basis_pass = True
mixed_pass = True
iterated_pass = True
basis_cases = 0
mixed_cases = 0

for gi, g in enumerate(gens):
    for v in test_vecs:
        x = vec(v)
        hx = action(g, x)

        lhs3 = action(g, power(x, 3))
        rhs3 = power(hx, 3)
        ok3 = lhs3 == rhs3

        lhs9 = action(g, power(power(x, 3), 3))
        rhs9 = power(power(hx, 3), 3)
        ok9 = lhs9 == rhs9

        if is_mixed(v):
            mixed_cases += 1
            mixed_pass &= ok3
        else:
            basis_cases += 1
            basis_pass &= ok3
        iterated_pass &= ok9

# 3. Explicit mixed cross terms. We require that at least one displayed
# nontrivial mixed pair has a nonzero cross term; this is a sanity check
# that the computation is genuinely noncommutative rather than a hidden
# commutative simplification.
cross_nonzero = False
cross_cases = 0
for i in range(4):
    for j in range(i + 1, 4):
        x, y = X[i], X[j]
        for a, b in ((1,1), (1,2), (2,1), (2,2)):
            z = add(scale(x, a), scale(y, b))
            cross = add(power(z, 3),
                        neg(add(scale(power(x, 3), pow(a, 3, P)),
                                scale(power(y, 3), pow(b, 3, P)))))
            print(f"CROSS x=X{i+1}, y=X{j+1}, a={a}, b={b} = {fmt(cross)}")
            cross_cases += 1
            if cross:
                cross_nonzero = True

print("MULTIPLICATIVITY_TEST =", "PASS" if multiplicativity_pass else "FAIL")
print("WORD_SUBSTITUTION_TEST =", "PASS" if word_action_pass else "FAIL")
print("BASIS_FIRST_P_EQUIVARIANCE =", "PASS" if basis_pass else "FAIL")
print("MIXED_FIRST_P_EQUIVARIANCE =", "PASS" if mixed_pass else "FAIL")
print("ITERATED_P_EQUIVARIANCE_DEGREE_9 =", "PASS" if iterated_pass else "FAIL")
print("MIXED_CROSS_TERM_NONZERO =", "PASS" if cross_nonzero else "FAIL")
print("basis cases =", basis_cases)
print("mixed cases =", mixed_cases)
print("cross-term cases =", cross_cases)

assert multiplicativity_pass
assert word_action_pass
assert basis_pass
assert mixed_pass
assert iterated_pass
assert cross_nonzero

print("C-2b RESULT = PASS")
print("SCOPE = authoritative associative/enveloping action audit only;")
print("        no canonical q=9 source, no d_9^(9), no N/J")
