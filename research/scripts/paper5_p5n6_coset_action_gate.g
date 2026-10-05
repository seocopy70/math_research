LoadPackage("autpgrp");

P:=5; N:=6; C:=5; Fld:=GF(P);

mkG:=function(s,a) local F;
  F:=FreeGroup("z","x","y");
  if s=0 then return F/[(F.2^(P^a)*Comm(F.2,F.3))]; fi;
  return F/[F.1^P*(F.2^(P^a)*Comm(F.2,F.3))^-1];
end;

winW:=function(G) local qs,epi,H,J,Dn,nat;
  qs:=PQuotient(G,P,C); epi:=EpimorphismQuotientSystem(qs); H:=Image(epi);
  J:=JenningsSeries(H); Dn:=TrivialSubgroup(H); if Length(J)>=N then Dn:=J[N]; fi;
  nat:=NaturalHomomorphismByNormalSubgroup(H,Dn);
  return [Image(nat),List(GeneratorsOfGroup(G),g->Image(nat,Image(epi,g)))];
end;

D:=function(i,a)
  local m;
  m:=IdentityMat(3,Fld); m[i][i]:=a*One(Fld); return m;
end;
EM:=function(i,j,a)
  local m;
  m:=IdentityMat(3,Fld); m[i][j]:=a*One(Fld); return m;
end;

MatPerm:=function(m)
  local vecs;
  vecs:=Elements(Fld^3);
  return PermList(List(vecs,v->Position(vecs,v*m)));
end;

CosetPerm:=function(alpha,W,Phi,basis)
  local vecs,reps,one,perm,i,j,v,img,ok;
  vecs:=Elements(Fld^3);
  reps:=List(vecs,v->basis[1]^Int(v[1])*basis[2]^Int(v[2])*basis[3]^Int(v[3]));
  perm:=List([1..Length(reps)],i->0);
  for i in [1..Length(reps)] do
    img:=Image(alpha,reps[i]); ok:=false;
    for j in [1..Length(reps)] do
      if img*reps[j]^-1 in Phi then perm[i]:=j; ok:=true; break; fi;
    od;
    if not ok then Error("coset coordinate not found"); fi;
  od;
  return PermList(perm);
end;

run:=function(s,a)
  local R,W,gens,A,Phi,basis,autGens,actual,Cand,els,pmats,i,eq,expected;
  R:=winW(mkG(s,a)); W:=R[1]; gens:=R[2];
  A:=AutomorphismGroupPGroup(W);
  Phi:=FrattiniSubgroup(W); basis:=[gens[2],gens[3],gens[1]];
  autGens:=Concatenation(A.glAutos,A.agAutos);
  actual:=Group(List(autGens,alpha->CosetPerm(alpha,W,Phi,basis)));
  Cand:=Group(D(1,2),EM(1,2,1),EM(1,3,1),EM(2,3,1),D(3,2));
  pmats:=List(GeneratorsOfGroup(Cand),MatPerm);
  Cand:=Group(pmats);
  eq:=actual=Cand;
  Print("=== P5 coset-action gate s=",s," a=",a," ===\n");
  Print("|W|=",Size(W)," |Aut(W)|=",A.size,"\n");
  Print("actual coset action order=",Size(actual)," candidate order=",Size(Cand),"\n");
  Print("embedded coset-action equality=",eq,"\n");
  if Size(actual)>A.size then Error("ACTION ORDER EXCEEDS AUT ORDER"); fi;
  if not eq then Error("COSET ACTION STABILIZER FAILURE"); fi;
  Print("P5_COSET_STABILIZER s=",s," a=",a," PASS\n");
end;

run(0,1); run(1,1);
Print("P5_COSET_STABILIZER_CERTIFICATE=PASS\n");
QUIT;
