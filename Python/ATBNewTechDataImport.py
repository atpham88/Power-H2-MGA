#Michael Craig
#Nov 11, 2016

#Script imports data from NREL ATB CSVs created for each technology
#of interest, and then saves data for each tech in new CSV. Also outputs
#relevant data for each tech.

#NOTE: To run this script, need to save CSV files of each separate page from 
#ATB Excel file. Also, CAPEX param name in Coal file had an extra space,
#and FOM label for wind was messed up.

import os, copy
from AuxFuncs import *

def setKeyParameters():
    #Special scenario
    lowSolar = False #if get low solar costs (rather than mid cap cost)
    lowNuclear = False #if get low nuclear costs
    #Other parameters
    plantCsvNames = ['solar','wind','coal','gas','nuclear']
    paramAtbNames = {'Heat Rate  (MMBtu/MWh)':'HR(Btu/kWh)','CAPEX ($/kW)':'CAPEX(2012$/MW)',
                    'Fixed Operation and Maintenance Expenses ($/kW-yr)':'FOM(2012$/MW/yr)',
                    'Variable Operation and Maintenance Expenses ($/MWh)':'VOM(2012$/MWh)'} #ABT costs in $2014
    paramAtbScalar = {'HR(Btu/kWh)':1000,'CAPEX(2012$/MW)':1000,'FOM(2012$/MW/yr)':1000,
                        'VOM(2012$/MWh)':1} #multiplied into val
    convert2014to2012Dollars = 229.6/236.7
    for param in paramAtbScalar: paramAtbScalar[param] = paramAtbScalar[param]*convert2014to2012Dollars
    csvToTechType = {'solar':'Solar PV','wind':'Wind','nuclear':'Nuclear',
                    'coal':('Coal Steam','Coal Steam CCS'),
                    'gas':('Combined Cycle','Combined Cycle CCS','Combustion Turbine')}
    if lowSolar == False: newTechFrameworkCsv = 'NewTechFramework.csv'
    elif lowSolar == True: newTechFrameworkCsv = 'NewTechFrameworkLowSolarCost.csv'
    atbDir = 'C:\\Users\\mtcraig\\Desktop\\EPP Research\\NewPlantData\\ATB'
    newTechFramework = readCSVto2dList(os.path.join(atbDir,newTechFrameworkCsv))
    return (plantCsvNames,atbDir,paramAtbNames,newTechFramework,csvToTechType,paramAtbScalar,
                lowSolar,lowNuclear)

#Set key params, then compile new tech data
def getNewPlantATBData():
    (plantCsvNames,atbDir,paramAtbNames,newTechFramework,csvToTechType,
                paramAtbScalar,lowSolar,lowNuclear) = setKeyParameters()    
    newTechData = compileNewTechData(atbDir,plantCsvNames,paramAtbNames,newTechFramework,csvToTechType,
                                    paramAtbScalar,lowSolar,lowNuclear)
    
#Puts all new tech data into single 2d list. Loops over each input CSV name,
#then goes through each plant type of interst in that CSV. Writes 2d list
#of compiled results.
def compileNewTechData(atbDir,plantCsvNames,paramAtbNames,newTechFramework,csvToTechType,
                        paramAtbScalar,lowSolar,lowNuclear):
    newTechData = []
    newTechData.append(['TechnologyType','Parameter'] + [val for val in range(2014,2051)])
    for plantCSV in plantCsvNames:
        if type(csvToTechType[plantCSV])==tuple:
            for fleetTechType in csvToTechType[plantCSV]:
                plantData = readDataFromCSV(atbDir,plantCSV,newTechFramework,fleetTechType,paramAtbNames,
                                            paramAtbScalar,lowNuclear)
                newTechData += plantData
        else:
            fleetTechType = csvToTechType[plantCSV]
            plantData = readDataFromCSV(atbDir,plantCSV,newTechFramework,fleetTechType,
                                        paramAtbNames,paramAtbScalar,lowNuclear)
            newTechData += plantData
    if lowSolar == True: write2dListToCSV(newTechData,os.path.join(atbDir,'newTechDataATBLowSolarCost.csv'))
    elif lowNuclear == True: write2dListToCSV(newTechData,os.path.join(atbDir,'newTechDataATBLowNukeCost.csv'))
    else: write2dListToCSV(newTechData,os.path.join(atbDir,'newTechDataATB.csv'))
    return newTechData

#Reads in data from CSV by finding where data starts, then going through
#each block of future values and saving thse values for parameters of interest.
def readDataFromCSV(atbDir,plantCSV,newTechFramework,fleetTechType,paramAtbNames,
                    paramAtbScalar,lowNuclear):
    techData = readCSVto2dList(os.path.join(atbDir,plantCSV + '.csv'))
    atbTechType = getAtbTechType(fleetTechType,newTechFramework)
    futureProjectionsRow = findFutureProjectionsRow(techData,plantCSV)
    techDataFuture = copy.deepcopy(techData[futureProjectionsRow:])
    paramNameCol = findParamNameCol(techDataFuture,plantCSV)
    currNewTechData = []
    for idx in range(len(techDataFuture)):
        if techDataFuture[idx][paramNameCol] in paramAtbNames:
            fleetParamName = paramAtbNames[techDataFuture[idx][paramNameCol]]
            if fleetParamName == 'CAPEX(2012$/MW)' and fleetTechType == 'Nuclear' and lowNuclear == True:
                paramData = getNukeLowCapCostData(atbDir,paramAtbScalar[fleetParamName])
            else:
                paramData = getParamData(atbTechType,techDataFuture[idx:],paramNameCol,
                                        paramAtbScalar[fleetParamName])
            currNewTechData.append([fleetTechType,fleetParamName] + paramData)
    return currNewTechData

def getAtbTechType(fleetTechType,newTechFramework):
    (techTypeCol,atbTechTypeCol) = (newTechFramework[0].index('TechnologyType'),
                                    newTechFramework[0].index('ATBTechnologyType'))
    techs = [row[techTypeCol] for row in newTechFramework]
    atbTechs = [row[atbTechTypeCol] for row in newTechFramework]
    return atbTechs[techs.index(fleetTechType)]

def findFutureProjectionsRow(techData,plantCSV):
    futProjKeyword = 'Future Projections'
    for idx in range(len(techData)):
        for val in techData[idx]:
            if val == futProjKeyword: return idx
    print('Did not find future projection for CSV:',plantCSV)

def findParamNameCol(techDataFuture,plantCSV):
    firstParamName = 'Net Capacity Factor (%)'
    for row in techDataFuture:
        for colIdx in range(len(techDataFuture[0])):
            if row[colIdx] == firstParamName: return colIdx 
    print('Did not find param name for CSV:',plantCSV)

def getParamData(atbTechType,techDataParam,paramNameCol,paramScalar):
    abtTechTypeCol = paramNameCol + 1
    abtTechTypes = [row[abtTechTypeCol] for row in techDataParam]
    dataRowIdx = abtTechTypes.index(atbTechType)
    paramData = techDataParam[dataRowIdx][abtTechTypeCol+1:abtTechTypeCol+1+(2050-2014)+1]
    return [convertToNum(val)*paramScalar for val in paramData]

def convertToNum(val):
    return float(val.replace("$","").replace(",",""))

def getNukeLowCapCostData(atbDir,paramScalar):
    nukeCapCost = readCSVto2dList(os.path.join(atbDir,'nuclearLowCost.csv'))
    dataRowIdx = [row[0] for row in nukeCapCost].index('CAPEX ($/kW)')
    return [convertToNum(val)*paramScalar for val in nukeCapCost[dataRowIdx][1:]]

getNewPlantATBData()