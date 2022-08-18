# Michael Craig
# October 4, 2016
# Functions that process demand data for CE model - select which days are
# included in CE, calculate blockal weights, get peak demand hour, and calculate
# planning reserve margin.

import copy, os, pandas as pd, numpy as np
from AuxFuncs import *


########### SELECT WEEKS FOR EXPANSION #########################################
def getHoursForCE(demand, netDemand, windGen, solarGen, daysPerRepBlock,
                  daysPerPeak, fullYearCE, currYear, resultsDir, numBlocks, metYear, planningReserveMargin):
    # Create dfs
    if currYear > 2050: currYear = 2050
    dfTotal = pd.DataFrame(demand.sum(axis=1), columns=['demand(MW)'])
    dfNet = pd.DataFrame(netDemand.sum(axis=1), columns=['netDemand(MW)'])
    prm = max(dfTotal['demand(MW)']) * (1 + planningReserveMargin)
    # Create dictionary for representative and all demand per block
    specialBlocks = dict()
    if not fullYearCE:
        # Get hours for peak net demand day
        dfNoSpecial, maxNet = getPeakDayHours(dfNet, daysPerPeak)
        specialBlocks['peaknet'] = maxNet
        # Get hours for day w/ max ramp up or down
        dfNoSpecial, maxRamp = getMaxRampDayHours(dfNet, daysPerPeak, dfNoSpecial)
        specialBlocks['peaknetramp'] = maxRamp
        # Get hours for peak demand day
        dfNoSpecial, maxTotal = getPeakDayHours(dfTotal, daysPerPeak, dfNoSpecial)
        specialBlocks['peaktotal'] = maxTotal
    else:
        dfNoSpecial = pd.concat([dfNet, dfTotal], axis=1)
    # Get representative hours for each block and weighting factors
    blockRepNetDemand, blockAllNetDemand = getRepBlockHoursByNLDC(dfNet, dfNoSpecial, daysPerRepBlock, numBlocks)
    blockWeights, weightsList = calculateBlockWeights(dfTotal, blockRepNetDemand, blockAllNetDemand)
    write2dListToCSV(weightsList, os.path.join(resultsDir, 'blockWeightsCE' + str(currYear) + '.csv'))
    # Get all hours by going from dfs to 1-8760 values
    if len(blockRepNetDemand) == 1:  # if running full year, add demand here
        blockRepNetDemand[0] = dfNoSpecial.loc[blockRepNetDemand[0].index]
    (allBlockHours, peakDemandHour, blockWeights, socScalars, blockNamesChronoList, lastRepBlockNames,
     specialBlocksPrior) = getHours(specialBlocks, blockRepNetDemand, blockWeights, daysPerRepBlock)
    return (allBlockHours['block'], prm, blockWeights, socScalars, peakDemandHour, blockNamesChronoList, lastRepBlockNames, specialBlocksPrior)


##### SELECT CE HOURS FOR DAY WITH PEAK DEMAND
def getPeakDayHours(df, daysPerPeak, dfNoSpecial=None):
    days = list()
    if dfNoSpecial is not None: df = df[df.index.isin(dfNoSpecial.index)].dropna()
    # Day w/ peak demand or net demand
    dfMax = df.loc[df.idxmax()].index
    # Find extra days on either side based on daysPerPeak
    extraDays = daysPerPeak - 1
    if daysPerPeak % 2 == 0:
        preDays, postDays = extraDays // 2 + 1, extraDays // 2
    else:
        preDays, postDays = extraDays // 2, extraDays // 2
    # Get day indices for extra days on either side
    preMax, postMax = (dfMax - pd.Timedelta(days=preDays)), (dfMax + pd.Timedelta(days=postDays))
    for d in [preMax, dfMax, postMax]:
        days.append(df[(df.index.month == d.month[0]) & (df.index.day == d.day[0])])
    peakDays = pd.concat(days)
    peakDays = peakDays[~peakDays.index.duplicated(keep='first')]
    if dfNoSpecial is None:
        dfNoSpecial = df[~df.isin(peakDays)].dropna()
    else:
        dfNoSpecial = dfNoSpecial[~dfNoSpecial.index.isin(peakDays.index)].dropna()
    return dfNoSpecial, peakDays


##### SELECT CE HOURS FOR DAY WITH MAX RAMP
# Take day w/ max ramp up
def getMaxRampDayHours(df, daysPerPeak, dfNoSpecial):
    ramp = df.shift() - df
    ramp = ramp.loc[dfNoSpecial.index]
    dfMax = ramp.loc[ramp.idxmax()].index
    # Find extra days on either side based on daysPerPeak
    extraDays = daysPerPeak - 1
    if daysPerPeak % 2 == 0:
        preDays, postDays = extraDays // 2 + 1, extraDays // 2
    else:
        preDays, postDays = extraDays // 2, extraDays // 2
    # Get day indices for extra days on either side
    days = list()
    preMax, postMax = (dfMax - pd.Timedelta(days=preDays)), (dfMax + pd.Timedelta(days=postDays))
    for d in [preMax, dfMax, postMax]:
        days.append(df[(df.index.month == d.month[0]) & (df.index.day == d.day[0])])
    peakDays = pd.concat(days)
    peakDays = peakDays[~peakDays.index.duplicated(keep='first')]
    dfNoSpecial = dfNoSpecial[~dfNoSpecial.isin(peakDays)].dropna()
    return dfNoSpecial, peakDays


##### SELECT CE HOURS FOR REPRESENTATIVE DAYS PER block
# Inputs: net demand (1d list), num representative days per block to select,
# set of hours already incluced as special days in CE (1d list, 1-8760 basis)
# Outputs: rep hours for each block (1d list no head, 1-8760 basis), dictionaries mapping
# blocks to representative and regular hours
def getRepBlockHoursByNLDC(df, dfNoSpecial, daysSampledPerBlock, numBlocks, hoursPerDay=24):
    hoursPerBlock = df.shape[0] / numBlocks
    blockRepNetDemand, blockAllNetDemand = dict(), dict()
    for nB in range(numBlocks):
        blockHours = df.iloc[int((nB * hoursPerBlock) // hoursPerDay) * hoursPerDay:int(((nB + 1) * hoursPerBlock) // hoursPerDay) * hoursPerDay]
        blockHours = blockHours[blockHours.isin(dfNoSpecial)].dropna()
        lowestRmse = blockHours.values.sum() ** 2
        for idx in range(0, blockHours.shape[0], hoursPerDay):
            sample = blockHours.iloc[idx: idx + hoursPerDay * daysSampledPerBlock]
            if sample.shape[0] == hoursPerDay * daysSampledPerBlock:
                # Want to avoid 1 day on either side of a special day
                hourDiff = sample.index[-1] - sample.index[0]
                hourDiff = abs(hourDiff.seconds // 3600 + hourDiff.days * 24) + 1
                if hourDiff == hoursPerDay * daysSampledPerBlock:
                    sampleFullBlock = pd.concat([sample] * (blockHours.shape[0] // (hoursPerDay * daysSampledPerBlock)))
                    blockHoursTruncated = blockHours.iloc[:sampleFullBlock.shape[0]]
                    rmse = getRMSE(sampleFullBlock.values, blockHoursTruncated.values)
                    if rmse < lowestRmse:
                        lowestRmse, lowestSample = rmse, sample.copy(deep=True)
        blockRepNetDemand[nB], blockAllNetDemand[nB] = lowestSample, blockHours
    return blockRepNetDemand, blockAllNetDemand


# Calculate RMSE b/wn 2 sets of data
def getRMSE(sampleData, originalData):
    sampleNLDC = np.sort(sampleData.flatten())
    originalNLDC = np.sort(originalData.flatten())
    return np.sqrt(np.mean((sampleNLDC - originalNLDC) ** 2))


# Convert dfs to hours 1-8760
def getHours(specialBlocks, blockRepNetDemand, blockWeights, daysPerRepBlock):
    # Sort and rename blocks
    allBlockHours, blockNames, blockWeightsAll, firstHours, blocks = sortAndRenameBlocks(specialBlocks, blockRepNetDemand, blockWeights)

    # Get SOC scalars between blocks for long-duration storage
    socScalarsAll, lastRepBlockNames, specialBlocksPrior = setSOCScalars(specialBlocks, firstHours, daysPerRepBlock)
    # hoursForCE,allHours,peakDemandHour = getHoursInBlocks(allPeriods,dates,blocks)

    # Assign block names as column in hours DF
    allBlockHours['block'] = ''
    for b in blocks: allBlockHours.loc[blocks[b].index, 'block'] = b
    # Get hour with peak demand
    peakDemandHour = allBlockHours['demand(MW)'].idxmax()
    return allBlockHours, peakDemandHour, blockWeightsAll, socScalarsAll, blockNames, lastRepBlockNames, specialBlocksPrior


def sortAndRenameBlocks(specialBlocks, blockRepNetDemand, blockWeights):
    blockWeightsAll = dict()
    # Sort all blocks in chronological order and rename accordingly
    allBlocks = specialBlocks.copy()
    allBlocks.update(blockRepNetDemand)
    firstHours = list()
    for b in allBlocks: firstHours.append(pd.Series([b], index=[allBlocks[b].index[0]]))
    firstHours = pd.concat(firstHours)
    firstHours = firstHours.sort_index()
    while firstHours.iloc[0] in specialBlocks:
        firstHours1 = firstHours.iloc[1:]
        firstHours2 = firstHours.iloc[0:1]
        firstHours = pd.concat([firstHours1, firstHours2])
    # firstHours df has 1 row for first hour of each block, sorted chronologically, w/
    # column giving block name
    blocks, blockNames, allPeriods, nameCtr = dict(), list(), list(), 0
    for i in range(firstHours.shape[0]):
        # Set block weights and order names and hours chronologically
        origName = firstHours.iloc[i]
        if origName in specialBlocks:
            name = origName + str(nameCtr)
            blockWeightsAll[name] = 1  # special days have weight=1, as not rep'ing longer period
        else:
            name = nameCtr
            blockWeightsAll[name] = blockWeights[origName]
        blockNames.append(name)
        blocks[name] = allBlocks[origName]
        nameCtr += 1
        allPeriods.append(blocks[name])
    return pd.concat(allPeriods), blockNames, blockWeightsAll, firstHours, blocks


# SOC scalar will scale SOC for seasonal storage b/wn blocks. Only want to scale
# changes in SOC during representative blocks, since scale costs for entire season.
# SOC scalar = (# hours since last REP block / # hours in last REP block).
# Apply this SOC scalar to get initial SOC for all blocks, but if have a special
# block halfway between 2 rep blocks, SOC scalar for special block will be
# 1/2 that for rep block.
# WARNING: This assumes a rep block is the first block!
def setSOCScalars(specialBlocks, firstHours, daysPerRepBlock):
    socScalarsAll, lastRepBlockNames, nameCtr, specialBlocksPrior, specialBlocksPriorList = dict(), dict(), 0, dict(), list()
    for i in range(firstHours.shape[0]):
        origName = firstHours.iloc[i]
        name = origName + str(nameCtr) if origName in specialBlocks else nameCtr
        if i > 0:
            hoursBeforeBlock = firstHours.index[i] - (lastRepBlockFirstHour + pd.Timedelta(hours=daysPerRepBlock * 24))
            socScalarsAll[name] = (hoursBeforeBlock / pd.Timedelta(hours=1)) / (daysPerRepBlock * 24)
            lastRepBlockNames[name] = lastRepBlockName
        specialBlocksPrior[name] = copy.copy(specialBlocksPriorList)
        if origName not in specialBlocks:
            lastRepBlockFirstHour, lastRepBlockName = firstHours.index[i], str(name)
            specialBlocksPriorList = list()
        else:
            specialBlocksPriorList.append(name)
        nameCtr += 1
    return socScalarsAll, lastRepBlockNames, specialBlocksPrior


# #Now sort all periods chronologically, get corresponding hour numbers, and save with new names
# def getHoursInBlocks(allPeriods,dates,blocks):
#     df = allPeriods.sort_index()
#     hourNums = pd.DataFrame({'num':list(range(1,len(dates)+1))},index=dates)
#     hourNums = hourNums.loc[df.index]
#     hoursForCE = hourNums['num'].tolist()
#     peakDemandHour = hourNums.loc[df['demand(MW)'].idxmax()].values[0]
#     allHours = dict()
#     for b in blocks:
#         hours = hourNums.loc[blocks[b].index]
#         allHours[b] = hours['num'].tolist()
#     return hoursForCE,allHours,peakDemandHour

########### CALCULATE blockAL WEIGHTS TO SCALE REP. DEMAND TO block VALUE ####
# Inputs: hourly demand in curr CE year (1d list w/out headers), 1d list of
# representative hours per block (1-8760 basis), 1d list of regular (i.e. non-rep)
# hours per block (1-8760 basis)
# Outputs: map of block to weight to scale rep demand to full block demand (scalar)
def calculateBlockWeights(dfTotal, blockRepNetDemand, blockAllNetDemand):
    blockDemandWeights, weightsList = dict(), [['block', 'blockWeight']]
    for block in blockRepNetDemand:
        repDemand = dfTotal.loc[blockRepNetDemand[block].index].sum().values[0]
        blockDemand = dfTotal.loc[blockAllNetDemand[block].index].sum().values[0]
        blockDemandWeights[block] = blockDemand / repDemand
        weightsList.append([block, blockDemandWeights[block]])
    return blockDemandWeights, weightsList

# def setSOCScalars(specialBlocks,firstHours,daysPerRepBlock):
#     socScalarsAll,lastRepBlockNames,nameCtr,specialBlocksPrior,specialBlocksPriorList = dict(),dict(),0,dict(),list()
#     for i in range(firstHours.shape[0]):
#         origName = firstHours.iloc[i]
#         name = origName+str(nameCtr) if origName in specialBlocks else nameCtr
#         if i>0:
#             hoursBeforeBlock = firstHours.index[i] - (lastRepBlockFirstHour + pd.Timedelta(hours=daysPerRepBlock*24))
#             socScalarsAll[name] = (hoursBeforeBlock/pd.Timedelta(hours=1))/(daysPerRepBlock*24)
#             lastRepBlockNames[name] = lastRepBlockName
#         if origName not in specialBlocks:
#             lastRepBlockFirstHour,lastRepBlockName = firstHours.index[i],str(name)
#             specialBlocksPrior[name] = specialBlocksPriorList
#             specialBlocksPriorList = list()
#         else:
#             specialBlocksPrior[name] = list()
#             specialBlocksPriorList.append(name)
#         nameCtr += 1
#     print(specialBlocksPrior)
#     print(firstHours)
#     aa
#     return socScalarsAll,lastRepBlockNames,specialBlocksPrior

