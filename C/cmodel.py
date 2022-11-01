# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 10:55:41 2022

@author: sophie ray morrison
"""
# import relevant bits
import random

# # set random seed
# random.seed(0)

# set random
r = random.random()
print(r) # print to test
r2 = random.randint(0,5)
print(r2) # print to text

# set variables for y and x positions
y0 = 50
x0 = 50
y1 = 40
x1 = 40

# change y0
if random.random() < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
    
# change x0
if random.random() < 0.5:
    x0 = x0 - 1
else:
    x0 = x0 + 1

# print results
print("y0",y0)
print("x0",x0)

# change y1
if random.random() > 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1
    
# change x1
if random.random() < 0.5:
    x1 = x1 - 1
else:
    x1 = x1 + 1
    
# print results
print("y1",y1)
print("x1",x1)

#x0 = y0 = 0   #to test the distance calculation
#x1 = -3
#y1 = -4
y_diff = (y0 - y1)
y_diffsq = y_diff * y_diff
x_diff = (x0 - x1)
x_diffsq = x_diff * x_diff
sum2 = y_diffsq + x_diffsq
answer = sum2**0.5
print(answer)

# if(random.randint(0,1) ==0):
#     x0 = x0 + 1
# else:
#     x0 = x0 - 1
    
# print("x0",x0)