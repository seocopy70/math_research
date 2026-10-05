Read("research/external/paper5_aut/aut_common.g");

runCase:=function(s,a)
  local R,W,gens,Q,elsQ,A,gensA,A2,XS,p,Act,rho,orbits,repIdx,pi,K,S,qgens,qels,
        imgsQ,beta,qperms,L,imSize,kerSize,idx,t,newt,alpha,i,orbitSizes,actOnK;

  R:=winW(mkG(s,a),4,4); W:=R[1]; gens:=R[2];
  Q:=winW(mkD(a),4,8)[1]; elsQ:=AsSortedList(Q);
  A:=AutomorphismGroupPGroup(W); gensA:=Concatenation(A.glAutos,A.agAutos); A2:=Group(gensA);
  if Size(A2)<>A.size then Error("Aut generator group size mismatch"); fi;

  XS:=epis(s,a,Q); if Length(XS)=0 then Error("no admissible kernels"); fi;

  p:=List(gensA,function(alpha)
    return PermList(List([1..Length(XS)],function(i)
      local pi0,newt;
      pi0:=GroupHomomorphismByImagesNC(W,Q,gens,XS[i]);
      newt:=List(gens,g->Image(pi0,Image(alpha,g)));
      return Position(XS,newt);
    end));
  end);
  Act:=Group(p);
  rho:=GroupHomomorphismByImages(A2,Act,gensA,p);

  orbits:=Orbits(Act,[1..Length(XS)],OnPoints);
  orbitSizes:=List(orbits,Length);
  Print("CASE s=",s," a=",a," kernels=",Length(XS)," orbit sizes=",orbitSizes,"\n");

  actOnK:=function(g,i) return i^Image(rho,g); end;
  for idx in [1..Length(orbits)] do
    repIdx:=orbits[idx][1]; t:=XS[repIdx];
    pi:=GroupHomomorphismByImagesNC(W,Q,gens,t); K:=Kernel(pi);
    S:=Stabilizer(A2,repIdx,actOnK);
    if Size(S)*Length(orbits[idx])<>A.size then Error("orbit-stabilizer mismatch"); fi;

    qgens:=List(gens,g->Image(pi,g)); qels:=elsQ; qperms:=[];
    for alpha in GeneratorsOfGroup(S) do
      imgsQ:=List(gens,g->Image(pi,Image(alpha,g)));
      beta:=GroupHomomorphismByImagesNC(Q,Q,qgens,imgsQ);
      Add(qperms,PermList(List(qels,q->Position(qels,Image(beta,q)))));
    od;
    L:=Group(qperms); imSize:=Size(L); kerSize:=Size(S)/imSize;
    Print("  orbit ",idx," size=",Length(orbits[idx]),
          " |K|=",Size(K)," |Stab|=",Size(S),
          " |Im Aut(W)->Aut(Q)|=",imSize,
          " |Ker|=",kerSize,"\n");
  od;
  Print("P5_QUOTIENT_ACTION_CASE s=",s," a=",a," PASS\n");
end;

runCase(1,1);
runCase(1,2);
runCase(2,1);
Print("P5_QUOTIENT_ACTION_CERTIFICATE=PASS\n");
QUIT;
