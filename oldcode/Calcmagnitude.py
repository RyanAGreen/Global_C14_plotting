import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
#cd ~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/Manuscript/Plotting/
import functions as f

# read in data

ISpath = '~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/Manuscript/Plotting/modeldata/ISchange/'
NoISpath = '~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/Manuscript/Plotting/modeldata/NoISchange/'
obspath = '~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/observations/'

# marchitto
mar = pd.read_fwf(obspath + 'Marchitto.txt',sep='\t')
mar = mar.drop([0])
mar = mar.rename(columns={"D14C": "D14CintNP","Cal.Age":"year"})

chen = pd.read_csv(obspath + 'Chen2020.txt',sep='\t',header=0,skiprows=110)
# Stott
Stott = chen[chen['water.depth']==617]
Stott = Stott[Stott['ref.']=='Stott et al. (2009)']

# Chen
Chen = chen[chen['water.depth']==627]

# Rafter
Rafter = chen[chen['ref.']=='Rafter et al. (2018)']

GoCobs_fromChen = [Stott,Rafter,Chen]


for i in range(3):
    GoCobs_fromChen[i] = GoCobs_fromChen[i].rename(columns = {'cal.age':'year','benthic.D14C':'D14CintNP'})
    GoCobs_fromChen[i] = GoCobs_fromChen[i][GoCobs_fromChen[i]['year']<20000]
    GoCobs_fromChen[i]['year'] = GoCobs_fromChen[i]['year'].apply(f.fix)

obs = [mar,GoCobs_fromChen[0],GoCobs_fromChen[1],GoCobs_fromChen[2]]

for i in range(4):
    mag = f.magnitude(obs[i])
    print(mag[0])
