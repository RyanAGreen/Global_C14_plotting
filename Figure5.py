import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import functions as f

ISpath = '~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/Manuscript/Plotting/modeldata/ISchange/'
NoISpath = '~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/Manuscript/Plotting/modeldata/NoISchange/'


control = pd.read_fwf(NoISpath + "control.txt",header=None,infer_nrows=1000)
control = f.organizedata(control)
#
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
both_1D[0]
# 1D D14C inversion
# improvement of .82%, 0.8
oneDoptimal = both_1D[1]
# improvement of 53%, 1.1
ISoneDoptimal = ISboth_1D[10]
#

df = control
all = (df.NPacCSH + df.SPacCSH + df.AtlCSH + df.IndCSH)/4
df1 = ISboth_1D[0]
all1 = (df1.NPacCSH + df1.SPacCSH + df1.AtlCSH + df1.IndCSH)/4
df2 = IStwoD_optimal
all2 = (df2.NPacCSH + df2.SPacCSH + df2.AtlCSH + df2.IndCSH)/4
fig,ax = plt.subplots(1,2,figsize=(8,4),sharey=True)
plt.rcParams["font.weight"] = "bold"

#thickening axis
for axis in ['top','left','right','bottom']:
    for i in range(2):
        ax[i].spines[axis].set_linewidth(3)

# ax1 = ax.twinx()
# ax.plot(df.year,df.AtlFdiss,label='Atl')
# ax.plot(df.year,df.IndFdiss,label='Ind')
# ax.plot(df.year,df.SPacFdiss,label='Spac')
# ax.plot(df.year,df.NPacFdiss,label='Npac')
# ax.plot(df.year,df.AtlCSH,label='Atl')
# ax.plot(df.year,df.IndCSH,label='Ind')
# ax.plot(df.year,df.SPacCSH,label='Spac')
# ax.plot(df.year,df.NPacCSH,label='Npac')

# ax.plot(df1.year,all1,label='1D IS change')
ax[1].plot(df2.year,all2,color='#984ea3',linestyle='-',lw=3.5,label='2D inversion with IS change')

ax[0].plot(df2.year,df2.NPacCSH,color='#984ea3',linestyle='-',lw=3.5)
ax[0].plot(df.year,df.NPacCSH,'--k',lw=3.5)
ax[1].plot(df.year,all,'--k',label='Control run',lw=3.5)

for i in range(2):
    ax[i].set_xlabel('Calendar age (kyr BP)',fontweight='bold')
    ax[i].axvspan(11.6, 12.9, alpha=0.4, color='darkgray',zorder=0)
    ax[i].axvspan(14.5, 18, alpha=0.4, color='darkgray',zorder=0)
    ax[i].text(18.5,3.05,'LGM',fontsize='x-small')
    ax[i].text(15.9,3.05,'HS1',fontsize='x-small')
    ax[i].text(11.9,3.05,'YD',fontsize='x-small')
    ax[i].text(4.9,3.05,'Holocene',fontsize='x-small')
    ax[i].tick_params(bottom=True, top=True, left=True, right=True)
    ax[i].tick_params(axis='both', direction="in", length=7, width=3, color="black")
    ax[i].grid()

ax[0].annotate('', ha = 'center', va = 'bottom', xy = (2.5,5),xytext = (2.5, 4.25),arrowprops = {'facecolor' : 'black'},zorder=4)
ax[0].text(2.85, 4.7,'carbonate\npreservation',fontsize='small')
ax[0].invert_yaxis()
# ax1.plot(df.year,df.TotalALK,'--k',label='control run Alk')
# ax1.plot(df1.year,df1.TotalALK,'--k',label='1D IS change Alk')
# ax1.plot(df2.year,df2.TotalALK,color='#984ea3',linestyle='--',label='2D IS change Alk')
# ax1.invert_yaxis()
ax[0].set_ylabel('CSH (m)',fontweight='bold')


ax[0].set_title('North Pacific',fontweight='bold',pad=15)
ax[1].set_title('Global',fontweight='bold',pad=15)
ax[1].legend()

names = ['a)','b)']
for i in range(2):
    ax[i].text(1,5.3,names[i],fontweight='bold',fontsize=10)

plt.tight_layout()
# plt.show()
plt.savefig('Figures/Figure5.pdf')
