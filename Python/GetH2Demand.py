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

    h2DemandAmmoniaCurr = h2DemandAmmonia * (1 + h2GrAmmonia) ** (currYear - baseYear)
    h2DemandBiofuelCurr = h2DemandBiofuel * (1 + h2GrBiofuel) ** (currYear - baseYear)
    h2DemandMetalCurr = h2DemandMetal * (1 + h2GrOthers) ** (currYear - baseYear)
    h2DemandMethanolCurr = h2DemandMethanol * (1 + h2GrOthers) ** (currYear - baseYear)
    h2DemandRefiningCurr = h2DemandRefining * (1 + h2GrRefining) ** (currYear - baseYear)
    h2DemandSynfuelCurr = h2DemandSynfuel * (1 + h2GrOthers) ** (currYear - baseYear)

    h2DemandTotNoTransport = h2DemandAmmoniaCurr + h2DemandBiofuelCurr + h2DemandMetalCurr + h2DemandMethanolCurr \
                             + h2DemandRefiningCurr + h2DemandSynfuelCurr

    return h2DemandTotNoTransport

