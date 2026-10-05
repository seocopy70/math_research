LoadPackage("autpgrp");

mkG:=function(s,a) local F; F:=FreeGroup("z","x","y");
  if s=0 then return F/[(F.2^(3^a)*Comm(F.2,F.3))]; fi;
  return F/[F.1^(3^s)*(F.2^(3^a)*Comm(F.2,F.3))^-1]; end;

winW:=function(G,n,c) local qs,epi,H,J,Dn,nat;
  qs:=PQuotient(G,3,c); epi:=EpimorphismQuotientSystem(qs); H:=Image(epi);
  J:=JenningsSeries(H); Dn:=TrivialSubgroup(H); if Length(J)>=n then Dn:=J[n]; fi;
  nat:=NaturalHomomorphismByNormalSubgroup(H,Dn);
  return [Image(nat),List(GeneratorsOfGroup(G),g->Image(nat,Image(epi,g)))]; end;

vec:=function(v,basis)
  return List(basis, b->Coefficient(basis,b,v));
end;

# GAP's pc-group coordinates: use ExponentsOfPcElement with the
# canonical pcgs of the elementary abelian Frattini quotient.
matFromAut:=function(alpha,frnat,basis)
  local cols,img;
  cols:=List(basis,img->ExponentsOfPcElement(
      Image(frnat,Image(alpha,PreImagesRepresentative(frnat,img)))));
  return List([1..Length(basis)],i->List(cols,c->c[i] mod 3));
end;

lineRepresentatives:=function(V)
  local els,seen,reps,v,w;
  els:=AsSortedList(V); seen:=[]; reps:=[];
  for v in els do
    if v<>One(V) and not v in seen then
      Add(reps,v);
      for w in els do
        if w<>One(V) and ForAny([0,1,2],k->w=v^k) then Add(seen,w); fi;
      od;
    fi;
  od;
  return reps;
end;

run:=function()
  local R,W,gens,A,frnat,V,basis,mats,L,H,Z,reps,
        w,c,cent,wpow,central,records,e,h;

  R:=winW(mkG(1,1),4,4); W:=R[1]; gens:=R[2];
  A:=AutomorphismGroupPGroup(W);
  frnat:=NaturalHomomorphismByNormalSubgroup(W,FrattiniSubgroup(W));
  V:=Image(frnat);

  # Basis is tied to the actual presentation generators z,x,y.
  basis:=List(gens,g->Image(frnat,g));
  if Size(Group(basis))<>Size(V) or Length(basis)<>3 then
    Error("Frattini basis z,x,y does not have rank 3");
  fi;

  mats:=List(Concatenation(A.glAutos,A.agAutos),
             alpha->matFromAut(alpha,frnat,basis));
  L:=Group(List(mats,m->GroupHomomorphismByImages(
      V,V,basis,List([1..3],i->Product(
        List([1..3],j->basis[j]^(m[j][i]))))))));
  if Size(L)<>6 then Error("actual Frattini image is not order 6"); fi;

  H:=Group([
    [[1,0,0],[0,2,0],[0,0,2]],
    [[1,0,0],[0,1,0],[0,1,1]]
  ]);
  if Size(H)<>6 then Error("expected subgroup H has wrong order"); fi;

  # Compare sets of matrices via canonical string representations.
  if Set(mats)<>Set(List(AsList(H),x->x)) then
    Print("ACTUAL_MATRICES=\n",Set(mats),"\n");
    Error("actual six matrices do not equal expected embedded subgroup");
  fi;

  # Intrinsicity test: scan all 13 projective lines in V and compare
  # centralizer size and whether the cube of a lift is central.
  Z:=Centre(W);
  reps:=lineRepresentatives(V);
  records:=[];
  for e in reps do
    w:=PreImagesRepresentative(frnat,e);
    cent:=Size(Centralizer(W,w));
    wpow:=w^3;
    central:=wpow in Z;
    Add(records,[e,cent,central]);
  od;
  Print("ACTUAL_MATRICES=",Set(mats),"\n");
  Print("EXPECTED_MATRICES=",Set(AsList(H)),"\n");
  Print("LINE_INVARIANTS=",records,"\n");

  # The intrinsicity criterion is deliberately exact: exactly one projective
  # line must have the distinguished pair (central cube, maximal centralizer).
  if Length(Filtered(records,r->r[3]))<>1 then
    Error("cube-centrality does not distinguish a unique projective line");
  fi;
  e:=Filtered(records,r->r[3])[1][1];
  cent:=Filtered(records,r->r[3])[1][2];
  if ForAny(records,r->r[2]>cent) then
    Error("distinguished line is not a centralizer extremum");
  fi;

  Print("P5_P3_STABILIZER_CASE s=1 a=1 PASS\n");
  Print("P5_P3_STABILIZER_IMAGE_ORDER=6\n");
  Print("P5_P3_STABILIZER_INTRINSIC_LINE=PASS\n");
  Print("P5_P3_STABILIZER_CERTIFICATE=PASS\n");
end;
run();
QUIT;

# CI retrigger after workflow registration: 2026-10-06.
