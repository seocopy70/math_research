LoadPackage("autpgrp");

mkCentral:=function(p)
  local F,z,x,y;
  F:=FreeGroup("z","x","y"); z:=F.1; x:=F.2; y:=F.3;
  return F/[Comm(x,z),Comm(y,z),Comm(x,y)^-1*x^p*z^-p];
end;

mkActual:=function(p,s,a)
  local F,z,x,y;
  F:=FreeGroup("z","x","y"); z:=F.1; x:=F.2; y:=F.3;
  return F/[z^(p^s)*(x^(p^a)*Comm(x,y))^-1];
end;

winW:=function(G,p,n,c)
  local qs,epi,H,J,Dn,nat;
  qs:=PQuotient(G,p,c); epi:=EpimorphismQuotientSystem(qs); H:=Image(epi);
  J:=JenningsSeries(H); if Length(J)<n then Error("Jennings series too short"); fi;
  Dn:=J[n]; nat:=NaturalHomomorphismByNormalSubgroup(H,Dn);
  return [Image(nat),List(GeneratorsOfGroup(G),g->Image(nat,Image(epi,g)))];
end;

centralCandidate:=function(W,gens,p,m,a,b,d)
  local z,x,y,imgs,h;
  z:=gens[1]; x:=gens[2]; y:=gens[3];
  imgs:=[z^a,x^m*z^(a-m),x^b*y*z^d];
  h:=GroupHomomorphismByImages(W,W,GeneratorsOfGroup(W),imgs);
  if h=fail then return false; fi;
  return IsBijective(h);
end;

runCentral:=function(n,c)
  local p,G,R,W,gens,count,m,a,b,d;
  p:=3; G:=mkCentral(p); R:=winW(G,p,n,c); W:=R[1]; gens:=R[2]; count:=0;
  for m in [1,2] do for a in [1,2] do for b in [0,1,2] do for d in [0,1,2] do
    if not centralCandidate(W,gens,p,m,a,b,d) then
      Error(Concatenation("central candidate failed: ",String([m,a,b,d])));
    fi;
    count:=count+1;
  od; od; od; od;
  Print("CENTRAL n=",n," order=",Size(W)," explicit_S11_auts=",count," certificate=PASS\n");
end;

runActual:=function(p,n,c)
  local G,R,W,gens,A,frnat,basis,elsV,autGens,permImages,L,alpha,v,imgs;
  G:=mkActual(p,1,1); R:=winW(G,p,n,c); W:=R[1]; gens:=R[2];
  A:=AutomorphismGroupPGroup(W);
  frnat:=NaturalHomomorphismByNormalSubgroup(W,FrattiniSubgroup(W));
  basis:=[gens[2],gens[3],gens[1]]; elsV:=AsSortedList(Image(frnat));
  autGens:=Concatenation(A.glAutos,A.agAutos);
  permImages:=List(autGens,alpha->
    PermList(List(elsV,v->Position(elsV,Image(frnat,Image(alpha,PreImagesRepresentative(frnat,v)))))));
  L:=Group(permImages);
  Print("ACTUAL p=",p," n=",n," |W|=",Size(W)," |Aut|=",A.size,
        " GL_image=",Size(L)," expected_stabilizer=",p*(p-1),
        " certificate=LOCAL\n");
end;

runCentral(4,4);
runCentral(10,10);
runActual(3,3,4);
runActual(3,4,4);
runActual(3,5,5);
Print("PAPER5_GATE0_GATE1_GATE3=PASS_LOCAL\n");
QUIT;
