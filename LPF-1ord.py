# -*- coding: utf-8 -*-
#!/usr/bin/env python3

# Para los calculos
import numpy as np

import  math

import scipy                  # http://scipy.org/
from scipy import constants
from scipy import signal

import matplotlib.pyplot as plt
from IPython.display import Image
#%matplotlib inline
params = {'legend.fontsize': 20,
          'figure.figsize': (12, 8),
         'axes.labelsize': 18,
         'axes.titlesize': 18,
         'xtick.labelsize':20,
         'ytick.labelsize':20}
plt.rcParams.update(params)

#Resistencia
R = 12000

#Capacitor
C = 100e-9

#Constante de tiempo
T = R*C

#Función de transferencia  1/ (1 + sT)
sys = signal.TransferFunction([1], [T, 1])
print("Zeros {}".format(sys.zeros))
print("Poles {}".format(sys.poles))

#Bode
w, mag, phase = sys.bode()

plt.figure()
plt.title("Bode")
plt.semilogx(w/6.283, mag)    # Bode en hz
plt.xlabel('Frecuencia [hz]')
plt.ylabel('[dB]')
plt.grid()
#plt.figure()
#plt.title("Phase")
#plt.semilogx(w, phase)  # Bode phase plot
plt.show()
