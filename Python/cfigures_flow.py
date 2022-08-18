import pandas as pd
import numpy as np

def flow_figures(m_dir2, resultsDir_other_NZ, resultsDir_other_NE2020, resultsDir_other_NE2030, resultsDir_other_NE2040,
                 resultsDir_other_NE2050_1, resultsDir_other_NE2050_2):
    # read in power flow solution:
    resultsFlow_NZ = pd.read_csv(m_dir2 + resultsDir_other_NZ + 'vLineflowCE2050.csv')
    resultsFlow_NE2020 = pd.read_csv(m_dir2 + resultsDir_other_NE2020 + 'vLineflowCE2050.csv')
    resultsFlow_NE2030 = pd.read_csv(m_dir2 + resultsDir_other_NE2030 + 'vLineflowCE2050.csv')
    resultsFlow_NE2040 = pd.read_csv(m_dir2 + resultsDir_other_NE2040 + 'vLineflowCE2050.csv')
    resultsFlow_NE2050_1 = pd.read_csv(m_dir2 + resultsDir_other_NE2050_1 + 'vLineflowCE2050.csv')
    resultsFlow_NE2050_2 = pd.read_csv(m_dir2 + resultsDir_other_NE2050_2 + 'vLineflowCE2060.csv')

    serc_to_miso_NZ = -resultsFlow_NZ.SERCMISO.sum()
    serc_to_pjm_NZ = -resultsFlow_NZ.SERCPJM.sum()
    ny_to_ne_NZ = -resultsFlow_NZ.NYNE.sum()
    ny_to_pjm_NZ = -resultsFlow_NZ.NYPJM.sum()
    miso_to_pjm_NZ = -resultsFlow_NZ.MISOPJM.sum()
    miso_to_spp_NZ = -resultsFlow_NZ.MISOSPP.sum()
    miso_to_serc_NZ = -resultsFlow_NZ.MISOSERC.sum()
    pjm_to_serc_NZ = -resultsFlow_NZ.PJMSERC.sum()
    ne_to_ny_NZ = -resultsFlow_NZ.NENY.sum()
    pjm_to_ny_NZ = -resultsFlow_NZ.PJMNY.sum()
    pjm_to_miso_NZ = -resultsFlow_NZ.PJMMISO.sum()
    spp_to_miso_NZ = -resultsFlow_NZ.SPPMISO.sum()

    serc_to_miso_NE2020 = -resultsFlow_NE2020.SERCMISO.sum()
    serc_to_pjm_NE2020 = -resultsFlow_NE2020.SERCPJM.sum()
    ny_to_ne_NE2020 = -resultsFlow_NE2020.NYNE.sum()
    ny_to_pjm_NE2020 = -resultsFlow_NE2020.NYPJM.sum()
    miso_to_pjm_NE2020 = -resultsFlow_NE2020.MISOPJM.sum()
    miso_to_spp_NE2020 = -resultsFlow_NE2020.MISOSPP.sum()
    miso_to_serc_NE2020 = -resultsFlow_NE2020.MISOSERC.sum()
    pjm_to_serc_NE2020 = -resultsFlow_NE2020.PJMSERC.sum()
    ne_to_ny_NE2020 = -resultsFlow_NE2020.NENY.sum()
    pjm_to_ny_NE2020 = -resultsFlow_NE2020.PJMNY.sum()
    pjm_to_miso_NE2020 = -resultsFlow_NE2020.PJMMISO.sum()
    spp_to_miso_NE2020 = -resultsFlow_NE2020.SPPMISO.sum()

    serc_to_miso_NE2030 = -resultsFlow_NE2030.SERCMISO.sum()
    serc_to_pjm_NE2030 = -resultsFlow_NE2030.SERCPJM.sum()
    ny_to_ne_NE2030 = -resultsFlow_NE2030.NYNE.sum()
    ny_to_pjm_NE2030 = -resultsFlow_NE2030.NYPJM.sum()
    miso_to_pjm_NE2030 = -resultsFlow_NE2030.MISOPJM.sum()
    miso_to_spp_NE2030 = -resultsFlow_NE2030.MISOSPP.sum()
    miso_to_serc_NE2030 = resultsFlow_NE2030.MISOSERC.sum()
    pjm_to_serc_NE2030 = -resultsFlow_NE2030.PJMSERC.sum()
    ne_to_ny_NE2030 = -resultsFlow_NE2030.NENY.sum()
    pjm_to_ny_NE2030 = -resultsFlow_NE2030.PJMNY.sum()
    pjm_to_miso_NE2030 = -resultsFlow_NE2030.PJMMISO.sum()
    spp_to_miso_NE2030 = -resultsFlow_NE2030.SPPMISO.sum()

    serc_to_miso_NE2040 = -resultsFlow_NE2040.SERCMISO.sum()
    serc_to_pjm_NE2040 = -resultsFlow_NE2040.SERCPJM.sum()
    ny_to_ne_NE2040 = -resultsFlow_NE2040.NYNE.sum()
    ny_to_pjm_NE2040 = -resultsFlow_NE2040.NYPJM.sum()
    miso_to_pjm_NE2040 = -resultsFlow_NE2040.MISOPJM.sum()
    miso_to_spp_NE2040 = -resultsFlow_NE2040.MISOSPP.sum()
    miso_to_serc_NE2040 = -resultsFlow_NE2040.MISOSERC.sum()
    pjm_to_serc_NE2040 = -resultsFlow_NE2040.PJMSERC.sum()
    ne_to_ny_NE2040 = -resultsFlow_NE2040.NENY.sum()
    pjm_to_ny_NE2040 = -resultsFlow_NE2040.PJMNY.sum()
    pjm_to_miso_NE2040 = -resultsFlow_NE2040.PJMMISO.sum()
    spp_to_miso_NE2040 = -resultsFlow_NE2040.SPPMISO.sum()

    serc_to_miso_NE2050 = -resultsFlow_NE2050_1.SERCMISO.sum() + resultsFlow_NE2050_2.SERCMISO.sum()
    serc_to_pjm_NE2050 = -resultsFlow_NE2050_1.SERCPJM.sum() + resultsFlow_NE2050_2.SERCPJM.sum()
    ny_to_ne_NE2050 = -resultsFlow_NE2050_1.NYNE.sum() + resultsFlow_NE2050_2.NYNE.sum()
    ny_to_pjm_NE2050 = -resultsFlow_NE2050_1.NYPJM.sum() + resultsFlow_NE2050_2.NYPJM.sum()
    miso_to_pjm_NE2050 = -resultsFlow_NE2050_1.MISOPJM.sum() + resultsFlow_NE2050_2.MISOPJM.sum()
    miso_to_spp_NE2050 = -resultsFlow_NE2050_1.MISOSPP.sum() + resultsFlow_NE2050_2.MISOSPP.sum()
    miso_to_serc_NE2050 = -resultsFlow_NE2050_1.MISOSERC.sum() + resultsFlow_NE2050_2.MISOSERC.sum()
    pjm_to_serc_NE2050 = -resultsFlow_NE2050_1.PJMSERC.sum() + resultsFlow_NE2050_2.PJMSERC.sum()
    ne_to_ny_NE2050 = -resultsFlow_NE2050_1.NENY.sum() + resultsFlow_NE2050_2.NENY.sum()
    pjm_to_ny_NE2050 = -resultsFlow_NE2050_1.PJMNY.sum() + resultsFlow_NE2050_2.PJMNY.sum()
    pjm_to_miso_NE2050 = -resultsFlow_NE2050_1.PJMMISO.sum() + resultsFlow_NE2050_2.PJMMISO.sum()
    spp_to_miso_NE2050 = -resultsFlow_NE2050_1.SPPMISO.sum() + resultsFlow_NE2050_2.SPPMISO.sum()

    netFlow_serc_NZ = - serc_to_miso_NZ - serc_to_pjm_NZ + miso_to_serc_NZ + pjm_to_serc_NZ
    netFlow_ny_NZ = - ny_to_ne_NZ - ny_to_pjm_NZ + ne_to_ny_NZ + pjm_to_ny_NZ
    netFlow_miso_NZ = - miso_to_pjm_NZ - miso_to_spp_NZ - miso_to_serc_NZ + serc_to_miso_NZ + pjm_to_miso_NZ + spp_to_miso_NZ
    netFlow_pjm_NZ = - pjm_to_serc_NZ - pjm_to_ny_NZ - pjm_to_miso_NZ + serc_to_pjm_NZ + ny_to_pjm_NZ + miso_to_pjm_NZ
    netFlow_ne_NZ = - ne_to_ny_NZ + ny_to_ne_NZ
    netFlow_spp_NZ = - spp_to_miso_NZ + miso_to_spp_NZ

    netFlow_serc_NE2020 = - serc_to_miso_NE2020 - serc_to_pjm_NE2020 + miso_to_serc_NE2020 + pjm_to_serc_NE2020
    netFlow_ny_NE2020 = - ny_to_ne_NE2020 - ny_to_pjm_NE2020 + ne_to_ny_NE2020 + pjm_to_ny_NE2020
    netFlow_miso_NE2020 = - miso_to_pjm_NE2020 - miso_to_spp_NE2020 - miso_to_serc_NE2020 + serc_to_miso_NE2020 + pjm_to_miso_NE2020 + spp_to_miso_NE2020
    netFlow_pjm_NE2020 = - pjm_to_serc_NE2020 - pjm_to_ny_NE2020 - pjm_to_miso_NE2020 + serc_to_pjm_NE2020 + ny_to_pjm_NE2020 + miso_to_pjm_NE2020
    netFlow_ne_NE2020 = - ne_to_ny_NE2020 + ny_to_ne_NE2020
    netFlow_spp_NE2020 = - spp_to_miso_NE2020 + miso_to_spp_NE2020

    netFlow_serc_NE2030 = - serc_to_miso_NE2030 - serc_to_pjm_NE2030 + miso_to_serc_NE2030 + pjm_to_serc_NE2030
    netFlow_ny_NE2030 = - ny_to_ne_NE2030 - ny_to_pjm_NE2030 + ne_to_ny_NE2030 + pjm_to_ny_NE2030
    netFlow_miso_NE2030 = - miso_to_pjm_NE2030 - miso_to_spp_NE2030 - miso_to_serc_NE2030 + serc_to_miso_NE2030 + pjm_to_miso_NE2030 + spp_to_miso_NE2030
    netFlow_pjm_NE2030 = - pjm_to_serc_NE2030 - pjm_to_ny_NE2030 - pjm_to_miso_NE2030 + serc_to_pjm_NE2030 + ny_to_pjm_NE2030 + miso_to_pjm_NE2030
    netFlow_ne_NE2030 = - ne_to_ny_NE2030 + ny_to_ne_NE2030
    netFlow_spp_NE2030 = - spp_to_miso_NE2030 + miso_to_spp_NE2030

    netFlow_serc_NE2040 = - serc_to_miso_NE2040 - serc_to_pjm_NE2040 + miso_to_serc_NE2040 + pjm_to_serc_NE2040
    netFlow_ny_NE2040 = - ny_to_ne_NE2040 - ny_to_pjm_NE2040 + ne_to_ny_NE2040 + pjm_to_ny_NE2040
    netFlow_miso_NE2040 = - miso_to_pjm_NE2040 - miso_to_spp_NE2040 - miso_to_serc_NE2040 + serc_to_miso_NE2040 + pjm_to_miso_NE2040 + spp_to_miso_NE2040
    netFlow_pjm_NE2040 = - pjm_to_serc_NE2040 - pjm_to_ny_NE2040 - pjm_to_miso_NE2040 + serc_to_pjm_NE2040 + ny_to_pjm_NE2040 + miso_to_pjm_NE2040
    netFlow_ne_NE2040 = - ne_to_ny_NE2040 + ny_to_ne_NE2040
    netFlow_spp_NE2040 = - spp_to_miso_NE2040 + miso_to_spp_NE2040

    netFlow_serc_NE2050 = - serc_to_miso_NE2050 - serc_to_pjm_NE2050 + miso_to_serc_NE2050 + pjm_to_serc_NE2050
    netFlow_ny_NE2050 = - ny_to_ne_NE2050 - ny_to_pjm_NE2050 + ne_to_ny_NE2050 + pjm_to_ny_NE2050
    netFlow_miso_NE2050 = - miso_to_pjm_NE2050 - miso_to_spp_NE2050 - miso_to_serc_NE2050 + serc_to_miso_NE2050 + pjm_to_miso_NE2050 + spp_to_miso_NE2050
    netFlow_pjm_NE2050 = - pjm_to_serc_NE2050 - pjm_to_ny_NE2050 - pjm_to_miso_NE2050 + serc_to_pjm_NE2050 + ny_to_pjm_NE2050 + miso_to_pjm_NE2050
    netFlow_ne_NE2050 = - ne_to_ny_NE2050 + ny_to_ne_NE2050
    netFlow_spp_NE2050 = - spp_to_miso_NE2050 + miso_to_spp_NE2050

    netFlow_serc_all = np.around([netFlow_serc_NZ, netFlow_serc_NE2050, netFlow_serc_NE2040,
                                  netFlow_serc_NE2030, netFlow_serc_NE2020], decimals=1)
    netFlow_ny_all = np.around([netFlow_ny_NZ, netFlow_ny_NE2050, netFlow_ny_NE2040,
                                netFlow_ny_NE2030, netFlow_ny_NE2020], decimals=1)
    netFlow_miso_all = np.around([netFlow_miso_NZ, netFlow_miso_NE2050, netFlow_miso_NE2040,
                                  netFlow_miso_NE2030, netFlow_miso_NE2020], decimals=1)
    netFlow_pjm_all = np.around([netFlow_pjm_NZ, netFlow_pjm_NE2050, netFlow_pjm_NE2040,
                                 netFlow_pjm_NE2030, netFlow_pjm_NE2020], decimals=1)
    netFlow_ne_all = np.around([netFlow_ne_NZ, netFlow_ne_NE2050, netFlow_ne_NE2040,
                                netFlow_ne_NE2030, netFlow_ne_NE2020], decimals=1)
    netFlow_spp_all = np.around([netFlow_spp_NZ, netFlow_spp_NE2050, netFlow_spp_NE2040,
                                 netFlow_spp_NE2030, netFlow_spp_NE2020], decimals=1)

    return (netFlow_miso_all, netFlow_ne_all, netFlow_ny_all, netFlow_pjm_all, netFlow_serc_all, netFlow_spp_all)
