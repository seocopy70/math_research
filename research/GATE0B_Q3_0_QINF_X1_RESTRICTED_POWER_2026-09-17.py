from itertools import product

P = 3
N = 4


def words(d):
    return list(product(range(1, N + 1), repeat=d))


def rank3(A):
    A = [list(map(lambda x: int(x) % P, row)) for row in A]
    m = len(A)
    n = len(A[0]) if m else 0
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if A[i][c]), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        if A[r][c] == 2:
            A[r] = [(2 * x) % P for x in A[r]]
        for i in range(m):
            if i != r and A[i][c]:
                f = A[i][c]
                A[i] = [(A[i][j] - f * A[r][j]) % P for j in range(n)]
        r += 1
        if r == m:
            break
    return r


def column_basis_rank(M):
    return rank3([list(col) for col in zip(*M)]) if M else 0

idx2 = {w: i for i, w in enumerate(words(2))}
idx3 = {w: i for i, w in enumerate(words(3))}

# R_inf = [X1,X2] + [X3,X4].
R = [0] * (N ** 2)
R[idx2[(1,2)]] = 1
R[idx2[(2,1)]] = 2
R[idx2[(3,4)]] = 1
R[idx2[(4,3)]] = 2

# [X_g, R] in the tensor realization.
def bracket_left_generator(g, v):
    out = [0] * (N ** 3)
    for j, coeff in enumerate(v):
        if coeff % P == 0:
            continue
        w = words(2)[j]
        out[idx3[(g,) + w]] = (out[idx3[(g,) + w]] + coeff) % P
        out[idx3[w + (g,)]] = (out[idx3[w + (g,)]] - coeff) % P
    return out

R3 = [bracket_left_generator(g, R) for g in range(1, N + 1)]

# In the tensor realization of the free restricted Lie algebra over F_3,
# X1^[3] is represented by the word X1 X1 X1.
x13 = [0] * (N ** 3)
x13[idx3[(1,1,1)]] = 1

rank_R3 = rank3(R3)
rank_aug = rank3(R3 + [x13])

# rank increases by one iff X1^[3] is not in the relation subspace.
contained = rank_aug == rank_R3

# Its ambient tensor representative is visibly nonzero; verify computationally.
x13_nonzero = any(c % P for c in x13)

print('GATE0B_Q3_0_QINF_X1_RESTRICTED_POWER')
print('dim (R_inf)_3 =', rank_R3)
print('X1^[3] ambient nonzero =', x13_nonzero)
print('X1^[3] in (R_inf)_3 =', contained)
print('rank R3 =', rank_R3)
print('rank [R3 | X1^[3]] =', rank_aug)
print('X1^[3] survives mod (R_inf)_3 =', (x13_nonzero and not contained))
print('RESULT =', 'PASS' if (x13_nonzero and not contained) else 'FAIL')

assert x13_nonzero
assert not contained
