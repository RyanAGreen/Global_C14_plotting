import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.path as mpath
import matplotlib.lines as mlines
import functions as f

ISpath = '~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/Manuscript/Plotting/modeldata/ISchange/'
NoISpath = '~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/Manuscript/Plotting/modeldata/NoISchange/'

#control should be same as Hain 2014
control = pd.read_fwf(NoISpath + "control.txt",header=None,infer_nrows=1000)
control = f.organizedata(control)
controlscore,controlmean = f.score(control,control)

IScontrol = pd.read_fwf(ISpath + "IScontrol.txt",header=None,infer_nrows=1000)
IScontrol = f.organizedata(IScontrol)
IScontrolscore,IScontrolmean = f.score(IScontrol,IScontrol)

# 2D Optimal No IS change (0.04 % of minimization)
twoD_optimal = pd.read_fwf(NoISpath + "2Druns/2Doptimal.txt",header=None,infer_nrows=1000)
twoD_optimal = f.organizedata(twoD_optimal)

# 2D optimal IS change (0.1 % of minimization)
IStwoD_optimal = pd.read_fwf(ISpath + "2Druns/IS_2Doptimal.txt",header=None,infer_nrows=1000)
IStwoD_optimal = f.organizedata(IStwoD_optimal)

D14C1D = f.readD14C(NoISpath)
ISD14C1D = f.readD14C(ISpath)
CO21D = f.readCO2(NoISpath)
ISCO21D = f.readCO2(ISpath)

totalerrorscore = []
D14Cerrorscore = []
CO2errorscore = []
Ccum1 = []

IStotalerrorscore = []
ISD14Cerrorscore = []
ISCO2errorscore = []
ISCcum1 = []
for i in range(19):
    # find total error values
    totalerrorscore.append(f.score(D14C1D[i],control)[0])
    IStotalerrorscore.append(f.score(ISD14C1D[i],IScontrol)[0])

    # find D14C error values
    D14Cerrorscore.append(f.D14Cscore(D14C1D[i],control))
    ISD14Cerrorscore.append(f.D14Cscore(ISD14C1D[i],IScontrol))

    # find CO2 error values
    CO2errorscore.append(f.CO2score(D14C1D[i],control))
    ISCO2errorscore.append(f.CO2score(ISD14C1D[i],IScontrol))

    # find cum carbon
    Ccum1.append(f.max(D14C1D[i]))
    ISCcum1.append(f.max(ISD14C1D[i]))

# since CO2 inversion only goes to 1.1 before breaking
totalerrorscore_CO2 = []
D14Cerrorscore_CO2 = []
CO2errorscore_CO2 = []
Ccum1_CO2 = []

IStotalerrorscore_CO2 = []
ISD14Cerrorscore_CO2 = []
ISCO2errorscore_CO2 = []
ISCcum1_CO2 = []
for i in range(12):
    totalerrorscore_CO2.append(f.score(CO21D[i],control)[0])
    IStotalerrorscore_CO2.append(f.score(ISCO21D[i],IScontrol)[0])

    # find D14C error values
    D14Cerrorscore_CO2.append(f.D14Cscore(CO21D[i],control))
    ISD14Cerrorscore_CO2.append(f.D14Cscore(ISCO21D[i],IScontrol))

    # find CO2 error values
    CO2errorscore_CO2.append(f.CO2score(CO21D[i],control))
    ISCO2errorscore_CO2.append(f.CO2score(ISCO21D[i],IScontrol))

    # find cum carbon
    Ccum1_CO2.append(f.max(CO21D[i]))
    ISCcum1_CO2.append(f.max(ISCO21D[i]))


# calculate scores and cum carbon for 2Doptimal runs

# total score
twoD_totalscore,twoD_totalratio = f.score(twoD_optimal,control)
IStwoD_totalscore,IStwoD_totalratio = f.score(IStwoD_optimal,IScontrol)
# D14C score
twoD_D14Cscore = f.D14Cscore(twoD_optimal,control)
IStwoD_D14Cscore = f.D14Cscore(IStwoD_optimal,IScontrol)
# CO2 scores
twoD_CO2score = f.CO2score(twoD_optimal,control)
IStwoD_CO2score = f.CO2score(IStwoD_optimal,IScontrol)
# Cumlative carbon
twoD_Ccum = f.max(twoD_optimal)
IStwoD_Ccum= f.max(IStwoD_optimal)

#create list so I can plot in a row
twoDlist = [twoD_CO2score,twoD_CO2score,twoD_D14Cscore,twoD_D14Cscore,twoD_totalscore,twoD_totalscore,twoD_Ccum,twoD_Ccum]
IStwoDlist = [IStwoD_CO2score,IStwoD_CO2score,IStwoD_D14Cscore,IStwoD_D14Cscore,IStwoD_totalscore,IStwoD_totalscore,IStwoD_Ccum,IStwoD_Ccum]

fig,ax = plt.subplots(4,2,figsize=(12,15),sharex='col',sharey='row')
ax=ax.flatten()
# plot D14C inversion
for i in range(19):
    # plot noIS change
    ax[0].plot(D14C1D[i].ADratio[0],CO2errorscore[i],color='#4daf4a',marker = 'o', linewidth=2, markersize=10)
    ax[2].plot(D14C1D[i].ADratio[0],D14Cerrorscore[i],color='#4daf4a',marker = 'o', linewidth=2, markersize=10)
    ax[4].plot(D14C1D[i].ADratio[0],totalerrorscore[i],color='#4daf4a',marker = 'o', linewidth=2, markersize=10)
    ax[6].plot(D14C1D[i].ADratio[0],Ccum1[i],marker = 'o',color='#4daf4a', linewidth=2, markersize=10)
    # plot IS ISchange
    ax[0].plot(ISD14C1D[i].ADratio[0],ISCO2errorscore[i],color = '#377eb8',marker = 'o', linewidth=2, markersize=10)
    ax[2].plot(ISD14C1D[i].ADratio[0],ISD14Cerrorscore[i],color = '#377eb8',marker = 'o', linewidth=2, markersize=10)
    ax[4].plot(ISD14C1D[i].ADratio[0],IStotalerrorscore[i],color = '#377eb8',marker = 'o', linewidth=2, markersize=10)
    ax[6].plot(ISD14C1D[i].ADratio[0],ISCcum1[i],color = '#377eb8',marker = 'o', linewidth=2, markersize=10)

# plot CO2 inverison
for i in range(11):
    # plot NoISchange
    ax[1].plot(CO21D[i].ADratio[0],totalerrorscore_CO2[i],color='#4daf4a',marker = 'o', linewidth=2, markersize=10)
    ax[3].plot(CO21D[i].ADratio[0],D14Cerrorscore_CO2[i],color='#4daf4a',marker = 'o', linewidth=2, markersize=10)
    ax[5].plot(CO21D[i].ADratio[0],totalerrorscore_CO2[i],color='#4daf4a',marker = 'o', linewidth=2, markersize=10)
    ax[7].plot(CO21D[i].ADratio[0],Ccum1_CO2[i],marker = 'o',color='#4daf4a', linewidth=2, markersize=10)
    # plot IS change
    ax[1].plot(ISCO21D[i].ADratio[0],ISCO2errorscore_CO2[i],color = '#377eb8',marker = 'o', linewidth=2, markersize=10)
    ax[3].plot(ISCO21D[i].ADratio[0],ISD14Cerrorscore_CO2[i],color = '#377eb8',marker = 'o', linewidth=2, markersize=10)
    ax[5].plot(ISCO21D[i].ADratio[0],IStotalerrorscore_CO2[i],color = '#377eb8',marker = 'o', linewidth=2, markersize=10)
    ax[7].plot(ISCO21D[i].ADratio[0],ISCcum1_CO2[i],color = '#377eb8',marker = 'o', linewidth=2, markersize=10)

for i in range(8):
    for axis in ['top','bottom','left','right']:
        ax[i].spines[axis].set_linewidth(3.5)
    ax[i].tick_params(axis='y',labelsize='large')
    ax[i].tick_params(axis='x',labelsize='large')
    ax[i].tick_params(bottom=True, top=True, left=True, right=True)
    ax[i].tick_params(axis="both", direction="in", length=7, width=3, color="black")
    ax[i].plot(twoD_totalratio,twoDlist[i],color='#e41a1c',marker='o', linewidth=2, markersize=10)
    ax[i].plot(IStwoD_totalratio,IStwoDlist[i],color='#984ea3',marker='o', linewidth=2, markersize=10)

plt.rcParams["font.weight"] = "bold"
ax[0].set_ylabel('CO$_{2atm}$ error score (%)',fontsize=12,fontweight='bold')
ax[2].set_ylabel('∆$^{14}$C$_{atm}$ error score (%)',fontweight='bold',fontsize=12)
ax[4].set_ylabel('Total error score (%)',fontweight='bold',fontsize=12)
ax[6].set_ylabel('Total carbon added (PgC)',fontweight='bold',fontsize=12)
ax[6].set_xlabel('A:D ratio',fontweight='bold',fontsize=12)
ax[7].set_xlabel('A:D ratio',fontweight='bold',fontsize=12)

for i in range(6):
    ax[i].hlines(y=100,linestyle='dashed',color='k',xmin=0, xmax=1.8)
    # ax[i].hlines(y=18,linestyle='solid',color='#e41a1c',xmin=0, xmax=1.8)
    # will need to seperate IS and noIS later
    #ax[i].hlines(y=18,linestyle='dashed',color='#e41a1c',xmin=0, xmax=1.8)

# legends
ISchange_legend = mlines.Line2D([], [], color='#377eb8', marker='o', linestyle='None',markersize=5, label='1D inversion, change in IS')
NoISchange_legend = mlines.Line2D([], [], color='#4daf4a', marker='o', linestyle='None',markersize=5, label='1D inversion, no change in IS')
twoD_legend = mlines.Line2D([], [], color='#e41a1c', marker='o', linestyle='None',markersize=5, label = '2D inversion, no change in IS')
IStwoD_legend = mlines.Line2D([], [], color='#984ea3', marker='o', linestyle='None',markersize=5, label = '2D inversion, change in IS')
control_legend = mlines.Line2D([], [], color='black', linewidth=1.5, linestyle ='--', label = 'Control run')
ax[7].legend(handles=[NoISchange_legend,ISchange_legend,twoD_legend,IStwoD_legend,control_legend],frameon=False,loc='best')


ax[1].set_title('CO$_2$ inversion',fontweight='bold')
ax[0].set_title('∆$^{14}$C inversion',fontweight='bold')

ax[0].invert_yaxis()
ax[1].invert_yaxis()

# ax[0].arrow(1.2, -400, 0, 300, head_width=0.05, head_length=35, fc='r', ec='r')
# ax[0].text()
# ax[0].annotate(text='better', xy=(1.18,-100), xytext=(1.1,-400), arrowprops=dict(color='red',arrowstyle='->',lw=3))
# #ax[2].annotate(text='better', xy=(1.18,60), xytext=(1.1,35), arrowprops=dict(color='red',arrowstyle='->',lw=3))
# ax[4].annotate(text='better', xy=(1.18,40), xytext=(1.1,-20), arrowprops=dict(color='red',arrowstyle='->',lw=3))
# ax[0].set_ylim(100,-400)
ax[7].set_xlim(0,1.2)
ax[1].set_ylim(0,200)
ax[3].set_ylim(0,100)
ax[4].set_ylim(-100,100)
ax[6].set_xlim(0,1.8)
#plt.tight_layout()
plt.show()

# potetntially thinking about adding a different color for IS and no IS Change
# all 1Ds experiments are one color
# actually that wouldnt work. I should figuere out why the model is doing worse first
