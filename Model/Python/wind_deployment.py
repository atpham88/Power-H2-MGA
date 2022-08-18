import pandas as pd
import numpy as np

def widep_figures(m_dir2, resultsDir_other_NZ, resultsDir_other_NE2020, resultsDir_other_NE2030, resultsDir_other_NE2040,
                 resultsDir_other_NE2050_2):
    # read in new capacity investment solution:
    resultsCE_NZ = pd.read_csv(m_dir2+resultsDir_other_NZ + 'genFleetAfterCE2050.csv')
    resultsCE_NE2020 = pd.read_csv(m_dir2+resultsDir_other_NE2020 + 'genFleetAfterCE2050.csv')
    resultsCE_NE2030 = pd.read_csv(m_dir2+resultsDir_other_NE2030 + 'genFleetAfterCE2050.csv')
    resultsCE_NE2040 = pd.read_csv(m_dir2+resultsDir_other_NE2040 + 'genFleetAfterCE2050.csv')
    resultsCE_NE2050 = pd.read_csv(m_dir2 + resultsDir_other_NE2050_2 + 'genFleetAfterCE2060.csv')

    resultsCE_NZ = resultsCE_NZ[resultsCE_NZ.YearAddedCE >= 2030]
    resultsCE_NE2020 = resultsCE_NE2020[resultsCE_NE2020.YearAddedCE >= 2030]
    resultsCE_NE2030 = resultsCE_NE2030[resultsCE_NE2030.YearAddedCE >= 2030]
    resultsCE_NE2040 = resultsCE_NE2040[resultsCE_NE2040.YearAddedCE >= 2030]
    resultsCE_NE2050 = resultsCE_NE2050[resultsCE_NE2050.YearAddedCE >= 2030]

    resultsCE_NZ = resultsCE_NZ[['PlantType', 'Capacity (MW)', 'region']]
    resultsCE_NE2020 = resultsCE_NE2020[['PlantType', 'Capacity (MW)', 'region']]
    resultsCE_NE2030 = resultsCE_NE2030[['PlantType', 'Capacity (MW)', 'region']]
    resultsCE_NE2040 = resultsCE_NE2040[['PlantType', 'Capacity (MW)', 'region']]
    resultsCE_NE2050 = resultsCE_NE2050[['PlantType', 'Capacity (MW)', 'region']]

    wind_CE_NZ = resultsCE_NZ.loc[(resultsCE_NZ['PlantType'].str.contains('Wind')) | (resultsCE_NZ['PlantType'].str.contains('wind'))]
    solar_CE_NZ = resultsCE_NZ.loc[(resultsCE_NZ['PlantType'].str.contains('Solar')) | (resultsCE_NZ['PlantType'].str.contains('solar'))]
    wind_CE_NE2020 = resultsCE_NE2020.loc[(resultsCE_NE2020['PlantType'].str.contains('Wind')) | (resultsCE_NE2020['PlantType'].str.contains('wind'))]
    solar_CE_NE2020 = resultsCE_NE2020.loc[(resultsCE_NE2020['PlantType'].str.contains('Solar')) | (resultsCE_NE2020['PlantType'].str.contains('solar'))]
    wind_CE_NE2030 = resultsCE_NE2030.loc[(resultsCE_NE2030['PlantType'].str.contains('Wind')) | (resultsCE_NE2030['PlantType'].str.contains('wind'))]
    solar_CE_NE2030 = resultsCE_NE2030.loc[(resultsCE_NE2030['PlantType'].str.contains('Solar')) | (resultsCE_NE2030['PlantType'].str.contains('solar'))]
    wind_CE_NE2040 = resultsCE_NE2040.loc[(resultsCE_NE2040['PlantType'].str.contains('Wind')) | (resultsCE_NE2040['PlantType'].str.contains('wind'))]
    solar_CE_NE2040 = resultsCE_NE2040.loc[(resultsCE_NE2040['PlantType'].str.contains('Solar')) | (resultsCE_NE2040['PlantType'].str.contains('solar'))]
    wind_CE_NE2050 = resultsCE_NE2050.loc[(resultsCE_NE2050['PlantType'].str.contains('Wind')) | (resultsCE_NE2050['PlantType'].str.contains('wind'))]
    solar_CE_NE2050 = resultsCE_NE2050.loc[(resultsCE_NE2050['PlantType'].str.contains('Solar')) | (resultsCE_NE2050['PlantType'].str.contains('solar'))]

    wind_CE_NZ = wind_CE_NZ.groupby('PlantType')['Capacity (MW)'].sum()
    wind_CE_NZ = wind_CE_NZ.reset_index()
    wind_CE_NZ['lat'] = wind_CE_NZ['PlantType'].str.slice(7, 11)
    wind_CE_NZ['lon'] = wind_CE_NZ['PlantType'].str.slice(15, 22)
    wind_CE_NZ['lat'] = wind_CE_NZ['lat'].astype(float)
    wind_CE_NZ['lon'] = wind_CE_NZ['lon'].astype(float)
    wind_CE_NZ = wind_CE_NZ.drop('PlantType', axis = 1)

    solar_CE_NZ = solar_CE_NZ.groupby('PlantType')['Capacity (MW)'].sum()
    solar_CE_NZ = solar_CE_NZ.reset_index()
    solar_CE_NZ['lat'] = solar_CE_NZ['PlantType'].str.slice(8, 12)
    solar_CE_NZ['lon'] = solar_CE_NZ['PlantType'].str.slice(16, 23)
    solar_CE_NZ['lat'] = solar_CE_NZ['lat'].astype(float)
    solar_CE_NZ['lon'] = solar_CE_NZ['lon'].astype(float)
    solar_CE_NZ = solar_CE_NZ.drop('PlantType', axis=1)

    wind_CE_NE2020 = wind_CE_NE2020.groupby('PlantType')['Capacity (MW)'].sum()
    wind_CE_NE2020 = wind_CE_NE2020.reset_index()
    wind_CE_NE2020['lat'] = wind_CE_NE2020['PlantType'].str.slice(7, 11)
    wind_CE_NE2020['lon'] = wind_CE_NE2020['PlantType'].str.slice(15, 22)
    wind_CE_NE2020['lat'] = wind_CE_NE2020['lat'].astype(float)
    wind_CE_NE2020['lon'] = wind_CE_NE2020['lon'].astype(float)
    wind_CE_NE2020 = wind_CE_NE2020.drop('PlantType', axis=1)
    solar_CE_NE2020 = solar_CE_NE2020.groupby('PlantType')['Capacity (MW)'].sum()
    solar_CE_NE2020 = solar_CE_NE2020.reset_index()
    solar_CE_NE2020['lat'] = solar_CE_NE2020['PlantType'].str.slice(8, 12)
    solar_CE_NE2020['lon'] = solar_CE_NE2020['PlantType'].str.slice(16, 23)
    solar_CE_NE2020['lat'] = solar_CE_NE2020['lat'].astype(float)
    solar_CE_NE2020['lon'] = solar_CE_NE2020['lon'].astype(float)
    solar_CE_NE2020 = solar_CE_NE2020.drop('PlantType', axis=1)

    wind_CE_NE2030 = wind_CE_NE2030.groupby('PlantType')['Capacity (MW)'].sum()
    wind_CE_NE2030 = wind_CE_NE2030.reset_index()
    wind_CE_NE2030['lat'] = wind_CE_NE2030['PlantType'].str.slice(7, 11)
    wind_CE_NE2030['lon'] = wind_CE_NE2030['PlantType'].str.slice(15, 22)
    wind_CE_NE2030['lat'] = wind_CE_NE2030['lat'].astype(float)
    wind_CE_NE2030['lon'] = wind_CE_NE2030['lon'].astype(float)
    wind_CE_NE2030 = wind_CE_NE2030.drop('PlantType', axis=1)
    solar_CE_NE2030 = solar_CE_NE2030.groupby('PlantType')['Capacity (MW)'].sum()
    solar_CE_NE2030 = solar_CE_NE2030.reset_index()
    solar_CE_NE2030['lat'] = solar_CE_NE2030['PlantType'].str.slice(8, 12)
    solar_CE_NE2030['lon'] = solar_CE_NE2030['PlantType'].str.slice(16, 23)
    solar_CE_NE2030['lat'] = solar_CE_NE2030['lat'].astype(float)
    solar_CE_NE2030['lon'] = solar_CE_NE2030['lon'].astype(float)
    solar_CE_NE2030 = solar_CE_NE2030.drop('PlantType', axis=1)

    wind_CE_NE2040 = wind_CE_NE2040.groupby('PlantType')['Capacity (MW)'].sum()
    wind_CE_NE2040 = wind_CE_NE2040.reset_index()
    wind_CE_NE2040['lat'] = wind_CE_NE2040['PlantType'].str.slice(7, 11)
    wind_CE_NE2040['lon'] = wind_CE_NE2040['PlantType'].str.slice(15, 22)
    wind_CE_NE2040['lat'] = wind_CE_NE2040['lat'].astype(float)
    wind_CE_NE2040['lon'] = wind_CE_NE2040['lon'].astype(float)
    wind_CE_NE2040 = wind_CE_NE2040.drop('PlantType', axis=1)
    solar_CE_NE2040 = solar_CE_NE2040.groupby('PlantType')['Capacity (MW)'].sum()
    solar_CE_NE2040 = solar_CE_NE2040.reset_index()
    solar_CE_NE2040['lat'] = solar_CE_NE2040['PlantType'].str.slice(8, 12)
    solar_CE_NE2040['lon'] = solar_CE_NE2040['PlantType'].str.slice(16, 23)
    solar_CE_NE2040['lat'] = solar_CE_NE2040['lat'].astype(float)
    solar_CE_NE2040['lon'] = solar_CE_NE2040['lon'].astype(float)
    solar_CE_NE2040 = solar_CE_NE2040.drop('PlantType', axis=1)

    wind_CE_NE2050 = wind_CE_NE2050.groupby('PlantType')['Capacity (MW)'].sum()
    wind_CE_NE2050 = wind_CE_NE2050.reset_index()
    wind_CE_NE2050['lat'] = wind_CE_NE2050['PlantType'].str.slice(7, 11)
    wind_CE_NE2050['lon'] = wind_CE_NE2050['PlantType'].str.slice(15, 22)
    wind_CE_NE2050['lat'] = wind_CE_NE2050['lat'].astype(float)
    wind_CE_NE2050['lon'] = wind_CE_NE2050['lon'].astype(float)
    wind_CE_NE2050 = wind_CE_NE2050.drop('PlantType', axis=1)
    solar_CE_NE2050 = solar_CE_NE2050.groupby('PlantType')['Capacity (MW)'].sum()
    solar_CE_NE2050 = solar_CE_NE2050.reset_index()
    solar_CE_NE2050['lat'] = solar_CE_NE2050['PlantType'].str.slice(8, 12)
    solar_CE_NE2050['lon'] = solar_CE_NE2050['PlantType'].str.slice(16, 23)
    solar_CE_NE2050['lat'] = solar_CE_NE2050['lat'].astype(float)
    solar_CE_NE2050['lon'] = solar_CE_NE2050['lon'].astype(float)
    solar_CE_NE2050 = solar_CE_NE2050.drop('PlantType', axis=1)

    return (wind_CE_NZ, solar_CE_NZ, wind_CE_NE2020, solar_CE_NE2020, wind_CE_NE2030, solar_CE_NE2030,
            wind_CE_NE2040, solar_CE_NE2040, wind_CE_NE2050, solar_CE_NE2050)
