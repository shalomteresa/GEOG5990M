
#Modules Imported
import random
import math
from matplotlib import pyplot as plt
import operator

# Set the pseudo-random seed for reproducibility
random.seed(0)


# Variables for constraining movement.
# The minimum x coordinate.
x_min = 0
# The minimum y coordinate.
y_min = 0
# The maximum x coordinate.
x_max =99
# The maximum y coordinate.
y_max =99

#Create a list to store agents
agents = []


# A variable to store the number of agents
n_agents = 10

# Initialise agents and append them into agents list
for i in range(n_agents):
        agents.append([random.randint(0, 99), random.randint(0, 99)])
        
        
print('agents',agents)


# A variable to store the number of moves
n_moves = 3
for n_moves in range(n_moves):
    for i in range(n_agents):
        # Change agents[i] coordinates randomly
        # x-coordinate
        rn = random.random()
        #print("rn", rn)
        if rn < 0.5:
            agents[i][0] = agents[i][0] + 1
        else:
            agents[i][0] = agents[i][0] - 1
       # Change agents[i] coordinates randomly
       # y-coordinate
        rn = random.random()
        #print("rn", rn)
        if rn < 0.5:
            agents[i][1] = agents[i][1] + 1
        else:
            agents[i][1] = agents[i][1] - 1
        #print(agents)
        # Apply movement constraints.
        if agents[i][0] < x_min:
            agents[i][0] = x_min
        if agents[i][1] < y_min:
            agents[i][1] = y_min
        if agents[i][0] > x_max:
            agents[i][0] = x_max
        if agents[i][1] > y_max:
            agents[i][1] = y_max


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
print('distance between the coordinates',get_distance(x0, y0, x1, y1))

#Calculating the maximum distance using defined functions
# Initialise max_distance
max_distance = 0
for a in agents:
    for b in agents:
            distance = get_distance(a[0], a[1], b[0], b[1])
            #print("distance between", a, b, distance)
            max_distance = max(max_distance, distance)
            #print("max_distance", max_distance)


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
        for j in range(i+1, len(agents), 1):
                b = agents[j]
                # Calculating the Euclidean distance between two agents
                distance = get_distance(a[0], a[1], b[0], b[1])
                #print("distance between", a, b, distance)
                max_distance = max(max_distance, distance)
                #print("max_distance", max_distance)
                #print("i", i, "j", j)
    return max_distance

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

    
