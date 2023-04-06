# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 10:43:57 2023

@author: gy22stp
"""
# Modules Imported
import random

    
#Defining the agent class
class Agent:
    def __init__(self, i, environment, n_rows, n_cols):
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
        
        Returns
        -------
        None.
        
        """
        self.i = i
        self.environment = environment
        tnc = int(n_cols / 3)
        self.x = random.randint(tnc - 1, (2 * tnc) - 1)
        tnr = int(n_rows / 3)
        self.y = random.randint(tnr - 1, (2 * tnr) - 1)
        self.store = 0
    
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
           
        Returns
        -------
        None.
        """
        if self.environment[self.y][self.x] >= 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0
            
            
  
        
        
    
            