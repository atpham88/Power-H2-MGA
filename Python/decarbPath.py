import numpy as np
import matplotlib.pyplot as plt

startYear = 2020
endYear = 2050
co2Ems2020 = 1274.06
co2EmsCapInFinalYear = -724.6662647

# Net-Zero System:
NZ_2020 = co2Ems2020 - (co2Ems2020-0)/3*0
NZ_2030 = co2Ems2020 - (co2Ems2020-0)/3*1
NZ_2040 = co2Ems2020 - (co2Ems2020-0)/3*2
NZ_2050 = co2Ems2020 - (co2Ems2020-0)/3*3

NZ = np.array([NZ_2020, NZ_2030, NZ_2040, NZ_2050])

# Negative System in 2020:
NEin2020_2020 = co2Ems2020 - (co2Ems2020-co2EmsCapInFinalYear)/3*0
NEin2020_2030 = co2Ems2020 - (co2Ems2020-co2EmsCapInFinalYear)/3*1
NEin2020_2040 = co2Ems2020 - (co2Ems2020-co2EmsCapInFinalYear)/3*2
NEin2020_2050 = co2Ems2020 - (co2Ems2020-co2EmsCapInFinalYear)/3*3

NEin2020 = np.array([NEin2020_2020, NEin2020_2030, NEin2020_2040, NEin2020_2050])

# Negative System in 2030:
NEin2030_2020 = NZ_2020
NEin2030_2030 = NZ_2030
NEin2030_2040 = NEin2030_2030 - (NEin2030_2030-co2EmsCapInFinalYear)/2
NEin2030_2050 = NEin2030_2030 - (NEin2030_2030-co2EmsCapInFinalYear)/2*2

NEin2030 = np.array([NEin2030_2020, NEin2030_2030, NEin2030_2040, NEin2030_2050])

# Negative System in 2040:
NEin2040_2020 = NZ_2020
NEin2040_2030 = NZ_2030
NEin2040_2040 = NZ_2040
NEin2040_2050 = NEin2040_2040 - (NEin2040_2040-co2EmsCapInFinalYear)

NEin2040 = np.array([NEin2040_2020, NEin2040_2030, NEin2040_2040, NEin2040_2050])

# Negative System in 2050:
NEin2050_2020 = NZ_2020
NEin2050_2030 = NZ_2030
NEin2050_2040 = NZ_2040
NEin2050_2050 = NZ_2050

NEin2050 = np.array([NEin2050_2020, NEin2050_2030, NEin2050_2040, NEin2050_2050, co2EmsCapInFinalYear])

# Plot decarbonization pathway:

fig, ax = plt.subplots(figsize=(10, 6),tight_layout=True)

x = np.array([2020, 2030, 2040, 2050])
plt.axhline(y=0, color='lightgrey', linestyle='-', alpha=0.3)
plt.axvline(x=2020, color='lightgrey', linestyle=':', alpha=0.5)
plt.axvline(x=2030, color='lightgrey', linestyle=':', alpha=0.5)
plt.axvline(x=2040, color='lightgrey', linestyle=':', alpha=0.5)
plt.axvline(x=2050, color='lightgrey', linestyle=':', alpha=0.5)
plt.plot(x, NZ, 'o-', linewidth=2, label="NZS", color='darkgrey', alpha=0.7)
plt.plot(x, NZ, 'o-', linewidth=2, label="NES in 2050", linestyle='--', color='saddlebrown', alpha=0.7)
ax.vlines([2050], 0, co2EmsCapInFinalYear, linestyles='--',linewidth=2, color='saddlebrown', alpha=0.7)
plt.plot(x, NEin2040, 'o-', linewidth=2, label="NES in 2040", linestyle='--', color='lightpink')
plt.plot(x, NEin2030, 'o-', linewidth=2, label="NES in 2030", linestyle='--', color='deepskyblue', alpha=0.7)
plt.plot(x, NEin2020, 'o-', linewidth=2, label="NES in 2020", linestyle='--', color='olivedrab', alpha=0.7)

# Annotation:
ax.text(2020-0.7,NZ_2020*0.92, str(int(np.around(co2Ems2020, decimals=0))), va='center', fontsize=12)
ax.text(2030-0.6,NZ_2030*1.09, str(int(np.around(NZ_2030, decimals=0))), va='center', fontsize=12)
ax.text(2030-0.6,NEin2020_2030*0.85, str(int(np.around(NEin2020_2030, decimals=0))), va='center', fontsize=12)
ax.text(2040-0.6,NZ_2040*1.17, str(int(np.around(NZ_2040, decimals=0))), va='center', fontsize=12)
ax.text(2040-0.4,NEin2030_2040*2.2, str(int(np.around(NEin2030_2040, decimals=0))), va='center', fontsize=12)
ax.text(2040-0.6,NEin2020_2040*2.5, str(int(np.around(NEin2020_2040, decimals=0))), va='center', fontsize=12)
ax.text(2050-0.2,NZ_2050+80, str(int(np.around(NZ_2050, decimals=0))), va='center', fontsize=12)
ax.text(2050-2,co2EmsCapInFinalYear-10, str(int(np.around(co2EmsCapInFinalYear, decimals=0))), va='center', fontsize=12)

# customization
plt.xticks([2020, 2030, 2040, 2050],fontsize=17)
plt.yticks(fontsize=17)
plt.xlabel('Years', fontsize=20)
plt.ylabel('$CO_2$ Emission Cap (Million Tons)', fontsize=20)
plt.legend(fontsize=17,loc='upper right')
plt.show()
fig.savefig('C:\\Users\\atpha\\Documents\\Postdocs\\'
            'Projects\\NETs\\Draft\\decarb_path.png', dpi=300)