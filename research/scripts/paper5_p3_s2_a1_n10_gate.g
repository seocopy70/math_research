Read("research/external/paper5_aut/aut_common.g");
run:=function(s,a)
  local o,K,comp,R,W,gens,Q,AQ,A,els,nQ,perms,beta,XS,kid,key,nk,t,orb,p,k0,reps,i,j,gensA,pi,imgs,newt,kidnew,parent,find,union,orbits,cnt,sizes,al,W2,stab,r,tm,perm,ind;
  tm:=Runtime(); R:=winW(mkG(s,a),4,4); W:=R[1]; gens:=R[2]; Q:=winW(mkD(a),4,8)[1]; els:=AsSortedList(Q); nQ:=Length(els);
  ind:=function(e) return PositionSorted(els,e); end; AQ:=AutomorphismGroup(Q); perms:=List(AsList(AQ),b->List(els,e->ind(Image(b,e)))); XS:=epis(s,a,Q);
  key:=function(t) return ((ind(t[1])-1)*nQ+(ind(t[2])-1))*nQ+ind(t[3]); end; kid:=ListWithIdenticalEntries(nQ^3,0); nk:=0; reps:=[];
  for t in XS do if kid[key(t)]=0 then nk:=nk+1; Add(reps,t); for p in perms do kid[((p[ind(t[1])]-1)*nQ+(p[ind(t[2])]-1))*nQ+p[ind(t[3])]]:=nk; od; fi; od;
  Print("s=",s," a=",a," kernels=",nk,"  (",(Runtime()-tm)/1000.0,"s)\n"); A:=AutomorphismGroupPGroup(W); gensA:=Concatenation(A.glAutos,A.agAutos); W2:=Subgroup(W,gens); parent:=[1..nk];
  find:=function(i) while parent[i]<>i do i:=parent[i]; od; return i; end;
  for i in [1..nk] do imgs:=reps[i]; pi:=GroupHomomorphismByImagesNC(W2,Q,gens,imgs); for al in gensA do newt:=List(gens,g->Image(pi,Image(al,g))); j:=kid[key(newt)]; if j=0 then Print("  action left admissible set?!\n"); else if find(i)<>find(j) then parent[find(i)]:=find(j); fi; fi; od; od;
  orbits:=Collected(List([1..nk],i->find(i))); Print("   Aut(W)-orbits on admissible kernels: sizes ",List(orbits,o->o[2]),"\n"); Print("   |Aut W|=",A.size,"  stabilizer orders: ",List(orbits,o->A.size/o[2]),"\n");
  for o in orbits do i:=Position(List([1..nk],x->find(x)),o[1]); imgs:=reps[i]; pi:=GroupHomomorphismByImagesNC(W2,Q,gens,imgs); K:=Kernel(pi); comp:=ComplementClassesRepresentatives(W,K); Print("   orbit of size ",o[2],": |K|=3^",Log(Size(K),3),"  K abelian: ",IsAbelian(K),"  complements(classes)=",Length(comp),"\n"); od;
  if nk=81 and Length(orbits)=1 and orbits[1][2]=81 and Length(AsList(ComplementClassesRepresentatives(W,Kernel(GroupHomomorphismByImagesNC(W2,Q,gens,reps[1])))))=59049 then
    Print("P5_N10_ORBIT_CERTIFICATE=PASS\n");
  else
    Error("P5_N10_ORBIT_CERTIFICATE_FAILURE");
  fi;
end; run(2,1); Print("P5_N10_ORBIT_CERTIFICATE=PASS\n"); QUIT;
