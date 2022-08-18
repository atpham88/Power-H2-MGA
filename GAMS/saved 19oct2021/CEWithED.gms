*Michael Craig 16 Apr 2020

*$offlisting
*$offsymxref offsymlist
Options
         optcr = 1E-3
         reslim = 100000
                 threads = 0
         solvelink = 5
         limcol = 999
         limrow = 999
*         solprint = silent
         ;

$include CESharedFeatures.gms
$include StorageEDModule.gms
$include EDVarsAndConstraints.gms
$include CETimeDependentConstraints.gms

Parameters
*DIAGNOSTIC PARAMETERS
         pModelstat
         pSolvestat
                ;

Variables
*Total cost variables
         vZannual                              obj func [thousandUSD per yr]
                ;

Equations
*Cost equations
         objfunc                         objective function = sum investment and variable costs
         investmentcost                  calculate investment costs = fixed O&M + annualized capital costs
*Generation and reserve constraints
         limitflexrestech(tech,h)        limit spin reserves by new plants by ramp rate
         limitcontrestech(tech,h)        limit cont reserves by new plants by ramp rate
         limitreguprestech(tech,h)       limit reg reserves by new plants by ramp rate
         limitallresuptech(tech,h)       limit total generation plus reserves of new plants to capacity
                 limitdacsgen(dacstech,h)
*Renewable generation
         setrenewgentech(renewtech,h)    set electricity generation by new renewable generators
*Storage constraints
                limitStoTechGen(storagetech,h)
                limitStoTechCharge(storagetech,h)
                stoTechSOCLimit(storagetech,h)
        limitstorageresuptech(storagetech,h)
*CO2 emissions cap
         enforceco2emissionscap          restrict total co2 emissions to cap
                 ;

******************CALCULATE COSTS (OBJ FUNC)**********
*Objective: minimize fixed + variable costs
objfunc..                vZannual =e= vFixedcostannual + vVarcostannual;
**************************************************

******************GENERATION AND RESERVE CONSTRAINTS******************
*Limit spinning and regulation reserves each to ramp capability and time of reserve
limitflexrestech(tech,h)$[pMaxflexoffertech(tech)>0].. vFlextech(tech,h) =l= pMaxflexoffertech(tech)*vN(tech);
limitcontrestech(tech,h)$[pMaxcontoffertech(tech)>0].. vConttech(tech,h) =l= pMaxcontoffertech(tech)*vN(tech);
limitreguprestech(tech,h)$[pMaxregupoffertech(tech)>0].. vReguptech(tech,h) =l= pMaxregupoffertech(tech)*vN(tech);

*Limit up reserves plus generation to spare capacity for generating technologies
limitallresuptech(gentechs,h).. vGentech(gentechs,h) + vFlextech(gentechs,h) + vConttech(gentechs,h) + vReguptech(gentechs,h) =l= pCapactech(gentechs) * vN(gentechs);

*Limit DACS generation and reserves
limitdacsgen(dacstech,h).. vGentech(dacstech,h) =g= pCapactech(dacstech)*vN(dacstech);

*Limit new wind and solar generation
setrenewgentech(renewtech,h)..   vGentech(renewtech,h) =l= pCapactech(renewtech)*pCf(renewtech,h)*vN(renewtech);
********************************************************************

******************STORAGE CONSTRAINTS******************
*Bound generation (based on market participation) charging and SOC
limitStoTechGen(storagetech,h) .. vGentech(storagetech,h) =l= pStoinenergymarket*vPowBuiltSto(storagetech);
limitStoTechCharge(storagetech,h) .. vChargetech(storagetech,h) =l= vPowBuiltSto(storagetech)*pChargeDischargeCapRatio;
stoTechSOCLimit(storagetech,h) .. vStateofchargetech(storagetech,h) =l= vEneBuiltSto(storagetech);

*Limit up reserves to spare capacity plus charging
limitstorageresuptech(storagetech,h) .. vReguptech(storagetech,h) + vFlextech(storagetech,h) + vConttech(storagetech,h) =l= (vPowBuiltSto(storagetech) - vGentech(storagetech,h)) + vChargetech(storagetech,h);
*******************************************************

******************CO2 EMISSIONS CONSTRAINT******************
*Meet emissions cap
enforceco2emissionscap.. vCO2emsannual =l= pCO2emcap;
************************************************************

Model ceWithED includes all equations /all/;
solve ceWithED using lp minimizing vZannual;

pModelstat = ceWithED.Modelstat;
pSolvestat = ceWithED.solvestat;
