# Updated 09/21/2022 by An P.

import pandas as pd, numpy as np, geopandas as gpd, os, sys

# Get annual H2 demand:
def getH2AnnualDemand(currYear, transRegions, pRegionShapes, h2DemandScr):
    h2DemandFileName = 'Hydrogen_Economic_Potential_Supply_Demand_Corrected.csv'
    h2Demand = pd.read_csv(os.path.join('Data','H2 Demand', h2DemandFileName))
    h2DemandGpd = gpd.GeoDataFrame(h2Demand, geometry=gpd.points_from_xy(h2Demand.longitude, h2Demand.latitude))

    h2Demand = h2DemandGpd.sjoin(pRegionShapes, how="inner", predicate='intersects')
    h2Demand = h2Demand[h2Demand['scenario'] == h2DemandScr]

    h2DemandAmmonia = h2Demand.groupby('region')['demand_ammonia_kg'].sum() / 1000      # h2 demand in ton
    h2DemandBiofuel = h2Demand.groupby('region')['demand_biofuel_kg'].sum() / 1000
    h2DemandLDV = h2Demand.groupby('region')['demand_ldv_kg'].sum() / 1000
    h2DemandMetal = h2Demand.groupby('region')['demand_metals_kg'].sum() / 1000
    h2DemandMethanol = h2Demand.groupby('region')['demand_methanol_kg'].sum() / 1000
    h2DemandMHDV = h2Demand.groupby('region')['demand_mhdv_kg'].sum() / 1000
    h2DemandRefining = h2Demand.groupby('region')['demand_refining_kg'].sum() / 1000
    h2DemandSynfuel = h2Demand.groupby('region')['demand_synfuel_kg'].sum() / 1000
    h2DemandTot = h2Demand.groupby('region')['total_demand_kg'].sum() / 1000

    # Interpolating annual growth rate of h2 demand (using NREL H2@Scale Report, table ES-1)
    baseYear = 2015
    h2Refining_2015, h2Refining_2050 = 6, 19  # MMT
    h2Ammonia_2015, h2Ammonia_2050 = 3, 4
    h2Biofuel_2015, h2Biofuel_2050 = 0, 9
    h2Others_2015, h2Others_2050 = 1, 30

    h2GrRefining = (h2Refining_2050 / h2Refining_2015) ** (1 / (2050 - baseYear)) - 1
    h2GrAmmonia = (h2Ammonia_2050 / h2Ammonia_2015) ** (1 / (2050 - baseYear)) - 1
    h2GrBiofuel = (h2Biofuel_2050 / (h2Biofuel_2015 + 0.0000001)) ** (1 / (2050 - baseYear)) - 1
    h2GrOthers = (h2Others_2050 / h2Others_2015) ** (1 / (2050 - baseYear)) - 1

    h2DemandAmmonia_2015 = h2DemandAmmonia / ((1 + h2GrAmmonia) ** (2050 - baseYear))
    h2DemandBiofuel_2015 = h2DemandBiofuel / ((1 + h2GrBiofuel) ** (2050 - baseYear))
    h2DemandMetal_2015 = h2DemandMetal / ((1 + h2GrOthers) ** (2050 - baseYear))
    h2DemandMethanol_2015 = h2DemandMethanol / ((1 + h2GrOthers) ** (2050 - baseYear))
    h2DemandRefining_2015 = h2DemandRefining / ((1 + h2GrRefining) ** (2050 - baseYear))
    h2DemandSynfuel_2015 = h2DemandSynfuel / ((1 + h2GrOthers) ** (2050 - baseYear))

    h2DemandAmmoniaCurr = h2DemandAmmonia_2015 * (1 + h2GrAmmonia) ** (currYear - baseYear)
    h2DemandBiofuelCurr = h2DemandBiofuel_2015 * (1 + h2GrBiofuel) ** (currYear - baseYear)
    h2DemandMetalCurr = h2DemandMetal_2015 * (1 + h2GrOthers) ** (currYear - baseYear)
    h2DemandMethanolCurr = h2DemandMethanol_2015 * (1 + h2GrOthers) ** (currYear - baseYear)
    h2DemandRefiningCurr = h2DemandRefining_2015 * (1 + h2GrRefining) ** (currYear - baseYear)
    h2DemandSynfuelCurr = h2DemandSynfuel_2015 * (1 + h2GrOthers) ** (currYear - baseYear)

    h2DemandTotNoTransport = h2DemandAmmoniaCurr + h2DemandBiofuelCurr + h2DemandMetalCurr + h2DemandMethanolCurr \
                             + h2DemandRefiningCurr + h2DemandSynfuelCurr
    h2demand = importHourlyH2Demand(currYear, transRegions, h2DemandTotNoTransport)
    return h2demand

def importHourlyH2Demand(currYear, transRegions, h2AnnualDemand):
    # Initialize df
    if currYear > 2050: currYear = 2050
    dates = pd.date_range('1/1/' + str(currYear) + ' 0:00', '12/31/' + str(currYear) + ' 23:00', freq='H')
    dates = dates[~((dates.month == 2) & (dates.day == 29))]  # ditch leap day
    h2demand = pd.DataFrame(index=dates)

    h2AnnualDemandTranspose = h2AnnualDemand.to_frame()
    h2AnnualDemandTranspose = h2AnnualDemandTranspose.T

    for zone, pRegions in transRegions.items():
        h2demand[zone] = float(h2AnnualDemandTranspose[zone]/len(dates))

    return h2demand

