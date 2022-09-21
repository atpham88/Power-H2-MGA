#Michael Craig
#Combine all wind and solar units in fleet together (separately for
#each plant type), then remove all but combined unit from fleet. 

#Inputs: gen fleet (2d list)
def combineWindSolarStoPlants(genFleet):
    for r in genFleet['region'].unique():
        genFleet = combinePlantsByRegion(genFleet,'FuelType','Wind',r)
        genFleet = combinePlantsByRegion(genFleet,'FuelType','Solar',r)
        genFleet = combinePlantsByRegion(genFleet,'PlantType','Battery Storage',r,True)
        genFleet = combinePlantsByRegion(genFleet,'PlantType','Hydrogen',r,True)
    return genFleet

#Adds new combined unit, then removes other units
#Inputs: gen fleet (2d list), fuel type to combine, plant type to combine
def combinePlantsByRegion(fleet,paramCombinedOn,fuelType,r,storage=False):
    gens = fleet.loc[(fleet[paramCombinedOn]==fuelType) & (fleet['region']==r)]
    if gens.shape[0] > 0:
        newRow = gens.iloc[-1].copy()
        newRow['Capacity (MW)'] = gens['Capacity (MW)'].sum()
        newRow['RampRate(MW/hr)'] = gens['RampRate(MW/hr)'].sum()
        if storage:
            newRow['Maximum Charge Rate (MW)'] = gens['Maximum Charge Rate (MW)'].sum()
            newRow['Nameplate Energy Capacity (MWh)'] = gens['Nameplate Energy Capacity (MWh)'].sum()
        newRow['Unit ID'] += 'COMBINED'
        fleet = fleet.drop(index=gens.index)
        fleet = fleet.append(newRow)
    return fleet
