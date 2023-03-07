# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 10:43:57 2023

@author: gy22stp
"""

import random
    
class Agent:
    def __init__(self):
        self.x = random.randint(0, 99)
        self.y = random.randint(0, 99)
        
    def __str__(self):
        return self.__class__.__name__ + "(x=" + str(self.x) \
        + ", y=" + str(self.y) + ")"
    def __repr__(self):
        return str(self)