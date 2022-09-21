#Michael Craig
#October 12, 2016
#Remove hydro (normal + pumped storage) units from fleet and subtract their monthly average generation
#from demand profile.

import copy, operator, os, numpy as np, pandas as pd, calendar
from CombinePlants import combinePlantsByRegion

#Inputs: gen fleet, demand and net demand dataframes
#Outputs: demand & net demand minus hydropower generation
def processHydro(genFleet, demand, netDemand, metYear, removeHydro):
    if 'Hydro' in genFleet['FuelType'].unique():
        #Get EIA data
        netGenCols = ['Netgen_'+ calendar.month_name[i][:3] for i in range(1,13)]
        yrGen = import923(metYear,netGenCols)

        #Convert EIA data to hourly
        hourGenAll = convert923ToHourlyGen(yrGen,genFleet,netDemand,netGenCols)

        #If removing hydro gen from demand, remove hydro from fleet; otherwise
        #aggregate hydro by zone
        if removeHydro:
            demand -= hourGenAll
            genFleet = genFleet.loc[genFleet['FuelType'] != 'Hydro']
        else: 
            for r in genFleet['region'].unique(): genFleet = combinePlantsByRegion(genFleet,'FuelType','Hydro',r)
    else: #create dummy copy of hourGenAll for later functions
        hourGenAll = demand.copy()
        hourGenAll *= 0

    return genFleet, hourGenAll, demand

def convert923ToHourlyGen(yrGen,genFleet,netDemand,netGenCols):
    hydroUnits = genFleet.loc[genFleet['FuelType'] == 'Hydro']
    hourGenAll = pd.DataFrame(index=netDemand.index,columns=netDemand.columns)
    for region in hydroUnits['region'].unique():
        #Aggregate hydro generators to plants, then get regional total capacity
        hydroRegion = hydroUnits.loc[hydroUnits['region']==region]
        initCap = hydroRegion['Capacity (MW)'].sum()
        capac = hydroRegion.groupby('ORIS Plant Code')['Capacity (MW)'].apply(lambda x: np.sum(x.astype(float))).reset_index()
        capac.index = capac['ORIS Plant Code']
        totalCapac = capac['Capacity (MW)'].sum()
        assert((initCap-totalCapac)<.01*initCap)
        
        #Match EIA data to hydro units
        genRegion = capac.merge(yrGen,how='left',left_index=True,right_index=True)

        #Get hourly generation based on regional net demand
        for mnth in range(1,13):
            #Get total month generation
            monthGen = genRegion[netGenCols[mnth-1]].sum()

            #Calculate hourly weights to determine hourly generation
            monthNetDemand = netDemand.loc[netDemand.index.month==mnth,region]
            monthNetDemand.loc[monthNetDemand<0] = 0 #sometimes negative, which messes w/ weights; so set these to zero

            #Calculate normalized weights so sum = 1, avoiding special case of all hours having negative net demand
            if int(monthNetDemand.max()) != 0: 
                wt = monthNetDemand/(monthNetDemand.max())
                wt = wt/wt.sum() 
            else: 
                wt = pd.Series(1/monthNetDemand.shape[0],index=monthNetDemand.index,name=region)

            # Estimate hourly generation using weights
            hourGen = monthGen * wt
            assert((hourGen.sum()-monthGen)<.01*monthGen)

            #If generation exceeds capacity in hours, reallocate that generation surplus to other hours
            hoursAboveCap,hoursBelowCap = hourGen.loc[hourGen>=totalCapac],hourGen.loc[hourGen<totalCapac]
            surplus = (hoursAboveCap - totalCapac).sum()
            while surplus > 0 and hoursBelowCap.shape[0] > 0:
                #Evenly spread surplus generation across hours below capacity
                hourGen[hoursBelowCap.index] += surplus/hoursBelowCap.shape[0]
                #Cap generation at capacity
                hourGen[hoursAboveCap.index] = totalCapac
                #Reassign hours and recalculate surplus
                hoursAboveCap,hoursBelowCap = hourGen.loc[hourGen>=totalCapac],hourGen.loc[hourGen<totalCapac]
                surplus = (hoursAboveCap - totalCapac).sum()

            #Might exit while loop w/ remaining surplus - if so, all hours are full, so truncate
            if surplus > 0: hourGen.loc[hourGen>=totalCapac] = totalCapac

            #Place gen for month & region into df w/ all months & regions
            hourGenAll.loc[hourGen.index,region] = hourGen
        
            #Make sure all generation was allocated (or dropped as surplus)
            assert((monthGen - (hourGen.sum()+surplus))<.0001*monthGen)
    return hourGenAll

def import923(metYear,netGenCols):
    #Import, skipping empty top rows
    yrGen = pd.read_csv(os.path.join('Data','EIA923','gen' + str(metYear) + '.csv'),skiprows=5,header=0,thousands=',')
    yrGen = yrGen[['Plant Id','Reported Fuel Type Code']+netGenCols]

    #Data very rarely has a missing value - replace with a zero for simplicity
    yrGen = yrGen.replace('.',0)

    #Slim down to hydro facilities
    yrGen = yrGen.loc[yrGen['Reported Fuel Type Code'] == 'WAT']
    yrGen.drop(['Reported Fuel Type Code'],axis=1,inplace=True)

    #Get rid of , text and convert to float (thousands=',' doesn't work above)
    for i in range(1,13):
        lbl = 'Netgen_'+calendar.month_name[i][:3]
        yrGen[lbl] = yrGen[lbl].astype(str).str.replace(',','')
        yrGen[lbl] = yrGen[lbl].astype(float)

    #Aggregate unit to plant level
    yrGen = yrGen.groupby('Plant Id').apply(lambda x: np.sum(x.astype(float))).reset_index(drop=True)

    #Reindex
    yrGen['Plant Id'] = yrGen['Plant Id'].astype(int)
    yrGen.index = yrGen['Plant Id']
    yrGen.drop(['Plant Id'],axis=1,inplace=True)

    return yrGen


