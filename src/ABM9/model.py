# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 10:43:43 2023

@author: gy22stp
"""

# Modules Imported

import random
import operator
import my_modules.agentframework as af
import my_modules.io as io
import my_modules.geometry as geometry
import imageio
import os
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import matplotlib
import matplotlib.animation as anim
import tkinter as tk
import requests
import bs4



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
    # # Random
    # if random.random() < 0.1:
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
    global carry_on
    while (ite <= n_iterations) & (carry_on) :
        yield ite # Returns control and waits next call.
        ite = ite + 1
    global data_written
    if data_written == False:
        # Set the Write data menu to normal.
        menu_0.entryconfig("Write data", state="normal")
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
    plt.imshow(environment)
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

def run(canvas):
    """
    The function to draw a canvas and display the animation.
    ---------
    
    This function takes a canvas object as input and runs the model by 
    creating an animation using the FuncAnimation function from the matplotlib.animation module. 

    Parameters
    ----------
    canvas : It is a TKinter canvas object.

    Returns
    -------
    None.

    """
    animation = anim.FuncAnimation(fig, update, init_func=plot, frames=gen_function, repeat=False)
    animation.new_frame_seq()
    canvas.draw()
    
def output():
    """
    The function to save output files in a given location.
    -------
    
    Writes environment data to a text file and Generates a GIF animation from the images
    saved during the model simulation and saves at the given location.

    Returns
    -------
    None.

    """
    # Write data
    print("write data")
    io.write_data('../../data/output/out.txt', environment)
    imageio.mimsave('../../data/output/out.gif', images, fps=3)

def exiting():
    """
    Exit the program.
    """
    root.quit()
    root.destroy()
    #sys.exit(0)

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
    
    # Define Neighbourhood threshold
    neighbourhood = 50
    
    # Move agents by defining the number of iterations
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
    
   
    
   # Send a request to the url to get the data
    url = 'https://agdturner.github.io/resources/abm9/data.html'
    r = requests.get(url, verify=False)
    content = r.text
   # Parse the html content using BeautifulSoup 
    soup = bs4.BeautifulSoup(content, 'html.parser')
    td_ys = soup.find_all(attrs={"class" : "y"})
    td_xs = soup.find_all(attrs={"class" : "x"})
    print(td_ys)
    print(td_xs)
    # Initialise agents
    agents = []
    for i in range(n_agents):
        # Create an agent
        y = int(td_ys[i].text) + 99
        x = int(td_xs[i].text) + 99
        agents.append(af.Agent(agents, i, environment, n_rows, n_cols, x, y))
        print(agents[i].agents[i]) 
        
    # Animate
    # Initialise fig and carry_on
    fig = matplotlib.pyplot.figure(figsize=(7, 7))
    ax = fig.add_axes([0, 0, 1, 1])
    carry_on = True
    data_written = False
    # GUI
    # Create the main window
    root = tk.Tk()
    root.wm_title("Agent Based Model")
    # Create a canvas to hold the plot
    canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    # Create a menu bar
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)
    # Create a "Model" menu in the menu bar
    menu_0 = tk.Menu(menu_bar)
    menu_bar.add_cascade(label="Model", menu=menu_0)
    # Add commands to the "Model" menu
    menu_0.add_command(label="Run model", command=lambda: run(canvas))
    menu_0.add_command(label="Write data", command=lambda: output())
    # Add an "Exit" command to the "Model" menu
    menu_0.add_command(label="Exit", command=lambda: exiting())
    # Disable the "Write data" command until the model has been run
    menu_0.entryconfig("Write data", state="disabled")
    # Exit if the window is closed.
    root.protocol('WM_DELETE_WINDOW', exiting)
    tk.mainloop()
    
      
    #Calculating the maximum distance using defined functions
    max_distance = 0 # Initialise max_distance
    for a in agents:
        for b in agents:
                #distance = get_distance(a[0], a[1], b[0], b[1])
                distance = geometry.get_distance(a.x, a.y, b.x, b.y)
                #print("distance between", a, b, distance)
                max_distance = max(max_distance, distance)
                #print("max_distance", max_distance)
    
    
   

    



