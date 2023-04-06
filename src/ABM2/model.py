# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 10:44:57 2023

@author: gy22stp
"""
#Modules imported

import random
from matplotlib import pyplot as plt 
import operator 
import math

# Set the pseudo-random seed for reproducibility
random.seed(0)

#create a list to store agents
agents = []


# A variable to store the number of agents
n_agents = 10

# Initialise agents and append them into agents list
for i in range(n_agents):
    agents.append([random.randint(0, 99), random.randint(0, 99)])
      
print('agents',agents)

# Move agents
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
print('agents after moving a step',agents)
print('random number',rn)


# Calculate the Euclidean distance 
# Set x0 and y0 to equal 0, x1 to equal 3, and y1 to equal 4
x0 = 0
y0 = 0
x1 = 3
y1 = 4

#Calculate the difference in the x coordinates
x = x0-x1
print("x",x)
# Calculate the difference in the y coordinates.
y = y0-y1
print("y",y)
# Square the differences and add the squares
ssd = ((x*x) + (y*y))
print("squared differences",ssd)
# Calculate the square root using math package 
dist = math.sqrt(ssd)
print("distance", dist)



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

