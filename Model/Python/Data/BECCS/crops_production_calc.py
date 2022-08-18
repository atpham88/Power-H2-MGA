
import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

ref_dir = "C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Data\\BECCS\\"
crop = 'Switchgrass'
data_dir = ref_dir + crop + '\\'

crop_data_raw = pd.read_excel(data_dir+'PCAs_switchgrass_Union_clean.xlsx')

crop_data_raw['county_st'] = crop_data_raw['county'] + ' ' + crop_data_raw['state']
crop_data_raw['production_w']= crop_data_raw['production']*(crop_data_raw['area_sqmile'] / crop_data_raw.groupby('county_st')['area_sqmile'].transform('sum'))