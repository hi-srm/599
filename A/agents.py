"""
A Practical: Agent-based modelling
Author: Sophie Ray Morrison
"""

# import relevant packages
import random

# set y0 and x0 variables
y0 = 50
x0 = 50

# move 1 point 50% of the time on both axes
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1
if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1

# print("y0 after move: ", y0)

# set y1 and x1 variables
y1 = 50
x1 = 50

# move y1 and x1 1 point 50% of the time on both axes
if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1
if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1

# print positions after move
print("y0 and x0 before move: ", y0,",", x0)
print("y1 and x1 after move: ", y1,",", x1)

# calculate distance between points and print
diffy = (y0 - y1)
diffx = (x0 - x1)
diffy2 = diffy * diffy
diffx2 = diffx * diffx
sumdiff = diffy2 + diffx2
distance = sumdiff**0.5
print("distance between x and y after move: ", distance)