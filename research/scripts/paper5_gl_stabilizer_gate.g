LoadPackage("autpgrp");

mkG:=function(s,a) local F;
  F:=FreeGroup("z","x","y");
  if s=0 then return F/[(F.2^(3^a)*Comm(F.2,F.3))]; fi;
  return F/[F.1^(3^s)*(F.2^(3^a)*Comm(F.2,F.3))^-1];
end;

winW:=function(G,n,c) local qs,epi,H,J,Dn,nat;
  qs:=PQuotient(G,3,c); epi:=EpimorphismQuotientSystem(qs); H:=Image(epi);
  J:=JenningsSeries(H); Dn:=TrivialSubgroup(H); if Length(J)>=n then Dn:=J[n]; fi;
  nat:=NaturalHomomorphismByNormalSubgroup(H,Dn);
  return [Image(nat),List(GeneratorsOfGroup(G),g->Image(nat,Image(epi,g)))];
end;

Coord:=function(v,b)
  local i,j,k;
  for i in [0..2] do for j in [0..2] do for k in [0..2] do
    if b[1]^i*b[2]^j*b[3]^k=v then return [i,j,k]; fi;
  od; od; od;
  Error("coordinate not found");
end;

ImageMatrix:=function(alpha,frnat,basis)
  local cols,j;
  # basis is a basis of V=W/Phi(W), so alpha must act on W-lifts,
  # then be projected by frnat.  Applying alpha directly to V caused
  # the GAP family mismatch in run 37199037517.
  cols:=List([1..Length(basis)],j->
    Coord(Image(frnat,Image(alpha,basis[j])),List(basis,k->Image(frnat,k))));
  local M;
  M:=TransposedMat(Matrix(GF(3),cols));
  return List([1..3],i->List([1..3],j->M[i][j]));
end;

CandidateGroups:=function()
  local G,els,G02,G01,G12,G11,m,detA;
  G:=GL(3,3); els:=Elements(G);
  # (s,a)=(0,2): preserve the plane <x,y>.
  G02:=Subgroup(G,Filtered(els,m->IsZero(m[3][1]) and IsZero(m[3][2]) and not IsZero(m[3][3])));
  # (s,a)=(0,1): preserve <x> inside <x,y> and impose the mixed
  # x^[3] / [x,y] scaling condition, giving y-coefficient 1.
  G01:=Subgroup(G,Filtered(els,m->IsZero(m[2][1]) and IsZero(m[3][1]) and
                           IsZero(m[3][2]) and IsOne(m[2][2])));
  # (s,a)=(1,2): preserve <x,y>, <z>, and impose z^[3]=[x,y]:
  # z-scalar equals determinant of the 2x2 block.
  G12:=Subgroup(G,Filtered(els,function(m)
    detA:=m[1][1]*m[2][2]-m[1][2]*m[2][1];
    return IsZero(m[3][1]) and IsZero(m[3][2]) and IsZero(m[1][3]) and
           IsZero(m[2][3]) and m[3][3]=detA;
  end));
  # (s,a)=(1,1): impose the stronger root relation
  # x -> a x, y -> b x+y, z -> a z.
  G11:=Subgroup(G,Filtered(els,m->IsZero(m[2][1]) and IsZero(m[3][1]) and
                           IsZero(m[3][2]) and IsOne(m[2][2]) and
                           IsZero(m[1][3]) and IsZero(m[2][3]) and
                           m[3][3]=m[1][1]));
  return [G01,G11,G02,G12];
end;

run:=function(s,a)
  local R,W,gens,A,frnat,basis,autGens,Mats,actual,Cands,expected,i,eq;
  R:=winW(mkG(s,a),4,4); W:=R[1]; gens:=R[2];
  A:=AutomorphismGroupPGroup(W);
  frnat:=NaturalHomomorphismByNormalSubgroup(W,FrattiniSubgroup(W));
  # Work in the presentation basis (x,y,z), not an arbitrary PC basis.
  basis:=[gens[2],gens[3],gens[1]];
  autGens:=Concatenation(A.glAutos,A.agAutos);
  Mats:=List(autGens,alpha->ImageMatrix(alpha,frnat,basis));
  Print("matrix determinants = ",List(Mats,DeterminantMat),"\n");
  if ForAny(Mats,m->DeterminantMat(m)=0) then
    Error("non-invertible Frattini action matrix");
  fi;
  actual:=Subgroup(GL(3,3),Mats);
  Cands:=CandidateGroups();
  expected:=[[0,1],[1,1],[0,2],[1,2]];
  i:=Position(expected,[s,a]); eq:=actual=Cands[i];
  Print("=== Paper5 GL stabilizer gate s=",s," a=",a," ===\n");
  Print("actual image order = ",Size(actual)," candidate order = ",Size(Cands[i]),"\n");
  Print("candidate structure = ",StructureDescription(Cands[i]),"\n");
  Print("embedded equality in basis (x,y,z) = ",eq,"\n");
  if not eq then
    Error("STABILIZER equality failure");
  fi;
  Print("STABILIZER s=",s," a=",a," PASS\n");
end;

for t in [[0,1],[1,1],[0,2],[1,2]] do run(t[1],t[2]); od;
Print("STABILIZER_CERTIFICATE=PASS\n");
QUIT;
