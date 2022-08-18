
'''
An Pham
12/8/2021
Processing Data by Interconnection-level
'''
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
from palettable.wesanderson import Margot1_5

# Interconnection boundaries data:
us_ic_data = gpd.read_file(r"C:\Users\atpha\Documents\Postdocs\Projects\NETs\GIS\GIS_population_weight_EI\REEDS PCA\PCAs.shp")

serc = list(range(87,99)) + list(range(101,103))
ny = [127,128]
ne = list(range(129,135))
miso = [37] + list(range(42,47)) + list(range(68,87)) + [56,58,66] + list(range(103,109))
pjm = list(range(109,127)) + [99,100]
spp = [35,36] + list(range(38,42)) + list(range(47,56)) + [57]
ei = serc + ny + ne  + miso + pjm + spp
ei.sort()

tx = list(range(60,66)) + [67]

for i in list(range(len(tx))):
    tx[i] = 'p' + str(tx[i])

for i in list(range(len(ei))):
    ei[i] = 'p' + str(ei[i])

us_ic_data["IC"] = np.where(us_ic_data["PCA_Code"].isin(ei), "EI", "Other")

for i in list(range(len(us_ic_data))):
    if us_ic_data["IC"][i] == "Other":
        if us_ic_data["PCA_Code"][i] in tx:
            us_ic_data["IC"][i] = "TX"

us_ic_data.loc[us_ic_data['IC'] =="Other", 'IC'] = "WI"
#us_ic_data = us_ic_data.dissolve(by='IC')
us_ic_data = us_ic_data.to_crs('epsg:4269')
us_ic_data.to_file(r"C:\Users\atpha\Documents\Postdocs\Projects\NETs\GIS\GIS_population_weight_EI\REEDS PCA\us_ic_data.shp")
#us_ic_data['IC'] = us_ic_data.index
#us_ic_data = us_ic_data.drop(columns=['OBJECTID','PCA_REG','Shape_Leng','Shape_Area'])

# US demographic data:
us_dem_data = gpd.read_file(r"C:\Users\atpha\Documents\Postdocs\Projects\NETs\GIS\GIS_population_weight_EI\USA_Counties\USA_Counties.shp")
us_dem_data = us_dem_data[~us_dem_data.STATE_FIPS.isin(['02','15','72'])]

#us_dem_data = us_dem_data.dissolve(by='STATE_NAME', aggfunc = 'sum')
us_dem_data = us_dem_data.to_crs('epsg:4269')

us_dem_data.to_file(r"C:\Users\atpha\Documents\Postdocs\Projects\NETs\GIS\GIS_population_weight_EI\REEDS PCA\us_dem_data.shp")

# Spatial join US demographic data and interconnection data:
us_IC_demographic = gpd.sjoin(us_dem_data, us_ic_data, how="inner", op='intersects')

us_IC_demographic.to_csv(r"C:\Users\atpha\Documents\Postdocs\Projects\NETs\GIS\us_IC_demographic.csv")

fig, ax = plt.subplots()
ax.set_aspect('equal')
us_IC_demographic.plot(ax=ax, column='IC', cmap=Margot1_5.mpl_colormap, figsize=(200, 100),
                  edgecolors='black', linewidth=0.6, legend='True',
                   legend_kwds=dict(loc='lower right', fontsize=9))
#us_dem_data.plot(ax=ax, color='none', figsize=(200, 100), edgecolors='black', linewidth=0.1)
plt.axis('off')
plt.tight_layout()
plt.title('US Interconnections', fontsize=16)
plt.show()
fig.savefig(r"C:\Users\atpha\Documents\Postdocs\Projects\NETs\GIS\US_IC_map.png", dpi=300)