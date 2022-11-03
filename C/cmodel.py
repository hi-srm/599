"""
C Practical: Code Shrinking II
Author: Sophie Ray Morrison
"""
# import relevant packages
import random

# # set random seed
# random.seed(0)

# set random
r = random.random()
print(r) # print to test
r2 = random.randint(0,5)
print(r2) # print to text

num_of_agents=10
agents = []

# create agents
for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])

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

# to test the distance calculation is working
# x0 = y0 = 0   
# x1 = -3
# y1 = -4

# working out the distance by taking the positions, squaring them
# then finding the square root of the total
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