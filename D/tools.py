# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 10:23:34 2022

@author: sophie ray morrison
"""

# import relevant bits
import random
import operator
import matplotlib.pyplot
import time 

# define the function
# def distance_between(agents_row_a, agents_row_b):
#    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5

# make the function more readable

def distance_between(a, b):
    """
    This calculates the distance between a and b
    
    Paramaters
    ----------
    a : List containing x and then y
        One of the coordinates
    a : List containing x and then y
        One of the coordinates        
    
    Returns
    ------
        distance : Number
        distance between a and b
    """
    return (((a[0] - b[0])**2) + ((a[1] - b[1])**2))**0.5

# 
start = time.process_time()
random.seed(0)

# define how many agents and an empty list
num_of_agents = 10
num_of_iterations = 100
agents = []

# create the agents
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

#
maxd = 0
mind = distance_between(agents[0],agents[1])
for i in range(num_of_agents):
    for j in range(num_of_agents):
        # print (i, j)
        d = distance_between(agents[i],agents[j])
        if(d > maxd):
            maxd = d
        if (d < mind):
            mind = d

# print max and min distance        
print(maxd)
print(mind)

countmind = 0

for i in range(0, num_of_agents):
    for j in range(i+1, num_of_agents):
        d = distance_between(agents[i], agents[j])
        if (d == mind):
                countmind = countmind + 1
                print(agents[i])

maxd = 0
for i in range(num_of_agents):
    for j in range(i+1, num_of_agents):
        # print (i, j)
        d = distance_between(agents[i],agents[j])
        if(d > maxd):
            maxd = d
            
print(maxd)

# move the agents
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100

# create a graph space / set coordinates
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)

# plot the agents on the graph
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()

# call the function, define variable distance, print the distance
distance = distance_between(agents[0], agents[1])

# to test it works 
# distance = distance_between([0,0],[3,4])
print(distance)


