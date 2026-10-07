if LoadPackage("anupq") <> true then
  Error("ANUPQ package not loaded");
fi;
Print("ANUPQ_CAPABILITY=PASS\n");
p:=5;
F:=FreeGroup("z","x","y");
z:=F.1; x:=F.2; y:=F.3;
G:=F/[z^p*(x^(p^2)*Comm(x,y))^-1];

# The default PQuotient collector/order bound is too small for this
# presentation at classes 7 and 8.  Use the documented larger order
# bound and combinatorial collector explicitly.
for n in [7,8] do
  Print("TRY_PQUOTIENT_N=",n,"\n");
  qs:=PQuotient(G,p,n,1024,"combinatorial");
  if qs=fail then Error("PQuotient returned fail"); fi;
  Print("ANUPQ_PQUOTIENT_N",n,"=PASS\n");
od;
QUIT;
