
#Modules imported
import random
import math
from matplotlib import pyplot as plt
import time

# Set the pseudo-random seed for reproducibility
random.seed(0)


#Create a list to store agents
agents = []

# A variable to store the number of agents
n_agents = 1000


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


# A list to store times
run_times = []
n_agents_range = range(500, 5000, 500)
# A variable to store the number of moves
n_moves = 3
for n_moves in range(n_moves):
    for n_agents in n_agents_range:
        
        # Initialise agents
        agents = []
        for i in range(n_agents):
            agents.append([random.randint(0, 99), random.randint(0, 99)])
        #print(agents)
       
        # Print the maximum distance between all the agents
        start = time.perf_counter()
        #print("Maximum distance between all the agents", get_max_distance())
        #print("Minimum distance between all the agents", get_min_distance())
        min_distance, max_distance, average = get_min_and_max_distance()
        print("Maximum distance between all the agents", max_distance)
        print("Minimum distance between all the agents", min_distance)
        print("Average distance between all the agents", average)
        end = time.perf_counter()
        run_time = end - start
        print("Time taken to calculate maximum distance", run_time)
        run_times.append(run_time)

print('agents',agents)
print('number of moves',n_moves)

# Plot
plt.title("Time taken to calculate maximum distance for different numbers of agent")
plt.xlabel("Number of agents")
plt.ylabel("Time")
j = 0
for i in n_agents_range:
    plt.scatter(i, run_times[j], color='black')
    j = j + 1
plt.show()
    
