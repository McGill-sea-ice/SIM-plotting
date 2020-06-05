import numpy as np
import math
from copy import copy,deepcopy
from matplotlib.dates import date2num,DateFormatter
import datetime
import matplotlib.pyplot as plt

#------ calc_extent_volume.py -----------------------------
#
# This script calculates and plots the extent and volume 
# of sea ice over the whole domain. A threshold must be 
# specified for the extent.
#
#----------------------------------------------------------

#------ INPUT by user ---------------------------

outputdir="/Users/jean-francoislemieux/Desktop/ECCC-divers/routine_SIM/output/"
exp="17"
listdates=["1980_09_15_00_00", "1981_09_15_00_00", "1982_09_15_00_00",
           "1983_09_15_00_00", "1984_09_15_00_00", "1985_09_15_00_00",
           "1986_09_15_00_00", "1987_09_15_00_00", "1988_09_15_00_00",
           "1989_09_15_00_00", "1990_09_15_00_00", "1991_09_15_00_00",
           "1992_09_15_00_00", "1993_09_15_00_00", "1993_09_15_00_00",
           "1994_09_15_00_00", "1995_09_15_00_00", "1996_09_15_00_00",
           "1997_09_15_00_00", "1998_09_15_00_00", "1999_09_15_00_00",
           "2000_09_15_00_00", "2001_09_15_00_00", "2002_09_15_00_00",
           "2003_09_15_00_00", "2004_09_15_00_00", "2005_09_15_00_00",
           "2006_09_15_00_00", "2007_09_15_00_00"]

Ath=0.15 # threshold for the extent.

#----- find domain dimensions -------------------

date=listdates[0]
fileA=outputdir+"A"+date+"."+exp
A = np.genfromtxt(fileA, dtype=None)
A=np.squeeze(A)
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

#------------------------------------------------

extent = []
volume = []

for i in range(len(listdates)) :
    date=listdates[i]
    print(date)
               
    #----- load data ----------------------------
    fileA=outputdir+"A"+date+"."+exp
    A = np.genfromtxt(fileA, dtype=None)
    A=np.squeeze(A)
    fileh=outputdir+"h"+date+"."+exp
    h = np.genfromtxt(fileh, dtype=None)
    h=np.squeeze(h)

    #----- calculate extent and volume ----------

    mextent=np.zeros(A.shape) # mask for extent
    mextent[(A>=Ath)&(A<=1)]=1
    extent.append(np.sum(mextent*cell_area)/1e6) # in M km^2
    volume.append(np.sum(cell_area*h/1e3)/1e3)   # in k km^3

#------ plot figures ----------------------------

datetime_format = '%Y_%m_%d_%H_%M'
mydates = [datetime.datetime.strptime(date_string, datetime_format)
             for date_string in listdates]

#create the numerical dates from these datetimes
numdates = date2num(mydates)
nd=numdates.shape[0]

plt.plot_date(numdates, volume, 'b-')
plt.axis([numdates[0], numdates[nd-1], 0, 15])
#date_format = numdates.DateFormatter('%d-%m-%Y')
#plt.gca().xaxis.set_major_formatter(date_format)
plt.ylabel('Volume (10$^3$ km$^3$)', fontsize=16)

plt.figure(2)
plt.plot_date(numdates, extent, 'b-')
plt.axis([numdates[0], numdates[nd-1], 0, 10])
plt.ylabel('Extent (10$^6$ km$^2$)', fontsize=16)

plt.show()
