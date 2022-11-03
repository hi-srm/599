"""
H Practical: Animation/behaviour
Author: Sophie Ray Morrison
Version: Final
"""
## Import relevant packages
import random
import operator
import matplotlib
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv
matplotlib.use('macosx')

## Read the in.txt file
f = open("in.txt") # open file
csv_reader = csv.reader(f) # read as csv
environment = [] # make empty environment list
for line in csv_reader: # scan through each line
    rowlist = [] # make empty row list
    for value in line: # loop through each value in each line of text file
        # print (type(value)) - to test type that the value is, as it wasn't plotting
        rowlist.append((int(value))) # adding integer to each row and change value from string to int
    # print(rowlist)
    environment.append(rowlist) # making a list for the environment with each value
f.close()

## Initialise the agents and creating empty agent list
num_of_agents = 10 # set number of agents
num_of_iterations = 100 # set iterations
neighbourhood = 20 # create neighborhood
agents = [] # make empty agents list

## Populate the agents list with agents
for i in range(num_of_agents): # loop through 'num_of_agents' from 0 to 9
    agents.append(agentframework.Agent(i, environment, agents)) # populatng agent list with agents intiailised through agentframework
    # print(agents[i]) 

## To check the agents have access to other agents lists
# print("testing - item from agents' list: ")
# print(agents[0].agents[1])
 
## Going through each agent for each iteration and having them move and eat
# for j in range(num_of_iterations):
#     for i in range(num_of_agents):
#         agents[i].move()
#         agents[i].eat()
#         agents[i].share_with_neighbours(neighbourhood)
#         # print(agents[i])

# I have commented out above and now replacing with code below so I can create more loops
for j in range(num_of_iterations):
    random.shuffle(agents)# shuffle the list
    for i in range(num_of_agents):
        agents[i].move() # stops any agent moving before any other agent
    for i in range(num_of_agents):
        agents[i].eat()
    # for i in range(num_of_agents): # removing as not needed
        agents[i].share_with_neighbours(neighbourhood)

# Print agents' positions after moving
for i in range(num_of_agents):
    print("after moving ", agents[i])

## Plotting the agents' positions and the data
# matplotlib.pyplot.xlim(0, 99)
# matplotlib.pyplot.ylim(0, 99)
# matplotlib.pyplot.imshow(environment)
# for i in range(num_of_agents):
#     matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
# matplotlib.pyplot.show()
# removed the code above from the model as now just working with the animation

## Animation
# Set up figure for animation and define axes
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Turn autoscale off
ax.set_autoscale_on(False)

def update(frame_number):
    """
    Defines when the animation updates each frame

    Paramaters
    ----------
    frame_number: each new frame

    Returns
    ----------
    x and y coordinates to plot the moving agents frame by frame
    """
    fig.clear()

    for j in range(num_of_iterations):
        random.shuffle(agents)  # shuffle the list
        for i in range(num_of_agents):
            agents[i].move()  # stops any agent moving before any other agent
        for i in range(num_of_agents):
            agents[i].eat()
            # for i in range(num_of_agents): # removing as not needed
            agents[i].share_with_neighbours(neighbourhood)

    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)

# Initialise the animation
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)

# Show the animation
matplotlib.pyplot.show()

# Print the eaten environment to a new text file
f2 = open('out.txt', 'w')
for item in environment:
    f2.write(str(item))
f2.close()