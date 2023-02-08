# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Packages Imported
import random
import math
# Set the pseudo-random seed for reproducibility
random.seed(0)
#Initialise variable x0
x0 = 0
print("x0", x0)
# Initialise variable y0
y0 = 0
print("y0", y0)
# Change x0 and y0 randomly
rn = random.random()
print(rn)
if rn < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1
print("x0",x0)
if rn < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
print("y0",y0)
# Initialise variable x1
x1 = random.randint(0,99)
print("x1", x1)
# Initialise variable y1
y1 = random.randint(0,99)
print("y1",y1)
# Change x1 and y1 randomly
rn= random.random()
print("rn", rn)
if rn < 0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1
print("x1",x1)
if rn < 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1
print("y1",y1)
#calculate the Euclidean distance 
x0 = 0
y0 = 0
x1 = 3
y1 = 4
#differences in the cordinates
x = x0-x1
print("x",x)
y = y0-y1
print("y",y)
#square the differences and add the squares
ssd = ((x*x) + (y*y))
print(ssd)
#Calculate the square root
dist = math.sqrt(ssd)
print(dist)

