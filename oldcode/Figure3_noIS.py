import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.path as mpath
import matplotlib.lines as mlines
import functions as f
import matplotlib.patches as mpatches

ISpath = '~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/Manuscript/Plotting/modeldata/ISchange/'
NoISpath = '~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/Manuscript/Plotting/modeldata/NoISchange/'

#control should be same as Hain 2014
control = pd.read_fwf(NoISpath + "control.txt",header=None,infer_nrows=1000)
control = f.organizedata(control)

IScontrol = pd.read_fwf(ISpath + "IScontrol.txt",header=None,infer_nrows=1000)
IScontrol = f.organizedata(IScontrol)

# 2D Optimal No IS change (0.04 % of minimization)
twoD_optimal = pd.read_fwf(NoISpath + "2Druns/Powell2Dinversion.txt",header=None,infer_nrows=1000)
twoD_optimal = f.organizedata(twoD_optimal)

# 2D optimal IS change (0.1 % of minimization)
IStwoD_optimal = pd.read_fwf(ISpath + "2Druns/ISPowell2Dinversion.txt",header=None,infer_nrows=1000)
IStwoD_optimal = f.organizedata(IStwoD_optimal)


both_1D = f.read1Dboth(NoISpath)
ISboth_1D = f.read1Dboth(ISpath)

CO2_only = both_1D[0]
ISCO2_only = ISboth_1D[0]

totalerrorscore_two = []

D14Cerrorscore_two = []

CO2errorscore_two = []
Ccum1_two = []


IStotalerrorscore_two = []
ISD14Cerrorscore_two = []
ISCO2errorscore_two = []
ISCcum1_two = []

for i in range(21):
    # find total error values
    totalerrorscore_two.append(f.score(both_1D[i],control)[0])
    #IStotalerrorscore.append(f.score(ISD14C1D[i],IScontrol)[0])
    IStotalerrorscore_two.append(f.score(ISboth_1D[i],control)[0])

    # find D14C error values
    D14Cerrorscore_two.append(f.D14Cscore(both_1D[i],control))
    #ISD14Cerrorscore.append(f.D14Cscore(ISD14C1D[i],IScontrol))
    ISD14Cerrorscore_two.append(f.D14Cscore(ISboth_1D[i],control))

    # find CO2 error values
    CO2errorscore_two.append(f.CO2score(both_1D[i],control))
    #ISCO2errorscore.append(f.CO2score(ISD14C1D[i],IScontrol))
    ISCO2errorscore_two.append(f.CO2score(ISboth_1D[i],control))

    # find cum carbon
    Ccum1_two.append(f.max(both_1D[i]))
    ISCcum1_two.append(f.max(ISboth_1D[i]))


# calculate scores and cum carbon for 2Doptimal runs and CO2 only

# total score
twoD_totalscore,twoD_totalratio = f.score(twoD_optimal,control)
IStwoD_totalscore,IStwoD_totalratio = f.score(IStwoD_optimal,control)
CO2only_totalscore,CO2only_totalratio = f.score(CO2_only,control)
ISCO2only_totalscore,ISCO2only_totalratio = f.score(ISCO2_only,control)
# D14C score
twoD_D14Cscore = f.D14Cscore(twoD_optimal,control)
IStwoD_D14Cscore = f.D14Cscore(IStwoD_optimal,control)
CO2only_D14Cscore = f.D14Cscore(CO2_only,control)
ISCO2only_D14Cscore = f.D14Cscore(ISCO2_only,control)
# CO2 scores
twoD_CO2score = f.CO2score(twoD_optimal,control)
IStwoD_CO2score = f.CO2score(IStwoD_optimal,control)
CO2only_CO2score = f.CO2score(CO2_only,control)
ISCO2only_CO2score = f.CO2score(ISCO2_only,control)
# Cumlative carbon
twoD_Ccum = f.max(twoD_optimal)
IStwoD_Ccum= f.max(IStwoD_optimal)
CO2only_Ccum = f.max(CO2_only)
ISCO2only_Ccum= f.max(ISCO2_only)


#create list so I can plot in a row
twoDlist = [twoD_CO2score,twoD_D14Cscore,twoD_totalscore,twoD_Ccum]
IStwoDlist = [IStwoD_CO2score,IStwoD_D14Cscore,IStwoD_totalscore,IStwoD_Ccum]
CO2onlylist = [CO2only_CO2score,CO2only_D14Cscore,CO2only_totalscore,CO2only_Ccum]
ISCO2onlylist = [ ISCO2only_CO2score,ISCO2only_D14Cscore,ISCO2only_totalscore,ISCO2only_Ccum]



fig,ax = plt.subplots(4,figsize=(7,10),sharex='col',sharey='row')
ax=ax.flatten()


# plot 1D both constraints
for i in range(21):
# plot noIS change
    ax[0].plot(both_1D[i].ADratio[0],CO2errorscore_two[i],color='darkgray',marker = 'o',markeredgecolor='k', linewidth=2, markersize=10,alpha=0.5)
    ax[1].plot(both_1D[i].ADratio[0],D14Cerrorscore_two[i],color='darkgray',marker = 'o',markeredgecolor='k', linewidth=2, markersize=10,alpha=0.5)
    ax[2].plot(both_1D[i].ADratio[0],totalerrorscore_two[i],color='darkgray',marker = 'o',markeredgecolor='k', linewidth=2, markersize=10,alpha=0.5)
    ax[3].plot(both_1D[i].ADratio[0],Ccum1_two[i],marker = 'o',markeredgecolor='k',color='darkgray', linewidth=2, markersize=10,alpha=0.5)
# # plot IS ISchange
#     ax[1].plot(ISboth_1D[i].ADratio[0],ISCO2errorscore_two[i],color = 'darkgray',marker = 'o',markeredgecolor='k', linewidth=2, markersize=10,alpha=0.5)
#     ax[3].plot(ISboth_1D[i].ADratio[0],ISD14Cerrorscore_two[i],color = 'darkgray',marker = 'o',markeredgecolor='k', linewidth=2, markersize=10,alpha=0.5)
#     ax[5].plot(ISboth_1D[i].ADratio[0],IStotalerrorscore_two[i],color = 'darkgray',marker = 'o',markeredgecolor='k', linewidth=2, markersize=10,alpha=0.5)
#     ax[7].plot(ISboth_1D[i].ADratio[0],ISCcum1_two[i],color = 'darkgray',marker = 'o',markeredgecolor='k', linewidth=2, markersize=10,alpha=0.5)

# plot optimal 1D both constraints
# plot noIS change
ax[0].plot(both_1D[1].ADratio[0],CO2errorscore_two[1],color='#ff7f00',marker = 'o',markeredgecolor='k', linewidth=2, markersize=10)
ax[1].plot(both_1D[1].ADratio[0],D14Cerrorscore_two[1],color='#ff7f00',marker = 'o',markeredgecolor='k', linewidth=2, markersize=10)
ax[2].plot(both_1D[1].ADratio[0],totalerrorscore_two[1],color='#ff7f00',marker = 'o',markeredgecolor='k', linewidth=2, markersize=10)
ax[3].plot(both_1D[1].ADratio[0],Ccum1_two[1],marker = 'o',markeredgecolor='k',color='#ff7f00', linewidth=2, markersize=10)
# # plot IS ISchange
#     ax[1].plot(ISboth_1D[10].ADratio[0],ISCO2errorscore_two[10],color = '#ff7f00',marker = 'o',markeredgecolor='k', linewidth=2, markersize=10)
#     ax[3].plot(ISboth_1D[10].ADratio[0],ISD14Cerrorscore_two[10],color = '#ff7f00',marker = 'o',markeredgecolor='k', linewidth=2, markersize=10)
#     ax[5].plot(ISboth_1D[10].ADratio[0],IStotalerrorscore_two[10],color = '#ff7f00',marker = 'o',markeredgecolor='k', linewidth=2, markersize=10)
#     ax[7].plot(ISboth_1D[10].ADratio[0],ISCcum1_two[10],color = '#ff7f00',marker = 'o',markeredgecolor='k', linewidth=2, markersize=10)

for i in range(4):
    for axis in ['top','bottom','left','right']:
        ax[i].spines[axis].set_linewidth(3.5)

    ax[i].tick_params(axis='y',labelsize='large')
    ax[i].tick_params(axis='x',labelsize='large')
    ax[i].tick_params(bottom=True, top=True, left=True, right=True)
    ax[i].tick_params(labelbottom=False, labeltop=False, labelleft=False, labelright=True)
    ax[i].tick_params(axis="both", direction="in", length=7, width=3, color="black")
ax[3].tick_params(labelbottom=True, labeltop=False, labelleft=False, labelright=True)

counter = 0
for i in range(4):
    #ax[i].plot(twoD_totalratio,twoDlist[counter],color='#984ea3',marker='o',markeredgecolor='k', linewidth=2, markersize=10)
    ax[i].plot(CO2only_totalratio,CO2onlylist[counter],color='#e41a1c',marker='o',markeredgecolor='k', linewidth=2, markersize=10)
    #ax[i].boxplot(test,positions=[ISCO2onlylist[counter]], vert=False)
    # ax[i].axvspan(0, 0.4, alpha=0.25, color='#ff7f00')
    # ax[i].axvspan(0.72, 0.85, alpha=0.25, color='#984ea3')
    counter += 1
ax[0].set_ylim(55,145)
ax[1].set_ylim(95,105)
ax[2].set_ylim(80,120)
ax[3].set_xlim(-0.15,2.15)
ax[3].set_ylim(0,800)

# get tick locations
locs0 = ax[0].get_yticks().tolist()
labels0 = ax[0].get_yticklabels()
locs1 = ax[1].get_yticks()
labels1 = ax[1].get_yticklabels()
locs2 = ax[2].get_yticks()
labels2 = ax[2].get_yticklabels()
locs3 = ax[3].get_yticks()
labels3 = ax[3].get_yticklabels()

twoD_optimal.loc[twoD_optimal['Crate'] == 0, 'ADratio'] = np.nan
test = np.array(twoD_optimal.ADratio)
filtered_data = test[~np.isnan(test)]
bp=[0,1,1,1]
bp[0] = ax[0].boxplot(filtered_data,positions=[twoDlist[0]],widths=15,showfliers=True, vert=False, patch_artist=True,zorder=0)
bp[1] = ax[1].boxplot(filtered_data,positions=[twoDlist[1]],widths=1.5,showfliers=False, vert=False, patch_artist=True,zorder=0)
bp[2] = ax[2].boxplot(filtered_data,positions=[twoDlist[2]],widths=6.5,showfliers=False, vert=False, patch_artist=True,zorder=0)
bp[3] = ax[3].boxplot(filtered_data,positions=[twoDlist[3]],widths=125,showfliers=False, vert=False, patch_artist=True,zorder=0)

for i in range(4):
    ## change outline color, fill color and linewidth of the boxes
    for box in bp[i]['boxes']:
        # change outline color
        box.set( color='#7570b3', linewidth=2)
        # change fill color
        box.set( facecolor = '#984ea3' )

    ## change color and linewidth of the whiskers
    for whisker in bp[i]['whiskers']:
        whisker.set(color='#7570b3', linewidth=2)

    ## change color and linewidth of the caps
    for cap in bp[i]['caps']:
        cap.set(color='#7570b3', linewidth=2)

    ## change color and linewidth of the medians
    for median in bp[i]['medians']:
        median.set(color='white', linewidth=3)

    ## change the style of fliers and their fill
    for flier in bp[i]['fliers']:
        flier.set(marker='o', color='#e7298a', alpha=0.5)
#plt.yticks(locs0)
ax[0].set_yticks(ticks=locs0)
ax[0].set_yticklabels(labels=locs0)
ax[1].set_yticks(ticks=locs1)
ax[1].set_yticklabels(labels=locs1)
ax[2].set_yticks(ticks=locs2)
ax[2].set_yticklabels(labels=locs2)
ax[3].set_yticks(ticks=locs3)
ax[3].set_yticklabels(labels=locs3)


counter = 0
# for i in range(1,8,2):
#     ax[i].plot(IStwoD_totalratio,IStwoDlist[counter],color='#984ea3',marker='o',markeredgecolor='k', linewidth=2, markersize=10)
#     ax[i].plot(ISCO2only_totalratio,ISCO2onlylist[counter],color='#e41a1c',marker='o',markeredgecolor='k', linewidth=2, markersize=10)
#     #ax[i].boxplot(test,positions=[ISCO2onlylist[counter]], vert=False)
#     ax[i].axvspan(0.9, 1.34, alpha=0.25, color='#ff7f00')
#     ax[i].axvspan(1.34, 1.47, alpha=0.25, color='#984ea3')
#     #ax[i].axvspan(0.89, 1.11, alpha=0.4, color='#BA3F1D')
#     counter += 1

# for i in range(6,8):
#     ax[i].hlines(y=483.6,linestyle='dotted',color='k',xmin=-1, xmax=3,zorder = 0)
#     ax[i].hlines(y=2516.59,linestyle='dotted',color='k',xmin=-1, xmax=3,zorder=0)
    #ax[i].axhspan(483.6,2516.59, alpha=0.25, color='k')
#
# ax[6].hlines(y=483.6,linestyle='solid',color='k',xmin=0.3, xmax=0.9,lw=2.5,zorder=1)
# ax[7].hlines(y=2516.59,linestyle='solid',color='k',xmin=1, xmax=1.5,lw=2.5,zorder=1)

plt.rcParams["font.weight"] = "bold"
ax[0].set_ylabel('CO$_{2atm}$ score \n (%)',fontsize=12,fontweight='bold')
ax[1].set_ylabel('∆$^{14}$C$_{atm}$ score \n (%)',fontweight='bold',fontsize=12)
ax[2].set_ylabel('Total score \n (%)',fontweight='bold',fontsize=12)
ax[3].set_ylabel('Total carbon \n (PgC)',fontweight='bold',fontsize=12)
ax[3].set_xlabel('ALK:DIC ratio',fontweight='bold',fontsize=12)
#ax[7].set_xlabel('ALK:DIC ratio',fontweight='bold',fontsize=12)

for i in range(3):
    ax[i].hlines(y=100,linestyle='dashed',color='k',xmin=-1, xmax=3)
    # ax[i].hlines(y=18,linestyle='solid',color='#e41a1c',xmin=0, xmax=1.8)
    # will need to seperate IS and noIS later
    #ax[i].hlines(y=18,linestyle='dashed',color='#e41a1c',xmin=0, xmax=1.8)

# adding arrows
# ax[1].arrow(x=1.6, y=100, dx=0, dy=40, width=.08, facecolor='red', edgecolor='none')
# ax[1].annotate('Ability to add carbonate ion', xy = (1.7, 80))
# ax[1].annotate('', ha = 'center', va = 'bottom', xy = (1.55,40),xytext = (1.55, 90),arrowprops = {'facecolor' : 'black'})
# ax[1].text(1.6, 60,'Ability to add \ncarbonate ion',fontsize='small')
# ax[5].annotate('', ha = 'center', va = 'bottom', xy = (1.35,63),xytext = (1, 63),arrowprops = {'facecolor' : 'black'})
# ax[5].text(0.95, 30,'Ability to add \ncarbonate ion',fontsize='small')

ax[2].annotate('', ha = 'center', va = 'bottom', xy = (1.8,111),xytext = (1.8, 101),arrowprops = {'facecolor' : 'red'},zorder=4)
ax[2].text(1.85, 106,'worse',fontsize='small')

ax[2].annotate('', ha = 'center', va = 'bottom', xy = (1.8,89),xytext = (1.8, 99),arrowprops = {'facecolor' : 'green'},zorder=4)
ax[2].text(1.85, 94,'better',fontsize='small')

# ax[6].text(1.6, 2600,'Upper bound',fontsize='small')
# ax[6].text(1.6, 250,'Lower bound',fontsize='small')
# ax[7].text(1.6, 2600,'Upper bound',fontsize='small')
# ax[7].text(1.6, 250,'Lower bound',fontsize='small')

# legends

oneDall_legend = mpatches.Patch(color='darkgray',alpha=0.5, label='1D inversion ensemble')
CO21D_legend = mpatches.Patch(color='#e41a1c', label='1D inversion CO$_2$ only')
both1D_legend = mpatches.Patch(color='#ff7f00', label='1D inversion optimal')
twoD_legend = mpatches.Patch(color='#984ea3', label='2D inversion')
ax[2].legend(handles=[oneDall_legend,CO21D_legend,both1D_legend,twoD_legend],frameon=True,loc='upper left')

#
# ax[0].set_title('No change in IS',fontweight='bold')
# ax[1].set_title('Change in IS',fontweight='bold')

ax[0].invert_yaxis()
ax[1].invert_yaxis()
#ax[0].set_yscale('symlog',base=10,linthresh=50,linscale=1)

#ax[1].set_ylim(50,150)
# first = np.array([0,50])
# second = np.linspace(50,150,1)
# third = np.array([150,200])
# ticks = first+second+third
# ax[0].set_yticks(ticks)
# ax[0].arrow(1.2, -400, 0, 300, head_width=0.05, head_length=35, fc='r', ec='r')
# ax[0].text()
# ax[0].annotate(text='better', xy=(1.18,-100), xytext=(1.1,-400), arrowprops=dict(color='red',arrowstyle='->',lw=3))
# #ax[2].annotate(text='better', xy=(1.18,60), xytext=(1.1,35), arrowprops=dict(color='red',arrowstyle='->',lw=3))
# ax[4].annotate(text='better', xy=(1.18,40), xytext=(1.1,-20), arrowprops=dict(color='red',arrowstyle='->',lw=3))
# ax[0].set_ylim(100,-400)
ax[3].set_xlim(-0.1,2.1)
# ax[1].set_ylim(0,200)
# ax[3].set_ylim(0,200)
# ax[4].set_ylim(0,200)
ax[0].set_ylim(55,145)
ax[1].set_ylim(95,105)
ax[2].set_ylim(80,120)
ax[3].set_xlim(-0.15,2.15)
ax[3].set_ylim(0,800)
#plt.tight_layout()
# plt.savefig('Figures/Figure3_noIS.pdf')
plt.show()
