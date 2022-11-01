# -*- coding: utf-8 -*-
"""
practical 1: agents

@author: sophie ray morrison
"""

# import relevant packages
import random
import operator
import matplotlib.pyplot

# define how many agents there are and make an empty agent list
num_of_agents=10
agents = []

# populate the "agents" list
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])
    
# print agents to check that the list was populated correctly
print(agents)

# set random number that will be used to scatter agents randomly
x = random.randint(0,99)

# change agents' positions 
for i in range(num_of_agents):
    # change the x
    if (random.random() < 0.5):
        agents[i][0] = agents[i][0] + 1
    else:
        agents[i][0] = agents[i][0] - 1
    # change the y
    if (random.random() < 0.5):
        agents[i][1] = agents[i][1] + 1
    else:
        agents[i][1] = agents[i][1] - 1    

# set the grid coordinates
matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.xlim(0, 100)

for i in range(num_of_agents):
    # plot all the agents
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])

# set min and max values for x and y
maxx = max(agents, key=operator.itemgetter(0))
minx = min(agents, key=operator.itemgetter(0))
maxy = max(agents, key=operator.itemgetter(1))
miny = min(agents, key=operator.itemgetter(1))

# make scatter plot
matplotlib.pyplot.scatter(maxy[1], maxy[0])

# plot right most coordinate red
# matplotlib.pyplot.scatter(m[1],m[0], color='red')

# show the resulting plot
matplotlib.pyplot.show()

# define distance between function
def distance_between(a, b):
    """
    This calculates the distance between agents a and b
    
    Paramaters
    ----------
    a : List containing x and y coordinates of agent a  -- [x,y]
    b : List containing x and y coordinates of agent b -- [x,y]
    
    Returns
    ------
        distance between a and b: float with 2 decimal points
    """
    diffy = a[1] - b[1]
    diffx = a[0] - b[0]
    diffy2 = diffy * diffy # diff y squared
    diffx2 = diffx * diffx # diff x square
    sumdiff = diffy2 + diffx2 # add 2 square numbers
    distance = round((sumdiff**0.5),2) # square root of the sum and reduce to 2 decimal points
    print("distance", distance)
    return distance

## calculate the distance between any two agents
# set initial value of maxd (maximum distance) to 0 (shortest possible distance between agents)
maxd = 0

# loop through each pair of agents
for i in range(num_of_agents):
    for j in range(num_of_agents):
        d = distance_between(agents[i],agents[j])
        if(d > maxd):
            # recursively replace maxd with highest distance found between pairs of agents
            maxd = d
  
# print max distance 
print(maxd)

# test to check that distance_between is working correctly
a = [0,0]
b = [3,4]
d = distance_between(a,b)
print(d)

# it is!
