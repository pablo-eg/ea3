# -*- coding: utf-8 -*-
#!/usr/bin/env python3

# Para los calculos
import numpy as np

import  math

import scipy                  # http://scipy.org/
from scipy import constants

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

#Frecuencia
f = np.linspace(1,1e6,1000000)
w = 2*np.pi*f

#Función de transferencia
h = 1 / (1 + w*1j*R*C)

plt.plot(f, np.abs(h))
plt.xscale('log')
plt.xlabel('Frecuencia [hz]')
plt.ylabel('Amplitud')
plt.grid()
plt.show()

#Salida filtro pasa bajo
#print('\n\nLa salida del filtro pasa bajo será: {:.4f}'.format(0.5*np.sin(p1-p2)))
