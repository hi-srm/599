"""
E Practical: Agents
Author: Sophie Ray Morrison
"""

import random
import operator
import matplotlib.pyplot
import agentframework

def distance_between(agent_a, agent_b):
    """
    This calculates the distance between agents
    
    Paramaters
    ----------
    agent_a :   List containing y,x coordinates of agent a
                One of the coordinates
    agent_b :   List containing y,x coordinates of agent b
                One of the coordinates
    
    Returns
    ------
    distance : Number
    distance between agent_a and agent_b
    """
    return (((agent_a.x - agent_b.x)**2) + 
    ((agent_a.y - agent_b.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 100
agents = []

# test connection between model and agent framework
a = agentframework.Agent()
print(a.y, a.x)
# this check worked! printing random values
a.move()
print(a.y, a.x)
# also worked

# making agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent())

# moving agents
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()

matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

## distance calculation - not needed?
# for agents_row_a in agents:
#     for agents_row_b in agents:
#         distance = distance_between(agents_row_a, agents_row_b)

# Test to check distance is being calculated correctly
# for this, i changed agents to 2 and iterations to 1
# for agent1 in agents:
#     for agent2 in agents:
#         distance = distance_between(agent1, agent2)
#         print("Printing position of agent 1: ")
#         print(agent1.x, agent1.y)
#         print("Printing position of agent 2: ")
#         print(agent2.x, agent2.y)
#         print("Printing distance: ")
#         print(distance)

# first pair calculates distance of agent 1 from itself
# second pair calculates distance between 1st and 2nd agent
# third pair calculates distance between 2nd and 1st
# last pair calculates distance between agent 2 and agent 2

# Print distance between agents
for agent1 in agents:
    for agent2 in agents:
        distance = distance_between(agent1, agent2)
        print(distance)