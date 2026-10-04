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
  return PermList(List(imgs,v->Position(elsV,v)));
end;

valuation:=function(N,p) local v; v:=0; while N mod p=0 do N:=N/p; v:=v+1; od; return v; end;

run:=function(s,a)
  local R,W,gens,A,V,frnat,elsV,AutG,autGens,autImages,L,IAkernel,act,agtriv,
        GLorder,Autorder,report,GLsize,pred,dimVok,genCheck,fullGenCheck;
  R:=winW(mkG(s,a),4,4); W:=R[1]; gens:=R[2];
  A:=AutomorphismGroupPGroup(W);
  frnat:=NaturalHomomorphismByNormalSubgroup(W,FrattiniSubgroup(W));
  V:=Image(frnat); elsV:=AsSortedList(V);
  d:=0; pred:=Size(V); while pred mod 3=0 do pred:=pred/3; d:=d+1; od;
  dimVok:=(pred=1);
  GLsize:=Size(GL(d,3));
  genCheck:=(Size(Group(gens))=Size(W));

  agtriv:=ForAll(A.agAutos,
    alpha->ForAll(gens,g->Image(frnat,Image(alpha,g))=Image(frnat,g)));

  AutG:=Group(Concatenation(A.glAutos,A.agAutos));
  fullGenCheck:=(Size(AutG)=A.size);
  autGens:=GeneratorsOfGroup(AutG);
  autImages:=List(autGens,alpha->permOnV(alpha,frnat,elsV));
  if ForAny(autImages,p->p=fail) then Error("induced Frattini action produced fail"); fi;
  L:=Group(autImages);
  GLorder:=Size(L);
  act:=GroupHomomorphismByImages(AutG,L,autGens,autImages);
  IAkernel:=Kernel(act);
  Autorder:=A.size;

  report:=rec(
    s:=s, a:=a, dimV:=d, GL3size:=GLsize,
    AutOrder:=Autorder,
    glAutosCount:=Length(A.glAutos),
    agAutosCount:=Length(A.agAutos),
    glOrderRecord:=A.glOrder,
    agOrder:=A.agOrder,
    linearImageOrder:=GLorder,
    WGeneratorCheck:=genCheck,
    dimVExact:=dimVok,
    IAKernelOrder:=Size(IAkernel),
    IAKernelp3:=valuation(Size(IAkernel),3),
    Lp3:=valuation(GLorder,3),
    Autp3:=valuation(Autorder,3),
    agGeneratorsTrivialOnV:=agtriv,
    glOrderMatchesLinearImage:=(GLorder=A.glOrder),
    fullAutGeneration:=fullGenCheck,
    factorization:=(Size(IAkernel)*GLorder=Autorder)
  );
  Print("=== Paper5 IA/GL audit s=",s," a=",a," ===\\n");
  Print(report,"\\n");
end;

for t in [[0,1],[1,1],[0,2],[1,2]] do run(t[1],t[2]); od;
QUIT;

# CI trigger: execution requested 2026-10-04.

# Audit trigger: 2026-10-04 Paper 5 takeover.

# CI trigger: 2026-10-04 16:58 KST — execute authoritative IA/GL gate.
# Audit trigger: Paper 5 takeover; no order-arithmetic promotion without runtime verification.
