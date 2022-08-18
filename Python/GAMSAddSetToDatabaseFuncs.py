#Michael Craig
#October 4, 2016
#Functions for adding sets to GAMS database. Used for CE & UC models.

from GAMSAuxFuncs import *

########### ADD GENERATOR SETS #################################################
#Add gen sets & subsets
def addGeneratorSets(db,genFleet):
    genSet = addSet(db,genFleet['GAMS Symbol'].tolist(),'egu') 
    reFTs = ['Wind','Solar']
    addSet(db,genFleet['GAMS Symbol'].loc[genFleet['FuelType'].isin(reFTs)].tolist(),'renewegu') 
    for reFT in reFTs: addSet(db,genFleet['GAMS Symbol'].loc[genFleet['FuelType']==reFT].tolist(),reFT.lower()+'egu') 
    addSet(db,genFleet['GAMS Symbol'].loc[genFleet['PlantType'] == 'DAC'].tolist(),'dacsegu')
    return genSet

def addStoGenSets(db,genFleet):
    stoSymbols = genFleet['GAMS Symbol'].loc[genFleet['FuelType']=='Energy Storage'].tolist()
    stoGenSet = addSet(db,stoSymbols,'storageegu') 
    return stoGenSet,stoSymbols

def addStorageSubsets(db,genFleet):
    storage = genFleet.loc[genFleet['FuelType']=='Energy Storage']
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

########### ADD NEW TECH SETS ##################################################
#Inputs: GAMS db, new techs (2d list)
def addNewTechsSets(db,newTechsCE):
    #All techs
    techSet = addSet(db,newTechsCE['GAMS Symbol'].tolist(),'tech') 
    #Thermal techs
    thermalSet = addSet(db,newTechsCE['GAMS Symbol'].loc[newTechsCE['ThermalOrRenewableOrStorage']=='thermal'].tolist(),'thermaltech')    
    addSet(db, newTechsCE['GAMS Symbol'].loc[newTechsCE['PlantType'] == 'Nuclear'].tolist(), 'nucleartech')
    addSet(db, newTechsCE['GAMS Symbol'].loc[newTechsCE['PlantType'] == 'Combined Cycle'].tolist(), 'CCtech')
    CCSSet = addSet(db, newTechsCE['GAMS Symbol'].loc[(newTechsCE['PlantCategory'] == 'CCS')].tolist(), 'CCStech')
    #Renewables
    reSet = addSet(db,newTechsCE['GAMS Symbol'].loc[newTechsCE['ThermalOrRenewableOrStorage']=='renewable'].tolist(),'renewtech') 
    addSet(db,newTechsCE['GAMS Symbol'].loc[newTechsCE['FuelType']=='Wind'].tolist(),'windtech')
    addSet(db,newTechsCE['GAMS Symbol'].loc[newTechsCE['FuelType']=='Solar'].tolist(),'solartech')
    #Storage
    storage = newTechsCE.loc[newTechsCE['ThermalOrRenewableOrStorage']=='storage']
    stoSymbols = storage['GAMS Symbol'].tolist()
    stoSet = addSet(db,stoSymbols,'storagetech')
    addSet(db,storage['GAMS Symbol'].loc[(storage['Nameplate Energy Capacity (MWh)']/storage['Capacity (MW)'] < 30*24)].tolist(),'ststoragetech') 
    addSet(db,storage['GAMS Symbol'].loc[(storage['Nameplate Energy Capacity (MWh)']/storage['Capacity (MW)'] >= 30*24)].tolist(),'ltstoragetech')
    #DACS
    dacsSet = addSet(db,newTechsCE['GAMS Symbol'].loc[newTechsCE['FuelType']=='DAC'].tolist(),'dacstech')
    return techSet,reSet,stoSet,stoSymbols,thermalSet,dacsSet,CCSSet

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
