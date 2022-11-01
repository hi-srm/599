"""
practical: animation/behaviour
"""
# import relevant bits
import random
import operator
import matplotlib
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv
matplotlib.use('macosx')

# read the in.txt file
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

# reading in the data - removed as this is not useful  anymore - this was earlie test
# with open('in.txt') as csv_file: # open as csv
#     csv_reader = csv.reader(csv_file, delimiter=',') # telling it delimiter is a comma
#     line_count = 0 # set variable line count to 0
#     for row in csv_reader: # go through each row
#         if line_count == 0: # counting how many lines are in the file
#             # print(f'Column names are {", ".join(row)}')
#             line_count += 1 # each row adding 1 to line count number
#         else:
#             # print(f'\t{row[0]}{row[1]}{row[2]}.')
#             line_count += 1 # each row adding 1 to line count number
#     # print(f'Processed {line_count} lines.')

# initialising the agents and creating empty agent list
num_of_agents = 10 # set number of agents
num_of_iterations = 100 # set iterations
neighbourhood = 20 # create neighborhood
agents = [] # make empty agents list

# populating the agents list with agents
for i in range(num_of_agents): # loop through 'num_of_agents' from 0 to 9
    agents.append(agentframework.Agent(i, environment, agents)) # populatng agent list with agents intiailised through agentframework
    # print(agents[i]) 

## to check the agents have access to other agents lists
# print("testing - item from agents' list: ")
# print(agents[0].agents[1])
 
## going through each agent for each iteration and having them move and eat
# for j in range(num_of_iterations):
#     for i in range(num_of_agents):
#         agents[i].move()
#         agents[i].eat()
#         agents[i].share_with_neighbours(neighbourhood)
#         # print(agents[i])

# have commented out above and now replacing with code below so i can create more loops
for j in range(num_of_iterations):
    random.shuffle(agents)# shuffle the list
    for i in range(num_of_agents):
        agents[i].move() # stops any agent moving before any other agent
    for i in range(num_of_agents):
        agents[i].eat()
    # for i in range(num_of_agents): # removing as not needed
        agents[i].share_with_neighbours(neighbourhood)

print("after moving")
for i in range(num_of_agents):
    print(agents[i])

# # plotting the agents' positions and the data
# matplotlib.pyplot.xlim(0, 99)
# matplotlib.pyplot.ylim(0, 99)
# matplotlib.pyplot.imshow(environment)
# for i in range(num_of_agents):
#     matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
# matplotlib.pyplot.show()
# removed the code above from the model as now just working with the animation

## animation

# set up figure for animation and define axes
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# turn autoscale off
ax.set_autoscale_on(False)

def update(frame_number):
    """
    defines when the animation updates each frame

    paramaters
    frame_number: each new frame

    returns
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


animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)

matplotlib.pyplot.show()