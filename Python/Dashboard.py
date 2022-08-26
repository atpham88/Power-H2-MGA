# Updated 08/18/2022 by An P.

import pandas as pd

from MASTER import *

def main():
    runningStage = ['CE', 'MGA']

    # ### STUDY AREA AND METEOROLOGICAL-DEPENDENT DATA
    metYear = 2012                                      # year of meteorological data used for demand and renewables
    interconn = 'EI'                                 # which interconnection to run - ERCOT, WECC, EI
    balAuths = 'full'                                   # full: run for all BAs in interconn. TODO: add selection of a subset of BAs.
    electrifiedDemand = True                            # whether to import electrified demand futures from NREL's EFS
    elecDemandScen = 'REFERENCE'                        # 'REFERENCE','HIGH','MEDIUM' (ref is lower than med)
    reSourceMERRA = True                                # == True: use MERRA as renewable data source, == False: use NSDB and Wind Toolkit
    fixDays = True

    annualDemandGrowth = 0                              # fraction demand growth per year - ignored if use EFS data (electrifieDemand=True)
    reDownFactor = 4                                    # downscaling factor for W&S new CFs; 1 means full resolution, 2 means half resolution, 3 is 1/3 resolution, etc

    # ### BUILD SCENARIO
    buildLimitsCase = 1                                 # 1 = reference case,
                                                        # 2 = limited nuclear,
                                                        # 3 = limited CCS and nuclear,
                                                        # 4 = limited hydrogen storage,
                                                        # 5 = limited transmission

    # ### RUNNING ON SC OR LOCAL
    runOnSC = False                                     # whether running on supercomputer
    if runOnSC == False:
        projectPath = "C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\Power-H2_MGA\\Model\\Python\\"
    else:
        projectPath = "/home/anph/projects/Power-H2_MGA/Model/Python/"

    co2EmsCapInFinalYear = 0                            # cap on co2 emissions in final year of CE
    yearIncDACS = 2060                                  # year to include DACS - set beyond end period if don't want DACS

    # ### CE AND UCED/ED OPTIONS
    compressFleet = True

    # ### CE OPTIONS
    runCE, ceOps = True, 'ED'                           # ops are 'ED' or 'UC' (econ disp or unit comm constraints)
    numBlocks, daysPerBlock, daysPerPeak = 4, 2, 3      # num rep time blocks, days per rep block, and days per peak block in CE
    startYear, endYear, yearStepCE = 2020, 2051, 30

    greenField = False                                  # whether to run greenField (set to True) or brownfield (False)
    includeRes = False                                  # whether to include reserves in CE & dispatch models (if False, multiplies reserve timeseries by 0)
    stoInCE, seasStoInCE = True, True                   # whether to allow new storage, new seasonal storage in CE model
    retireByAge = True                                  # whether to retire by age or not
    planningReserveMargin = 0.1375                      # fraction of peak demand; ERCOT targeted planning margin
    retirementCFCutoff = .3                             # retire units w/ CF lower than given value
    discountRate = 0.07                                 # fraction
    ptEligRetCF = ['Coal Steam']                        # which plant types retire based on capacity factor (economics)
    incITC, incNuc = False, True                        # include Investment Tax Credit or not; include nuclear as new investment option or not

    # ### ED/UCED OPTIONS
    runFirstYear = False                                # whether to run first year of dispatch
    ucOrED = 'None'                                     # STRING that is either: ED, UC, None
    useCO2Price = False                                 # whether to calc & inc CO2 price in operations run

    # ### MGA OPTIONS:
    maxIter = 100                                       # Maximum number of iterations

    # ### LIMITS ON TECHNOLOGY DEPLOYMENT
    maxCapPerTech = {'Wind': 2000 * reDownFactor, 'Solar': 17000 * reDownFactor, 'Thermal': 999999, 'Combined Cycle': 999999,
                     'Storage': 999999, 'Dac': -9999999, 'CCS': 999999, 'Nuclear': 999999, 'Battery Storage': 999999,
                     'Hydrogen': 999999, 'Transmission': 1000000000}  # max added MW per CE run (W&S by cell)

    for item in runningStage:
        rStage = item
        mgaWeight, iteration, newGenspD, iterationLast = 0, 1, 0, 0
        if rStage == 'CE':
            objLimit = 0
            (resultsCE, mgaWeight,
             newGenspD, iterationLast) = masterFunction(rStage, objLimit, metYear, interconn, balAuths, electrifiedDemand, elecDemandScen, reSourceMERRA, fixDays,
                                                        buildLimitsCase, runOnSC, co2EmsCapInFinalYear, yearIncDACS, compressFleet, runCE, ceOps, numBlocks, daysPerBlock,
                                                        daysPerPeak, startYear, endYear, yearStepCE, greenField, includeRes, stoInCE, seasStoInCE, retireByAge,
                                                        planningReserveMargin, retirementCFCutoff, discountRate, ptEligRetCF, incITC, incNuc, runFirstYear, ucOrED,
                                                        useCO2Price, maxCapPerTech, reDownFactor, annualDemandGrowth, iteration, mgaWeight, newGenspD, iterationLast)
        elif rStage == 'MGA':
            fval = pd.read_csv(projectPath + resultsCE + "\\vZannualCE" + str(endYear-1) + ".csv", header=None)
            objLimit = fval.iloc[0,0]*1.1
            while iteration <= maxIter:
                (resultsMGA, mgaWeight,
                 newGenspD, iterationLast) = masterFunction(rStage, objLimit, metYear, interconn, balAuths, electrifiedDemand, elecDemandScen, reSourceMERRA, fixDays,
                                                            buildLimitsCase, runOnSC, co2EmsCapInFinalYear, yearIncDACS, compressFleet, runCE, ceOps, numBlocks, daysPerBlock,
                                                            daysPerPeak, startYear, endYear, yearStepCE, greenField, includeRes, stoInCE, seasStoInCE, retireByAge,
                                                            planningReserveMargin, retirementCFCutoff, discountRate, ptEligRetCF, incITC, incNuc, runFirstYear, ucOrED,
                                                            useCO2Price, maxCapPerTech, reDownFactor, annualDemandGrowth, iteration, mgaWeight, newGenspD, iterationLast)
                if iteration == iterationLast:
                    break
                else:
                    iteration +=1

main()
