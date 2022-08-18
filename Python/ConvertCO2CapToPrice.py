#Michael Craig
#October 4, 2016
#Converts annual CO2 cap into a CO2 price. Two methods: run ED model in GAMS
#or use generation stack.

import pandas as pd, numpy as np

#Calculate net demand, then for each hour of year, calculate op cost of all gens
#for given co2 price, arrange in increasing cost order, and meet demand using
#gen stack. Based on gen stack, calculate hourly emissions.
def convertCo2CapToPrice(genFleet,hourlyWindGen,hourlySolarGen,demand,co2Cap,scaleLbToShortTon=2000,scaleHR=1000):
    #Get net demand
    netDemand = np.array(demand) - hourlyWindGen.sum(axis=1).values - hourlySolarGen.sum(axis=1).values
    #Setup fleet
    fleet = genFleet.copy()
    fleet = fleet.loc[(fleet['FuelType']!='Wind')&(fleet['FuelType']!='Solar')&(fleet['FuelType']!='Energy Storage')]
    fleet['CO2Ems(ton/MWh)'] = fleet['CO2EmRate(lb/MMBtu)']/scaleLbToShortTon*fleet['Heat Rate (Btu/kWh)']/scaleHR
    #Run dispatch to get emissions
    (annualCo2Ems,co2Price) = (co2Cap*10,0) #ton, $/ton
    while annualCo2Ems > co2Cap:
        #Update op cost & sort fleet
        fleet['OpCostWithCO2'] = fleet['OpCost($/MWh)']+fleet['CO2Ems(ton/MWh)']*co2Price
        fleet.sort_values('OpCostWithCO2',inplace=True)
        fleet['cumCap'] = fleet['Capacity (MW)'].cumsum()
        #Sum hourly emissions from dispatching
        annualCo2Ems = sum([getHourCo2Ems(hourNetDemand,fleet) for hourNetDemand in netDemand])
        co2Price = co2Price+5 if annualCo2Ems > co2Cap else co2Price
    print('Annual CO2 emissions (tons):'+str(round(annualCo2Ems)))
    return co2Price

#For given hourly net demand value, calculate total system CO2 ems using gen stack IN TONS.
def getHourCo2Ems(hourNetDemand,fleet):
    hourFleet = fleet.copy()
    hourFleet['dispatched'] = hourFleet['cumCap']<=hourNetDemand
    hourFleet.loc[hourFleet.loc[hourFleet['dispatched']==0].index[0],'dispatched'] = True
    gen = hourFleet.loc[hourFleet['dispatched']==True]
    gen,last = gen.iloc[:-1],gen.iloc[-1]
    return (gen['CO2Ems(ton/MWh)']*gen['Capacity (MW)']).sum()+(last['CO2Ems(ton/MWh)']*(last['cumCap']-hourNetDemand)).sum()
