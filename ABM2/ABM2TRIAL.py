# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 10:44:57 2023

@author: gy22stp
"""
#import packages

import random
import matplotlib
from matplotlib import pyplot as plt 
import math
import operator 

#Set the random seed

random.seed(0)

#create a list to store agents
agents = []

#initialize x0 and y0 and append them into agents

x0 = random.randint(0,99)
y0 = random.randint(0,99)
agents.append([x0,y0])

#create more agents

n_agents = 10

for i in range(n_agents):
    agents.append([random.randint(0, 99), random.randint(0, 99)])
      
print(agents)

for i in range(n_agents):
    # Change agents[i] coordinates randomly
    # x-coordinate
    rn = random.random()
    #print("rn", rn)
    if rn < 0.5:
        agents[i][0] = agents[i][0] + 1
    else:
        agents[i][0] = agents[i][0] - 1
    # y-coordinate
    rn = random.random()
    #print("rn", rn)
    if rn < 0.5:
        agents[i][1] = agents[i][1] + 1
    else:
        agents[i][1] = agents[i][1] - 1
print(agents)
print(rn)


# Plot
for i in range(n_agents):
    plt.scatter(agents[i][0], agents[i][1], color='black')
# Plot the coordinate with the largest x red
lx = max(agents, key=operator.itemgetter(0))
plt.scatter(lx[0], lx[1], color='red')
# Plot the coordinate with the smallest x blue
sx = min(agents, key=operator.itemgetter(0))
plt.scatter(sx[0], sx[1], color='blue')
# Plot the coordinate with the largest y yellow
ly = max(agents, key=operator.itemgetter(1))
plt.scatter(ly[0], ly[1], color='yellow')
# Plot the coordinate with the smallest y green
sy = min(agents, key=operator.itemgetter(1))
plt.scatter(sy[0], sy[1], color='green')
plt.show()

