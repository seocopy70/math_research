LoadPackage("autpgrp");

mkG:=function(s,a) local F; F:=FreeGroup("z","x","y");
  if s=0 then return F/[(F.2^(3^a)*Comm(F.2,F.3))]; fi;
  return F/[F.1^(3^s)*(F.2^(3^a)*Comm(F.2,F.3))^-1]; end;

winW:=function(G,n,c) local qs,epi,H,J,Dn,nat;
  qs:=PQuotient(G,3,c); epi:=EpimorphismQuotientSystem(qs); H:=Image(epi);
  J:=JenningsSeries(H); Dn:=TrivialSubgroup(H); if Length(J)>=n then Dn:=J[n]; fi;
  nat:=NaturalHomomorphismByNormalSubgroup(H,Dn);
  return [Image(nat),List(GeneratorsOfGroup(G),g->Image(nat,Image(epi,g)))]; end;

permOnV:=function(alpha,frnat,elsV)
  local imgs;
  imgs:=List(elsV,v->Image(frnat,Image(alpha,PreImagesRepresentative(frnat,v))));
  return PermList(List(imgs,v->PositionSorted(elsV,v)));
end;

valuation:=function(N,p) local v; v:=0; while N mod p=0 do N:=N/p; v:=v+1; od; return v; end;

run:=function(s,a)
  local R,W,gens,A,V,frnat,elsV,glperms,L,IA,agtriv,GLorder,Autorder,
        alpha,d,report,GLsize;
  R:=winW(mkG(s,a),4,4); W:=R[1]; gens:=R[2];
  A:=AutomorphismGroupPGroup(W);
  frnat:=NaturalHomomorphismByNormalSubgroup(W,FrattiniSubgroup(W));
  V:=Image(frnat); elsV:=AsSortedList(V); d:=Log(Size(V),3);
  GLsize:=Size(GL(d,3));

  agtriv:=ForAll(A.agAutos,
    alpha->ForAll(gens,g->Image(frnat,Image(alpha,g))=Image(frnat,g)));

  glperms:=List(A.glAutos,alpha->permOnV(alpha,frnat,elsV));
  L:=Group(glperms);
  IA:=Product(A.agOrder);
  Autorder:=A.size; GLorder:=Size(L);

  report:=rec(
    s:=s, a:=a, dimV:=d, GL3size:=GLsize,
    AutOrder:=Autorder,
    glOrderRecord:=A.glOrder,
    linearImageOrder:=GLorder,
    IAOrder:=IA,
    IAp3:=valuation(IA,3),
    Lp3:=valuation(GLorder,3),
    Autp3:=valuation(Autorder,3),
    agGeneratorsTrivialOnV:=agtriv,
    glOrderMatchesRecord:=(GLorder=A.glOrder),
    factorization:=(IA*GLorder=Autorder)
  );
  Print(report,"\n");
end;

for t in [[0,1],[1,1],[0,2],[1,2]] do run(t[1],t[2]); od;
QUIT;
