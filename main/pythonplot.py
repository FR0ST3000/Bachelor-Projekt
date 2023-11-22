# plot plot

# 3x3 = [0.02 , 0.02 , 0.03 , 0.02 , 0.02 , 0.02 , 0.04 , 0.02 , 0.02 , 0.02] sec
# 4x3 = [0.21 , 0,24 , 0.28 , 0.27 , 0.20 , 0.28 , 0.20 , 0.21 , 0.27 , 0.20] sec
# 4x4 = [6.27 , 6.54 , 6.10 , 6.13 , 5.39 , 7.03 , 10.52 , 9.65 , 10.09 , 10.55] sec
# 5x4 = [191.48 , 270.35 , 212.39 , 223.93 , 273.11 , 248.08 , 270.52 , 245.76 , 270.69 , 267.54] sec

import matplotlib.pyplot as plt
import numpy as np
import scipy as scipy
import math
from scipy.interpolate import interp1d


#"""
points_3x3 = [0.02 , 0.02 , 0.03 , 0.02 , 0.02 , 0.02 , 0.04 , 0.02 , 0.02 , 0.02]  # prints the rounded average for the 3x3 tsp proccesing time
time_3x3_average = 0
for x in points_3x3:
    time_3x3_average += x
time_3x3_average = time_3x3_average/10
time_3x3_average_rounded = round(time_3x3_average, 2)
print("Time for 3x3 rounded: " + str(time_3x3_average_rounded) + "sec")

points_4x3 = [0.21 , 0.24 , 0.28 , 0.27 , 0.20 , 0.28 , 0.20 , 0.21 , 0.27 , 0.20] # prints the rounded average for the 4x3 tsp proccesing time
time_4x3_average = 0
for x in points_4x3:
    time_4x3_average += x
time_4x3_average =  time_4x3_average/10
time_4x3_average_rounded = round(time_4x3_average, 2)
print("Time for 4x3 rounded: " + str(time_4x3_average_rounded) + "sec")

points_4x4 = [6.27 , 6.54 , 6.10 , 6.13 , 5.39 , 7.03 , 10.52 , 9.65 , 10.09 , 10.55] # prints the rounded average for the 4x4 tsp proccesing time
time_4x4_average = 0
for x in points_4x4:
    time_4x4_average += x
time_4x4_average = time_4x4_average/10
time_4x4_average_rounded = round(time_4x4_average, 2)
print("Time for 4x4 rounded: " + str(time_4x4_average_rounded) + "sec")

points_5x4 = [191.48 , 270.35 , 212.39 , 223.93 , 273.11 , 248.08 , 270.52 , 245.76 , 270.69 , 267.54] # prints the rounded average for the 5x4 tsp proccesing time
time_5x4_average = 0
for x in points_5x4:
    time_5x4_average += x
time_5x4_average = time_5x4_average/10
time_5x4_average_rounded = round(time_5x4_average, 2)
print("Time for 5x4 rounded: " + str(time_5x4_average_rounded) + "sec")
#"""

# Varinaz and Abweichung

Abweichungsquadratsumme_3x3 = 0
for x in points_3x3:
    Abweichungsquadratsumme_3x3 += (x - time_3x3_average)**2
korrigierte_empirische_Varianz_3x3 = Abweichungsquadratsumme_3x3/9
Standardabweichung_3x3 = math.sqrt(korrigierte_empirische_Varianz_3x3)
Standardabweichung_3x3_rounded = round(Standardabweichung_3x3, 2)
print("korrigierte_empirische_Varianz for 3x3 rounded: " + str(korrigierte_empirische_Varianz_3x3) + "sec")
print("Standardabweichung for 3x3 rounded: " + str(Standardabweichung_3x3_rounded) + "sec")


Abweichungsquadratsumme_4x3 = 0
for x in points_4x3:
    Abweichungsquadratsumme_4x3 += (x - time_4x3_average)**2
korrigierte_empirische_Varianz_4x3 = Abweichungsquadratsumme_4x3/9
Standardabweichung_4x3 = math.sqrt(korrigierte_empirische_Varianz_4x3)
Standardabweichung_4x3_rounded = round(Standardabweichung_4x3, 2)
print("korrigierte_empirische_Varianz for 4x3 rounded: " + str(korrigierte_empirische_Varianz_4x3) + "sec")
print("Standardabweichung for 4x3 rounded: " + str(Standardabweichung_4x3_rounded) + "sec")


Abweichungsquadratsumme_4x4 = 0
for x in points_4x4:
    Abweichungsquadratsumme_4x4 += (x - time_4x4_average)**2
korrigierte_empirische_Varianz_4x4 = Abweichungsquadratsumme_4x4/9
Standardabweichung_4x4 = math.sqrt(korrigierte_empirische_Varianz_4x4)
Standardabweichung_4x4_rounded = round(Standardabweichung_4x4, 2)
print("korrigierte_empirische_Varianz for 4x4 rounded: " + str(korrigierte_empirische_Varianz_4x4) + "sec")
print("Standardabweichung for 4x4 rounded: " + str(Standardabweichung_4x4_rounded) + "sec")


Abweichungsquadratsumme_5x4 = 0
for x in points_5x4:
    Abweichungsquadratsumme_5x4 += (x - time_5x4_average)**2
korrigierte_empirische_Varianz_5x4 = Abweichungsquadratsumme_5x4/9
Standardabweichung_5x4 = math.sqrt(korrigierte_empirische_Varianz_5x4)
Standardabweichung_5x4_rounded = round(Standardabweichung_5x4, 2)
print("korrigierte_empirische_Varianz for 5x4 rounded: " + str(korrigierte_empirische_Varianz_5x4) + "sec")
print("Standardabweichung for 5x4 rounded: " + str(Standardabweichung_5x4_rounded) + "sec")




# ploting and extrapolating ----------------------
x_axis = [9 , 12 , 16 , 20]
y_axis = [0.02 , 0.24 , 7.83 , 247.38]
f1d = interp1d(x_axis , y_axis , kind='quadratic')
f1d_extrapolate = interp1d(x_axis , y_axis , kind='cubic' , fill_value='extrapolate')
x_axis_addon = [9 , 12 , 16 , 20 , 25, 30]
y_axis_addon = [0.02 , 0.24 , 7.83 , 247.38 , f1d_extrapolate(25), f1d_extrapolate(30)]
fig, ax = plt.subplots()
#ax.set_facecolor('lightgray')
#ax.set_title('Rechendauer abhängig der Zellenanzahl', color='orange')
ax.set_xlabel('Anzahl der Zellen', color='black')
ax.set_ylabel('Rechenzeit in [s]', color='black')
ax.plot(x_axis_addon, y_axis_addon, color='purple')  # ex. green = 157/255 = 0.615   color=(0.0, 0.615, 0.505, 0.99)
ax.plot(x_axis, y_axis, color=(0.0, 0.615, 0.505, 0.99))
plt.errorbar(9, 0.02, xerr = 0, yerr = 0.01 ,color='red')
plt.errorbar(12, 0.24, xerr = 0, yerr = 0.04 ,color='red')
plt.errorbar(16, 7.83, xerr = 0, yerr = 2.1 ,color='red')
plt.errorbar(20, 247.38, xerr = 0, yerr = 29.02 ,color='red')
plt.yscale('log') # log ; symlog : logit
plt.show()