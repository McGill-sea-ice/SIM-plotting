import numpy as np
import math
from copy import copy,deepcopy
#import mpl_toolkits.basemap as basemap
import matplotlib.pyplot as plt

#------ calc_extent_volume.py -----------------------------
#
# This script calculates the extent and volume of sea ice 
# over the whole domain. A threshold must be specified for
# the extent.
#
#----------------------------------------------------------

#------ INPUT by user ---------------------------

outputdir="/Users/jean-francoislemieux/Desktop/ECCC-divers/routine_SIM/output/"
exp="17"
date="1989_09_15_00_00"
Ath=0.15

#------------------------------------------------

#load data
fileA=outputdir+"A"+date+"."+exp
A = np.genfromtxt(fileA, dtype=None)
A=np.squeeze(A)
fileh=outputdir+"h"+date+"."+exp
h = np.genfromtxt(fileh, dtype=None)
h=np.squeeze(h)

#----- find domain dimensions -------------------
nxp2=A.shape[1] # nx + 2

if nxp2 == 65:
    dx=80
elif nxp2 == 130:
    dx=40
elif nxp2 == 260:
    dx=20
elif nxp2 == 520:
    dx=10
else:
    print("wrong value of nx")
    dx=np.nan

cell_area=dx*dx #km^2

#----- calculate extent and volume --------------

mextent=np.zeros(A.shape) # mask for extent
mextent[(A>=Ath)&(A<=1)]=1
extent=np.sum(mextent*cell_area)/1e6 # in M km^2
volume=np.sum(cell_area*h/1e3)/1e3 # in k km^3

print("The extent (10^6 km^2) is = ")
print(extent)
print("The volume (10^3 km^3) is = ")
print(volume)

#plt.pcolor(h, cmap='bwr', vmin=0, vmax=4)
#plt.colorbar()
#plt.show()
