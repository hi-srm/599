import random
import operator
import matplotlib.pyplot
import agentframework

def distance_between(a, b):
    """
    

    Parameters
    ----------
    a : TYPE
        DESCRIPTION.
    b : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    return (((a.x - b.x)**2) + ((a.y - b.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 1
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(str(i)))
    
print(agents)
for i in range(num_of_agents):
    #print(agents[i].name, agents[i].x)              
    print(agents[i])              
        

# # Make the agents.
# for i in range(num_of_agents):
    # agents.append([random.randint(0,99),random.randint(0,99)])

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        # if random.random() < 0.5:
        #     agents[i][0] = (agents[i][0] + 1) % 100
        # else:
        #     agents[i][0] = (agents[i][0] - 1) % 100

        # if random.random() < 0.5:
        #     agents[i][1] = (agents[i][1] + 1) % 100
        # else:
        #     agents[i][1] = (agents[i][1] - 1) % 100

print(agents)
for i in range(num_of_agents):
    print(agents[i])

matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].y,agents[i].x)
matplotlib.pyplot.show()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)