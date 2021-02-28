import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.dates as dates
from datetime import datetime

exp="42"
file1="outputSIM/sea_ice_volume." +exp

lista = [] # dates
listb = [] # volume
with open(file1, 'r') as file:
   for row in file:
      a, b = row.split()
      lista.append(int(a))
      listb.append(float(b))

datetp=np.array(lista)

dtime = ["" for i in range(len(datetp))]

for i in range(len(datetp)):
   dstr=str(datetp[i])
   dtime[i]=datetime.strptime(dstr, "%Y%m%d")  

#plt.plot_date(dtime,listb)
plt.plot(dtime,listb)


fileout="FIGS/volume_" + exp +".png"
#plt.axis([0, h.shape[1], 0, h.shape[0]])
plt.savefig(fileout)

plt.show()
