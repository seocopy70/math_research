import runpy
import subprocess
import tempfile
import numpy as np

P = 3
ROOT = 'research/'

# Reuse exactly the A3-4-16 representation data.
ns = runpy.run_path(ROOT + 'A3-4-16_STRONG_MODULAR_FINGERPRINT_2026-09-16.py')
BA = [np.array(x, dtype=np.int64) % P for x in ns['BA_gens']]
K = [np.array(x, dtype=np.int64) % P for x in ns['K_gens']]

assert len(BA) == len(K) == 5
assert all(A.shape == (35, 35) for A in BA + K)

def gap_matrix_literal(A):
    return '[' + ','.join('[' + ','.join(str(int(x) % P) for x in row) + ']' for row in A.tolist()) + ']'

def gap_matrix_list(mats):
    # A3-4-18 convention: transpose column-action matrices for GAP row-action modules.
    return '[' + ','.join(gap_matrix_literal(A.T) for A in mats) + ']'

ba_literal = gap_matrix_list(BA)
k_literal = gap_matrix_list(K)

gap_code = r'''F := GF(3);;
BAraw := %s;;
Kraw := %s;;
ToField := function(m)
  return ImmutableMatrix(F,List(m,r->List(r,x->One(F)*x)));
end;;
BAgens := List(BAraw,ToField);;
Kgens := List(Kraw,ToField);;
MBA := GModuleByMats(BAgens,F);;
MK := GModuleByMats(Kgens,F);;
Print("A3-4-19 / EXPLICIT SIMPLE-FACTOR MATCH\n");
Print("FIELD = GF(3)\n");
Print("DIM_BA = ",MTX.Dimension(MBA),"\n");
Print("DIM_K = ",MTX.Dimension(MK),"\n");

cba := MTX.CollectedFactors(MBA);;
ck := MTX.CollectedFactors(MK);;
Print("BA_COLLECTED_FACTORS = ",List(cba,x->[MTX.Dimension(x[1]),x[2]]),"\n");
Print("K_COLLECTED_FACTORS = ",List(ck,x->[MTX.Dimension(x[1]),x[2]]),"\n");

FactorOfDim := function(cfs,d)
  local z;
  z := Filtered(cfs,x->MTX.Dimension(x[1])=d);
  if Length(z) <> 1 then
    Error("expected exactly one collected factor of requested dimension");
  fi;
  if z[1][2] <> 1 then
    Error("expected multiplicity one for requested factor");
  fi;
  return z[1][1];
end;;

SBA10 := FactorOfDim(cba,10);;
SK10 := FactorOfDim(ck,10);;
SBA25 := FactorOfDim(cba,25);;
SK25 := FactorOfDim(ck,25);;

# Both inputs are irreducible composition factors. MTX.Isomorphism is
# therefore an exact irreducible-module isomorphism test.
iso10 := MTX.Isomorphism(SBA10,SK10);;
iso25 := MTX.Isomorphism(SBA25,SK25);;

Print("DIMENSION_10_FACTOR_ISOMORPHISM = ",iso10<>fail,"\n");
Print("DIMENSION_25_FACTOR_ISOMORPHISM = ",iso25<>fail,"\n");
if iso10 <> fail then Print("ISO10_MATRIX_SIZE = ",Length(iso10),"x",Length(iso10[1]),"\n"); fi;
if iso25 <> fail then Print("ISO25_MATRIX_SIZE = ",Length(iso25),"x",Length(iso25[1]),"\n"); fi;

PASS := (Length(cba)=Length(ck)
  and ForAll(cba,x->x[2]=1)
  and ForAll(ck,x->x[2]=1)
  and iso10<>fail
  and iso25<>fail);;
Print("A3-4-19_PASS = ",PASS,"\n");
if not PASS then
  Error("A3-4-19 simple-factor matching failed");
fi;
Print("RESULT: the 10- and 25-dimensional simple factors match across B/A and K.\n");
QUIT;
''' % (ba_literal, k_literal)

with tempfile.NamedTemporaryFile('w', suffix='.g', delete=False, encoding='utf-8') as f:
    f.write(gap_code)
    gap_path = f.name
try:
    proc = subprocess.run(['gap', '-q', gap_path], text=True, capture_output=True)
finally:
    import os
    os.unlink(gap_path)

print(proc.stdout, end='')
if proc.stderr:
    print('--- GAP STDERR ---')
    print(proc.stderr, end='')
if proc.returncode != 0 or 'Error,' in proc.stderr or 'Error,' in proc.stdout:
    raise SystemExit('GAP simple-factor matching failed')
print('PYTHON_DRIVER_RETURN_CODE =', proc.returncode)
print('ACTION_MATRICES_SOURCE = A3-4-16')
print('RESULT: exact simple-factor isomorphism tests completed.')
