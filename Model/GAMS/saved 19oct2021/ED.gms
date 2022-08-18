*Michael Craig 16 Apr 2020

*$offlisting
*$offsymxref offsymlist
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
$include StorageEDModule.gms

Parameters
*Storage initial SOC
         pInitsoc(storageegu)            initial state of charge (GWh)
*Diagnostic parameters
         pModelstat
         pSolvestat
         ;

$if not set gdxincname $abort 'no include file name for data file provided'
$gdxin %gdxincname%
$load pInitsoc
$gdxin

$include EDVarsAndConstraints.gms
$include EDAndUCOpConstraintsExistingGens.gms

Variable
         vZ                             total variable costs for new and existing plants = variable O&M + fuel + emission costs [thousandUSD per yr]
         ;

Equations
*Cost equations
         objfunc                         objective function = sum investment and variable costs
*Ramp limits
         limitrampup(egu,h)
         limitrampdown(egu,h)
         ;

******************OBJECTIVE FUNCTION******************
*Objective: minimize fixed + variable costs
objfunc..                vZ =e= sum((egu,h),vVarcost(egu,h)) + sum(h,vNse(h)*pCnse);
******************************************************

******************RAMP CONSTRAINTS******************
*EXISTING UNITS
*Ensure plants are limited to their ramping speed
limitrampup(egu,h)$[ORD(h)>1] .. vGen(egu,h)+vRegup(egu,h)+vFlex(egu,h)+vCont(egu,h)-vGen(egu,h-1) =l= pRamprate(egu);
limitrampdown(egu,h)$[ORD(h)>1] .. (vGen(egu,h-1)-vGen(egu,h)) =l= pRamprate(egu);
****************************************************

Model econDispatch includes all equations /all/;
solve econDispatch using lp minimizing vZ;

pModelstat = econDispatch.Modelstat;
pSolvestat = econDispatch.solvestat;
