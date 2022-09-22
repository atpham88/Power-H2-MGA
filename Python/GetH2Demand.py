# Updated 09/21/2022 by An P.

import pandas as pd, numpy as np, geopandas as gpd, os, sys

# Get annual H2 demand:
def getH2AnnualDemand(transRegions, pRegionShapes, h2DemandScr):
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

    h2DemandTotNoTransport = h2DemandAmmonia + h2DemandBiofuel + h2DemandMetal + h2DemandMethanol \
                             + h2DemandRefining + h2DemandSynfuel

    return h2DemandTotNoTransport

