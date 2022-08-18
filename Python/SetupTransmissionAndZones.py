#Michael Craig
#August 30, 2021
#Import transmission and regional data

import pandas as pd, numpy as np, geopandas as gpd, os, sys

################################################################################
#Define regions with inter-regional transmission constraints
#Output: dict of zone:[p-regions from REEDS] (zone is same as p-region in WECC & ERCOT since no aggregation)
def defineTransmissionRegions(interconn,balAuths):
    transRegions = dict()
    if balAuths == 'full': #running full interconnection
        if interconn == 'ERCOT' or interconn == 'WECC':
            regions = pd.read_csv(os.path.join('Data','REEDS','regions_default.csv'))
            csvRegions = {'ERCOT':'texas','WECC':'western','EI':'eastern'}
            regionRows = regions.loc[regions['interconnect']==csvRegions[interconn]]
            pRegions = regionRows['p'].unique()
            for p in pRegions: transRegions[p] = [p] #want value to be list so consistent format across interconns 
        elif interconn == 'EI':
            transRegions = createEIGroupings(transRegions)
    else:
        sys.exit('defineTransmissionRegions not set up for non-full run!')
    return transRegions

def createEIGroupings(transRegions):
    transRegions['SERC'] = list(range(87,99)) + list(range(101,103))
    transRegions['NY'] = [127,128]
    transRegions['NE'] = list(range(129,135))
    transRegions['MISO'] = [37] + list(range(42,47)) + list(range(68,87)) + [56,58,66] + list(range(103,109))
    transRegions['PJM'] = list(range(109,127)) + [99,100]
    transRegions['SPP'] = [35,36] + list(range(38,42)) + list(range(47,56)) + [57]
    for r,p in transRegions.items():
        transRegions[r] = ['p' + str(i) for i in p]
    return transRegions
################################################################################

################################################################################
def setupTransmissionAndZones(genFleetFull,transRegions,interconn,balAuths):
    #Read regions and map to zones
    pRegionShapes = loadRegions(transRegions)
    #Assign generators to zones (through p-regions)
    genFleet = assignGensToPRegions(genFleetFull.copy(),pRegionShapes)
    if interconn == 'ERCOT': genFleet = pd.concat([genERCOTRegionReassign(genFleetFull.copy()),genFleet])
    checkZones(genFleet,transRegions) 
    #Get transmission constraints between zones
    limits,costs,dists = getTransmissionData(interconn,transRegions,pRegionShapes)
    return genFleet,transRegions,limits,dists,costs,pRegionShapes

############################
def loadRegions(transRegions):
    pRegionShapes = importPRegions()
    pRegions = getAllPRegions(transRegions)
    pRegionShapes = pRegionShapes.loc[pRegionShapes['PCA_Code'].isin(pRegions)]
    transRegionsReversed = reverseTransRegions(transRegions)
    pRegionShapes['region'] = pRegionShapes['PCA_Code'].map(transRegionsReversed)
    return pRegionShapes

def importPRegions():
    return gpd.read_file(os.path.join('Data','REEDS','Shapefiles','PCAs.shp'))

def getAllPRegions(transRegions):
    allPRegions = list()
    for r,pRegions in transRegions.items(): allPRegions += pRegions
    return allPRegions

def reverseTransRegions(transRegions):
    transRegionsReversed = dict()
    for zone,pRegions in transRegions.items(): 
        for p in pRegions: 
            transRegionsReversed[p] = zone
    return transRegionsReversed

############################
# Assign generators to appropriate regions
def assignGensToPRegions(genFleet,pRegionShapes):
    genFleetGdf = gpd.GeoDataFrame(genFleet, geometry=gpd.points_from_xy(genFleet.Longitude, genFleet.Latitude))
    genFleetPCA = gpd.sjoin(genFleetGdf, pRegionShapes, how="inner", op='intersects')
    genFleet = pd.DataFrame(genFleetPCA)
    return genFleet

############################
#REEDS regions don't cover many ERCOT generators, so push ERCOT gens outside of 
#REEDS ERCOT bounds into ERCOT per regionSubs.
def genERCOTRegionReassign(genFleet):
    regionSubs = {'p57':'p63','p48':'p60','p66':'p64'}
    pRegionShapes = importPRegions()
    pRegionShapes = pRegionShapes.loc[pRegionShapes['PCA_Code'].isin([k for k in regionSubs])]
    pRegionShapes['region'] = pRegionShapes['PCA_Code'].map(regionSubs)
    genFleet = assignGensToPRegions(genFleet,pRegionShapes)
    return genFleet

###########################
def checkZones(genFleet,transRegions):
    genZones = genFleet['region'].unique()
    transZones = [z for z in transRegions]
    for z in genZones:
        if z not in transZones:
            sys.exit(('Generator zone ' + z + ' not in transmission zones ',transZones))

##########################
def getTransmissionData(interconn,transRegions,pRegionShapes):
    #Import raw transmission data from REEDS
    limits,costs,dists = importTransmissionData(interconn)
    #Filter data to p-regions of interest and, if using larger regions, combine p-region data
    limits,costs,dists = filterOrCombineTransmissionData(interconn,limits,costs,dists,transRegions,pRegionShapes)
    print(dists)
    print(limits)
    print(costs)
    dists,limits,costs = expandTransmissionData(interconn,limits,costs,dists)
    #Should have distances, costs, and limits for all possible lines; if not, need to align (likely add zero existing capacities).
    print(dists)
    print(limits)
    print(costs)
    assert((dists.shape[0] == limits.shape[0]) and (dists.shape[0] == costs.shape[0]))
    #Add GAMS symbols
    for df in [dists,limits,costs]: df['GAMS Symbol'] = df['r'] + df['rr']
    return limits,costs,dists

def importTransmissionData(interconn):
    limits = pd.read_csv(os.path.join('Data','REEDS','transmission_capacity_initial.csv'),header=0)
    costs = pd.read_csv(os.path.join('Data','REEDS','transmission_line_cost.csv'),names=['r','cost($/mw-mile)'])
    dists = pd.read_csv(os.path.join('Data','REEDS','transmission_distance.csv'),header=0)
    return limits,costs,dists

def filterOrCombineTransmissionData(interconn,limits,costs,dists,transRegions,pRegionShapes):
    #Filter dfs to only include lines that start/end within p-regions of interest
    pRegions = getAllPRegions(transRegions)
    limits = limits.loc[limits['r'].isin(pRegions)]
    limits = limits.loc[limits['rr'].isin(pRegions)]
    costs = costs.loc[costs['r'].isin(pRegions)]
    #If have multi-p-region zones, aggregate transmission data (median of costs & distances; sum of initial capacity)
    if interconn == 'EI':
        #Get total inter-regional transmission limits per REEDS data
        limits,costs = getInterregionalLimitsAndCostsEI(transRegions,limits,costs)
        #Get regional (instead of p-region) centroids for distance calculations
        regionShapes = pRegionShapes.dissolve(by='region')
        centroids = regionShapes.centroid
        #For each unique bidirectional regional pair, get distances.
        dists = list()
        for r,rr in zip(limits['r'],limits['rr']):
            #Get distance b/wn region centroids
            centR,centRR = centroids[r],centroids[rr]
            dist = haversine(centR,centRR)
            dists.append(pd.Series({'r':r,'rr':rr,'dist(mile)':haversine(centR,centRR)}))
        dists = pd.concat(dists,axis=1).T
    else: #load distances if not aggregating data. All pairwise combinations of p-regions included in data.
        dists = dists.loc[dists['r'].isin(pRegions)]
        dists = dists.loc[dists['rr'].isin(pRegions)]
    return limits,costs,dists

# REEDS transmission limits are only reported once for each unique p-region pair.
# E.g., p87 to p88 has 1 value that is NOT repeated for p88 to p87. So need to combine
# limits between regions independent of direction.
def getInterregionalLimitsAndCostsEI(transRegions,limits,costs):
    #Map p-regions to zones for aggregation
    transRegionsReversed = reverseTransRegions(transRegions)
    limits['rZone'] = limits['r'].map(transRegionsReversed)
    limits['rrZone'] = limits['rr'].map(transRegionsReversed)
    limits = limits.loc[limits['rZone']!=limits['rrZone']]
    #For each pair of regions, get inter-regional capacity
    totalLimits,medianCosts,finishedRegions = list(),list(),list()
    for r in transRegions:
        for rr in transRegions:
            if r != rr and (r,rr) not in finishedRegions:
                #Get inter-regional lines (if any) for both possible unidirectional routes
                interZoneLimitsRtoRR = limits.loc[(limits['rZone']==r) & (limits['rrZone']==rr)]
                interZoneLimitsRRtoR = limits.loc[(limits['rZone']==rr) & (limits['rrZone']==r)]
                interZoneLimits = pd.concat([interZoneLimitsRtoRR,interZoneLimitsRRtoR])
                if interZoneLimits.shape[0]>0:
                    #Get limits as sum of interregional capacity
                    totalLimitAC,totalLimitDC = interZoneLimits['AC'].sum(),interZoneLimits['DC'].sum()
                    totalLimits.append(pd.Series({'r':r,'rr':rr,'AC':totalLimitAC,'DC':totalLimitDC}))
                    finishedRegions += [(r,rr),(rr,r)]
                    #Get bidrectional inter-regional costs as median of costs between each pair of p-regions
                    interZoneCostsR = costs.loc[costs['r'].isin(interZoneLimits['r'].unique())]
                    interZoneCostsRR = costs.loc[costs['r'].isin(interZoneLimits['rr'].unique())]
                    medianR,medianRR = np.median(interZoneCostsR['cost($/mw-mile)']),np.median(interZoneCostsRR['cost($/mw-mile)'])
                    medianCosts.append(pd.Series({'r':r,'rr':rr,'cost($/mw-mile)':((medianR + medianRR)/2)}))
    return pd.concat(totalLimits,axis=1).T,pd.concat(medianCosts,axis=1).T

#Calculate distance between two coordinates using haversine formula.
def haversine(centR,centRR,kmToMi=0.621371):
    latR,lonR = np.radians(centR.y),np.radians(centR.x)
    latRR,lonRR = np.radians(centRR.y),np.radians(centRR.x)
    R = 6378.137 #km; mean Earth radius
    h = (np.sin((latR-latRR)/2))**2 + np.cos(latR) * np.cos(latRR) * (np.sin((lonR-lonRR)/2))**2
    c = 2 * np.arcsin(np.sqrt(h))
    return R*c*kmToMi #dist in mi

#Expand transmission data by (1) reversing source-sink line limits & (2) mapping costs to lines (not regions)
#& (3) add GAMS symbols as r + rr.
def expandTransmissionData(interconn,limits,costs,dists):
    #Reverse source-sink limits
    limits = addReversedLines(limits)
    if interconn == 'EI': #reverse dist & cost limits
        costsAllLines,dists = addReversedLines(costs),addReversedLines(dists)
    else: #map costs to lines using dists df, which has all pairwise combos
        costs = costs.set_index(costs['r'].values).to_dict()['cost($/mw-mile)']
        costsAllLines = dists[['r','rr']].copy()
        costsAllLines['rCost'],costsAllLines['rrCost'] = costsAllLines['r'].map(costs),costsAllLines['rr'].map(costs)
        costsAllLines['Line Cost ($/mw-mile)'] = (costsAllLines['rCost'] + costsAllLines['rrCost'])/2
    return dists,limits,costsAllLines

#Reverse all lines and add to df (e.g., df w/ r:p60,rr:p43 now has r:p60,rr:p43 and r:p43,rr:p60).
def addReversedLines(df):
    dfReversed = df.rename(columns={'r':'rr','rr':'r'})
    df = pd.concat([df,dfReversed])
    df.reset_index(inplace=True,drop=True)
    return df
################################################################################

#Unused distance code in getTransmissionData
# dists = pd.read_csv(os.path.join('Data','REEDS','transmission_distance.csv'),header=0)
# dists = dists.loc[dists['r'].isin(pRegions)]
# dists = dists.loc[dists['rr'].isin(pRegions)]
# dists['rZone'] = dists['r'].map(transRegionsReversed)
# dists['rrZone'] = dists['rr'].map(transRegionsReversed)
# dists = dists.loc[dists['rZone']!=dists['rrZone']]
# #Get distances
# interZoneDists = dists.loc[(dists['rZone']==r) & (dists['rrZone']==rr)]
# medDistAC,medDistDC = np.median(interZoneDists['AC'].values),np.median(interZoneDists['DC'].values)
# medianDists.append(pd.Series({'r':r,'rr':rr,'AC':medDistAC,'DC':medDistDC}))