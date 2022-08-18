#Michael Craig
#October 12, 2016
#Remove hydro (normal + pumped storage) units from fleet and subtract their monthly average generation
#from demand profile.

import copy, operator, os, numpy as np
from AuxFuncs import *

########### MASTER FUNCTION ####################################################
#Inputs: gen fleet, demand profile (1d list of hourly demand values)
#Outputs: gen fleet w/out hydro units, demand profile w/ average monthly 
#hydro generation subtracted (1d list of hourly values)
def removeHydroFromFleetAndDemand(genFleet,demand):
    eia923years = list(range(2016,2019))
    hydroRows,genFleet = genFleet.loc[genFleet['FuelType']=='Hydro'],genFleet.loc[genFleet['FuelType']!='Hydro']
    demandMinusHydroGen = removeHydroGenFromDemand(hydroRows,demand,eia923years)
    return (genFleet,demandMinusHydroGen)
################################################################################

########### REMOVE HYDRO GENERATION FROM DEMAND ################################
#Returns 1d list of demand minus average monthly hydro generation
def removeHydroGenFromDemand(allHydroRows,demand,eia923years):
    for region in allHydroRows['region'].unique():
        hydroRows = allHydroRows.loc[allHydroRows['region']==region]
        plantCapacs = hydroRows.groupby('ORIS Plant Code')['Capacity (MW)'].apply(lambda x: np.sum(x.astype(float))).reset_index()
        plantCapacs.index = plantCapacs['ORIS Plant Code']
        orisIDtoCapac = plantCapacs['Capacity (MW)'].to_dict()
        hydroAvgMonthlyGen = getTotalHydroAvgMonthlyGen(orisIDtoCapac,eia923years)
        hourlyHydroGen = expandMonthlyGenToHourly(hydroAvgMonthlyGen)
        assert(demand[region].shape[0] == len(hourlyHydroGen)) #make sure same length
        demand[region] -= hourlyHydroGen
    return demand

#Get total average monthly hydro generation by getting monthly generation per year
#for each unit, then adding average values.
#Inputs: dict mapping ORIS id to capac of all hydro units, years of EIA 923
#data to use, & dir of that data.
#Outputs: 1d list (len=12) of average total hydro generation per month
def getTotalHydroAvgMonthlyGen(orisIDtoCapac,eia923years):
    (orisIDtoMonthlyGen,orisIDtoMonthlyGenCount) = (dict(),dict())
    for orisId in orisIDtoCapac: orisIDtoMonthlyGen[orisId],orisIDtoMonthlyGenCount[orisId] = [],[]
    for year in eia923years:
        (orisIDtoMonthlyGen,orisIDtoMonthlyGenCount) = getMonthlyGenInYear(orisIDtoMonthlyGen,
                                                        orisIDtoMonthlyGenCount,year)
    return getCombinedAverageMonthlyGen(orisIDtoMonthlyGen,orisIDtoMonthlyGenCount)
     
#For each hydro unit in fleet, get monthly generation in a given year.
#Inputs: dict mapping oris ID to list of monthly gen, dict mapping ORIS ID to 
#list of count of gen values per month, year of analysis, dir w/ EIA 923 data
#Outputs: dict mapping oris ID to list of monthly gen, dict mapping ORIS ID to 
#list of count of gen values per month
def getMonthlyGenInYear(orisIDtoMonthlyGen,orisIDtoMonthlyGenCount,year):
    numMonths,idCol,idLabel,genFile = 12,0,'Plant Id','gen' + str(year) + '.csv'
    genData = readCSVto2dList(os.path.join('Data','EIA923',genFile))
    firstColVals = [row[idCol] for row in genData]
    headsRow = firstColVals.index(idLabel) #this has detailed header rows; 1 row up are overarching headers, hence -1 in next line
    netGenFirstCol = genData[headsRow-1].index('Electricity Net Generation (MWh)')
    if 'Reported Fuel Type Code' in genData[headsRow]: fuelCol = genData[headsRow].index('Reported Fuel Type Code') 
    else: fuelCol = genData[headsRow].index('Reported\nFuel Type Code') 
    for row in genData[headsRow+1:]:
        (orisId,fuel) = (int(row[idCol]),row[fuelCol])
        if orisId in orisIDtoMonthlyGen and fuel == 'WAT':
            monthlyGen = [toNum(row[idx]) for idx in range(netGenFirstCol,netGenFirstCol+numMonths)]
            if orisIDtoMonthlyGen[orisId]==[]:
                orisIDtoMonthlyGen[orisId] = monthlyGen
                orisIDtoMonthlyGenCount[orisId] = [1]*len(monthlyGen)
            else:
                orisIDtoMonthlyGen[orisId] = list(map(operator.add,orisIDtoMonthlyGen[orisId],monthlyGen))
                orisIDtoMonthlyGenCount[orisId] = list(map(operator.add,orisIDtoMonthlyGenCount[orisId],[1]*len(monthlyGen)))
    return (orisIDtoMonthlyGen,orisIDtoMonthlyGenCount)

#For each unit, calculate average monthly gen, then add value to 
#running total of hydro gen for all units. 
#Inputs: dict mapping oris ID to list of monthly gen, dict mapping ORIS ID to 

#list of count of gen values per month
#Outputs: 1d list of total hydro average monthly gen (len=12)
def getCombinedAverageMonthlyGen(orisIDtoMonthlyGen,orisIDtoMonthlyGenCount):
    combinedAverageGen = []
    for orisId in orisIDtoMonthlyGen:
        (monthlyGen,count) = (orisIDtoMonthlyGen[orisId],orisIDtoMonthlyGenCount[orisId])
        averageMonthlyGen = [monthlyGen[idx]/count[idx] for idx in range(len(monthlyGen))]
        if monthlyGen != []:
            if combinedAverageGen==[]: combinedAverageGen = copy.copy(averageMonthlyGen)
            else: combinedAverageGen = list(map(operator.add,combinedAverageGen,averageMonthlyGen))
    return combinedAverageGen

#Expand average monthly generation from 1d list of len=12 to 1d list of n=8760.
#Also spreads out average monthly generation to hourly generation values,
#assuming equal generation per hour. 
def expandMonthlyGenToHourly(hydroAvgMonthlyGen):
    hoursPerDay = 24
    daysPerMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
    hydroAvgMonthlyGenHourly = []
    for idx in range(len(hydroAvgMonthlyGen)):
        (days,avgMonthlyGen) = (daysPerMonth[idx],hydroAvgMonthlyGen[idx])
        hourlyGen = avgMonthlyGen/(hoursPerDay*days)
        hydroAvgMonthlyGenHourly += [hourlyGen]*(hoursPerDay*days)
    return hydroAvgMonthlyGenHourly
################################################################################

########### HELPER FUNCTION ####################################################
#Converts a string w/ commas in it to a float
def toNum(s):
    numSegments = s.split(',')
    result = ""
    for segment in numSegments:
        result += segment
    return float(result) if result != '.' else 0
################################################################################