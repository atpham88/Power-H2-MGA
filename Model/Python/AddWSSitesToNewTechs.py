import pandas as pd, geopandas as gpd
from SetupTransmissionAndZones import assignGensToPRegions

def addWSSitesToNewTechs(newCfs,newTechsCE,pRegionShapes):
    sitesDfList = list()
    #For wind & solar, repeat tech row for each potential site, then remove original row
    for l,f in zip(['wind','solar'],['Wind','Solar']):
        re = newTechsCE.loc[newTechsCE['FuelType']==f]
        sites = [c for c in newCfs if l in c]
        sitesDf = pd.concat([re]*len(sites),ignore_index=True)
        sitesDf['PlantType'] = sites
        #Get lat/lon
        txt = sitesDf['PlantType'].str.split('lat',expand=True)[1]
        sitesDf[['Latitude','Longitude']] = txt.str.split('lon',expand=True).astype(float)
        newTechsCE.drop(re.index,inplace=True)
        sitesDfList.append(sitesDf)
    #Combine wind & solar rows into df, then map to regions & concat onto newTechsCE
    sitesDf = pd.concat(sitesDfList)
    sitesDf = sitesDf.drop('region',axis=1)
    sitesDf = assignGensToPRegions(sitesDf,pRegionShapes)
    newTechsCE = pd.concat([newTechsCE,sitesDf],ignore_index=True)
    newTechsCE.reset_index(inplace=True,drop=True)
    #Create GAMS symbol as plant type + region
    newTechsCE['GAMS Symbol'] = newTechsCE['PlantType'] + newTechsCE['region']
    #Relabel new CF columns to match GAMS symbols (needed for GAMS model later)
    reRows = newTechsCE.loc[newTechsCE['ThermalOrRenewableOrStorage']=='renewable']
    reRows.index = reRows['PlantType']
    gamsDict = reRows['GAMS Symbol'].to_dict()
    newCfs = newCfs[[k for k in gamsDict]].rename(gamsDict,axis=1)
    return newTechsCE,newCfs
