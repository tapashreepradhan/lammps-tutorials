#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 19:46:44 2021

@author: tapashreepradhan
"""

import matplotlib.pyplot as plt
import numpy as np
import csv

results = []
with open('Al_tens_100.def1.txt',newline='') as file:
    reader = csv.reader(file, delimiter=' ')
    next(reader)  # Skip header row.
    for row in reader:
        row2 = [float(i) for i in row]
        results.append(row2)
        print(row2)
        
results2 = np.transpose(results)
plt.plot(results2[0],results2[1], '-or', label='Stress in X', lw=2, markersize = 1, mec = 'r', mfc = 'r')
plt.plot(results2[0],results2[2], '-ob', label='Stress in Y', lw=2, markersize = 1, mec = 'b', mfc = 'b')
plt.plot(results2[0],results2[3], '-og', label='Stress in Z', lw=2, markersize = 1, mec = 'g', mfc = 'g')
plt.xlabel('Strain',fontsize=16)
plt.ylabel('Stress (GPa)',fontsize=16)
plt.title('Stress versus Strain',fontsize=16)
plt.legend(fontsize=12)
plt.axis(aspect='equal')
plt.ylim(0,10)
plt.show()        
