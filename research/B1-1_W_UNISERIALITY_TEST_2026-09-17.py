import os
import runpy
import subprocess
import tempfile
import numpy as np

P = 3
ROOT = 'research/'
ns = runpy.run_path(ROOT + 'phase2_1_invariant_space_verification_2026-09-15.py')
A = [np.array(x, dtype=np.int64) % P for x in ns['action_matrices']]
assert len(A) == 5 and all(x.shape == (45,45) for x in A)

def gap_rows(M):
    return '[' + ','.join('[' + ','.join(str(int(x)%P) for x in row) + ']' for row in M.tolist()) + ']'

def gap_matrix_list(mats):
    return '[' + ','.join(gap_rows(M.T) for M in mats) + ']'

literal = gap_matrix_list(A)
gap_code = r'''F := GF(3);;
Raw := %s;;
ToField := function(m)
  return ImmutableMatrix(F,List(m,r->List(r,x->One(F)*x)));
end;;
Gens := List(Raw,ToField);;
M := GModuleByMats(Gens,F);;
Print("B1-1 / W45 SUBMODULE STRUCTURE\n");
Print("DIM_W = ",Dimension(M),"\n");
SB := MTX.BasisSocle(M);;
Print("SOCLE_DIM = ",Length(SB),"\n");
Print("SOCLE_BASIS_ROWS = ",Length(SB),"\n");
# Probe standard GAP/MeatAxe maximal-submodule operation if installed.
if IsBound(MTX.MaximalSubmodules) then
  MM := MTX.MaximalSubmodules(M);;
  Print("MAXIMAL_SUBMODULE_COUNT = ",Length(MM),"\n");
  Print("MAXIMAL_SUBMODULE_DIMS = ",[Length(x):x in MM],"\n");
else
  Print("MAXIMAL_SUBMODULES_API = NOT_AVAILABLE\n");
fi;
# Also probe all submodule lattice APIs without assuming their presence.
if IsBound(SubmoduleLattice) then
  Print("SUBMODULE_LATTICE_API = AVAILABLE\n");
else
  Print("SUBMODULE_LATTICE_API = NOT_AVAILABLE\n");
fi;
QUIT;
''' % literal
with tempfile.NamedTemporaryFile('w', suffix='.g', delete=False, encoding='utf-8') as f:
    f.write(gap_code); path=f.name
try:
    p=subprocess.run(['gap','-q',path],text=True,capture_output=True)
finally:
    os.unlink(path)
print(p.stdout,end='')
if p.stderr: print('--- GAP STDERR ---'); print(p.stderr,end='')
if p.returncode != 0 or 'Error,' in p.stdout or 'Error,' in p.stderr:
    raise SystemExit('GAP B1-1 probe failed')
if 'SUBMODULE_LATTICE_API = AVAILABLE' not in p.stdout and 'MAXIMAL_SUBMODULES_API = NOT_AVAILABLE' not in p.stdout:
    raise SystemExit('Unexpected B1-1 API probe state')
