"""
An Pham
Updated 02/09/2022
Clean solar and wind CF after downloaded from NREL.
Combine all downloaded CF files into one master file

"""
import os
import pandas as pd
import geopandas as gpd
from geopandas import GeoDataFrame
import matplotlib.patheffects as PathEffects
import matplotlib.pyplot as plt
from shapely.geometry import Point
import glob
from timezonefinder import TimezoneFinder

dataset = 'solar'           # or 'wind
if dataset == 'solar':
    m_dir = "C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Data\\RE\\solar\\"
elif dataset == 'wind':
    m_dir = "C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Data\\RE\\wind\\"

# Combine all solar/wind capacity factors from all files:
cwd = os.path.dirname(m_dir)

if dataset == 'solar':
    all_files = glob.glob(m_dir + "solar*.csv")
elif dataset == 'wind':
    all_files = glob.glob(m_dir + "wind*.csv")

li = []
for filename in all_files:
    df = pd.read_csv(filename)
    df = df.iloc[:,1:]
    li.append(df)
frame = pd.concat(li, axis=1)
frame_T = frame.T

frame_T_index = frame_T.reset_index()

frame_T.insert(0, 'lat', 0)
frame_T.insert(0, 'lon', 0)

frame_T_index.rename(columns={'index': 'coordinates'}, inplace=True)
frame_split = frame_T_index["coordinates"].str.split(" ", n=1, expand=True)

frame_T_index["lat"] = frame_split[0]
frame_T_index["lon"] = frame_split[1]
frame_T_index.drop("coordinates", axis=1, inplace=True)

cols = frame_T_index.columns.tolist()
cols = cols[-1:] + cols[:-1]
cols = cols[0:1] + cols[-1:] + cols[1:-1]

frame_T_index = frame_T_index[cols]
frame_T_index["lon"] = pd.to_numeric(frame_T_index["lon"], downcast="float")
frame_T_index["lat"] = pd.to_numeric(frame_T_index["lat"], downcast="float")
frame_T_index = frame_T_index.sort_values(['lon', 'lat'], ignore_index=True)

# Save to csv:
frame_T_index.to_csv('C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Data\\RE\\' + dataset + '_cf_2012.csv')

# Map of renewable sites:
cf = frame_T_index[['lon','lat']]
frame_cf = frame_T_index.iloc[:,2:]
cf['cf'] = frame_cf.mean(axis=1)

geometry = [Point(xy) for xy in zip(cf.lon, cf.lat)]
cf = gpd.GeoDataFrame(cf, crs="EPSG:4326", geometry=geometry)

transRegions = dict()
transRegions['SERC'] = list(range(87, 99)) + list(range(101, 103))
transRegions['NYISO'] = [127, 128]
transRegions['ISONE'] = list(range(129, 135))
transRegions['MISO'] = [37] + list(range(42, 47)) + list(range(68, 87)) + [56, 58, 66] + list(range(103, 109))
transRegions['PJM'] = list(range(109, 127)) + [99, 100]
transRegions['SPP'] = [35, 36] + list(range(38, 42)) + list(range(47, 56)) + [57]
for r, p in transRegions.items():
    transRegions[r] = ['p' + str(i) for i in p]

pRegionShapes = gpd.read_file('C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Data\\REEDS\\Shapefiles\\' + 'PCAs.shp')
allPRegions = list()
for r, pRegions in transRegions.items(): allPRegions += pRegions
pRegions = allPRegions
pRegionShapes = pRegionShapes.loc[pRegionShapes['PCA_Code'].isin(pRegions)]
transRegionsReversed = dict()
for zone, pRegions in transRegions.items():
    for p in pRegions:
        transRegionsReversed[p] = zone
pRegionShapes['region'] = pRegionShapes['PCA_Code'].map(transRegionsReversed)
loadregions = pRegionShapes.dissolve(by='region')
loadregions = loadregions.reset_index()
loadregions = loadregions.drop(['PCA_Code', 'PCA_REG', 'RTO_Code'], axis=1)

fig, ax = plt.subplots()
cln = 'region'
#ax.set_aspect('equal')
cf.plot(ax=ax, column='cf', cmap='viridis_r', markersize=20, legend='True', label=dataset + " capacity factor")

loadregions.plot(ax=ax, facecolor="none",figsize=(200, 100),
                   edgecolors='black', linewidth=0.7)
                   #legend='True', legend_kwds=dict(loc='lower right', fontsize=9))
plt.axis('on')
f = plt.gcf()
cax = f.get_axes()[1]
cax.set_ylabel("Capacity Factor (MW)")
for idx, row in loadregions.iterrows():
    fnt = 10
    txt=plt.annotate(s=row[cln], xy=(loadregions.geometry.centroid.x[idx],loadregions.geometry.centroid.y[idx]),
                 horizontalalignment='center', fontsize=8, wrap=True, color='k')
    txt.set_path_effects([PathEffects.withStroke(linewidth=4, foreground='w')])
#ax.autoscale()
#sm = plt.cm.ScalarMappable(cmap='rainbow', norm=plt.Normalize(vmin=latlonGpd_join['wind_cf'].min(), vmax=latlonGpd_join['wind_cf'].max()))
#cbar_axis = inset_axes(latlonGpd_join, width='10%', height='5%',loc='lower right')
#plt.colorbar(sm, cax=cbar_axis, orientation='horizontal', pad=0.02)
#latlonGpd_join.text(x=-74, y=28, s='Wind capacity factors', fontsize=9.8)
minx, miny, maxx, maxy = pRegionShapes.total_bounds
plt.xlim(minx, maxx)
plt.ylim(miny, maxy)
fig.tight_layout()
plt.show()

fig.savefig(m_dir + dataset + '_cf_map.png', dpi=300)
