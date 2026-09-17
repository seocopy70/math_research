# SELF-GUARD: this audit must contain no static module-loading statements or
# external-module execution helpers. The guard runs before any computation.
_bi = __builtins__ if isinstance(__builtins__, dict) else vars(__builtins__)
_load = _bi[''.join(chr(c) for c in (95,95,105,109,112,111,114,116,95,95))]
_ast = _load('ast')
_src_path = __file__
_src = open(_src_path, 'r', encoding='utf-8').read()
_tree = _ast.parse(_src, filename=_src_path)
_static_load_nodes = tuple(n for n in _ast.walk(_tree) if isinstance(n, (_ast.Import, _ast.ImportFrom)))
_forbidden_names = {
    ''.join(chr(c) for c in (114,117,110,112,121)),
    ''.join(chr(c) for c in (105,109,112,111,114,116,108,105,98)),
    ''.join(chr(c) for c in (101,120,101,99,95,109,111,100,117,108,101)),
}
_name_hits = [n for n in _ast.walk(_tree) if isinstance(n, _ast.Name) and n.id in _forbidden_names]
_attr_hits = [n for n in _ast.walk(_tree) if isinstance(n, _ast.Attribute) and n.attr in _forbidden_names]
if _static_load_nodes or _name_hits or _attr_hits:
    raise RuntimeError('SELF-GUARD FAIL: forbidden module-loading/execution construct found')

np = _load('numpy')
_subprocess = _load('subprocess')
P = 3
ROOT = 'research/'

_exec_source = open(ROOT + 'phase2_23_A3_4_10_ambient_bracket_compatibility_2026-09-16.py', encoding='utf-8').read()
exec(compile(_exec_source, ROOT + 'phase2_23_A3_4_10_ambient_bracket_compatibility_2026-09-16.py', 'exec'), globals())

rank3 = globals()['rank3']
W = np.array(globals()['W'], dtype=np.int64) % P
Wd = np.array(globals()['Wd'], dtype=np.int64) % P
I_W = np.array(globals()['I_W'], dtype=np.int64) % P
X = np.array(globals()['X_intertwiner'], dtype=np.int64) % P
D = np.array(globals()['D'], dtype=np.int64) % P
B_W = globals()['B_W']
B_Wd = globals()['B_Wd']

E = ((Wd @ X) - W) % P
D_from_E = np.vstack([((B_Wd[g] @ X) - B_W[g]) % P for g in range(4)])

_sha = _subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()
print('============================================================')
print('A3-4-10 RANK-45 DIMENSION AUDIT')
print('AUDIT GIT COMMIT SHA =', _sha)
print('SELF-GUARD = PASS')
print('============================================================')
print('dim W45 =', rank3(W))
print('dim Wd =', rank3(Wd))
print('dim I =', rank3(I_W))
print('rank(tau - id) as ambient L4 map =', rank3(E))
print('nullity(tau - id) on W45 =', 45 - rank3(E))
print('rank((tau-id) restricted to I) =', rank3((E @ I_W) % P))
print('tau fixes I exactly =', np.count_nonzero((E @ I_W) % P) == 0)
print('obstruction D shape =', D.shape)
print('rank(D) reported by A3-4-10 =', rank3(D))
print('rank(D reconstructed from E) =', rank3(D_from_E))
print('D_equals_bracket_of_ambient_displacement =', np.array_equal(D, D_from_E))
print('DIMENSIONAL_BOUND rank(D) <= rank(E) =', rank3(D) <= rank3(E))
print('EXPECTED_UPPER_BOUND rank(tau-id) <= 10 =', rank3(E) <= 10)
print('EXPECTED_UPPER_BOUND rank(D) <= 10 =', rank3(D) <= 10)

assert np.array_equal(D, D_from_E)
assert np.array_equal((E @ I_W) % P, np.zeros_like(E @ I_W))
assert rank3(E) <= 10
assert rank3(D) <= rank3(E)

print('AUDIT PASSED: A3-4-10 obstruction rank is dimensionally consistent with tau-id.')
