
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 10:43:43 2023

@author: gy22stp
"""

# Modules Imported
import random
import math
from matplotlib import pyplot as plt
import operator
import my_modules.agentframework as af
import my_modules.io as io


#read the data from txt file
environment, n_rows, n_cols = io.read_data()

# Set the pseudo-random seed for reproducibility
random.seed(0)

# Initialise paramters
n_agents = 10

# Variables for constraining movement.
# The minimum x coordinate.
x_min = 0
# The minimum y coordinate.
y_min = 0

# The maximum an agents x coordinate is allowed to be.
x_max = n_cols - 1
# The maximum an agents y coordinate is allowed to be.
#y_max = 99
y_max = n_rows - 1

# Initialise agents
agents = []
for i in range(n_agents):
    # Create an agent
    agents.append(af.Agent(i,environment,n_rows,n_cols))
    print(agents[i])
print(agents)


# Calculate the Euclidean distance between (x0, y0) and (x1, y1) using functions
#Setting variables of coordinates
x0 = 0
y0 = 0
x1 = 3
y1 = 4
def get_distance(x0, y0, x1, y1):
    """
    Calculate the Euclidean distance between (x0, y0) and (x1, y1).

    Parameters
    ----------
    x0 : Number
        The x-coordinate of the first coordinate pair.
    y0 : Number
        The y-coordinate of the first coordinate pair.
    x1 : Number
        The x-coordinate of the second coordinate pair.
    y1 : Number
        The y-coordinate of the second coordinate pair.

    Returns
    -------
    distance : Number
        The Euclidean distance between (x0, y0) and (x1, y1).
    """
    # Calculate the difference in the x coordinates.
    diff_x = x0 - x1
    # Calculate the difference in the y coordinates.
    diff_y = y0 - y1
    # Square the differences and add the squares
    add_squaresxy = (diff_x * diff_x) + (diff_y * diff_y)
    # Calculate the square root
    distance = math.sqrt(add_squaresxy)
    return distance
#print('distance between the coordinates',get_distance(x0, y0, x1, y1))


#Calculating the maximum distance using defined functions
max_distance = 0 # Initialise max_distance
for a in agents:
    for b in agents:
            #distance = get_distance(a[0], a[1], b[0], b[1])
            distance = get_distance(a.x, a.y, b.x, b.y)
            #print("distance between", a, b, distance)
            max_distance = max(max_distance, distance)
            #print("max_distance", max_distance)

def get_min_and_max_distance():
    """
   This function Calculates and returns the minimum and maximum distance
   between all the agents along with the average distances between the agents.

   Returns
   -------
   min_distance : Number
       The minimum distance betwee all the agents.
   min_distance : Number
       The minimum distance betwee all the agents.
    total distances/n : Number
        Average distance between all the agents
   """
   # Initialize max_distance, min_distance, total_distances and n
    max_distance = 0
    min_distance = math.inf
    total_distances = 0
    n = 0
    # Loop through all the agents to calculate distance 
    for i in range(len(agents)):
        a = agents[i]
        for j in range(i+1, len(agents), 1):
                b = agents[j]
                # Calculating the Euclidean distance between two agents
                distance = get_distance(a[0], a[1], b[0], b[1])
                #print("distance between", a, b, distance)
                min_distance = min(min_distance, distance)
                max_distance = max(max_distance, distance)
                total_distances = total_distances + distance
                n = n + 1
                #print("min_distance", min_distance)
                #print("i", i, "j", j)
    return min_distance, max_distance, total_distances / n


def sum_env():
    """The function to Calculate the sum of all values in the `environment` list.
       ----------

       This function iterates through all elements in the environment list
       and calculates the sum of all of its values. 

       Returns
       ----------
       The sum of all values in the `environment` list.
    """
    sum_env = 0
    for row in environment:
        for value in row:
            sum_env += value
    return sum_env
    
def sum_store():
    """The function to calculate the sum of all agents store attributes.
       ----------
    
        This function iterates through all agents in the agents list and
        calculates the sum of their store attribute. 

        Returns
        ----------
        The sum of all agents store attributes.
    """
    sum_store = 0
    for agent in agents:
        sum_store += agent.store
    return sum_store

print ('sum of environment',sum_env())
print ('sum of the stores',sum_store())
# Move agents
n_iterations = 100
for n_iterations in range(n_iterations):
    for i in range(n_agents):
        #Change agents(i) coordinates randomly
        agents[i].move(x_min, y_min, x_max, y_max)
        agents[i].eat()
# Plot
# Plot environment

print ('sum of stores after movement',sum_store())


# Calling the write function 
n_cols = io.write_Data(environment)

# Plot the environment      
plt.imshow(environment)

# Plot agents
for i in range(n_agents):
    plt.scatter(agents[i].x, agents[i].y, color='black')
# Plot the coordinate with the largest x red
lx = max(agents, key=operator.attrgetter('x'))
plt.scatter(lx.x, lx.y, color='red')
# Plot the coordinate with the smallest x blue
sx = min(agents, key=operator.attrgetter('x'))
plt.scatter(sx.x, sx.y, color='blue')
# Plot the coordinate with the largest y yellow
ly = max(agents, key=operator.attrgetter('y'))
plt.scatter(ly.x, ly.y, color='yellow')
# Plot the coordinate with the smallest y green
sy = min(agents, key=operator.attrgetter('y'))
plt.scatter(sy.x, sy.y, color='green')
plt.ylim(y_max / 3, y_max * 2 / 3)
plt.xlim(x_max / 3, x_max * 2 / 3)   
plt.show()

