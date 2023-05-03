#Michael Craig
#October 4, 2016
#Functions for adding parameters to GAMS database. Used for CE & UC models.

import copy, math, pandas as pd, numpy as np
from GAMSAuxFuncs import *
from GAMSAddSetToDatabaseFuncs import createHourSubsetName
from WriteTimeDependentConstraints import createInitSOCName

################################################################################
##################### CE & UC PARAMETERS #######################################
################################################################################
##### ADD HOURLY DEMAND PARAMETERS (GWh)
def addDemandParam(db, demand, h2Demand, hourSet, zoneSet, demandShifter, demandShiftingBlock, mwToGW):
    add2dParam(db, convert2DTimeseriesDfToDict(demand, 1/mwToGW), zoneSet, hourSet, 'pDemand')
    add2dParam(db, convert2DTimeseriesDfToDict(h2Demand, 1), zoneSet, hourSet, 'pH2Demand')
    add0dParam(db,'pDemandShifter', demandShifter)
    add0dParam(db,'pDemandShiftingBlock', demandShiftingBlock)


##### ADD EXISTING OR NEW GENERATOR PARAMETERS (scalars account for unit conversions)
def addGenParams(db,df,genSet,mwToGW,lbToShortTon,zoneOrder,newTechs=False):
    techLbl = 'tech' if newTechs else ''
    # Heat rate (MMBtu/GWh)
    add1dParam(db,getGenParamDict(df,'Heat Rate (Btu/kWh)'), genSet, df['GAMS Symbol'],'pHr' + techLbl)
    # Emissions rate (short ton/MMBtu)
    add1dParam(db,getGenParamDict(df,'CO2EmRate(lb/MMBtu)', 1/lbToShortTon), genSet, df['GAMS Symbol'],'pCO2emrate' + techLbl)
    # Ramp rate (GW/hr)
    add1dParam(db,getGenParamDict(df,'RampRate(MW/hr)', 1/mwToGW), genSet, df['GAMS Symbol'],'pRamprate' + techLbl)
    # Op cost (thousand$/GWh)
    add1dParam(db,getGenParamDict(df,'OpCost($/MWh)'), genSet,df['GAMS Symbol'],'pOpcost' + techLbl)
    # Capacity (GW) or 1000 ton
    add1dParam(db,getGenParamDict(df,'Capacity (MW)', 1/mwToGW), genSet,df['GAMS Symbol'],'pCapac' + techLbl)
    # Generator zone
    add1dParam(db,getZonalParamDict(df, zoneOrder), genSet, df['GAMS Symbol'],'pGenzone' + techLbl)

def getZonalParamDict(df, zoneOrder, zonalCol='region'):
    zoneDict = df[zonalCol].map(zoneOrder).astype(int)
    zoneDict.index = df['GAMS Symbol']
    return zoneDict.to_dict()

##### ADD EXISTING OR NEW STORAGE PARAMETERS (scalars account for unit conversions)
def addStorageParams(db, df, stoSet, stoSymbols, mwToGW, stoMkts, newTechs=False):
    techLbl = 'tech' if newTechs else ''
    df = df.loc[df['GAMS Symbol'].isin(stoSymbols)]
    # Efficiency (fraction)
    add1dParam(db, getGenParamDict(df, 'Efficiency'), stoSet, df['GAMS Symbol'], 'pEfficiency' + techLbl)
    # For existing generators
    if not newTechs:
        # Charge capacity (GW) for existing storage or **TO IMPLEMENT** ratio of discharge to charge (fraction) for new storage
        add1dParam(db,getGenParamDict(df, 'Maximum Charge Rate (MW)', 1/mwToGW), stoSet, df['GAMS Symbol'], 'pCapaccharge' + techLbl)
        # Max SOC (GWh)
        add1dParam(db,getGenParamDict(df, 'Nameplate Energy Capacity (MWh)', 1/mwToGW), stoSet,df['GAMS Symbol'], 'pMaxsoc' + techLbl)
        # Min SOC (GWh)
        add1dParam(db,getGenParamDict(df, 'Minimum Energy Capacity (MWh)'), stoSet, df['GAMS Symbol'], 'pMinsoc' + techLbl)
    # Whether storage can provide energy in energy market
    if not newTechs: add0dParam(db, 'pStoinenergymarket', 1 if 'energy' in stoMkts else 0)

##### ADD EXISTING OR NEW GENERATOR UNIT COMMITMENT PARAMETERS (scalars account for unit conversions)
def addGenUCParams(db, df, genSet, mwToGW, newTechs=False):
    techLbl = 'tech' if newTechs else ''
    # Min load (GWh)
    add1dParam(db, getGenParamDict(df, 'MinLoad(MWh)', 1/mwToGW), genSet, df['GAMS Symbol'], 'pMinload' + techLbl)
    # Start up fixed cost (thousand$)
    add1dParam(db, getGenParamDict(df, 'StartCost($)', 1/1000), genSet, df['GAMS Symbol'], 'pStartupfixedcost' + techLbl)
    # Min down time (hours)
    add1dParam(db, getGenParamDict(df, 'MinDownTime(hrs)'), genSet, df['GAMS Symbol'], 'pMindowntime' + techLbl)
    # Regulation offer cost (thousand$/GW)
    # add1dParam(db,getGenParamDict(df,'RegOfferCost($/MW)'),genSet,df['GAMS Symbol'],'pRegoffercost' + techLbl)

##### ADD EXISTING RENEWABLE COMBINED MAXIMUM GENERATION VALUES
#Converts 1d list of param vals to hour-indexed dicts, then adds dicts to GAMS db
def addExistingRenewableMaxGenParams(db, hourSet, zoneSet, solarGen, windGen, mwToGW):
    add2dParam(db,convert2DTimeseriesDfToDict(solarGen, 1/mwToGW), zoneSet, hourSet,'pMaxgensolar')
    add2dParam(db,convert2DTimeseriesDfToDict(windGen, 1/mwToGW), zoneSet, hourSet,'pMaxgenwind')

###### ADD RESERVE PROVISION ELIGIBILITY (1 or 0 indicating can or can't provide reserve)
def addSpinReserveEligibility(db,df,genSet,newTechs=False):
    techLbl = 'tech' if newTechs else ''
    add1dParam(db,getGenParamDict(df, 'RegOfferElig'), genSet,df['GAMS Symbol'], 'pRegeligible' + techLbl)
    add1dParam(db,getGenParamDict(df, 'FlexOfferElig'), genSet,df['GAMS Symbol'], 'pFlexeligible' + techLbl)
    add1dParam(db,getGenParamDict(df, 'ContOfferElig'), genSet,df['GAMS Symbol'], 'pConteligible' + techLbl)

##### ADD EXISTING LINE PARAMETERS
def addLineParams(db, lineLimits, transmissionEff, lineSet, zoneOrder, mwToGW):
    # Transmission line limits
    add1dParam(db, pd.Series(lineLimits['TotalCapacity'].values.astype(float)/mwToGW, index=lineLimits['GAMS Symbol']).to_dict(), lineSet, lineLimits['GAMS Symbol'],'pLinecapac')
    # Transmission efficiency
    add0dParam(db,'pTransEff', transmissionEff)
    # Transmission line sources & sinks
    addLineSourceSink(db,lineLimits,lineSet,zoneOrder)

def addH2LineParams(db, H2lineLimits, transmissionEff, H2lineSet, zoneOrder, mwToGW):
    # Existing h2 pipeline between zone = 0:
    add1dParam(db, pd.Series(H2lineLimits['TotalCapacity'].values.astype(float)/mwToGW, index=H2lineLimits['GAMS Symbol']).to_dict(), H2lineSet, H2lineLimits['GAMS Symbol'],'pH2Linecapac')

def addLineSourceSink(db,df,lineSet,zoneOrder,techLbl=''):
    add1dParam(db,getZonalParamDict(df,zoneOrder,'r'), lineSet, df['GAMS Symbol'],'pLinesource'+techLbl)
    add1dParam(db,getZonalParamDict(df,zoneOrder,'rr'), lineSet, df['GAMS Symbol'],'pLinesink'+techLbl)
################################################################################
################################################################################
################################################################################

################################################################################
##################### CAPACITY EXPANSION PARAMETERS ############################
################################################################################
##### ADD NEW TECH PARAMS FOR CE
def addTechCostParams(db, df, coOptH2, genSet, stoSet, mwToGW):
    if not coOptH2:
        #Fixed O&M (thousand$/GW/yr):
        add1dParam(db,getGenParamDict(df,'FOM(2012$/MW/yr)', mwToGW/1000), genSet, df['GAMS Symbol'],'pFom')
        #Overnight capital cost (thousand$/GW)
        add1dParam(db,getGenParamDict(df,'CAPEX(2012$/MW)', mwToGW/1000), genSet, df['GAMS Symbol'],'pOcc')
        #Lifetime (years)
        add1dParam(db,getGenParamDict(df,'Lifetime(years)'), genSet, df['GAMS Symbol'],'pLife')

        #Power & energy capital costs for storage (thousand$/GW & thousand$/GWh)
        sto = df.loc[df['ThermalOrRenewableOrStorage']=='storage']
        add1dParam(db,getGenParamDict(sto,'CAPEX(2012$/MW)', mwToGW/1000), stoSet,sto['GAMS Symbol'], 'pPowOcc')
        add1dParam(db,getGenParamDict(sto,'ECAPEX(2012$/MWH)', mwToGW/1000), stoSet,sto['GAMS Symbol'], 'pEneOcc')
    else:
        # Fixed O&M (thousand$/GW/yr) or (thousand $/thousand ton/yr):
        add1dParam(db, getGenParamDict(df, 'FOM(2012$/MW/yr)', mwToGW / 1000), genSet, df['GAMS Symbol'], 'pFom')
        # Overnight capital cost (thousand$/GW) or (thousand $/thousand ton)
        add1dParam(db, getGenParamDict(df, 'CAPEX(2012$/MW)', mwToGW / 1000), genSet, df['GAMS Symbol'], 'pOcc')
        # Lifetime (years)
        add1dParam(db, getGenParamDict(df, 'Lifetime(years)'), genSet, df['GAMS Symbol'], 'pLife')

        # Power & energy capital costs for storage (thousand$/GW & thousand$/GWh)
        sto = df.loc[df['ThermalOrRenewableOrStorage'] == 'storage']
        add1dParam(db, getGenParamDict(sto, 'CAPEX(2012$/MW)', mwToGW / 1000), stoSet, sto['GAMS Symbol'], 'pPowOcc')
        add1dParam(db, getGenParamDict(sto, 'ECAPEX(2012$/MWH)', mwToGW / 1000), stoSet, sto['GAMS Symbol'], 'pEneOcc')
    
##### ADD PLANNING RESERVE MARGIN FRACTION PARAMETER (GW)
def addPlanningReserveParam(db, planningReserve, mwToGW):
    add0dParam(db,'pPlanningreserve',planningReserve/mwToGW)

##### ADD DISCOUNT RATE PARAMETER
def addDiscountRateParam(db, discountRate):
    add0dParam(db, 'pR', discountRate)

##### INITIAL SOC IN FIRST BLOCK FOR STORAGE (GWh)
def addStoInitSOCCE(db, df, stoSet, stoSymbols, mwToGW, initSOCFraction, newTechs=False):
    techLbl = 'tech' if newTechs else ''
    df = df.loc[df['GAMS Symbol'].isin(stoSymbols)]
    initSOCs = df['PlantType'].map(initSOCFraction)
    if newTechs:
        add1dParam(db,pd.Series(initSOCs.values,index=df['GAMS Symbol']).to_dict(), stoSet, df['GAMS Symbol'],'pInitSOC' + techLbl)
    else:
        initSOCs *= df['Nameplate Energy Capacity (MWh)']/mwToGW
        add1dParam(db, pd.Series(initSOCs.values,index=df['GAMS Symbol']).to_dict(), stoSet, df['GAMS Symbol'],'pInitSOC')

##### ADD HOURLY CAPACITY FACTORS FOR NEW RENEWABLE TECHS
#For wind and solar CFs, creates dict of (hour,techSymbol):CF, then adds them to GAMS db
def addRenewTechCFParams(db, renewTechSet, hourSet, newCFs):
    add2dParam(db, convert2DTimeseriesDfToDict(newCFs), renewTechSet, hourSet, 'pCf')

##### ADD CO2 EMISSIONS CAP (short tons)
def addCO2Cap(db, co2Cap):
    add0dParam(db, 'pCO2emcap', co2Cap)

##### ADD CONVERTERS (ELECTROLYZERS, FUEL CELLS, H2 TURBINES)
def addElectrolyzerCon(db, electrolyzerCon):
    add0dParam(db, 'pElectrolyzerCon', electrolyzerCon)
def addFuelCellCon(db, fuelcellCon):
    add0dParam(db, 'pFuelCellCon', fuelcellCon)
def addH2TurbineCon(db, h2TurbineCon):
    add0dParam(db, 'pH2TurbineCon', h2TurbineCon)

##### ADD CE PARAMETERS FOR BLOCKS
def addSeasonDemandWeights(db, blockWeights):
    for bl in blockWeights:
        add0dParam(db, 'pWeight' + createHourSubsetName(bl), blockWeights[bl])

def addBlockSOCScalars(db, scalars):
    for block in scalars:
        add0dParam(db, 'pSOCScalar' + createHourSubsetName(block), scalars[block])

##### ADD LIMIT ON MAX NUMBER OF NEW BUILDS PER TECH (#)
def addMaxNewBuilds(db, df, thermalSet, stoTechSet, dacsSet, CCSSet, maxCapPerTech, coOptH2, h2Pathway, SMRSet, ElectrolyzerSet, currYear, mwToGW):
    # Wind & solar
    for pt in ['Wind','Solar']:
        genCaps = df.loc[df['FuelType']==pt.capitalize(),'Capacity (MW)']
        add0dParam(db, 'pNMax'+pt.capitalize(), np.ceil(maxCapPerTech[pt]/genCaps.mean()))
    # Nuclear
    pt = 'Nuclear'
    genCaps = df.loc[df['PlantType']==pt.capitalize(),'Capacity (MW)']
    add0dParam(db, 'pNMaxNuclear', np.ceil(maxCapPerTech[pt]/genCaps.mean()))

    if coOptH2:
        pt = 'SR'
        genCaps = df.loc[df['PlantType'] == pt, 'Capacity (MW)']
        add0dParam(db, 'pNMaxSR', np.ceil(maxCapPerTech[pt] / genCaps.mean()))

    # CCS
    pt1 = 'Coal Steam CCS'
    pt2 = 'Combined Cycle CCS'
    pt = 'CCS'
    techs = df.loc[(df['PlantType'] == pt1) | (df['PlantType'] == pt2)]
    techs.index = techs['GAMS Symbol']
    maxBuilds = np.ceil(maxCapPerTech[pt] / techs['Capacity (MW)']).to_dict()
    add1dParam(db, maxBuilds, CCSSet, techs['GAMS Symbol'], 'pNMaxCCS')
    # CC
    pt = 'Combined Cycle'
    genCaps = df.loc[df['PlantType'] == pt, 'Capacity (MW)']
    add0dParam(db, 'pNMaxCC', np.ceil(maxCapPerTech[pt] / genCaps.mean()))
    # DACS
    ft = 'DAC'
    techs = df.loc[df['FuelType']==ft]
    techs.index = techs['GAMS Symbol']
    maxBuilds = np.ceil(maxCapPerTech[ft.capitalize()]/techs['Capacity (MW)']).to_dict()
    add1dParam(db, maxBuilds, dacsSet, techs['GAMS Symbol'], 'pNMaxDACS')
    # Storage. Use positive continuous variable for added power & energy separately,
    # so ignore capacity & set upper P & E bounds.
    ft = 'Energy Storage'
    techs = df.loc[df['FuelType'] == ft]
    techs.index = techs['GAMS Symbol']
    techs['Max Capacity (MW)'] = techs['PlantType'].map(maxCapPerTech)
    peRatio = techs['Nameplate Energy Capacity (MWh)']/techs['Capacity (MW)']
    maxESto = peRatio * techs['Max Capacity (MW)']/mwToGW
    add1dParam(db,(techs['Max Capacity (MW)']/mwToGW).to_dict(),stoTechSet, techs['GAMS Symbol'], 'pPMaxSto')
    add1dParam(db,maxESto.to_dict(),stoTechSet,techs['GAMS Symbol'], 'pEMaxSto')

    if coOptH2:
        # SMR
        pt = 'SMR'
        if h2Pathway != 'reference':
            df.loc[(df['PlantCategory'] == pt) & (df['region'] != 'WY'), 'Capacity (MW)'] = 0
        techs = df.loc[(df['PlantCategory'] == pt)]
        techs.index = techs['GAMS Symbol']
        maxBuilds = np.ceil(maxCapPerTech[pt] / techs['Capacity (MW)']).to_dict()
        for key, value in maxBuilds.items():
            if math.isinf(value):
                maxBuilds[key] = 0
        add1dParam(db, maxBuilds, SMRSet, techs['GAMS Symbol'], 'pNMaxSMR')

        # Electrolyzer
        pt = 'Electrolyzer'
        if h2Pathway != 'reference':
            if currYear <= 2035: df.loc[df['PlantType'] == pt, 'Capacity (MW)'] = 0
        if h2Pathway == 'blueToZeroWY':
            if currYear > 2035: df.loc[(df['PlantType'] == pt) & (df['region'] != 'WY'), 'Capacity (MW)'] = 0
        techs = df.loc[(df['PlantType'] == pt)]
        techs.index = techs['GAMS Symbol']
        maxBuilds = np.ceil(maxCapPerTech[pt] / techs['Capacity (MW)']).to_dict()
        for key, value in maxBuilds.items():
            if math.isinf(value):
                maxBuilds[key] = 0
        add1dParam(db, maxBuilds, ElectrolyzerSet, techs['GAMS Symbol'], 'pNMaxElectrolyzer')

        # Fuel Cell
        pt = 'Fuel Cell'
        genCaps = df.loc[df['PlantType'] == pt, 'Capacity (MW)']
        add0dParam(db, 'pNMaxFuelcell', np.ceil(maxCapPerTech[pt] / genCaps.mean()))

        # H2 Turbine
        pt = 'H2 Turbine'
        genCaps = df.loc[df['PlantType'] == pt, 'Capacity (MW)']
        add0dParam(db, 'PNMaxH2Turbine', np.ceil(maxCapPerTech[pt] / genCaps.mean()))

##### ADD NEW LINE PARAMETERS
def addNewLineParams(db, lineDists, lineCosts, lineSet, maxCapPerTech, buildLimitsCase, zoneOrder, interconn, mwToGW, lineLife=60):
    # Transmission costs = $/mw-mile * mw (= $/mw = thousand$/gw)
    if interconn == 'ERCOT':
        cost = pd.Series(lineCosts['Line Cost ($/mw-mile)'].values.astype(float), index=lineCosts['GAMS Symbol'])
        dist = pd.Series(lineDists['AC'].values.astype(float), index=lineDists['GAMS Symbol'])
    elif interconn == 'EI' or interconn == 'WECC':
        cost = pd.Series(lineCosts['cost($/mw-mile)'].values.astype(float), index=lineCosts['GAMS Symbol'])
        dist = pd.Series(lineDists['dist(mile)'].values.astype(float), index=lineDists['GAMS Symbol'])
    totalCost = cost*dist
    add1dParam(db, totalCost.to_dict(), lineSet, totalCost.index, 'pLinecost')
    # Maximum transmission expansion (GW)
    maxCapacs = pd.Series(maxCapPerTech['Transmission'], index=totalCost.index)/mwToGW #convert from MW to GW
    add1dParam(db, maxCapacs.to_dict(), lineSet, maxCapacs.index, 'pNMaxLine')
    # Lifetime of new lines
    add0dParam(db,'pLifeline', lineLife)

    # H2 pipeline cost = $3.72M/mile (The Future of Hydrogen, IEA report)
    maxH2LineCapac = 38.8/1.10231 # per unit if pipeline unit (ton)
    h2Cost = 3.72*1e6*(1/maxH2LineCapac)*dist
    h2LineLife = 40  # Years
    add1dParam(db, h2Cost.to_dict(), lineSet, h2Cost.index, 'pH2Linecost')
    add0dParam(db, 'pH2Lifeline', h2LineLife)
    # Maximum H2 pipeline capacity (metric ton)
    add1dParam(db, pd.Series(maxH2LineCapac, index=h2Cost.index).to_dict(), lineSet, h2Cost.index, 'pNMaxH2Line')

##### ADD INITIAL COMMITMENT STATE FOR EXISTING GENS FOR EACH TIME BLOCK
def addInitialOnOffForEachBlock(db, onOffInitialEachPeriod,genSet):
    print('NOT CHECKED addInitialOnOffForEachBlock')
    for block in onOffInitialEachPeriod:
        onOffBlockDict = onOffInitialEachPeriod[block]
        print(onOffBlockDict)
        add1dParam(db, onOffBlockDict, genSet, [g for g in onOffBlockDict],'pOnoroffinit' + createHourSubsetName(block))

##### ADD TOTAL LIMIT ON HYDROPOWER GENERATION BY BLOCK
def addHydroGenLimits(db, hydroGenCE, zoneSet, mwToGW):
    for block in hydroGenCE.index:
        add1dParam(db, (hydroGenCE.loc[block]/mwToGW).to_dict(),zoneSet,hydroGenCE.columns,'pMaxgenhydro' + createHourSubsetName(block))

################################################################################
################################################################################
################################################################################

################################################################################
##################### UNIT COMMITMENT PARAMETERS ###############################
################################################################################
def addStorageInitSOC(db, initSOC, stoGenSet, mwToGW):
    add1dParam(db, (initSOC/mwToGW).to_dict(), stoGenSet, initSOC.index, 'pInitsoc')

##### RESERVE PARAMETERS
def addReserveParameters(db, contRes, regUpRes, flexRes, rrToRegTime, rrToFlexTime, rrToContTime, hourSet, zoneSet, mwToGW):
    for p,v in zip(['pRampratetoregreservescalar','pRampratetoflexreservescalar','pRampratetocontreservescalar'],[rrToRegTime,rrToFlexTime,rrToContTime]):
        add0dParam(db,p,v)
    for p,df in zip(['pRegupreserves','pFlexreserves','pContreserves'], [regUpRes, flexRes,contRes]):
        add2dParam(db,convert2DTimeseriesDfToDict(df, 1/mwToGW), zoneSet, hourSet,p)
        
def addResIncParams(db, regUpInc, flexInc, renewTechSet, hourSet):
    for p,df in zip(['pRegUpReqIncRE','pFlexReqIncRE'], [regUpInc, flexInc]):
        add2dParam(db,convert2DTimeseriesDfToDict(df),renewTechSet, hourSet,p)
    
##### INITIAL CONDITIONS
# Always pass in energy values in MWh
def addEguInitialConditions(db, genSet, onOffInitial, genAboveMinInitial, mdtCarriedInitial,mwToGW):
    add1dParam(db, onOffInitial.to_dict(),genSet, onOffInitial.index, 'pOnoroffinitial')
    add1dParam(db, mdtCarriedInitial.to_dict(), genSet, mdtCarriedInitial.index, 'pMdtcarriedhours')
    add1dParam(db, (genAboveMinInitial/mwToGW).to_dict(), genSet, genAboveMinInitial.index, 'pGenabovemininitial')

def getInitialCondsDict(fleetUC, initialCondValues, scalar):
    initCondsDict = dict()
    for rowNum in range(1, len(fleetUC)):
        initCondsDict[createGenSymbol(fleetUC[rowNum], fleetUC[0])] = initialCondValues[rowNum-1] / scalar
    return initCondsDict

##### COST OF NON-SERVED ENERGY (thousand$/GWh)
def addCostNonservedEnergy(db, cnse):
    add0dParam(db, 'pCnse', cnse)

##### CO2 PRICE (thousand$/short ton)
def addCo2Price(db, co2Price):
    add0dParam(db,'pCO2Cost', co2Price/1000)
################################################################################
################################################################################
################################################################################

################################################################################
############ GENERIC FUNCTIONS TO ADD PARAMS TO GAMS DB ########################
################################################################################
def add0dParam(db, paramName, paramValue, paramDescrip=''):
    addedParam = db.add_parameter(paramName, 0, paramDescrip)
    addedParam.add_record().value = paramValue
    if len(addedParam.get_symbol_dvs())>0: print('Domain violations in ' + paramName)

def add1dParam(db, paramDict, idxSet, setSymbols, paramName, paramDescrip=''):
    addedParam = db.add_parameter_dc(paramName, [idxSet], paramDescrip)
    for idx in setSymbols: addedParam.add_record(str(idx)).value = paramDict[idx]
    if len(addedParam.get_symbol_dvs())>0: print('Domain violations in ' + paramName)

def add2dParam(db,param2dDict, idxSet1, idxSet2, paramName, paramDescrip=''):
    addedParam = db.add_parameter_dc(paramName, [idxSet1, idxSet2], paramDescrip)
    for k,v in iter(param2dDict.items()): addedParam.add_record(k).value = float(v)
    if len(addedParam.get_symbol_dvs())>0: print('Domain violations in ' + paramName)

def getGenParamDict(df,param, scalar=1):
    return (pd.Series(df[param].values.astype(float)*scalar, index=df['GAMS Symbol']).to_dict())

def convert2DTimeseriesDfToDict(df, scalar=1):
    d,dTuples = df.to_dict(), dict() #d is {col1:{idx1:val1,idx2:val2,etc.},etc.}
    for col in d:
        for hr,val in d[col].items(): 
            dTuples[(col,str(hr))] = float(val)*scalar
    return dTuples
################################################################################
################################################################################
################################################################################

