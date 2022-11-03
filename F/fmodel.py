"""
F Practical: I/O
Author: Sophie Ray Morrison
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

# # test: printing the uneaten environment for comparison later
# print("basic environment: ")
# print(environment[5])

# # test: all the rows having the same number of columns (is it rectangular)
# plot = True
# nrows = len(environment) # how many rows 
# print("nrows", nrows) 
# ncols = len(environment[0]) # set ncols to be number of columns in first row
# print("ncols", ncols)
# for i in range(1, nrows):
#     ncolsini = len(environment[i]) # gives us number of columns in the i'th row
#     if ncols != ncolsini:
#         print("error line", i, ", wrong number of columns, expecting", ncols, "received", ncolsini)
#         plot = False
# if plot: 
#     matplotlib.pyplot.imshow(environment)
#     matplotlib.pyplot.show()
    
# # change values
# for row in range(nrows):
#     for col in range(ncols):
#         value = environment[row][col]
#         # value2 = value * value #  shortening code
#         environment[row][col] = value * value
    
# # to test the value at a given row and column
# row = nrows-1 # test the very last row
# col = ncols-1 # test last col

# print(environment[row][col]) # i checked in the file and this was correct

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
# num_of_agents = 100000 # I maxed out the number of agents to  check the environment was being eaten
num_of_iterations = 1
agents = []

# populating the agents list with agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment))

# going through each agent for each iteration and having them move and eat
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()

# checking the environment is being eaten and printing out the values at one point in the environment
# print("eaten environment: ")
# print(environment[5])

# print(agents)
# for i in range(num_of_agents):
#    print(agents[i])

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

# print the eaten environment to a new text file
f2 = open('out.txt', 'w')
for item in environment:
    f2.write(str(item))
f2.close()