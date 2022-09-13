# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 10:23:34 2022

@author: gysmo
"""

'import relevant bits'
import random
import operator
import matplotlib.pyplot

def distance_between(agents_row_a, agents_row_b):
    return (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5

'define how many agents and an empty list'
num_of_agents = 10
num_of_iterations = 100
agents = []

'create the agents'
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

'move the agents'
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


'create a graph space / set coordinates'
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
'plot the agents on the graph'
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()

'call the function, define variable distance, print the distance'
distance = distance_between(agents[0], agents[1])
print(distance)