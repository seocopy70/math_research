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

ImageMatrix:=function(alpha,frnat,basisW)
  local vbasis,cols,j,M;
  # A.glAutos/A.agAutos may have a source copy of W.  Therefore recover
  # each Frattini-basis element through frnat before applying alpha.
  vbasis:=List(basisW,k->Image(frnat,k));
  cols:=List([1..Length(vbasis)],j->
    Coord(Image(frnat,Image(alpha,PreImagesRepresentative(frnat,vbasis[j]))),
          vbasis));
  M:=TransposedMat(Matrix(GF(3),cols));
  return List([1..3],i->List([1..3],j->M[i][j]));
end;

Vecs:=Elements(GF(3)^3);

MatPerm:=function(m)
  return PermList(List(Vecs,v->Position(Vecs,v*m)));
end;

CandidateGroups:=function()
  local G,els,G02,G01,G12,G11,m,detA;
  G:=GL(3,3); els:=Elements(G);
  # Candidate groups are transported to a faithful permutation action on GF(3)^3.
  G02:=Group(List(Filtered(els,m->IsZero(m[3][1]) and IsZero(m[3][2]) and not IsZero(m[3][3])),MatPerm));
  G01:=Group(List(Filtered(els,m->IsZero(m[2][1]) and IsZero(m[3][1]) and
                           IsZero(m[3][2]) and IsOne(m[2][2])),MatPerm));
  G12:=Group(List(Filtered(els,function(m)
    detA:=m[1][1]*m[2][2]-m[1][2]*m[2][1];
    return IsZero(m[3][1]) and IsZero(m[3][2]) and IsZero(m[1][3]) and
           IsZero(m[2][3]) and m[3][3]=detA;
  end),MatPerm));
  G11:=Group(List(Filtered(els,m->IsZero(m[2][1]) and IsZero(m[3][1]) and
                           IsZero(m[3][2]) and IsOne(m[2][2]) and
                           IsZero(m[1][3]) and IsZero(m[2][3]) and
                           m[3][3]=m[1][1]),MatPerm));
  return [G01,G11,G02,G12];
end;

run:=function(s,a)
  local R,W,gens,A,frnat,basis,autGens,Mats,actual,Cands,expected,i,eq,Huser,Z,centerV;
  R:=winW(mkG(s,a),4,4); W:=R[1]; gens:=R[2];
  A:=AutomorphismGroupPGroup(W);
  frnat:=NaturalHomomorphismByNormalSubgroup(W,FrattiniSubgroup(W));
  # Work in the presentation basis (x,y,z), not an arbitrary PC basis.
  basis:=[gens[2],gens[3],gens[1]];
  autGens:=Concatenation(A.glAutos,A.agAutos);
  Mats:=List(autGens,alpha->ImageMatrix(alpha,frnat,basis));

  Z:=Centre(W);
  centerV:=Group(List(GeneratorsOfGroup(Z),z->Image(frnat,z)));
  Print("CENTER_IMAGE_ORDER=",Size(centerV),"\\n");
  if Size(centerV)<>3 then Error("center image is not a unique line"); fi;
  if centerV<>Group([Image(frnat,gens[1])]) then
    Error("center image line is not the z-line");
  fi;
  if ForAny(Mats,m->DeterminantMat(m)=0) then
    Error("non-invertible Frattini action matrix");
  fi;
  actual:=Group(List(Mats,MatPerm));
  Cands:=CandidateGroups();
  expected:=[[0,1],[1,1],[0,2],[1,2]];
  i:=Position(expected,[s,a]); eq:=actual=Cands[i];
  Print("=== Paper5 GL stabilizer gate s=",s," a=",a," ===\n");
  Print("actual image order = ",Size(actual)," candidate order = ",Size(Cands[i]),"\n");
  Print("candidate structure = ",StructureDescription(Cands[i]),"\n");
  Print("embedded equality in basis (x,y,z) = ",eq,"\n");
  if [s,a]=[1,1] then
    Print("ACTUAL_MATRICES_XYZ=",Set(Mats),"\n");
    # Convert the user-proposed subgroup from (z,x,y) to (x,y,z).
    # It is {[[e,h,0],[0,e^-1,0],[0,0,1]] : e in F3^*, h in F3}.
    Print("USER_EXPECTED_XYZ=",
      Set(List(Filtered(Elements(GL(3,3)),m->
        m[1][1] in [1,2] and
        m[1][1]<>0 and m[2][2]=Inverse(m[1][1]) and m[3][3]=1 and
        m[1][3]=0 and m[2][3]=0 and m[3][1]=0 and m[3][2]=0 and
        m[2][1]=0),m->m)),"\n");
  fi;
  if not eq then
    Error("STABILIZER equality failure");
  fi;
  Print("STABILIZER s=",s," a=",a," PASS\n");
end;

for t in [[0,1],[1,1],[0,2],[1,2]] do run(t[1],t[2]); od;
Print("STABILIZER_CERTIFICATE=PASS\n");
QUIT;

# CI retrigger after source-family correction: 2026-10-06.

# CI retrigger after actual embedded-line diagnostics: 2026-10-06.
