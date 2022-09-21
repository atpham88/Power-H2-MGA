#Michael Craig
#Determine which coal plants should retire based on CF in PRIOR CE run. (May
#not retire after prior CE run to maintain planning margin.)

import pandas as pd
from CreateFleetForCELoop import getOnlineGenFleet

#Retire units based on CFs in prior CE run. Immediately after each CE run,
#also check for retirements but maintain ability for supply & demand balance
#so can pass generator fleet to operational model. Here, we retire those generators
#we would have retired if we did not maintain supply & demand balance capabilities. 
def retireUnitsCFPriorCE(genFleet,genFleetPriorCE,retirementCFCutoff,priorCapacExpModel,
            priorHoursCE,ptEligForRetireByCF,currYear):
    if currYear > 2050: currYear = 2050
    #Get which generators from last CE run are still online based on age of this year
    genFleetOnline = getOnlineGenFleet(genFleetPriorCE,currYear)

    #Update online fleet based on economic retirements in last CE run
    currentStatus = genFleet.loc[genFleet['GAMS Symbol'].isin(genFleetOnline['GAMS Symbol'])] 
    currentStatus = currentStatus.loc[currentStatus['Retired'] == False]
    genFleetOnline = genFleetOnline.loc[genFleetOnline['GAMS Symbol'].isin(currentStatus['GAMS Symbol'])]

    #Get total generation from prior CE run
    gen = getPriorGen(genFleetOnline,priorHoursCE,priorCapacExpModel)
    
    #Retire units based on prior CE results
    unitsRetireCF = selectRetiredUnitsByCE(retirementCFCutoff,gen,genFleetOnline,priorHoursCE,ptEligForRetireByCF)
    print('Num units & units w/ econ retires prior to CE in ' + str(currYear) + ':' + str(len(unitsRetireCF)) + '\n',unitsRetireCF)
    
    #Mark retired units
    genFleet.loc[genFleet['GAMS Symbol'].isin(unitsRetireCF),'YearRetiredByCE'] = currYear
    genFleet.loc[genFleet['GAMS Symbol'].isin(unitsRetireCF),'Retired'] = True
    return genFleet

#Get generation from prior CE run by plant
def getPriorGen(genFleet,hoursForCE,ceModel):
    gen = pd.DataFrame(columns=genFleet['GAMS Symbol'],index=hoursForCE.index)
    for rec in ceModel.out_db['vGen']: gen.loc[rec.key(1),rec.key(0)] = rec.level
    return gen
    
#Determines which units retire for economic reasons after CE run.
def selectRetiredUnitsByCE(retirementCFCutoff,gen,genFleet,hoursForCE,ptEligForRetireByCF):
    totalGen = gen.sum()
    capacs = pd.Series((genFleet['Capacity (MW)']*hoursForCE.shape[0]).values,index=genFleet['GAMS Symbol'])
    cfs = totalGen*1000/(capacs*len(hoursForCE))
    symbols = genFleet.loc[genFleet['PlantType'].isin(ptEligForRetireByCF)]['GAMS Symbol']
    cfsEligibleForRetirements = cfs[symbols]
    cfsSorted = cfsEligibleForRetirements.sort_values()
    cfsSorted = cfsSorted.loc[cfsSorted<retirementCFCutoff]
    return cfsSorted.index.values