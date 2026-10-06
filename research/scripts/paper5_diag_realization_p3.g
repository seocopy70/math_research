LoadPackage("autpgrp");
p:=3;
F:=FreeGroup("z","x","y"); z:=F.1; x:=F.2; y:=F.3;
G:=F/[z^p*(x^p*Comm(x,y))^-1];
qs:=PQuotient(G,p,p); ep:=EpimorphismQuotientSystem(qs); W:=Image(ep);
gens:=List(GeneratorsOfGroup(G),g->Image(ep,g));
A:=AutomorphismGroupPGroup(W);
phi:=NaturalHomomorphismByNormalSubgroup(W,FrattiniSubgroup(W));
V:=Image(phi); pc:=Pcgs(V);
vec:=v->ExponentsOfPcElement(pc,v);
matof:=function(alpha)
  local imgs;
  imgs:=List(gens,g->Image(phi,Image(alpha,g)));
  return TransposedMat(List(imgs,vec));
end;
Ag:=Concatenation(A.glAutos,A.agAutos);
target:=ImmutableMatrix(GF(3),[[2,0,0],[0,1,0],[0,0,2]]);
id:=IdentityMapping(W);
queue:=[id]; qmat:=[matof(id)]; qidx:=1; found:=fail;
while qidx<=Length(queue) and found=fail do
  cur:=queue[qidx]; cm:=qmat[qidx]; qidx:=qidx+1;
  if cm=target then found:=cur; break; fi;
  for gg in Ag do
    nxt:=cur*gg; nm:=matof(nxt);
    if not nm in qmat then
      Add(queue,nxt); Add(qmat,nm);
    fi;
  od;
od;
if found=fail then Print("DIAG_IMAGE_MATRICES=",qmat,"\\n"); Error("diag target not reached"); fi;
Print("DIAG_TARGET=",target,"\\n");
Print("DIAG_X=",Image(found,gens[2]),"\\n");
Print("DIAG_Y=",Image(found,gens[3]),"\\n");
Print("DIAG_Z=",Image(found,gens[1]),"\\n");
Print("DIAG_CERT=PASS_LOCAL\n");
QUIT;
