import os, copy, datetime
from os import path
from AuxFuncs import *
import pandas as pd
import datetime as dt
import numpy as np
from netCDF4 import Dataset
from GetRenewableCFsMERRA_old import *


# Output: dfs of wind and solar generation (8760 dt rows, arbitrary cols)
def getNewRenewableCFs(genFleet, tgtTz, reYear, currYear, reDownFactor, interconn,pRegionShapes):
    if currYear > 2050: currYear = 2050
    # Import state bounds (array of within state = 1, outside = 0)
    if interconn == 'ERCOT':
        stateBounds = pd.read_excel(os.path.join('Data', 'MERRA', 'state_MERRA_Format_Bounds.xlsx'), index_col=0)
    elif interconn == 'EI':
        stateBounds = pd.read_excel(os.path.join('Data', 'MERRA', 'EI_offshore_MERRA_Format_Bounds.xlsx'), index_col=0)
    # Isolate wind & solar units
    windUnits, solarUnits = getREInFleet('Wind', genFleet), getREInFleet('Solar PV', genFleet)
    # Get list of wind / solar sites in region.
    lats, lons, cf = loadMerraData(reYear, interconn, pRegionShapes)
    assert (len(lats) == stateBounds.shape[0] and len(lons) == stateBounds.shape[1])
    # Match existing gens to CFs
    get_cf_index(windUnits, lats, lons), get_cf_index(solarUnits, lats, lons)
    # Calculate new CFs. Use given met year data but set dt index to currYear.
    cf = enforceStateBounds(cf, stateBounds)

    windCfs = calcNewCfs(windUnits, lats, lons, cf, 'wind', currYear)
    solarCfs = calcNewCfs(solarUnits, lats, lons, cf, 'solar', currYear)
    # Downscale if desired
    windCfs, solarCfs = windCfs[windCfs.columns[::reDownFactor]], solarCfs[solarCfs.columns[::reDownFactor]]
    # Shift to target timezone
    windCfs, solarCfs = shiftTz(windCfs, tgtTz, currYear, 'wind'), shiftTz(solarCfs, tgtTz, currYear, 'solar')
    return pd.concat([windCfs, solarCfs], axis=1)


def calcNewCfs(existingGens, lats, lons, cf, re, currYear):
    if currYear > 2050: currYear = 2050
    density = .9 if re == 'wind' else 5.7  # W/m^2; from https://www.seas.harvard.edu/news/2018/10/large-scale-wind-power-would-require-more-land-and-cause-more-environmental-impact
    cfs = dict()
    for latIdx in range(len(lats)):
        for lonIdx in range(len(lons)):
            lat, lon = lats[latIdx], lons[lonIdx]
            gensAtLoc = existingGens.loc[(existingGens['lat idx'] == latIdx) & (existingGens['lon idx'] == lonIdx)]
            existingCap = gensAtLoc['Capacity (MW)'].astype(float).sum()
            coordCfs = cf[re][latIdx, lonIdx, :]
            if existingCap > 0 or coordCfs.sum() > 0:  # filter out coords w/ no gen
                if existingCap < (
                        density * 1000 * 3014) / 1000:  # 1000 to get to kW/km^2; 3014 for km^2 of lat/long box per https://www.usgs.gov/faqs/how-much-distance-does-a-degree-minute-and-second-cover-your-maps?qt-news_science_products=0#qt-news_science_products
                    cfs[re + 'lat' + str(round(lat, 3)) + 'lon' + str(round(lon, 3))] = coordCfs
                else:
                    cfs[re + 'lat' + str(round(lat, 3)) + 'lon' + str(round(lon, 3))] = 0
                    print('**Max RE capacity @ lat/long:', lat, lon, ' (GetNewRenewableCFsMERRA)')
    # Add dt and set to Dataframe
    idx = pd.date_range('1/1/' + str(currYear) + ' 0:00', '12/31/' + str(currYear) + ' 23:00', freq='H')
    idx = idx.drop(idx[(idx.month == 2) & (idx.day == 29)])
    return pd.DataFrame(cfs, index=idx)


def enforceStateBounds(cf, stateBounds):
    for re in cf:
        for row in stateBounds.index:
            for col in stateBounds.columns:
                cf[re][row, col] *= stateBounds.loc[row, col]
    # plotCFs(cf)
    return cf

# import matplotlib.pyplot as plt
# def plotCFs(cf):
#     avgCfs,lats,lons = np.zeros((23,23)),np.zeros(23),np.zeros(23)
#     for re in cf:
#         cfs = cf[re]
#         for lat in range(cfs.shape[0]):
#             for lon in range(cfs.shape[1]):
#                 avgCfs[lat,lon] = cfs[lat,lon].mean()
#                 # lats[lat] = cfs['lat'][lat]
#                 # lons[lon] = cfs['lon'][lon]

#         plt.figure()
#         ax = plt.subplot(111)
#         im = ax.contourf(avgCfs,cmap='plasma')#,extent = [np.min(lons),np.max(lons),np.min(lats),np.max(lats)])
#         cbar = ax.figure.colorbar(im, ax=ax)#, ticks=np.arange(vmin,vmax,int((vmax-vmin)/5)))
#         plt.title(re)
#     plt.show()