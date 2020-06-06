# -*- coding: utf-8 -*-
#!/usr/bin/env python3

# Para los calculos
import numpy as np

import  math

import scipy                  # http://scipy.org/
from scipy import constants


kb = constants.value('Boltzmann constant')

#temp
T  = 293

#Resistance
R  = 1e5

#Bandwidth
BW = 1e6

#Voltage noise
#v2  = math.sqrt(4*kb*T*R)  # [V/sqrt(Hz)]
v2  = (4*kb*T*R*BW)**(1/2.)  # [V/sqrt(Hz)]

# presenta los resultados
print('Valor de tensión sobre el resistor: {:1.2e} V/(Hz)^(1/2)'.format(v2) )
