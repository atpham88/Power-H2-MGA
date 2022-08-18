*Michael Craig 14 May 2020

*Turn off output in .lst file
$offlisting
$offsymxref offsymlist
Options
         optcr = 1E-3
         reslim = 100000
         limcol = 0
         limrow = 0
*         threads = 0
         solprint = silent
         solvelink = 5
         ;

$include EDAndUCSharedFeatures.gms
$include StorageSetsParamsVariables.gms
$include UCFeatures.gms

Parameters
*Carried unit-specific parameters from last optimization
         pOnoroffinitial(egu)                    "whether plant is set to on or off in hour 1 from prior optimization"
         pMdtcarriedhours(egu)                   "MDT carried over from last optimization (hours)"
         pGenabovemininitial(egu)                "gen above min load from last period of prior optimization (GW)"
*Scalars
         pRegoffercost(egu)
*Storage initial SOC
         pInitsoc(storageegu)            initial state of charge (GWh)
*Diagnostic parameters
         pModelstat
         pSolvestat
                ;

$if not set gdxincname $abort 'no include file name for data file provided'
$gdxin %gdxincname%
$load pOnoroffinitial,pMdtcarriedhours,pGenabovemininitial,pInitsoc,pRegoffercost
$gdxin

$include EDAndUCOpConstraintsExistingGens.gms
$include StorageUCModule.gms

Variable
         vZ                             total variable costs for new and existing plants = variable O&M + fuel + emission costs [thousandUSD per yr]
         ;

Equations
*Cost equations
         objfunc                         objective function = sum investment and variable costs
*Ramp constraints
         rampconstraintup(egu,h)                 "ramping up constraint for t>1"
         rampconstraintdown(egu,h)               "ramping down constraint for t>1"
*Commitment constraints
         statusofplant(egu,h)                    "balance whether thermal plant is on or off with whether shutting down or starting up"
         enforcemindowntime(egu,h)               "make sure plant once it turns off doesn't turn back on before MDT passes"
         enforcemindowntimecarryover(egu,h)      "enforce MDT from turn off decisions in prior optimization"
         ;

******************OBJECTIVE FUNCTION******************
*Minimize total operational cost
objfunc .. vZ =e= sum(h,pCnse*vNse(h)) + sum((egu,h),vVarcost(egu,h))
                 + sum((egu,h), pStartupfixedcost(egu)*vTurnon(egu,h) + vRegup(egu,h)*pRegoffercost(egu));
******************************************************

******************RAMPING CONSTRAINTS******************
*Ensure plants are limited to their ramping speed
rampconstraintup(egu,h)$[ORD(h)>1] .. (vGenabovemin(egu,h) + vFlex(egu,h) + vCont(egu,h) + vRegup(egu,h)) - vGenabovemin(egu,h-1)$[ORD(h)>1] - pGenabovemininitial(egu)$[ORD(h)=1] =l= pRamprate(egu);
rampconstraintdown(egu,h)$[ORD(h)>1] .. (vGenabovemin(egu,h-1)$[ORD(h)>1] + pGenabovemininitial(egu)$[ORD(h)=1] - vGenabovemin(egu,h)) =l= pRamprate(egu);
*******************************************************

******************ON/OFF CONSTRAINTS******************
*Constrains status of plant per whether it's on off, turning on, or shutting down
statusofplant(egu,h) .. vOnoroff(egu,h) =e= pOnoroffinitial(egu)$[ORD(h)=1]+vOnoroff(egu,h-1)$[ORD(h)>1]+vTurnon(egu,h)-vTurnoff(egu,h);

*Limit plant to not start up until it reaches its min down time
enforcemindowntime(egu,h)$[ORD(h)>pMdtcarriedhours(egu)] .. 1-vOnoroff(egu,h) =g= sum(hh$[ORD(hh)<=ORD(h) and ORD(hh)>(ORD(h)-pMindowntime(egu))],vTurnoff(egu,hh));

*Enforce MDT hours carried over from last optimization
enforcemindowntimecarryover(egu,h)$[ORD(h)<=pMdtcarriedhours(egu)] .. vOnoroff(egu,h) =l= 0;
******************************************************

Model unitCommitment includes all equations /all/;
solve unitCommitment using mip minimizing vZ;

pModelstat = unitCommitment.Modelstat;
pSolvestat = unitCommitment.solvestat;
