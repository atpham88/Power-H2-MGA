import pandas as pd
import numpy as np

def cost_figures(m_dir, resultsDir_NZ, resultsDir_NE2020, resultsDir_NE2030, resultsDir_NE2040,
                 resultsDir_NE2050, co2EmsCapInFinalYear):
    # read in cost solution:
    resultsCost_NZ = pd.read_excel(m_dir + resultsDir_NZ + '.xlsx', sheet_name="Costs", header=None)
    resultsCost_NE2020 = pd.read_excel(m_dir + resultsDir_NE2020 + '.xlsx', sheet_name="Costs", header=None)
    resultsCost_NE2030 = pd.read_excel(m_dir + resultsDir_NE2030 + '.xlsx', sheet_name="Costs", header=None)
    resultsCost_NE2040 = pd.read_excel(m_dir + resultsDir_NE2040 + '.xlsx', sheet_name="Costs", header=None)
    resultsCost_NE2050 = pd.read_excel(m_dir + resultsDir_NE2050 + '.xlsx', sheet_name="Costs", header=None)

    opeCost_2030_NZ = resultsCost_NZ.iloc[0, 1] / 1000
    opeCost_2040_NZ = resultsCost_NZ.iloc[1, 1] / 1000
    opeCost_2050_NZ = resultsCost_NZ.iloc[2, 1] / 1000
    opeCost_tot_NZ = resultsCost_NZ.iloc[3, 1] / 1000

    capCost_2030_NZ = resultsCost_NZ.iloc[5, 1] / 1000
    capCost_2040_NZ = resultsCost_NZ.iloc[6, 1] / 1000
    capCost_2050_NZ = resultsCost_NZ.iloc[7, 1] / 1000
    capCost_tot_NZ = resultsCost_NZ.iloc[8, 1] / 1000

    totCost_2030_NZ = resultsCost_NZ.iloc[11, 1] / 1000
    totCost_2040_NZ = resultsCost_NZ.iloc[12, 1] / 1000
    totCost_2050_NZ = resultsCost_NZ.iloc[13, 1] / 1000
    totCost_tot_NZ = resultsCost_NZ.iloc[15, 1] / 1000

    opeCost_2030_NE2020 = resultsCost_NE2020.iloc[0, 1] / 1000
    opeCost_2040_NE2020 = resultsCost_NE2020.iloc[1, 1] / 1000
    opeCost_2050_NE2020 = resultsCost_NE2020.iloc[2, 1] / 1000
    opeCost_tot_NE2020 = resultsCost_NE2020.iloc[3, 1] / 1000

    capCost_2030_NE2020 = resultsCost_NE2020.iloc[5, 1] / 1000
    capCost_2040_NE2020 = resultsCost_NE2020.iloc[6, 1] / 1000
    capCost_2050_NE2020 = resultsCost_NE2020.iloc[7, 1] / 1000
    capCost_tot_NE2020 = resultsCost_NE2020.iloc[8, 1] / 1000

    totCost_2030_NE2020 = resultsCost_NE2020.iloc[11, 1] / 1000
    totCost_2040_NE2020 = resultsCost_NE2020.iloc[12, 1] / 1000
    totCost_2050_NE2020 = resultsCost_NE2020.iloc[13, 1] / 1000
    totCost_tot_NE2020 = resultsCost_NE2020.iloc[15, 1] / 1000

    opeCost_2030_NE2030 = resultsCost_NE2030.iloc[0, 1] / 1000
    opeCost_2040_NE2030 = resultsCost_NE2030.iloc[1, 1] / 1000
    opeCost_2050_NE2030 = resultsCost_NE2030.iloc[2, 1] / 1000
    opeCost_tot_NE2030 = resultsCost_NE2030.iloc[3, 1] / 1000

    capCost_2030_NE2030 = resultsCost_NE2030.iloc[5, 1] / 1000
    capCost_2040_NE2030 = resultsCost_NE2030.iloc[6, 1] / 1000
    capCost_2050_NE2030 = resultsCost_NE2030.iloc[7, 1] / 1000
    capCost_tot_NE2030 = resultsCost_NE2030.iloc[8, 1] / 1000

    totCost_2030_NE2030 = resultsCost_NE2030.iloc[11, 1] / 1000
    totCost_2040_NE2030 = resultsCost_NE2030.iloc[12, 1] / 1000
    totCost_2050_NE2030 = resultsCost_NE2030.iloc[13, 1] / 1000
    totCost_tot_NE2030 = resultsCost_NE2030.iloc[15, 1] / 1000

    opeCost_2030_NE2040 = resultsCost_NE2040.iloc[0, 1] / 1000
    opeCost_2040_NE2040 = resultsCost_NE2040.iloc[1, 1] / 1000
    opeCost_2050_NE2040 = resultsCost_NE2040.iloc[2, 1] / 1000
    opeCost_tot_NE2040 = resultsCost_NE2040.iloc[3, 1] / 1000

    capCost_2030_NE2040 = resultsCost_NE2040.iloc[5, 1] / 1000
    capCost_2040_NE2040 = resultsCost_NE2040.iloc[6, 1] / 1000
    capCost_2050_NE2040 = resultsCost_NE2040.iloc[7, 1] / 1000
    capCost_tot_NE2040 = resultsCost_NE2040.iloc[8, 1] / 1000

    totCost_2030_NE2040 = resultsCost_NE2040.iloc[11, 1] / 1000
    totCost_2040_NE2040 = resultsCost_NE2040.iloc[12, 1] / 1000
    totCost_2050_NE2040 = resultsCost_NE2040.iloc[13, 1] / 1000
    totCost_tot_NE2040 = resultsCost_NE2040.iloc[15, 1] / 1000

    opeCost_2030_NE2050 = resultsCost_NE2050.iloc[0, 1] / 1000
    opeCost_2040_NE2050 = resultsCost_NE2050.iloc[1, 1] / 1000
    opeCost_2050_NE2050 = resultsCost_NE2050.iloc[0, 4] / 1000
    opeCost_tot_NE2050 = resultsCost_NE2050.iloc[3, 1] / 1000

    capCost_2030_NE2050 = resultsCost_NE2050.iloc[5, 1] / 1000
    capCost_2040_NE2050 = resultsCost_NE2050.iloc[6, 1] / 1000
    capCost_2050_NE2050 = resultsCost_NE2050.iloc[7, 1] / 1000 + resultsCost_NE2050.iloc[5, 4] / 1000
    capCost_tot_NE2050 = resultsCost_NE2050.iloc[8, 1] / 1000

    totCost_2030_NE2050 = resultsCost_NE2050.iloc[11, 1] / 1000
    totCost_2040_NE2050 = resultsCost_NE2050.iloc[12, 1] / 1000
    totCost_2050_NE2050 = resultsCost_NE2050.iloc[13, 1] / 1000 + resultsCost_NE2050.iloc[11, 4] / 1000
    totCost_tot_NE2050 = resultsCost_NE2050.iloc[15, 1] / 1000

    NZ_tot_cost = np.array([totCost_2030_NZ, totCost_2040_NZ, totCost_2050_NZ])
    NE2050_tot_cost = np.array([totCost_2030_NE2050, totCost_2040_NE2050, totCost_2050_NE2050])
    NE2040_tot_cost = np.array([totCost_2030_NE2040, totCost_2040_NE2040, totCost_2050_NE2040])
    NE2030_tot_cost = np.array([totCost_2030_NE2030, totCost_2040_NE2030, totCost_2050_NE2030])
    NE2020_tot_cost = np.array([totCost_2030_NE2020, totCost_2040_NE2020, totCost_2050_NE2020])

    NZ_cap_cost = np.array([capCost_2030_NZ, capCost_2040_NZ, capCost_2050_NZ])
    NE2050_cap_cost = np.array([capCost_2030_NE2050, capCost_2040_NE2050, capCost_2050_NE2050])
    NE2040_cap_cost = np.array([capCost_2030_NE2040, capCost_2040_NE2040, capCost_2050_NE2040])
    NE2030_cap_cost = np.array([capCost_2030_NE2030, capCost_2040_NE2030, capCost_2050_NE2030])
    NE2020_cap_cost = np.array([capCost_2030_NE2020, capCost_2040_NE2020, capCost_2050_NE2020])

    NZ_ope_cost = np.array([opeCost_2030_NZ, opeCost_2040_NZ, opeCost_2050_NZ])
    NE2050_ope_cost = np.array([opeCost_2030_NE2050, opeCost_2040_NE2050, opeCost_2050_NE2050])
    NE2040_ope_cost = np.array([opeCost_2030_NE2040, opeCost_2040_NE2040, opeCost_2050_NE2040])
    NE2030_ope_cost = np.array([opeCost_2030_NE2030, opeCost_2040_NE2030, opeCost_2050_NE2030])
    NE2020_ope_cost = np.array([opeCost_2030_NE2020, opeCost_2040_NE2020, opeCost_2050_NE2020])

    NE2020_bNZ_cost = totCost_2050_NE2020 - totCost_2050_NZ
    NE2030_bNZ_cost = totCost_2050_NE2030 - totCost_2050_NZ
    NE2040_bNZ_cost = totCost_2050_NE2040 - totCost_2050_NZ
    NE2050_bNZ_cost = totCost_2050_NE2050 - totCost_2050_NZ

    NE2020_aba_cost = NE2020_bNZ_cost * 1000 / (0 - co2EmsCapInFinalYear)
    NE2030_aba_cost = NE2030_bNZ_cost * 1000 / (0 - co2EmsCapInFinalYear)
    NE2040_aba_cost = NE2040_bNZ_cost * 1000 / (0 - co2EmsCapInFinalYear)
    NE2050_aba_cost = NE2050_bNZ_cost * 1000 / (0 - co2EmsCapInFinalYear)

    # Transmission capacity expansion:
    p_serc_miso = 789601.399349318
    p_serc_pjm = 443112.18615991
    p_ny_ne = 1116716.40273073
    p_ny_pjm = 1066925.99970673
    p_miso_pjm = 564650.139171335
    p_miso_spp = 303709.700893924

    # read in line capacity expansion:
    resultsLine_NZ_2050 = pd.read_csv("C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Results_EI_NetZero_DACS2020_reference_TrueREFERENCE\\2050CO2Cap0\\CE\\" + 'vNl2050.csv')
    resultsLine_NE2020_2050 = pd.read_csv("C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Results_EI_Negative-724_DACS2020NEin2020_reference_TrueREFERENCE\\2050CO2Cap-724\\CE\\" + 'vNl2050.csv')
    resultsLine_NE2030_2050 = pd.read_csv("C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Results_EI_Negative-724_DACS2020NEin2030_reference_TrueREFERENCE\\2050CO2Cap-724\\CE\\" + 'vNl2050.csv')
    resultsLine_NE2040_2050 = pd.read_csv("C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Results_EI_Negative-724_DACS2020NEin2040_reference_TrueREFERENCE\\2050CO2Cap-724\\CE\\" + 'vNl2050.csv')
    resultsLine_NE2050_1_2050 = pd.read_csv("C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Results_EI_Negative-724_DACS2020NEin2050_reference_TrueREFERENCE\\2050CO2Cap-724\\CE\\" + 'vNl2050.csv')
    resultsLine_NE2050_2_2050 = pd.read_csv("C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Results_EI_Negative-724_DACS2020NEin2050_reference_TrueREFERENCE\\2060CO2Cap-724\\CE\\" + 'vNl2060.csv')

    miso_serc_NZ_2050 = resultsLine_NZ_2050.iloc[0, 1] + resultsLine_NZ_2050.iloc[6, 1]
    pjm_serc_NZ_2050 = resultsLine_NZ_2050.iloc[1, 1] + resultsLine_NZ_2050.iloc[7, 1]
    ne_ny_NZ_2050 = resultsLine_NZ_2050.iloc[2, 1] + resultsLine_NZ_2050.iloc[8, 1]
    pjm_ny_NZ_2050 = resultsLine_NZ_2050.iloc[3, 1] + resultsLine_NZ_2050.iloc[9, 1]
    pjm_miso_NZ_2050 = resultsLine_NZ_2050.iloc[4, 1] + resultsLine_NZ_2050.iloc[10, 1]
    spp_miso_NZ_2050 = resultsLine_NZ_2050.iloc[5, 1] + resultsLine_NZ_2050.iloc[11, 1]

    miso_serc_NE2020_2050 = resultsLine_NE2020_2050.iloc[0, 1] + resultsLine_NE2020_2050.iloc[6, 1]
    pjm_serc_NE2020_2050 = resultsLine_NE2020_2050.iloc[1, 1] + resultsLine_NE2020_2050.iloc[7, 1]
    ne_ny_NE2020_2050 = resultsLine_NE2020_2050.iloc[2, 1] + resultsLine_NE2020_2050.iloc[8, 1]
    pjm_ny_NE2020_2050 = resultsLine_NE2020_2050.iloc[3, 1] + resultsLine_NE2020_2050.iloc[9, 1]
    pjm_miso_NE2020_2050 = resultsLine_NE2020_2050.iloc[4, 1] + resultsLine_NE2020_2050.iloc[10, 1]
    spp_miso_NE2020_2050 = resultsLine_NE2020_2050.iloc[5, 1] + resultsLine_NE2020_2050.iloc[11, 1]

    miso_serc_NE2030_2050 = resultsLine_NE2030_2050.iloc[0, 1] + resultsLine_NE2030_2050.iloc[6, 1]
    pjm_serc_NE2030_2050 = resultsLine_NE2030_2050.iloc[1, 1] + resultsLine_NE2030_2050.iloc[7, 1]
    ne_ny_NE2030_2050 = resultsLine_NE2030_2050.iloc[2, 1] + resultsLine_NE2030_2050.iloc[8, 1]
    pjm_ny_NE2030_2050 = resultsLine_NE2030_2050.iloc[3, 1] + resultsLine_NE2030_2050.iloc[9, 1]
    pjm_miso_NE2030_2050 = resultsLine_NE2030_2050.iloc[4, 1] + resultsLine_NE2030_2050.iloc[10, 1]
    spp_miso_NE2030_2050 = resultsLine_NE2030_2050.iloc[5, 1] + resultsLine_NE2030_2050.iloc[11, 1]

    miso_serc_NE2040_2050 = resultsLine_NE2040_2050.iloc[0, 1] + resultsLine_NE2040_2050.iloc[6, 1]
    pjm_serc_NE2040_2050 = resultsLine_NE2040_2050.iloc[1, 1] + resultsLine_NE2040_2050.iloc[7, 1]
    ne_ny_NE2040_2050 = resultsLine_NE2040_2050.iloc[2, 1] + resultsLine_NE2040_2050.iloc[8, 1]
    pjm_ny_NE2040_2050 = resultsLine_NE2040_2050.iloc[3, 1] + resultsLine_NE2040_2050.iloc[9, 1]
    pjm_miso_NE2040_2050 = resultsLine_NE2040_2050.iloc[4, 1] + resultsLine_NE2040_2050.iloc[10, 1]
    spp_miso_NE2040_2050 = resultsLine_NE2040_2050.iloc[5, 1] + resultsLine_NE2040_2050.iloc[11, 1]

    miso_to_serc_NE2050_2050 = resultsLine_NE2050_1_2050.iloc[0, 1] + resultsLine_NE2050_2_2050.iloc[0, 1]
    pjm_to_serc_NE2050_2050 = resultsLine_NE2050_1_2050.iloc[1, 1] + resultsLine_NE2050_2_2050.iloc[1, 1]
    ne_to_ny_NE2050_2050 = resultsLine_NE2050_1_2050.iloc[2, 1] + resultsLine_NE2050_2_2050.iloc[2, 1]
    pjm_to_ny_NE2050_2050 = resultsLine_NE2050_1_2050.iloc[3, 1] + resultsLine_NE2050_2_2050.iloc[3, 1]
    pjm_to_miso_NE2050_2050 = resultsLine_NE2050_1_2050.iloc[4, 1] + resultsLine_NE2050_2_2050.iloc[4, 1]
    spp_to_miso_NE2050_2050 = resultsLine_NE2050_1_2050.iloc[5, 1] + resultsLine_NE2050_2_2050.iloc[5, 1]
    serc_to_miso_NE2050_2050 = resultsLine_NE2050_1_2050.iloc[6, 1] + resultsLine_NE2050_2_2050.iloc[6, 1]
    serc_to_pjm_NE2050_2050 = resultsLine_NE2050_1_2050.iloc[7, 1] + resultsLine_NE2050_2_2050.iloc[7, 1]
    ny_to_ne_NE2050_2050 = resultsLine_NE2050_1_2050.iloc[8, 1] + resultsLine_NE2050_2_2050.iloc[8, 1]
    ny_to_pjm_NE2050_2050 = resultsLine_NE2050_1_2050.iloc[9, 1] + resultsLine_NE2050_2_2050.iloc[9, 1]
    miso_to_pjm_NE2050_2050 = resultsLine_NE2050_1_2050.iloc[10, 1] + resultsLine_NE2050_2_2050.iloc[10, 1]
    miso_to_spp_NE2050_2050 = resultsLine_NE2050_1_2050.iloc[11, 1] + resultsLine_NE2050_2_2050.iloc[11, 1]

    miso_serc_NE2050_2050 = miso_to_serc_NE2050_2050 + serc_to_miso_NE2050_2050
    pjm_serc_NE2050_2050 = pjm_to_serc_NE2050_2050 + serc_to_pjm_NE2050_2050
    ne_ny_NE2050_2050 = ne_to_ny_NE2050_2050 + ny_to_ne_NE2050_2050
    pjm_ny_NE2050_2050 = pjm_to_ny_NE2050_2050 + ny_to_pjm_NE2050_2050
    pjm_miso_NE2050_2050 = pjm_to_miso_NE2050_2050 + miso_to_pjm_NE2050_2050
    spp_miso_NE2050_2050 = spp_to_miso_NE2050_2050 + miso_to_spp_NE2050_2050

    NZ_trans_cost_2050 = miso_serc_NZ_2050*p_serc_miso/1000+pjm_serc_NZ_2050*p_serc_pjm/1000\
                         +ne_ny_NZ_2050*p_ny_ne/1000 + pjm_ny_NZ_2050*p_ny_pjm/1000 \
                         + p_miso_pjm*pjm_miso_NZ_2050/1000 + spp_miso_NZ_2050*p_miso_spp/1000

    NE2020_trans_cost_2050 = miso_serc_NE2020_2050 * p_serc_miso / 1000 + pjm_serc_NE2020_2050 * p_serc_pjm / 1000 \
                             + ne_ny_NE2020_2050 * p_ny_ne/1000 + pjm_ny_NE2020_2050 * p_ny_pjm / 1000 \
                             + p_miso_pjm * pjm_miso_NE2020_2050 / 1000 + spp_miso_NE2020_2050 * p_miso_spp / 1000

    NE2030_trans_cost_2050 = miso_serc_NE2030_2050 * p_serc_miso / 1000 + pjm_serc_NE2030_2050 * p_serc_pjm / 1000 \
                             + ne_ny_NE2030_2050 * p_ny_ne/1000 + pjm_ny_NE2030_2050 * p_ny_pjm / 1000 \
                             + p_miso_pjm * pjm_miso_NE2030_2050 / 1000 + spp_miso_NE2030_2050 * p_miso_spp / 1000

    NE2040_trans_cost_2050 = miso_serc_NE2040_2050 * p_serc_miso / 1000 + pjm_serc_NE2040_2050 * p_serc_pjm / 1000 \
                             + ne_ny_NE2040_2050 * p_ny_ne/1000 + pjm_ny_NE2040_2050 * p_ny_pjm / 1000 \
                             + p_miso_pjm * pjm_miso_NE2040_2050 / 1000 + spp_miso_NE2040_2050 * p_miso_spp / 1000

    NE2050_trans_cost_2050 = miso_serc_NE2050_2050 * p_serc_miso / 1000 + pjm_serc_NE2050_2050 * p_serc_pjm / 1000 \
                             + ne_ny_NE2050_2050 * p_ny_ne/1000 + pjm_ny_NE2050_2050 * p_ny_pjm / 1000 \
                             + p_miso_pjm * pjm_miso_NE2050_2050 / 1000 + spp_miso_NE2050_2050 * p_miso_spp / 1000


    resultsLine_NZ_2030 = pd.read_csv(
        "C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Results_EI_NetZero_DACS2020_reference_TrueREFERENCE\\2030CO2Cap0\\CE\\" + 'vNl2030.csv')
    resultsLine_NE2020_2030 = pd.read_csv(
        "C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Results_EI_Negative-724_DACS2020NEin2020_reference_TrueREFERENCE\\2030CO2Cap-724\\CE\\" + 'vNl2030.csv')
    resultsLine_NE2030_2030 = pd.read_csv(
        "C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Results_EI_Negative-724_DACS2020NEin2030_reference_TrueREFERENCE\\2030CO2Cap-724\\CE\\" + 'vNl2030.csv')
    resultsLine_NE2040_2030 = pd.read_csv(
        "C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Results_EI_Negative-724_DACS2020NEin2040_reference_TrueREFERENCE\\2030CO2Cap-724\\CE\\" + 'vNl2030.csv')
    resultsLine_NE2050_2030 = pd.read_csv(
        "C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Results_EI_Negative-724_DACS2020NEin2050_reference_TrueREFERENCE\\2030CO2Cap-724\\CE\\" + 'vNl2030.csv')

    miso_serc_NZ_2030 = resultsLine_NZ_2030.iloc[0, 1] + resultsLine_NZ_2030.iloc[6, 1]
    pjm_serc_NZ_2030 = resultsLine_NZ_2030.iloc[1, 1] + resultsLine_NZ_2030.iloc[7, 1]
    ne_ny_NZ_2030 = resultsLine_NZ_2030.iloc[2, 1] + resultsLine_NZ_2030.iloc[8, 1]
    pjm_ny_NZ_2030 = resultsLine_NZ_2030.iloc[3, 1] + resultsLine_NZ_2030.iloc[9, 1]
    pjm_miso_NZ_2030 = resultsLine_NZ_2030.iloc[4, 1] + resultsLine_NZ_2030.iloc[10, 1]
    spp_miso_NZ_2030 = resultsLine_NZ_2030.iloc[5, 1] + resultsLine_NZ_2030.iloc[11, 1]

    miso_serc_NE2020_2030 = resultsLine_NE2020_2030.iloc[0, 1] + resultsLine_NE2020_2030.iloc[6, 1]
    pjm_serc_NE2020_2030 = resultsLine_NE2020_2030.iloc[1, 1] + resultsLine_NE2020_2030.iloc[7, 1]
    ne_ny_NE2020_2030 = resultsLine_NE2020_2030.iloc[2, 1] + resultsLine_NE2020_2030.iloc[8, 1]
    pjm_ny_NE2020_2030 = resultsLine_NE2020_2030.iloc[3, 1] + resultsLine_NE2020_2030.iloc[9, 1]
    pjm_miso_NE2020_2030 = resultsLine_NE2020_2030.iloc[4, 1] + resultsLine_NE2020_2030.iloc[10, 1]
    spp_miso_NE2020_2030 = resultsLine_NE2020_2030.iloc[5, 1] + resultsLine_NE2020_2030.iloc[11, 1]

    miso_serc_NE2030_2030 = resultsLine_NE2030_2030.iloc[0, 1] + resultsLine_NE2030_2030.iloc[6, 1]
    pjm_serc_NE2030_2030 = resultsLine_NE2030_2030.iloc[1, 1] + resultsLine_NE2030_2030.iloc[7, 1]
    ne_ny_NE2030_2030 = resultsLine_NE2030_2030.iloc[2, 1] + resultsLine_NE2030_2030.iloc[8, 1]
    pjm_ny_NE2030_2030 = resultsLine_NE2030_2030.iloc[3, 1] + resultsLine_NE2030_2030.iloc[9, 1]
    pjm_miso_NE2030_2030 = resultsLine_NE2030_2030.iloc[4, 1] + resultsLine_NE2030_2030.iloc[10, 1]
    spp_miso_NE2030_2030 = resultsLine_NE2030_2030.iloc[5, 1] + resultsLine_NE2030_2030.iloc[11, 1]

    miso_serc_NE2040_2030 = resultsLine_NE2040_2030.iloc[0, 1] + resultsLine_NE2040_2030.iloc[6, 1]
    pjm_serc_NE2040_2030 = resultsLine_NE2040_2030.iloc[1, 1] + resultsLine_NE2040_2030.iloc[7, 1]
    ne_ny_NE2040_2030 = resultsLine_NE2040_2030.iloc[2, 1] + resultsLine_NE2040_2030.iloc[8, 1]
    pjm_ny_NE2040_2030 = resultsLine_NE2040_2030.iloc[3, 1] + resultsLine_NE2040_2030.iloc[9, 1]
    pjm_miso_NE2040_2030 = resultsLine_NE2040_2030.iloc[4, 1] + resultsLine_NE2040_2030.iloc[10, 1]
    spp_miso_NE2040_2030 = resultsLine_NE2040_2030.iloc[5, 1] + resultsLine_NE2040_2030.iloc[11, 1]

    miso_serc_NE2050_2030 = resultsLine_NE2050_2030.iloc[0, 1] + resultsLine_NE2050_2030.iloc[6, 1]
    pjm_serc_NE2050_2030 = resultsLine_NE2050_2030.iloc[1, 1] + resultsLine_NE2050_2030.iloc[7, 1]
    ne_ny_NE2050_2030 = resultsLine_NE2050_2030.iloc[2, 1] + resultsLine_NE2050_2030.iloc[8, 1]
    pjm_ny_NE2050_2030 = resultsLine_NE2050_2030.iloc[3, 1] + resultsLine_NE2050_2030.iloc[9, 1]
    pjm_miso_NE2050_2030 = resultsLine_NE2050_2030.iloc[4, 1] + resultsLine_NE2050_2030.iloc[10, 1]
    spp_miso_NE2050_2030 = resultsLine_NE2050_2030.iloc[5, 1] + resultsLine_NE2050_2030.iloc[11, 1]

    NZ_trans_cost_2030 = miso_serc_NZ_2030 * p_serc_miso / 1000 + pjm_serc_NZ_2030 * p_serc_pjm / 1000 \
                         + ne_ny_NZ_2030 * p_ny_ne/1000 + pjm_ny_NZ_2030 * p_ny_pjm / 1000 \
                         + p_miso_pjm * pjm_miso_NZ_2030 / 1000 + spp_miso_NZ_2030 * p_miso_spp / 1000

    NE2020_trans_cost_2030 = miso_serc_NE2020_2030 * p_serc_miso / 1000 + pjm_serc_NE2020_2030 * p_serc_pjm / 1000 \
                             + ne_ny_NE2020_2030 * p_ny_ne/1000 + pjm_ny_NE2020_2030 * p_ny_pjm / 1000 \
                             + p_miso_pjm * pjm_miso_NE2020_2030 / 1000 + spp_miso_NE2020_2030 * p_miso_spp / 1000

    NE2030_trans_cost_2030 = miso_serc_NE2030_2030 * p_serc_miso / 1000 + pjm_serc_NE2030_2030 * p_serc_pjm / 1000 \
                             + ne_ny_NE2030_2030 * p_ny_ne/1000 + pjm_ny_NE2030_2030 * p_ny_pjm / 1000 \
                             + p_miso_pjm * pjm_miso_NE2030_2030 / 1000 + spp_miso_NE2030_2030 * p_miso_spp / 1000

    NE2040_trans_cost_2030 = miso_serc_NE2040_2030 * p_serc_miso / 1000 + pjm_serc_NE2040_2030 * p_serc_pjm / 1000 \
                             + ne_ny_NE2040_2030 * p_ny_ne/1000 + pjm_ny_NE2040_2030 * p_ny_pjm / 1000 \
                             + p_miso_pjm * pjm_miso_NE2040_2030 / 1000 + spp_miso_NE2040_2030 * p_miso_spp / 1000

    NE2050_trans_cost_2030 = miso_serc_NE2050_2030 * p_serc_miso / 1000 + pjm_serc_NE2050_2030 * p_serc_pjm / 1000 \
                             + ne_ny_NE2050_2030 * p_ny_ne/1000 + pjm_ny_NE2050_2030 * p_ny_pjm / 1000 \
                             + p_miso_pjm * pjm_miso_NE2050_2030 / 1000 + spp_miso_NE2050_2030 * p_miso_spp / 1000


    resultsLine_NZ_2040 = pd.read_csv(
        "C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Results_EI_NetZero_DACS2020_reference_TrueREFERENCE\\2040CO2Cap0\\CE\\" + 'vNl2040.csv')
    resultsLine_NE2020_2040 = pd.read_csv(
        "C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Results_EI_Negative-724_DACS2020NEin2020_reference_TrueREFERENCE\\2040CO2Cap-724\\CE\\" + 'vNl2040.csv')
    resultsLine_NE2030_2040 = pd.read_csv(
        "C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Results_EI_Negative-724_DACS2020NEin2030_reference_TrueREFERENCE\\2040CO2Cap-724\\CE\\" + 'vNl2040.csv')
    resultsLine_NE2040_2040 = pd.read_csv(
        "C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Results_EI_Negative-724_DACS2020NEin2040_reference_TrueREFERENCE\\2040CO2Cap-724\\CE\\" + 'vNl2040.csv')
    resultsLine_NE2050_2040 = pd.read_csv(
        "C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Results_EI_Negative-724_DACS2020NEin2050_reference_TrueREFERENCE\\2040CO2Cap-724\\CE\\" + 'vNl2040.csv')

    miso_serc_NZ_2040 = resultsLine_NZ_2040.iloc[0, 1] + resultsLine_NZ_2040.iloc[6, 1]
    pjm_serc_NZ_2040 = resultsLine_NZ_2040.iloc[1, 1] + resultsLine_NZ_2040.iloc[7, 1]
    ne_ny_NZ_2040 = resultsLine_NZ_2040.iloc[2, 1] + resultsLine_NZ_2040.iloc[8, 1]
    pjm_ny_NZ_2040 = resultsLine_NZ_2040.iloc[3, 1] + resultsLine_NZ_2040.iloc[9, 1]
    pjm_miso_NZ_2040 = resultsLine_NZ_2040.iloc[4, 1] + resultsLine_NZ_2040.iloc[10, 1]
    spp_miso_NZ_2040 = resultsLine_NZ_2040.iloc[5, 1] + resultsLine_NZ_2040.iloc[11, 1]

    miso_serc_NE2020_2040 = resultsLine_NE2020_2040.iloc[0, 1] + resultsLine_NE2020_2040.iloc[6, 1]
    pjm_serc_NE2020_2040 = resultsLine_NE2020_2040.iloc[1, 1] + resultsLine_NE2020_2040.iloc[7, 1]
    ne_ny_NE2020_2040 = resultsLine_NE2020_2040.iloc[2, 1] + resultsLine_NE2020_2040.iloc[8, 1]
    pjm_ny_NE2020_2040 = resultsLine_NE2020_2040.iloc[3, 1] + resultsLine_NE2020_2040.iloc[9, 1]
    pjm_miso_NE2020_2040 = resultsLine_NE2020_2040.iloc[4, 1] + resultsLine_NE2020_2040.iloc[10, 1]
    spp_miso_NE2020_2040 = resultsLine_NE2020_2040.iloc[5, 1] + resultsLine_NE2020_2040.iloc[11, 1]

    miso_serc_NE2030_2040 = resultsLine_NE2030_2040.iloc[0, 1] + resultsLine_NE2030_2040.iloc[6, 1]
    pjm_serc_NE2030_2040 = resultsLine_NE2030_2040.iloc[1, 1] + resultsLine_NE2030_2040.iloc[7, 1]
    ne_ny_NE2030_2040 = resultsLine_NE2030_2040.iloc[2, 1] + resultsLine_NE2030_2040.iloc[8, 1]
    pjm_ny_NE2030_2040 = resultsLine_NE2030_2040.iloc[3, 1] + resultsLine_NE2030_2040.iloc[9, 1]
    pjm_miso_NE2030_2040 = resultsLine_NE2030_2040.iloc[4, 1] + resultsLine_NE2030_2040.iloc[10, 1]
    spp_miso_NE2030_2040 = resultsLine_NE2030_2040.iloc[5, 1] + resultsLine_NE2030_2040.iloc[11, 1]

    miso_serc_NE2040_2040 = resultsLine_NE2040_2040.iloc[0, 1] + resultsLine_NE2040_2040.iloc[6, 1]
    pjm_serc_NE2040_2040 = resultsLine_NE2040_2040.iloc[1, 1] + resultsLine_NE2040_2040.iloc[7, 1]
    ne_ny_NE2040_2040 = resultsLine_NE2040_2040.iloc[2, 1] + resultsLine_NE2040_2040.iloc[8, 1]
    pjm_ny_NE2040_2040 = resultsLine_NE2040_2040.iloc[3, 1] + resultsLine_NE2040_2040.iloc[9, 1]
    pjm_miso_NE2040_2040 = resultsLine_NE2040_2040.iloc[4, 1] + resultsLine_NE2040_2040.iloc[10, 1]
    spp_miso_NE2040_2040 = resultsLine_NE2040_2040.iloc[5, 1] + resultsLine_NE2040_2040.iloc[11, 1]

    miso_serc_NE2050_2040 = resultsLine_NE2050_2040.iloc[0, 1] + resultsLine_NE2050_2040.iloc[6, 1]
    pjm_serc_NE2050_2040 = resultsLine_NE2050_2040.iloc[1, 1] + resultsLine_NE2050_2040.iloc[7, 1]
    ne_ny_NE2050_2040 = resultsLine_NE2050_2040.iloc[2, 1] + resultsLine_NE2050_2040.iloc[8, 1]
    pjm_ny_NE2050_2040 = resultsLine_NE2050_2040.iloc[3, 1] + resultsLine_NE2050_2040.iloc[9, 1]
    pjm_miso_NE2050_2040 = resultsLine_NE2050_2040.iloc[4, 1] + resultsLine_NE2050_2040.iloc[10, 1]
    spp_miso_NE2050_2040 = resultsLine_NE2050_2040.iloc[5, 1] + resultsLine_NE2050_2040.iloc[11, 1]

    NZ_trans_cost_2040 = miso_serc_NZ_2040 * p_serc_miso / 1000 + pjm_serc_NZ_2040 * p_serc_pjm / 1000 \
                         + ne_ny_NZ_2040 * p_ny_ne/1000 + pjm_ny_NZ_2040 * p_ny_pjm / 1000 \
                         + p_miso_pjm * pjm_miso_NZ_2040 / 1000 + spp_miso_NZ_2040 * p_miso_spp / 1000

    NE2020_trans_cost_2040 = miso_serc_NE2020_2040 * p_serc_miso / 1000 + pjm_serc_NE2020_2040 * p_serc_pjm / 1000 \
                             + ne_ny_NE2020_2040/1000 * p_ny_ne + pjm_ny_NE2020_2040 * p_ny_pjm / 1000 \
                             + p_miso_pjm * pjm_miso_NE2020_2040 / 1000 + spp_miso_NE2020_2040 * p_miso_spp / 1000

    NE2030_trans_cost_2040 = miso_serc_NE2030_2040 * p_serc_miso / 1000 + pjm_serc_NE2030_2040 * p_serc_pjm / 1000 \
                             + ne_ny_NE2030_2040 * p_ny_ne/1000 + pjm_ny_NE2030_2040 * p_ny_pjm / 1000 \
                             + p_miso_pjm * pjm_miso_NE2030_2040 / 1000 + spp_miso_NE2030_2040 * p_miso_spp / 1000

    NE2040_trans_cost_2040 = miso_serc_NE2040_2040 * p_serc_miso / 1000 + pjm_serc_NE2040_2040 * p_serc_pjm / 1000 \
                             + ne_ny_NE2040_2040 * p_ny_ne/1000 + pjm_ny_NE2040_2040 * p_ny_pjm / 1000 \
                             + p_miso_pjm * pjm_miso_NE2040_2040 / 1000 + spp_miso_NE2040_2040 * p_miso_spp / 1000

    NE2050_trans_cost_2040 = miso_serc_NE2050_2040 * p_serc_miso / 1000 + pjm_serc_NE2050_2040 * p_serc_pjm / 1000 \
                             + ne_ny_NE2050_2040 * p_ny_ne/1000 + pjm_ny_NE2050_2040 * p_ny_pjm / 1000 \
                             + p_miso_pjm * pjm_miso_NE2050_2040 / 1000 + spp_miso_NE2050_2040 * p_miso_spp / 1000

    NZ_trans_cost = np.array([NZ_trans_cost_2030, NZ_trans_cost_2040, NZ_trans_cost_2050])/1000000
    NE2050_trans_cost = np.array([NE2050_trans_cost_2030, NE2050_trans_cost_2040, NE2050_trans_cost_2050])/1000000
    NE2040_trans_cost = np.array([NE2040_trans_cost_2030, NE2040_trans_cost_2040, NE2040_trans_cost_2050])/1000000
    NE2030_trans_cost = np.array([NE2030_trans_cost_2030, NE2030_trans_cost_2040, NE2030_trans_cost_2050])/1000000
    NE2020_trans_cost = np.array([NE2020_trans_cost_2030, NE2020_trans_cost_2040, NE2020_trans_cost_2050])/1000000

    return (NZ_tot_cost, NE2050_tot_cost, NE2040_tot_cost, NE2030_tot_cost, NE2020_tot_cost,
            NZ_cap_cost, NE2050_cap_cost, NE2040_cap_cost, NE2030_cap_cost, NE2020_cap_cost,
            NZ_ope_cost, NE2050_ope_cost, NE2040_ope_cost, NE2030_ope_cost, NE2020_ope_cost,
            NE2020_aba_cost, NE2030_aba_cost, NE2040_aba_cost, NE2050_aba_cost,
            NZ_trans_cost, NE2050_trans_cost, NE2040_trans_cost, NE2030_trans_cost, NE2020_trans_cost)
