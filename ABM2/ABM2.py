# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Packages installed 
import random
import math
import matplotlib
from matplotlib import pyplot as plt
import operator

#Set the random seed
random.seed(0)


#Initialise agents
n_agents = 10
n_moves = 0
#Create a list to store agents
agents = []
for i in range(n_agents):
    # Initialise variable x0
    x0 = random.randint(0, 99)
    #print("x0", x0)
    # Initialise variable y0
    y0 = random.randint(0, 99)
    #print("y0", y0)
    agents.append([x0, y0])
    agents.append([random.randint(0, 99), random.randint(0, 99)])
    
print(agents)


for i in range(n_agents):
    rn = random.random()
    if rn < 0.5:
        agents[i][0] = agents[i][0] + 1
    else:
        agents[i][0] = agents[i][0] - 1
    rn = random.random()
    if rn < 0.5:
        agents[i][1] = agents[i][1] + 1
    else:
        agents[i][1] = agents[i][1] - 1
        
print(rn)
    




# Plot the agents
for i in range(n_agents):
    plt.scatter(agents[i][0], agents[i][1], color='black')
    # Get the coordinates with the largest x-coordinate
    maxx = max(agents, key=operator.itemgetter(0))
    plt.scatter(maxx[0], maxx[1], color='green')
    # Get the coordinates with the smallest x-coordinate
    minx = min(agents, key=operator.itemgetter(0))
    plt.scatter(minx[0], minx[1], color='pink')
plt.show()
