#Michael Craig
#October 4, 2016
#Functions for adding sets to GAMS database. Used for CE & UC models.

from GAMSAuxFuncs import *

########### ADD GENERATOR SETS #################################################
#Add gen sets & subsets
def addGeneratorSets(db, genFleet):
    genSet = addSet(db, genFleet['GAMS Symbol'].tolist(), 'egu')
    reFTs = ['Wind', 'Solar', 'Hydro']
    addSet(db,genFleet['GAMS Symbol'].loc[genFleet['FuelType'].isin(reFTs)].tolist(), 'renewegu')
    for reFT in reFTs:
        symbs = genFleet['GAMS Symbol'].loc[genFleet['FuelType'] == reFT]
        addSet(db, symbs.tolist() if symbs.shape[0] > 0 else [], reFT.lower() + 'egu')
    addSet(db,genFleet['GAMS Symbol'].loc[genFleet['PlantType'] == 'DAC'].tolist(), 'dacsegu')
    addSet(db, genFleet['GAMS Symbol'].loc[(genFleet['PlantType'] == 'SMR') | (genFleet['PlantType'] == 'Electrolyzer')].tolist(), 'h2egu')
    addSet(db, genFleet['GAMS Symbol'].loc[(genFleet['PlantType'] == 'H2Turbine') | (genFleet['PlantType'] == 'FuelCell')].tolist(), 'h2eegu')
    addSet(db, genFleet['GAMS Symbol'].loc[(genFleet['PlantType'] == 'FuelCell')].tolist(), 'fuelcellegu')
    addSet(db, genFleet['GAMS Symbol'].loc[(genFleet['PlantType'] == 'H2Turbine')].tolist(), 'h2turbineegu')
    addSet(db, genFleet['GAMS Symbol'].loc[(genFleet['PlantType'] == 'Electrolyzer')].tolist(), 'electrolyzeregu')
    return genSet

def addStoGenSets(db, genFleet, stoFTLabels):
    stoSymbols = genFleet.loc[genFleet['FuelType'].isin(stoFTLabels), 'GAMS Symbol'].tolist()
    stoGenSet = addSet(db, stoSymbols, 'storageegu')
    # hydrogen:
    h2stoSymbols = genFleet.loc[genFleet['PlantType'] == 'Hydrogen', 'GAMS Symbol'].tolist()
    h2stoGenSet = addSet(db, h2stoSymbols, 'h2storageegu')
    return stoGenSet, stoSymbols, h2stoGenSet, h2stoSymbols


def addStorageSubsets(db, genFleet, stoFTLabels):
    storage = genFleet.loc[genFleet['FuelType'].isin(stoFTLabels)]
    addSet(db,storage['GAMS Symbol'].loc[(storage['Nameplate Energy Capacity (MWh)']/storage['Capacity (MW)'] < 30*24)].tolist(),'ststorageegu') 
    addSet(db,storage['GAMS Symbol'].loc[(storage['Nameplate Energy Capacity (MWh)']/storage['Capacity (MW)'] >= 30*24)].tolist(),'ltstorageegu') 

########### ADD HOUR SETS ######################################################
#Add all hours
def addHourSet(db,hours):
    hourSymbols = hours.index.astype(str)
    hourSet = addSet(db,hourSymbols,'h')
    return hourSet,hourSymbols

#Define season subsets of hours
#Inputs: GAMS db, dict of (season:rep hrs)
def addHourSubsets(db,hoursForCE):
    for bl in hoursForCE.unique():
        blockHourSymbols = hoursForCE.loc[hoursForCE==bl].index.astype(str)
        addSet(db,blockHourSymbols,createHourSubsetName(bl))

def createHourSubsetName(subsetPrefix):
    return 'block' + str(subsetPrefix) + 'h'

#Define peak demand hour subset
def addPeakHourSubset(db,peakDemandHour):
    # addSet(db,[createHourSymbol(peakDemandHour)],'peakh')
    addSet(db,[str(peakDemandHour)],'peakh')

########### ADD ZONE AND LINE SETS #############################################
def addZoneSet(db,transRegions):
    zoneSymbols = [k for k in transRegions]
    zoneSet = addSet(db,zoneSymbols,'z')
    #Create dict of zone symbol:order of zone symbol in zone symbols
    ctr,zoneOrder = 1,dict() #GAMS ordering starts @ 1 so start ctr @ 1!
    for r in zoneSymbols: zoneOrder[r],ctr = ctr,ctr+1
    return zoneSet,zoneSymbols,zoneOrder

def addLineSet(db,limits):
    lineSymbols = limits['GAMS Symbol'].values
    lineSet = addSet(db,lineSymbols,'l')
    return lineSet,lineSymbols

def addH2LineSet(db,H2limits):
    H2lineSymbols = H2limits['GAMS Symbol'].values
    H2lineSet = addSet(db,H2lineSymbols,'H2l')
    return H2lineSet, H2lineSymbols

########### ADD NEW TECH SETS ##################################################
#Inputs: GAMS db, new techs (2d list)
def addNewTechsSets(db,newTechsCE):
    # All  techs
    techSet = addSet(db, newTechsCE['GAMS Symbol'].tolist(), 'tech')
    # Thermal techs
    thermalSet = addSet(db, newTechsCE['GAMS Symbol'].loc[newTechsCE['ThermalOrRenewableOrStorage'] == 'thermal'].tolist(), 'thermaltech')
    addSet(db, newTechsCE['GAMS Symbol'].loc[newTechsCE['PlantType'] == 'Nuclear'].tolist(), 'nucleartech')
    addSet(db, newTechsCE['GAMS Symbol'].loc[newTechsCE['PlantType'] == 'SR'].tolist(), 'srtech')
    addSet(db, newTechsCE['GAMS Symbol'].loc[newTechsCE['PlantType'] == 'Combined Cycle'].tolist(), 'CCtech')
    CCSSet = addSet(db, newTechsCE['GAMS Symbol'].loc[(newTechsCE['PlantCategory'] == 'CCS')].tolist(), 'CCStech')
    # H2 producing techs:
    h2Set = addSet(db, newTechsCE['GAMS Symbol'].loc[newTechsCE['ThermalOrRenewableOrStorage'] == 'h2'].tolist(), 'h2tech')
    ElectrolyzerSet = addSet(db, newTechsCE['GAMS Symbol'].loc[newTechsCE['PlantType'] == 'Electrolyzer'].tolist(), 'electrolyzertech')
    SMRSet = addSet(db, newTechsCE['GAMS Symbol'].loc[(newTechsCE['PlantCategory'] == 'SMR')].tolist(), 'smrtech')
    # H2 to electricity techs:
    h2TSet = addSet(db, newTechsCE['GAMS Symbol'].loc[(newTechsCE['PlantCategory'] == 'FuelCell') | (newTechsCE['PlantCategory'] == 'H2Turbine')].tolist(), 'h2etech')
    addSet(db, newTechsCE['GAMS Symbol'].loc[(newTechsCE['PlantCategory'] == 'FuelCell')].tolist(), 'fuelcelltech')
    addSet(db, newTechsCE['GAMS Symbol'].loc[(newTechsCE['PlantCategory'] == 'H2Turbine')].tolist(), 'h2turbinetech')
    # Renewables
    reSet = addSet(db, newTechsCE['GAMS Symbol'].loc[newTechsCE['ThermalOrRenewableOrStorage'] == 'renewable'].tolist(), 'renewtech')
    addSet(db, newTechsCE['GAMS Symbol'].loc[newTechsCE['FuelType'] == 'Wind'].tolist(), 'windtech')
    addSet(db, newTechsCE['GAMS Symbol'].loc[newTechsCE['FuelType'] == 'Solar'].tolist(), 'solartech')
    # Storage
    storage = newTechsCE.loc[newTechsCE['ThermalOrRenewableOrStorage'] == 'storage']
    stoSymbols = storage['GAMS Symbol'].tolist()
    stoSet = addSet(db, stoSymbols, 'storagetech')
    addSet(db, storage['GAMS Symbol'].loc[(storage['Nameplate Energy Capacity (MWh)'] / storage['Capacity (MW)'] < 30 * 24)].tolist(), 'ststoragetech')
    addSet(db, storage['GAMS Symbol'].loc[(storage['Nameplate Energy Capacity (MWh)'] / storage['Capacity (MW)'] >= 30 * 24)].tolist(), 'ltstoragetech')
    # DACS
    dacsSet = addSet(db, newTechsCE['GAMS Symbol'].loc[newTechsCE['FuelType'] == 'DAC'].tolist(), 'dacstech')
    return techSet, reSet, stoSet, stoSymbols, thermalSet, dacsSet, CCSSet, h2Set, SMRSet, ElectrolyzerSet, h2TSet

def addNewLineSet(db,dists):
    lineSymbols = dists['GAMS Symbol'].values
    lineSet = addSet(db,lineSymbols,'ltech')
    return lineSet,lineSymbols

########### GENERIC FUNCTION TO ADD SET TO DATABASE ############################
#Adds set to GAMS db
def addSet(db,setSymbols,setName,setDim=1,setDescription=''):
    addedSet = db.add_set(setName, setDim, setDescription) 
    for symbol in setSymbols: addedSet.add_record(symbol) 
    return addedSet
