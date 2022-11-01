"""
"""
# import relevant bits
import random
import operator
import matplotlib.pyplot
import agentframework
import csv

# read the in.txt file
f = open("in.txt")
csv_reader = csv.reader(f)
environment = []
for line in csv_reader:
    rowlist = []
    for value in line:
        # print (type(value)) - to test type that the value is, as it wasn't plotting
        rowlist.append((int(value))) # change value from string to int
    # print(rowlist)
    environment.append(rowlist)
f.close()

# reading in the data
with open('in.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # print(f'\t{row[0]}{row[1]}{row[2]}.')
            line_count += 1
    # print(f'Processed {line_count} lines.')

# initialising the agents and creating empty agent list
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20 # create neighborhood
agents = []

# populating the agents list with agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(i, environment, agents))
for i in range(num_of_agents):
    print(agents[i])

# to check the agents have access to other agents lists
# print("testing - item from agents' list: ")
# print(agents[0].agents[1])
 
# # going through each agent for each iteration and having them move and eat
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

# plotting the agents' positions and the data
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

# for agents_row_a in agents:
 #   for agents_row_b in agents:
  #      distance = distance_between(agents_row_a, agents_row_b)

# # print the eaten environment to a new text file
# f2 = open('out.txt', 'w')
# for item in environment:
#     f2.write(str(item))
# f2.close()