"""
B Practical: Code Shrinking I
Author: Sophie Ray Morrison
"""
# import relevant packages
import random
import operator
import matplotlib.pyplot

# define number of agents and make empty agents list
num_of_agents=10
agents = []

# create agents using random numbers (remove need for creating x0 and y0)
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])
    
# print agents
print("agents positions: ", agents)

# set random number
x = random.randint(0,99)

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

maxx = max(agents, key=operator.itemgetter(0))
minx = min(agents, key=operator.itemgetter(0))
maxy = max(agents, key=operator.itemgetter(1))
miny = min(agents, key=operator.itemgetter(1))

# prints maximum in x
print("maximum in the x direction: ", max(agents, key=operator.itemgetter(1)))

# plot right most coordinate red
matplotlib.pyplot.scatter(maxy[1], maxy[0])

# matplotlib.pyplot.scatter(m[1],m[0], color='red')
matplotlib.pyplot.show()

# define distance between function
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
    diffy = a[1] - b[1]
    diffx = a[0] - b[1]
    diffy2 = diffy * diffy
    diffx2 = diffx * diffx
    sumdiff = diffy2 + diffx2
    distance = sumdiff**0.5
    print("distance", distance)
    return distance

# Calculate the distance between any two agents
maxd = 0
for i in range(num_of_agents):
    for j in range(num_of_agents):
        d = distance_between(agents[i],agents[j])
        if(d > maxd):
            maxd = d

# print max distance 
print("max distance: ", maxd)

# distance test to check it works
a = [0,0]
b = [3,4]
d = distance_between(a,b)
print("distance: ", d)

# set y0 and x0
y0 = random.randint(0,99)
x0 = random.randint(0,99)

agents.append([y0,x0])

print("agents' positions after move: ", agents)