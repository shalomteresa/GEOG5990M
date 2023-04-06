# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 10:43:57 2023

@author: gy22stp
"""
# Moduls Imported

import random
import my_modules.geometry as geometry
    
class Agent:
   def __init__(self, agents, i, environment, n_rows, n_cols, x = None, y = None):
        """
        The constructor method.
        
        Parameters
        ----------
        i : Integer
            To be unique to each instance.
        environment : List
            A reference to a shared environment
        n_rows : Integer
            The number of rows in environment.
        n_cols : Integer
            The number of columns in environment.
        x : Integer
            For initialising the x coordinate of the agent.
        y : Integer
            For initialising the y coordinate of the agent.
        
        Returns
        -------
        None.
        
        """
        self.agents = agents
        self.i = i
        self.environment = environment
        if x == None:
            tnc = int(n_cols / 3)
            self.x = random.randint(tnc - 1, (2 * tnc) - 1)
        else:
            self.x = x
        if y == None:
            tnr = int(n_rows / 3)
            self.y = random.randint(tnr - 1, (2 * tnr) - 1)
        else:
            self.y = y
        # Initialize the agent's store with a random value between 0 and 99
        self.store = random.randint(0, 99)
        # Initialize the agent's store_shares to 0
        self.store_shares = 0
   def __str__(self):
        """
        The function to return a string representation of the Agent object.
        
        Parameter
        -------
        self: An instance of the Agent class.

        Returns
        -------
        A string containing the class name, x and y coordinates, 
        and index i of the Agent object.
   

        """
        return self.__class__.__name__ + "(x=" + str(self.x) \
        + ", y=" + str(self.y) + ", i=" + str(self.i) + ")"
   def __repr__(self):
        """
        The function to return a string representation of an object.

        Returns
        -------
        A string of the object.

        """
        return str(self)
   def move(self, x_min, y_min, x_max, y_max):
        """
        The function to move agents 
        ---------
        This function moves the agents by randomly increasing or decreasing
        its x and y coordinates, subject to the given constraints.


        Parameters
        ----------
        x_min : The minimum x-coordinate that the agent can occupy.
        y_min : The minimum y-coordinate that the agent can occupy.
        x_max : The maximum x-coordinate that the agent can occupy.
        y_max : The maximum y-coordinate that the agent can occupy.


        Returns
        -------
        None.

        """
        rn =random.random()
        if rn < 0.5:
            self.x = self.x + 1
        else:
            self.x = self.x - 1
        #y-coordinate
        rn = random.random()
        #print("rn", rn)
        if rn < 0.5:
            self.y = self.y  + 1
        else:
            self.y  = self.y  - 1
            
         # Apply movement constraints.
        if self.x < x_min:
         self.x = x_min
        if self.y  < y_min:
         self.y  = y_min
        if self.x > x_max:
         self.x = x_max
        if self.y  > y_max:
         self.y  = y_max
         
   def eat(self):
        """
        This function updates the environment and stores according to certain constraints.
        -------
        If the environment value is greater than 10, the agent will add 10 units to its store 
        and decrease the environment value by 10. If the environment value is less than or equal to 10, 
        the agent will add the environment value to its store and set the environment value to 0. 
        If the agent's store exceeds 99, the store is divided by 2 and half of it is added back to the environment 
        
        Returns
        -------
        None.

        """
        if  self.environment[self.y][self.x] > 10:
            self.store = self.store + 10
            self.environment[self.y][self.x] = self.environment[self.y][self.x] - 10
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0
        # If the store exceeds 99, it is divided by 2.
        if  self.store >  99:
            self.store = self.store/2
            self.environment[self.y][self.x] += self.store
            
   def share(self, neighbourhood):
        """
        This function shares the agent's resources with its neighbors within a given neighbourhood.


        Parameters
        ----------
        neighbourhood : int
        the distance threshold for which other agents are considered neighbors.

        Returns
        -------
        None.

        """
    # Create a list of agents in neighbourhood
        neighbours = []
        #print(self.agents[self.i])
        for a in self.agents:
            distance = geometry.get_distance(a.x, a.y, self.x, self.y)
            if distance < neighbourhood:
                neighbours.append(a.i)
        # Calculate amount to share
        n_neighbours = len(neighbours)
        #print("n_neighbours", n_neighbours)
        shares = self.store / n_neighbours
        #print("shares", shares)
        # Add shares to store_shares
        for i in neighbours:
            self.agents[i].store_shares += shares
            
            
    
            