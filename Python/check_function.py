
import gdxpds
import pandas as pd
import matplotlib.pyplot as plt


time_step = 10
case_to_run = 1
gdx_basename = "_gams_py_gdb1"

m_dir = "C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\Python\\Results\\"
gdx_file = m_dir + gdx_basename + "_" + str(time_step) + "_years_case" + str(case_to_run) + ".gdx"


df = gdxpds.to_dataframes(gdx_file)

vN = df['vN']
vCoalCCS = vN['Level'][0]
vCC = vN['Level'][1]
vCCCCS = vN['Level'][2]
vNuclear = vN['Level'][3]
vBat = vN['Level'][4]
vH2 = vN['Level'][5]
vDAC = vN['Level'][6]
vWind = vN['Level'][7:61].sum()
vSolar = vN['Level'][61:].sum()

vGentech = df['vGentech']
vGentechTot = vGentech.groupby(['h'],sort=False).sum()
vGentechTot = vGentechTot['Level']
#vGentech = vGentech.groupby(['tech','h']).sum()

vGenNewCoalCCS = vGentech[0:696]
vGenNewCoalCCS = vGenNewCoalCCS.groupby(['h'],sort=False).sum()
vGenNewCoalCCS = vGenNewCoalCCS['Level']

vGenNewCC = vGentech[696:1392]
vGenNewCC = vGenNewCC.groupby(['h'],sort=False).sum()
vGenNewCC = vGenNewCC['Level']

vGenNewCCCCS = vGentech[1392:2088]
vGenNewCCCCS = vGenNewCCCCS.groupby(['h'],sort=False).sum()
vGenNewCCCCS = vGenNewCCCCS['Level']

vGenNewNuclear = vGentech[2088:2784]
vGenNewNuclear = vGenNewNuclear.groupby(['h'],sort=False).sum()
vGenNewNuclear = vGenNewNuclear['Level']

vGenNewBat = vGentech[2784:3480]
vGenNewBat = vGenNewBat.groupby(['h'],sort=False).sum()
vGenNewBat = vGenNewBat['Level']

vGenNewH2 = vGentech[3480:4176]
vGenNewH2 = vGenNewH2.groupby(['h'],sort=False).sum()
vGenNewH2 = vGenNewH2['Level']

vGenNewDAC = vGentech[4176:4872]
vGenNewDAC = vGenNewDAC.groupby(['h'],sort=False).sum()
vGenNewDAC = vGenNewDAC['Level']

vGenNewWind = vGentech[4872:42456]
vGenNewWind = vGenNewWind.groupby(['h'],sort=False).sum()
vGenNewWind = vGenNewWind['Level']

vGenNewSolar = vGentech[42456:]
vGenNewSolar = vGenNewSolar.groupby(['h'],sort=False).sum()
vGenNewSolar = vGenNewSolar['Level']

vGen = df['vGen']
vGen = vGen.groupby(['h'],sort=False).sum()
vGenTot = vGen['Level']
#vGenGT = vGen['Level'][0:696].reset_index(inplace = True)
#vGenWind = vGen['Level'][696:1392].reset_index(inplace = True)
#vGenOthers = vGen['Level'][1392:].reset_index(inplace = True)

vZannual = df['vZannual']
vZannual = vZannual['Level']/1000000

pDemand = df['pDemand']
pDemand = pDemand.groupby(['h'],sort=False).sum()
pDemand = pDemand['Value']

vShiftedDemand = df['vShiftedDemand']
vShiftedDemand = vShiftedDemand.groupby(['h'],sort=False).sum()
vShiftedDemand = vShiftedDemand['Level']
#vNetdemand = vShiftedDemand.add(pDemand,fill_value=0)
vNetdemand = vShiftedDemand + pDemand

# Plot demand shifting vs original demand:
#fig, ax = plt.subplots()
#plt.plot(pDemand[400:500], 'b', label='Original Demand', linewidth=0.5)
#plt.plot(pDemand, 'b', label='Original Demand', linewidth=0.5)
#plt.legend(loc="upper left")

#ax2 = ax.twinx()
#plt.plot(vShiftedDemand[400:500], 'r', label='Demand Shifter', linewidth=0.5)
#plt.plot(vNetdemand, 'r', label='Demand Shifter', linewidth=0.5)
#plt.legend(loc="upper right")

#plt.xlabel('Demand Shifter vs Original Demand')
#plt.ylabel('MWh')
#plt.show()
#fig.savefig('demand_shifting.png')

fig, ax = plt.subplots()
plt.plot(pDemand[459:483], 'b', label='Original Demand', linewidth=0.5)
#plt.plot(pDemand, 'b', label='Original Demand', linewidth=0.5)
plt.legend(loc="upper left")

plt.plot(vNetdemand[459:483], 'r', label='Demand after Shifting', linewidth=0.5)
#plt.plot(vNetdemand, 'r', label='Demand Shifter', linewidth=0.5)
plt.legend(loc="upper left")

plt.xlabel('Demand after Shifting vs Original Demand')
plt.ylabel('MWh')
plt.show()
fig.savefig('demand_after_shift.png')

# Plot storage battery usage vs original demand:
fig, ax = plt.subplots()
plt.plot(vNetdemand[459:483], 'b', label='Demand after Shifting', linewidth=0.5)
#plt.plot(pDemand, 'b', label='Original Demand', linewidth=0.5)
plt.legend(loc="upper left")

plt.plot(pDemand[459:483], 'k', label='Original Demand', linewidth=0.5)
#plt.plot(pDemand, 'b', label='Original Demand', linewidth=0.5)
plt.legend(loc="upper left")

ax2 = ax.twinx()
plt.plot(vGenNewBat[459:483]+vGenNewH2[459:483], 'r', label='Storage Generation', linewidth=0.5)
#plt.plot(vNetdemand, 'r', label='Demand Shifter', linewidth=0.5)
plt.legend(loc="upper right")

plt.plot(vGenNewDAC[459:483], 'g', label='DAC Generation', linewidth=0.5)
#plt.plot(vNetdemand, 'r', label='Demand Shifter', linewidth=0.5)
plt.legend(loc="upper right")

plt.xlabel('Storage+DAC Generation vs Demand')
plt.ylabel('MWh')
plt.show()
fig.savefig('gen_ref.png')

# Different types of gen vs demand:
fig, ax = plt.subplots()
plt.plot(pDemand[459:483], 'b', label='Original Demand', linewidth=0.5)
#plt.plot(pDemand, 'b', label='Original Demand', linewidth=0.5)
#plt.legend(loc="upper left")

plt.plot(vNetdemand[459:483], 'r', label='Demand after Shifting', linewidth=0.5)
#plt.plot(vNetdemand, 'r', label='Demand Shifter', linewidth=0.5)
#plt.legend(loc="upper left")

ax2 = ax.twinx()

plt.plot(vGenNewCCCCS[459:483], 'm', label='NGCC CCS', linewidth=1)
#plt.plot(vNetdemand, 'r', label='Demand Shifter', linewidth=0.5)
plt.legend(loc="upper left")

plt.plot(vGenNewWind[459:483]+vGenNewSolar[459:483], 'g', label='Renewable', linewidth=1)
#plt.plot(vNetdemand, 'r', label='Demand Shifter', linewidth=0.5)
plt.legend(loc="upper left")

plt.plot(vGenNewBat[459:483]+vGenNewH2[459:483], 'k', label='Storage', linewidth=1)
plt.legend(loc="upper left")

plt.xlabel('Generations vs Demand')
plt.ylabel('MWh')
plt.show()
fig.savefig('gens_vs_demand.png')

