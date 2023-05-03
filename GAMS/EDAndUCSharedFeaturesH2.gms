*Michael Craig 14 May 2020

$onEmpty

Sets
*Existing generators
         egu                             existing generators
         renewegu(egu)                   existing wind and solar generators
         windegu(renewegu)               existing wind generators
         solaregu(renewegu)              existing solar generators
         hydroegu(renewegu)
         genegu(egu)                     egus that are not dacs or storage
         dacsegu(egu)                    direct air capture units
         notdacsegu(egu)                 egus that are not dac units
         storageegu(egu)                 storage units
         h2storageegu(storageegu)        storage units that are hydrogen
         nonh2storageegu(storageegu)     non h2 storage units
         h2egu(egu)                      egus that produce h2 (not electricity producing egus) (ton)
         egenegu(egu)                    egus that produce electricity
         electrolyzeregu(egu)            existing electrolyzer (ton)
         h2eegu(egu)                     egus that produce electricty from h2 (GWh)
         fuelcellegu(h2eegu)
         h2turbineegu(h2eegu)
         h                               hours
                 z                       zones
                 l                       lines
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
*Conversion[MWh/kg or GWh/ton]         
         pElectrolyzerCon
         pFuelCellCon
         pH2TurbineCon
*RENEWABLE GENERATION CAPS
         pMaxgenwind(z,h)                  max hourly generation for existing wind [GWh]
         pMaxgensolar(z,h)                 max hourly generation for existing solar [GWh]
*STORAGE PARAMETERS
         pStoinenergymarket              whether storage can provide energy (1) or not (0)
         pEfficiency(storageegu)         round trip storage efficiency
         pCapaccharge(storageegu)        max charging capacity (GW)
         pMaxsoc(storageegu)             max stored energy (GWh)
         pMinsoc(storageegu)             min stored energy (GWh)
*ZONAL PROPERTIES
                pGenzone(egu)                                   zone in which egu is located
                pDemand(z,h)                      hourly electricity demand [GWh]
                pH2Demand(z,h)
                pLinesource(l)                                  zone that is the source of line l
                pLinesink(l)                                    zone that is the sink of line l
                pLinecapac(l)                                   MW capacity of line l
                pH2LineCapac(l)
                pTransEff
*HOURLY ELECTRICITY DEMAND [GWh]
         pDemandShifter                  demand shifter (percentage)
         pDemandShiftingBlock
*COST OF NONSERVED ENERGY [THOUSAND$/GWH]
         pCnse                                   cost of non-served energy [thousandUSD per GWh]
*HOURLY RESERVE REQUIREMENTS [GW]
         pRegupreserves(z,h)         regulation up reserve [GW]
         pFlexreserves(z,h)
         pContreserves(z,h)
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
$load egu, renewegu, windegu, solaregu, hydroegu, h, z, l, dacsegu, storageegu, h2storageegu, h2egu, h2eegu, fuelcellegu, h2turbineegu, electrolyzeregu
$load pCapac, pHr, pOpcost, pRamprate, pCO2emrate, pCO2cost, pElectrolyzerCon, pFuelCellCon, pH2TurbineCon
$load pMaxgensolar, pMaxgenwind
$load pH2Demand, pH2LineCapac
$load pStoinenergymarket, pEfficiency, pMaxsoc, pMinsoc, pCapaccharge
$load pGenzone, pDemand, pLinesource, pLinesink, pLinecapac, pTransEff
$load pDemandShifter, pDemandShiftingBlock, pCnse, pRegupreserves, pFlexreserves, pContreserves
$load pRampratetoregreservescalar, pRampratetoflexreservescalar, pRampratetocontreservescalar
$load pFlexeligible, pConteligible, pRegeligible
$gdxin

*DEFINE EGU SUBSETS
notdacsegu(egu) = not dacsegu(egu);
egenegu(egu) = not h2egu(egu);
genegu(egu) = not (dacsegu(egu) + storageegu(egu));
nonh2storageegu(storageegu) = not h2storageegu(storageegu);

*CALCULATE MAX RESERVE OFFERS
pMaxflexoffer(egu) = pFlexeligible(egu)*pRamprate(egu)*pRampratetoflexreservescalar;
pMaxcontoffer(egu) = pConteligible(egu)*pRamprate(egu)*pRampratetocontreservescalar;
pMaxregupoffer(egu) = pRegeligible(egu)*pRamprate(egu)*pRampratetoregreservescalar;

Variables
*COSTS
                 vVarcost(egu,h)
*DEMAND RESPONSE
                 vShiftedDemand(z,h)
                 ;

Positive variables
*GENERATION AND RESERVES
         vGen(egu,h)                     hourly electricity generation by existing plant [GWh or ton]
         vRegup(egu,h)                   hourly reg up reserves provided by existing plant [GWh]
         vFlex(egu,h)
         vCont(egu,h)
*STORAGE VARIABLES
         vStateofcharge(storageegu,h)            "energy stored in storage unit at end of hour h (GWh or ton)"
         vCharge(storageegu,h)                   "charged energy by storage unit in hour h (GWh or ton)"
*Inputs for existing electrolyzers, fuel cells and H2 turbines:
         vELCharge(electrolyzeregu,h)                electricity input to power electrolyzer
         vH2TCharge(h2eegu,h)                     hydrogen input to power H2T tech (hydrogen turbines + fuel cells)         
*EMISSIONS
         vCO2ems(egu,h)
*TRANSMISSION LINE FLOWS
                vLineflow(l,h)
                vH2Lineflow(l,h)
         ;

Equations
*Op costs
         calcvarcosts(egu,h)
*Generation and reserve constraints
         limitallresup(egu,h)                           limit total generation plus up reserves of existing plants to capacity
*Renewable generation
         limitWindGen(z,h)
                 limitSolarGen(z,h)
*Line flows
*               limitLineFlow(l,h)
*Carbon limits
         calcco2ems(egu,h)                              sum annual co2 emissions
*Limit of h2 output from electrolyzers         
         electrolyzerconversion(electrolyzeregu,h)
*Limit of electricity output from fuel cells          
         fuelcellconversion(fuelcellegu,h)
*Limit of electricity output from H2 turbines          
         h2turbineconversion(h2turbineegu,h)
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
limitallresup(genegu,h) .. vGen(genegu,h) + vFlex(genegu,h) + vCont(genegu,h) + vRegup(genegu,h) =l= pCapac(genegu);

*Set lower bound to zero for generation by storage and generating techs.
vGen.lo(notdacsegu,h) = 0;
*Set upper bound to zero for DACS. DACS max capacity is negative and has negative vGen values.
vGen.up(dacsegu,h) = 0;
********************************************************************

******************STORAGE PARAMETERS*******************
*LIMIT GENERATION AND RESERVES
*Bound generation to capacity and ability to participate in energy market
vGen.up(storageegu,h) = pStoinenergymarket * pCapac(storageegu);

*CHARGE CONSTRAINTS
*Place upper bound on charging
vCharge.up(storageegu,h) = pCapaccharge(storageegu);

*STATE OF CHARGE BOUNDS
vStateofcharge.lo(storageegu,h) = pMinsoc(storageegu);
vStateofcharge.up(storageegu,h) = pMaxsoc(storageegu);
*******************************************************

******************RENEWABLE GENERATION*****************
limitWindGen(z,h)..  pMaxgenwind(z,h) =g= sum(windegu$[pGenzone(windegu)=ORD(z)],vGen(windegu,h));
limitSolarGen(z,h).. pMaxgensolar(z,h) =g= sum(solaregu$[pGenzone(solaregu)=ORD(z)],vGen(solaregu,h));
*******************************************************

******************TRANSMISSION LINE FLOWS*****************
*limitLineFlow(l,h).. pLinecapac(l) =g= vLineflow(l,h);
**********************************************************

******************CO2 EMISSIONS CONSTRAINT******************
calcco2ems(egu,h)..   vCO2ems(egu,h) =e= vGen(egu,h)*pHr(egu)*pCO2emrate(egu);
************************************************************

******************ELECTROLYZER CONSTRAINT******************
electrolyzerconversion(electrolyzeregu,h)..   vELCharge(electrolyzeregu,h) =e= vGen(electrolyzeregu,h)*pElectrolyzerCon/1000;
************************************************************

******************FUEL CELL CONSTRAINT******************
fuelcellconversion(fuelcellegu,h)..   vH2TCharge(fuelcellegu,h) =e= vGen(fuelcellegu,h)/(pFuelCellCon*1000);
************************************************************

******************H2 TURBINE CONSTRAINT******************
h2turbineconversion(h2turbineegu,h)..   vH2TCharge(h2turbineegu,h) =e= vGen(h2turbineegu,h)/(pH2TurbineCon*1000);
************************************************************
