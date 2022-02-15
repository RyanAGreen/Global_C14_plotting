import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#cd ~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/Manuscript/Plotting/
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
CO2obs = CO2obs.iloc[:-2]

#d14C observations
d14C = pd.read_csv("~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/observations/D14Cdata.txt",header=None,sep='\t')
D14C = d14C.rename(columns = {0:'year',1:'D14C'})
D14C['year'] = D14C['year'].apply(f.fix)
D14C['Crate'] = 0
D14C['Ccum'] = 0

#control should be same as Hain 2014
control = pd.read_fwf(NoISpath + "control.txt",header=None,infer_nrows=1000)
control = f.organizedata(control)

#colors
colors = ['#a65628','black']

#only difference is the observations so I can plot in loop
D14C_atm = [D14C,control]
CO2_atm = [CO2obs,control]

linestyles = ['-','--']
linewidths = ['2.5','2.5']
labels = ['Observations','Control run']

# make figure
fig, ax = plt.subplots(2,sharex=True,sharey='row',figsize=(8,5))

plt.rcParams["font.weight"] = "bold"

for i in range(len(D14C_atm)):
    ax[0].plot(D14C_atm[i].year,D14C_atm[i].D14C,linewidth=linewidths[i],ls=linestyles[i],color = colors[i],label=labels[i])

ax[0].fill_between(D14C_atm[0].year,D14C_atm[0].D14C, D14C_atm[1].D14C,color='#ffff99',alpha=0.6,zorder = 2,label='Mismatch')
ax[0].legend(loc='upper left',frameon=False)

for i in range(len(CO2_atm)):
    # plot atmospheric CO2 for no IS change
    ax[1].plot(CO2_atm[i].year,CO2_atm[i].CO2,linewidth=linewidths[i],ls=linestyles[i],color = colors[i])

ax[1].fill_between(CO2_atm[0].year,CO2_atm[0].CO2, CO2_atm[1].CO2,color='#ffff99',alpha=0.6,zorder = 2,label='Mismatch')

for i in range(2):
    for axis in ['top','left','right','bottom']:
        ax[i].spines[axis].set_linewidth(3)
    ax[i].tick_params(bottom=True, top=True, left=True, right=True)
    ax[i].tick_params(axis='both', direction="in", length=7, width=3, color="black")
    ax[i].axvspan(11.6, 12.9, alpha=0.4, color='darkgray')
    ax[i].axvspan(14.5, 18, alpha=0.4, color='darkgray')
    ax[i].grid()
# for i in range(4,6):
#     for axis in ['top','left','right','bottom']:
#         ax[i].spines[axis].set_linewidth(3)
#     ax[i].tick_params(bottom=True, top=True, left=True, right=True)
#     ax[i].tick_params(axis='both', direction="in", length=7, width=3, color="black")
#     ax[i].axvspan(11.6, 12.9, alpha=0.4, color='darkgray',zorder=0)
#     ax[i].axvspan(14.5, 18, alpha=0.4, color='darkgray',zorder=0)
#     ax[i].grid()

for i in range(1):
    ax[i].text(18.5,515,'LGM',fontsize='x-small')
    ax[i].text(15.8,515,'HS1',fontsize='x-small')
    ax[i].text(11.9,515,'YD',fontsize='x-small')
    ax[i].text(4.9,515,'Holocene',fontsize='x-small')

ax[1].set_xlim(0,20)
ax[1].set_ylim(175,325)
ax[0].set_ylim(-75,500)


# making legends
control_legend = mlines.Line2D([], [], color='black', linestyle ='dashed',lw=2.5,label = 'Control run')
observations_legend = mlines.Line2D([], [], color='#a65628', linestyle ='solid',lw=2.5,label = 'Observations')
#ax[0].legend(handles=[control_legend,observations_legend],frameon=False)

# labeling
ax[1].set_ylabel('Atmospheric CO$_2$ \n (ppm)',fontweight='bold',fontsize=10)
ax[0].set_ylabel('Atmospheric ∆$^{14}$C \n (‰)',fontweight='bold',fontsize=10)

ax[1].set_xlabel('Calendar age (kyr BP)',fontweight='bold',fontsize=10)

#plt.tight_layout()
plt.savefig('Figures/Control.pdf')
#plt.show()
