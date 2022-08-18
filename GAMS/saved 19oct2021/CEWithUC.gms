*Michael Craig 16 Apr 2020

*$offlisting
*$offsymxref offsymlist
Options
         optcr = 1E-3
         reslim = 100000
*         limcol = 0
*         limrow = 0
         threads = 0
*         solprint = silent
*         solvelink = 5
         ;

$include CESharedFeatures.gms
$include UCFeatures.gms
$include StorageUCModule.gms

Parameters
*Commitment parameters
         pMinloadtech(tech)                           "minimum load of EGU (GW)"
         pStartupfixedcosttech(tech)                  "start up cost of EGU (thousands$)"
         pMindowntimetech(tech)                       "MDT (hours)"
*Diagnostic parameters
         pModelstat
         pSolvestat
		;

$if not set gdxincname $abort 'no include file name for data file provided'
$gdxin %gdxincname%
$load pMinloadtech, pStartupfixedcosttech, pMindowntimetech
$gdxin

Variables
*Total cost variables
         vZannual                              obj func [thousandUSD per yr]
         vFixedcostannual                             total investment costs for new plants = fixed O&M + overnight capital costs [thousandUSD per yr]
		;

Positive Variables
*Commitment variables
         vGenabovemintech(tech,h)        hourly electricity generation above min load by new plants [GWh]
         vTurnofftech(tech,h)            number of new plants that turn off
		 ;
		 
Integer Variables
*Commitment variables
         vOnorofftech(tech,h)            number of new plants that are on
         vTurnontech(tech,h)             number of new plants that turn on
         ;

$include CETimeDependentConstraints.gms

Equations		
*Cost equations
         objfunc                         objective function = sum investment and variable costs
         investmentcost                  calculate investment costs = fixed O&M + annualized capital costs
*Commitment constraints
		 limitCommitmentToBuilt(tech,h)
		 limitTurnOnToBuilt(tech,h)
		 limitTurnOffToBuilt(tech,h)
*Generation and reserve constraints
         setgentech(tech,h)              set electricity generation by new plants
         setgenabovemintech(tech,h)      set electricity generation above min load by new plants
         limitflexrestech(tech,h)        limit spin reserves by new plants by ramp rate
         limitcontrestech(tech,h)        limit cont reserves by new plants by ramp rate
         limitreguprestech(tech,h)       limit reg reserves by new plants by ramp rate
         limitallresuptech(tech,h)       limit total generation plus reserves of new plants to capacity
*Renewable generation
         setrenewgentech(renewtech,h)    set electricity generation by new renewable generators
*Storage constraints
		limitStoTechGen(storagetech,h)
		limitStoTechCharge(storagetech,h)
		stoTechSOCFloor(storagetech,h)
		stoTechSOCLimit(storagetech,h)
        limitstorageresuptech(storagetech,h)		 
		limitregupstoragetoramptech(storagetech,h)
		limitflexstoragetoramptech(storagetech,h)
		limitcontstoragetoramptech(storagetech,h)
*CO2 emissions cap
         enforceco2emissionscap          restrict total co2 emissions to cap
		 ;

******************CALCULATE COSTS (OBJ FUNC)**********
*Objective: minimize fixed + variable costs
objfunc..                vZannual =e= vFixedcostannual + vVarcostannual;
**************************************************

***************** LIMIT COMMITMENT TO BUILD DECISIONS**************
limitCommitmentToBuilt(tech,h) .. vOnorofftech(tech,h) =l= vN(tech);
limitTurnOnToBuilt(tech,h) .. vTurnontech(tech,h) =l= vN(tech);
limitTurnOffToBuilt(tech,h) .. vTurnofftech(tech,h) =l= vN(tech);
*******************************************************************

******************GENERATION AND RESERVE CONSTRAINTS******************
*Limit gen and genabovemin which account for # units on in each tech set
setgentech(tech,h)..  vGentech(tech,h) =e= vOnorofftech(tech,h)*pMinloadtech(tech)+vGenabovemintech(tech,h);
setgenabovemintech(tech,h) .. vGenabovemintech(tech,h) =l= (pCapactech(tech)-pMinloadtech(tech))*vOnorofftech(tech,h);

*Renewable generation limited by CF capacity and number built
setrenewgentech(renewtech,h)..          vGentech(renewtech,h) =l= vOnorofftech(renewtech,h)*pCapactech(renewtech)*pCf(renewtech,h);

*Limit spinning and regulation reserves each to ramp capability and time of reserve
limitflexrestech(nonstoragetech,h)$[pMaxflexoffertech(nonstoragetech)>0].. vFlextech(nonstoragetech,h) =l= pMaxflexoffertech(nonstoragetech)*vOnorofftech(nonstoragetech,h);
limitcontrestech(nonstoragetech,h)$[pMaxcontoffertech(nonstoragetech)>0].. vConttech(nonstoragetech,h) =l= pMaxcontoffertech(nonstoragetech)*vOnorofftech(nonstoragetech,h);
limitreguprestech(nonstoragetech,h)$[pMaxregupoffertech(nonstoragetech)>0].. vReguptech(nonstoragetech,h) =l= pMaxregupoffertech(nonstoragetech)*vOnorofftech(nonstoragetech,h);

*Limit spinning and regulation up reserves together to spare capacity
limitallresuptech(tech,h).. vGentech(tech,h) + vFlextech(tech,h) + vConttech(tech,h) + vReguptech(tech,h) =l= pCapactech(tech) * vOnorofftech(tech,h);
********************************************************************

******************STORAGE CONSTRAINTS******************
*Bound generation (based on market participation) charging and SOC
limitStoTechGen(storagetech,h) .. vGentech(storagetech,h) =l= pStoinenergymarket*pCapactech(storagetech)*vOnorofftech(storagetech,h);
limitStoTechCharge(storagetech,h) .. vChargetech(storagetech,h) =l= pCapacchargetech(storagetech) * (vN(storagetech)-vOnorofftech(storagetech,h));
stoTechSOCFloor(storagetech,h) .. vStateofchargetech(storagetech,h) =g= pMinsoctech(storagetech)*vN(storagetech);
stoTechSOCLimit(storagetech,h) .. vStateofchargetech(storagetech,h) =l= pMaxsoctech(storagetech)*vN(storagetech);

*Limit up reserves to spare capacity plus charging
limitstorageresuptech(storagetech,h) .. vReguptech(storagetech,h) + vFlextech(storagetech,h) + vConttech(storagetech,h) =l= (pCapactech(storagetech)*vOnorofftech(storagetech,h) - vGentech(storagetech,h)) + vChargetech(storagetech,h);

*Limit reserves to ramp capabilities and market participation
limitregupstoragetoramptech(storagetech,h) .. vReguptech(storagetech,h) =l= pMaxregupoffertech(storagetech)*vN(storagetech);
limitflexstoragetoramptech(storagetech,h) .. vFlextech(storagetech,h) =l= pMaxflexoffertech(storagetech)*vN(storagetech);
limitcontstoragetoramptech(storagetech,h) .. vConttech(storagetech,h) =l= pMaxcontoffertech(storagetech)*vN(storagetech);
*******************************************************

******************CO2 EMISSIONS CONSTRAINT******************
*Meet emissions cap
enforceco2emissionscap.. vCO2emsannual =l= pCO2emcap;
************************************************************

Model ceWithUC includes all equations /all/;
solve ceWithUC using mip minimizing vZannual;

pModelstat = ceWithUC.Modelstat;
pSolvestat = ceWithUC.solvestat;