"""
Final project

Agent-based Model
Author: Sophie Ray Morrison
Version: Final
"""
## Import relevant packages
import random
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
    environment.append(rowlist) # The environment list is populated with lists of each row, making the environment a list of lists
f.close()

## Initialise the agents and creating empty agent list
num_of_agents = 10 # Set number of agents
num_of_iterations = 100 # Set iterations
neighbourhood = 20 # Create neighborhood radius
agents = [] # Make empty agents list

## Populate the agents list with agents
for i in range(num_of_agents): # Loop through 'num_of_agents' from 0 to 9
    agents.append(agentframework.Agent(i, environment, agents)) # Populates agent list with agents intiailised through agentframework

# Create loops for agents to move, eat and share with neighbours
for j in range(num_of_iterations): # Runs processes below for defined number of iterations
    random.shuffle(agents)# Shuffles the list
    for i in range(num_of_agents):
        agents[i].move() # Stops any agent moving before any other agent
    for i in range(num_of_agents):
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

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
    frame_number: Each new frame
        Shuffles the agents; shows how they have moved and eaten; changes the environment

    Returns
    ----------
    Numbers
        Updated values for both agents and environment after agents have moved, eaten, shared with neighbours.
    """
    fig.clear()

    for j in range(num_of_iterations):
        random.shuffle(agents)  # Shuffles the agents' list
        for i in range(num_of_agents):
            agents[i].move()  # Stops any agent moving before any other agent
        for i in range(num_of_agents):
            agents[i].eat() # Calls the eat function
            agents[i].share_with_neighbours(neighbourhood) # Calls the share with neighbours function

    matplotlib.pyplot.xlim(0, 99) # Plots on x axis
    matplotlib.pyplot.ylim(0, 99) # Plots on y axis
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)

# Initialise the animation
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)

# Show the animation
matplotlib.pyplot.show()

# Print out the final eaten environment to a new text file (after the chosen number of iterations)
f2 = open('out.txt', 'w')
for item in environment: # Loop through each list in the environment
    for item1 in item: # Loop through each item in the list
        f2.write(str(int((item1)))) # Write the file and change values to integers
        f2.write(", ") # Add commas between values
f2.close()
