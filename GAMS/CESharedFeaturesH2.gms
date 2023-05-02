*Michael Craig 16 Apr 2020

$include EDAndUCSharedFeaturesH2.gms

Sets
*EXISTING GENERATORS
         nonrenewegu(egu)                   existing nonrenewable generators
                ststorageegu(storageegu)    existing battery storage
                ltstorageegu(storageegu)    existing h2 storage
*CANDIDATE TECHNOLOGIES FOR CONSTRUCTION
         tech                               candidate technologies for new construction
*Generators
         gentechs(tech)                     generating techs specifically not DACS or storage or h2 production
         thermaltech(tech)                  thermal plant types for new construction
            CCStech(thermaltech)
            nucleartech(thermaltech)
            srtech(thermaltech)             small modular reactors
            CCtech(thermaltech)
         renewtech(tech)                    renewable plant types for new construction
            windtech(renewtech)             transInvestments
            solartech(renewtech)
*H2 generators and H2 input electricity generators:
         h2tech(tech)                       technologies that produce h2
            SMRtech(h2tech)                 SMR that produce h2
            electrolyzertech(h2tech)        Electrolyzers that produce h2
         h2etech(tech)                      H2 turbines and fuel cell
            fuelcelltech(h2etech)           Fuel cells  
            h2turbinetech(h2etech)          H2 turbines
*Storage
         storagetech(tech)                  storage plant types for new construction
            ststoragetech(storagetech)      new battery storage [GWh]
            ltstoragetech(storagetech)      new h2 storage [ton]
         nonstoragetech(tech)               non storage techs
                
*CO2 removal
         dacstech(tech)
         notdacstech(tech)
*CANDIDATE TRANSMISSION LINES FOR CONSTRUCTION
*               ltech
*HOURS
         peakH(h)                           hour with peak net demand
         nonInitH(h)                        hours that are not initial horus of a block
         ;

Alias (h,hh);
Alias (l,ll);

Parameters
*MAX NEW UNITS TO BE BUILT
                 pNMaxWind
                 pNMaxSolar
                 pNMaxNuclear
                 pNMaxSR
                 pNMaxCC
                 pNMaxCCS(CCStech)
                 pNMaxDACS(dacstech)
                 pPMaxSto(storagetech)        Max battery power capacity
                 pEMaxSto(storagetech)        Max battery energy capacity
                 pPERatio(ststoragetech)
                 pNMaxSMR
                 pNMaxSMRCCS
                 pNMaxElectrolyzer
                 pNMaxFuelcell
                 PNMaxH2Turbine
*SIZE PARAMETERS [GW]
         pCapactech(tech)                       nameplate capacity of new builds for cost calculations [GW] or [ton]
         pMaxZCaptech(tech)                     max capacity allowed to be built by zone [GW]
         pWeighttech(tech)                      Coefficients of capacity investment variables for MGA (initial = 1)
*HEAT RATES [MMBtu/GWh]
         pHrtech(tech)                          heat rate of new builds [MMBtu per GWh]
*COST PARAMETERS
         pOpcosttech(tech)                      total operational cost [thousandUSD per GWh] = VOM + FuelCost*HR + EmsCost*EmsRate*HR
         pFom(tech)                             fixed O&M cost [thousand$ per GW per yr]
         pOcc(tech)                             overnight capital cost [thousandUSD per GW] or [thousandUSD per ton]
                 pPowOcc(storagetech)           occ for power capcity for lt storage
                 pEneOcc(storagetech)           occ for energy capacity for lt storage
*                pCnse                          cost of nonserved energy [thousandUSD per GW]
*RAMP RATES [GW/hr]
         pRampratetech(tech)                    up and down ramp rate of EGU assumed to be the same up & down [GW per hr]
*STORAGE PARAMETERS
         pEfficiencytech(storagetech)           round trip battery storage efficiency
         pChargeDischargeCapRatio               "ratio of charging to discharging" /1/
*EMISSIONS RATES [short ton/MMBtu]
         pCO2emratetech(tech)                   CO2 emissions rate of potential new generators [short ton per MMBtu]
*EMISSIONS CAP AND COST
         pCO2emcap                              CO2 annual emissions cap [short tons]
*RENEWABLE GENERATION CAPS
         pCf(renewtech,h)                       hourly capacity factors for potential new renewables
*FINANCIAL PARAMETERS
         pR                                     discount rate
         pLife(tech)                            lifetime of tech [years]
         pLifeline
         pH2Lifeline
         pCrf(tech)                             capital recovery factor
                 pCrfline
*ZONAL PARAMETERS
                pGenzonetech(tech)
*               pLinesourcetech(ltech)
*               pLinesinktech(ltech)
*               pLinecapactech(ltech)
                pLinecost(l)
                pH2Linecost(l)
                pNMaxLine(l)
                pNMaxH2Line(l)
*               pPeakhtozone(peakH)
*HOURLY RESERVE REQUIREMENTS [GW]
         pRegUpReqIncRE(renewtech,h)
         pFlexReqIncRE(renewtech,h)
*RESERVE PROVISION PARAMETERS
         pRegeligibletech(tech)          candidate plant types eligible to provide reg reserves [0] or not [1]
         pFlexeligibletech(tech)
         pConteligibletech(tech)
         pMaxflexoffertech(tech)
         pMaxcontoffertech(tech)
         pMaxregupoffertech(tech)
*PLANNING RESERVE
         pPlanningreserve                planning margin reserve capacity [GW]
         ;

$if not set gdxincname $abort 'no include file name for data file provided'
$gdxin %gdxincname%
$load ststorageegu, ltstorageegu, tech, dacstech, thermaltech, CCStech, nucleartech, srtech, CCtech, renewtech, solartech, windtech, storagetech, ststoragetech, ltstoragetech, peakH
$load h2tech, electrolyzertech, SMRtech, h2etech, fuelcelltech, h2turbinetech
$load pNMaxWind, pNMaxSolar, pNMaxNuclear, pNMaxSR, pNMaxCC, pNMaxCCS, pNMaxDACS, pPMaxSto, pEMaxSto, pCapactech, pHrtech, pOpcosttech, pMaxZCaptech, pWeighttech
$load pNMaxSMR, pNMaxElectrolyzer, pNMaxFuelcell, PNMaxH2Turbine
$load pNMaxH2Line, pH2Lifeline, pH2Linecost
$load pFom, pOcc, pPowOcc, pEneOcc, pRampratetech, pCO2emratetech
$load pEfficiencytech
$load pCO2emcap, pCf, pR, pLife, pLifeline
$load pGenzonetech, pLinecost, pNMaxLine
$load pRegUpReqIncRE, pFlexReqIncRE
$load pFlexeligibletech, pConteligibletech, pRegeligibletech
$load pPlanningreserve
$gdxin

*DEFINE SET EXCLUSIONS
nonrenewegu(egu) = not renewegu(egu);
nonstoragetech(tech) = not storagetech(tech);
notdacstech(tech) = not dacstech(tech);
gentechs(tech) = not (dacstech(tech) + storagetech(tech));
*CALCULATE CAPITAL RECOVERY FACTOR
pCrf(tech) = pR / (1 - (1 / ( (1 + pR)**pLife(tech))));
pCrfline = pR / (1 - (1 / ( (1 + pR)**pLifeline)));
*CALCULATE PE RATIO FOR SHORTTERM STORAGE
pPERatio(ststoragetech) = pEMaxSto(ststoragetech)/pPMaxSto(ststoragetech);
*CALCULATE MAX RESERVE OFFERS
pMaxflexoffertech(tech) = pFlexeligibletech(tech)*pRampratetech(tech)*pRampratetoflexreservescalar;
pMaxcontoffertech(tech) = pConteligibletech(tech)*pRampratetech(tech)*pRampratetocontreservescalar;
pMaxregupoffertech(tech) = pRegeligibletech(tech)*pRampratetech(tech)*pRampratetoregreservescalar;

Variable
         vVarcosttech(tech,h)
         vVarcostannual                  total variable costs for new and existing plants = variable O&M + fuel + emission costs [thousandUSD per yr]
         vFixedcostannual                total investment costs for new plants = fixed O&M + overnight capital costs [thousandUSD per yr]
         vGentech(tech,h)                hourly electricity generation by new plants [GWh] or [ton]
*Emission variables
         vCO2emstech(tech,h)
         vCO2emsannual                   co2 emissions in entire year from new and existing plants [short ton]
         ;

Positive variables
*Reserve requirements
         vRegupreserve(z,h)              amount of reg up reserves [GW]
         vFlexreserve(z,h)
*Generation and reserve variables
         vReguptech(tech,h)              hourly reg up reserves provided by new plants [GWh]
         vFlextech(tech,h)
         vConttech(tech,h)
*Storage
         vStateofchargetech(storagetech,h)              "energy stored in storage unit at end of hour h (GWh)"
         vChargetech(storagetech,h)                     "charged energy by storage unit in hour h (GWh)"
         vPowBuiltSto(storagetech)                      built power capacity for storage
         vEneBuiltSto(storagetech)                      built energy capacity for storage
*Inputs for electrolyzers, fuel cells and H2 turbines:
         vELChargetech(electrolyzertech,h)              electricity input to power electrolyzer
         vH2TChargetech(h2etech,h)                      hydrogen input to power H2T tech (hydrogen turbines + fuel cells)
*Line builds and flows
         vNl(l)
         vLinecapacnew(l)
         vNH2l(l)
         vH2Linecapacnew(l)
*        vLinenewflow(ltech,h)
                   ;

$include CEBuildVariable.gms

Equations
*Costs
                calcvarcoststech(tech,h)
                investmentcost
*Meet demand and reserves
         meetdemand(z,h)                   meet electricity supply with electrcity demand
         meeth2demand(z,h)                 meet h2 demand
         meetreservemargin                 meet planning reserve requirement with installed capacity
         setflexreserve(z,h)               determine quantity of required spin reserves
         setregupreserve(z,h)              determine quantity of required reg up reserves
         meetflexreserve(z,h)              meet spin reserve requirement
         meetcontreserve(z,h)              meet contingency reserve requirement
         meetregupreserve(z,h)             meet reg up reserve requirement
         limitshiftingdemandupper(z,h)     limit the amount of demand that can be shifted
         limitshiftingdemandlower(z,h)     limit the amount of demand that can be shifted
         meetshiftingdemand(z,h)
         limitLineFlows(l,h)
         limitH2LineFlows(l,h)
         linecapacnew(l,ll)
         h2linecapacnew(l,ll)

*Maximum build constraints
                 maxSolar(solartech)
                 maxWind(windtech)
                 maxNuclear(nucleartech)
                 maxCCS(CCStech)
                 maxCC(CCtech)
                 maxDAC(dacstech)
                 maxPSto(storagetech)
                 setVNSto(storagetech)
                 maxELTSto(ltstoragetech)
                 maxESTSto(ststoragetech)
                                 maxL(l)
                                 maxH2l(l)
                 maxSR(srtech)
                 maxSMR(SMRtech)
                 maxElectrolyzer(electrolyzertech)
                 maxFuelcell(fuelcelltech)
                 maxH2Turbine(h2turbinetech)
*                 biLineLimit(l)
*Carbon emissions
                calcco2emstech(tech,h)
*Limit of h2 output from electrolyzers         
         electrolyzerconversiontech(electrolyzertech,h)
*Limit of electricity output from fuel cells          
         fuelcellconversiontech(fuelcelltech,h)
*Limit of electricity output from h2 turbines          
         h2turbineconversiontech(h2turbinetech,h)
         ;

*****************CALCULATE COSTS*******************
*Variable costs for new techs
calcvarcoststech(tech,h).. vVarcosttech(tech,h) =e= vGentech(tech,h)*pOpcosttech(tech);

*Fixed costs = annual fixed O&M + fixed annualized capital costs
investmentcost..         vFixedcostannual =e= sum(nonstoragetech,vN(nonstoragetech)*pCapactech(nonstoragetech)*(pFom(nonstoragetech)+pOcc(nonstoragetech)*pCrf(nonstoragetech)))
                                                 + sum(storagetech,vPowBuiltSto(storagetech)*pPowOcc(storagetech)*pCrf(storagetech)+vEneBuiltSto(storagetech)*pEneOcc(storagetech)*pCrf(storagetech))
                                                 + sum(l,vNl(l)*pLinecost(l)*pCrfline) + sum(l,vNH2l(l)*pH2Linecost(l)*pCrfline);
                                                 
***************************************************

******************SYSTEM-WIDE GENERATION AND RESERVE CONSTRAINTS******************* vH2TChargetech
*Demand = generation by new and existing plants
meetdemand(z,h)..          sum(thermaltech$[pGenzonetech(thermaltech)=ORD(z)],vGentech(thermaltech,h)) + sum(renewtech$[pGenzonetech(renewtech)=ORD(z)],vGentech(renewtech,h))
                                                        + sum(h2etech$[pGenzonetech(h2etech)=ORD(z)],vGentech(h2etech,h)) + sum(egenegu$[pGenzone(egenegu)=ORD(z)],vGen(egenegu,h))
                                                        + sum(l$[pLinesink(l)=ORD(z)],vLineflow(l,h))*pTransEff =g= (pDemand(z,h) + vShiftedDemand(z,h)
                                                        + sum(electrolyzertech$[pGenzonetech(electrolyzertech)=ORD(z)],vELChargetech(electrolyzertech,h))
                                                        + sum(electrolyzeregu$[pGenzone(electrolyzeregu)=ORD(z)],vELCharge(electrolyzeregu,h))
                                                        + sum(nonh2storageegu$[pGenzone(nonh2storageegu)=ORD(z)],vCharge(nonh2storageegu,h)) + sum(ststoragetech$[pGenzonetech(ststoragetech)=ORD(z)],vChargetech(ststoragetech,h))
                                                        + sum(l$[pLinesource(l)=ORD(z)],vLineflow(l,h)));
                                                                                                                
meeth2demand(z,h)..          sum(h2tech$[pGenzonetech(h2tech)=ORD(z)],vGentech(h2tech,h)) + sum(h2egu$[pGenzone(h2egu)=ORD(z)],vGen(h2egu,h))
                                                        + sum(l$[pLinesink(l)=ORD(z)],vH2Lineflow(l,h)) =g= (pH2Demand(z,h)
                                                        + sum(h2etech$[pGenzonetech(h2etech)=ORD(z)],vH2TChargetech(h2etech,h)) + sum(h2eegu$[pGenzone(h2eegu)=ORD(z)],vH2TCharge(h2eegu,h))
                                                        + sum(h2storageegu$[pGenzone(h2storageegu)=ORD(z)],vCharge(h2storageegu,h)) + sum(ltstoragetech$[pGenzonetech(ltstoragetech)=ORD(z)],vChargetech(ltstoragetech,h))
                                                        + sum(l$[pLinesource(l)=ORD(z)],vH2Lineflow(l,h)));

*meetdemand(z,h)..          sum(tech$[pGenzonetech(tech)=ORD(z)],vGentech(tech,h)) + sum(egu$[pGenzone(egu)=ORD(z)],vGen(egu,h)) =g= pDemand(z,h);

*Demand response
limitshiftingdemandupper(z,h)..       vShiftedDemand(z,h) =l= pDemand(z,h)*pDemandShifter;
limitshiftingdemandlower(z,h)..       vShiftedDemand(z,h) =g= -1*pDemand(z,h)*pDemandShifter;
meetshiftingdemand(z,h)$(mod(ord(h),pDemandShiftingBlock)=1).. sum(hh$((ord(hh)>=ord(h) and (ord(hh)<=ord(h)+pDemandShiftingBlock-1))), vShiftedDemand(z,h))=e= 0;

*Meet planning reserve margin
meetreservemargin..        sum(thermaltech,pCapactech(thermaltech)*vN(thermaltech))
                           + sum(storagetech,vPowBuiltSto(storagetech))
                           + sum((renewtech,peakH),pCapactech(renewtech)*vN(renewtech)*pCf(renewtech,peakH))
                           + sum(nonrenewegu,pCapac(nonrenewegu))
                           + sum((z,peakH),pMaxgenwind(z,peakH) + pMaxgensolar(z,peakH)) =g= pPlanningreserve;

*Define spinning and reg reserve requirement based on new builds
setflexreserve(z,h)..      sum(renewtech$[pGenzonetech(renewtech)=ORD(z)],vN(renewtech)*pCapactech(renewtech)*pFlexReqIncRE(renewtech,h)) + pFlexreserves(z,h) =e= vFlexreserve(z,h);
setregupreserve(z,h)..     sum(renewtech$[pGenzonetech(renewtech)=ORD(z)],vN(renewtech)*pCapactech(renewtech)*pRegUpReqIncRE(renewtech,h)) + pRegupreserves(z,h) =e= vRegupreserve(z,h);

*Meet spinning and regulation reserve requirements
meetflexreserve(z,h)..     sum(tech$[pGenzonetech(tech)=ORD(z)],vFlextech(tech,h)) + sum(egu$[pGenzone(egu)=ORD(z)],vFlex(egu,h)) =g= vFlexreserve(z,h);
meetcontreserve(z,h)..     sum(tech$[pGenzonetech(tech)=ORD(z)],vConttech(tech,h)) + sum(egu$[pGenzone(egu)=ORD(z)],vCont(egu,h)) =g= pContreserves(z,h);
meetregupreserve(z,h)..    sum(tech$[pGenzonetech(tech)=ORD(z)],vReguptech(tech,h)) + sum(egu$[pGenzone(egu)=ORD(z)],vRegup(egu,h)) =g= vRegupreserve(z,h);

*Limit line flows on new lines
linecapacnew(l,ll)$(pLinesource(l)=pLinesink(ll) and pLinesource(ll)=pLinesink(l)).. vLinecapacnew(l) =e= vNl(l) + vNl(ll);
limitLineFlows(l,h).. pLinecapac(l)+vLinecapacnew(l) =g= vLineflow(l,h);
h2linecapacnew(l,ll)$(pLinesource(l)=pLinesink(ll) and pLinesource(ll)=pLinesink(l)).. vH2Linecapacnew(l) =e= vNH2l(l) + vNH2l(ll);
limitH2LineFlows(l,h).. pH2Linecapac(l)+vH2Linecapacnew(l) =g= vH2Lineflow(l,h);
*new lines with same sources and sinks have the same capacity:
*biLineLimit(l,ll)$(pLinesource(l)=pLinesink(ll) and pLinesource(ll)=pLinesink(l)).. vNl(l) =e= vNl(ll);
***********************************************************************************

*************UPPER AND LOWER GENERATION BOUNDS*****
*Set lower bound to zero for generation by storage and generating techs.
vGentech.lo(notdacstech,h) = 0;
*Set upper bound to zero for DACS techs. DACS max capacity is negative and has negative vGen values.
vGentech.up(dacstech,h) = 0;
***************************************************


******************ELECTROLYZER CONSTRAINT******************
electrolyzerconversiontech(electrolyzertech,h)..   vELChargetech(electrolyzertech,h) =e= vGentech(electrolyzertech,h)*(pElectrolyzerCon/1000);
************************************************************

******************FUEL CELL CONSTRAINT******************
fuelcellconversiontech(fuelcelltech,h)..   vH2TChargetech(fuelcelltech,h) =e= vGentech(fuelcelltech,h)/(pFuelCellCon*1000);
************************************************************

******************H2 TURBINE CONSTRAINT******************
h2turbineconversiontech(h2turbinetech,h)..   vH2TChargetech(h2turbinetech,h) =e= vGentech(h2turbinetech,h)/(pH2TurbineCon*1000);
************************************************************

******************BUILD DECISIONS******************
*Limit number builds to input value.
maxWind(windtech) .. vN(windtech) =l= pNMaxWind;
maxSolar(solartech) .. vN(solartech) =l= pNMaxSolar;
maxNuclear(nucleartech) .. vN(nucleartech) =l= pNMaxNuclear;
maxCCS(CCStech) .. vN(CCStech) =l= pNMaxCCS(CCStech);
maxCC(CCtech) .. vN(CCtech) =l= pNMaxCC;
maxDAC(dacstech) .. vN(dacstech) =l= pNMaxDACS(dacstech);
maxPSto(storagetech) .. vPowBuiltSto(storagetech) =l= pPMaxSto(storagetech);
setVNSto(storagetech) .. vN(storagetech) =e= vPowBuiltSto(storagetech)/pCapactech(storagetech);
maxELTSto(ltstoragetech) .. vEneBuiltSto(ltstoragetech) =l= pEMaxSto(ltstoragetech);
maxESTSto(ststoragetech) .. vEneBuiltSto(ststoragetech) =e= pPERatio(ststoragetech)*vPowBuiltSto(ststoragetech);
maxL(l) .. vNl(l) =l= pNMaxLine(l);
maxH2L(l) .. vNH2l(l) =l= pNMaxH2Line(l);
maxSR(srtech) .. vN(srtech) =l= pNMaxSR;
maxSMR(smrtech) .. vN(SMRtech) =l= pNMaxSMR(smrtech);
maxElectrolyzer(electrolyzertech) .. vN(electrolyzertech) =l= pNMaxElectrolyzer(electrolyzertech);
maxFuelcell(fuelcelltech) .. vN(fuelcelltech) =l= pNMaxFuelcell;
maxH2Turbine(h2turbinetech) .. vN(h2turbinetech) =l= pNMaxH2Turbine;

***************************************************

******************RESERVE CONSTRAINTS******************
vFlextech.fx(tech,h)$[pMaxflexoffertech(tech)=0] = 0;
vConttech.fx(tech,h)$[pMaxcontoffertech(tech)=0] = 0;
vReguptech.fx(tech,h)$[pMaxregupoffertech(tech)=0] = 0;
*******************************************************

********CALCULATE CO2 EMISSIONS*************
calcco2emstech(tech,h).. vCO2emstech(tech,h) =e= vGentech(tech,h)*pHrtech(tech)*pCO2emratetech(tech);
********************************************


