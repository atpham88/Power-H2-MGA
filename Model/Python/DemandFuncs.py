#Michael Craig
#October 4, 2016
#Functions related to electricity demand profile

import operator, os, sys, pandas as pd
from AuxFuncs import *

########### GET SCALED DEMAND BASED ON CURRENT YEAR ############################
#Inputs: initial demand values (1d list), annual demand growth (fraction), 
#year of initial demand values, current CE year
#Outputs: demand values in current CE year (1d list)
def getDemandForFutureYear(demand,annualDemandGrowth,metYear,currYear,electrifiedDemand,
                            transRegions,elecDemandScen):
    if currYear > 2050: currYear = 2050
    if electrifiedDemand:
        demand = importHourlyEFSDemand(currYear,transRegions,elecDemandScen)
    else:
        demandScalar = (1 + annualDemandGrowth)**(currYear - metYear)
        print(demand)
        for region in demand: demand[region] *= demandScalar
        print(demand)
        sys.exit('have not tested thsi code section yet')
    return demand

########### IMPORT DEMAND DATA FROM ELECTRIFICATION FUTURES STUDY ##############
def importHourlyEFSDemand(currYear,transRegions,elecDemandScen):
    #Initialize df
    if currYear > 2050: currYear = 2050
    dates = pd.date_range('1/1/'+str(currYear)+' 0:00','12/31/' + str(currYear) + ' 23:00',freq='H')
    dates = dates[~((dates.month == 2) & (dates.day == 29))] #ditch leap day
    demand = pd.DataFrame(index=dates)
    #Read EFS data
    filename = 'EP' + elecDemandScen + '_FlexNONEload_hourly.csv'
    rawDemand = pd.read_csv(os.path.join('Data','REEDS', filename), delimiter=',',header=0)
    rawDemand = rawDemand.loc[rawDemand['year']==currYear]

    #Iterate through dict of zone:p regions (from REEDS) & aggregate demand for p-regions
    for zone,pRegions in transRegions.items():
        for p in pRegions:
            pDemand = rawDemand[p]
            if zone in demand.columns:
                demand[zone] += pDemand.values
            else:
                demand[zone] = pDemand.values
    return demand

########### GET NET DEMAND AND REMOVE WIND & SOLAR FROM FLEET ##################
#Inputs: hourly demand values (1d list w/out header), wind and solar CFs (2d list),
#list of solar/wind IDs and their capacities in fleet (2d list), 
#current CE year, name of model (CE versus UC)
#Outputs: net demand (1d list w/out headers), hourly wind and solar gen (1d lists w/out headers)
def getNetDemand(hourlyDemand,windCFs,ewdIdAndCapac,solarCFs,solarFilenameAndCapac):
    hourlyWindGen = getHourlyGenProfile(windCFs,ewdIdAndCapac)
    hourlySolarGen = getHourlyGenProfile(solarCFs,solarFilenameAndCapac)
    netDemand = calcNetDemand(hourlyDemand,hourlyWindGen,hourlySolarGen)
    return (netDemand,hourlyWindGen,hourlySolarGen)

#Inputs: CFs (2d list w/ header), unit ids and capacities (2d list w/ header)
#Outputs: hourly generation values (1d list w/out header)
def getHourlyGenProfile(cfs,idAndCapacs):
    (idCol,capacCol) = (idAndCapacs[0].index('Id'),idAndCapacs[0].index('FleetCapacity')) 
    totalHourlyGen = []
    for idAndCapac in idAndCapacs[1:]:
        (unitID,capac) = (idAndCapac[idCol],idAndCapac[capacCol])
        cfRow = [row[1:] for row in cfs[1:] if row[0]==unitID]
        hourlyGen = [capac*cf for cf in cfRow[0]]
        if totalHourlyGen==[]: totalHourlyGen = hourlyGen
        else: 
            for hr in range(len(hourlyGen)): totalHourlyGen[hr] += hourlyGen[hr]
    return totalHourlyGen

#Inputs: hourly demand & wind & solar gen (1d lists w/out headers)
#Outputs: hourly net demand (1d list w/out headers)
def calcNetDemand(hourlyDemand,hourlyWindGen,hourlySolarGen):
    if len(hourlyWindGen)>0 and len(hourlySolarGen)>0:
        hourlyWindAndSolarGen = list(map(operator.add,hourlyWindGen,hourlySolarGen))
        return list(map(operator.sub,hourlyDemand,hourlyWindAndSolarGen))
    elif len(hourlyWindGen)>0:
        return list(map(operator.sub,hourlyDemand,hourlyWindGen))
    elif len(hourlySolarGen)>0:
        return list(map(operator.sub,hourlyDemand,hourlySolarGen))
    else:
        return hourlyDemand