import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import functions as f
import matplotlib.path as mpath
import matplotlib.lines as mlines
import matplotlib.patches as mpatches


# read in data

ISpath = '~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/Manuscript/Plotting/modeldata/ISchange/'
NoISpath = '~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/Manuscript/Plotting/modeldata/NoISchange/'


# 2D Optimal No IS change
# IS_2D optimal
twoD_optimal = pd.read_fwf(NoISpath + "2Druns/Powell2Dinversion.txt",header=None,infer_nrows=1000)
twoD_optimal = f.organizedata(twoD_optimal)

# 2D optimal IS change
IStwoD_optimal = pd.read_fwf(ISpath + "2Druns/ISPowell2Dinversion.txt",header=None,infer_nrows=1000)
IStwoD_optimal = f.organizedata(IStwoD_optimal)

both_1D = f.read1Dboth(NoISpath)
ISboth_1D = f.read1Dboth(ISpath)

# No IS change both constraints 1D inversion optimal. AD 0.1
both_1D_optimal = both_1D[1]
# IS change both constraints 1D inversion optimal. AD 1.0
ISboth_1D_optimal = ISboth_1D[10]

fan_before = [] # no need for fan before because CO2 only
fan_after = []
ISfan_before = []
ISfan_after = []
for i in range(1,14):
    fan_after.append(both_1D[1+i])
for i in range(1,6):
    ISfan_before.append(ISboth_1D[10-i])
for i in range(1,5):
    ISfan_after.append(ISboth_1D[10+i])
ISfan = ISfan_before + ISfan_after

colors_fan = ['#e41a1c','#ff7f00','#984ea3']
IScolors_fan = ['#ff7f00','#984ea3']
alpha = [1,1,1]
ISalpha = [1,1]
noIS = [both_1D[0],both_1D_optimal,twoD_optimal]
for i in range(len(fan_after)):
    noIS.append(fan_after[i])
    colors_fan.append('darkgray')
    alpha.append(0.5)

IS = [ISboth_1D_optimal,IStwoD_optimal]
for i in range(len(ISfan)):
    IS.append(ISfan[i])
    IScolors_fan.append('darkgray')
    ISalpha.append(0.5)


markers = []
for i in range(len(noIS)):
    markers.append('o')
for i in range(len(IS)):
    markers.append('s')

maxCO2 = both_1D[0].Ccum[200]
maxCcum = IStwoD_optimal.Ccum[200]
oldmaxCcum = twoD_optimal.Ccum[200]

for i in range(len(noIS)):
    noIS[i] = f.decompose(noIS[i])
for i in range(len(IS)):
    IS[i] = f.decompose(IS[i])
all = noIS + IS
allcolors = colors_fan + IScolors_fan
allalpha = alpha + ISalpha

fig,ax = plt.subplots()
plt.rcParams["font.weight"] = "bold"
for i in range(len(all)):
    # ax[0].plot(all[i].PgHCO3.sum(),all[i].PgCO2.sum(),alpha=allalpha[i],color = allcolors[i],marker='o',markeredgecolor='k', linewidth=2, markersize=10)
    ax.plot(all[i].Ccum[200],all[i].PgCO2.sum(),alpha=allalpha[i],color = allcolors[i],marker=markers[i],markeredgecolor='k', linewidth=2, markersize=10)
for axis in ['top','left','right','bottom']:
    ax.spines[axis].set_linewidth(3)
ax.tick_params(bottom=True, top=True, left=True, right=True)
ax.tick_params(axis='both', direction="in", length=7, width=3, color="black")

ax.hlines(y=maxCO2,linestyle='solid',color='k',xmin=-300, xmax=2750,zorder = 0,linewidth=3)
ax.vlines(x=maxCcum,linestyle='solid',color='k',ymin=-100, ymax=600,zorder=0,linewidth=3)
# ax.vlines(x=500,linestyle='dotted',color='k',ymin=-100, ymax=600,zorder=0,linewidth=3)

ax.annotate('', ha = 'center', va = 'bottom', xy = (1500,175),xytext = (750, 175),arrowprops = {'facecolor' : 'black'},zorder=4)
ax.text(700, 200,'change in \ninitial state',fontsize='large',style='italic')
ax.text(700, 105,'shifts ∆$^{14}$C \nconstraint',fontsize='large',style='italic')

ax.axvspan(maxCcum,2750, alpha=0.25, color='darkgray')
ax.axhspan(maxCO2,450, alpha=0.25, color='darkgray')
ax.text(500, 400,'Constrained by CO$_2$ budget',fontsize='medium',fontweight='bold')
ax.text(2470, 50,'Constrained by ∆$^{14}$C budget',rotation=270,fontsize='medium',fontweight='bold')


ax.set_xlabel('Total carbon added (PgC)',fontweight='bold',fontsize=10)
ax.set_ylabel('Total pure CO$_2$ added (PgC)',fontweight='bold',fontsize=10)
ax.set_ylim(-50,450)
ax.set_xlim(-250,2750)

noISlegend = mlines.Line2D([], [], color='white',markeredgecolor='k', marker='o',linestyle='None', markersize=10, label='No change in initial state')
ISlegend = blue_line = mlines.Line2D([], [], color='white',markeredgecolor='k', marker='s',linestyle='None', markersize=10, label='Change in initial state')

ax.legend(handles=[noISlegend,ISlegend],loc='lower left',frameon=True)
plt.show()
# plt.savefig('Figures/CO2vsCarbon.pdf')
