# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Modules Imported
import random
import math

# Set the pseudo-random seed for reproducibility
random.seed(0)

#Initialise variable x0
x0 = 0
#print x0
print("x0", x0)
# Initialise variable y0
y0 = 0
#print y0
print("y0", y0)
# Change x0 and y0 randomly
rn = random.random()
print("random number", rn)

#If the value 'rn' is less that '0.5' increase 'x0' by '1', otherwise decrease 'x0' by '1'
if rn < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1
print("x0",x0)

#If the value 'rn' is less that '0.5' increase 'y0' by '1', otherwise decrease 'x0' by '1'
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
print("random number", rn)

#If the value 'rn' is less that '0.5' increase 'x1' by '1', otherwise decrease 'x0' by '1'
if rn < 0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1
print("x1",x1)
#If the value 'rn' is less that '0.5' increase 'y1' by '1', otherwise decrease 'x0' by '1'
if rn < 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1
print("y1",y1)

# Calculate the Euclidean distance 
# Set x0 and y0 to equal 0, x1 to equal 3, and y1 to equal 4
x0 = 0
y0 = 0
x1 = 3
y1 = 4

#Calculate the difference in the x coordinates
x = x0-x1
print("x",x)
# Calculate the difference in the y coordinates.
y = y0-y1
print("y",y)
# Square the differences and add the squares
ssd = ((x*x) + (y*y))
print("squared differences",ssd)
# Calculate the square root using math package 
dist = math.sqrt(ssd)
print("distance", dist)

