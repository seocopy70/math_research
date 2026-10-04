LoadPackage("autpgrp");

mkG:=function(s,a) local F; F:=FreeGroup("z","x","y");
  if s=0 then return F/[(F.2^(3^a)*Comm(F.2,F.3))]; fi;
  return F/[F.1^(3^s)*(F.2^(3^a)*Comm(F.2,F.3))^-1]; end;

winW:=function(G,n,c) local qs,epi,H,J,Dn,nat;
  qs:=PQuotient(G,3,c); epi:=EpimorphismQuotientSystem(qs); H:=Image(epi);
  J:=JenningsSeries(H); Dn:=TrivialSubgroup(H); if Length(J)>=n then Dn:=J[n]; fi;
  nat:=NaturalHomomorphismByNormalSubgroup(H,Dn);
  return [Image(nat),List(GeneratorsOfGroup(G),g->Image(nat,Image(epi,g)))]; end;

valuation:=function(N,p) local v; v:=0; while N mod p=0 do N:=N/p; v:=v+1; od; return v; end;

run:=function(s,a)
  local R,W,gens,A,H,V,frnat,onV,homAll,homGL,IAcandidate,GLcandidate,
        ker,genCheck,IAorder,GLorder,Autorder,report,d,GL3size;
  R:=winW(mkG(s,a),4,4); W:=R[1]; gens:=R[2];
  A:=AutomorphismGroupPGroup(W);
  H:=ConvertHybridAutGroup(A);
  frnat:=NaturalHomomorphismByNormalSubgroup(W,FrattiniSubgroup(W));
  V:=Image(frnat); d:=Log(Size(V),3); GL3size:=Size(GL(d,3));

  genCheck:=Size(Group(gens))=Size(W);
  onV:=function(v,alpha)
    return Image(frnat,Image(alpha,PreImagesRepresentative(frnat,v)));
  end;

  homAll:=ActionHomomorphism(H,V,onV,"surjective");
  ker:=Kernel(homAll);
  IAcandidate:=Group(Concatenation(A.agAutos),A.one);
  GLcandidate:=Group(Concatenation(A.glAutos),A.one);
  homGL:=ActionHomomorphism(GLcandidate,V,onV,"surjective");

  IAorder:=Size(IAcandidate);
  GLorder:=Size(Image(homGL));
  Autorder:=Size(H);

  report:=rec(
    s:=s, a:=a, dimV:=d, GL3size:=GL3size,
    WOrder:=Size(W),
    generatorsGenerateW:=genCheck,
    AutOrder:=Autorder,
    hybridAutOrder:=A.size,
    IAOrderCandidate:=IAorder,
    IAKernelOrder:=Size(ker),
    glOrderRecord:=A.glOrder,
    linearImageOrder:=GLorder,
    IAp3:=valuation(IAorder,3),
    IAKernelp3:=valuation(Size(ker),3),
    Lp3:=valuation(GLorder,3),
    Autp3:=valuation(Autorder,3),
    IACandidateEqualsKernel:=(IAorder=Size(ker)),
    factorization:=(Size(ker)*GLorder=Autorder),
    hybridOrderConsistency:=(A.size=A.glOrder*Product(A.agOrder)),
    standardHybridSizeMatch:=(A.size=Autorder)
  );
  Print(report,"\\n");
end;
end;

for t in [[0,1],[1,1],[0,2],[1,2]] do run(t[1],t[2]); od;
QUIT;
