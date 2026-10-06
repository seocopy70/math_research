LoadPackage("autpgrp");
p:=3;
F:=FreeGroup("z","x","y"); z:=F.1; x:=F.2; y:=F.3;
G:=F/[z^p*(x^p*Comm(x,y))^-1];
qs:=PQuotient(G,p,p); ep:=EpimorphismQuotientSystem(qs); W:=Image(ep);
gens:=List(GeneratorsOfGroup(G),g->Image(ep,g));
A:=AutomorphismGroupPGroup(W);
phi:=NaturalHomomorphismByNormalSubgroup(W,FrattiniSubgroup(W));
V:=Image(phi); pc:=Pcgs(V);
vcoords:=function(v)
  return List(ExponentsOfPcElement(pc,v),e->
    [0*Z(3),Z(3)^0,Z(3)^2][e+1]);
end;
gensV:=List(gens,g->Image(phi,g));
B:=TransposedMat(List(gensV,v->vcoords(v)));
B:=B;
matof:=function(alpha)
  local imgs,C;
  imgs:=List(gens,g->Image(phi,Image(alpha,g)));
  C:=TransposedMat(List(imgs,v->vcoords(v)));
  return InverseMat(B)*C;
end;
Ag:=Concatenation(A.glAutos,A.agAutos);
target:=ImmutableMatrix(GF(3),[[2,0,0],[0,2,0],[0,0,1]]);
id:=IdentityMapping(W);
queue:=[id]; qmat:=[matof(id)]; qidx:=1; found:=fail;
while qidx<=Length(queue) and found=fail do
  cur:=queue[qidx]; cm:=qmat[qidx]; qidx:=qidx+1;
  if cm=target then found:=cur; break; fi;
  for gg in Ag do
    nxt:=cur*gg; nm:=matof(nxt);
    if ForAll(qmat,m->m<>nm) then Add(queue,nxt); Add(qmat,nm); fi;
  od;
od;
if found=fail then
  Print("DIAG_IMAGE_MATRICES=",qmat,"\\n");
  Error("diag target not reached");
fi;
Print("DIAG_TARGET_ZXY=",target,"\\n");
Print("DIAG_X=",Image(found,gens[2]),"\\n");
Print("DIAG_Y=",Image(found,gens[3]),"\\n");
Print("DIAG_Z=",Image(found,gens[1]),"\\n");
Print("DIAG_CERT=PASS_LOCAL\n");
QUIT;
