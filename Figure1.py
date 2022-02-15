## need to fix Marchitto and Rafter Data both in the observation file now

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import functions as f
import cartopy
import matplotlib.ticker as mticker
import cartopy.mpl.geoaxes
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import cartopy.crs as ccrs
import cartopy.feature as cfeature

plt.rcParams["font.weight"] = "bold"

obspath = '~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/observations/'

#CO2 observations
CO2obs = pd.read_csv('~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/observations/CO2data1.txt',sep='\t')
CO2obs['year'] = CO2obs['year'].apply(f.fix)

#d14C observations
d14C = pd.read_csv("~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/observations/IntCalSmoothed.txt",header=None)
D14C = d14C.rename(columns = {0:'year',3:'D14C'})
D14C['year'] = D14C['year'].apply(f.fix)

chen = pd.read_csv(obspath + 'Chen2020.txt',sep='\t',header=0,skiprows=110)

# Marchitto
Mar = pd.read_csv(obspath + 'Marchitto.txt',sep='\s+')
Mar["Cal.Age"] = 1000 * Mar["Cal.Age"]

# Stott
Stott = chen[chen['water.depth']==617]
Stott = Stott[Stott['ref.']=='Stott et al. (2009)']

# Chen
Chen = chen[chen['water.depth']==627]

# Rafter
Rafter = pd.read_csv(obspath + 'Rafter_2019.tab',sep='\t', header=24)
Rafter["Cal age [ka BP]"] = 1000 * Rafter["Cal age [ka BP]"]

GoCobs = [Mar,Stott,Rafter]

GoCobs[0] = GoCobs[0].rename(columns = {'Cal.Age':'year','D14C':'D14CintNP',})
GoCobs[1] = GoCobs[1].rename(columns = {'cal.age':'year','benthic.D14C':'D14CintNP'})
GoCobs[2] = GoCobs[2].rename(columns = {'Cal age [ka BP]':'year','Δ14C [‰]':'D14CintNP'})

for i in range(3):
    GoCobs[i] = GoCobs[i][GoCobs[i]['year']<20000]
    GoCobs[i]['year'] = GoCobs[i]['year'].apply(f.fix)

Lats = [23.50,-1.22,22.90]
Lons = [-111.60,-89.68,-109.50]

# markers = ['o','v','s','D']
markers = ['o','s','D']

fig,axs = plt.subplots(2, 1, sharex=True,figsize=(9,11))
fig.subplots_adjust(hspace=-0.15)

#thickening axis
for axis in ['top','left','right','bottom']:
  axs[0].spines[axis].set_linewidth(3)
for axis in ['left','right','bottom']:
  axs[1].spines[axis].set_linewidth(3)

ax2 = axs[0].twinx()
#get rid of middle
axs[1].spines['top'].set_visible(False)
ax2.spines['bottom'].set_visible(False)
axs[1].tick_params(axis='y',labelsize='large')
axs[1].tick_params(axis='x',labelsize='large')
ax2.tick_params(axis='y',labelsize='large')
axs[0].set_yticklabels([])


ax2.set_ylabel("CO$_2$ (ppm)",fontsize=15,fontweight='bold')
axs[1].set_ylabel("∆$^{14}$C (‰)",fontsize=15,fontweight='bold')
axs[1].set_xlabel("Calendar age (kyr BP)",fontsize=15,fontweight='bold')
axs[1].set_xlim((0,20))
labels = ['Marchitto et al. 2007','Stott et al. 2009','Rafter et al. 2018','Chen et al. 2020']
Anomalies = [GoCobs[0],GoCobs[1],GoCobs[2]]
for i in range(len(Anomalies)):
    axs[1].plot(Anomalies[i].year,Anomalies[i].D14CintNP,marker=markers[i],markeredgecolor='k',markerfacecolor='white', color = '#a65628',label = labels[i],markersize=10,lw=4,zorder=2)
axs[1].plot(D14C.year,D14C.D14C,color = 'darkgray',ls = "-",label="∆$^{14}$C and CO$_2$ observations",lw=4)




axs[1].legend(loc='upper right', bbox_to_anchor=(0.94, 1.1), fontsize=12,ncol=1,frameon=False)


ax2.plot(CO2obs.year,CO2obs.CO2,color = 'darkgray',ls = "-",label='Atmospheric CO2 observations',lw=4)

axins = inset_axes(axs[0], width="40%", height="40%", loc="lower left",
                   axes_class=cartopy.mpl.geoaxes.GeoAxes,
                   axes_kwargs=dict(map_projection= ccrs.PlateCarree()))
axins.stock_img()
llx, lly = -120,-10
urx, ury =  -50,40
axins.set_xlim((llx, urx))
axins.set_ylim((lly, ury))

for i in range(len(Anomalies)):
    axins.plot(Lons[i],Lats[i],marker=markers[i],markeredgecolor='k',markerfacecolor='white',markersize=6.5, color = '#a65628',transform=ccrs.PlateCarree())

axins.add_feature(cfeature.LAND)
axins.add_feature(cfeature.OCEAN)
axins.add_feature(cfeature.COASTLINE, linewidth=1.5)
axins.add_feature(cfeature.BORDERS, linewidth=1.5)

for axis in ['top','left','right','bottom']:
            axins.spines[axis].set_linewidth(3)

g1 = axins.gridlines(draw_labels=True, dms=True, x_inline=False, y_inline=False,)

g1.xlocator = mticker.FixedLocator([-110,-90,-70])

g1.ylabel_style = {'size': 10, 'color': 'black','weight':'bold'}
g1.xlabel_style = {'size': 10, 'color': 'black','weight':'bold'}
g1.left_labels = False
g1.top_labels = False


axs[0].set_yticks([])
axs[0].set_yticklabels([])
#axs[1].tick_params(axis='both', which='minor', labelsize=15)
axs[1].tick_params(bottom=True, top=False, left=True, right=True)
axs[1].tick_params(axis="both", direction="in", length=7, width=3, color="black")
axs[0].tick_params(bottom=False, top=True, left=True, right=False)
axs[0].tick_params(axis='both', direction="in", length=7, width=3, color="black")
ax2.tick_params(bottom=True, top=False, left=True, right=True)
ax2.tick_params(axis="both", direction="in", length=7, width=3, color="black")
ax2.set_ylim(175,290)
axs[1].set_xlim(0,20)
plt.savefig('Figures/Figure1.pdf')
# plt.show()
