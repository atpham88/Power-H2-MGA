import pandas as pd
import numpy as np
import geopandas as gpd
from netCDF4 import Dataset

def resite_figures(merra_dir):
    solarFile, windFile = "C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Data\\RE\\solar_cf_2012.csv", \
                          "C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Data\\RE\\wind_cf_2012.csv"

    # Load data
    solarPowGen = pd.read_csv(solarFile)
    windPowGen = pd.read_csv(windFile)              # assume solar and wind cover same geographic region

    # Get lat and lons for both datasets
    lats_temp, lons_temp = solarPowGen['lat'], solarPowGen['lon']
    latsPd = pd.DataFrame(lats_temp, columns=['lat'])
    latsPd = latsPd.drop_duplicates()
    latsPd = latsPd.sort_values(by=['lat'])
    latsPd = latsPd.reset_index()
    lats = latsPd['lat'].to_numpy()
    lats_temp = lats_temp.to_numpy()

    lonsPd = pd.DataFrame(lons_temp, columns=['lon'])
    lonsPd = lonsPd.drop_duplicates()
    lonsPd = lonsPd.sort_values(by=['lon'])
    lonsPd = lonsPd.reset_index()
    lons = lonsPd['lon'].to_numpy()
    lons_temp = lons_temp.to_numpy()

    latsAll = pd.Series(latsPd['lat'])
    lonsAll = pd.Series(lonsPd['lon'])

    latlonList = [(i, j)
                  for i in latsPd.lat
                  for j in lonsPd.lon]

    latlonPd = pd.DataFrame(data=latlonList, columns=['lat', 'lon'])
    latlonGpd = gpd.GeoDataFrame(latlonPd, geometry=gpd.points_from_xy(latlonPd.lon, latlonPd.lat))
    latlonGpd = latlonGpd.set_crs(epsg=4326, inplace=True)

    cf_solar = solarPowGen.iloc[:,2:]
    cf_wind = windPowGen.iloc[:,2:]
    cf_solar = cf_solar.to_numpy()
    cf_wind = cf_wind.to_numpy()

    cf_solar = pd.DataFrame(np.mean(cf_solar, axis=1))
    cf_wind = pd.DataFrame(np.mean(cf_wind, axis=1))
    cf_solar, cf_wind = cf_solar.stack(), cf_wind.stack()
    cf_solar, cf_wind = cf_solar.reset_index(), cf_wind.reset_index()

    wind_cf = pd.DataFrame(data=lats_temp, columns=['lat'])
    wind_cf['lon'] = lons_temp
    solar_cf = pd.DataFrame(data=lats_temp, columns=['lat'])
    solar_cf['lon'] = lons_temp

    wind_cf['wind_cf'] = cf_wind.iloc[:,2]
    solar_cf['solar_cf'] = cf_solar.iloc[:,2]


    return (wind_cf, solar_cf)
