*Michael Craig 14 May 2020

Sets
*Existing generators
         egu                             existing generators
         windegu(egu)                    existing wind generators
         solaregu(egu)                   existing solar generators
         h                               hours
         ;

Parameters
*SIZE PARAMETERS [GW]
         pCapac(egu)                     hourly capacity of existing generators accounting for curtailments [GW]
*HEAT RATES [MMBtu/GWh]
         pHr(egu)                        heat rate of existing generators [MMBtu per GWh]
*COST PARAMETERS
         pOpcost(egu)                    total operational cost [thousandUSD per GWh] = VOM + FuelCost*HR + EmsCost*EmsRate*HR
*RAMP RATES [GW/hr]
         pRamprate(egu)                  up and down ramp rate of EGU [GW per hr]
*EMISSIONS RATES [short ton/MMBtu]
         pCO2emrate(egu)                 CO2 emissions rate of existing generators [short ton per MMBtu]
*EMISSIONS COST [$/short ton]
         pCO2cost
*RENEWABLE GENERATION CAPS
         pMaxgenwind(h)                  max hourly generation for existing wind [GWh]
         pMaxgensolar(h)                 max hourly generation for existing solar [GWh]
*HOURLY ELECTRICITY DEMAND [GWh]
         pDemand(h)                      hourly electricity demand [GWh]
         pDemandShifter                  demand shifter (percentage)
         pDemandShiftingBlock            demand shifting block
*COST OF NONSERVED ENERGY [THOUSAND$/GWH]
         pCnse                                   cost of non-served energy [thousandUSD per GWh]
*HOURLY RESERVE REQUIREMENTS [GW]
         pRegupreserves(h)         regulation up reserve [GW]
         pFlexreserves(h)
         pContreserves(h)
*RESERVE PROVISION PARAMETERS
*Convert ramp rate to reserve timeframe
         pRampratetoregreservescalar     converts ramp rate timeframe to reg reserve timeframe
         pRampratetoflexreservescalar    converts ramp rate timeframe to spin reserve timeframe
         pRampratetocontreservescalar    converts ramp rate timeframe to spin reserve timeframe
*Set whether generator can provide reserve
         pRegeligible(egu)               existing generators eligible to provide reg reserves [0] or not [1]
         pFlexeligible(egu)
         pConteligible(egu)
*Set max reserve offer based on eligibility and ramp rate
         pMaxflexoffer(egu)
         pMaxcontoffer(egu)
         pMaxregupoffer(egu)
         ;

$if not set gdxincname $abort 'no include file name for data file provided'
$gdxin %gdxincname%
$load egu, windegu, solaregu, h
$load pCapac, pHr, pOpcost, pRamprate, pCO2emrate, pCO2cost
$load pMaxgensolar, pMaxgenwind
$load pDemand, pDemandShifter, pDemandShiftingBlock, pCnse, pRegupreserves, pFlexreserves, pContreserves
$load pRampratetoregreservescalar, pRampratetoflexreservescalar, pRampratetocontreservescalar
$load pFlexeligible, pConteligible, pRegeligible
$gdxin

*CALCULATE MAX RESERVE OFFERS
pMaxflexoffer(egu) = pFlexeligible(egu)*pRamprate(egu)*pRampratetoflexreservescalar;
pMaxcontoffer(egu) = pConteligible(egu)*pRamprate(egu)*pRampratetocontreservescalar;
pMaxregupoffer(egu) = pRegeligible(egu)*pRamprate(egu)*pRampratetoregreservescalar;

Variables
                 vVarcost(egu,h)
                 ;

Positive variables
         vGen(egu,h)                     hourly electricity generation by existing plant [GWh]
         vRegup(egu,h)                   hourly reg up reserves provided by existing plant [GWh]
         vFlex(egu,h)
         vCont(egu,h)
         vCO2ems(egu,h)
         ;

Equations
*Op costs
         calcvarcosts(egu,h)
*Generation and reserve constraints
         limitallresup(egu,h)            limit total generation plus up reserves of existing plants to capacity
*Renewable generation
         eguwindgen(h)                   restrict electricity generation by existing wind generation to maximum aggregate output
         egusolargen(h)                  restrict electricity generation by existing solar generation to maximum aggregate output
*Carbon limits
         calcco2ems(egu,h)                    sum annual co2 emissions
         ;

******************VAR COSTS*****************
calcvarcosts(egu,h)..  vVarcost(egu,h) =e= vGen(egu,h)*pOpcost(egu) + vCO2ems(egu,h)*pCO2cost;
********************************************

******************GENERATION AND RESERVE CONSTRAINTS******************
*Limit spining and regulation reserves each to market participation
vFlex.fx(egu,h)$[pMaxflexoffer(egu)=0] = 0;
vCont.fx(egu,h)$[pMaxcontoffer(egu)=0] = 0;
vRegup.fx(egu,h)$[pMaxregupoffer(egu)=0] = 0;

*Limit spinning and regulation up reserves together to spare capacity
limitallresup(egu,h) .. vGen(egu,h) + vFlex(egu,h) + vCont(egu,h) + vRegup(egu,h) =l= pCapac(egu);
********************************************************************

******************RENEWABLE GENERATION*****************
eguwindgen(h)..  pMaxgenwind(h) =g= sum(windegu,vGen(windegu,h));
egusolargen(h).. pMaxgensolar(h) =g= sum(solaregu,vGen(solaregu,h));
*******************************************************

******************CO2 EMISSIONS CONSTRAINT******************
calcco2ems(egu,h)..   vCO2ems(egu,h) =e= vGen(egu,h)*pHr(egu)*pCO2emrate(egu);
************************************************************
