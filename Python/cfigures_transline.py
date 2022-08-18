import pandas as pd
import geopandas as gpd

def transline_figures(shapefile_dir,m_dir2, resultsDir_other_NZ, resultsDir_other_NE2020, resultsDir_other_NE2030, resultsDir_other_NE2040,
                 resultsDir_other_NE2050_1, resultsDir_other_NE2050_2):
    # read in power flow solution:
    resultsFlow_NZ = pd.read_csv(m_dir2 + resultsDir_other_NZ + 'vNl2050.csv')
    resultsFlow_NE2020 = pd.read_csv(m_dir2 + resultsDir_other_NE2020 + 'vNl2050.csv')
    resultsFlow_NE2030 = pd.read_csv(m_dir2 + resultsDir_other_NE2030 + 'vNl2050.csv')
    resultsFlow_NE2040 = pd.read_csv(m_dir2 + resultsDir_other_NE2040 + 'vNl2050.csv')
    resultsFlow_NE2050_1 = pd.read_csv(m_dir2 + resultsDir_other_NE2050_1 + 'vNl2050.csv')
    resultsFlow_NE2050_2 = pd.read_csv(m_dir2 + resultsDir_other_NE2050_2 + 'vNl2060.csv')

    miso_serc_NZ = resultsFlow_NZ.iloc[0, 1] + resultsFlow_NZ.iloc[6, 1]
    pjm_serc_NZ = resultsFlow_NZ.iloc[1, 1] + resultsFlow_NZ.iloc[7, 1]
    ne_ny_NZ = resultsFlow_NZ.iloc[2, 1] + resultsFlow_NZ.iloc[8, 1]
    pjm_ny_NZ = resultsFlow_NZ.iloc[3, 1] + resultsFlow_NZ.iloc[9, 1]
    pjm_miso_NZ = resultsFlow_NZ.iloc[4, 1] + resultsFlow_NZ.iloc[10, 1]
    spp_miso_NZ = resultsFlow_NZ.iloc[5, 1] + resultsFlow_NZ.iloc[11, 1]

    miso_serc_NE2020 = resultsFlow_NE2020.iloc[0, 1] + resultsFlow_NE2020.iloc[6, 1]
    pjm_serc_NE2020 = resultsFlow_NE2020.iloc[1, 1] + resultsFlow_NE2020.iloc[7, 1]
    ne_ny_NE2020 = resultsFlow_NE2020.iloc[2, 1] + resultsFlow_NE2020.iloc[8, 1]
    pjm_ny_NE2020 = resultsFlow_NE2020.iloc[3, 1] + resultsFlow_NE2020.iloc[9, 1]
    pjm_miso_NE2020 = resultsFlow_NE2020.iloc[4, 1] + resultsFlow_NE2020.iloc[10, 1]
    spp_miso_NE2020 = resultsFlow_NE2020.iloc[5, 1] + resultsFlow_NE2020.iloc[11, 1]

    miso_serc_NE2030 = resultsFlow_NE2030.iloc[0, 1] + resultsFlow_NE2030.iloc[6, 1]
    pjm_serc_NE2030 = resultsFlow_NE2030.iloc[1, 1] + resultsFlow_NE2030.iloc[7, 1]
    ne_ny_NE2030 = resultsFlow_NE2030.iloc[2, 1] + resultsFlow_NE2030.iloc[8, 1]
    pjm_ny_NE2030 = resultsFlow_NE2030.iloc[3, 1] + resultsFlow_NE2030.iloc[9, 1]
    pjm_miso_NE2030 = resultsFlow_NE2030.iloc[4, 1] + resultsFlow_NE2030.iloc[10, 1]
    spp_miso_NE2030 = resultsFlow_NE2030.iloc[5, 1] + resultsFlow_NE2030.iloc[11, 1]

    miso_serc_NE2040 = resultsFlow_NE2040.iloc[0, 1] + resultsFlow_NE2040.iloc[6, 1]
    pjm_serc_NE2040 = resultsFlow_NE2040.iloc[1, 1] + resultsFlow_NE2040.iloc[7, 1]
    ne_ny_NE2040 = resultsFlow_NE2040.iloc[2, 1] + resultsFlow_NE2040.iloc[8, 1]
    pjm_ny_NE2040 = resultsFlow_NE2040.iloc[3, 1] + resultsFlow_NE2040.iloc[9, 1]
    pjm_miso_NE2040 = resultsFlow_NE2040.iloc[4, 1] + resultsFlow_NE2040.iloc[10, 1]
    spp_miso_NE2040 = resultsFlow_NE2040.iloc[5, 1] + resultsFlow_NE2040.iloc[11, 1]

    miso_to_serc_NE2050 = resultsFlow_NE2050_1.iloc[0, 1] + resultsFlow_NE2050_2.iloc[0, 1]
    pjm_to_serc_NE2050 = resultsFlow_NE2050_1.iloc[1, 1] + resultsFlow_NE2050_2.iloc[1, 1]
    ne_to_ny_NE2050 = resultsFlow_NE2050_1.iloc[2, 1] + resultsFlow_NE2050_2.iloc[2, 1]
    pjm_to_ny_NE2050 = resultsFlow_NE2050_1.iloc[3, 1] + resultsFlow_NE2050_2.iloc[3, 1]
    pjm_to_miso_NE2050 = resultsFlow_NE2050_1.iloc[4, 1] + resultsFlow_NE2050_2.iloc[4, 1]
    spp_to_miso_NE2050 = resultsFlow_NE2050_1.iloc[5, 1] + resultsFlow_NE2050_2.iloc[5, 1]
    serc_to_miso_NE2050 = resultsFlow_NE2050_1.iloc[6, 1] + resultsFlow_NE2050_2.iloc[6, 1]
    serc_to_pjm_NE2050 = resultsFlow_NE2050_1.iloc[7, 1] + resultsFlow_NE2050_2.iloc[7, 1]
    ny_to_ne_NE2050 = resultsFlow_NE2050_1.iloc[8, 1] + resultsFlow_NE2050_2.iloc[8, 1]
    ny_to_pjm_NE2050 = resultsFlow_NE2050_1.iloc[9, 1] + resultsFlow_NE2050_2.iloc[9, 1]
    miso_to_pjm_NE2050 = resultsFlow_NE2050_1.iloc[10, 1] + resultsFlow_NE2050_2.iloc[10, 1]
    miso_to_spp_NE2050 = resultsFlow_NE2050_1.iloc[11, 1] + resultsFlow_NE2050_2.iloc[11, 1]

    miso_serc_NE2050 = miso_to_serc_NE2050 + serc_to_miso_NE2050
    pjm_serc_NE2050 = pjm_to_serc_NE2050 + serc_to_pjm_NE2050
    ne_ny_NE2050 = ne_to_ny_NE2050 + ny_to_ne_NE2050
    pjm_ny_NE2050 = pjm_to_ny_NE2050 + ny_to_pjm_NE2050
    pjm_miso_NE2050 = pjm_to_miso_NE2050 + miso_to_pjm_NE2050
    spp_miso_NE2050 = spp_to_miso_NE2050 + miso_to_spp_NE2050

    transRegions = dict()
    transRegions['SERC'] = list(range(87, 99)) + list(range(101, 103))
    transRegions['NYISO'] = [127, 128]
    transRegions['ISONE'] = list(range(129, 135))
    transRegions['MISO'] = [37] + list(range(42, 47)) + list(range(68, 87)) + [56, 58, 66] + list(range(103, 109))
    transRegions['PJM'] = list(range(109, 127)) + [99, 100]
    transRegions['SPP'] = [35, 36] + list(range(38, 42)) + list(range(47, 56)) + [57]
    for r, p in transRegions.items():
        transRegions[r] = ['p' + str(i) for i in p]

    pRegionShapes = gpd.read_file(shapefile_dir + 'PCAs.shp')
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

    miso_serc = [miso_serc_NZ, miso_serc_NE2050, miso_serc_NE2040, miso_serc_NE2030, miso_serc_NE2020]
    pjm_serc = [pjm_serc_NZ, pjm_serc_NE2050, pjm_serc_NE2040, pjm_serc_NE2030, pjm_serc_NE2020]
    ne_ny = [ne_ny_NZ, ne_ny_NE2050, ne_ny_NE2040, ne_ny_NE2030, ne_ny_NE2020]
    pjm_ny = [pjm_ny_NZ, pjm_ny_NE2050, pjm_ny_NE2040, pjm_ny_NE2030, pjm_ny_NE2020]
    pjm_miso = [pjm_miso_NZ, pjm_miso_NE2050, pjm_miso_NE2040, pjm_miso_NE2030, pjm_miso_NE2020]
    spp_miso = [spp_miso_NZ, spp_miso_NE2050, spp_miso_NE2040, spp_miso_NE2030, spp_miso_NE2020]

    return (pRegionShapes, loadregions, miso_serc, pjm_serc, ne_ny, pjm_ny, pjm_miso, spp_miso)
