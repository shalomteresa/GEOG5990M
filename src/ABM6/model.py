# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 10:43:43 2023

@author: gy22stp
"""

# Modules Imported
import random
from matplotlib import pyplot as plt
import operator
import my_modules.agentframework as af
import my_modules.io as io
import my_modules.geometry as geometry
import imageio
import os

# Defining Functions 

def get_max_distance():
    """
   This function Calculates and returns the maximum distance between
   all the agents.

   Returns
   -------
   max_distance : Number
       The maximum distance betwee all the agents.

   """
    max_distance = 0
    for i in range(len(agents)):
        a = agents[i]
        #for j in range(len(agents)):
        for j in range(i+1, len(agents), 1):
                #if i != j:
                #if i < j:
                #print(i, j) 
                b = agents[j]
                # Calculating the Euclidean distance between two agents
                distance = geometry.get_distance(a.x, a.y, b.x, b.y)
                #print("distance between", a, b, distance)
                max_distance = max(max_distance, distance)
                #print("max_distance", max_distance)
                #print("i", i, "j", j)
    return max_distance

def sum_env():
    """The function to Calculate the sum of all values in the `environment` list.
       ----------

       This function iterates through all elements in the environment list
       and calculates the sum of all of its values. 

       Returns
       ----------
       sum_store: Number
       The sum of all values in the `environment` list.
    """
    sum_env = 0
    for row in environment:
        for value in row:
            sum_env += value
    #addenv += sum(row)
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

# Check if this script is being run as the main program and read input data if so
if __name__ == '__main__' :
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
        agents.append(af.Agent(agents, i, environment, n_rows, n_cols))
        print(agents[i])
    print(agents)
    
        #Calculating the maximum distance using defined functions
    max_distance = 0 # Initialise max_distance
    for a in agents:
        for b in agents:
                #distance = get_distance(a[0], a[1], b[0], b[1])
                distance = geometry.get_distance(a.x, a.y, b.x, b.y)
                #print("distance between", a, b, distance)
                max_distance = max(max_distance, distance)
                #print("max_distance", max_distance)

    
    #Define Neighbourhood
    neighbourhood = 50
    
    # Move agents
    n_iterations = 100
    
    # Create directory to write images to.
    try:
        os.makedirs('../../data/output/images/')
    except FileExistsError:
        print("path exists")
    
    # For storing images
    global ite
    ite = 0
    images = []
    
    # Model loop
    for ite in range(n_iterations):
        print("Iteration", ite)
        # Move agents
        print("Move")
        for i in range(n_agents):
            agents[i].move(x_min, y_min, x_max, y_max)
            agents[i].eat()
            #print(agents[i])
        # Share store
        # Distribute shares
        for i in range(n_agents):
            agents[i].share(neighbourhood)
        # Add store_shares to store and set store_shares back to zero
        for i in range(n_agents):
            print(agents[i])
            agents[i].store = agents[i].store_shares
            agents[i].store_shares = 0
        print(agents)
        # Print the maximum distance between all the agents
        print("Maximum distance between all the agents", get_max_distance())
        # Print the total amount of resource
        sum_as = sum_store()
        print("sum_agent_stores", sum_as)
        sum_e = sum_env()
        print("sum_environment", sum_e)
        print("total resource", (sum_as + sum_e))
    
        # Plot
        
        # Plot environment
        
        print (sum_store())
        
        n_rows = io.write_Data(environment)
                   
        plt.imshow(environment)
        plt.ylim(y_max / 3, y_max * 2 / 3)
        plt.xlim(x_max / 3, x_max * 2 / 3) 
        
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
        filename = '../../data/output/images/image' + str(ite) + '.png'
        #filename = '../../data/output/images/image' + str(ite) + '.gif'
        plt.savefig(filename)
        plt.show()
        plt.close()
        images.append(imageio.imread(filename))
        imageio.mimsave('../../data/output/out.gif', images, fps=3)
    
