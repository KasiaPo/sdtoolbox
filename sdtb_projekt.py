# -*- coding: utf-8 -*-
"""
Created on Wed May 24 19:41:55 2017

@author: Kasia
"""

import cantera as ct
import SDToolbox as sd
import matplotlib.pyplot as plt
import numpy as np

P0=1
T0=300
mech = 'gri30.xml'

pressure_array = np.linspace(0.5,8,20)
temperature_array = np.linspace(300,1000,20)

pressure=[]
temperature=[]
speed=[]
C=[]
i=0

for P0 in pressure_array: 

    P0 *= ct.one_atm
    x = 0.1065 # value of max
    a=4.76*x/(1-x)
    q ='O2:1.,N2:3.76,CH4:' + str(a)
    
    
    [cj_speed,R2] = sd.CJspeed(P0, T0, q, mech, 0)
    U1 = cj_speed  #shock speed

    gas = sd.PostShock_eq(cj_speed, P0, T0, q, mech)
    Ps = gas.P/ct.one_atm
    #print i, cj_speed
    C.append(x*100)
    
    pressure.append(gas.P/ct.one_atm)
    temperature.append(gas.T)
    speed.append(cj_speed)
    i=i+1

plt.plot(temperature_array,speed)
plt.xlabel('Initial Temperature [K]')
plt.ylabel('C-J Speed [m/s]')
plt.show()