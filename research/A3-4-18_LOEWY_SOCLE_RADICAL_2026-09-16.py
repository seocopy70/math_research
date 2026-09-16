import os
import subprocess
import tempfile
import runpy
import numpy as np

P = 3
ROOT = 'research/'

# Reuse the exact A3-4-16/A3-4-17 representation setting.
ns = runpy.run_path(ROOT + 'A3-4-16_STRONG_MODULAR_FINGERPRINT_2026-09-16.py')
BA = [np.array(x, dtype=np.int64) % P for x in ns['BA_gens']]
K = [np.array(x, dtype=np.int64) % P for x in ns['K_gens']]
assert len(BA) == len(K) == 5
assert all(A.shape == (35, 35) for A in BA + K)

# GAP/MeatAxe uses row-vector actions.  Our existing matrices are left
# actions on column vectors, so transpose before constructing G-modules.
def gap_matrix_literal(A):
    rows = []
    for row in A.tolist():
        rows.append('[' + ','.join(str(int(x) % P) for x in row) + ']')
    return '[' + ','.join(rows) + ']'

def gap_matrix_list(mats):
    return '[' + ','.join(gap_matrix_literal(A.T) for A in mats) + ']'

ba_literal = gap_matrix_list(BA)
k_literal = gap_matrix_list(K)

gap_code = r'''F := GF(3);;
BAraw := %s;;
Kraw := %s;;
BAgens := List(BAraw, m -> ImmutableMatrix(F,m));;
Kgens := List(Kraw, m -> ImmutableMatrix(F,m));;
MBA := GModuleByMats(BAgens,F);;
MK := GModuleByMats(Kgens,F);;

Print("A3-4-18 / EXACT MEATAXE LOEWY ANALYSIS\n");
Print("FIELD = GF(3)\n");
Print("DIM_BA = ",MTX.Dimension(MBA),"\n");
Print("DIM_K = ",MTX.Dimension(MK),"\n");
Print("GENERATOR_COUNT = ",Length(MTX.Generators(MBA)),"\n");

AnalyzeModule := function(name,M)
  local soc,rad,nsoc,nrad,cur,b,nb,curdim,rad_dims,soc_dims,
        comp,collected,indecomp;

  Print("MODULE = ",name,"\n");
  Print("INDECOMPOSABLE = ",MTX.IsIndecomposable(M),"\n");

  soc := MTX.BasisSocle(M);
  nsoc := Length(soc);
  Print("SOCLE_DIM = ",nsoc,"\n");

  rad := MTX.BasisRadical(M);
  nrad := Length(rad);
  Print("RADICAL_DIM = ",nrad,"\n");
  Print("TOP_DIM = ",MTX.Dimension(M)-nrad,"\n");

  # Exact radical filtration dimensions: M >= rad M >= rad^2 M >= ...
  rad_dims := [MTX.Dimension(M)];
  cur := M;
  while MTX.Dimension(cur) > 0 do
    b := MTX.BasisRadical(cur);
    nb := Length(b);
    Add(rad_dims,nb);
    if nb = 0 then break; fi;
    b := MTX.NormedBasisAndBaseChange(b)[1];
    cur := MTX.InducedActionSubmodule(cur,b);
  od;
  Print("RADICAL_FILTRATION_DIMS = ",rad_dims,"\n");
  Print("LOEWY_LENGTH_RADICAL = ",Length(rad_dims)-1,"\n");

  # Exact socle filtration dimensions via successive quotient modules.
  soc_dims := [0];
  cur := M;
  curdim := MTX.Dimension(cur);
  while curdim > 0 do
    b := MTX.BasisSocle(cur);
    nb := Length(b);
    Add(soc_dims,MTX.Dimension(M)-curdim+nb);
    if nb = curdim then break; fi;
    b := MTX.NormedBasisAndBaseChange(b)[1];
    cur := MTX.InducedActionFactorModule(cur,b);
    curdim := MTX.Dimension(cur);
  od;
  Print("SOCLE_FILTRATION_CUMULATIVE_DIMS = ",soc_dims,"\n");
  Print("LOEWY_LENGTH_SOCLE = ",Length(soc_dims)-1,"\n");

  comp := MTX.CompositionFactors(M);
  Print("COMPOSITION_FACTOR_COUNT = ",Length(comp),"\n");
  Print("COMPOSITION_FACTOR_DIMS = ",List(comp,MTX.Dimension),"\n");
  collected := MTX.CollectedFactors(M);
  Print("COLLECTED_FACTOR_COUNT = ",Length(collected),"\n");
  Print("COLLECTED_FACTOR_DIMS_MULT = ",List(collected,x->[MTX.Dimension(x[1]),x[2]]),"\n");

  return rec(soc_dim:=nsoc,rad_dim:=nrad,rad_dims:=rad_dims,
             soc_dims:=soc_dims,comp_dims:=List(comp,MTX.Dimension),
             indecomp:=MTX.IsIndecomposable(M));
end;;

RBA := AnalyzeModule("B/A",MBA);;
RK := AnalyzeModule("K",MK);;

Print("SUMMARY\n");
Print("SOCLE_DIM_BA = ",RBA.soc_dim,"\n");
Print("SOCLE_DIM_K = ",RK.soc_dim,"\n");
Print("RADICAL_DIM_BA = ",RBA.rad_dim,"\n");
Print("RADICAL_DIM_K = ",RK.rad_dim,"\n");
Print("RADICAL_FILTRATION_EQUAL = ",RBA.rad_dims=RK.rad_dims,"\n");
Print("SOCLE_FILTRATION_EQUAL = ",RBA.soc_dims=RK.soc_dims,"\n");
Print("COMPOSITION_FACTOR_DIMENSIONS_EQUAL = ",RBA.comp_dims=RK.comp_dims,"\n");
Print("INDECOMPOSABLE_EQUAL = ",RBA.indecomp=RK.indecomp,"\n");
Print("A3-4-18 GAP/MEATAXE CHECK COMPLETED\n");
QUIT;
''' % (ba_literal, k_literal)

with tempfile.NamedTemporaryFile('w', suffix='.g', delete=False, encoding='utf-8') as f:
    f.write(gap_code)
    gap_path = f.name

try:
    proc = subprocess.run(['gap', '-q', gap_path], text=True, capture_output=True)
finally:
    os.unlink(gap_path)

print(proc.stdout, end='')
if proc.stderr:
    print('--- GAP STDERR ---')
    print(proc.stderr, end='')

if proc.returncode != 0:
    raise SystemExit(proc.returncode)

print('PYTHON_DRIVER_RETURN_CODE =', proc.returncode)
print('ACTION_MATRICES_SOURCE = A3-4-16')
print('RESULT: exact socle/radical/Loewy computation delegated to GAP MeatAxe.')
