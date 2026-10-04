# Paper 4 Q-invariant stress probe
LoadPackage("autpgrp");
Print("GAP=",GAPInfo.Version,"\n");
# Construction: G_u = <z,x | z^(p^u)=x^p>, W_u = G_u/D_{p^s+1}.
# This probe records the two finite windows; exhaustive Q counting is intentionally
# a separate implementation because subgroup enumeration is the expensive step.
run:=function(p,s,t)
 local F,Gs,Gt,qs,qt,es,et,Ws,Wt;
 F:=FreeGroup("z","x");
 Gs:=F/[F.1^(p^s)*F.2^(-p)];
 Gt:=F/[F.1^(p^t)*F.2^(-p)];
 qs:=PQuotient(Gs,p,p^s+1); qt:=PQuotient(Gt,p,p^s+1);
 es:=EpimorphismQuotientSystem(qs); et:=EpimorphismQuotientSystem(qt);
 Ws:=Image(es); Wt:=Image(et);
 Print("p=",p," s=",s," t=",t,
       " |Ws|=",Size(Ws)," |Wt|=",Size(Wt),"\n");
end;
run(3,1,2);
run(5,1,2);
QUIT;
