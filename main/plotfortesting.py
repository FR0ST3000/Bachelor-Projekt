import matplotlib.pyplot as plt
import numpy as np
import scipy as scipy
import math
from scipy.interpolate import interp1d


# ploting -----------------------------------------
#x_axis = [0 , 1 , 2 , 3]
#y_axis = [0.02 , 0.24 , 7.83 , 247.38]


# create data time
x = np.arange(4)
y1 = [0.169, 0.139, 0.107, 0.086]
y2 = [0.285, 0.255, 0.210, 0.189]
y3 = [0.149, 0.123, 0.100, 0.083]
y4 = [0.296, 0.246, 0.219, 0.192]
y1err = [0.026, 0.031, 0.047, 0.038]
y2err = [0.012, 0.047, 0.058, 0.057]
y3err = [0.030, 0.047, 0.040, 0.032]
y4err = [0.024, 0.047, 0.058, 0.053]
width = 0.2

  
# plot data in grouped manner of bar type
plt.bar(x-0.3, y1, width, color='limegreen')
plt.bar(x-0.1, y2, width, color=(0.0, 0.615, 0.505, 0.99))
plt.bar(x+0.1, y3, width, color='mediumslateblue')
plt.bar(x+0.3, y4, width, color='indigo')
plt.xticks(x, ['0', '1', '2', '3'])
plt.errorbar(x-0.3, y1, xerr = 0, yerr = y1err, ls = 'none', color='red')
plt.errorbar(x-0.1, y2, xerr = 0, yerr = y2err, ls = 'none', color='red')
plt.errorbar(x+0.1, y3, xerr = 0, yerr = y3err, ls = 'none', color='red')
plt.errorbar(x+0.3, y4, xerr = 0, yerr = y4err, ls = 'none', color='red')
plt.xlabel('Anzahl der Hindernisse', color='black')
plt.ylabel('Rechenzeit in [s]', color='black')
plt.show()



# create data time/cover 5
x = np.arange(4)
y01 = [0.169, 0.139, 0.107, 0.086]
y02 = [0.285, 0.255, 0.210, 0.189]
y03 = [0.149, 0.123, 0.100, 0.083]
y04 = [0.296, 0.246, 0.219, 0.192]
y01err = [0.026, 0.031, 0.047, 0.038]
y02err = [0.012, 0.047, 0.058, 0.057]
y03err = [0.030, 0.047, 0.040, 0.032]
y04err = [0.024, 0.047, 0.058, 0.053]
y11 = [0.8277, 0.7129, 0.6193, 0.5079]
y12 = [1, 0.9988, 0.9984, 0.9977]
y13 = [0.5929, 0.5687, 0.5117, 0.4646]
y14 = [1, 0.9971, 0.9916, 0.9859]

y1 = [(y01[0]/y11[0]), (y01[1]/y11[1]), (y01[2]/y11[2]), (y01[3]/y11[3])]
y2 = [(y02[0]/y12[0]), (y02[1]/y12[1]), (y02[2]/y12[2]), (y02[3]/y12[3])]
y3 = [(y03[0]/y13[0]), (y03[1]/y13[1]), (y03[2]/y13[2]), (y03[3]/y13[3])]
y4 = [(y04[0]/y14[0]), (y04[1]/y14[1]), (y04[2]/y14[2]), (y04[3]/y14[3])]

y1err = [(y01err[0]/y11[0]), (y01err[1]/y11[1]), (y01err[2]/y11[2]), (y01err[3]/y11[3])]
y2err = [(y02err[0]/y12[0]), (y02err[1]/y12[1]), (y02err[2]/y12[2]), (y02err[3]/y12[3])]
y3err = [(y03err[0]/y13[0]), (y03err[1]/y13[1]), (y03err[2]/y13[2]), (y03err[3]/y13[3])]
y4err = [(y04err[0]/y14[0]), (y04err[1]/y14[1]), (y04err[2]/y14[2]), (y04err[3]/y14[3])]
width = 0.2

  
# plot data in grouped manner of bar type
plt.bar(x-0.3, y1, width, color='limegreen')
plt.bar(x-0.1, y2, width, color=(0.0, 0.615, 0.505, 0.99))
plt.bar(x+0.1, y3, width, color='mediumslateblue')
plt.bar(x+0.3, y4, width, color='indigo')
plt.xticks(x, ['0', '1', '2', '3'])
plt.errorbar(x-0.3, y1, xerr = 0, yerr = y1err, ls = 'none', color='red')
plt.errorbar(x-0.1, y2, xerr = 0, yerr = y2err, ls = 'none', color='red')
plt.errorbar(x+0.1, y3, xerr = 0, yerr = y3err, ls = 'none', color='red')
plt.errorbar(x+0.3, y4, xerr = 0, yerr = y4err, ls = 'none', color='red')
plt.xlabel('Anzahl der Hindernisse', color='black')
plt.ylabel('Rechenzeit/Abdeckung in [s]', color='black')
plt.show()


#fig, ax = plt.subplots()
#ax.set_facecolor('lightgray')
#ax.set_title('Rechendauer abhängig der Zellenanzahl', color='red')
#ax.set_xlabel('Anzahl der Hindernisse', color='black')
#ax.set_ylabel('Rechenzeit in [s]', color='black')
#ax.plot(x_axis, y_axis, color=(0.0, 0.615, 0.505, 0.99))
#plt.errorbar(0, 0.02, xerr = 0, yerr = 0.01 ,color='red')
#plt.errorbar(1, 0.24, xerr = 0, yerr = 0.04 ,color='red')
#plt.errorbar(2, 7.83, xerr = 0, yerr = 2.1 ,color='red')
#plt.errorbar(3, 247.38, xerr = 0, yerr = 29.02 ,color='red')
#plt.yscale('log') # log ; symlog : logit
#plt.show()


# abdeckungs %

x = np.arange(4)
y1 = [82.77, 71.29, 61.93, 50.79]
y2 = [100.00, 99.88, 99.84, 99.77]
y3 = [59.29, 56.87, 51.17, 46.46]
y4 = [100.00, 99.71, 99.16, 98.59]
y1err = [17.55, 21.22, 27.67, 25.26]
y2err = [0.00, 0.49, 0.92, 0.74]
y3err = [23.95, 26.05, 25.54, 20.21]
y4err = [0.00, 1.86, 2.00, 4.34]
width = 0.2

  
# plot data in grouped manner of bar type
plt.bar(x-0.3, y1, width, color='limegreen')
plt.bar(x-0.1, y2, width, color=(0.0, 0.615, 0.505, 0.99))
plt.bar(x+0.1, y3, width, color='mediumslateblue')
plt.bar(x+0.3, y4, width, color='indigo')
plt.xticks(x, ['0', '1', '2', '3'])
plt.errorbar(x-0.3, y1, xerr = 0, yerr = y1err, ls = 'none', color='red')
plt.errorbar(x-0.1, y2, xerr = 0, yerr = y2err, ls = 'none', color='red')
plt.errorbar(x+0.1, y3, xerr = 0, yerr = y3err, ls = 'none', color='red')
plt.errorbar(x+0.3, y4, xerr = 0, yerr = y4err, ls = 'none', color='red')
plt.ylim(0, 100)
plt.xlabel('Anzahl der Hindernisse', color='black')
plt.ylabel('Abdeckung in %', color='black')
plt.show()

# doppel abdeckungs %

x = np.arange(4)
y1 = [0.00, 0.92, 1.79, 4.08]
y2 = [1.33, 2.69, 4.33, 5.30]
y1err = [0.00, 1.56, 2.94, 3.87]
y2err = [0.00, 2.27, 5.63, 4.41]
width = 0.2

  
# plot data in grouped manner of bar type
plt.bar(x-0.1, y1, width, color=(0.0, 0.615, 0.505, 0.99))
plt.bar(x+0.1, y2, width, color='indigo')
plt.xticks(x, ['0', '1', '2', '3'])
plt.errorbar(x-0.1, y1, xerr = 0, yerr = y1err, ls = 'none', color='red')
plt.errorbar(x+0.1, y2, xerr = 0, yerr = y2err, ls = 'none', color='red')
plt.ylim(0, 10.5)
plt.xlabel('Anzahl der Hindernisse', color='black')
plt.ylabel('Doppelte Abdeckung in %', color='black')
plt.show()

# Rechenzeit nach Zellenanzahl

x = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1200, 1500, 1800, 2000]
y = [0.15, 0.51, 1.13, 1.97, 3.15, 4.49, 6.11, 7.90, 9.95, 12.19, 17.40, 27.59, 39.86, 49.45]
y1err = [0.026, 0.028, 0.025, 0.020, 0.032, 0.049, 0.075, 0.073, 0.140, 0.062, 0.177, 0.382, 0.409, 0.585]


fig, ax = plt.subplots()
#ax.set_facecolor('lightgray')
#ax.set_title('Rechendauer abhängig der Zellenanzahl', color='red')
ax.set_xlabel('Anzahl der Zellen', color='black')
ax.set_ylabel('Rechenzeit in [s]', color='black')
ax.plot(x, y, color=(0.0, 0.615, 0.505, 0.99))
plt.errorbar(x, y, xerr = 0, yerr = y1err ,ls = 'none', color='red')
plt.show()


# VLOS----------------------------------

# time data
x = np.arange(4)
y1 = [0.374, 1.158, 1.083, 1.173]   # view range = 20
y2 = [1.28, 1.2, 0.865, 1.09]   # view range = 8

y1err = [0.114, 0.454, 0.361, 0.261]
y2err = [0.12, 0.182, 0.254, 0.19]

width = 0.2

  
# plot data in grouped manner of bar type
plt.bar(x-0.1, y1, width, color=(0.0, 0.615, 0.505, 0.99))
plt.bar(x+0.1, y2, width, color='indigo')

plt.xticks(x, ['0', '1', '2', '3'])
plt.errorbar(x-0.1, y1, xerr = 0, yerr = y1err, ls = 'none', color='red')
plt.errorbar(x+0.1, y2, xerr = 0, yerr = y2err, ls = 'none', color='red')

plt.xlabel('Anzahl der Hindernisse', color='black')
plt.ylabel('Rechenzeit in [s]', color='black')
plt.show()


# cover % data
x = np.arange(4)
y1 = [100, 99.14, 95.86, 94.44]   # view range = 20
y2 = [97.33, 95.49, 96.06, 94.06]   # view range = 8

y1err = [0, 2.24, 7.62, 5.18]
y2err = [0, 5.14, 6.32, 5.88]

width = 0.2

  
# plot data in grouped manner of bar type
plt.bar(x-0.1, y1, width, color=(0.0, 0.615, 0.505, 0.99))
plt.bar(x+0.1, y2, width, color='indigo')

plt.xticks(x, ['0', '1', '2', '3'])
plt.errorbar(x-0.1, y1, xerr = 0, yerr = y1err, ls = 'none', color='red')
plt.errorbar(x+0.1, y2, xerr = 0, yerr = y2err, ls = 'none', color='red')

plt.xlabel('Anzahl der Hindernisse', color='black')
plt.ylabel('Abdeckung in %', color='black')
plt.ylim(0, 100)
plt.show()

# double cover % data
x = np.arange(4)
y1 = [0.0, 9.17, 9.62, 12.4]        # view range 20
y2 = [10, 11.17, 12.04, 16.31]  # view range 8
y3 = [0.0, 1.455, 2.72, 5.16]    # better dc view range 20 
y4 = [0, 1.02, 2.06, 3.3] # better dc view range 8
y1err = [0, 8.05, 10.17, 10.1]
y2err = [0, 7.13, 12.21, 12.68]
y3err = [0, 2.00, 3.81, 4.73]
y4err = [0, 1.15, 3.4, 3.2]
width = 0.2

  
# plot data in grouped manner of bar type
plt.bar(x-0.3, y1, width, color='limegreen')
plt.bar(x-0.1, y2, width, color=(0.0, 0.615, 0.505, 0.99))
plt.bar(x+0.1, y3, width, color='mediumslateblue')
plt.bar(x+0.3, y4, width, color='indigo')
plt.xticks(x, ['0', '1', '2', '3'])
plt.errorbar(x-0.3, y1, xerr = 0, yerr = y1err, ls = 'none', color='red')
plt.errorbar(x-0.1, y2, xerr = 0, yerr = y2err, ls = 'none', color='red')
plt.errorbar(x+0.1, y3, xerr = 0, yerr = y3err, ls = 'none', color='red')
plt.errorbar(x+0.3, y4, xerr = 0, yerr = y4err, ls = 'none', color='red')
plt.ylim(0, 30)
plt.xlabel('Anzahl der Hindernisse', color='black')
plt.ylabel('Doppel-Abdeckung in %', color='black')
plt.show()
