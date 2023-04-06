# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 10:43:43 2023

@author: gy22stp
"""

# Modules Imported
import random
import matplotlib
from matplotlib import pyplot as plt
import operator
import my_modules.agentframework as af
import my_modules.io as io
import my_modules.geometry as geometry
import imageio
import os
import matplotlib.animation as anim

# Defining functions

def get_max_distance():
    """The maximum distance function.
         --------
        
        Calculates the maximum distance between any two agents.
        
        This function iterates through every pair of agents in the agents
        list and calculates the distance between them and returns the maximum
        distance between them.
       
        Returns
        -------
        The maximum distance between any two agents.
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

def update(frames):
    """The function to update the state of the model
       ----------

        This function updates the state of the model with the steps such as
        move and eat agents, share stores, calculate maximum distance between all agents, 
        calculate total amount of resources,and check for stopping condition. 
        Finally, it plots the current state of the model.

        Parameters
        ----------
        frames (int): The current iteration number.

        Returns
        ----------
        None
    """
    # Model loop
    global carry_on
    #for ite in range(1, n_iterations + 1):
    print("Iteration", frames)
    # Move agents
    print("Move and eat")
    for i in range(n_agents):
        agents[i].move(x_min, y_min, x_max, y_max)
        agents[i].eat()
        #print(agents[i])
    # Share store
    print("Share")
    # Distribute shares
    for i in range(n_agents):
        agents[i].share(neighbourhood)
    # Add store_shares to store and set store_shares back to zero
    for i in range(n_agents):
        #print(agents[i])
        agents[i].store = agents[i].store_shares
        agents[i].store_shares = 0
    #print(agents)
    # Print the maximum distance between all the agents
    print("Maximum distance between all the agents", get_max_distance())
    # Print the total amount of resource
    sum_as = sum_store()
    print("sum_agent_stores", sum_as)
    sum_e = sum_env()
    print("sum_environment", sum_e)
    print("total resource", (sum_as + sum_e))

    # Stopping condition
    # Random
    #if random.random() < 0.1:    
    if sum_as / n_agents > 80:
       carry_on = False
       print("stopping condition")

       
    # Plot
    plot()
   
def gen_function():
    """
        The function that yields the iteration number and checks for the stopping condition.
        ----------
        
        This function loops over the iterations while the iteration number is less than
        or equal to the maximum number of iterations until the stopping condition has been reached.
        
    
       This function is a generator that yields the current iteration number and
       checks if the stopping condition has been reached. It does this by looping
       over the iterations while the iteration number is less than or equal to the
       maximum number of iterations and the stopping condition has not been reached.
       A flag is set by the function to check whether the data has been written. 
    
    
       Returns
       ----------
       None
   """
    global ite
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (ite <= n_iterations) & (carry_on) :
        yield ite # Returns control and waits next call.
        ite = ite + 1
    global data_written
    if data_written == False:
        # Write data
        print("write data")
        io.write_Data('../../data/output/out7.txt', environment)
        imageio.mimsave('../../data/output/out7.gif', images, fps=3)
        data_written = True


def plot():
    """
    The function to plot the environment and the agents.
    -------
    
    This function plots the environment and the agents' positions at a certain iteration
    of the model. It also saves the plot as an image file and appends it to a list of images.
    

    Returns
    -------
    fig : matlplotlib figure of the agents and the environment.

    """
    fig.clear()
    plt.ylim(y_min, y_max)
    plt.xlim(x_min, x_max)
    # Plot the environment 
    plt.imshow(environment)
    # Plot the agents
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
    global ite
    filename = '../../data/output/images/image' + str(ite) + '.png'
    plt.savefig(filename)
    images.append(imageio.imread(filename))
    plt.show
    return fig


#print (sum_env())
#print (sum_store())

# Check if this script is being run as the main program and read input data if so
if __name__ == '__main__' :
    environment, n_rows, n_cols = io.read_data()  

    # Set the pseudo-random seed for reproducibility
    random.seed(0)
    
    # Initialise paramters
    n_agents = 10
    
    #Define Neighbourhood
    neighbourhood = 50
    
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
        
         # Animate
        # Initialise fig and carry_on
        fig = matplotlib.pyplot.figure(figsize=(7, 7))
        ax = fig.add_axes([0, 0, 1, 1])
        carry_on = True
        data_written = False
        animation = anim.FuncAnimation(fig, update, init_func=plot, frames=gen_function, repeat=False)
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


