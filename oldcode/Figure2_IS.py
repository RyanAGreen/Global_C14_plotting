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

#CO2 observations
CO2obs = pd.read_csv('~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/observations/CO2data1.txt',sep='\t')
CO2obs['year'] = CO2obs['year'].apply(f.fix)
CO2obs['Crate'] = 0
CO2obs['Ccum'] = 0



#d14C observations
d14C = pd.read_csv("~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/observations/IntCalSmoothed.txt",header=None)
D14C = d14C.rename(columns = {0:'year',3:'D14C'})
D14C['year'] = D14C['year'].apply(f.fix)
D14C['Crate'] = 0
D14C['Ccum'] = 0

#control should be same as Hain 2014
control = pd.read_fwf(NoISpath + "control.txt",header=None,infer_nrows=1000)
control = f.organizedata(control)

IScontrol = pd.read_fwf(ISpath + "IScontrol.txt",header=None,infer_nrows=1000)
IScontrol = f.organizedata(IScontrol)

# 2D Optimal No IS change (0.04 % of minimization) improvement of 18%, 0.49
# IS_2D optimal
twoD_optimal = pd.read_fwf(NoISpath + "2Druns/Powell2Dinversion.txt",header=None,infer_nrows=1000)
twoD_optimal = f.organizedata(twoD_optimal)

# 2D optimal IS change (0.1 % of minimization) improvement of  58%, 1.16
IStwoD_optimal = pd.read_fwf(ISpath + "2Druns/ISPowell2Dinversion.txt",header=None,infer_nrows=1000)
IStwoD_optimal = f.organizedata(IStwoD_optimal)

both_1D = f.read1Dboth(NoISpath)
ISboth_1D = f.read1Dboth(ISpath)

CO2_only = both_1D[0]

ISCO2_only = ISboth_1D[0]

fan_before = [] # no need for fan before because 0.1
fan_after = []
ISfan_before = []
ISfan_after = []
for i in range(1,5):
    fan_after.append(both_1D[1+i])
    ISfan_before.append(ISboth_1D[10-i])
    ISfan_after.append(ISboth_1D[10+i])


# No IS change both constraints 1D inversion optimal. AD 0.4
both_1D_optimal = both_1D[1]
# IS change both constraints 1D inversion optimal. AD 1.1
ISboth_1D_optimal = ISboth_1D[10]

#colors
colors_fan = ['darkgray','darkgray','darkgray','darkgray','#a65628','black','#e41a1c','#ff7f00','#984ea3']
IScolors_fan = ['darkgray','darkgray','darkgray','darkgray','darkgray','darkgray','darkgray','darkgray','#a65628','black','#e41a1c','#ff7f00','#984ea3']
colors = ['#a65628','black','#e41a1c','#ff7f00','#984ea3']
colors2 = ['white','white','#e41a1c','#ff7f00','#984ea3']

#only difference is the observations so I can plot in loop
D14C_atm = [D14C,control,CO2_only,both_1D_optimal,twoD_optimal]
IS_D14C_atm = [D14C,control,ISCO2_only,ISboth_1D_optimal,IStwoD_optimal]
CO2_atm = [fan_after[0],fan_after[1],fan_after[2],fan_after[3],CO2obs,control,CO2_only,both_1D_optimal,twoD_optimal]
IS_CO2_atm = [ISfan_before[0],ISfan_before[1],ISfan_before[2],ISfan_before[3],ISfan_after[0],ISfan_after[1],ISfan_after[2],ISfan_after[3],CO2obs,control,ISCO2_only,ISboth_1D_optimal,IStwoD_optimal]



linestyles_fan = ['-','-','-','-','-','--','-','-','-']
ISlinestyles_fan = ['-','-','-','-','-','-','-','-','-','--','-','-','-']
linewidths_fan = ['2','2','2','2','2.5','2.5','2.5','2.5','2.5']
ISlinewidths_fan = ['2','2','2','2','2','2','2','2','2.5','2.5','2.5','2.5','2.5']
linestyles = ['-','--','-','-','-']
linewidths = ['2.5','2.5','2.5','2.5','2.5']
linewidths2 = ['2.5','2.5','2.5','2.5','2.5']
alpha = [0.5,0.5,0.5,0.5,1,1,1,1,1]
ISalpha = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,1,1,1,1,1]
alpha2 = [0,0,1,1,1]
colorsAD = f.ADcolors(twoD_optimal)
IScolorsAD = f.ADcolors(IStwoD_optimal)

# make figure
fig, ax = plt.subplots(3,sharex=True,sharey='row',figsize=(8.5,8))
ax=ax.flatten()

plt.rcParams["font.weight"] = "bold"

for i in range(len(IS_D14C_atm)):
    ax[0].plot(IS_D14C_atm[i].year,IS_D14C_atm[i].D14C,linewidth=linewidths[i],ls=linestyles[i],color = colors[i])

for i in range(len(IS_CO2_atm)):
    # plot atmospheric CO2 for IS change
    ax[1].plot(IS_CO2_atm[i].year,IS_CO2_atm[i].CO2,linewidth=ISlinewidths_fan[i],ls=ISlinestyles_fan[i],color = IScolors_fan[i],alpha = ISalpha[i])

# ax[4].plot(D14C_atm[4].year,D14C_atm[4].Crate,linewidth=linewidths2[4],ls=linestyles[4],color = colors2[4])
# ax[5].plot(IS_D14C_atm[4].year,IS_D14C_atm[4].Crate,linewidth=linewidths2[4],ls=linestyles[4],color = colors2[4])
fir,sec,thi = f.binning(IStwoD_optimal)

ax[2].bar(IStwoD_optimal.year, IStwoD_optimal.Crate,width=0.1, color = IScolorsAD,zorder=2)
ax[2].plot(IStwoD_optimal.year, IStwoD_optimal.Crate,color='#984ea3',lw=2.5, zorder=3)
ax[2].text(15.36, 0.76,"{:0.2f} PgC \n{:0.2f} ALK:DIC ratio".format(fir[0],fir[1]),fontweight='bold')
ax[2].text(10.1, 0.9,"{:0.2f} PgC \n{:0.2f} ALK:DIC ratio".format(sec[0],sec[1]),fontweight='bold')
ax[2].text(2.5, 0.26,"{:0.2f} PgC \n{:0.2f} ALK:DIC ratio".format(thi[0],thi[1]),fontweight='bold')
#ax[5].bar(IStwoD_optimal.year, IStwoD_optimal.Crate,width=0.1,color = IScolorsAD,zorder=2)

for i in range(3):
    for axis in ['top','left','right','bottom']:
        ax[i].spines[axis].set_linewidth(3)
    ax[i].tick_params(bottom=True, top=True, left=True, right=True)
    ax[i].tick_params(axis='both', direction="in", length=7, width=3, color="black")
    ax[i].axvspan(11.6, 12.9, alpha=0.4, color='darkgray')
    ax[i].axvspan(14.5, 18, alpha=0.4, color='darkgray')
    ax[i].grid()
    ax[i].tick_params(labelbottom=False, labeltop=False, labelleft=False, labelright=True)
ax[2].tick_params(labelbottom=True, labeltop=False, labelleft=False, labelright=True)

for i in range(1):
    ax[i].text(18.5,515,'LGM',fontsize='x-small')
    ax[i].text(15.8,515,'HS1',fontsize='x-small')
    ax[i].text(11.9,515,'YD',fontsize='x-small')
    ax[i].text(4.9,515,'Holocene',fontsize='x-small')

ax[2].set_xlim(0,20)
#ax[5].set_xlim(0,20)
ax[1].set_ylim(175,325)
#ax1.set_ylim(175,300)
ax[0].set_ylim(-75,500)
#ax[1].set_ylim(-50,500)
# ax[0].set_title('No change in IS',fontweight='bold',pad=20)
# ax[1].set_title('Change in IS',fontweight='bold',pad=20)

# making legends
control_legend = mlines.Line2D([], [], color='black', linestyle ='dashed',lw=2.5,label = 'Control run')
observations_legend = mlines.Line2D([], [], color='#a65628', linestyle ='solid',lw=2.5,label = 'Observations')
CO2only_legend = mlines.Line2D([], [], color='#e41a1c', linestyle ='solid',lw=2.5,label = '1D inversion CO$_2$ only')
oneD_legend = mlines.Line2D([], [], color='#ff7f00', linestyle ='solid',lw=2.5,label = '1D inversion optimal')
twoD_legend = mlines.Line2D([], [], color='#984ea3', linestyle ='solid',lw=2.5,label = '2D inversion')
oneDrange_legend = mlines.Line2D([], [], color='darkgray', linestyle ='solid',alpha=0.5,lw=2.5,label = '1D inversion ensemble')
CO2 = mpatches.Patch(color='#018571', label='CO$_2$ (ALK:DIC < 0.7)')
bicarb = mpatches.Patch(color='#80cdc1', label='HCO$_3$$^{-}$ (0.7 < ALK:DIC < 1.3)')
carb = mpatches.Patch(color='#dfc27d', label='H$_2$CO$_{3}$$^{2-}$ (ALK:DIC > 1.3)')


ax[0].legend(handles=[control_legend,observations_legend,CO2only_legend,oneD_legend,oneDrange_legend,twoD_legend],ncol=2,frameon=True)
ax[2].legend(handles=[CO2,bicarb,carb],loc='best',frameon=True)

# labeling
#ax0.set_ylabel('Atmospheric CO$_2$ (ppm)',fontweight='bold',fontsize=14)
ax[1].set_ylabel('Atmospheric CO$_2$ \n (ppm)',fontweight='bold',fontsize=10)
ax[0].set_ylabel('Atmospheric ∆$^{14}$C \n (‰)',fontweight='bold',fontsize=10)
#ax[1].set_ylabel('Atmospheric ∆$^{14}$C (‰)',fontweight='bold',fontsize=14)
#ax[3].set_ylabel('Rate of carbon addition (pgC/yr)',fontweight='bold',fontsize=14)
ax[2].set_ylabel('Rate of addition \n (pgC/yr)',fontweight='bold',fontsize=10)
# ax5.set_ylabel('Total carbon added \n (pgC)',fontweight='bold',fontsize=10)

ax[2].set_xlabel('Calendar age (kyr BP)',fontweight='bold',fontsize=10)
#ax[5].set_xlabel('Calendar age (ka BP)',fontweight='bold',fontsize=10)
#
#
#plt.tight_layout()
plt.savefig('Figures/Figure2_IS.pdf')
#plt.show()
