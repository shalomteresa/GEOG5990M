# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 11:25:21 2023

@author: Shalom Teresa
"""
#import modules
import random
import math

def get_distance(x0, y0, x1, y1):
    # Calculate the difference in the x coordinates.
    diff_x = x0 - x1
    # Calculate the difference in the y coordinates.
    diff_y = y0 - y1
    # Square the differences and add the squares
    add_squaresxy = (diff_x * diff_x) + (diff_y * diff_y)
    # Calculate the square root
    distance = math.sqrt(add_squaresxy)
    return distance