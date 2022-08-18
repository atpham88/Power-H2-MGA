#Michael Craig
#December 16, 2016

#Calculates spinning reserve requirements per WWSIS 
#Regulation: geometric sum (square root of sum of squared values) of 
#1% load, 95th percentile of 10-min forecast erros for wind and solar.
#Contingency: 3% load
#Flexibility: geometric sum of 70th percentile of 1-hour forecast errors for wind and solar

import csv, os, datetime, copy, operator
import pandas as pd
from AuxFuncs import *
import numpy as np

########## CALCULATE WWSIS RESERVES ############################################
#Loads raw data, gets gen errors, and returns reserve 
#requirements. Based on WWSIS Phase 2 requirements.
#Outputs: 1d list (1x8760) of hourly contingency, regulation up and down, and flexibility
#reserve requirements; 2d list of all res and res components w/ labels
def calcWWSISReserves(windGenRegion,solarGenRegion,demandRegion,regLoadFrac,contLoadFrac,regErrorPercentile,flexErrorPercentile):
    #Set contingency reserves as a fraction of hourly demand
    cont = contLoadFrac * demandRegion
    #Set regulation & flexibility reserves based on demand, wind & solar
    regUp,flex = pd.DataFrame(index=cont.index),pd.DataFrame(index=cont.index)
    regDemand,regUpSolar,regUpWind,flexSolar,flexWind = flex.copy(),flex.copy(),flex.copy(),flex.copy(),flex.copy()
    for region in demandRegion.columns:
        demand,wind,solar = demandRegion[region],windGenRegion[region],solarGenRegion[region]
        (regUpRegion,regDownRegion,regDemRegion,regUpWindRegion,regDownWindRegion,regUpSolarRegion,
            regDownSolarRegion) = setRegReserves(regErrorPercentile,regLoadFrac,wind,solar,demand)
        flexResRegion,flexWindRegion,flexSolarRegion = setFlexReserves(flexErrorPercentile,wind,solar)
        regUp[region],flex[region] = regUpRegion,flexResRegion
        regDemand[region],regUpSolar[region],regUpWind[region],flexSolar[region],flexWind[region] = regDemRegion,regUpSolarRegion,regUpWindRegion,flexSolarRegion,flexWindRegion
        #Visualization  
        # plotGenDemandAndRes(demand,windGenRegion,solarGenRegion,regUpHourly,flexResHourly,contResHourly)
        # plotWindAndSolarRes(regUpWind,regUpSolar,windGenRegion,solarGenRegion,'RegUp')
        # plotWindAndSolarRes(regDownWind,regDownSolar,windGenRegion,solarGenRegion,'RegDown')
        # plotWindAndSolarRes(flexWind,flexSolar,windGenRegion,solarGenRegion,'Flex')        
    return cont,regUp,flex,regDemand,regUpSolar,regUpWind,flexSolar,flexWind
################################################################################

########## SET RESERVE REQUIREMENTS ############################################
#All setReserve funcs output 1d list (1x8760) w/ hourly reserve requirement in MW
#Set contingency reserves as fraction of hourly demand
def setContReserves(contLoadFrac,demand):
    return [val*contLoadFrac for val in demand]

#Set reg reserve requirement as % of hourly load plus percentile of subhourly wind and solar gen (ideally)
def setRegReserves(regErrorPercentile,regLoadFrac,windGen,solarGen,demand):
    regDemand = regLoadFrac*demand
    regUpWind,regDownWind = calcWindReserves(windGen,regErrorPercentile)
    regUpSolar,regDownSolar = calcSolarReserves(solarGen,regErrorPercentile)
    regUpTotal = [(regDemand[idx]**2 + regUpWind[idx]**2 + 
                    regUpSolar[idx]**2)**.5 for idx in range(len(regDemand))]
    regDownTotal = [(regDemand[idx]**2 + regDownWind[idx]**2 + 
                    regDownSolar[idx]**2)**.5 for idx in range(len(regDemand))]
    return regUpTotal,regDownTotal,regDemand,regUpWind,regDownWind,regUpSolar,regDownSolar

#Set flex reserve requirement as percentile of hourly wind and solar gen
def setFlexReserves(flexErrorPercentile,windGenHourlyTotal,solarGenHourlyTotal):
    flexUpWind,flexDownWind = calcWindReserves(windGenHourlyTotal,flexErrorPercentile)
    flexUpSolar,flexDownSolar = calcSolarReserves(solarGenHourlyTotal,flexErrorPercentile)
    flexUpTotal = [(flexUpWind[idx]**2 + flexUpSolar[idx]**2)**.5 for idx in range(len(flexUpWind))]
    return flexUpTotal,flexUpWind,flexUpSolar
################################################################################

########## CALCULATE WIND RESERVES #############################################
#Calculate wind reserves by taking error versus power, divide power into ten groups,
#calculate percentile for errors, then interpolate between averages to get error
#value for each power value. Errors are positive for overforecast (think will
#be 20, but is actually 10) and negative if underforecast (think will be 10, but is actually 20).
#Inputs: 2d list of wind gen (col 1 = datetime, col 2 = total gen), scalar 
#for percentile error (%)
#Outputs: 1d lists of up and down res at hourly timescale
def calcWindReserves(windGen,errorPercentile):
    if windGen.max()>0:
        #Get errors
        gen = windGen.values
        errors = [-(gen[idx]-gen[idx-1]) for idx in range(1,len(gen))]
        genErrors = gen[1:] #cut off first gen entry since no error for it
        #Divide into groups and get average power & percentile errors per group
        numGroups = 10
        # plotWindErrors(genErrors,errors,numGroups,errorPercentile)
        avgGens,lowPtlVals,upPtlVals = getAvgPowerAndPtlErrorPerGroup(numGroups,errorPercentile,
                                genErrors,errors)
        res = windGen.apply(getResForGen,args=(avgGens,lowPtlVals,upPtlVals,))
        res = pd.DataFrame(res.tolist(),columns=['up','down']) #split tuples
    else:
        res = pd.DataFrame({'up':0,'down':0},index=windGen.index)
    return res['up'].tolist(),abs(res['down']).tolist() 
    
#Get average power & percentile errors for each group
#Inputs: # groups to divide power by, error percentile, gen, errors
#Outputs: 2d list (avg pwoer, low ptl error, high ptl error)
def getAvgPowerAndPtlErrorPerGroup(numGroups,errorPercentile,gen,errors):
    lowPtl,upPtl = (100 - errorPercentile)/2,errorPercentile + (100 - errorPercentile)/2
    genAndErrorsSorted = sorted([[gen[idx],errors[idx]] for idx in range(len(gen))])
    ptsPerGroup = len(genAndErrorsSorted)//numGroups
    avgGens,lowPtlVals,upPtlVals = list(),list(),list()
    for grp in range(numGroups):
        avgGen,lowPtlVal,upPtlVal,genGrp,errorGrp = getAvgGenAndPtls(numGroups,grp,
                                    ptsPerGroup,genAndErrorsSorted,lowPtl,upPtl)
        avgGens.append(avgGen),lowPtlVals.append(lowPtlVal),upPtlVals.append(upPtlVal)
    return avgGens,lowPtlVals,upPtlVals
    
#Get avg gen & percentile errors for a single group
#Inputs: num groups, curr grp #, # points per group, and gen & errors in 2d list
#sorted in ascending gen order ([gen,errors], nx2)
#Outputs: avg gen, low ptl val, high ptl val, list of gen in grp, list of error in grp
def getAvgGenAndPtls(numGroups,grp,ptsPerGroup,genAndErrorsSorted,lowPtl,upPtl):
    startIdx = grp*ptsPerGroup
    endIdx = (grp+1)*ptsPerGroup if (grp != numGroups-1) else len(genAndErrorsSorted) #captures leftover points
    genGrp = [row[0] for row in genAndErrorsSorted[startIdx:endIdx]]
    errorGrp = [row[1] for row in genAndErrorsSorted[startIdx:endIdx]]
    avgGen = sum(genGrp)/len(genGrp)
    lowPtlVal,upPtlVal = np.percentile(np.array(errorGrp),lowPtl),np.percentile(np.array(errorGrp),upPtl)
    return avgGen,lowPtlVal,upPtlVal,genGrp,errorGrp

#Given low & high pctl error vals for average power in each group, interpolate
#between average values for each wind gen value to get up & down reserve
#values specific to that gen value. For points below & above lowest & highest
#avg power output, use error for average value. Positive error
#indicates overforecast (predict 20 but is 10), which coresponds to reg up.
#Negative errors indicates underforecast, which responds to reg down.
def getResForGen(gen,avgPows,lowErrs,highErrs):
    locInAvgPows = [(val-gen)<0 for val in avgPows]
    if False not in locInAvgPows: 
        downRes,upRes = lowErrs[-1],highErrs[-1] #gen > highest avg gen
    else:
        avgPowIdx = locInAvgPows.index(False) #idx is for first False, so b/wn that & prior idx
        if avgPowIdx == 0: 
            downRes,upRes = lowErrs[avgPowIdx],highErrs[avgPowIdx] #gen < lowest avg gen
        else: 
            downRes = calcYValOnLine(lowErrs[avgPowIdx-1],lowErrs[avgPowIdx],
                        avgPows[avgPowIdx-1],avgPows[avgPowIdx],gen)
            upRes = calcYValOnLine(highErrs[avgPowIdx-1],highErrs[avgPowIdx],
                        avgPows[avgPowIdx-1],avgPows[avgPowIdx],gen)
    return upRes,downRes

def calcYValOnLine(y0,y1,x0,x1,x):
    return y0 + (y1-y0)/(x1-x0) * (x-x0)
################################################################################

########## CALCULATE SOLAR RESERVES ############################################
#Calculate solar reserves by calculating error versus time of day, divide day
#into night (no gen), pre-midday (sunrise -> peak), and post-midday (peak -> sunset)
#for each month, then use those values for each part of day by month.
#Inputs: 2d list of solar gen (col 1 = datetime, col 2 = gen (MWh) w/ headers),
#percentile error (float)
#Outputs: 1d list of solar reserves by hour
def calcSolarReserves(solarGen,errorPercentile):
    # plotSolarErrorsVsReserves(solarGen,errorPercentile)
    # plotSolarGen([[mnth,mnth+1] for mnth in range(1,13,2)],solarGen)
    # plotSolarErrors(solarGen)
    if solarGen.max()>0:
        #Offsets for which errors are used to calculate percentiles; sunrise & sunset have
        #large but predictable ramps. Offsets try to skip those ramps.
        if solarGen.shape[0]>8761: sunriseOffset,sunsetOffset = 5,8 #skip several intervals when using sub-hourly data
        else: sunriseOffset,sunsetOffset = 2,2 #skip first & last 2 hours of gen each day (sunrise & sunset)
        lowPtl,upPtl = (100 - errorPercentile)/2,errorPercentile + (100 - errorPercentile)/2
        monthGroups = [[mnth,mnth+1] for mnth in range(1,13,2)] #months in groups of 2; datetime month is 1..12
        upRes,downRes,dts = list(),list(),list()
        for months in monthGroups: #months is list of months
            monthsRows = solarGen[(solarGen.index.month==months[0]) | (solarGen.index.month==months[1])]
            preMiddayErrorsMonths,postMiddayErrorsMonths = getMonthsErrors(months,
                                monthsRows,sunriseOffset,sunsetOffset)
            lowPtlPre = np.percentile(np.array(preMiddayErrorsMonths),lowPtl)
            highPtlPre = np.percentile(np.array(preMiddayErrorsMonths),upPtl)
            lowPtlPost = np.percentile(np.array(postMiddayErrorsMonths),lowPtl)
            highPtlPost = np.percentile(np.array(postMiddayErrorsMonths),upPtl)           
            upResMonths,downResMonths = assignReserves(months,monthsRows,lowPtlPre,
                                                    highPtlPre,lowPtlPost,highPtlPost)
            upRes.extend(copy.copy(upResMonths))
            downRes.extend(copy.copy(downResMonths))
            dts.extend(list(monthsRows.index))
    else:
        upRes,downRes = [0 for i in range(solarGen.shape[0])],[0 for i in range(solarGen.shape[0])]
    return upRes,downRes

#Get power output errors for months divided by pre- and post-midday, skipping errors
#for sunrise & sunset.
#Inputs: 2d list of (dt,power output) for particular months (no headers),
#col #s w/ dt & gen data.
#Outputs: 1d lists of power output errors for pre-midday (sunrise -> midday)
#and post-midday (midday -> sunset), not including sunrise or sunset.
def getMonthsErrors(months,monthsRows,sunriseOffset,sunsetOffset):
    preMiddayErrorsMonths,postMiddayErrorsMonths = list(),list()
    currDate = monthsRows.index[0]
    while currDate.month in months:
        currDateRows = monthsRows[(monthsRows.index.month==currDate.month) & (monthsRows.index.day==currDate.day)]
        preMiddayErrors,postMiddayErrors = getDateErrors(currDateRows,sunriseOffset,sunsetOffset)
        preMiddayErrorsMonths.extend(preMiddayErrors)
        postMiddayErrorsMonths.extend(postMiddayErrors)
        currDate += datetime.timedelta(days=1)
    return preMiddayErrorsMonths,postMiddayErrorsMonths

#Calculate solar errors as chagne in power output from 1 time interval to next.
#Skip sunrise and sunset. Aggregate solar errors spearately for pre-midday
#and post-midday time periods.
#Inputs: 2d list for current date (col 1 = dt, col 2 = gen), col # w/ dt & gen
#data in that 2d list, datetimes for sunrise, sunset, and midday
#Outputs: 2 1d lists w/ errors for each time interval in pre-midday and
#post-midday time periods. Errors are positive if overforecast solar gen and negative
#if under forecast solar gen.
def getDateErrors(currDateRows,sunriseOffset,sunsetOffset):
    sunrise,sunset,midday = getSunriseAndSunset(currDateRows)
    gen,dts = list(currDateRows.values),list(currDateRows.index)
    errors = [0] + [-(gen[idx]-gen[idx-1]) for idx in range(1,len(gen))] #- so gen redux means positive error (overest)
    sunriseIdx,middayIdx,sunsetIdx = dts.index(sunrise),dts.index(midday),dts.index(sunset)
    preMiddayErrors = errors[sunriseIdx+sunriseOffset:middayIdx] 
    postMiddayErrors = errors[middayIdx:(sunsetIdx + 1 - sunsetOffset)] #+1 includes sunset
    return preMiddayErrors,postMiddayErrors 

#Return datetimes of rows w/ sunrise (first gen), sunset (last gen), and midday
#(point b/wn sunrise & sunset datetimes).
#Inputs: 2d list (col 1 = dt, col 2 = gen, no headers)
#Outputs: datetimes
def getSunriseAndSunset(currDateRows):
    gen = list(currDateRows.values)
    sunriseIdx = [val>0 for val in gen].index(True)
    sunsetIdx = len(gen) - [val>0 for val in list(reversed(gen))].index(True)
    sunrise,sunset = currDateRows.index[sunriseIdx],currDateRows.index[sunsetIdx]
    midday = sunrise + (sunset - sunrise)/2
    minuteIntervals = int(60*24/len(currDateRows))
    middayDistToNearestInterval = datetime.timedelta(minutes=((midday - sunrise).seconds/60%minuteIntervals))
    midday -= middayDistToNearestInterval
    return sunrise,sunset,midday

#Assign reserves based on time of day (sunrise -> midday, midday -> sunset)
#Inputs: 2d list w/ dt and gen (col 1 = dt, col 2 =gen, no header),
#col #s w/ dt & gen data, floats w/ low & high percentiles for pre-midday and post-midday
#Ouputs: up & down res (1d lists) for months
def assignReserves(months,monthsRows,lowPtlPre,highPtlPre,lowPtlPost,highPtlPost):
    upRes,downRes = [],[]
    currDate = monthsRows.index[0]
    while currDate.month in months:
        currDateRows = monthsRows[(monthsRows.index.month==currDate.month) & (monthsRows.index.day==currDate.day)]
        sunrise,sunset,midday = getSunriseAndSunset(currDateRows)
        preMidday = [(val>=sunrise and val<midday) for val in currDateRows.index]
        postMidday = [(val>=midday and val<sunset) for val in currDateRows.index]
        preMiddayUpRes,preMiddayDownRes = setUpAndDownRes(highPtlPre,lowPtlPre,preMidday)
        postMiddayUpRes,postMiddayDownRes = setUpAndDownRes(highPtlPost,lowPtlPost,postMidday)
        downRes.extend(list(map(operator.add,preMiddayDownRes,postMiddayDownRes)))
        upRes.extend(list(map(operator.add,preMiddayUpRes,postMiddayUpRes)))
        currDate += datetime.timedelta(days=1)
    return upRes,downRes

#Low ptl = reg down, high ptl = reg up (errors are positive when overforecast solar 
#gen, meaning need other units to ramp up, so that's reg up; and negative when
#underforecast solar gen, meaning need other units to ramp down, so that's reg down).
#Note that low ptl values are only reg down if negative; if positive, then don't
#need any ramp down capability, so set them to zero. As of 1/2/17 with NREL TX
#dataset, all hours have negative and positive low and high ptl vals, so all
#hours have reg up and down reqs.
#Inputs: floats (low ptl & high ptl values), 1d list of True/False where
#Trues indicate hours in pre- or post-midday.
#Outputs: 2 1d lists of up and down res requirements with high and low ptl values,
#respectively, for hours in pre- or post-midday. Down reserve requirements
#are returned as absolute values.
def setUpAndDownRes(highPtl,lowPtl,hoursInPartOfDay):
    if lowPtl < 0: downRes = [abs(lowPtl)*val for val in hoursInPartOfDay]
    else: downRes = [0*val for val in hoursInPartOfDay]
    if highPtl > 0: upRes = [highPtl*val for val in hoursInPartOfDay]
    else: upRes = [0*val for val in hoursInPartOfDay]
    return upRes,downRes

#If doing 5-min gen data, need to aggregate reserves to hourly level by 
#taking max reserve requirements for that hour
#Inputs: 1d lists of up & down res, 1d list of correpsonding datetimes
#Outputs: 1d lists of hourly up & down res
def aggregateResToHourly(upRes,downRes,dts):
    upResHourly,downResHourly = list(),list()
    lastDate = datetime.datetime(1980,1,1,1) #some random date not in dts
    for idx in range(len(upRes)):
        if dts[idx].hour != lastDate.hour: #new hour
            upResHourly.append(upRes[idx])
            downResHourly.append(downRes[idx])
        elif dts[idx].hour == lastDate.hour:
            if abs(upRes[idx]) > abs(upResHourly[-1]): upResHourly[-1] = upRes[idx]
            if abs(downRes[idx]) > abs(downResHourly[-1]): downResHourly[-1] = downRes[idx]
        lastDate = dts[idx]
    return upResHourly,downResHourly
################################################################################


########## PLOT SOLAR GEN VS TIME OF DAY #######################################
def plotSolarGen(monthGroups,solarGen):
    dtCol,genCol = solarGen[0].index('datetime'),solarGen[0].index('totalGen(MWh)')
    # plt.figure(2,figsize = (20,30))
    # grp = 0
    # for months in monthGroups: #datetime month is 1..12
    #     genRows = [row for row in solarGen[1:] if row[dtCol].month in months]
    #     genCountByHour = countGenByHour(genRows,dtCol,genCol)
    #     xCoords = [val+.5 for val in range(24)]
    #     ax = plt.subplot(3,4,grp+1)
    #     # ax = plt.subplot(2,3,grp+1)
    #     # ax = plt.subplot(2,2,grp+1)
    #     ax.bar(xCoords,genCountByHour)
    #     grp += 1
    # plt.ylabel('Count of Gen > 0')
    # plt.xlabel('Hour of Day')
    fig = plt.figure(3,figsize = (12,10))
    # plt.figure(3)
    grp = 0
    monthLabels = ['Jan. & Feb.','Mar. & Apr.','May & Jun.','Jul. & Aug.','Sep. & Oct.','Nov. & Dec.']
    labelCtr = 0
    for months in monthGroups:
        genRows = [row for row in solarGen[1:] if row[dtCol].month in months]
        errorsByHour = getErrorsByHour(genRows,dtCol,genCol) #returns 2d list w/ each row = errors in an hour
        ax = plt.subplot(2,3,grp+1)
        # ax = plt.subplot(2,3,grp+1)
        # ax = plt.subplot(2,2,grp+1)
        ax.boxplot(errorsByHour,whis=[5,95])
        xmin,xmax = 5,22
        ax.set_xlim([xmin,xmax]) #only show hours between 5 and 22
        ax.set_ylim([-60,60])
        plt.xticks(list(range(xmin,xmax,2)),list(range(xmin,xmax,2)))
        plt.title(monthLabels[labelCtr])
        if grp == 0 or grp == 3: plt.ylabel('Forecast Error (MW)')
        if grp in [3,4,5]: plt.xlabel('Hour of Day')
        labelCtr += 1
        grp += 1
    fig.set_size_inches(12,8)
    fig.savefig('test.png',dpi=300,
        transparent=True, bbox_inches='tight', pad_inches=0.1)
    plt.show()

def countGenByHour(genRows,dtCol,genCol):
    genCountByHour = [0]*24
    for row in genRows:
        if row[genCol] > 0: genCountByHour[row[dtCol].hour] += 1
    return genCountByHour

def getErrorsByHour(genRows,dtCol,genCol):
    gen = [row[genCol] for row in genRows]
    errors = [0] + [gen[idx]-gen[idx-1] for idx in range(1,len(gen))]
    dts = [row[dtCol] for row in genRows]
    errorByHour = []
    for hr in range(24):
        errorByHour.append([errors[idx] for idx in range(len(dts)) if dts[idx].hour == hr])
    return errorByHour

def plotSolarErrors(solarGen):
    dtCol,genCol = solarGen[0].index('datetime'),solarGen[0].index('totalGen(MWh)')
    monthsToPlot = [1,3,5,7,9,11]
    if len(solarGen) > 8761: 
        periodsPerDay = int(60/5*24)
        sunriseOffset,sunsetOffset = 5,8
        xmin,xmax = 50,250
    else: 
        periodsPerDay = 24
        sunriseOffset,sunsetOffset = 2,2
        xmin,xmax = 5,22
    plt.figure(1,figsize = (25,35))
    ctr = 1
    for monthToPlot in monthsToPlot:
        monthRows = [row for row in solarGen[1:] if row[dtCol].month == monthToPlot]
        monthGen = [row[genCol] for row in monthRows]    
        errors = [0] + [monthGen[idx] - monthGen[idx-1] for idx in range(1,len(monthGen))]
        for idx in range(0,len(errors),periodsPerDay):
            currErrors = errors[idx:(idx+periodsPerDay)]
            sunrise = [val>0 for val in currErrors].index(True) - 1
            sunset = len(currErrors) - [val<0 for val in list(reversed(currErrors))].index(True)
            ax = plt.subplot(230 + ctr)
            ax.plot(currErrors)
            ax.axvline(sunrise + sunriseOffset,color='k',ls='--')
            ax.axvline(sunset - sunsetOffset,color='k',ls='--')
        plt.title('Month #: ' + str(monthToPlot))
        ax.set_xlim([xmin,xmax])
        ctr += 1
    plt.ylabel('Error (MW)')
    plt.xlabel('Time interval (5 min intervals)')

def plotSolarErrorsVsReserves(solarGen,errorPercentile):
    if len(solarGen)>8761: sunriseOffset,sunsetOffset = 5,8 #skip several intervals when 
    else: sunriseOffset,sunsetOffset = 2,2 #skip first & last 2 hours of gen each day (sunrise & sunset)
    lowPtl,upPtl = (100 - errorPercentile)/2,errorPercentile + (100 - errorPercentile)/2
    dtCol,genCol = solarGen[0].index('datetime'),solarGen[0].index('totalGen(MWh)')
    monthGroups = [[mnth,mnth+1] for mnth in range(1,13,2)] #months in groups of 2; datetime month is 1..12
    preErrors,postErrors = list(),list()
    lowPtlPres,highPtlPres,lowPtlPosts,highPtlPosts = list(),list(),list(),list()
    for months in monthGroups: #months is list of months
        monthsRows = [row for row in solarGen[1:] if row[dtCol].month in months]
        preMiddayErrorsMonths,postMiddayErrorsMonths = getMonthsErrors(months,
                            monthsRows,dtCol,genCol,sunriseOffset,sunsetOffset)
        preErrors.append(preMiddayErrorsMonths)
        postErrors.append(postMiddayErrorsMonths)
        lowPtlPre = np.percentile(np.array(preMiddayErrorsMonths),lowPtl)
        lowPtlPres.append(lowPtlPre)
        highPtlPre = np.percentile(np.array(preMiddayErrorsMonths),upPtl)
        highPtlPres.append(highPtlPre)
        lowPtlPost = np.percentile(np.array(postMiddayErrorsMonths),lowPtl)
        lowPtlPosts.append(lowPtlPost)
        highPtlPost = np.percentile(np.array(postMiddayErrorsMonths),upPtl)    
        highPtlPosts.append(highPtlPost)
    xs = [i+1 for i in range(len(monthGroups))]
    xticklabels = ['JanFeb','MarApr','MayJun','JulAug','SepOct','NovDec']
    plt.figure(7,figsize=(25,35))
    ax = plt.subplot(121)
    ax.boxplot(preErrors,whis=[5,95])
    ax.plot(xs,lowPtlPres,'r.',ms=20)
    ax.plot(xs,highPtlPres,'r.',ms=20)
    ax.set_ylim([-100,100])
    plt.title('Pre-Midday')
    plt.xticks(xs,xticklabels)
    plt.yticks([val for val in range(-100,100,10)],[val for val in range(-100,100,10)])
    plt.xlabel('Month Sets')
    plt.ylabel('Error and Reserve Reqs (MW)')
    ax = plt.subplot(122)
    ax.boxplot(postErrors,whis=[5,95])
    ax.plot(xs,lowPtlPosts,'r.',ms=20)
    ax.plot(xs,highPtlPosts,'r.',ms=20)
    ax.set_ylim([-100,100])
    plt.title('Post-Midday')
    plt.ylabel('Error and Reserve Reqs (MW)')
    plt.xticks(xs,xticklabels)
    plt.yticks([val for val in range(-100,100,10)],[val for val in range(-100,100,10)])
    plt.xlabel('Month Sets')
################################################################################

########## PLOT WIND GEN VERSUS ERRORS #########################################
def plotWindErrors(gen,errors,numGroups,errorPercentile):
    plt.figure(1,figsize=(6,3))
    plt.scatter(gen,errors)
    plt.ylabel('Forecast Error (MW)')
    plt.xlabel('Power Output (MW)')
    #Plot errors & power for each group
    genAndErrorsSorted = sorted([[gen[idx],errors[idx]] for idx in range(len(gen))])
    ptsPerGroup = len(genAndErrorsSorted)//numGroups
    lowPtl,upPtl = (100 - errorPercentile)/2,errorPercentile + (100 - errorPercentile)/2
    plt.figure(2,figsize = (20,30))
    for grp in range(numGroups):
        avgGen,lowPtlVal,upPtlVal,genGrp,errorGrp = getAvgGenAndPtls(numGroups,grp,
                                                ptsPerGroup,genAndErrorsSorted,lowPtl,upPtl)
        ax = plt.subplot(2,5,grp+1)
        ax.scatter(genGrp,errorGrp,color='black')
        ax.plot([avgGen,avgGen],[lowPtlVal,upPtlVal],color='red',lw=5)
        if len(gen)>8761: ax.set_ylim([-2000,2000])
        else: ax.set_ylim([-5500,5500])
        ax.set_xlim([min(genGrp),max(genGrp)])
    plt.ylabel('Error'), plt.xlabel('Gen')
    plt.show()
################################################################################

########## PLOT DEMAND, WIND AND SOLAR GEN, AND RESERVES #######################
def plotGenDemandAndRes(demand,windGenRegion,solarGenRegion,regResHourly,flexResHourly,contResHourly):
    dateCol,genCol = windGenRegion[0].index('datetime'),windGenRegion[0].index('totalGen(MWh)')
    windGen,solarGen = [row[genCol] for row in windGenRegion[1:]],[row[genCol] for row in solarGenRegion[1:]]
    aug5DayOfYear,jan5DayOfYear,daysToPlot = 217, 5, 3
    tSliceJan = [val for val in range(24*(jan5DayOfYear-1)-1,24*(jan5DayOfYear-1)-1+24*daysToPlot)]
    tSliceAug = [val for val in range(24*(aug5DayOfYear-1)-1,24*(aug5DayOfYear-1)-1+24*daysToPlot)] 
    tSlices,labels = [tSliceJan,tSliceAug],['Jan','Aug']
    figctr = 1
    for idx in range(len(tSlices)):
        tSlice,label = tSlices[idx],labels[idx]
        demandSlice = [demand[idx] for idx in tSlice]
        windSlice = [windGen[idx] for idx in tSlice]
        solarSlice = [solarGen[idx] for idx in tSlice]
        regSlice = [regResHourly[idx] for idx in tSlice]
        flexSlice = [flexResHourly[idx] for idx in tSlice]
        contSlice = [contResHourly[idx] for idx in tSlice]
        totalResSlice = [regResHourly[idx] + flexResHourly[idx] + contResHourly[idx] for idx in tSlice]
        plt.figure(figctr,figsize = (15,15))
        figctr += 1
        ax = plt.subplot(411) #all res components
        reg = ax.plot(tSlice,regSlice,label='Regulation')
        flex = ax.plot(tSlice,flexSlice,label='Flexibility')
        cont = ax.plot(tSlice,contSlice,label='Contingency')
        res = ax.plot(tSlice,totalResSlice,label='Total Reserve')
        plt.legend()
        plt.ylabel('Reserves (MWh)')
        # plt.title(label)
        ax = plt.subplot(412) #demand
        ax.plot(tSlice,demandSlice)
        plt.ylabel('Demand (MWh)')
        ax = plt.subplot(413) #wind gen
        ax.plot(tSlice,windSlice)
        plt.ylabel('Wind Generation (MWh)')
        ax = plt.subplot(414) #solar gen
        ax.plot(tSlice,solarSlice)
        plt.ylabel('Solar Generation (MWh)')
        plt.xlabel('Hour in Year')
    plt.show()

def plotWindAndSolarRes(resWind,resSolar,windGenRegion,solarGenRegion,resType):
    dateCol,genCol = windGenRegion[0].index('datetime'),windGenRegion[0].index('totalGen(MWh)')
    windGen,solarGen = [row[genCol] for row in windGenRegion[1:]],[row[genCol] for row in solarGenRegion[1:]]
    aug5DayOfYear,jan5DayOfYear,daysToPlot = 217, 5, 5
    tSliceJan = [val for val in range(24*(jan5DayOfYear-1)-1,24*(jan5DayOfYear-1)-1+24*daysToPlot)]
    tSliceAug = [val for val in range(24*(aug5DayOfYear-1)-1,24*(aug5DayOfYear-1)-1+24*daysToPlot)] 
    tSlices,labels = [tSliceJan,tSliceAug],['January 5','August 5']
    figctr = 1
    for idx in range(len(tSlices)):
        tSlice,label = tSlices[idx],labels[idx]
        windSlice = [windGen[idx] for idx in tSlice]
        solarSlice = [solarGen[idx] for idx in tSlice]
        windResSlice = [resWind[idx] for idx in tSlice]
        solarResSlice = [resSolar[idx] for idx in tSlice]
        plt.figure(figctr,figsize = (15,15))
        figctr += 1
        ax = plt.subplot(411) 
        ax.plot(tSlice,windResSlice)
        plt.ylabel('Wind Reserves (MWh)')
        # plt.title(resType + ' Reserves for ' + str(daysToPlot) + ' Days Starting ' + label)
        ax = plt.subplot(412) #wind gen
        ax.plot(tSlice,windSlice)
        plt.ylabel('Wind Gen. (MWh)')
        ax = plt.subplot(413)
        ax.plot(tSlice,solarResSlice)
        plt.ylabel('Solar Reserves (MWh)')
        ax = plt.subplot(414) #solar gen
        ax.plot(tSlice,solarSlice)
        plt.ylabel('Solar Gen. (MWh)')
        plt.xlabel('Hour in Year')
    plt.show()
################################################################################

########## PLOT HOURLY WIND GEN TO COMPARE YEARS OF DATA #######################
#3 years of NREL wind gen data: 2004-2006. Compare CFs and gen shape in each year.
def plotHourlyWindGen(windGenHourlyTotal):
    dateCol,genCol = 0,1
    totalGenByYear = {2004:0,2005:0,2006:0}
    hourlyGenByYear = {2004:[],2005:[],2006:[]}
    for row in windGenHourlyTotal[1:]:
        if row[dateCol].year in totalGenByYear:
            totalGenByYear[row[dateCol].year] += row[genCol]
            hourlyGenByYear[row[dateCol].year].append(row[genCol])
    print('Total wind gen by year:',totalGenByYear)
    plt.figure(2,figsize=(20,30))
    numSubplots = 4
    for i in range(numSubplots):
        ax = plt.subplot(numSubplots*100 + 10 + (i+1))
        startHr,endHr = i*8760//numSubplots,(i+1)*8760//numSubplots
        gen2004 = ax.plot(hourlyGenByYear[2004][startHr:endHr],label='2004')
        gen2005 = ax.plot(hourlyGenByYear[2005][startHr:endHr],label='2005')
        gen2006 = ax.plot(hourlyGenByYear[2006][startHr:endHr],label='2006')
    plt.legend()
    plt.ylabel('Gen (MWh)')
    plt.xlabel('Hour')

    plt.figure(3,figsize=(20,30))
    ax = plt.subplot(111)
    years = [2004,2005,2006]
    for yr in years:
        ax.plot(sorted(hourlyGenByYear[yr]),label=str(yr))
    plt.legend()
    plt.ylabel('Gen MWh')

    plt.figure(4,figsize=(20,30))
    ax = plt.subplot(111)
    for yr in years:
        currGen = hourlyGenByYear[yr]
        diffGen = [currGen[idx]-currGen[idx-1] for idx in range(1,len(currGen))]
        ax.plot(sorted(diffGen),label=str(yr))
    plt.legend()
    plt.ylabel('Change in gen MWh')
################################################################################