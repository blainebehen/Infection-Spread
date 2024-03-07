# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:42:32 2024

@author: bsbehen
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 10:49:00 2024

@author: bsbehen
"""

import numpy as np
import networkx as nx
from matplotlib import pyplot as plt
import matplotlib.animation as animation

########################################################################
#Setting Up Graph Where Each Person Is Randomly 
#Given A Color Indicating Initial Infection Status
#Red for Infected, Green for Uninfected
People = np.arange(10) #Dictate Number of People Here
Graph = nx.complete_graph(len(People))
InitialColors = []

for i in range(0,len(People)):
    InitialStatus = np.random.choice(['red','green'], p=[0.15,0.85])
    InitialColors.append(InitialStatus)
    Graph.add_node(i, InfectionStatus = InitialStatus)
    
nx.draw_circular(Graph, with_labels = True, node_color=InitialColors)
plt.show()

########################################################################
#Setting Up Variables
NumberofRounds = 0
TimesRun = 15
Storage = np.zeros([TimesRun + 1,len(Graph)])
FinalColors = []

########################################################################
#Setting Initial Row of Storage
for i in range(0,len(Graph)):
    if Graph.nodes[i]['InfectionStatus'] == 'red':
        Storage[0,i] = 1
    else:
        Storage[0,i] = 0

########################################################################
#Running Simulation Based on Colors of Nodes Indicating Infection Status
while NumberofRounds < TimesRun:
    for i in range(0,len(Graph)):
        if Graph.nodes[i]['InfectionStatus'] == 'red':
            for j in range(0,len(Graph)):
                if Graph.nodes[j]['InfectionStatus'] == 'green':
                    Graph.nodes[j]['InfectionStatus'] = np.random.choice(['red','green'],p=[0.006,0.994])
        if Graph.nodes[i]['InfectionStatus'] == 'red':
            Storage[NumberofRounds + 1,i] = 1
        else:
            Storage[NumberofRounds + 1,i] = 0
    NumberofRounds = NumberofRounds + 1
    
for i in range(0,len(Graph)):
    FinalColors.append(Graph.nodes[i]['InfectionStatus'])

########################################################################
#Display Last Graph and Storage Matrix
nx.draw_circular(Graph, with_labels = True, node_color=FinalColors)
plt.show()
print(Storage)

########################################################################
#Plot Rounds vs Number of People Infected
fig2, ax2 = plt.subplots()
x = np.arange(NumberofRounds + 1)
y = []
for i in range(0,len(Storage)):
    y.append(np.sum(Storage[i,:]))
line, = ax2.plot(x,y)
ax2.set(xlabel = 'Round Number', ylabel = 'Number of Infected')
ax2.set(title = 'Round Number vs Number of Infected')

########################################################################
#Animation For The First Graph (Infection Network)
fig, ax = plt.subplots()
nx.draw_circular(Graph, with_labels=True, node_color=InitialColors, ax=ax)

def update1(frame1):
    NodeColors = []
    for i in range(0, len(Graph)):
        if Graph.nodes[i]['InfectionStatus'] == 'red':
            for j in range(0, len(Graph)):
                if Graph.nodes[j]['InfectionStatus'] == 'green':
                    Graph.nodes[j]['InfectionStatus'] = np.random.choice(['red', 'green'], p=[0.006, 0.994])
    for q in range(0,len(Graph)):
        NodeColors.append(Graph.nodes[q]['InfectionStatus'])
    nx.draw_circular(Graph, with_labels=True, node_color=NodeColors, ax=ax)
    return

animation1 = animation.FuncAnimation(fig, update1, frames=5, interval=10, repeat_delay = 10)
animation1.save('First Graph Animation.gif', writer = 'pillow', fps=1)

########################################################################
#Animation for Second Graph (Rounds vs People Infected)
def update2(frame2):
    line.set_data(x[:frame2], y[:frame2])
    return line,

animation2 = animation.FuncAnimation(fig2, update2, len(x) + 1, blit = True)
animation2.save('Second Graph Animation.gif', writer = 'pillow', fps=100)
