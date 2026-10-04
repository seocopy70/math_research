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
  local R,W,gens,A,AutW,V,frnat,basis,matOf,glMats,L,ker,gensA,imgsA,homA,
        genCheck,agtriv,genFixKernel,fullGenCheck,Autorder,GLorder,IAorder,
        report,d,GL3size;
  R:=winW(mkG(s,a),4,4); W:=R[1]; gens:=R[2];
  A:=AutomorphismGroupPGroup(W);
  AutW:=AutomorphismGroup(W);
  frnat:=NaturalHomomorphismByNormalSubgroup(W,FrattiniSubgroup(W));
  V:=Image(frnat); basis:=Pcgs(V); d:=Length(basis); GL3size:=Size(GL(d,3));

  genCheck:=Size(Group(gens))=Size(W);
  matOf:=function(alpha) local rows,b,img;
    rows:=[];
    for b in basis do
      img:=Image(frnat,Image(alpha,PreImagesRepresentative(frnat,b)));
      Add(rows,ExponentsOfPcElement(basis,img));
    od;
    return Matrix(GF(3),rows);
  end;

  glMats:=List(A.glAutos,matOf);
  L:=GL(d,3);
  IAorder:=Product(A.agOrder);
  gensA:=GeneratorsOfGroup(AutW);
  imgsA:=List(gensA,matOf);
  homA:=GroupHomomorphismByImages(A,L,gensA,imgsA);
  L:=Image(homA);
  ker:=Kernel(homA);
  GLorder:=Size(L); Autorder:=Size(AutW);

  agtriv:=ForAll(A.agAutos,alpha->matOf(alpha)=IdentityMat(d,GF(3)));
  genFixKernel:=IAorder=Size(ker) and ForAll(A.agAutos,alpha->Image(homA,alpha)=One(L));
  fullGenCheck:=Autorder=A.glOrder*IAorder and A.size=Autorder;

  report:=rec(
    s:=s, a:=a, dimV:=d, GL3size:=GL3size,
    WOrder:=Size(W),
    generatorsGenerateW:=genCheck,
    AutOrder:=Autorder,
    hybridAutOrder:=A.size,
    glOrderRecord:=A.glOrder,
    linearImageOrder:=GLorder,
    IAOrder:=IAorder,
    kernelOrder:=Size(ker),
    IAp3:=valuation(IAorder,3),
    Lp3:=valuation(GLorder,3),
    Autp3:=valuation(Autorder,3),
    agGeneratorsTrivialOnV:=agtriv,
    IAEqualsKernel:=genFixKernel,
    glPlusAgGenerateAut:=fullGenCheck,
    glOrderMatchesRecord:=(GLorder=A.glOrder),
    factorization:=(IAorder*GLorder=Autorder)
  );
  Print(report,"\\n");
end;

for t in [[0,1],[1,1],[0,2],[1,2]] do run(t[1],t[2]); od;
QUIT;
