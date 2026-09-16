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

def gap_rows(M):
    return '[' + ','.join('[' + ','.join(str(int(x)%P) for x in row) + ']' for row in M.tolist()) + ']'

def gap_matrix_list(mats):
    return '[' + ','.join(gap_rows(M.T) for M in mats) + ']'

literal = gap_matrix_list(A)
n_literal = gap_rows(N)
gap_code = r'''F := GF(3);;
Raw := %s;;
Nraw := %s;;
ToField := function(m)
  return ImmutableMatrix(F,List(m,r->List(r,x->One(F)*x)));
end;;
Gens := List(Raw,ToField);;
N := ToField(Nraw);;
M := GModuleByMats(Gens,F);;
Print("B1-1 / W45 SOCLE VS im(N)\n");
Print("DIM_W_FROM_EXACT_PYTHON = %s\n");
Print("RANK_N_FROM_EXACT_PYTHON = %s\n");
SB := MTX.BasisSocle(M);;
Print("SOCLE_DIM = ",Length(SB),"\n");
Nrank := RankMat(N);;
Print("RANK_N_GAP = ",Nrank,"\n");
JoinRank := RankMat(ImmutableMatrix(F,Concatenation(List(SB,r->List(r)),List(N,r->List(r)))));;
Print("SOCLE_PLUS_IMN_RANK = ",JoinRank,"\n");
Print("SOCLE_EQ_IMN = ",Length(SB)=Nrank and JoinRank=Length(SB),"\n");
QUIT;
''' % (literal, n_literal, DIM_W, int(np.linalg.matrix_rank(N)))
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
