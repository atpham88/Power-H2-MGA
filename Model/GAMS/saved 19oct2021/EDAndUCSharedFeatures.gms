*Michael Craig 14 May 2020

$onEmpty

Sets
*Existing generators
         egu                             existing generators
		 renewegu(egu)					existing wind and solar generators
		 windegu(renewegu)				existing wind generators
		 solaregu(renewegu)				existing solar generators
		 genegu(egu)                  egus that are not dacs or storage
		 dacsegu(egu)                 direct air capture units
		 notdacsegu(egu)              egus that are not dac units
         h                               hours
		 z 								zones
		 l 								lines
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
         pMaxgenwind(z,h)                  max hourly generation for existing wind [GWh]
         pMaxgensolar(z,h)                 max hourly generation for existing solar [GWh]
*ZONAL PROPERTIES
		pGenzone(egu)					zone in which egu is located
		pDemand(z,h)                      hourly electricity demand [GWh]
        pLinesource(l)					zone that is the source of line l
		pLinesink(l)					zone that is the sink of line l
		pLinecapac(l)					MW capacity of line l
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
$load egu, renewegu, windegu, solaregu, h, z, l, dacsegu
$load pCapac, pHr, pOpcost, pRamprate, pCO2emrate, pCO2cost
$load pMaxgensolar, pMaxgenwind
$load pGenzone, pDemand, pLinesource, pLinesink, pLinecapac
$load pDemandShifter, pDemandShiftingBlock, pCnse, pRegupreserves, pFlexreserves, pContreserves
$load pRampratetoregreservescalar, pRampratetoflexreservescalar, pRampratetocontreservescalar
$load pFlexeligible, pConteligible, pRegeligible
$gdxin

*DEFINE EGUS THAT ARE NOT DACS
notdacsegu(egu) = not dacsegu(egu);

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
		 vGen(egu,h)                     hourly electricity generation by existing plant [GWh]
         vRegup(egu,h)                   hourly reg up reserves provided by existing plant [GWh]
         vFlex(egu,h)
         vCont(egu,h)
*EMISSIONS
         vCO2ems(egu,h)
*TRANSMISSION LINE FLOWS
		vLineflow(l,h)
         ;

Equations
*Op costs
         calcvarcosts(egu,h)
*Generation and reserve constraints
         limitallresup(egu,h)            limit total generation plus up reserves of existing plants to capacity
*Renewable generation
         limitWindGen(z,h)
		 limitSolarGen(z,h)
*Line flows
*		limitLineFlow(l,h)
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
limitWindGen(z,h)..  pMaxgenwind(z,h) =g= sum(windegu$[pGenzone(windegu)=ORD(z)],vGen(windegu,h));
limitSolarGen(z,h).. pMaxgensolar(z,h) =g= sum(solaregu$[pGenzone(solaregu)=ORD(z)],vGen(solaregu,h));
*******************************************************

******************TRANSMISSION LINE FLOWS*****************
*limitLineFlow(l,h).. pLinecapac(l) =g= vLineflow(l,h);
**********************************************************

******************CO2 EMISSIONS CONSTRAINT******************
calcco2ems(egu,h)..   vCO2ems(egu,h) =e= vGen(egu,h)*pHr(egu)*pCO2emrate(egu);
************************************************************
