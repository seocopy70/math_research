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
rank3 = ns['rank3']
assert len(A) == 5 and all(x.shape == (45,45) for x in A)
assert N.shape == (45,45)
DIM_W = 45

# Python: column action v -> A v. GAP: row action v -> v A.
def gap_rows(M):
    return '[' + ','.join('[' + ','.join(str(int(x) % P) for x in row) + ']' for row in M.tolist()) + ']'

def gap_matrix_list(mats):
    return '[' + ','.join(gap_rows(M.T) for M in mats) + ']'

# Exact F3 sanity checks.
rank_N = rank3(N)
assert rank_N == 10
assert np.array_equal((N @ N) % P, np.zeros_like(N))
assert all(np.array_equal((N @ g) % P, (g @ N) % P) for g in A)
assert DIM_W - rank_N == 35

# In GAP row coordinates, the corresponding endomorphism is N^T.
# Its row kernel is exactly the Python column kernel ker(N).
literal = gap_matrix_list(A)
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
Print("B1-1-2 UNIQUE 35D SUBMODULE TEST\n");
Print("DIM_W = %s\n");
Print("RANK_N_F3 = %s\n");
Print("N2_ZERO = ",RankMat(N*N)=0,"\n");
SB := MTX.BasisSocle(M);;
Print("SOCLE_DIM = ",Length(SB),"\n");
K := NullspaceMat(N);;
Print("KER_N_DIM = ",Length(K),"\n");
maxs := MTX.BasesMaximalSubmodules(M);;
Print("MAXIMAL_SUBMODULE_COUNT = ",Length(maxs),"\n");
Print("MAXIMAL_SUBMODULE_DIMS = ",List(maxs,Length),"\n");
idx35 := Filtered([1..Length(maxs)],i->Length(maxs[i])=35);;
Print("MAXIMAL_35D_COUNT = ",Length(idx35),"\n");
all35eqK := ForAll(idx35,i->RankMat(ImmutableMatrix(F,Concatenation(maxs[i],K)))=35);;
Print("ALL_35D_MAXIMAL_EQUAL_KER_N = ",all35eqK,"\n");
KisMaximal := Length(Filtered([1..Length(maxs)],i->Length(maxs[i])=Length(K) and RankMat(ImmutableMatrix(F,Concatenation(maxs[i],K)))=Length(K)))=1;;
Print("KER_N_IS_UNIQUE_35D_MAXIMAL = ",KisMaximal,"\n");
UNIQUE_35D := Length(idx35)=1 and all35eqK and KisMaximal;;
Print("B1_1_2_PASS = ",UNIQUE_35D,"\n");
QUIT;
''' % (literal, n_literal, DIM_W, rank_N)

with tempfile.NamedTemporaryFile('w', suffix='.g', delete=False, encoding='utf-8') as f:
    f.write(gap_code)
    path = f.name
try:
    p = subprocess.run(['gap', '-q', path], text=True, capture_output=True)
finally:
    os.unlink(path)
print(p.stdout, end='')
if p.stderr:
    print('--- GAP STDERR ---')
    print(p.stderr, end='')
if p.returncode != 0 or 'Error,' in p.stdout or 'Error,' in p.stderr:
    raise SystemExit('B1-1-2 GAP computation failed')
if 'B1_1_2_PASS = true' not in p.stdout:
    raise SystemExit('B1-1-2 uniqueness criterion failed')
