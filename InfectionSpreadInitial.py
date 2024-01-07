# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
    
Dict = {0: {'Neighbors': [1,3,5,7], 'Infection Status': 'Infected'},
        1: {'Neighbors': [0,4,6,7], 'Infection Status': 'Uninfected'},
        2: {'Neighbors': [3,4,6,7], 'Infection Status': 'Infected'},
        3: {'Neighbors': [0,2,4,5,6], 'Infection Status': 'Uninfected'},
        4: {'Neighbors': [1,2,3,6], 'Infection Status': 'Infected'},
        5: {'Neighbors': [0,3,6,7], 'Infection Status': 'Uninfected'},
        6: {'Neighbors': [1,2,3,4,5], 'Infection Status': 'Uninfected'},
        7: {'Neighbors': [0,1,2,5,6], 'Infection Status': 'Infected'}}

NumberofInfections = 4
NumberofRounds = 0
ProbabilityofInfection = [0.6,0.4]

while NumberofRounds <= 10:
    for i in range(0,7):
        if Dict[i]['Infection Status'] == 'Infected':
            for j in range(0,len(Dict[i]['Neighbors'])):
                Dict[Dict[i]['Neighbors'][j]]['Infection Status'] = np.random.choice(['Infected','Uninfected'], p = ProbabilityofInfection)
    NumberofRounds = NumberofRounds + 1
