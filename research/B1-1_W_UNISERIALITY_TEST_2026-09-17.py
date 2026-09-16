import os
import runpy
import subprocess
import tempfile
import numpy as np

P = 3
ROOT = 'research/'
ns = runpy.run_path(ROOT + 'phase2_1_invariant_space_verification_2026-09-15.py')
ns3 = runpy.run_path(ROOT + 'phase2_3_endH_optimized_2026-09-15.py')
A = [np.array(x, dtype=np.int64) % P for x in ns['action_matrices']]
N = np.array(ns3['N'], dtype=np.int64) % P
assert len(A) == 5 and all(x.shape == (45,45) for x in A)
assert N.shape == (45,45)
DIM_W = A[0].shape[0]


def rank_mod_p(M, p=P):
    """Exact Gaussian-elimination rank over F_p."""
    A0 = np.array(M, dtype=np.int64) % p
    if A0.ndim != 2:
        raise ValueError('rank_mod_p expects a 2D matrix')
    A0 = A0.copy()
    m, n = A0.shape
    rank = 0
    for col in range(n):
        piv = None
        for r in range(rank, m):
            if int(A0[r, col]) % p != 0:
                piv = r
                break
        if piv is None:
            continue
        if piv != rank:
            A0[[rank, piv]] = A0[[piv, rank]]
        inv = pow(int(A0[rank, col]), -1, p)
        A0[rank, :] = (A0[rank, :] * inv) % p
        for r in range(m):
            if r != rank and A0[r, col] % p:
                factor = int(A0[r, col])
                A0[r, :] = (A0[r, :] - factor * A0[rank, :]) % p
        rank += 1
        if rank == m:
            break
    return rank


def gap_rows(M):
    return '[' + ','.join('[' + ','.join(str(int(x)%P) for x in row) + ']' for row in M.tolist()) + ']'


def gap_matrix_list(mats):
    # GAP GModuleByMats uses row vectors on the right. The authoritative
    # Python action matrices act on columns, so transpose generators.
    return '[' + ','.join(gap_rows(M.T) for M in mats) + ']'


# Exact finite-field sanity checks in the authoritative Python coordinates.
rank_N_F3 = rank_mod_p(N)
N2 = (N @ N) % P
assert rank_N_F3 == 10, f'Unexpected F3 rank(N): {rank_N_F3}'
assert np.array_equal(N2, np.zeros_like(N2)), 'N^2 != 0 over F3'
assert all(np.array_equal((N @ g) % P, (g @ N) % P) for g in A), 'N does not commute with all generators over F3'
assert DIM_W - rank_N_F3 == 35, 'Rank-nullity sanity check failed for N'

literal = gap_matrix_list(A)
# N is an endomorphism for the authoritative column-action representation:
# N A = A N. After passing to GAP's row-action representation, the
# corresponding endomorphism is N^T, and im(N) must therefore be compared
# as the ROW SPAN of N^T. This is exactly the same conversion used for
# submodule bases in A3-4-20S.
n_literal = gap_rows(N.T)

gap_code = r'''F := GF(3);;
Raw := %s;;
Nraw := %s;;
ToField := function(m)
  return ImmutableMatrix(F,List(m,r->List(r,x->One(F)*x)));
end;;
Gens := List(Raw,ToField);;
N := ToField(Nraw);;
M := GModuleByMats(Gens,F);;
Print("B1-1 / W45 SOCLE VS im(N) -- TRANSPOSE + F3 RANK CORRECTED\n");
Print("DIM_W_FROM_EXACT_PYTHON = %s\n");
Print("RANK_N_FROM_EXACT_F3 = %s\n");
SB := MTX.BasisSocle(M);;
Print("SOCLE_DIM = ",Length(SB),"\n");
Nrank := RankMat(N);;
Print("RANK_N_GAP = ",Nrank,"\n");
JoinRank := RankMat(ImmutableMatrix(F,Concatenation(List(SB,r->List(r)),List(N,r->List(r)))));;
Print("SOCLE_PLUS_IMN_RANK = ",JoinRank,"\n");
Print("SOCLE_EQ_IMN = ",Length(SB)=Nrank and JoinRank=Length(SB),"\n");
QUIT;
''' % (literal, n_literal, DIM_W, rank_N_F3)
with tempfile.NamedTemporaryFile('w', suffix='.g', delete=False, encoding='utf-8') as f:
    f.write(gap_code); path=f.name
try:
    p=subprocess.run(['gap','-q',path],text=True,capture_output=True)
finally:
    os.unlink(path)
print(p.stdout,end='')
if p.stderr:
    print('--- GAP STDERR ---')
    print(p.stderr,end='')
if p.returncode != 0 or 'Error,' in p.stdout or 'Error,' in p.stderr:
    raise SystemExit('GAP B1-1 socle/imN comparison failed')
if 'SOCLE_EQ_IMN = true' not in p.stdout:
    raise SystemExit('B1-1 socle is not equal to im(N)')
