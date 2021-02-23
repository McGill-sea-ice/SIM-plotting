import numpy as np
import math
import matplotlib.pyplot as plt

exp="40"
dx="40"
date="2002_01_01_00_00"
file1="outputSIM/h" + date + "." +exp
h = np.genfromtxt(file1, dtype=None)

filemask="../MASKS/mask"+dx+"_1_0_1.dat"
mask = np.genfromtxt(filemask, dtype=None)

print(h.shape[0])
print(h.shape[1])

hplot = np.zeros(h.shape)
hplot[:,:]=h[:,:]
hplot[mask==0]=np.nan
hplot = np.ma.masked_invalid(hplot)

fileout="FIGS/h" + date +"_" + exp +".png"
cmap = plt.get_cmap('BuPu')
cmap.set_bad(color = 'gray', alpha = 1.)
plt.pcolormesh(hplot, cmap=cmap, vmin=0, vmax=4)
plt.colorbar()
plt.axis([0, h.shape[1], 0, h.shape[0]])
plt.savefig(fileout)

plt.show()
