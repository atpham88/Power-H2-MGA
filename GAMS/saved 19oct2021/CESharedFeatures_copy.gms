*Michael Craig 16 Apr 2020

$include EDAndUCSharedFeatures.gms
$include StorageSetsParamsVariables.gms

Sets
*Existing generators
         nonrenewegu(egu)                existing nonrenewable generators
         ststorageegu(storageegu)
         ltstorageegu(storageegu)
*Candidate plants for construction
         tech                            candidate plant types for new construction
         dacstech(tech)
         notdacstech(tech)
         thermaltech(tech)               thermal plant types for new construction
         CCStech(tech)
         nucleartech(tech)
         CCtech(tech)
         renewtech(tech)                 renewable plant types for new construction
         windtech(renewtech)
         solartech(renewtech)
         storagetech(tech)               storage plant types for new construction
         batterytech(tech)
         hydrogentech(tech)
         ststoragetech(storagetech)
         ltstoragetech(storagetech)
         nonstoragetech(tech)            non storage techs
         gentechs(tech)                  generating techs specifically not DACS or storage
*Hours
         peakh(h)                        hour with peak net demand
         nonInitH(h)                     hours that are not initial horus of a block
*         dshifth(h)
         ;

Parameters
*MAX NEW UNITS TO BE BUILT
         pNMaxWind
         pNMaxSolar
         pNMaxThermal(thermaltech)
         pNMaxNuclear
         pNMaxCC
         pNMaxCCS(CCStech)
         pNMaxDACS(dacstech)
         pPMaxSto(storagetech)
         pEMaxSto(storagetech)
         pPERatio(ststoragetech)
         pPMaxH2Sto
         pEMaxH2Sto
         pPMaxBatSto
         pEMaxBatSto
         pPEBatRatio
*SIZE PARAMETERS [GW]
         pCapactech(tech)                nameplate capacity of new builds for cost calculations [GW]
*HEAT RATES [MMBtu/GWh]
         pHrtech(tech)                   heat rate of new builds [MMBtu per GWh]
*COST PARAMETERS
         pOpcosttech(tech)               total operational cost [thousandUSD per GWh] = VOM + FuelCost*HR + EmsCost*EmsRate*HR
         pFom(tech)                      fixed O&M cost [thousand$ per GW per yr]
         pOcc(tech)                      overnight capital cost [thousandUSD per GW]
         pPowOcc(storagetech)            occ for power capacity for lt storage
         pEneOcc(storagetech)            occ for energy capacity for lt storage
         pPowH2Occ(hydrogentech)           occ for power capacity for lt storage
         pEneH2Occ(hydrogentech)           occ for energy capacity for lt storage
         pCnse                           cost of nonserved energy [thousandUSD per GW]
*RAMP RATES [GW/hr]
         pRampratetech(tech)             up and down ramp rate of EGU assumed to be the same up & down [GW per hr]
*STORAGE PARAMETERS
         pEfficiencytech(storagetech)    round trip storage efficiency
*         pEfficiencyH2tech                round trip storage efficiency
*         pEfficiencyBattech               round trip storage efficiency
         pChargeDischargeCapRatio       "ratio of charging to discharging" /1/
*EMISSIONS RATES [short ton/MMBtu]
         pCO2emratetech(tech)            CO2 emissions rate of potential new generators [short ton per MMBtu]
*EMISSIONS CAP AND COST
         pCO2emcap                       CO2 annual emissions cap [short tons]
*RENEWABLE GENERATION CAPS
         pCf(renewtech,h)                hourly capacity factors for potential new renewables
*FINANCIAL PARAMETERS
         pR                              discount rate
         pLife(tech)                     lifetime of tech [years]
         pCrf(tech)                      capital recovery factor
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
$load ststorageegu, ltstorageegu, tech, dacstech, CCStech, thermaltech, nucleartech, CCtech, renewtech, solartech, windtech, storagetech, ststoragetech, ltstoragetech, peakh
$load pNMaxWind, pNMaxSolar, pNMaxThermal, pNMaxNuclear, pNMaxCC, pNMaxCCS, pNMaxDACS, pPMaxSto, pEMaxSto, pPMaxH2Sto, pEMaxH2Sto, pPMaxBatSto, pEMaxBatSto, pCapactech, pHrtech, pOpcosttech
$load pFom, pOcc, pPowOcc, pEneOcc, pRampratetech, pCO2emratetech
$load pEfficiencytech
*pEfficiencyH2tech, pEfficiencyBattech, pPowH2Occ, pEneH2Occ,
$load pCO2emcap, pCf, pR, pLife
$load pRegUpReqIncRE, pFlexReqIncRE
$load pFlexeligibletech, pConteligibletech, pRegeligibletech
$load pPlanningreserve
$gdxin

*DEFINE SET EXCLUSIONS
nonrenewegu(egu) = not windegu(egu) + solaregu(egu);
nonstoragetech(tech) = not storagetech(tech);
notdacstech(tech) = not dacstech(tech);
gentechs(tech) = not (dacstech(tech) + storagetech(tech));
*CALCULATE CAPITAL RECOVERY FACTOR
pCrf(tech) = pR / (1 - (1 / ( (1 + pR)**pLife(tech))));
*CALCULATE PE RATIO FOR SHORTTERM STORAGE
pPERatio(ststoragetech) = pEMaxSto(ststoragetech)/pPMaxSto(ststoragetech);
pPEBatRatio = pEMaxBatSto/pPMaxBatSto;
*CALCULATE MAX RESERVE OFFERS
pMaxflexoffertech(tech) = pFlexeligibletech(tech)*pRampratetech(tech)*pRampratetoflexreservescalar;
pMaxcontoffertech(tech) = pConteligibletech(tech)*pRampratetech(tech)*pRampratetocontreservescalar;
pMaxregupoffertech(tech) = pRegeligibletech(tech)*pRampratetech(tech)*pRampratetoregreservescalar;

Variable
         vVarcosttech(tech,h)
         vVarcostannual                  total variable costs for new and existing plants = variable O&M + fuel + emission costs [thousandUSD per yr]
         vFixedcostannual                total investment costs for new plants = fixed O&M + overnight capital costs [thousandUSD per yr]
         vGentech(tech,h)                hourly electricity generation by new plants [GWh]
*Emission variables
         vCO2emstech(tech,h)
         vCO2emsannual                   co2 emissions in entire year from new and existing plants [short ton]
         ;

Positive variables
*Reserve requirements
         vRegupreserve(h)                amount of reg up reserves [GW]
         vFlexreserve(h)
*Generation and reserve variables
         vReguptech(tech,h)              hourly reg up reserves provided by new plants [GWh]
         vFlextech(tech,h)
         vConttech(tech,h)
*Storage
*         vStateofchargetech(storagetech,h)             "energy stored in storage unit at end of hour h (GWh)"
*         vChargetech(storagetech,h)                    "charged energy by storage unit in hour h (GWh)"
         vStateofchargeh2tech(hydrogentech,h)           "energy stored in H2 storage unit at end of hour h (GWh)"
         vChargeH2tech(hydrogentech,h)                  "charged energy by H2 storage unit in hour h (GWh)"
         vStateofchargehBattech(batterytech,h)         "energy stored in battery storage unit at end of hour h (GWh)"
         vChargeBattech(batterytech,h)                 "charged energy by battery storage unit in hour h (GWh)"
*         vPowBuiltSto(storagetech)                     built power capacity for storage
*         vEneBuiltSto(storagetech)                     built energy capacity for storage
         vPowBuiltStoH2(hydrogentech)                   built power capacity for H2 storage
         vEneBuiltStoH2(hydrogentech)                   built energy capacity for H2 storage
         vPowBuiltStoBat(batterytech)                   built power capacity for battery storage
         vEneBuiltStoBat(batterytech)                   built energy capacity for battery storage
                   ;

$include CEBuildVariable.gms

Equations
*Costs
         calcvarcoststech(tech,h)
         investmentcost
*Meet demand and reserves
         meetdemand(h)                   meet supply with demand
         meetreservemargin               meet planning reserve requirement with installed capacity
         setflexreserve(h)               determine quantity of required spin reserves
         setregupreserve(h)              determine quantity of required reg up reserves
         meetflexreserve(h)              meet spin reserve requirement
         meetcontreserve(h)              meet contingency reserve requirement
         meetregupreserve(h)             meet reg up reserve requirement

*Maximum build constraints
         maxSolar(solartech)
         maxWind(windtech)
*        maxThermal(thermaltech)
         maxNuclear(nucleartech)
         maxCCS(CCStech)
         maxCC(CCtech)
         maxDAC(dacstech)
*         maxPSto(storagetech)
*         setVNSto(storagetech)
         maxPH2Sto(hydrogentech)
         setVNH2Sto(hydrogentech)
         maxPBatSto(batterytech)
         setVNBatSto(batterytech)
*         maxELTSto(ltstoragetech)
*         maxESTSto(ststoragetech)
         maxELTSto(hydrogentech)
         maxESTSto(batterytech)
*Carbon emissions
         calcco2emstech(tech,h)
         ;

*****************CALCULATE COSTS*******************
*Variable costs for new techs
calcvarcoststech(tech,h).. vVarcosttech(tech,h) =e= vGentech(tech,h)*pOpcosttech(tech);

*Fixed costs = annual fixed O&M + fixed annualized capital costs
*investmentcost..         vFixedcostannual =e= sum(nonstoragetech,vN(nonstoragetech)*pCapactech(nonstoragetech)*(pFom(nonstoragetech)+pOcc(nonstoragetech)*pCrf(nonstoragetech)))
*                                               + sum(hydrogentech,vPowBuiltStoH2(hydrogentech)*pPowOcc(hydrogentech)*pCrf(hydrogentech)+vEneBuiltStoH2(hydrogentech)*pEneOcc(hydrogentech)*pCrf(hydrogentech))
*                                              + sum(batterytech,vPowBuiltStoBat(batterytech)*pPowOcc(batterytech)*pCrf(batterytech)+vEneBuiltStoBat(batterytech)*pEneOcc(batterytech)*pCrf(batterytech));

investmentcost..         vFixedcostannual =e= sum(nonstoragetech,vN(nonstoragetech)*pCapactech(nonstoragetech)*(pFom(nonstoragetech)+pOcc(nonstoragetech)*pCrf(nonstoragetech)))
                                               + sum(storagetech,vPowBuiltSto(storagetech)*pPowOcc(storagetech)*pCrf(storagetech)+vEneBuiltSto(storagetech)*pEneOcc(storagetech)*pCrf(storagetech));
***************************************************

******************SYSTEM-WIDE GENERATION AND RESERVE CONSTRAINTS*******************
*Demand = generation by new and existing plants
*meetdemand(h)..          sum(tech,vGentech(tech,h))+sum(egu,vGen(egu,h)) =g= (pDemand(h)
*                                                        + sum(storageegu,vCharge(storageegu,h))
*                                                        + sum(hydrogentech,vChargetech(hydrogentech,h)));
*                                                        + sum(batterytech,vChargetech(batterytech,h)));

meetdemand(h)..          sum(tech,vGentech(tech,h))+sum(egu,vGen(egu,h)) =g= (pDemand(h)
                                                        + sum(storageegu,vCharge(storageegu,h)) + sum(storagetech,vChargetech(storagetech,h)));
*Meet planning reserve margin

*meetreservemargin..       sum(nucleartech,pCapactech(nucleartech)*vN(nucleartech))
*                          + sum(CCtech,pCapactech(CCtech)*vN(CCtech))
*                           + sum(CCStech,pCapactech(CCStech)*vN(CCStech))
*                           + sum(hydrogentech,vPowBuiltStoH2(hydrogentech))
*                           + sum(batterytech,vPowBuiltStoBat(batterytech))
*                           + sum((renewtech,peakh),pCapactech(renewtech)*vN(renewtech)*pCf(renewtech,peakh))
*                           + sum(nonrenewegu,pCapac(nonrenewegu))
*                                                  + sum(peakh,pMaxgenwind(peakh) + pMaxgensolar(peakh)) =g= pPlanningreserve;

meetreservemargin..      sum(thermaltech,pCapactech(thermaltech)*vN(thermaltech))
                                                   + sum(storagetech,vPowBuiltSto(storagetech))
                                                   + sum((renewtech,peakh),pCapactech(renewtech)*vN(renewtech)*pCf(renewtech,peakh))
                           + sum(nonrenewegu,pCapac(nonrenewegu))
                                                  + sum(peakh,pMaxgenwind(peakh) + pMaxgensolar(peakh)) =g= pPlanningreserve;

*Define spinning and reg reserve requirement based on new builds
setflexreserve(h)..      sum(renewtech,vN(renewtech)*pCapactech(renewtech)*pFlexReqIncRE(renewtech,h)) + pFlexreserves(h) =e= vFlexreserve(h);
setregupreserve(h)..     sum(renewtech,vN(renewtech)*pCapactech(renewtech)*pRegUpReqIncRE(renewtech,h)) + pRegupreserves(h) =e= vRegupreserve(h);

*Meet spinning and regulation reserve requirements
meetflexreserve(h)..     sum(tech,vFlextech(tech,h)) + sum(egu,vFlex(egu,h)) =g= vFlexreserve(h);
meetcontreserve(h)..     sum(tech,vConttech(tech,h)) + sum(egu,vCont(egu,h)) =g= pContreserves(h);
meetregupreserve(h)..    sum(tech,vReguptech(tech,h)) + sum(egu,vRegup(egu,h)) =g= vRegupreserve(h);
***********************************************************************************

******************BUILD DECISIONS******************
*Limit number builds to input value.
maxWind(windtech) .. vN(windtech) =l= pNMaxWind;
maxSolar(solartech) .. vN(solartech) =l= pNMaxSolar;
*maxThermal(thermaltech) .. vN(thermaltech) =l= pNMaxThermal(thermaltech);
maxNuclear(nucleartech) .. vN(nucleartech) =l= pNMaxNuclear;
maxCCS(CCStech) .. vN(CCStech) =l= pNMaxCCS(CCStech);
maxCC(CCtech) .. vN(CCtech) =l= pNMaxCC;
maxDAC(dacstech) .. vN(dacstech) =l= pNMaxDACS(dacstech);
maxPSto(storagetech) .. vPowBuiltSto(storagetech) =l= pPMaxSto(storagetech);
*maxPH2Sto(hydrogentech) .. vPowBuiltStoH2(hydrogentech) =l= pPMaxH2Sto;
*maxPBatSto(batterytech) .. vPowBuiltStoBat(batterytech) =l= pPMaxBatSto;
setVNSto(storagetech) .. vN(storagetech) =e= vPowBuiltSto(storagetech)/pCapactech(storagetech);
maxELTSto(ltstoragetech) .. vEneBuiltSto(ltstoragetech) =l= pEMaxSto(ltstoragetech);
maxESTSto(ststoragetech) .. vEneBuiltSto(ststoragetech) =e= pPERatio(ststoragetech)*vPowBuiltSto(ststoragetech);
*setVNH2Sto(hydrogentech) .. vN(hydrogentech) =e= vPowBuiltStoH2(hydrogentech)/pCapactech(hydrogentech);
*setVNBatSto(batterytech) .. vN(batterytech) =e= vPowBuiltStoBat(batterytech)/pCapactech(batterytech);
*maxELTSto(hydrogentech) .. vEneBuiltStoH2(hydrogentech) =l= pPMaxH2Sto;
*maxESTSto(batterytech) .. vEneBuiltStoBat(batterytech) =e= pPERatio*vPowBuiltStoBat(batterytech);
***************************************************

******************RESERVE CONSTRAINTS******************
vFlextech.fx(tech,h)$[pMaxflexoffertech(tech)=0] = 0;
vConttech.fx(tech,h)$[pMaxcontoffertech(tech)=0] = 0;
vReguptech.fx(tech,h)$[pMaxregupoffertech(tech)=0] = 0;
*******************************************************

********CALCULATE CO2 EMISSIONS*************
calcco2emstech(tech,h) .. vCO2emstech(tech,h) =e= vGentech(tech,h)*pHrtech(tech)*pCO2emratetech(tech);
********************************************

