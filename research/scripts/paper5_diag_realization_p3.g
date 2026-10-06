LoadPackage("autpgrp");
p:=3;
F:=FreeGroup("z","x","y"); z:=F.1; x:=F.2; y:=F.3;
G:=F/[z^p*(x^p*Comm(x,y))^-1];
qs:=PQuotient(G,p,p); ep:=EpimorphismQuotientSystem(qs); W:=Image(ep);
gens:=List([z,x,y],g->Image(ep,g));
A:=AutomorphismGroupPGroup(W);
phi:=NaturalHomomorphismByNormalSubgroup(W,FrattiniSubgroup(W));
V:=Image(phi);
els:=GeneratorsOfGroup(V);
# coordinate vectors by fixed generators of V
coords:=function(v)
  local w;
  w:=Factorization(V,v);
  return List(gens,i->0);
end;
matof:=function(alpha)
  local imgs,cols,v,j;
  imgs:=List(gens,g->Image(alpha,g));
  cols:=List(imgs,g->List(gens,h->LogVector(phi,Image(phi,g),Image(phi,h))));
  return cols;
end;
# use explicit quotient coordinate vectors from pcgs
pc:=Pcgs(V);
vec:=function(v) return ExponentsOfPcElement(pc,v); end;
matof:=function(alpha)
  local imgs;
  imgs:=List(gens,g->Image(phi,Image(alpha,g)));
  return TransposedMat(List(imgs,vec));
end;
Ag:=GeneratorsOfGroup(A);
Ms:=List(Ag,a->matof(a));
GL:=Group(Ms);
target:=ImmutableMatrix(GF(3),[[2,0,0],[0,1,0],[0,0,2]]);
# target lies in GL image if equality local certificate holds
if not target in GL then Error("target diag not in image"); fi;
hm:=GroupHomomorphismByImages(A,GL,Ag,Ms);
aa:=PreImagesRepresentative(hm,target);
Print("DIAG_TARGET_MATRIX=",target,"\n");
Print("DIAG_IMAGE_X=",Image(aa,gens[2]),"\n");
Print("DIAG_IMAGE_Y=",Image(aa,gens[3]),"\n");
Print("DIAG_IMAGE_Z=",Image(aa,gens[1]),"\n");
Print("DIAG_CERT=PASS_LOCAL\n");
QUIT;
