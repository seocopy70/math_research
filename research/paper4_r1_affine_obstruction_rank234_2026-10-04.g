# Paper 4 R1 independent GAP certificate
# Verifies the same marked affine E_s obstruction mechanism in ranks 2,3,4.
# Convention: [x,y] = x^-1*y^-1*x*y.
#
# E_s = A_s semidirect U_s, A_s=Z/p^(s+1), U_s=<1+p^s>.
# A generator x_i is sent to (u_i, 1+p^s*alpha_i).
# We search alpha and the coordinate cocycles u=e_i. Since the relator
# evaluation is linear in the cocycle coordinates, one successful basis
# vector proves existence of a cocycle with v_p(delta(r))=s.

p := 3;
s := 2;
P := p^s;
M := p^(s+1);

AffMul := function(a,b)
  return [ (a[1] + a[2]*b[1]) mod M, (a[2]*b[2]) mod M ];
end;

AffInv := function(a)
  local ai;
  ai := InverseMod(a[2],M);
  return [ (-ai*a[1]) mod M, ai mod M ];
end;

EvalWord := function(word,xs)
  local out,g,t;
  out := [0,1];
  for g in word do
    t := xs[AbsInt(g)];
    if g < 0 then
      t := AffInv(t);
    fi;
    out := AffMul(out,t);
  od;
  return out;
end;

Comm := function(i,j)
  return [-i,-j,i,j];
end;

Relator := function(d)
  local r;
  r := Comm(1,2);
  if d = 4 then
    r := Concatenation(r,Comm(3,4));
  fi;
  return r;
end;

VP := function(x)
  local y,v;
  y := x mod M;
  if y = 0 then
    return 999;
  fi;
  v := 0;
  while y mod p = 0 do
    y := QuoInt(y,p);
    v := v+1;
  od;
  return v;
end;

CheckRank := function(d)
  local r,alpha,units,xs,j,u,ev,coeff,found, witness, target;
  r := Relator(d);
  found := false;
  witness := fail;

  for alpha in Tuples([0..p-1],d) do
    units := List([1..d],j->(1+P*alpha[j]) mod M);
    # psi(r)=1 is the multiplicative/unit-coordinate condition.
    xs := List([1..d],j->[0,units[j]]);
    ev := EvalWord(r,xs);
    if ev[2] = 1 then
      for j in [1..d] do
        u := List([1..d],k->Int(k=j));
        xs := List([1..d],k->[u[k],units[k]]);
        ev := EvalWord(r,xs);
        target := ev[1] mod M;
        if target mod P = 0 and VP(target) = s then
          found := true;
          witness := rec(
            rank := d,
            alpha := alpha,
            cocycle_basis_index := j,
            delta_r := target,
            valuation := VP(target),
            psi_r := ev[2],
            relator := r
          );
          break;
        fi;
      od;
    fi;
    if found then break; fi;
  od;

  if not found then
    Error(Concatenation("R1 FAIL: no affine witness in rank ",String(d)));
  fi;

  Print("R1 rank-",d,
        " PASS: alpha=",String(witness.alpha),
        ", cocycle=e_",String(witness.cocycle_basis_index),
        ", delta(r)=",String(witness.delta_r),
        ", v_p=",String(witness.valuation),
        ", psi(r)=",String(witness.psi_r),"
");
  return witness;
end;

Print("Paper 4 R1 independent GAP certificate
");
Print("p=",p,", s=",s,", A=Z/",M,", critical translation p^s=",P,"
");
results := List([2,3,4],CheckRank);
if ForAll(results,r->r.valuation=s and r.psi_r=1) then
  Print("R1_CERTIFICATE=PASS
");
else
  Error("R1 certificate failed.");
fi;
QUIT;
