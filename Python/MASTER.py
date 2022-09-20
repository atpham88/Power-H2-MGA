# Michael Craig

import sys, os, csv, operator, copy, time, random, warnings, numpy as np, datetime as dt, pandas as pd
from os import path
from netCDF4 import Dataset
from gams import *
from AuxFuncs import *
from GAMSAuxFuncs import *
from SetupGeneratorFleet import *
from RemoveHydroFromFleetAndDemand import removeHydroFromFleetAndDemand
from ImportERCOTDemand import importHourlyERCOTDemand
from UpdateFuelPriceFuncs import *
from DemandFuncs import *
from DemandFuncsCE import *
from IsolateDataInCEHours import isolateDataInCEHours
from SetInitCondsUC import *
from ImportNewTechs import getNewTechs
from RetireUnitsCFPriorCE import retireUnitsCFPriorCE
from CreateFleetForCELoop import *
from GetRenewableCFsMERRA import getREGenMERRA
from GetRenewableCFsNonMERRA import getREGenNonMERRA
from GetNewRenewableCFs import *
from AddWSSitesToNewTechs import addWSSitesToNewTechs
from ProcessCEResults import *
from ScaleRegResForAddedWind import scaleRegResForAddedWind
from CombinePlants import combineWindSolarStoPlants
from GAMSAddSetToDatabaseFuncs import *
from GAMSAddParamToDatabaseFuncs import *
from ConvertCO2CapToPrice import convertCo2CapToPrice
from SaveDispatchResults import saveDispatchResults, writeDispatchResults
from InitializeOnOffExistingGensCE import initializeOnOffExistingGens
from ReservesWWSIS import calcWWSISReserves
from GetIncResForAddedRE import getIncResForAddedRE
from SaveCEOperationalResults import saveCapacExpOperationalData
from ImportStorageParams import *
from WriteTimeDependentConstraints import writeTimeDependentConstraints
from WriteBuildVariable import writeBuildVariable
from CreateEmptyReserveDfs import createEmptyReserveDfs
from SetupTransmissionAndZones import setupTransmissionAndZones, defineTransmissionRegions
import pickle

# SET OPTIONS
warnings.filterwarnings("ignore")
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 10)

# SCALARS
mwToGW = 1000
lbToShortTon = 2000


# ###################################################################4############
# ##### UNIVERSAL PARAMETERS ####################################################
# ###############################################################################
def setKeyParameters(metYear, interconn, electrifiedDemand, buildLimitsCase, ceOps, numBlocks, daysPerBlock, ucOrED, maxCapPerTech):

    metYear = 2012 if electrifiedDemand else metYear                            # EFS data is for 2012; ensure met year is 2012

    # ### CO2 EMISSION CAPS AND DACS TREATMENT
    if interconn == 'ERCOT':
        co2Ems2020 = 130594820                                                  # TONS. Initial emission for ERCOT: 130594820.
    elif interconn == 'EI':
        co2Ems2020 = 1274060000


    # ### CE AND UCED/ED OPTIONS
    tzAnalysis = {'ERCOT': 'CST', 'EI': 'EST', 'WECC': 'PST'}[interconn]        # timezone for analysis
    fuelPrices = importFuelPrices('Reference case')                             # import fuel price time series

    # ### CE OPTIONS
    fullYearCE = True if (numBlocks == 1 and daysPerBlock > 300) else False     # whether running full year in CE

    # ### STORAGE OPTIONS
    stoMkts = 'energyAndRes'                                                    # energy,res,energyAndRes - whether storage participates in energy, reserve, or energy and reserve markets
    stoFTLabels = ['Energy Storage']
    stoPTLabels = ['Energy Storage', 'Hydrogen', 'Battery Storage', 'Flywheels', 'Batteries']   # potential plant type labels
    stoDuration = {'Energy Storage': 'st', 'Hydrogen': 'lt', 'Battery Storage': 'st', 'Flywheels': 'st', 'Batteries': 'st'}  # mapping plant types to short-term (st) or long-term (lt) storage
    initSOCFraction = {pt: {'st': .1, 'lt': .05}[dur] for pt, dur in stoDuration.items()}       # get initial SOC fraction per st or lt storage
    stoMinSOC = 0  # min SOC

    # ### GENERIC DEMAND FLEXIBILITY PARAMETERS
    demandShifter = 0                                           # Percentage of hourly demand that can be shifted
    demandShiftingBlock = 4                                     # moving shifting demand window (hours)

    if buildLimitsCase == 2:
        maxCapPerTech['Nuclear'] = 0
    elif buildLimitsCase == 3:
        maxCapPerTech['CCS'], maxCapPerTech['Nuclear'] = 1500, 9000
    elif buildLimitsCase == 4:
        maxCapPerTech['Hydrogen'] = 0
    elif buildLimitsCase == 5:
        maxCapPerTech['Transmission'] = 0

    # ### WARNINGS OR ERRORS
    if ceOps == 'UC': sys.exit('CEwithUC.gms needs to be updated for DACS operations - add DACS constraints and include gentechs set')
    if ucOrED != 'None': sys.exit('ED and UC.gms need to be checked for DACS constraints')

    return (fullYearCE, fuelPrices, co2Ems2020, stoMkts, stoFTLabels, stoPTLabels, initSOCFraction,
            tzAnalysis, stoMinSOC, demandShifter, demandShiftingBlock)


def importFuelPrices(fuelPriceScenario):
    fuelPrices = pd.read_csv(os.path.join('Data', 'Energy_Prices_Electric_Power.csv'), skiprows=4, index_col=0)
    fuelPrices = fuelPrices[[col for col in fuelPrices if fuelPriceScenario in col]]
    fuelPrices.columns = [col.split(':')[0] for col in fuelPrices.columns]
    return fuelPrices


# Define reserve parameters for UC & CE w/ UC constraints models
def defineReserveParameters(stoMkts, stoFTLabels):
    # Regulation eligibility
    regElig = ['Steam', 'Combined Cycle', 'Geothermal'] + (stoFTLabels if 'res' in stoMkts.lower() else [])
    contFlexInelig = ['Wind', 'Solar', 'DAC']  # fuel types that are ineligible to provide flex or cont reserves

    # Regulation provision cost as fraction of operating cost
    regCostFrac = 0                     # 0.1

    # Requirement parameters - based on WWSIS Phase 2
    regLoadFrac = .01                   # frac of hourly load in reg up & down
    contLoadFrac = .03                  # frac of hourly load in contingency
    regErrorPercentile = 40             # ptl of hourly W&S forecast errors for reg reserves; in WWSIS, 95th ptl of 10-m wind & 5-m solar forecast errors
    flexErrorPercentile = 70            # ptl of hourly W&S forecast errors used in flex reserves

    # Timeframes
    regReserveMinutes = 5               # reg res must be provided w/in 5 minutes
    flexReserveMinutes = 10             # spin reserves must be provided w/in 10 minutes
    contingencyReserveMinutes = 30      # contingency res must be provided w/in 30 minutes
    minutesPerHour = 60
    rampRateToRegReserveScalar = regReserveMinutes / minutesPerHour             # ramp rate in MW/hr
    rampRateToFlexReserveScalar = flexReserveMinutes / minutesPerHour           # ramp rate in MW/hr
    rampRateToContReserveScalar = contingencyReserveMinutes / minutesPerHour

    return (regLoadFrac, contLoadFrac, regErrorPercentile, flexErrorPercentile, regElig, contFlexInelig,
            regCostFrac, rampRateToRegReserveScalar, rampRateToFlexReserveScalar, rampRateToContReserveScalar)


# ###############################################################################
# ###############################################################################
# ###############################################################################

# ###############################################################################
# ##### MASTER FUNCTION #########################################################
# ###############################################################################
def masterFunction(rStage, objLimit, metYear, interconn, balAuths, electrifiedDemand, elecDemandScen, reSourceMERRA, fixDays,
                   buildLimitsCase, runOnSC, co2EmsCapInFinalYear, yearIncDACS, compressFleet, runCE, ceOps, numBlocks, daysPerBlock,
                   daysPerPeak, startYear, endYear, yearStepCE, greenField, includeRes, stoInCE, seasStoInCE, retireByAge,
                   planningReserveMargin, retirementCFCutoff, discountRate, ptEligRetCF, incITC, incNuc, runFirstYear, ucOrED,
                   useCO2Price, maxCapPerTech, reDownFactor, annualDemandGrowth, iteration, mgaWeight, newGenspD, iterationLast):
    # Import key parameters
    (fullYearCE, fuelPrices, co2Ems2020, stoMkts, stoFTLabels, stoPTLabels, initSOCFraction,
     tzAnalysis, stoMinSOC, demandShifter, demandShiftingBlock) = setKeyParameters(metYear, interconn, electrifiedDemand, buildLimitsCase, ceOps,
                                                                                   numBlocks, daysPerBlock, ucOrED, maxCapPerTech)

    (regLoadFrac, contLoadFrac, regErrorPercentile, flexErrorPercentile, regElig, contFlexInelig, regCostFrac,
     rrToRegTime, rrToFlexTime, rrToContTime) = defineReserveParameters(stoMkts, stoFTLabels)

    # Create results directory
    buildScen = {1: 'reference', 2: 'lNuclear', 3: 'lNuclearCCS', 4: 'lH2', 5: 'lTrans'}[buildLimitsCase]
    resultsDirAll = 'Results_' + interconn + '_' + buildScen + '_' + str(electrifiedDemand) + elecDemandScen

    if not os.path.exists(resultsDirAll): os.makedirs(resultsDirAll)

    # Setup initial fleet and demand
    (genFleet, demandProfile, transRegions, pRegionShapes,
     lineLimits, lineDists, lineCosts) = getInitialFleetDemandTransmission(startYear, fuelPrices, electrifiedDemand,
                                                                           elecDemandScen, compressFleet, resultsDirAll,
                                                                           regElig, regCostFrac, metYear, stoMinSOC, greenField,
                                                                           interconn, balAuths, contFlexInelig, stoFTLabels, stoPTLabels)

    # Run CE and/or ED/UCED
    for currYear in range(startYear, endYear, yearStepCE):
        # Set CO2 cap and demand for year
        currCo2Cap = co2Ems2020 + (co2EmsCapInFinalYear - co2Ems2020) / ((endYear - 1) - startYear) * (currYear - startYear)

        print('Entering year ', currYear, ' with CO2 cap (million tons):', round(currCo2Cap / 1e6))

        # Create results directory
        resultsDir = os.path.join(resultsDirAll, rStage, str(currYear) + 'CO2Cap' + str(int(co2EmsCapInFinalYear / 1e6)))
        if not os.path.exists(resultsDir): os.makedirs(resultsDir)

        # Scale up demand profile if needed
        demandProfile = getDemandForFutureYear(demandProfile, annualDemandGrowth, metYear, currYear,
                                               electrifiedDemand, transRegions, elecDemandScen)

        # Run CE
        if currYear > startYear and runCE:
            if rStage == 'CE':
                print('Starting CE')
            elif rStage == 'MGA':
                print('Starting MGA')
            # Initialize results & inputs
            if currYear == startYear + yearStepCE:
                priorCEModel, priorHoursCE, genFleetPriorCE = None, None, None,

            if iteration == 1:
                mgaWeight = 0

            (genFleet, genFleetPriorCE,
             priorCEModel, priorHoursCE,
             newGenspD, mgaWeight,
             maxZoneCap, iterationLast) = runCapacityExpansion(genFleet, demandProfile, startYear, currYear, planningReserveMargin,
                                                                discountRate, fuelPrices, currCo2Cap, numBlocks, daysPerBlock, daysPerPeak,
                                                                fullYearCE, retirementCFCutoff, retireByAge, tzAnalysis, resultsDir,
                                                                maxCapPerTech, regLoadFrac, contLoadFrac, regErrorPercentile, flexErrorPercentile,
                                                                rrToRegTime, rrToFlexTime, rrToContTime, regElig, regCostFrac, ptEligRetCF,
                                                                genFleetPriorCE, priorCEModel, priorHoursCE, incITC, metYear, stoInCE, seasStoInCE,
                                                                ceOps, stoMkts, initSOCFraction, includeRes, reDownFactor, incNuc, demandShifter,
                                                                demandShiftingBlock, runOnSC, interconn, yearIncDACS, transRegions, pRegionShapes,
                                                                lineLimits, lineDists, lineCosts, contFlexInelig, buildLimitsCase, co2EmsCapInFinalYear,
                                                                electrifiedDemand, elecDemandScen, reSourceMERRA, fixDays, rStage, objLimit,
                                                                iteration, mgaWeight, newGenspD, iterationLast)

        # Run dispatch
        if (ucOrED != 'None') and ((currYear == startYear and runFirstYear) or (currYear > startYear)):
            print('Starting dispatch')
            runDispatch(genFleet, objLimit, demandProfile, currYear, demandShifter, demandShiftingBlock, fuelPrices, currCo2Cap, useCO2Price,
                        tzAnalysis, resultsDir, stoMkts, metYear, regLoadFrac, contLoadFrac, interconn, regErrorPercentile, reSourceMERRA,
                        flexErrorPercentile, includeRes, rrToRegTime, rrToFlexTime, rrToContTime, regCostFrac,
                        ucOrED, initSOCFraction, includeRes)

    return resultsDir, mgaWeight, newGenspD, iterationLast

# ###############################################################################
# ###############################################################################
# ###############################################################################

# ###############################################################################
# ###### SET UP INITIAL FLEET AND DEMAND ########################################
# ###############################################################################
def getInitialFleetDemandTransmission(startYear, fuelPrices, electrifiedDemand, elecDemandScen, compressFleet,
                                      resultsDir, regElig, regCostFrac, metYear, stoMinSOC, greenField,
                                      interconn, balAuths, contFlexInelig, stoFTLabels, stoPTLabels, stoEff=0.81):
    # GENERATORS
    genFleet = setupGeneratorFleet(interconn, startYear, fuelPrices, stoEff, stoMinSOC, stoFTLabels)

    # DEFINE TRANSMISSION REGIONS
    transRegions = defineTransmissionRegions(interconn, balAuths)

    # DEMAND - TODO: if import non-EFS, need to map p-regions to demandInitialnd region(s), & reflect in defineTransmissionRegions
    demand = importHourlyEFSDemand(startYear, transRegions, elecDemandScen) if electrifiedDemand else importHourlyERCOTDemand(metYear)
    demand.to_csv(os.path.join(resultsDir, 'demandInitial.csv'))

    # TRANSMISSION
    genFleet, transRegions, limits, dists, costs, pRegionShapes = setupTransmissionAndZones(genFleet, transRegions, interconn, balAuths)
    for df, l in zip([limits, dists, costs], ['Limits', 'Dists', 'Costs']): df.to_csv(os.path.join(resultsDir, 'transmission' + l + 'Initial.csv'))

    # FINISH PROCESSING GENFLEET
    # Compress generators and add size dependent params (cost, reg offers, UC params)
    genFleet = compressAndAddSizeDependentParams(genFleet, compressFleet, regElig, contFlexInelig, regCostFrac, stoPTLabels)

    # If greenfield, elim existing generator fleet except tiny NG, wind, & solar plant (to avoid crash).
    if greenField: genFleet = stripDownGenFleet(genFleet, greenField)

    # PROCESS HYDROPOWER
    if not greenField: (genFleet, demand) = removeHydroFromFleetAndDemand(genFleet, demand)  # If running greenfield, skip step where get rid of hydro (since none in fleet).
    genFleet.to_csv(os.path.join(resultsDir, 'genFleetInitial.csv'))
    return (genFleet, demand, transRegions, pRegionShapes, limits, dists, costs)


# ###############################################################################
# ###############################################################################
# ###############################################################################

# ###############################################################################
# ###### RUN CAPACITY EXPANSION #################################################
# ###############################################################################
def runCapacityExpansion(genFleet, demand, startYear, currYear, planningReserveMargin, discountRate, fuelPrices, currCo2Cap, numBlocks,
                         daysPerBlock, daysPerPeak, fullYearCE, retirementCFCutoff, retireByAge, tzAnalysis, resultsDirOrig, maxCapPerTech,
                         regLoadFrac, contLoadFrac, regErrorPercentile, flexErrorPercentile, rrToRegTime, rrToFlexTime, rrToContTime,
                         regElig, regCostFrac, ptEligRetCF, genFleetPriorCE, priorCEModel, priorHoursCE, incITC, metYear, stoInCE, seasStoInCE,
                         ceOps, stoMkts, initSOCFraction, includeRes, reDownFactor, incNuc, demandShifter, demandShiftingBlock, runOnSC,
                         interconn, yearIncDACS, transRegions, pRegionShapes, lineLimits, lineDists, lineCosts, contFlexInelig,
                         buildLimitsCase, co2EmsCapInFinalYear, electrifiedDemand, elecDemandScen, reSourceMERRA, fixDays, rStage, objLimit,
                         iteration, mgaWeight, newGenspD, iterationLast):

    # Create results directory
    resultsDir = os.path.join(resultsDirOrig)

    if not os.path.exists(resultsDir): os.makedirs(resultsDir)

    if rStage == 'CE':
        print('Entering CE loop for year ' + str(currYear))
    elif rStage == 'MGA':
        print('Entering MGA loop for year ' + str(currYear))

    # Update new technology and fuel price data
    write2dListToCSV([[currCo2Cap]], os.path.join(resultsDir, 'co2CapCE' + str(currYear) + '.csv'))
    newTechsCE = getNewTechs(regElig, regCostFrac, currYear, incITC, stoInCE, seasStoInCE,
                             fuelPrices, yearIncDACS, incNuc, transRegions, contFlexInelig)
    genFleet = updateFuelPricesAndCosts(genFleet, currYear, fuelPrices, regCostFrac)

    # Retire units and create fleet for current CE loop
    if priorCEModel != None:  # if not in first CE loop
        genFleet = retireUnitsCFPriorCE(genFleet, genFleetPriorCE, retirementCFCutoff,
                                        priorCEModel, priorHoursCE, ptEligRetCF, currYear)
    genFleet, genFleetForCE = createFleetForCurrentCELoop(genFleet, currYear, retireByAge)
    genFleetForCE.to_csv(os.path.join(resultsDir, 'genFleetForCEPreRECombine' + str(currYear) + '.csv'))

    # Combine wind, solar, and storage plants by region
    genFleetForCE = combineWindSolarStoPlants(genFleet)
    genFleetForCE.to_csv(os.path.join(resultsDir, 'genFleetForCE' + str(currYear) + '.csv'))

    # Get renewable CFs from MERRA or non-MERRA data by plant and region and calculate net demand by region
    if reSourceMERRA:
        print('Loading RE data (MERRA)')
        windGen, solarGen, windGenRegion, solarGenRegion, latlonRegion = getREGenMERRA(genFleet, tzAnalysis, metYear, currYear, pRegionShapes)
    elif not reSourceMERRA:
        print('Loading RE data (NSRDB and Wind Toolkit)')
        windGen, solarGen, windGenRegion, solarGenRegion, latlonRegion = getREGenNonMERRA(genFleet, tzAnalysis, metYear, currYear, pRegionShapes)
    # windGen,solarGen,windGenRegion,solarGenRegion =getREGen(genFleet, tzAnalysis, metYear, currYear, interconn, pRegionShapes)
    netDemand = demand - windGenRegion - solarGenRegion

    # Get hours included in CE model (representative + special blocks)
    (hoursForCE, planningReserve, blockWeights, socScalars, peakDemandHour, blockNamesChronoList,
     lastRepBlockNames, specialBlocksPrior) = getHoursForCE(demand, netDemand, windGenRegion, solarGenRegion,
                                                            daysPerBlock, daysPerPeak, fullYearCE, currYear,
                                                            resultsDir, numBlocks, metYear, planningReserveMargin)

    # Get CFs for new wind and solar sites and add wind & solar sites to newTechs
    newCfs = getNewRenewableCFs(genFleet, tzAnalysis, metYear, currYear, reDownFactor, pRegionShapes, reSourceMERRA)
    # newCfs = getNewRenewableCFs(genFleet, tzAnalysis, metYear, currYear, reDownFactor, interconn, pRegionShapes)
    newTechsCE, newCfs = addWSSitesToNewTechs(newCfs, newTechsCE, pRegionShapes)

    # Add max capacity by zone for each fuel type in newTechCE:
    newTechsCE['Max Zonal Cap'] = newTechsCE['Capacity (MW)']
    if iteration == 1:
        newTechsCE['Variable Weight'] = 1
    elif iteration > 1:
        newTechsCE['Variable Weight'] = mgaWeight['Variable Weight']

    pt = ['CCS', 'Combined Cycle', 'Nuclear', 'Battery Storage', 'Hydrogen', 'Wind', 'Solar']
    for item in list(range(len(pt))):
        if pt[item] == 'Wind' or pt[item] == 'Solar':
            newTechsCE.loc[newTechsCE['PlantType'].str.contains(pt[item].lower()), 'Max Zonal Cap'] = maxCapPerTech[pt[item]]/newTechsCE['Capacity (MW)']
        elif pt[item] == 'Hydrogen' or pt[item] == 'Battery Storage':
            newTechsCE.loc[newTechsCE['PlantType'].str.contains(pt[item]), 'Max Zonal Cap'] = maxCapPerTech[pt[item]] / mwToGW
        else:
            newTechsCE.loc[newTechsCE['PlantType'].str.contains(pt[item]), 'Max Zonal Cap'] = maxCapPerTech[pt[item]]/newTechsCE['Capacity (MW)']

    mgaWeight = newTechsCE[['GAMS Symbol','Variable Weight']]
    maxZoneCap = newTechsCE[['GAMS Symbol','Max Zonal Cap']]

    # Initialize which generators are on or off at start of each block of hours (useful if CE has UC constraints)
    onOffInitialEachPeriod = initializeOnOffExistingGens(genFleetForCE, hoursForCE, netDemand)

    # Set reserves for existing and incremental reserves for new generators
    print('Calculating reserves')
    if includeRes:
        cont, regUp, flex, regDemand, regUpSolar, regUpWind, flexSolar, flexWind = calcWWSISReserves(windGenRegion, solarGenRegion, demand, regLoadFrac,
                                                                                                     contLoadFrac, regErrorPercentile, flexErrorPercentile)
        regUpInc, flexInc = getIncResForAddedRE(newCfs, regErrorPercentile, flexErrorPercentile)
    else:
        cont, regUp, flex, regDemand, regUpSolar, regUpWind, flexSolar, flexWind, regUpInc, flexInc = createEmptyReserveDfs(windGenRegion, newCfs)

    # Get timeseries hours for CE (demand, wind, solar, new wind, new solar, reserves) & save dfs
    (demandCE, windGenCE, solarGenCE, newCfsCE,
     contCE, regUpCE, flexCE, regUpIncCE, flexIncCE) = isolateDataInCEHours(hoursForCE, demand, windGenRegion,
                                                                            solarGenRegion, newCfs, cont, regUp,
                                                                            flex, regUpInc, flexInc)

    # Save CE inputs
    for df, n in zip([windGen, solarGen, windGenRegion, solarGenRegion, newCfs, demand, netDemand, cont, regUp,
                      flex, regUpInc, flexInc, regDemand, regUpSolar, regUpWind, flexSolar, flexWind],
                     ['windGen', 'solarGen', 'windGenRegion', 'solarGenRegion', 'windSolarNewCFs', 'demand', 'netDemand',
                      'contRes', 'regUpRes', 'flexRes', 'regUpInc', 'flexInc', 'regUpDemComp', 'regUpSolComp',
                      'regUpWinComp', 'flexSolComp', 'flexWinComp']):
        df.to_csv(os.path.join(resultsDir, n + 'FullYr' + str(currYear) + '.csv'))

    for df, n in zip([demandCE, windGenCE, solarGenCE, newCfsCE, newTechsCE, contCE, regUpCE, flexCE, regUpIncCE, flexIncCE],
                     ['demand', 'windGen', 'solarGen', 'windAndSolarNewCFs', 'newTechs', 'contRes', 'regUpRes', 'flexRes', 'regUpInc', 'flexInc']):
        df.to_csv(os.path.join(resultsDir, n + 'CE' + str(currYear) + '.csv'))

    hoursForCE.to_csv(os.path.join(resultsDir, 'hoursCEByBlock' + str(currYear) + '.csv'))
    write2dListToCSV([[planningReserve]], os.path.join(resultsDir, 'planningReserveCE' + str(currYear) + '.csv'))
    write2dListToCSV([[k, v] for k, v in socScalars.items()], os.path.join(resultsDir, 'socScalars' + str(currYear) + '.csv'))

    # ######### RUN CAPACITY EXPANSION
    # If at MGA stage, return objective function value from initial least cost solution then set upper bound
    if rStage == 'CE':
        print('Running CE for ' + str(currYear))
    elif rStage == 'MGA':
        print('Running MGA for ' + str(currYear))

    ws, db, gamsFileDir = createGAMSWorkspaceAndDatabase(runOnSC)
    writeTimeDependentConstraints(blockNamesChronoList, stoInCE, seasStoInCE, gamsFileDir, ceOps, lastRepBlockNames, specialBlocksPrior)
    writeBuildVariable(ceOps, gamsFileDir)
    genSet, hourSet, hourSymbols, zoneOrder, lineSet = edAndUCSharedFeatures(db, objLimit, genFleetForCE, hoursForCE, demandCE, contCE, regUpCE, flexCE,
                                                                             demandShifter, demandShiftingBlock, rrToRegTime, rrToFlexTime, rrToContTime, 0,
                                                                             solarGenCE, windGenCE, transRegions, lineLimits)  # 0 is for co2Price
    stoGenSet, stoGenSymbols = storageSetsParamsVariables(db, genFleetForCE, stoMkts)
    stoTechSet, stoTechSymbols = ceSharedFeatures(db, peakDemandHour, genFleetForCE, newTechsCE, planningReserve, discountRate, currCo2Cap,
                                                  hourSet, hourSymbols, newCfsCE, maxCapPerTech, regUpIncCE, flexIncCE, stoMkts,
                                                  lineDists, lineCosts, lineSet, zoneOrder, ceOps, interconn, buildLimitsCase)
    if ceOps == 'UC': ucFeatures(db, genFleetForCE, genSet),
    ceTimeDependentConstraints(db, hoursForCE, blockWeights, socScalars, ceOps, onOffInitialEachPeriod, genSet, genFleetForCE, stoGenSet,
                               stoGenSymbols, blockNamesChronoList, seasStoInCE, newTechsCE, stoTechSet, stoTechSymbols, initSOCFraction)
    if rStage == 'CE':
        capacExpModel, ms, ss = runGAMS('CEWith{o}.gms'.format(o=ceOps), ws, db)
    elif rStage == 'MGA':
        capacExpModel, ms, ss = runGAMS('MGAWith{o}.gms'.format(o=ceOps), ws, db)

    # ########## SAVE AND PROCESS CE RESULTS
    newGens, newStoECap, newStoPCap, newLines = saveCEBuilds(capacExpModel, iteration, rStage, resultsDir, currYear)

    # Recalculate MGA weight for next iteration and determine termination condition for MGA:
    newGenspDPrior = newGenspD
    newGenspD = pd.DataFrame.from_dict(newGens, orient='index')
    newGenspD = newGenspD.reset_index()
    newGenspD = newGenspD.rename(columns={'index': 'GAMS Symbol', 0: 'Cap Investments'})
    mgaWeight['Variable Weight'] = mgaWeight['Variable Weight'] + newGenspD['Cap Investments'] / maxZoneCap['Max Zonal Cap']

    if rStage == 'MGA':
        if iteration > 1:
            capVarChange = pd.DataFrame(np.zeros([len(newGenspD), 1]))
            for item in list(range(len(newGenspD))):
                if newGenspD['Cap Investments'][item] > 0:
                    capVarChange[0][item] = abs(newGenspD['Cap Investments'][item] - newGenspDPrior['Cap Investments'][item]) / newGenspDPrior['Cap Investments'][item]
                else:
                    capVarChange[0][item] = 0
                    mgaWeight['Variable Weight'][item] = 0

            capVarChange = capVarChange.rename(columns={0: 'Pct'})
            capVarChange = capVarChange.dropna()
            capVarChange = capVarChange.reset_index()
            if (capVarChange['Pct'] < 0.05).all():
                iterationLast = iteration

    if rStage == 'CE' or (rStage == 'MGA' and iteration == iterationLast):
        write2dListToCSV([['ms', 'ss'], [ms, ss]], os.path.join(resultsDir, 'msAndSsCE' + str(currYear) + '.csv'))
        saveCapacExpOperationalData(capacExpModel, genFleetForCE, newTechsCE, hoursForCE, transRegions, lineLimits, resultsDir, 'CE', currYear)
    print('Investments in ' + str(currYear) + ':\n', newGens, '\n', newStoECap, '\n', newStoPCap, '\n', newLines)
    genFleet = addNewGensToFleet(genFleet, newGens, newStoECap, newStoPCap, newTechsCE, currYear)
    lineLimits = addNewLineCapToLimits(lineLimits, newLines)
    genFleet.to_csv(os.path.join(resultsDir, 'genFleetAfterCE' + str(currYear) + '.csv'))
    lineLimits.to_csv(os.path.join(resultsDir, 'lineLimitsAfterCE' + str(currYear) + '.csv'))

    return (genFleet, genFleetForCE, capacExpModel, hoursForCE, newGenspD, mgaWeight, maxZoneCap, iterationLast)


# ###############################################################################
# ###############################################################################
# ###############################################################################

# ###############################################################################
# ###### RUN DISPATCH ###########################################################
# ###############################################################################
def runDispatch(genFleet, objLimit, hourlyDemand, currYear, demandShifter, demandShiftingBlock, runOnSC, fuelPrices, currCo2Cap, useCO2Price,
                tzAnalysis, resultsDir, stoMkts, metYear, regLoadFrac, contLoadFrac, interconn, regErrorPercentile, reSourceMERRA,
                flexErrorPercentile, rrToRegTime, rrToFlexTime, rrToContTime, regCostFrac, ucOrED, initSOCFraction, includeRes,
                firstDay=0, lastDay=364, daysOpt=364, daysLA=1):
    resultsDir = os.path.join(resultsDir, 'Dispatch')
    if not os.path.exists(resultsDir): os.makedirs(resultsDir)
    print('Entering dispatch for year ' + str(currYear))

    # Remove retired units from fleet
    genFleet = getOnlineGenFleet(genFleet, currYear)
    genFleet.to_csv(os.path.join(resultsDir, 'genFleetForDispatch' + str(currYear) + '.csv'))

    # Get renewable generation
    if reSourceMERRA:
        hourlyWindGen, hourlySolarGen = getREGenMERRA(genFleet, tzAnalysis, metYear, interconn)
    elif not reSourceMERRA:
        hourlyWindGen, hourlySolarGen = getREGenNonMERRA(genFleet, tzAnalysis, metYear, interconn)

    hourlyWindGen.to_csv(path.join(resultsDir, 'windGenDispatch' + str(currYear) + '.csv'))
    hourlySolarGen.to_csv(path.join(resultsDir, 'solarGenDispatch' + str(currYear) + '.csv'))
    write2dListToCSV([hourlyDemand], os.path.join(resultsDir, 'demandDispatch' + str(currYear) + '.csv'))

    # Get reserves
    if includeRes:
        hourlyReserves, resComps = calcWWSISReserves(hourlyWindGen, hourlySolarGen, hourlyDemand,
                                                     regLoadFrac, contLoadFrac, regErrorPercentile, flexErrorPercentile)
    else:
        hourlyReserves, resComps, regUpInc, flexInc = createEmptyReserveDfs(hourlyWindGen)

    hourlyReserves.to_csv(path.join(resultsDir, 'resDispatch' + str(currYear) + '.csv'))
    resComps.to_csv(path.join(resultsDir, 'resCompsDispatch' + str(currYear) + '.csv'))

    # Update fuel prices
    genFleet = updateFuelPricesAndCosts(genFleet, currYear, fuelPrices, regCostFrac)

    # Combine wind & solar generators
    genFleet = combineWindSolarStoPlants(genFleet)
    genFleet.to_csv(path.join(resultsDir, 'genFleetDispatch' + str(currYear) + '.csv'))

    # Set CO2 price
    co2Price = convertCo2CapToPrice(genFleet, hourlyWindGen, hourlySolarGen, hourlyDemand, currCo2Cap) if useCO2Price else 0
    print('CO2 price:', co2Price, '$/ton')
    write2dListToCSV([[co2Price]], path.join(resultsDir, 'co2PriceDispatch' + str(currYear) + '.csv'))

    # Setup result dataframes
    daysToRun = range(firstDay, lastDay, daysOpt)
    dispatchResults = dict()
    for k in ['vGen', 'vRegup', 'vFlex', 'vCont', 'vTurnon', 'vTurnoff', 'vOnoroff', 'vCharge', 'vStateofcharge']:
        dispatchResults[k] = pd.DataFrame(columns=genFleet['GAMS Symbol'], index=hourlyWindGen.index)
    sysResults = pd.DataFrame(columns=['vNse', 'vZ', 'mcGen', 'mcRegup', 'mcFlex', 'mcCont'], index=hourlyWindGen.index)
    msAndSs = pd.DataFrame(columns=['ms', 'ss'], index=daysToRun)

    # Run dispatch for each day of year
    for day in daysToRun:
        # Get time series for current days
        hours = list(range(day * 24, (day + daysOpt + daysLA) * 24))
        dayDtIdx = hourlyWindGen.index[hours]
        wind, solar = hourlyWindGen.loc[dayDtIdx].sum(axis=1).values, hourlySolarGen.loc[dayDtIdx].sum(axis=1).values
        demand = [hourlyDemand[i] for i in hours]
        reserves = hourlyReserves.loc[dayDtIdx]

        # Set initial conditions (all returned as pd Series w/ gen index)
        if day == firstDay:  # first day, therefore no initial conditions defined. MW energy values
            (onOffInitial, genAboveMinInitial, mdtCarriedInitial,
             socInitial) = setInitCondsFirstDay(genFleet, initSOCFraction)
        else:  # MW energy values
            (onOffInitial, genAboveMinInitial, mdtCarriedInitial,
             socInitial) = setInitConds(dayDtIdx, genFleet, dispatchResults)
        # ############# RUN DISPATCH
        print('Running ' + ucOrED + ' for ' + str(day))
        ws, db, gamsFileDir = createGAMSWorkspaceAndDatabase(runOnSC)
        genSet, hourSet, hourSymbols = edAndUCSharedFeatures(db, objLimit, genFleet, hours, demand, reserves, demandShifter, demandShiftingBlock,
                                                             rrToRegTime, rrToFlexTime, rrToContTime, 0, solar, wind)  # 0 is for co2Price

        stoGenSet, stoGenSymbols = storageSetsParamsVariables(db, genFleet, stoMkts)
        if ucOrED == 'UC':
            ucFeatures(db, genFleet, genSet)
            uc(db, stoGenSet, genSet, socInitial, onOffInitial, genAboveMinInitial, mdtCarriedInitial)
        else:
            ed(db, socInitial, stoGenSet)
        opsModel, ms, ss = runGAMS(ucOrED + '.gms', ws, db)

        # ########### SAVE RESULTS
        msAndSs.loc[day] = [ms, ss]
        dispatchResults, sysResults = saveDispatchResults(dispatchResults, sysResults, opsModel, hourlyWindGen.index, dayDtIdx)
        writeDispatchResults(dispatchResults, sysResults, msAndSs, resultsDir, currYear)


# ###############################################################################
# ###############################################################################
# ###############################################################################

# ###############################################################################
# ################## GAMS FUNCTIONS #############################################
# ###############################################################################
def createGAMSWorkspaceAndDatabase(runOnSC):
    # currDir = os.getcwd()
    if runOnSC:
        gamsFileDir = '/home/anph/projects/PH2/Model/GAMS'
        gamsSysDir = '/home/anph/gams_35_1'
    else:
        # gamsFileDir = 'C:\\Users\\mtcraig\\Desktop\\Research\\Models\\CEGit\\GAMS'
        # gamsSysDir = 'C:\\GAMS\\win64\\31.1'
        gamsFileDir = r"C:\Users\atpha\Documents\Postdocs\Projects\Power-H2_MGA\Model\GAMS"
        gamsSysDir = r"C:\GAMS\win64\30.2"
    ws = GamsWorkspace(working_directory=gamsFileDir, system_directory=gamsSysDir)
    db = ws.add_database()
    return ws, db, gamsFileDir


def runGAMS(gamsFilename, ws, db):
    t0 = time.time()
    model = ws.add_job_from_file(gamsFilename)
    opts = GamsOptions(ws)
    opts.defines['gdxincname'] = db.name
    model.run(opts, databases=db)
    ms, ss = model.out_db['pModelstat'].find_record().value, model.out_db['pSolvestat'].find_record().value
    if (int(ms) != 8 and int(ms) != 1) or int(ss) != 1: print('Modelstat & solvestat:', ms, ' & ', ss, ' (ms1 global opt, ms8 int soln, ss1 normal)')
    print('Time (mins) for GAMS run: ' + str(round((time.time() - t0) / 60)))
    return model, ms, ss


def edAndUCSharedFeatures(db, objLimit, genFleet, hours, demand, contRes, regUpRes, flexRes, demandShifter, demandShiftingBlock, rrToRegTime, rrToFlexTime,
                          rrToContTime, co2Price, hourlySolarGen, hourlyWindGen, transRegions, lineLimits, cnse=10000):
    # SETS
    genSet = addGeneratorSets(db, genFleet)
    hourSet, hourSymbols = addHourSet(db, hours)
    zoneSet, zoneSymbols, zoneOrder = addZoneSet(db, transRegions)
    lineSet, lineSymbols = addLineSet(db, lineLimits)

    # PARAMETERS
    # Demand and reserves
    addDemandParam(db, demand, hourSet, zoneSet, demandShifter, demandShiftingBlock, mwToGW)
    addReserveParameters(db, contRes, regUpRes, flexRes, rrToRegTime, rrToFlexTime, rrToContTime, hourSet, zoneSet, mwToGW)

    # CO2 cap or price
    addCo2Price(db, co2Price)

    # Least-cost solution limit
    addObjLimit(db, objLimit)

    # Generators
    addGenParams(db, genFleet, genSet, mwToGW, lbToShortTon, zoneOrder)
    addExistingRenewableMaxGenParams(db, hourSet, zoneSet, hourlySolarGen, hourlyWindGen, mwToGW)
    addSpinReserveEligibility(db, genFleet, genSet)
    addCostNonservedEnergy(db, cnse)

    # Transmission lines
    addLineParams(db, lineLimits, lineSet, zoneOrder, mwToGW)
    return genSet, hourSet, hourSymbols, zoneOrder, lineSet


def storageSetsParamsVariables(db, genFleet, stoMkts):
    (stoGenSet, stoGenSymbols) = addStoGenSets(db, genFleet)
    addStorageParams(db, genFleet, stoGenSet, stoGenSymbols, mwToGW, stoMkts)
    return stoGenSet, stoGenSymbols


def ed(db, socInitial, stoGenSet):
    addStorageInitSOC(db, socInitial, stoGenSet, mwToGW)


def ucFeatures(db, genFleet, genSet):
    addGenUCParams(db, genFleet, genSet, mwToGW)


def uc(db, stoGenSet, genSet, socInitial, onOffInitial, genAboveMinInitial, mdtCarriedInitial):
    addStorageInitSOC(db, socInitial, stoGenSet, mwToGW)
    addEguInitialConditions(db, genSet, onOffInitial, genAboveMinInitial, mdtCarriedInitial, mwToGW)


def ceSharedFeatures(db, peakDemandHour, genFleet, newTechs, planningReserve, discountRate,
                     co2Cap, hourSet, hourSymbols, newCfs, maxCapPerTech, regUpInc, flexInc, stoMkts,
                     lineDists, lineCosts, lineSet, zoneOrder, ceOps, interconn, buildLimitsCase):
    # Sets
    addPeakHourSubset(db, peakDemandHour)
    addStorageSubsets(db, genFleet)
    (techSet, renewTechSet, stoTechSet, stoTechSymbols, thermalSet, dacsSet, CCSSet) = addNewTechsSets(db, newTechs)

    # Long-term planning parameters
    addPlanningReserveParam(db, planningReserve, mwToGW)
    addDiscountRateParam(db, discountRate)
    addCO2Cap(db, co2Cap)

    # New tech parameters
    addGenParams(db, newTechs, techSet, mwToGW, lbToShortTon, zoneOrder, True)
    addTechCostParams(db, newTechs, techSet, stoTechSet, mwToGW)
    addRenewTechCFParams(db, renewTechSet, hourSet, newCfs)
    addMaxNewBuilds(db, newTechs, thermalSet, stoTechSet, dacsSet, CCSSet, maxCapPerTech, mwToGW, interconn)
    if ceOps == 'UC': addGenUCParams(db, newTechs, techSet, mwToGW, True)
    addResIncParams(db, regUpInc, flexInc, renewTechSet, hourSet)
    addSpinReserveEligibility(db, newTechs, techSet, True)
    addStorageParams(db, newTechs, stoTechSet, stoTechSymbols, mwToGW, stoMkts, True)
    addNewLineParams(db, lineDists, lineCosts, lineSet, maxCapPerTech, buildLimitsCase, zoneOrder, interconn)
    return stoTechSet, stoTechSymbols


def ceTimeDependentConstraints(db, hoursForCE, blockWeights, socScalars, ceOps, onOffInitialEachPeriod,
                               genSet, genFleet, stoGenSet, stoGenSymbols, blockNamesChronoList, seasStoInCE,
                               newTechs, stoTechSet, stoTechSymbols, initSOCFraction):
    addHourSubsets(db, hoursForCE)
    addSeasonDemandWeights(db, blockWeights)
    addBlockSOCScalars(db, socScalars)
    if ceOps == 'UC': addInitialOnOffForEachBlock(db, onOffInitialEachPeriod, genSet)
    addStoInitSOCCE(db, genFleet, stoGenSet, stoGenSymbols, mwToGW, blockNamesChronoList, seasStoInCE, initSOCFraction)
    addStoInitSOCCE(db, newTechs, stoTechSet, stoTechSymbols, mwToGW, blockNamesChronoList, seasStoInCE, initSOCFraction, True)


################################################################################
################################################################################
################################################################################
################################################################################


