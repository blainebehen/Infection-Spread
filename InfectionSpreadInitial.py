# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import networkx as nx
from matplotlib import pyplot as plt

#Initial Dictionary
Dict = {0: {'Neighbors': [1,3,5,7], 'Infection Status': 1},
        1: {'Neighbors': [0,4,6,7], 'Infection Status': 0},
        2: {'Neighbors': [3,4,6,7], 'Infection Status': 1},
        3: {'Neighbors': [0,2,4,5,6], 'Infection Status': 0},
        4: {'Neighbors': [1,2,3,6], 'Infection Status': 1},
        5: {'Neighbors': [0,3,6,7], 'Infection Status': 0},
        6: {'Neighbors': [1,2,3,4,5], 'Infection Status': 0},
        7: {'Neighbors': [0,1,2,5,6], 'Infection Status': 1}}

#Setting Up Variables
NumberofRounds = 0
ProbabilityofInfection = [0.05,0.95]
TimesRun = 10
Storage = np.zeros([TimesRun + 1,len(Dict)])
Graphs = []

#Sets Up Initial Round Of Storage for 2D Array That Tracks Infected
for m in range(0,len(Dict)):
   Storage[NumberofRounds,m] = Dict[m]['Infection Status']

#Makes Initial Graph for People and the Infected
InitialGraph = nx.Graph()
for i in range(0,len(Dict)):
    for m in range(0,len(Dict[i]['Neighbors'])):
        InitialGraph.add_edge(i,Dict[i]['Neighbors'][m])
plt.figure(0)
nx.draw_circular(InitialGraph,with_labels = True)

#Runs Simulation Based on Number of Rounds and Stores Data for a Graph for Each Round
while NumberofRounds < TimesRun:
    Graphs.append((chr(NumberofRounds)))
    Graphs[NumberofRounds] = nx.Graph()
    for i in range(0,len(Dict)):
        if Dict[i]['Infection Status'] == 1:
            for j in range(0,len(Dict[i]['Neighbors'])):
                if Dict[Dict[i]['Neighbors'][j]]['Infection Status'] == 0:
                    Dict[Dict[i]['Neighbors'][j]]['Infection Status'] = np.random.choice([1,0], p = ProbabilityofInfection)
        Storage[NumberofRounds + 1,i] = Dict[i]['Infection Status']
        for m in range(0,len(Dict[i]['Neighbors'])):
          Graphs[NumberofRounds].add_edge(i,Dict[i]['Neighbors'][m])
    NumberofRounds = NumberofRounds + 1

#Tells Number of Infected Initially / After Each Round and Displays 2D Array Showing Such
NumberofInfectedEachRound = np.sum(Storage,1)
print(NumberofInfectedEachRound)
print(Storage)

#Makes Graphs for Each Round
# use a different axis for each time point to see them all in one window.

m = int( np.sqrt(TimesRun) )
n = int( np.ceil(TimesRun/m) )

fig,ax = plt.subplots(m,n, sharex=True, sharey=True, constrained_layout=True)

for i in range(0,TimesRun):
#    plt.figure(i+1)
    p,q = np.unravel_index(i, (m,n)) # convert linear index to (row,col)
    nx.draw_circular(Graphs[i],with_labels = True, node_color=Storage[i], ax=ax[p,q])
    ax[p,q].set_title(f"Step {i}", loc='left')

fig.show()

