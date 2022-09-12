# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 10:55:41 2022

@author: gysmo
"""



import random
import operator
import matplotlib.pyplot

x0 = random.randint(0,99)
y0 = random.randint(0,99)

agents = []
agents.append([x0,y0])

# change y0
if random.random() < 0.5:
    agents[0][1] = agents[0][1] + 1
else:
    agents[0][1] = agents[0][1] - 1
    
# change x0
if random.random() < 0.5:
    agents[0][0] = agents[0][0] + 1
else:
    agents[0][0] = agents[0][0] - 1


x1 = random.randint(0,99)
y1 = random.randint(0,99)

# change y0
#if random.random() < 0.5:
#    agents[1][0] = agents[1][0] + 1
#else:
#    agents[1][0] = agents[1][0] - 1
    
# change x0
#if random.random() < 0.5:
#    agents[1][1] = agents[1][1] + 1
#else:
#    agents[1][1] = agents[1][1] - 1


print(agents)
print(agents[0])
print(agents[0][0])
print(agents[0][1])
# 
# 
# y1 = random.randint(0,99)
# x1 = random.randint(0,99)
# 
# change y1
# if random.random() > 0.5:
#     agents[1][0] = agents[1][0] + 1
# else:
#     y1 = y1 - 1
    
# change x1
# if random.random() < 0.5:
#     x1 = x1 - 1
# else:
#     x1 = x1 + 1
    


print(max(agents, key=operator.itemgetter(1)))

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
matplotlib.pyplot.show()